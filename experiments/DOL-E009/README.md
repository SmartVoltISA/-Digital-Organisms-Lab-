# DOL-E009 — Synthetic future-dependent planning

## Status
**EXECUTED — INCONCLUSIVE**

## Complexity target
**L6 — Planning**

## Operational definition
L6 requires a future-dependent action sequence to outperform a matched myopic control.

## Core design
The environment creates a deliberate conflict between immediate and future value.

At START:
- action A gives immediate reward +1 but enters TRAP, where the goal cannot be reached within the horizon;
- action B gives immediate reward 0 but enters PATH;
- from PATH, B reaches GOAL;
- GOAL gives +4.

Therefore:
- a myopic controller prefers A because +1 > 0 immediately;
- a planning controller must choose B because its future return is 4.

The task is deterministic so the distinction is about temporal evaluation, not noise exploitation.

## Registered horizon
3 actions/steps from START. Discount = 1.

## Controls
- matched myopic controller;
- random controller;
- counterfactual first-action comparison;
- same environment and horizon.

## Criteria
PASS requires:
- planning mean return >= 4.0;
- planning advantage over myopic >= 3.0;
- planning selects B at START in >=95% episodes;
- myopic selects B in <=5%;
- planning reaches GOAL in >=95%.

## Interpretation
A PASS establishes the tested synthetic future-dependent action-selection property.

It does not establish general planning, reasoning, intelligence, cognition, self-model, consciousness, biological equivalence, or universality.

FACT → CHECK → RESULT → DECISION → FIXATION.
