# DOL-E005 — RUN LOG

## FACT
The preregistered L4 memory experiment was executed for 100 seeds (1000–1099) using the locked configuration.

## CHECK
- MemoryEffect >= 0.10: FAIL; measured 0.00460518554423805.
- >=95% seeds R_A > R_B: PASS; measured 100%.
- Erase residual ratio <= 0.10: PASS; measured 0.
- Sham ratio <= 0.10: PASS; measured 0.

The observable state x was aligned to exactly 0 before every probe. Paired A/B trajectories used the same noise sequence per seed.

## RESULT
The model contains a reproducible history-dependent directional effect, and erasing the hidden state removes the effect. However, the effect magnitude is 0.004605..., below the preregistered 0.10 threshold.

## DECISION
FAIL for DOL-E005. L4 is not established.

## DECISION DISCIPLINE
No parameters were changed after this result. Any redesigned L4 test must receive a new version/experiment record and be preregistered before execution.

## Interpretation
This is a useful falsification: the operational structure can retain history, but the chosen coupling is too weak to satisfy the preregistered measurable-memory criterion.
