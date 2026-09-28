#!/usr/bin/env python3
"""
DOL-E003 strict local runner.

This runner never edits the pinned c302 checkout. It creates derived NeuroML/LEMS
variants in an isolated work directory and invokes pynml.

IMPORTANT:
The pinned c302 C1 Syns source contains multiple inputLists/stimuli. E003
requires an isolated AIZL primary perturbation and an isolated AS2 negative
control. Therefore this runner surgically keeps ONLY the requested stimulus
active in each run and removes all other inputList elements. This is a
pre-registered execution representation: no cell, channel, connection,
stimulus definition, integration setting, or initial condition is changed;
only activation of the already-existing inputList is controlled.

Usage:
  python run_c302_e003.py /path/to/c302 --pynml pynml

Prerequisite:
  pinned c302 checkout, Java, and pyNeuroML/pynml.

The runner refuses to emit a scientific PASS/FAIL if a required output,
intervention, or provenance check fails.
"""
from __future__ import annotations
import argparse, hashlib, json, shutil, subprocess, sys
from pathlib import Path
import xml.etree.ElementTree as ET

PINNED = "6cd861f8ca4d3241ee9cf4627884caa930dab53c"
RELATION = {"AIZL", "ASHL"}
NS = {"n": "http://www.neuroml.org/schema/neuroml2"}
BASELINE = (400.0, 500.0)
WINDOW = (500.0, 1300.0)
DT_MS = 0.05

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def surgical_variant(src: Path, dst: Path, weight: str, active_stimulus: str) -> dict:
    tree = ET.parse(src)
    root = tree.getroot()
    found = 0
    for p in root.findall(".//n:electricalProjection", NS):
        pre = p.attrib.get("presynapticPopulation")
        post = p.attrib.get("postsynapticPopulation")
        if {pre, post} == RELATION:
            for c in p.findall("n:electricalConnectionInstanceW", NS):
                c.set("weight", weight)
                found += 1
    if found != 2:
        raise RuntimeError(f"Expected 2 AIZL<->ASHL electrical connections, found {found}")

    # Isolate exactly one already-defined inputList; do not alter pulse definitions.
    net = root.find(".//n:network", NS)
    if net is None:
        raise RuntimeError("No network element found")
    input_lists = net.findall("n:inputList", NS)
    available = sorted({x.attrib.get("component") for x in input_lists if x.attrib.get("component")})
    expected = {"stim_AIZL_1", "stim_AS2_1"}
    if not expected.issubset(set(available)):
        raise RuntimeError(f"Required existing stimuli missing; found={available}")
    kept = 0
    for il in list(input_lists):
        if il.attrib.get("component") == active_stimulus:
            kept += 1
        else:
            net.remove(il)
    if kept != 1:
        raise RuntimeError(f"Expected exactly one active {active_stimulus} inputList, kept={kept}")

    tree.write(dst, encoding="utf-8", xml_declaration=True)
    return {
        "relation_connections_modified": found,
        "active_stimulus": active_stimulus,
        "source_sha256": sha256(src),
        "derived_sha256": sha256(dst),
    }

def metric(path: Path) -> float:
    lines = [line.strip() for line in path.read_text().splitlines() if line.strip()]
    if len(lines) < 3:
        raise RuntimeError(f"Not enough output rows: {path}")
    data = [[float(x) for x in line.split()] for line in lines[1:]]
    times = [r[0] for r in data]
    ash = [r[3] for r in data]
    base = [v for t, v in zip(times, ash) if BASELINE[0] <= t < BASELINE[1]]
    if not base:
        raise RuntimeError("No 400-500 ms baseline samples")
    baseline = sum(base) / len(base)
    vals = [abs(v - baseline) for t, v in zip(times, ash) if WINDOW[0] <= t <= WINDOW[1]]
    return sum(vals) * DT_MS

def run_one(pynml: str, lems: Path, cwd: Path) -> None:
    p = subprocess.run([pynml, lems.name], cwd=cwd, text=True,
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (cwd / (lems.stem + ".stdout.log")).write_text(p.stdout)
    if p.returncode != 0:
        raise RuntimeError(f"pynml failed for {lems.name}; see stdout log")

def stage_dependencies(root: Path, work: Path) -> None:
    # Preserve c302's relative include structure.
    for rel in ["examples/Cells.xml", "examples/Networks.xml",
                "examples/Simulation.xml", "c302/cell_C.xml"]:
        src = root / rel
        if not src.exists():
            raise SystemExit(f"Missing required dependency file: {src}")
    (work / "examples").mkdir(parents=True, exist_ok=True)
    (work / "c302").mkdir(parents=True, exist_ok=True)
    for rel in ["examples/Cells.xml", "examples/Networks.xml", "examples/Simulation.xml",
                "c302/cell_C.xml"]:
        shutil.copy2(root / rel, work / rel)

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("c302_root", type=Path)
    ap.add_argument("--work-dir", type=Path, default=Path("dol_e003_run"))
    ap.add_argument("--pynml", default="pynml")
    args = ap.parse_args()

    root = args.c302_root.resolve()
    src = root / "examples/c302_C1_Syns.net.nml"
    lems_src = root / "examples/LEMS_c302_C1_Syns.xml"
    if not src.exists() or not lems_src.exists():
        raise SystemExit("Pinned c302 C1 Syns files not found")
    head = subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()
    if head != PINNED:
        raise SystemExit(f"Wrong c302 checkout: expected {PINNED}, got {head}")

    work = args.work_dir.resolve()
    work.mkdir(parents=True, exist_ok=True)
    stage_dependencies(root, work)

    source_sha = sha256(src)
    provenance = {
        "c302_commit": head,
        "source_file": str(src),
        "source_sha256": source_sha,
        "python": sys.version,
        "platform": sys.platform,
        "pynml": args.pynml,
        "conditions": {}
    }

    metrics = {}
    # ON and CUT use the isolated AIZL perturbation. Sham repeats ON.
    runs = [
        ("ON", "1.0", "stim_AIZL_1"),
        ("CUT", "0.0", "stim_AIZL_1"),
        ("RESTORE", "1.0", "stim_AIZL_1"),
        ("SHAM", "1.0", "stim_AIZL_1"),
        ("NEGCTRL_AS2", "1.0", "stim_AS2_1"),
    ]

    for name, weight, stim in runs:
        nml_name = f"c302_C1_Syns_{name}.net.nml"
        lems_name = f"LEMS_c302_C1_Syns_{name}.xml"
        nml = work / "examples" / nml_name
        surgical_variant(src, nml, weight, stim)

        lems = work / "examples" / lems_name
        txt = lems_src.read_text()
        txt = txt.replace("c302_C1_Syns.net.nml", nml_name)
        for old in ["c302_C1_Syns.dat", "c302_C1_Syns.activity.dat",
                    "c302_C1_Syns.muscles.dat", "c302_C1_Syns.muscles.activity.dat"]:
            txt = txt.replace(old, old.replace("c302_C1_Syns", f"c302_C1_Syns_{name}"))
        lems.write_text(txt)

        run_one(args.pynml, lems, work / "examples")
        dat = work / "examples" / f"c302_C1_Syns_{name}.dat"
        metrics[name] = metric(dat)
        provenance["conditions"][name] = {
            "weight": weight,
            "active_stimulus": stim,
            "nml_sha256": sha256(nml),
            "lems_sha256": sha256(lems),
            "output_sha256": sha256(dat),
        }

    metrics["CUT_OVER_ON"] = metrics["CUT"] / metrics["ON"]
    metrics["RESTORE_OVER_ON"] = metrics["RESTORE"] / metrics["ON"]
    metrics["NEGCTRL_RATIO"] = metrics["ON"] / max(metrics["NEGCTRL_AS2"], 1e-15)
    metrics["SHAM_REL_DIFF"] = abs(metrics["SHAM"] - metrics["ON"]) / max(abs(metrics["ON"]), 1e-15)
    # Numerical tolerance is deliberately explicit and only checks pipeline invariance.
    sham_tol = 1e-9
    metrics["DECISION"] = (
        "PASS"
        if metrics["CUT_OVER_ON"] <= 0.10
        and 0.90 <= metrics["RESTORE_OVER_ON"] <= 1.10
        and metrics["NEGCTRL_RATIO"] > 3
        and metrics["SHAM_REL_DIFF"] <= sham_tol
        else "FAIL"
    )
    (work / "metrics.json").write_text(json.dumps(metrics, indent=2) + "\n")
    (work / "provenance.json").write_text(json.dumps(provenance, indent=2) + "\n")
    print(json.dumps(metrics, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
