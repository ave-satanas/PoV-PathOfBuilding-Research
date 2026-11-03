---
id: contribution-map
type: synthesis
status: proposed
tags: [pob, pov, priorities]
---

# Contributions ranked by usefulness

PoB can reduce design mistakes and supply concrete reference implementations. It cannot validate Path of Valheiman's rules: that authority remains the extracted mod, native-code probes, and in-game observations.

| Priority | PoB pattern / evidence | Fit for Claude's tool | Smallest useful adaptation |
|---|---|---|---|
| First | Source-aware modifier queries and calculation breakdowns: `ModDB:TabulateInternal`, `CalcBreakdown` | `stats.py`, `character.py`, later hit/defence integration | Explain a few selected metrics with contributing source IDs and omitted-effect reasons. |
| First | Saved configuration sets: `ConfigTab:Load/Save` | Fixed baseline in `evaluate.py`; future scenarios | A small explicit scenario record, with unsupported states rejected rather than guessed. |
| First | Build serialization owns tree, items, skills and configuration: `Build.lua` | Native `POV1` only carries passives/choices | A separate versioned full-build manifest that preserves the native passive code. |
| Next | Node/path counterfactual power: `CalcsTab:PowerBuilder`, `TreeTab:BuildPowerReportList` | `evaluate.py`, `passives.py`, future recommendation layer | Report total metric change, complete added path, choice costs, and change per incremental point. |
| Next | Targeted recalculation weights: `TradeQueryGenerator` | Candidate ordering for gear/affixes after item modelling | Use local weights to shortlist; fully evaluate and validate finalists. |
| Next | Headless regression suite and generated-cache CI check | Existing probes, tests, mutation policy | Add complete request/build/scenario fixtures without replacing native oracles. |
| After mechanics | Access-changing jewel removal tests | Dunin's jewel-opened second start | Explicit access grants and dependencies, derived from Valheiman code. |
| After profiling | Run-local memoization, resumable work | Future expensive search | Establish correct cold evaluation first; add cache-equivalence tests before reuse. |

Primary references: [modifier queries](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/Classes/ModDB.lua#L278-L305), [configuration persistence](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/Classes/ConfigTab.lua#L839-L1006), [power calculations](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/Classes/CalcsTab.lua#L496-L758), [trade weights](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/Classes/TradeQueryGenerator.lua#L563-L600).

## What this adds to the previous supplementary research

The earlier vault identified baseline wording, comparison legality, precision, context identity, stale artifacts, and search scope. This vault supplies external implementation references for addressing those gaps. It does not repeat their discovery or imply PoB itself solves them all.

In particular, PoB's conditional configuration is a model for making assumptions visible, not evidence that any chosen condition will hold in Valheim gameplay. Its per-point display is a model for useful explanations, not a substitute for constrained search.

## What to avoid importing

Keep the existing Valheiman stat engine and verified formulas. Do not copy PoE armour, energy shield, leech, crit, damage conversion, passive restrictions, or percentages just because their names resemble Valheiman concepts. Do not add a large text parser when Valheiman already supplies structured modifier rows. These are engineering recommendations based on the differing data contracts, not claims that PoB's mechanics are wrong.
