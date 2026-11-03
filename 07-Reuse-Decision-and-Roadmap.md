---
id: reuse-and-roadmap
type: decision-proposal
status: recommended
tags: [pob, reuse, roadmap]
---

# Reuse decision and staged roadmap

## Preferred route

| Approach | Contribution | Cost/limit | Recommendation |
|---|---|---|---|
| Study source and adapt small patterns | Contexts, counterfactuals, provenance, tests | Requires Valheiman-specific design and verification | **Start here** |
| Port an isolated helper | May save a small amount of code | Units, dependencies and license notices still need attention | Only when smaller than the existing solution |
| Run PoB headless beside Python | PoE calculations, reference behavior for PoE fixtures | Another runtime and data model; no Valheiman oracle | Optional research experiment, not a product dependency |
| Replace PoB's game model with Valheiman data | Potential reuse of some planner UI | Requires replacing deep PoE-specific calculations, data and legality | Defer; no evidence this is the shortest path |
| Fork the full desktop application | Rich existing UI | Long-term Lua/host/data integration and upstream maintenance | Not justified for the current Python engine |

The wrapper's application dependencies and the calculation setup's PoE-specific build inputs support the integration-cost assessment. This is an engineering judgment, not a measured port estimate. [Headless entry point](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/HeadlessWrapper.lua), [calculation setup](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/Modules/CalcSetup.lua#L470-L517).

## Small complete milestones

1. **An explainable scenario evaluation.** Pick one already-supported objective. Persist its inputs and evidence identity; explain its important sources and omissions. Reject incompatible/unsupported required inputs.
2. **A legal path-value report.** From a valid starting build, evaluate complete reachable node/option packages under one scenario. Include total and incremental cost, metric direction, lost mechanics, and deterministic ordering. Keep this descriptive until the recommendation boundary validates it.
3. **A tiny exact value optimizer.** Enumerate legal synthetic candidates, compare search output with the oracle, include synergy/shared-path examples, then evaluate a bounded real task. Report the searched domain and avoid unsupported optimality claims.
4. **Full-build and progression state.** Add equipment/skills only as their mechanics become supported. Save manifest/scenario versions and validate each milestone or purchase prefix.
5. **Jewel access and incremental evaluation.** First derive native access behavior, then add dependency tests. Profile cold calculation before introducing caching.

This order is proposed for after Claude's current milestone. It should be reconciled with the repository's final checkpoint; it does not authorize overwriting active work or rerunning its mutation gate.

## Code reuse and notices

The pinned repository's top-level notice grants MIT-style reuse and requires its copyright and permission notice to accompany copies or substantial portions. The same file lists separate notices for bundled components. If actual source is copied or substantially ported, record the original file/revision and preserve applicable notices. This vault supplies links and analysis rather than copied implementation. It does not establish redistribution rights for all game data or assets. [Pinned license file](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/LICENSE.md).
