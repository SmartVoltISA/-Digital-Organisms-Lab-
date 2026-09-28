# DOL-E015 Run Log

- Preregistration fixed before execution.
- Execution: local Python.
- RNG seed: 15015.
- Held-out cases: 1000.

## FACT
Learned actuator gain = 0.5268610523963687.
Self-model action accuracy = 1.0.
Reactive accuracy = 0.5.
Damaged self-model accuracy = 0.0.
Oracle accuracy = 1.0.
Self-model advantage over reactive = 0.5.
Causal drop after replacing the learned gain with generic gain 1.0 = 1.0.
Prediction RMSE = 0.01914518588508577.

## CHECK
All preregistered criteria pass.

## RESULT
PASS.

## DECISION
The tested synthetic organism-specific self-model improves held-out action selection and the advantage disappears under the registered model-damage intervention.

## FIXATION
E015 is retained as an executed PASS. E013 and E014 remain unchanged.
