---
id: pob-research-index
type: index
status: ready-for-review
created: 2026-11-02
tags: [pob, pov, optimization, research]
---

# What Path of Building can contribute

**Recommendation: use Path of Building as an architectural and testing reference. Extend the existing Python Valheiman engine; do not start by porting PoB or substituting its game formulas.** Its most useful contribution is a disciplined way to evaluate proposed changes, expose assumptions, explain results, and test interacting systems.

Research target: [PathOfBuildingCommunity/PathOfBuilding](https://github.com/PathOfBuildingCommunity/PathOfBuilding). Inspected revision: **`3dbca4463c0a59079d9f7f032d8240cf868e09da`**, commit dated 2026-10-30, from the `dev` branch. This is a development snapshot, not a claim about the installed release. References use that fixed revision.

## Reading map

| Note | Purpose |
|---|---|
| [[01-Contribution-Map]] | Prioritized mapping to Claude's existing modules |
| [[02-Calculation-and-Modifier-Design]] | Calculation phases, source provenance, units, and unsupported effects |
| [[03-Power-Reports-and-Search-Limits]] | Node/path value, comparisons, heuristics, and global-search limits |
| [[04-Build-State-and-Scenarios]] | Full-build manifests, saved assumptions, and progression sets |
| [[05-Jewels-and-Dependency-Changes]] | What PoB can teach about Dunin's unresolved second start |
| [[06-Testing-and-Performance]] | Headless tests, generated data checks, caching, and independent examples |
| [[07-Reuse-Decision-and-Roadmap]] | Practical reuse choices, license notice, and staged plan |
| [[08-Claude-Handoff]] | A concise future handoff with acceptance checks |
| [[90-Sources]] | Source registry with pinned links, symbols, hashes, and limits |

Machine entry points: [findings](evidence/findings.json), [source registry](evidence/sources.json), [checked examples](evidence/benchmarks.json), and [package verification](evidence/package-checks.json).

## Scope and confidence

This package is static source research plus independent mathematical examples. No PoB runtime, PoB test suite, game, or Claude optimizer code was executed. Claude's repository, reports, and session were not changed or contacted. The local comparison uses the earlier supplementary vault's captured Valheiman context; it is not a claim that Claude's active branch still has exactly that state.

The reviewed power-report and trade-weight paths provide local candidate evaluation, not a proof of globally optimal constrained builds. PoB also contains specialized search tools, including Timeless Jewel seed search and socket optimization; this research does not claim PoB has no optimization features. See [[03-Power-Reports-and-Search-Limits]].
