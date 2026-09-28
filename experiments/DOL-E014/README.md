# DOL-E014 — Causal organism-specific self-model

## Status
**EXECUTED — FAIL**

## Complexity target
**L8 — Self-model**

## Why E014 exists
E013 showed accurate self-state prediction but only a +0.0437 reward advantage over a strong reactive controller, below its preregistered threshold. E014 therefore tests a more causally specific property without changing E013.

## Core question
Does an organism-specific learned model of its own action-state dynamics improve held-out control, and does damaging that model remove a substantial part of the advantage?

## System
Each organism has its own actuator gain:
g = 0.55.

e_next = clip(e + g*a - 0.2 + drift + noise, 0, 10)

The controller must learn the organism-specific gain from its own training trajectory.

## Held-out condition
Training uses drift +0.2. Evaluation uses drift -0.2 and unseen initial energies.

## Policies
1. Intact self-model: uses learned organism-specific dynamics.
2. Reactive baseline: uses current state only and no self-dynamics model.
3. Damaged self-model: same learned policy, but its learned gain is replaced by a generic incorrect gain of 1.0.
4. Oracle: true organism dynamics.

## Causal intervention
The key test is model damage. If the learned self-model is causally useful, replacing its organism-specific gain with an incorrect generic value should reduce held-out control performance.

## Criteria
PASS requires:
- intact self-model advantage over reactive >= 0.20;
- held-out prediction RMSE <= 0.20;
- damage causes >=0.15 reward drop;
- intact self-model is within 0.30 reward of oracle.

## Interpretation
This is an operational self-model test only. It does not establish consciousness, subjective self-awareness, general self-knowledge, intelligence, or universality.

FACT → CHECK → RESULT → DECISION → FIXATION.
