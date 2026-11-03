---
id: testing-and-performance
type: engineering-research
status: source-reviewed-and-synthetic-checks-passed
tags: [pob, testing, headless, performance]
---

# Testing and performance lessons

## Headless does not mean a small standalone library

PoB provides `HeadlessWrapper.lua`, stubs host graphics functions, loads its application, and exposes build-loading helpers. It recommends LuaJIT. The wrapper still depends on launch/data/modules and runtime libraries; a sparse source download alone is not an executable evaluator. It is not a drop-in Python API or a Valheiman calculation service. [Wrapper](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/HeadlessWrapper.lua).

**Recommendation:** keep Claude's Python/JSON CLI path headless and deterministic. Use PoB's wrapper as an example of exercising real application calculations without a GUI. Do not add a Lua bridge merely to reuse structural ideas.

## Layer the tests

PoB's default Busted configuration uses the headless wrapper and excludes the `builds` tag. A separate build test loader checks stored expected outputs, rounding numeric comparisons to four places. Therefore the existence of saved-build tests does not mean the default invocation runs them. [Busted configuration](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/.busted), [saved build tests](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/spec/System/TestBuilds_spec.lua).

The offence suite includes direct scenarios that vary cooldown recovery and check resulting speed/DPS relationships. This is a useful model for interaction tests rather than only isolated arithmetic checks. Its expected values belong to PoE, not Valheiman. [Offence tests](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/spec/System/TestOffence_spec.lua#L18-L81).

PoB CI runs Busted and separately regenerates the modifier cache, then fails if the generated cache differs. Claude can adapt the generated-artifact consistency check to extracted tables or deterministic reports. Keep its existing native probes, brute-force routing checks, and mutation gate; PoB's test results are not an independent oracle for another game's rules. [CI workflow](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/.github/workflows/test.yml).

## Cache after correctness

PoB's node-power builder memoizes equivalent modifier effects within a run and yields periodically to report progress. Borrow bounded work and explicit cancellation/progress for long searches. Do not use modifier identity alone as a cross-build cache key: gate access, choices, scenario, gear and state can affect the result. [Power-builder cache and yield](https://github.com/PathOfBuildingCommunity/PathOfBuilding/blob/3dbca4463c0a59079d9f7f032d8240cf868e09da/src/Classes/CalcsTab.lua#L496-L740).

Cold evaluation should equal warmed evaluation, and visiting candidates in a different order must not change the result. Re-evaluating A after B should reproduce A. Measure time and cache hits on a fixed, representative candidate corpus before adopting incremental complexity.

## Checks executed for this vault

The standard-library script [build_evidence.py](analysis/build_evidence.py) records source hashes and asserts four independent examples:

| Check | Result | What it establishes |
|---|---|---|
| Percentage normalization | 100 × 1.5 × 1.2 × 0.9 = 162 | A small unit-conversion/stacking fixture |
| Two-node synergy | Positive-immediate-gain greedy = 0; exhaustive = 10 | A stated greedy policy can miss interactions |
| Shared bridge cost | Two separate path costs sum to 4; union cost = 3 | Package costs need shared-node accounting |
| Direction metadata | Delay 5 → 4 improves a minimize objective | Raw positive delta is not universally desirable |

These are mathematical checks, not PoB execution, performance measurements, gameplay validation, or a test of Claude's code. Source anchor checks and vault/link verification are recorded separately in [package-checks.json](evidence/package-checks.json).
