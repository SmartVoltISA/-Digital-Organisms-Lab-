# DOL-E003 — c302 reversible relation ablation

## Status

**PREREGISTERED — NOT RUN**

This experiment is the first DOL cross-model test using an external biological computational model.

c302 is treated as an independent comparison/control object. It is **not connected to SPACE** and the canonical c302 repository is never modified.

## Question

Does an existing reversible electrical relation in the c302 C1 model produce a measurable target response under perturbation, disappear when that relation is cut, and recover when the exact relation is restored?

## Hypothesis

For the existing bidirectional electrical coupling AIZL <-> ASHL:

- ON + perturb AIZL -> measurable response in ASHL.
- CUT + same perturbation -> strong suppression of the ASHL response.
- RESTORE + same perturbation -> recovery toward ON.
- A perturbation of an unrelated source (AS2) should not produce the same target response in ASHL.

This is a model-level intervention hypothesis. It does **not** claim biological equivalence, universal relational laws, or that c302 is a complete model of the animal.

## Fixed external reference

Repository: https://github.com/openworm/c302
Pinned commit: `6cd861f8ca4d3241ee9cf4627884caa930dab53c`
Reference file: `examples/c302_C1_Syns.net.nml`

The pinned file identifies c302 version 0.12.0 and contains:

- AIZL and ASHL populations.
- `neuron_to_neuron_elec_syn` with conductance `0.00052 nS`.
- AIZL -> ASHL electrical projection.
- ASHL -> AIZL electrical projection.
- Existing AIZL 1 pA stimulus from 500 ms to 1300 ms.
- Recommended duration 3600 ms.
- Recommended timestep 0.05 ms.

The source model remains immutable. Experiment variants are derived copies with a logged surgical diff.

## Relation under test

Relation unit:

`AIZL <-> ASHL`

Intervention:

- **ON:** both electrical projection weights = 1.0.
- **CUT:** both electrical projection weights = 0.0.
- **RESTORE:** both electrical projection weights = 1.0.

No other connection, cell parameter, stimulus, integration setting, or initial condition may change.

If the selected simulator rejects a zero electrical-connection weight, the run is **INCONCLUSIVE** until an equivalent pre-registered surgical representation is validated. Do not silently substitute a different intervention.

## Perturbation

Primary perturbation: use the already present `stim_AIZL_1` input:

- source: AIZL
- amplitude: 1 pA
- delay: 500 ms
- duration: 800 ms

Negative-control perturbation: use the already present `stim_AS2_1` input with identical timing and amplitude.

No new stimulus is introduced for the primary experiment.

## Observables

Primary target observable:

- ASHL membrane potential over the 500–1300 ms stimulation window.

Primary effect quantity:

`E = integral(abs(V_ASHL(t) - V_ASHL_pre(t))) dt`

where `V_ASHL_pre` is the mean ASHL membrane potential over a fixed pre-stimulus baseline window immediately preceding the perturbation.

The same time window, baseline definition, timestep, simulator, and output sampling must be used for ON, CUT, and RESTORE.

Secondary observables:

- AIZL membrane potential.
- ASHL peak absolute deviation from pre-stimulus baseline.
- ON/CUT/RESTORE trajectory differences.
- Negative-control AS2 -> ASHL effect.

Raw membrane-potential units are retained. Cross-model comparison uses normalized within-model effect ratios, not raw voltage magnitudes.

## Controls

Required:

1. ON condition.
2. CUT condition.
3. RESTORE condition.
4. Negative-control source AS2 -> ASHL.
5. Sham control: duplicate ON run with no surgical change.
6. Exact same external stimuli and simulation settings across paired conditions.

Because the model is deterministic unless stochasticity is explicitly introduced, stochastic seeds are not required. If the selected simulator introduces stochasticity, the simulator seed must be fixed and recorded.

## Decision criteria

The experiment is PASS only if all primary criteria are satisfied:

1. **CUT suppression:** `E_CUT / E_ON <= 0.10`.
2. **RESTORE recovery:** `0.90 <= E_RESTORE / E_ON <= 1.10`.
3. **Negative control:** `E_ON(AIZL -> ASHL) / max(E_ON(AS2 -> ASHL), epsilon) > 3`.
4. **Sham invariance:** ON replicate and sham ON must agree within the pre-registered numerical tolerance of the simulator/output pipeline.

If any required criterion cannot be evaluated because the simulator, output recording, or intervention representation is invalid, decision = **INCONCLUSIVE**, not FAIL.

## Required provenance

Record:

- c302 commit SHA.
- exact source file SHA.
- simulator and version.
- Python version.
- pyNeuroML/jNeuroML/NEURON versions if used.
- operating system.
- exact derived-file diff for ON/CUT/RESTORE.
- command line.
- full stdout/stderr or equivalent run log.
- output files.
- metrics.
- final decision.

## Integrity rule

Do not edit the canonical c302 source.

Do not change parameters after inspecting the result and still call the run the preregistered experiment.

Do not claim PASS until all required runs are actually executed and the metrics are computed from recorded output.

## Current execution state

**NOT RUN.**

The present execution environment has Java and git, but does not have `pynml`, and direct network access from the execution environment is unavailable. Therefore no c302 simulation result is claimed here.

## Scope of interpretation

A PASS would establish only that this specified c302 model exhibits the tested reversible intervention-response property under the specified protocol.

It would not establish:

- a universal law of nature;
- biological equivalence between c302 and a living C. elegans;
- a common mechanism with Ω/RELATION-LAB;
- cognition, intelligence, planning, or memory;
- that all relations in c302 behave the same way.

The result is intended for the DOL cross-model comparison protocol.
