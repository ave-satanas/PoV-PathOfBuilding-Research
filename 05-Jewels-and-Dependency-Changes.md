---
id: jewels-and-dependencies
type: mechanics-research
status: reference-pattern-only
tags: [pob, pov, jewels, dunin]
---

# Jewels can change access, not just numbers

The captured Valheiman context leaves Dunin's jewel-opened second start unresolved. PoB offers a useful reference for representing access-changing equipment, but its jewel rules do not establish what that Valheiman jewel actually does.

## What the PoB code shows

`CalcSetup` processes radius-jewel effects in multiple stages. Its modifier construction considers allocated and relevant nearby nodes. This warns against treating every jewel as a final additive stat bonus. [Radius-jewel passes](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/Modules/CalcSetup.lua#L147-L315).

PoB's build loader explicitly delays passive-tree loading until other sections, including items, are available; its comment identifies jewel-dependent route checks as the reason. This is a concrete dependency-order lesson for loading a full Valheiman manifest. [Deferred tree load](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/Modules/Build.lua#L651-L675).

The radius-jewel regression suite tests removal/replacement of access-changing jewels, including nodes that are not ordinarily connected to the start. One removal test builds a `removeNodes` override for nodes dependent on the removed access. Other cases distinguish support from another jewel. [Removal and replacement tests](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/spec/System/TestRadiusJewelStatDiff_spec.lua#L406-L526).

## A safe Valheiman research task

1. Identify the exact jewel ID, source version, acquisition constraints, and native methods that grant access.
2. Separate ordinary adjacency, granted starts, radius/free allocation, and any item-allocated passives. Record which source grants each permission.
3. Revalidate allocation when the item is added, removed, moved, or replaced. Determine native behavior rather than assuming whether disconnected nodes remain allocated, are muted, or are refunded.
4. Recalculate stats and budget from the resulting effective allocation, preserving uncertainty where behavior cannot yet be verified.

These are proposed investigation steps. No Valheiman jewel rule was implemented or experimentally resolved in this research.

## Targeted future tests

| Case | Required evidence/result |
|---|---|
| Second start without granting jewel | Ordinary validator outcome remains unchanged. |
| Second start with verified jewel | Access derived from that specific effect and version, not a global multi-start exception. |
| Remove the sole granting jewel | Detect every dependent node; match native persistence/muting/refund semantics. |
| A second source still grants access | Preserve access when independently justified. |
| Jewel changes numerical mods and access | Apply both effects in the documented dependency order. |
| Jewel removed after a saved evaluation | Invalidate access/stat results and cached legality. |

The main contribution is the dependency model and test shape. Porting Thread of Hope, Impossible Escape, PoE radii, or Timeless Jewel seed logic would not answer Dunin's legality question.
