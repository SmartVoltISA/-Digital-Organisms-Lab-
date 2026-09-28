# Cross-Model Comparison Protocol v1.0

## Purpose

Compare systems of different internal architecture without pretending that their internal mechanisms are identical.

The protocol is designed for:
- c302 / C. elegans;
- Ω/RELATION synthetic systems;
- future Digital Organism models;
- future SPACE experiments, only if separately preregistered.

## Non-negotiable boundary

c302 is an independent comparison object.

No c302 code, model, state, or dependency is imported into SPACE.

SPACE is not altered to accommodate c302.

## Comparison unit

The unit of comparison is not "organism".

It is:

`task + intervention + observable + control`

Example:

`relation ablation → target response → recovery after restoration`

## Common dimensions

Every participating system is described using:

| Dimension | Question |
|---|---|
| Substrate | What variables actually evolve? |
| Components | What are the interacting units? |
| Relations | How is influence represented? |
| Dynamics | How do states change over time? |
| Environment | What external variables exist? |
| Feedback | Which loops close the system? |
| Perturbation | What can be changed experimentally? |
| Ablation | Can a relation/component be removed? |
| Restoration | Can the removed element be restored? |
| Memory | Does history alter later response? |
| Goal | Is there a measurable target state? |
| Planning | Are action sequences selected for future consequences? |
| Reasoning | Are novel combinations/counterfactuals solved? |
| Self-model | Does an internal model of self affect behavior? |

## Experimental ladder

### C0 — Baseline reproducibility

Same model + same configuration + same seed.

Measure:
- state trajectory;
- final state;
- run-to-run variance.

### C1 — Perturbation response

Apply a fixed local perturbation.

Measure:
- response magnitude;
- latency;
- spatial/component spread;
- recovery.

### C2 — Relation ablation

`relation ON → CUT → RESTORE`

Compare:
1. intact;
2. relation removed;
3. relation restored.

The critical quantity is the **change in influence**, not the absolute response.

### C3 — Adaptive response

Repeat a controlled stimulus after a defined history.

Compare:
- naïve state;
- exposed state;
- washout/control state.

### C4 — Memory

Remove the original stimulus, wait a fixed interval, then probe.

A positive result requires a reproducible history-dependent difference.

### C5 — Goal/planning

Provide at least two action paths with different future consequences.

Measure whether action selection depends on the future objective rather than only the current stimulus.

### C6 — Reasoning / transfer

Train/expose on one structural configuration.

Test an unseen configuration sharing the relevant relation but not the surface form.

### C7 — Self-model intervention

Perturb the system's internal self-representation or uncertainty estimate.

Measure whether behavior changes specifically through that representation.

## Controls

Every experiment should specify, where applicable:
- no-intervention control;
- sham intervention;
- source permutation;
- time shuffle;
- independent seed;
- magnitude controls;
- negative relation control;
- alternative mechanism control.

## Cross-model rule

If two systems produce the same observable property under equivalent task/intervention definitions, record:

**"same observed property under the tested conditions."**

Do NOT record:

**"same mechanism."**

Mechanistic equivalence requires an additional experiment.

## Result classes

- PASS — preregistered criterion met.
- FAIL — preregistered criterion not met.
- INCONCLUSIVE — measurement/control insufficient.
- NOT APPLICABLE — the intervention cannot be defined for that system.
- NOT IMPLEMENTED — adapter/model capability absent.

"NOT APPLICABLE" is not a failure of the organism; it means the common operation cannot be mapped without changing the model.

## Provenance

Each result must contain:
- HYP-ID;
- system/model and version;
- adapter version;
- configuration;
- seed(s);
- intervention definition;
- metrics;
- controls;
- raw result location;
- execution environment;
- decision.

## Interpretation rule

A result at L4-L7 does not retroactively prove that lower-level systems possess the same property.

Likewise, failure at a higher level does not invalidate lower-level results.

The ladder is cumulative only where the experiment explicitly establishes the dependency.

## Core research question

> Which additional organizational mechanisms are necessary to move from reactive behavior toward memory, goal-directed behavior, planning, reasoning, and self-modeling?
