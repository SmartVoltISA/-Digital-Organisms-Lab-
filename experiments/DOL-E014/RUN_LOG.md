# DOL-E014 Run Log

- Preregistration fixed before execution.
- Execution: local Python.
- RNG seed: 14014.
- Held-out steps: 30,000.

## FACT
Intact self-model reward = -0.6677068415692811.
Reactive reward = -0.8128309313310007.
Damaged self-model reward = -0.32472722003927545.
Oracle reward = -0.4340073204450382.
Prediction RMSE = 0.4027319156580134.
Self-model gap = 0.14512408976171964.
Causal drop = -0.3429796215300056.

## CHECK
The self-model advantage, prediction RMSE, and causal-drop criteria all fail. The damaged model unexpectedly performs better.

## RESULT
FAIL.

## DECISION
E014 does not establish L8.

## FIXATION
E014 remains FAIL. No parameters or thresholds were changed after execution.
