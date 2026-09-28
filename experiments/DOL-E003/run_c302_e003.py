#!/usr/bin/env python3
"""
DOL-E003 local runner.

Usage:
  python run_c302_e003.py /path/to/c302

The script never edits the c302 checkout. It creates derived ON/CUT/RESTORE
NeuroML files in a separate work directory and invokes pynml on the matching
LEMS file. Results are written under --work-dir.

Prerequisite:
  pynml (pyNeuroML) must be installed and Java must be available.

This runner intentionally refuses to declare a result if a simulation command
fails or output is missing.
"""
from __future__ import annotations
import argparse
import csv
import shutil
import subprocess
from pathlib import Path
import xml.etree.ElementTree as ET

PINNED = "6cd861f8ca4d3241ee9cf4627884caa930dab53c"
RELATION = ("AIZL", "ASHL")
NS = {"n": "http://www.neuroml.org/schema/neuroml2"}

def surgical_variant(src: Path, dst: Path, weight: str) -> None:
    tree = ET.parse(src)
    root = tree.getroot()
    found = 0
    for p in root.findall(".//n:electricalProjection", NS):
        pre = p.attrib.get("presynapticPopulation")
        post = p.attrib.get("postsynapticPopulation")
        if {pre, post} == set(RELATION):
            for c in p.findall("n:electricalConnectionInstanceW", NS):
                c.set("weight", weight)
                found += 1
    if found != 2:
        raise RuntimeError(f"Expected 2 AIZL<->ASHL electrical connections, found {found}")
    tree.write(dst, encoding="utf-8", xml_declaration=True)

def metric(path: Path) -> float:
    rows = list(csv.reader(path.open(newline="")))
    if len(rows) < 3:
        raise RuntimeError(f"Not enough output rows: {path}")
    # c302 output: time, AIZL, AS2, ASHL, ...
    data = [[float(x) for x in row] for row in rows[1:] if row]
    times = [r[0] for r in data]
    ash = [r[3] for r in data]
    base = [v for t, v in zip(times, ash) if 400 <= t < 500]
    if not base:
        raise RuntimeError("No 400-500 ms baseline samples")
    baseline = sum(base) / len(base)
    vals = [abs(v - baseline) for t, v in zip(times, ash) if 500 <= t <= 1300]
    return sum(vals) * 0.05

def run_one(pynml: str, lems: Path, cwd: Path) -> None:
    p = subprocess.run([pynml, lems.name], cwd=cwd, text=True,
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (cwd / (lems.stem + ".stdout.log")).write_text(p.stdout)
    if p.returncode != 0:
        raise RuntimeError(f"pynml failed for {lems.name}; see stdout log")

def main():
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

    # Keep required relative NeuroML includes together in the work directory.
    for rel in [
        "examples/Cells.xml", "examples/Networks.xml", "examples/Simulation.xml",
        "c302/cell_C.xml",
    ]:
        src_file = root / rel
        if not src_file.exists():
            raise SystemExit(f"Missing required dependency file: {src_file}")
        shutil.copy2(src_file, work / src_file.name)

    metrics = {}
    for name, weight in [("ON", "1.0"), ("CUT", "0.0"), ("RESTORE", "1.0")]:
        nml_name = f"c302_C1_Syns_{name}.net.nml"
        lems_name = f"LEMS_c302_C1_Syns_{name}.xml"
        nml = work / nml_name
        surgical_variant(src, nml, weight)

        lems = work / lems_name
        txt = lems_src.read_text()
        txt = txt.replace("c302_C1_Syns.net.nml", nml_name)
        txt = txt.replace("c302_C1_Syns.dat", f"c302_C1_Syns_{name}.dat")
        txt = txt.replace("c302_C1_Syns.activity.dat", f"c302_C1_Syns_{name}.activity.dat")
        lems.write_text(txt)

        run_one(args.pynml, lems, work)
        dat = work / f"c302_C1_Syns_{name}.dat"
        metrics[name] = metric(dat)

    metrics["CUT_OVER_ON"] = metrics["CUT"] / metrics["ON"]
    metrics["RESTORE_OVER_ON"] = metrics["RESTORE"] / metrics["ON"]
    decision = (
        "PASS"
        if metrics["CUT_OVER_ON"] <= 0.10
        and 0.90 <= metrics["RESTORE_OVER_ON"] <= 1.10
        else "FAIL"
    )
    metrics["DECISION"] = decision
    (work / "metrics.txt").write_text("\n".join(f"{k}={v}" for k,v in metrics.items()) + "\n")
    print(metrics)

if __name__ == "__main__":
    main()
