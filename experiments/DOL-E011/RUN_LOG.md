# DOL-E011 Run Log

- Preregistration was fixed before execution.
- Execution: local Python in STAND environment.
- RNG seed: 11011.
- Tasks: 1000.
- Held-out test cases: 5000.

## FACT
Reasoner exact-grid accuracy = 1.0.
Lookup accuracy = 0.002.
Random-rule accuracy = 0.2092.
Tasks with all five held-out outputs correct = 1.0.
Reasoner-vs-lookup control gap = 0.998.

Per-rule accuracy was 1.0 for all six registered transformations.

## CHECK
All preregistered decision criteria pass.

Train/test exact input sets were disjoint. Each task's training examples uniquely identified one rule from the registered rule family before the held-out inputs were evaluated.

## RESULT
PASS.

## DECISION
The tested synthetic system demonstrates the registered representation-transformation and held-out rule-application property.

## FIXATION
E011 is retained as an executed PASS. The interpretation remains limited to the registered operational L7 test.
