# DOL-E001 — Complexity Ladder / Cross-Model Comparison

## Status

PREREGISTRATION / PROTOCOL ONLY.

No result is claimed by this document.

## Purpose

Establish the first common experimental frame for comparing systems at different organizational levels.

## Systems

### External baseline

**c302 / C. elegans**

Role: independent biological computational baseline.

No connection to SPACE.

### Abstract research baselines

- Ω experimental models;
- RELATION-LAB models.

Role: controlled synthetic systems in which relations and interventions can be precisely manipulated.

### Digital Organisms Lab

- DOL-E000 minimal organism;
- future C. elegans adapter;
- future adaptive/memory/planning models.

### SPACE

Not included in execution by default.

A SPACE experiment requires a separate preregistration and must enter only through the external experiment interface.

## Primary hypothesis

Increasing organizational layers can introduce experimentally distinguishable behavioral properties that are not present, or are not detectable, at lower layers.

## Null hypothesis

Observed differences can be explained by differences in substrate, parameters, task implementation, or measurement rather than by the proposed organizational layer.

## First target

C2 — relation ablation/restoration.

Canonical operation:

`ON → CUT → RESTORE`

Primary observable:

change in cross-component influence.

Secondary observables:
- response latency;
- response magnitude;
- recovery;
- stability;
- collateral effects.

## Second target

C3/C4 — adaptation and memory.

Required distinction:

`persistent internal state affecting future response`

versus

`temporary dynamical after-effect`

## Third target

C5/C6 — planning and reasoning.

These are not inferred from complex trajectories.

They require controlled tasks with alternative actions and withheld/counterfactual cases.

## Decision rule

Do not assign a higher complexity level from architecture alone.

A level is recorded only when the corresponding preregistered behavioral criterion is met.

## Expected first implementation

1. Formalize common intervention vocabulary.
2. Build adapters where technically possible.
3. Run DOL-E000 regression.
4. Implement synthetic C2 test first.
5. Map the same intervention to c302 only after confirming that the required c302 manipulation is technically valid.
6. Compare measured properties.
7. Only then move upward to adaptation and memory.

## Explicit non-goals

- connecting c302 to SPACE;
- claiming that c302 is a complete digital worm;
- claiming that SPACE is already a digital mind;
- claiming that Ω explains biology;
- ranking systems;
- replacing biological validation with architectural analogy.
