---
id: claude-handoff
type: handoff
status: ready-not-sent
tags: [pob, claude, handoff]
---

# Suggested handoff to Claude

This note has not been sent to the running session. It is supplementary input for a later handoff, after reconciling the current checkpoint.

## Main recommendation

Use PoB revision `3dbca4463c0a59079d9f7f032d8240cf868e09da` as a reference for evaluation and explanation patterns. Preserve the existing Python engine and Valheiman native verification. Do not port PoE mechanics or add a runtime bridge before a demonstrated need.

## Best source entry points

1. `src/Classes/ModDB.lua:TabulateInternal` and `src/Modules/CalcBreakdown.lua` — source-aware explanations.
2. `src/Classes/ConfigTab.lua:Load/Save` and `src/Modules/ConfigOptions.lua` — explicit saved scenario assumptions.
3. `src/Modules/Build.lua` — full-build sections and jewel-sensitive load ordering.
4. `src/Classes/CalcsTab.lua:PowerBuilder` and `src/Classes/TreeTab.lua:BuildPowerReportList` — separate node and path impact, then per-point presentation.
5. `spec/System/TestRadiusJewelStatDiff_spec.lua` — item removal can invalidate access-dependent allocations.
6. `.busted`, `spec/System/TestBuilds_spec.lua`, `.github/workflows/test.yml` — distinguish fast tests, saved-build regressions and generated-data checks.

Pinned source links and symbols are in [[90-Sources]] and [sources.json](evidence/sources.json).

## Concrete acceptance checks for an adaptation

- The same build/scenario gives the same result after another candidate is evaluated.
- A comparison records identical effective configuration and compatible data/model identities on both sides.
- Every recommended path includes all bridge nodes and extra option costs, and passes Valheiman legality.
- Shared bridge nodes are paid for once; unreachable mandatory mechanics stop the recommendation.
- Single-node/path scores are labelled local effects, not global optima.
- Metric direction is explicit; scoring uses unrounded values and stable tie-breaking.
- Unsupported mechanics remain visible and cannot satisfy mandatory requirements by omission.
- Full-build loading preserves the passive code, supported gear/skill inputs, scenario and version identities.
- A jewel-dependent access claim requires Valheiman evidence and passes removal/replacement tests.
- Tiny exact search agrees with exhaustive enumeration on synergy, shared paths, ties and hard constraints.

## Research artifacts ready to reuse

Four checked independent examples are in [benchmarks.json](evidence/benchmarks.json). They are useful fixtures or design counterexamples, not reference outputs from PoB or Valheiman. The machine-readable [findings ledger](evidence/findings.json) maps each proposed contribution to sources, existing modules, limitations and next actions.

No patch, live test, game action, message, or publication was performed as part of this research. Reconfirm local implementation details after the active milestone; the mapping was made against the earlier supplementary vault's capture.
