# DOL-E005 — Synthetic memory under matched present state

## Status
**PREREGISTERED — NOT RUN**

## Complexity target
**L4 — Memory**

Operational definition: past history measurably changes later behavior under matched present observable conditions.

This experiment is synthetic and independent of c302, Ω, RELATION-LAB, and SPACE.

## Core question
Can two trajectories with the same present observable state and identical future input produce different subsequent behavior solely because of different past histories?

## Model
Observable state x, hidden persistent state m, environment e.

x[t+1] = 0.05*x[t] + 0.4*e[t] + 0.005*m[t] + noise[t]
m[t+1] = 0.995*m[t] + 0.05*clip(e[t], -1, 1)
y[t] = x[t]

Noise SD is 0.0001. Parameters are locked before execution.

The hidden state m is not exposed to the probe. It is the candidate memory trace.

## Histories
Two histories start from the same initial state and receive:
- History A: e=+1 for 20 steps.
- History B: e=-1 for 20 steps.

Both then receive e=0 for 150 steps.

Immediately before the memory probe, the observable state x is aligned to exactly 0 in both trajectories. This alignment operation is identical for A and B and does not modify m.

The memory probe is identical for both histories: e=0.2 for 10 steps.

## Controls
1. **Memory-erase control:** after the same history and washout, set x=0 and m=0 before the identical probe. A and B should converge after erasure.
2. **Sham-history control:** no cue, same timing, washout, x alignment, identical probe.
3. **Matched-present-state control:** probe starts with x=0 in both A and B.
4. **Matched noise:** paired trajectories use the same noise sequence within each seed.
5. **100 independent seeds:** 1000–1099.

## Primary metric
MemoryEffect = mean(|R_A - R_B|), where R is the mean absolute x response during the 10-step identical probe.

The primary metric is paired per seed.

## Secondary checks
- Present-state mismatch must be exactly 0 after alignment.
- Erasure must reduce the A/B probe difference to <= 10% of the un-erased difference.
- Sham-history effect must remain <= 10% of the un-erased memory effect.
- At least 95% of seeds must show the preregistered directional memory effect: R_A > R_B.

## Decision criteria
PASS only if:
- mean MemoryEffect >= 0.10;
- >=95% seeds satisfy R_A > R_B;
- mean erase residual ratio <= 0.10;
- mean sham ratio <= 0.10.

## Interpretation
A PASS establishes an operational memory property in this specified synthetic dynamical system. It does not establish biological memory, cognition, consciousness, or a universal law.

The critical distinction is:
**same present observable state + same current input + different past history -> different future behavior.**

FACT → CHECK → RESULT → DECISION → FIXATION.
