# DOL-E003 Run Log

## Preflight — 2026-09-28

- c302 pinned commit: `6cd861f8ca4d3241ee9cf4627884caa930dab53c`
- Reference model: `examples/c302_C1_Syns.net.nml`
- Java detected: OpenJDK 21.0.11
- Python detected: 3.13.5
- `pynml`: NOT INSTALLED
- `pyneuroml`: NOT INSTALLED
- Direct git access to GitHub from the execution environment: FAILED (DNS/network unavailable)
- Simulation: **NOT RUN**
- Decision: **INCONCLUSIVE / NOT RUN**, not FAIL

The experiment must not be marked PASS until ON/CUT/RESTORE are actually simulated and the preregistered metrics are computed.


## Runner hardening — 2026-09-28

Pre-execution audit found that the pinned c302 C1 Syns source contains multiple pre-defined inputList elements. The previous runner did not isolate the selected AIZL/AS2 perturbation, so it could not satisfy the intended paired intervention protocol.

The runner was therefore replaced with a strict version that:

- verifies the pinned c302 commit;
- records source and derived SHA-256 hashes;
- keeps only the requested existing inputList active in each derived condition;
- executes ON, CUT, RESTORE, SHAM and AS2 negative-control conditions;
- preserves the original stimulus definitions;
- preserves all non-target model parameters and connections;
- refuses to emit a scientific result when required outputs are missing.

This is a **pre-execution infrastructure correction**. No scientific result is claimed and no preregistered threshold was changed.

Current state remains: **NOT RUN**.
