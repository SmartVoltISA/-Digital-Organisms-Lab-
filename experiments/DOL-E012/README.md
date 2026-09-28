# DOL-E012 — Synthetic self-model and held-out control

## Status
**PREREGISTERED — NOT RUN**

## Complexity target
**L8 — Self-model**

## Operational definition
DOL L8 requires predictions about the system's own state/actions to improve held-out control or prediction.

## Core question
Does an explicit learned model of the system's own next-state dynamics improve control on held-out conditions compared with a matched controller that uses the present observable state but does not predict its own next state?

## System
Internal energy e ∈ [0,10]. Actions are -1, 0, +1.

e_next = clip(e + 0.8*a - 0.3 + drift + noise, 0, 10)

The objective is to keep energy near 5 while minimizing action magnitude:
reward = -abs(e_next - 5) - 0.1*abs(a).

## Training
The self-model is fitted only from training trajectories with drift +0.2.

## Held-out evaluation
Evaluation uses drift -0.2 and initial energies {2,4,6,8}. These conditions are not used for fitting.

## Self-model policy
Fit:
e_next = β0 + β1 e + β2 a

At each held-out step, predict the next internal state for each candidate action and select the action with highest predicted reward.

## Controls
- Reactive controller: uses current e but no learned self-dynamics.
- Oracle controller: uses the true transition law as a positive control.
- Same noise sequences.
- Held-out drift and initial states.

## Criteria
PASS requires:
- self-model held-out reward >= -1.0;
- self-model advantage over reactive >= 0.20;
- held-out one-step prediction RMSE <= 0.35;
- self-model remains within 0.50 reward of oracle.

## Interpretation
PASS establishes only the registered operational self-model property. It does not establish consciousness, subjective self-awareness, general self-knowledge, intelligence, cognition, or universality.

FACT → CHECK → RESULT → DECISION → FIXATION.
