---
id: repository-readme
type: landing
status: ready-for-review
tags: [pob, pov, research]
---

# Path of Building research for Path of Valheiman

A separate Obsidian research vault investigating how Path of Building can inform development of the Path of Valheiman optimization tool.

**[Start here](00-Start-Here.md)** · [Contribution map](01-Contribution-Map.md) · [Claude handoff](08-Claude-Handoff.md) · [Findings ledger](evidence/findings.json)

Open this repository's root folder as an Obsidian vault. No plugins are required. Source citations are pinned to Path of Building commit `3dbca4463c0a59079d9f7f032d8240cf868e09da`; hashes and symbols are in [the source registry](evidence/sources.json).

The package contains architectural research and independent synthetic checks, not a PoB fork, runtime integration, or test of either game's mechanics. Historical statements about publication describe the research session before this repository was created.

To refresh source evidence and package checks with Python 3, from the repository root:

```text
python -B analysis/build_evidence.py <path-to-pinned-pob-checkout>
```

The source checkout must have the referenced files and be clean at the pinned revision. The script updates this vault's evidence and source index, without executing upstream code.
