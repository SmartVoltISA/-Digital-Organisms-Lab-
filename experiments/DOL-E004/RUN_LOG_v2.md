# DOL-E004 — RUN LOG v2

## Execution
- Status: EXECUTED
- Seeds: 1000–1099 (100 independent seeds)
- Runner: experiments/DOL-E004/run_e004.py
- Reproduction: local deterministic NumPy run using the exact runner equations and schedule.

## FACT
The complete 100-seed run was reproduced.

## CHECK
All preregistered decision assertions pass:
- mean AdaptationIndex >= 0.20: PASS
- mean absolute no-training index <= 0.05: PASS
- mean ReversalRecovery >= 0.50: PASS
- >=95% seeds AdaptationIndex >= 0.20: PASS (100%)
- >=95% seeds ReversalRecovery >= 0.50: PASS (100%)
- >=95% seeds absolute no-training index <= 0.05: PASS (100%)

## Result correction
The original RESULT.json contains 0.004654352562096703 under `mean_abs_no_training_index`. Re-running the exact current runner gives 0.00978113976342602 for the absolute mean. The original value is the signed mean of the same per-seed control indices. The decision is unchanged.

## DECISION
PASS for the operational L3 adaptation test.

## FIXATION
RESULT_v2.json is the corrected result record. The original RESULT.json is retained unchanged as historical record.

## Interpretation
This establishes only the tested operational L3 property in this synthetic model. It does not establish biological adaptation, universal memory, or a universal law.
