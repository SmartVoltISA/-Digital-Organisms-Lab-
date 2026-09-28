# DOL-E002 — C2 Relation Ablation/Restoration Replication

## Status

EXECUTED / SYNTHETIC REPLICATION

This experiment is an engineering replication of the C2 protocol.
It is not a biological result and does not validate c302.

## Question

Does controlled relation ablation produce a measurable loss of cross-component influence, followed by recovery when the relation is restored?

## Fixed model

Ten state variables.

`x[t+1] = x[t] - x[t]/5 + drive + noise`

`y[t+1] = y[t] - y[t]/5 + k*x_2[t]`

Target observable: `y_7`.

The tested relation is `2 → 7`.

- ON: k = 0.2
- CUT: k = 0
- RESTORE: k = 0.2
- perturbation: +1.0 to source 2 at t=10
- negative-control source: source 3
- T = 80
- noise SD = 0.03
- seeds: 1000–1099
- paired runs use identical future noise.

## Primary metric

Integrated absolute target response over t=11..30 relative to the k=0 baseline.

`R = sum(abs(y_target - y_baseline))`

## Fixed decision criteria

The relation-ablation sequence is considered reproduced if all are satisfied:

1. mean CUT / mean ON <= 0.10;
2. mean RESTORE / mean ON is within [0.90, 1.10];
3. mean ON / mean negative-control > 3;
4. at least 95% of seeds have ON > 3 × negative-control.

These criteria are fixed for this replication run.

## Result

| Metric | Result |
|---|---:|
| Seeds | 100 |
| Mean ON response | 4.70075709 |
| Mean CUT response | 0.00000000 |
| Mean RESTORE response | 4.70075709 |
| Mean negative-control response | 0.51776521 |
| CUT / ON | 0.000000 |
| RESTORE / ON | 1.000000 |
| Mean ON / negative-control | 9.077* |
| Seeds ON > 3× negative control | 100/100 = 1.000 |

*Ratio of means. The per-seed ON/negative-control ratio had 5th/50th/95th percentiles of 4.331 / 9.542 / 23.397.

## Decision

**PASS — synthetic C2 replication.**

The tested relation is experimentally distinguishable by controlled ablation and restoration under this model.

## Scope

Established:
- relation ON produces measurable cross-component influence;
- CUT removes the measured coupling contribution;
- RESTORE recovers it;
- source permutation is substantially weaker.

Not established:
- biological equivalence;
- universal relation recovery;
- causal equivalence across different physical substrates;
- cognition or intelligence.

## Next

Map the same C2 operation to c302 only if a technically valid, reversible synapse/gap-junction intervention can be defined without changing the model's other parameters.
