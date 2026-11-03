---
id: power-and-search
type: optimization-research
status: source-reviewed
tags: [pob, counterfactuals, optimization, bounds]
---

# Power reports: valuable heuristics, limited claims

## Compare a change against a fixed baseline

`getMiscCalculator` returns a baseline output and a callable for overrides, including nodes, item slots, and conditions. This is a practical reference for repeatable what-if evaluation. The implementation also warns that inappropriate cache reuse can compare a baseline with itself and erase a real difference. [Calculator factory](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/Modules/Calcs.lua#L75-L120).

**Valheiman adaptation:** evaluate a copied candidate against the same explicit scenario as the base. Validate the resulting full allocation before recommending it. A scoring override is not proof that a player can legally acquire that change.

## Distinguish node effect from complete path effect

PoB's power builder calculates single-node impact and, for a node more than one step away, can recalculate with its path nodes included. For removal it can include dependent nodes. Mastery effects are considered separately. The report exposes point distance and per-point path effect. [Power builder](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/Classes/CalcsTab.lua#L496-L740), [report assembly](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/Classes/TreeTab.lua#L1060-L1185).

Claude can reuse its routing primitive to construct legal candidate packages, then evaluate each package. A useful row contains destination/choice, added nodes, extra choice costs, final cost, objective delta, per-incremental-point delta, lost mechanics, and evidence limitations. Do not charge again for nodes already held. When two candidate paths overlap, score the union rather than summing separate path costs.

PoB also has category-based build comparisons for tree nodes, items, skills, support gems, and configuration. This is a useful direction for the full-build diff once those Valheiman components exist. [Comparison power builder](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/Classes/CompareTab.lua#L2521-L2707).

## Local weights shortlist candidates

PoB's trade-query code tests individual modifiers, computes weighted output ratios, and derives search weights. It explicitly handles metric direction and exceptional baselines. That can inspire fast gear candidate screening after Valheiman items are modelled, but a local marginal weight is not a universal affix value. Recalculate shortlisted complete items and respect slot, acquisition, and budget constraints. [Weighted ratios](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/Classes/TradeQueryGenerator.lua#L164-L199), [weight generation](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/Classes/TradeQueryGenerator.lua#L563-L600).

## What these paths do not establish

The reviewed code does not supply the missing proof that a recommendation is globally best across Valheiman's legal allocations, options, items, and scenarios. Do not describe a heat map, one-step gain ranking, or path-normalized score as that proof. This is a conclusion about the inspected calculation/report mechanisms, not an exhaustive absence claim about every PoB feature.

There are specialized searches: for example the inspected `TreeTab` contains Timeless Jewel seed/weight search. Those bounded domain searches can be studied later when Valheiman has the corresponding data and rules. [Timeless Jewel search](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/Classes/TreeTab.lua#L1186-L1205).

## Independent counterexamples checked here

- **Synergy:** with two adjacent selectable nodes, each alone has utility 0 but both together have utility 10. A greedy policy that requires a strictly positive immediate improvement stops at 0; exhaustive enumeration finds 10. This refutes that greedy policy, not every possible heuristic.
- **Shared path:** `g-a-x` and `g-a-y` each require two buyable nodes, but their union costs three, not four. Separate per-path estimates cannot simply be added.
- **Metric direction:** lower delay can be preferable to higher delay. Direction must be part of the metric contract; do not infer it from a positive raw delta.

These synthetic checks inform future acceptance tests. No PoB or Valheiman optimization was benchmarked. A future global optimizer still needs exact small-instance oracles, feasibility constraints, stable tie-breaking, and valid bounds before making optimality claims.
