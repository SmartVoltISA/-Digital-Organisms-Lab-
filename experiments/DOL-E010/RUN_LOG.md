# DOL-E010 Run Log

- Preregistration commit: E010 config/README commit created before execution
- Execution: local Python
- RNG seed: 9010
- Episodes: 1000
- Horizon: 4

## FACT
Planning mean return = 8.0.
Myopic mean return = 1.0.
Random mean return = 1.729.
Planning gap = 7.0.
Planning B-at-START fraction = 1.0.
Myopic B-at-START fraction = 0.0.
Planning GOAL fraction = 1.0.

## CHECK
All preregistered criteria pass.

The planning policy must sacrifice the immediate +1 at START to enter PATH, then reach GOAL and collect future reward. The matched myopic policy selects A because A has the highest immediate reward.

## RESULT
PASS.

## DECISION
The tested synthetic system demonstrates the registered future-dependent action-sequence property against a matched myopic control.

## FIXATION
E010 is retained as an executed PASS. E009 remains INCONCLUSIVE and unchanged.
