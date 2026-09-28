# DOL-E008 Run Log

- Preregistration commit: 394acb372b4bad7b00b597cdfe9c12b50b3e9dcb
- Execution: local Python
- RNG seed: 8008
- Decisions: 2000

## FACT
Goal-policy mean objective improvement = 0.9843018938484878.
Random-policy mean objective improvement = -0.00023908302953384376.
Control gap = 0.9845409768780216.
Anti-goal mean objective improvement = -1.0012524971301766.
Maximal-choice fraction = 1.0.

## CHECK
All four preregistered decision criteria pass.

Protocol deviation: the config field held_out_goal_states was not separately operationalized as a train/test split because the policy has no fitted parameters. It does not affect the decision criteria.

## RESULT
PASS.

## DECISION
The tested synthetic system demonstrates one-step goal-directed action selection under the DOL L5 operational definition.

## FIXATION
E008 is retained as an executed PASS. No parameters were changed after execution.
