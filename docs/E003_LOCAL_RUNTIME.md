# DOL-E003 — local runtime setup

## Purpose

Prepare a local machine to execute the already-preregistered c302 E003 experiment.

The canonical c302 checkout must remain untouched. DOL creates derived experiment files in a separate work directory.

## Pinned model

- Repository: openworm/c302
- Commit: `6cd861f8ca4d3241ee9cf4627884caa930dab53c`
- Model: `examples/c302_C1_Syns.net.nml`
- LEMS: `examples/LEMS_c302_C1_Syns.xml`

## Recommended environment

Use a dedicated virtual environment.

For Windows, c302 currently documents Python 3.10 for its dependency stack. Do not replace the DOL E003 preregistration with a different Python version merely to make installation easier.

### Windows / PowerShell

~~~powershell
py -3.10 -m venv .venv-c302
.\.venv-c302\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install pyneuroml
python -m pip install .
~~~

The final `pip install .` is run from the pinned c302 checkout.

Verify:

~~~powershell
java -version
python --version
pynml -h
git -C C:\path\to\c302 rev-parse HEAD
~~~

The last command must print:

`6cd861f8ca4d3241ee9cf4627884caa930dab53c`

### Linux

~~~bash
python3.10 -m venv .venv-c302
source .venv-c302/bin/activate
python -m pip install --upgrade pip
python -m pip install pyneuroml
python -m pip install .
~~~

Verify:

~~~bash
java -version
python --version
pynml -h
git -C /path/to/c302 rev-parse HEAD
~~~

For Linux, c302 also documents OpenJDK and Graphviz as dependencies for its examples.

## Get the pinned c302 checkout

~~~bash
git clone https://github.com/openworm/c302.git
cd c302
git checkout 6cd861f8ca4d3241ee9cf4627884caa930dab53c
git rev-parse HEAD
~~~

Do not edit files inside this checkout.

## Execute DOL-E003

From the DOL repository:

~~~bash
python experiments/DOL-E003/run_c302_e003.py /path/to/c302 --work-dir experiments/DOL-E003/dol_e003_run
~~~

The runner performs:

1. pinned-commit verification;
2. source SHA-256 capture;
3. derived ON condition with only `stim_AIZL_1` active;
4. CUT condition with the same isolated AIZL perturbation;
5. RESTORE condition;
6. SHAM ON repeat;
7. AS2 negative-control run with only `stim_AS2_1` active;
8. metric calculation;
9. provenance and output SHA-256 capture.

The pinned source contains multiple pre-defined input lists. The runner removes the other input-list activations from each derived experiment while retaining the original stimulus definitions. This prevents unrelated simultaneous stimuli from contaminating the intervention comparison.

## Expected artifacts

After a successful simulation:

- `dol_e003_run/examples/*.net.nml`
- `dol_e003_run/examples/*.xml`
- `dol_e003_run/examples/*.dat`
- stdout logs
- `metrics.json`
- `provenance.json`

A scientific PASS is valid only when the actual simulator outputs exist and all preregistered criteria pass.

If installation or simulation fails, record the exact error and keep the experiment NOT RUN/INCONCLUSIVE. Never convert an environment failure into FAIL.

## Documentation source

c302 documents pyNeuroML/jNeuroML as its simulation path. NeuroML documentation recommends installing pyNeuroML in a virtual environment with `pip install pyneuroml`.
