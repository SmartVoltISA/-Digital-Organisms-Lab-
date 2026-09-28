# DOL-E008 — Synthetic goal-directed action selection

## Status
**EXECUTED — PASS**

## Complexity target
**L5 — Goal-directed behavior**

## Operational definition
L5 requires a system to select actions that improve a pre-defined objective under available alternatives.

E008 deliberately tests only one-step action selection. It does not test future-dependent sequences; therefore a PASS is not evidence for L6 planning.

## Core question
Given the same present state, goal, candidate actions, and matched stochastic disturbance, does the system consistently select the action that maximizes the pre-defined objective?

## Model
State s, goal g, action a ∈ {-1,0,+1}.

s_next = clip(s + a + noise, -10, 10)

Objective:
J(s,g) = -abs(s-g)

For every decision, all candidate actions are evaluated from the same present state and goal using the same noise realization. The selected action maximizes predicted J(s_next,g). Ties use the smallest absolute action.

## Controls
1. Random policy: uniformly selects one candidate.
2. Anti-goal control: selects the action that maximizes distance from the goal.
3. Matched noise across policies.
4. Multiple goal values and initial states, including combinations not used as a single fixed reflex.

## Preregistered criteria
PASS requires:
- mean objective improvement >= 0.50;
- >=90% decisions select an action attaining the maximal available objective;
- goal-policy improvement exceeds random-policy improvement by >=0.40;
- anti-goal control has negative mean objective improvement.

## Execution note
The execution result is fixed in `RESULT.json`; this README status reflects the completed run.\n\n## Interpretation
A PASS establishes the tested operational property: the synthetic system selects actions that improve a pre-defined objective under alternatives.

It does not establish planning, reasoning, self-model, intelligence, cognition, consciousness, biological equivalence, or universality.

FACT → CHECK → RESULT → DECISION → FIXATION.
