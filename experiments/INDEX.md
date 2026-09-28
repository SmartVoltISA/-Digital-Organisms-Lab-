# Experiments

Все эксперименты получают ID: DOL-E000, DOL-E001, DOL-E002 ...

Для каждого эксперимента фиксируются hypothesis, config, run log, result и README.

Результаты не редактируются задним числом. Исправления создают новую версию.
- DOL-E000 — engineering baseline; executed as local reproducibility baseline; not a biological result.

- DOL-E003 — c302 AIZL↔ASHL reversible electrical relation ablation; preregistered, not yet run.

- DOL-E004 — synthetic L3 adaptation with persistence and reversal controls; executed, PASS. Corrected execution record: `experiments/DOL-E004/RESULT_v2.json`.

- DOL-E005 — synthetic L4 memory under matched present state; executed, FAIL (effect-size criterion not met).

- DOL-E006 — synthetic L4 memory persistence curve; executed, FAIL (effect threshold not met; monotonic persistence observed).

- DOL-E007 — synthetic memory detectability without absolute-unit threshold; executed, PASS (100/100 directional, preregistered statistical test and controls pass).

- DOL-E008 — synthetic one-step goal-directed action selection; executed, PASS (2000 decisions; all preregistered decision criteria pass).

- DOL-E009 — synthetic planning test; executed, INCONCLUSIVE due preregistered horizon/reward-timing inconsistency.

- DOL-E010 — synthetic future-dependent planning; executed, PASS (planning return 8.0 vs myopic 1.0; all preregistered criteria pass).

- DOL-E011 — synthetic rule induction and held-out representation transformation; executed, PASS (5000 held-out cases; all preregistered criteria pass).

- DOL-E012 — self-model test; not executed because method-check found unmatched disturbance streams.
- DOL-E013 — self-model under matched disturbances; executed, FAIL (accurate prediction but self-model advantage threshold not met).

- DOL-E014 — organism-specific self-model causal control; executed, FAIL (damaged model unexpectedly outperformed intact model).
- DOL-E015 — organism-specific self-model at held-out decision boundary; executed, PASS (100% vs 50% reactive; 0% damaged; all criteria pass).
