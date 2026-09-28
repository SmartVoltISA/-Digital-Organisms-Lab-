# DOL-E015 — Organism-specific self-model controls held-out action selection

## Status
**EXECUTED — PASS**

## Complexity target
**L8 — Self-model**

## Why E015 exists
E013 showed accurate self-state prediction but insufficient control advantage. E014 attempted a causal model-damage test, but the damaged model unexpectedly performed better; that experiment remains independent and is not modified.

E015 isolates the self-model contribution at the decision boundary itself.

## Core question
Does knowing the organism's own actuator gain allow correct action selection on held-out states where a generic gain and a fixed state-only controller choose the wrong action?

## System
Actuator gain is organism-specific and fixed at g=0.55.

e_next = clip(e + g*a - 0.1 + noise, 0, 10)

Reward:
reward = -abs(e_next-5) - 0.30*a

For held-out states 4.40, 4.45, 4.50, and 4.55, the optimal action under g=0.55 is action 1. A generic gain of 1.00 predicts action 0 for these states under the same objective.

## Training
The gain is estimated only from training trajectories with initial states {3,4,5,6,7}. Held-out decision states are disjoint from training states.

## Policies
- Intact self-model: estimates its own gain and predicts the consequence of each action.
- Reactive: uses current state only with a fixed threshold 4.475.
- Damaged self-model: learned policy with its gain replaced by generic 1.00.
- Oracle: uses true gain 0.55.

## Criteria
PASS requires:
- self-model held-out action accuracy >=90%;
- advantage over reactive >=40 percentage points;
- damage causes >=40 percentage-point accuracy drop;
- prediction RMSE <=0.05.

## Interpretation
This is an operational self-model test only. It does not establish consciousness, subjective self-awareness, general self-knowledge, intelligence, or universality.

FACT → CHECK → RESULT → DECISION → FIXATION.
