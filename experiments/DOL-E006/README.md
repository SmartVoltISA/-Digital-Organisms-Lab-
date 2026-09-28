# DOL-E006 — Synthetic memory persistence curve

## Status
**EXECUTED — FAIL**

The preregistered persistence-curve test was executed for 100 seeds. See `RUN_LOG.md` and `RESULT.json`.

## Complexity target
**L4 — Memory persistence**

## Relation to DOL-E005
DOL-E005 is retained unchanged as a failed preregistered test. E006 is a new experiment, not a correction of E005.

## Question
How does a history-dependent effect decay as the interval between memory writing and memory readout increases?

## Hypothesis
A signed persistent internal state can retain information about opposite histories for a measurable interval. The observable memory effect should decrease with increasing delay and approach the sham/erase baseline.

## Model
x[t+1] = 0.05*x[t] + 0.4*e[t] + 0.005*m[t] + noise[t]
m[t+1] = 0.995*m[t] + 0.05*clip(e[t], -1, 1)
y[t] = x[t]

Noise SD = 0.0001.

## Protocol
For each seed and each delay:
1. Baseline: 50 neutral steps.
2. History A: e=+1 for 20 steps.
3. History B: e=-1 for 20 steps.
4. Neutral washout for the registered delay.
5. Set x=0 in both trajectories without modifying m.
6. Identical probe: e=0.2 for 10 steps.
7. Compute paired memory effect |R_A-R_B|.

Delays are fixed in config.json: 0, 20, 50, 100, 200, 500, 1000 steps.

The same noise sequence is used for A/B within each seed and delay.

## Controls
- sham history at every delay;
- erase control at every delay;
- exact x alignment before probe;
- 100 seeds (1000–1099).

## Primary metrics
MemoryEffect(delay) = mean over seeds of |R_A - R_B|.
RetentionRatio(delay) = MemoryEffect(delay) / MemoryEffect(0).

## Decision criteria
This experiment is descriptive and falsification-oriented. It does not award L4 from a single threshold.

PASS for the persistence-curve hypothesis requires:
- MemoryEffect(0) >= 0.10;
- MemoryEffect(delay) decreases monotonically within numerical tolerance for the registered delay sequence;
- erase residual ratio <= 0.10 at every delay;
- sham ratio <= 0.10 at every delay.

If these criteria fail, the experiment is FAIL/INCONCLUSIVE as specified; parameters are not changed after execution.

## Interpretation
A successful curve would characterize persistence of the synthetic memory mechanism. It would not establish biological memory or universality.

FACT → CHECK → RESULT → DECISION → FIXATION.
