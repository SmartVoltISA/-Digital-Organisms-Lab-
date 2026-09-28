# Cross-Model Comparison Protocol v1.0

## Purpose
Compare independent digital organisms or dynamical models without requiring them to share an implementation, ontology, or internal representation.

Primary question:

> Which observable properties depend on a specific architecture, and which can arise from more general dynamical rules?

## Separation
The compared systems remain independent.
- c302 remains an external biological computational model.
- Ω/RELATION models remain research models.
- DOL supplies the comparison protocol and adapter layer.
- SPACE is outside this experiment and is not modified or treated as a control.

## Comparison dimensions
1. State variables / observable state.
2. Relation representation.
3. Relation dynamics.
4. Perturbation interface.
5. Ablation operation.
6. Restoration operation.
7. Response observable.
8. Recovery/stability.
9. Adaptation.
10. Memory.
11. Goal-directed behavior.
12. Planning/reasoning, when independently operationalized.
13. Provenance and reproducibility.

## Core relation test
RELATION ON → PERTURB → RESPONSE
RELATION CUT → PERTURB → RESPONSE
RELATION RESTORE → PERTURB → RESPONSE

The same perturbation is used where technically valid. If the substrate requires different physical intervention mechanisms, the difference is documented rather than hidden.

## Required controls
- no-intervention control;
- source/target permutation where meaningful;
- relation-cut control;
- restoration control;
- perturbation magnitude series;
- independent seeds or matched stochastic trajectories;
- sham intervention where possible;
- model/version hash;
- fixed configuration before execution.

## Primary quantities
For each system report:
- baseline response;
- ON response;
- CUT response;
- RESTORE response;
- negative-control response;
- suppression ratio;
- recovery ratio;
- effect size;
- uncertainty across runs.

Do not compare raw numerical magnitudes across incompatible units without normalization.

## Decision logic
A system may receive:
- PASS — operational criterion met;
- FAIL — operational criterion not met;
- INCONCLUSIVE — execution or measurement cannot distinguish hypotheses.

Never convert these into a ranking between systems.

## Interpretation
A shared ON → CUT → RESTORE signature across independent substrates supports a statement about a shared observable property of the tested systems.

It does not by itself establish:
- a universal physical law;
- a common ontology;
- identical mechanisms;
- biological equivalence;
- intelligence;
- cognition.

## c302-specific requirement
Before execution, identify one existing reversible relation in the chosen c302 model, record the exact NeuroML projection and parameter source, and define the cut operation without changing unrelated model parameters.

The preferred first candidate is an existing electrical or graded synaptic projection for which the simulator can produce matched control and intervention runs.

## Provenance
Every completed comparison must retain:

FACT → CHECK → RESULT → DECISION → FIXATION

External model files are never silently edited into the comparison result.
