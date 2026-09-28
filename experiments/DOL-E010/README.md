# DOL-E010 — Synthetic future-dependent planning, corrected timing

## Status
**EXECUTED — PASS**

## Complexity target
**L6 — Planning**

## Relation to DOL-E009
E009 is retained as INCONCLUSIVE because its preregistered horizon was internally inconsistent with its registered GOAL reward timing. E010 is a new experiment, not a correction of E009.

## Operational definition
L6 requires a future-dependent action sequence to outperform a matched myopic control.

## Core design
At START:
- A gives +1 immediately but enters TRAP;
- B gives 0 immediately but enters PATH;
- from PATH, B reaches GOAL;
- at GOAL, the next action gives +4.

With a registered horizon of 4, the planning route B → B → A/B/WAIT reaches GOAL and collects +4. The myopic controller prefers A at START because +1 > 0.

## Controls
- matched myopic controller;
- random controller;
- counterfactual first-action comparison;
- identical environment and horizon.

## Criteria
PASS requires:
- planning mean return >= 4.0;
- planning advantage over myopic >= 3.0;
- planning selects B at START in >=95% episodes;
- myopic selects B at START in <=5%;
- planning reaches GOAL in >=95%.

## Interpretation
A PASS establishes the tested synthetic future-dependent action-selection property only. It does not establish general planning, reasoning, intelligence, cognition, self-model, biological equivalence, or universality.

FACT → CHECK → RESULT → DECISION → FIXATION.
