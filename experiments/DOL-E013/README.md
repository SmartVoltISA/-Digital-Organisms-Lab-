# DOL-E013 — Self-model under matched disturbances

## Status
**EXECUTED — FAIL**

## Complexity target
**L8 — Self-model**

## Relation to DOL-E012
E012 is retained as an unexecuted method-check failure: code review found that its held-out disturbance streams were not actually matched between policies. E013 is a new preregistered experiment with explicit common disturbances.

## Operational definition
L8 requires predictions about the system's own state/actions to improve held-out control or prediction.

## Core question
Does a learned model of the system's own next-state dynamics improve held-out control when compared with a reactive controller under identical initial states and identical disturbance sequences?

## System
e_next = clip(e + 0.8*a - 0.3 + drift + noise, 0, 10)

reward = -abs(e_next-5) - 0.1*abs(a)

The self-model is fitted only on training trajectories with drift +0.2.

Held-out evaluation uses drift -0.2 and initial energies {2,4,6,8}.

## Controls
Self-model and reactive policies receive the same initial energy and the same pre-generated noise sequence within each episode.

Oracle uses the true transition model as a positive control.

## Criteria
PASS requires:
- self-model mean reward >= -1.0;
- self-model advantage over reactive >= 0.20;
- held-out one-step prediction RMSE <= 0.35;
- self-model within 0.50 reward of oracle.

## Interpretation
PASS establishes only this registered operational self-model property. It does not establish consciousness, subjective self-awareness, general self-knowledge, intelligence, or universality.

FACT → CHECK → RESULT → DECISION → FIXATION.
