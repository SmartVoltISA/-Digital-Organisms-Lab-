# DOL-E004 — Synthetic adaptation with persistence and reversal controls

## Status
**PREREGISTERED — NOT RUN**

## Complexity target
**L3 — Adaptation**

Operational target: after repeated exposure to a defined perturbation, the system changes its response; the change persists after the immediate stimulus is removed; the changed response reverses or generalizes according to a pre-registered rule.

This experiment is synthetic and independent of c302, Ω, RELATION-LAB, and SPACE.

## Core question
Can a minimal dynamical organism adapt to repeated environmental conditions without the result being explained merely by the instantaneous stimulus or a transient state variable?

## Model
Internal state x, adaptive state a, environment e, output y.

x[t+1] = 0.8*x[t] + 0.6*e[t] - 0.4*a[t]
a[t+1] = 0.98*a[t] + 0.08*clip(abs(e[t]) - 0.5, 0, 1)
y[t] = x[t] - 0.5*a[t]

The adaptive state changes slowly and can persist after the immediate stimulus ends. Parameters are locked before execution.

## Phases
1. Baseline: neutral environment.
2. Training: repeated high-magnitude environment pulses.
3. Washout: neutral environment.
4. Probe: identical test input.
5. Reversal: repeated opposite-sign pulses.
6. Post-reversal washout and identical probe.

The exact schedule is fixed in config.json.

## Primary metric
AdaptationIndex = (R_pre - R_post) / max(R_pre, epsilon)
where R_pre and R_post are mean absolute responses to identical probe inputs before and after training/washout.

## Controls
- no-training control;
- sham/washout timing control;
- matched pre/post probe;
- fixed neutral washout;
- reversal condition;
- 100 independent seeds;
- locked parameters and schedule.

## Decision criteria
PASS only if all criteria in config.json hold: training produces adaptation >= 0.20; no-training absolute index <= 0.05; reversal index <= -0.10; and at least 95% of seeds satisfy the preregistered directional criterion.

## Interpretation
PASS establishes only an operational L3 adaptation property in this specified synthetic system. It does not establish biological adaptation, universal memory, or a universal law.

FACT → CHECK → RESULT → DECISION → FIXATION.
Failed runs remain in the experiment history.