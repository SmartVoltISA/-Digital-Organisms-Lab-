# Digital Organisms Complexity Ladder v1.0

## Purpose

Определить исследовательскую лестницу от минимальной динамической системы до архитектуры, в которой отдельно проверяются память, планирование и рассуждение.

Это **не рейтинг организмов** и не утверждение, что более высокий уровень «лучше».
Уровни описывают наличие проверяемых механизмов и наблюдаемых свойств.

## Core principle

Не сравниваем «червя» и SPACE как равные объекты.

Сравниваем, **какие свойства поведения требуют какого уровня организации**.

```
L0  Dynamic substrate
 ↓
L1  Reactive organism
 ↓
L2  Relational organism
 ↓
L3  Adaptive organism
 ↓
L4  Memory-bearing organism
 ↓
L5  Goal-directed / planning organism
 ↓
L6  Reasoning organism
 ↓
L7  Meta-cognitive / self-modeling system
```

## L0 — Dynamic substrate

State evolves according to fixed rules.

Required observations:
- state;
- transition;
- stability;
- perturbation response.

No claim of cognition.

## L1 — Reactive organism

Closed loop:

`state → environment → action → feedback`

Required properties:
- measurable stimulus;
- measurable response;
- repeatability;
- environment dependence.

DOL-E000 is an engineering baseline for this layer.

## L2 — Relational organism

Behavior depends on structured relations between components.

Required tests:
- relation ON;
- relation CUT;
- relation RESTORED;
- paired perturbation;
- negative controls.

Primary observable:

`relation state → change in cross-component influence`

This layer connects to the independently developed RELATION/Ω experimental methodology.

## L3 — Adaptive organism

The system changes its future response as a consequence of prior interaction.

Required distinction:

`state change ≠ adaptation`

Adaptation requires:
1. history-dependent response;
2. controlled repeated exposure;
3. changed future behavior;
4. comparison against a history-free/control condition.

## L4 — Memory-bearing organism

A persistent internal state affects later behavior after the original stimulus is removed.

Minimum test:

`stimulus → internal change → stimulus removed → delayed probe`

A memory claim requires:
- retention interval;
- probe;
- control without retained state;
- reproducible behavioral difference.

## L5 — Goal-directed / planning organism

The system selects actions with reference to a future state or objective.

Required evidence:
- explicit or inferable target state;
- multiple available actions;
- action sequence;
- comparison against reactive policy;
- cost/time or other fixed objective;
- counterfactual or blocked-path test where possible.

Planning must not be inferred merely from complex trajectories.

## L6 — Reasoning organism

The system can transform internal representations to derive an action or conclusion not reducible to a direct stimulus-response mapping.

Required tests should include:
- novel combinations;
- withheld information;
- distractors;
- counterfactual task;
- transfer to structurally related but unseen cases.

A language model connected to the system does not by itself prove that the organism possesses the corresponding reasoning mechanism.

## L7 — Meta-cognitive / self-modeling system

The system maintains a usable model of aspects of its own state, uncertainty, limits, or operation and this model changes behavior.

Required evidence:
- self-referential state representation;
- measurable uncertainty or capability estimate;
- intervention on the self-model;
- behavioral consequence;
- external validation.

## Important separation

The ladder is about **properties to test**, not labels to assign.

A system may implement a property without implementing every lower-level mechanism in the same way.

Conversely, having an architectural component named "memory", "planning", or "reasoning" is not evidence that the corresponding behavioral property exists.

## External control point

c302 / C. elegans remains an **independent biological computational baseline**.

It is not connected to SPACE.

Its role is to provide a lower-complexity reference against which specific experimentally defined properties can be compared.

## SPACE boundary

SPACE is not modified by this document.

If SPACE is later tested, it enters only through the same external experimental interface and only for preregistered questions.

## Research question

The central question is:

> At which added organizational layer does a new behavioral property become experimentally detectable, and which mechanism is necessary for that property?

This converts "building a mind" from an architectural claim into a sequence of falsifiable comparisons.
