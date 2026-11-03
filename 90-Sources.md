---
id: source-registry
type: sources
status: pinned-and-hashed
tags: [pob, sources, reproducibility]
---

# Source registry

Revision: `3dbca4463c0a59079d9f7f032d8240cf868e09da`. Hashes and precise anchors: [sources.json](evidence/sources.json).

Implementation observations take precedence over potentially older documentation. These links establish PoB behavior; all Valheiman adaptations are proposals.

## S01

[README.md](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/README.md#L9) — Project feature overview.

Anchor: `### Features`; line 9.

## S02

[src/Modules/Calcs.lua](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/Modules/Calcs.lua#L89) — Baseline and override evaluation.

Anchor: `function calcs.getMiscCalculator(build)`; line 89.

## S03

[src/Modules/CalcSetup.lua](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/Modules/CalcSetup.lua#L487) — Calculation environment and overrides.

Anchor: `function calcs.initEnv(build, mode, override, specEnv)`; line 487.

## S04

[src/Classes/CalcsTab.lua](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/Classes/CalcsTab.lua#L496) — Node, mastery, path and removal power.

Anchor: `function CalcsTabClass:PowerBuilder()`; line 496.

## S05

[src/Classes/TreeTab.lua](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/Classes/TreeTab.lua#L1060) — Path-normalized power report.

Anchor: `function TreeTabClass:BuildPowerReportList(currentStat)`; line 1060.

## S06

[src/Classes/PowerReportListControl.lua](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/Classes/PowerReportListControl.lua#L14) — Power report columns and filters.

Anchor: `function PowerReportListClass:PowerReportListControl`; line 14.

## S07

[src/Classes/TradeQueryGenerator.lua](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/Classes/TradeQueryGenerator.lua#L164) — Weighted local output ratios and mod screening.

Anchor: `function TradeQueryGeneratorClass.WeightedRatioOutputs`; line 164.

## S08

[src/Classes/ModDB.lua](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/Classes/ModDB.lua#L278) — Values paired with modifier provenance.

Anchor: `function ModDBClass:TabulateInternal`; line 278.

## S09

[src/Classes/ModStore.lua](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/Classes/ModStore.lua#L40) — Shared modifier store and actor/condition state.

Anchor: `function ModStoreClass:ModStore(parent)`; line 40.

## S10

[src/Modules/CalcBreakdown.lua](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/Modules/CalcBreakdown.lua#L44) — Formula and slot breakdowns.

Anchor: `function breakdown.simple`; line 44.

## S11

[docs/modSyntax.md](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/docs/modSyntax.md#L9) — Modifier types, flags, sources and tags.

Anchor: `### ModType`; line 9.

## S12

[docs/addingMods.md](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/docs/addingMods.md#L1) — Text parsing, cached mods and unsupported text.

Anchor: `ModParser`; line 1.

## S13

[src/Classes/ConfigTab.lua](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/Classes/ConfigTab.lua#L839) — Saved configuration sets.

Anchor: `function ConfigTabClass:Load(xml, fileName)`; line 839.

## S14

[src/Modules/ConfigOptions.lua](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/Modules/ConfigOptions.lua#L171) — Named player and enemy assumptions.

Anchor: `conditionMoving`; line 171.

## S15

[src/Modules/Build.lua](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/Modules/Build.lua#L629) — Build sections, versions and deferred tree loading.

Anchor: `self.savers = {`; line 629.

## S16

[src/HeadlessWrapper.lua](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/HeadlessWrapper.lua#L60) — Headless application setup and build loaders.

Anchor: `function loadBuildFromXML`; line 60.

## S17

[.busted](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/.busted#L11) — Default headless test selection.

Anchor: `exclude-tags`; line 11.

## S18

[.github/workflows/test.yml](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/.github/workflows/test.yml#L16) — Tests and regenerated modifier-cache check.

Anchor: `busted --lua=luajit`; line 16.

## S19

[spec/System/TestBuilds_spec.lua](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/spec/System/TestBuilds_spec.lua#L18) — Stored build-output regression loader.

Anchor: `expose("test all builds #builds"`; line 18.

## S20

[spec/System/TestOffence_spec.lua](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/spec/System/TestOffence_spec.lua#L29) — Interaction tests for skill rate limits.

Anchor: `Cooldown Recovery Rate`; line 29.

## S21

[spec/System/TestRadiusJewelStatDiff_spec.lua](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/spec/System/TestRadiusJewelStatDiff_spec.lua#L409) — Jewel access dependency comparisons.

Anchor: `Thread of Hope removal comparison`; line 409.

## S22

[src/Classes/CompareTab.lua](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/Classes/CompareTab.lua#L2516) — Category-based build-element comparisons.

Anchor: `function CompareTabClass:ComparePowerBuilder`; line 2516.

## S23

[src/Modules/CalcTools.lua](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/Modules/CalcTools.lua#L16) — Explicit percentage arithmetic.

Anchor: `function calcLib.mod(modStore, cfg, ...)`; line 16.

## S24

[LICENSE.md](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/LICENSE.md#L5) — Project and bundled-component notices.

Anchor: `Copyright (c) 2016 David Gowor`; line 5.

## S25

[docs/rundown.md](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/docs/rundown.md#L3) — Navigation guide; implementation takes precedence.

Anchor: `Layout`; line 3.

## S26

[src/Classes/SkillsTab.lua](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/Classes/SkillsTab.lua#L256) — Example specialized optimizer.

Anchor: `Optimise Sockets`; line 256.

## Local Valheiman comparison context

The comparison uses the prior supplementary vault, captured at 2026-11-03T00:48:09Z, and its source manifest. It is a dated reference, not a fresh audit of Claude's active repository.

Known context: Python stat and character assembly; passive-only evaluation; exact routing; native POV1 codec; feasibility/legality layers; full gear/jewel/scenario integration incomplete in that capture.

## Reproduce package checks

Run `python -B Path-of-Building-Research/analysis/build_evidence.py pob-source` from the parent directory with Python 3. The checkout must be at the pinned commit with the referenced sparse files present and no working-tree changes.

The script reads the checkout and writes only this vault's evidence and source index. It runs independent examples, not PoB or Valheiman code. Re-running replaces evidence timestamps. Package verification does not assert every linked GitHub page was fetched in a browser.

## Excluded work

No PoB runtime, LuaJIT installation, PoB tests, performance benchmark, game session, full source port, or modification/message to Claude. The sparse read-only checkout is outside the distributable vault. No raw Valheiman tables or community build codes are bundled.
