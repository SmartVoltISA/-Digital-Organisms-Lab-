# DOL-E013 Run Log

- Preregistration fixed before execution.
- Execution: local Python.
- RNG seed: 13013.
- Held-out episodes: 1000.
- Held-out steps: 20,000 total.

## FACT
Self-model mean reward = -0.14732180472911047.
Reactive mean reward = -0.19103861714009193.
Self-model gap = 0.04371681241098146.
Prediction RMSE = 0.04997831274435184.
Oracle mean reward = -0.13125000000000003.
Oracle gap = 0.01607180472911044.

## CHECK
Prediction and oracle-distance criteria pass, but the preregistered self-model advantage threshold of 0.20 is not met.

## RESULT
FAIL.

## DECISION
The experiment does not establish L8. The learned self-dynamics model predicts accurately and controls reasonably, but the registered evidence for improvement over the reactive baseline is insufficient.

## FIXATION
E013 remains FAIL. No thresholds or parameters were changed after execution. E012 remains an unexecuted method-check failure.
