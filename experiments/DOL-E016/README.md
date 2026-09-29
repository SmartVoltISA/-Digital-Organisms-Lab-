# DOL-E016 — Minimum Organism Description (MOD)

## Status
PREREGISTERED — NOT RUN

## Purpose
Measure the minimum description required to preserve a predefined observable capability profile of one digital organism model.

E016 is an orthogonal complexity experiment. It does not create L9 and does not rank organisms.

## Core question
How far can the executable description of a fixed organism model be reduced while the model continues to satisfy the same preregistered behavioral criteria?

## Important distinction
E016 separates:
1. artifact size — bytes of files;
2. executable description length — canonical model/configuration representation;
3. runtime state size — number/precision of state variables;
4. behavioral preservation — whether the registered tests still pass.

Raw repository size, comments, formatting, dependencies, caches, and generated outputs are not organism complexity.

## Pilot target
DOL-E004 synthetic L3 adaptation model.

The pilot uses E004's locked equations, schedule, seeds, and criteria as the behavioral preservation target. E004 itself is not modified.

## Hypothesis
H0: reducing the executable description does not produce a measurable monotonic loss of the registered capability until a boundary is crossed.

H1: there is a measurable description-length boundary below which the registered capability fails.

## Null-control principle
A size reduction is valid only if it changes the declared model representation. Deleting comments, whitespace, filenames, or packaging metadata alone is not counted as biological/model compression.

## Canonical description
For E016, the model description is a normalized manifest containing:
- state variables;
- transition equations/rules;
- parameters;
- output rule;
- environment interface;
- initial conditions;
- random/noise specification.

The manifest is serialized deterministically before byte counting.

## Compression operators
The pilot tests independent, explicitly declared operators:
- parameter quantization;
- removal of numerically inactive precision;
- equation/rule simplification where the resulting rule is explicitly recorded;
- state-variable elimination only when the reduced model remains executable;
- relation removal only where a relation is explicitly declared removable.

No operator may be chosen after seeing the behavioral result.

## Behavioral equivalence
Each compressed candidate must run the complete E004 behavioral protocol:
- baseline;
- training;
- washout;
- probe;
- reversal;
- post-reversal probe;
- no-training control;
- 100 registered seeds.

The candidate passes preservation only if all original E004 decision criteria remain satisfied.

## Description metrics
Report at minimum:
- canonical manifest bytes;
- UTF-8 normalized description bytes;
- number of state variables;
- number of parameters;
- number of transition terms;
- runtime peak state count;
- execution time separately.

Do not combine these into a single score in the pilot.

## Search protocol
Start from the locked E004 model M0. Generate a preregistered sequence of candidate representations M1...Mn.

For each candidate:
1. construct it without observing candidate results;
2. hash the candidate;
3. run the full E004 protocol;
4. record FACT → CHECK → RESULT → DECISION → FIXATION.

The first candidate that fails is not automatically the minimum. Search continues below it to characterize the boundary.

## Controls
- M0 identity control: exact E004 model must reproduce the E004 result;
- serialization control: equivalent formatting must not change the canonical description size;
- sham compression: packaging-only reduction must not be interpreted as model reduction;
- fixed seed set;
- fixed environment and schedule;
- locked candidate sequence;
- no post-result parameter tuning.

## Decision
E016 reports a preservation boundary, not a biological complexity ranking.

For a capability C:
L*(C) = minimum measured description length among tested candidates that satisfy all preregistered criteria for C.

If the tested sequence does not bracket a failure boundary, report the result as unresolved rather than extrapolating.

## Scope
The pilot establishes the measurement method on one synthetic organism. It does not estimate the minimum description of a worm, fly, frog, bird, cat, pig, or human.

Cross-organism comparison is a later experiment and requires independently pinned models plus a common behavioral test suite.

## Interpretation
A smaller description is not automatically a better organism. A failed compression is evidence only about the tested representation and criterion.

FACT → CHECK → RESULT → DECISION → FIXATION.
