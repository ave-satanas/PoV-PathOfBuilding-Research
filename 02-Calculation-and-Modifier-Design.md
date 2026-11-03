---
id: calculation-and-modifiers
type: architecture-research
status: source-reviewed
tags: [pob, modifiers, provenance, calculations]
---

# Calculation and modifier design

## Reuse the separation of responsibilities

PoB's calculation setup builds an environment from build state, configuration, actors, equipment, allocated passives, and skills. A later calculation pass produces outputs. That separation is a useful reference for extending Claude's passive evaluator into a character evaluator without making the language model perform mechanical arithmetic. [Setup entry point](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/Modules/CalcSetup.lua#L470-L517).

**Proposed Valheiman flow:** resolve the request → validate supported inputs → construct effective allocation/equipment/scenario → assemble stats → apply verified hit/defence/recovery stages → evaluate the stated objective → attach evidence and limitations. Keep feasibility and legality distinct from performance. This is an adaptation proposal, not an extracted PoB algorithm.

## Keep provenance through evaluation

PoB modifiers have a name, stacking type, value, source, applicability flags, and condition tags. Its query layer can return values paired with their originating modifier. Claude already has structured `Mod`, `Gate`, and subject handling; replacing them would discard useful work. The transferable addition is retaining where a row came from and why it was or was not used. [Modifier syntax](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/docs/modSyntax.md), [tabulation](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/Classes/ModDB.lua#L278-L305).

A useful result for one stat would identify passive node/option or item slot, raw row, stacking form, subjects, gate outcome, source scaling, and evidence classification. Omitted effects need explicit reasons such as unsupported mechanic, inactive condition, incompatible subject, or missing live-state input. Add provenance only as far as needed to explain and debug the supported metric.

## Explain arithmetic and dependency order

`CalcBreakdown` constructs explanations for base amounts, increased/reduced terms, multiplicative terms, totals, and item-slot sources. It is a concrete example of producing explanations alongside calculations rather than asking an LLM to reconstruct a plausible formula afterward. [Breakdown builders](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/Modules/CalcBreakdown.lua#L13-L93).

For Valheiman, emit a small structured trace before formatting Markdown. An attribute-derived bonus should show the attribute total used and its derivation stage. A live-state-dependent effect should show its supplied state or the reason it remains uncomputed. Sum-of-sources output alone does not explain overrides, conversions, or stage-dependent calculations.

## Units need an explicit boundary

PoB's basic modifier helpers divide additive percentage values by 100; Valheiman's captured documentation says percentage stats use fractions such as 0.12. Similar modifier names do not imply compatible units or stacking semantics. If porting a small helper or writing a cross-engine arithmetic test, normalize units first and assert the conversion. [PoB arithmetic helpers](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/Modules/CalcTools.lua#L16-L39).

The checked synthetic example uses base 100, additive increases 20% and 30%, then multipliers 1.2 and 0.9: result **162**. It verifies a generic arithmetic convention only; it does not verify a Valheiman damage formula or execute PoB. Results are in [benchmarks.json](evidence/benchmarks.json).

## Prefer structured data over a new English parser

PoB documents a text-to-modifier pipeline with cached parsed output and handling of old wording. That solves its import/data needs. Claude's extracted structured rows already carry IDs, values, subjects, and conditions. Borrow parser observability and explicit unsupported status; defer copying the parser itself until a specific Valheiman import requires it. [Parser development guide](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/docs/addingMods.md).
