---
id: build-state-and-scenarios
type: design-research
status: proposed
tags: [pob, manifests, scenarios, progression]
---

# Build state and scenario assumptions

## A passive code is only one component

PoB serializes separate configuration, tree, items, skills, notes and other sections. It also tracks target version and conversion handling. Those are concrete examples of a build being more than a list of nodes. [Build sections and load order](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/Modules/Build.lua#L628-L680), [version handling](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/Modules/Build.lua#L84-L110).

For Claude, keep `POV1` as a native passive export and add a separate full-build manifest when gear/skills/scenarios are supported. Proposed fields are schema version, mod/data/rule identities, effective server settings, passive code and resolved allocation, equipment and rolled values, chosen skills, progression stage, scenario, mandatory constraints, and evidence limitations. Unsupported sections must be explicit rather than empty fields that imply zero effects.

The manifest should let another machine reproduce the same evaluation or refuse with a clear version/missing-data error. Do not silently upgrade old identifiers or reuse a cached legality verdict after configuration changes. This is a Valheiman design proposal, not a PoB file-format compatibility promise.

## Save assumptions beside the character

PoB's `ConfigTab` persists multiple named configuration sets. `ConfigOptions` applies player/enemy conditions as modifiers. This is a strong model for replacing a single invisible baseline with explicit, named assumptions. [Configuration persistence](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/Classes/ConfigTab.lua#L839-L1006), [condition definitions](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/Modules/ConfigOptions.lua#L158-L202).

Start small: one supported scenario with exact subjects and only the live inputs its objective needs. Distinguish a known false condition, a deliberately disabled condition, and an unknown condition. Check incompatible states. A checked box is an assumption, not a measured uptime guarantee.

Later useful scenarios could distinguish a short opening burst from sustained attacks, or a specified incoming sequence from idle regeneration. These require appropriate mechanics first; naming a scenario does not implement them. For probabilities/uptime, avoid applying an average multiplier across nonlinear thresholds without verifying that approximation.

## Progression sets need their own validation

The inspected build controller can link named tree, item, skill, and configuration sets. This is useful inspiration for level/content milestones, but it does not prove every intermediate purchase or equipment swap is reachable. [Linked sets](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/Modules/Build.lua#L361-L415).

Each Valheiman milestone still needs available points, allowed content, obtainable gear, and a legal allocation. A purchase sequence needs prefix validation. A respec needs kept requirements, refund assumptions, and explicit removals. Do not copy PoE level limits, class starts, ascendancy constraints, or item-slot rules.

## Comparison identity

A reproducible context key should cover build/scenario/configuration content and model/data versions. This extends the previous vault's context-identity proposal. Keep the UI-facing scenario name separate from the canonical identity: renaming a scenario should not alter its mechanics; changing an effective assumption must.
