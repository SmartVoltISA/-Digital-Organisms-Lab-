# DOL Repository Audit — 2026-09-28

## Scope
Full documentation/provenance audit of the DOL repository after E015. No new scientific claim is introduced by this audit.

## Current ladder
- L0 PASS — E000
- L1 PASS — E000
- L2 PASS — E002
- L3 PASS — E004
- L4 PASS — E007; E005/E006 remain FAIL
- L5 PASS — E008
- L6 PASS — E010; E009 remains INCONCLUSIVE
- L7 PASS — E011
- L8 PASS — E015; E013/E014 remain FAIL; E012 was not scientifically executed

## Consistency fixes made
1. E004 config status corrected to EXECUTED_PASS.
2. E005 config status corrected to EXECUTED_FAIL.
3. E006 config status corrected to EXECUTED_FAIL.
4. E007 config status corrected to EXECUTED_PASS.
5. E012 config status corrected to METHOD_CHECK_NOT_EXECUTED.
6. E013 RESULT decision corrected from stale PASS metadata to FAIL; numerical results unchanged.
7. E014 recorded as EXECUTED_FAIL.
8. E015 recorded as EXECUTED_PASS.
9. Complexity Ladder next target updated: L8 is demonstrated; next work is cross-model transfer, not an invented L9.
10. NEXT_STEPS updated to prioritize E003/c302 and cross-model validation while keeping SPACE outside DOL.
11. INDEX corrected to include E000 in the experiment ID convention and current list.

## Repository gaps found
### GAP-1 — E000 lacks RESULT.json
E000 is an engineering baseline and has README/config, but no RESULT.json was found. Do not fabricate one. A future bookkeeping pass can add a genuine result if the original execution output is available.

### GAP-2 — E002 lacks config.json and RESULT.json
E002 README contains the reported result and fixed criteria, but the expected config/result artifacts are absent. The result should be treated as documented historical evidence, not silently reconstructed.

### GAP-3 — E003 remains NOT RUN
The c302 experiment is preregistered and the external model is pinned. No simulation result is claimed.

### GAP-4 — Run provenance is incomplete for some historical experiments
The protocol requires seed, code version, run log, and reproducible local command. Several historical experiments have results but not the full artifact set in the repository. This is a provenance gap, not evidence that the scientific result is false.

### GAP-5 — Protocol requires HYP-ID
The experiment protocol lists HYP-ID as required, but the inspected configs do not consistently contain a HYP-ID field. Future experiments should include one before execution.

## Scientific integrity checks
- Failed and inconclusive experiments remain recorded.
- No threshold was changed after E013/E014 results.
- E009 remains INCONCLUSIVE rather than being rewritten.
- E012 is not treated as a scientific FAIL because it was stopped at method check.
- E015 is the current operational L8 PASS.
- c302 remains independent and is not connected to SPACE.
- DOL does not establish biological equivalence, consciousness, intelligence, or universality.

## Audit conclusion
The repository is scientifically coherent at the level of its current operational claims, but its historical provenance is not yet artifact-complete. The main remaining technical/scientific item is E003, not another synthetic complexity level.
