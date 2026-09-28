# DOL-E011 — Synthetic rule induction on held-out representations

## Status
**PREREGISTERED — NOT RUN**

## Complexity target
**L7 — Reasoning**

## Operational definition
DOL L7 requires a system to derive/usefully transform representations to solve held-out tasks.

## Core question
Can the system infer a transformation rule from several input/output examples and apply the inferred rule to new inputs that were not present during rule induction?

## Representation
Each problem uses a 3×3 binary grid. The registered rule family contains six transformations:
- identity;
- rotate 90°;
- rotate 180°;
- horizontal mirror;
- vertical mirror;
- binary inversion.

For each task, three training input/output pairs are generated from one hidden rule. Five test inputs are generated independently and are guaranteed not to be exact copies of training inputs.

## Reasoning policy
The policy enumerates the registered rule family and retains rules consistent with all training pairs. The hidden rule is accepted only when the training pairs identify one unique rule. The selected rule is then applied to the held-out inputs.

This is deliberately narrow: it tests rule induction and representation transformation, not language reasoning or open-ended intelligence.

## Controls
**Lookup baseline:** memorizes training pairs and cannot transform an unseen exact input. It returns a fixed default grid for unseen inputs.

**Random baseline:** samples one registered transformation uniformly.

All policies receive identical task data.

## Preregistered criteria
PASS requires:
- held-out exact-grid accuracy >= 0.95;
- >=90% of tasks have all five test outputs correct;
- reasoner accuracy exceeds lookup accuracy by >=0.80;
- lookup accuracy <=0.10.

## Interpretation
A PASS establishes the tested synthetic representation-transformation property only. It does not establish general reasoning, intelligence, cognition, consciousness, self-model, biological equivalence, or universality.

FACT → CHECK → RESULT → DECISION → FIXATION.
