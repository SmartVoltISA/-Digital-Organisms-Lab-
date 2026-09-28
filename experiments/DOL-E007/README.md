# DOL-E007 — Detectable synthetic memory without absolute-unit threshold

## Status
**PREREGISTERED — NOT RUN**

## Complexity target
**L4 — Memory**

## Why this experiment exists
DOL-E005 and DOL-E006 used an absolute MemoryEffect threshold of 0.10. Those experiments remain unchanged and failed that preregistered criterion.

The DOL complexity definition itself is behavioral: past history must measurably change later behavior under matched present conditions. E007 therefore tests detectability and reproducibility without treating 0.10 as a universal unit-independent L4 threshold.

## Core question
With the same present observable state and identical probe input, does the tested synthetic system produce a reproducible difference attributable to prior history?

## Locked model and protocol
The model is unchanged from E005/E006. E007 uses new seeds 2000–2099 and reads out immediately after the 20-step history cue.

Before the probe, observable x is aligned to exactly 0 without modifying hidden state m. The probe is identical: e=0.2 for 10 steps.

## Primary test
For each seed:
D_i = R_A_i - R_B_i.

The primary inferential test is preregistered before execution:
- one-sided paired sign test, H0: P(D>0) <= 0.5, alpha=0.01;
- bootstrap 95% confidence interval for mean(D) must exclude 0 on the positive side;
- at least 95% of seeds must have D_i > 0.

## Controls
- erase: x=0 and m=0 before identical probe;
- sham: no history cue;
- matched noise;
- exact observable-state alignment.

Erase and sham ratios must each be <= 0.10.

## Secondary metric
Scale-free contrast:
2*abs(R_A-R_B) / max(R_A+R_B, epsilon).

This is descriptive only and cannot by itself award L4.

## Interpretation
PASS means the preregistered synthetic mechanism produces reproducible history-dependent behavior under matched present observable state.

It does not establish biological memory, cognition, consciousness, universality, or a ranking of organisms.

FACT → CHECK → RESULT → DECISION → FIXATION.
