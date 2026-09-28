# DOL-E006 — RUN LOG

## FACT
The preregistered persistence-curve experiment was executed for 100 seeds (1000–1099) across delays 0, 20, 50, 100, 200, 500 and 1000 steps.

## CHECK
Memory effect:
- 0: 0.0097675360
- 20: 0.0088358154
- 50: 0.0076021959
- 100: 0.0059168846
- 200: 0.0035842737
- 500: 0.0007967561
- 1000: 0.0000649929

The curve is strictly monotonic decreasing.
A > B in 100/100 seeds at every delay.
Erase residual ratio is 0 at every delay.
Sham ratio is 0 at every delay.

## RESULT
The experiment demonstrates a reproducible persistence curve for the synthetic hidden state, with the effect decaying toward zero as the readout delay increases.

However, the preregistered minimum MemoryEffect(0) >= 0.10 is not met (measured 0.0097675360).

## DECISION
FAIL for the preregistered E006 criteria. L4 is not awarded.

## FIXATION
The result is retained as a separate experiment. No parameters were changed after observing the result.

## Interpretation
This supports the narrower statement that the tested model has a measurable, history-dependent trace with finite persistence. It does not establish L4 under the current DOL threshold, biological memory, cognition, or universality.
