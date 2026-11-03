"""Record pinned source evidence and verify this vault; never execute PoB or optimizer code."""
import argparse
import hashlib
import itertools
import json
import re
import subprocess
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path

VAULT = Path(__file__).resolve().parents[1]
COMMIT = '3dbca4463c0a59079d9f7f032d8240cf868e09da'
REPO_URL = 'https://github.com/PathOfBuildingCommunity/PathOfBuilding'
# IDs refer to exact files and checked symbols, not mutable branch links.
SOURCES = [
    ('S01', 'README.md', '### Features', 'Project feature overview'),
    ('S02', 'src/Modules/Calcs.lua', 'function calcs.getMiscCalculator(build)', 'Baseline and override evaluation'),
    ('S03', 'src/Modules/CalcSetup.lua', 'function calcs.initEnv(build, mode, override, specEnv)', 'Calculation environment and overrides'),
    ('S04', 'src/Classes/CalcsTab.lua', 'function CalcsTabClass:PowerBuilder()', 'Node, mastery, path and removal power'),
    ('S05', 'src/Classes/TreeTab.lua', 'function TreeTabClass:BuildPowerReportList(currentStat)', 'Path-normalized power report'),
    ('S06', 'src/Classes/PowerReportListControl.lua', 'function PowerReportListClass:PowerReportListControl', 'Power report columns and filters'),
    ('S07', 'src/Classes/TradeQueryGenerator.lua', 'function TradeQueryGeneratorClass.WeightedRatioOutputs', 'Weighted local output ratios and mod screening'),
    ('S08', 'src/Classes/ModDB.lua', 'function ModDBClass:TabulateInternal', 'Values paired with modifier provenance'),
    ('S09', 'src/Classes/ModStore.lua', 'function ModStoreClass:ModStore(parent)', 'Shared modifier store and actor/condition state'),
    ('S10', 'src/Modules/CalcBreakdown.lua', 'function breakdown.simple', 'Formula and slot breakdowns'),
    ('S11', 'docs/modSyntax.md', '### ModType', 'Modifier types, flags, sources and tags'),
    ('S12', 'docs/addingMods.md', 'ModParser', 'Text parsing, cached mods and unsupported text'),
    ('S13', 'src/Classes/ConfigTab.lua', 'function ConfigTabClass:Load(xml, fileName)', 'Saved configuration sets'),
    ('S14', 'src/Modules/ConfigOptions.lua', 'conditionMoving', 'Named player and enemy assumptions'),
    ('S15', 'src/Modules/Build.lua', 'self.savers = {', 'Build sections, versions and deferred tree loading'),
    ('S16', 'src/HeadlessWrapper.lua', 'function loadBuildFromXML', 'Headless application setup and build loaders'),
    ('S17', '.busted', 'exclude-tags', 'Default headless test selection'),
    ('S18', '.github/workflows/test.yml', 'busted --lua=luajit', 'Tests and regenerated modifier-cache check'),
    ('S19', 'spec/System/TestBuilds_spec.lua', 'expose("test all builds #builds"', 'Stored build-output regression loader'),
    ('S20', 'spec/System/TestOffence_spec.lua', 'Cooldown Recovery Rate', 'Interaction tests for skill rate limits'),
    ('S21', 'spec/System/TestRadiusJewelStatDiff_spec.lua', 'Thread of Hope removal comparison', 'Jewel access dependency comparisons'),
    ('S22', 'src/Classes/CompareTab.lua', 'function CompareTabClass:ComparePowerBuilder', 'Category-based build-element comparisons'),
    ('S23', 'src/Modules/CalcTools.lua', 'function calcLib.mod(modStore, cfg, ...)', 'Explicit percentage arithmetic'),
    ('S24', 'LICENSE.md', 'Copyright (c) 2016 David Gowor', 'Project and bundled-component notices'),
    ('S25', 'docs/rundown.md', 'Layout', 'Navigation guide; implementation takes precedence'),
    ('S26', 'src/Classes/SkillsTab.lua', 'Optimise Sockets', 'Example specialized optimizer'),
]


def dump(name, value):
    (VAULT / 'evidence' / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


def reachable(graph, selected):
    seen, stack = {'g'}, ['g']
    while stack:
        for node in graph[stack.pop()]:
            if node in selected and node not in seen:
                seen.add(node)
                stack.append(node)
    return selected <= seen


def subsets(values):
    for size in range(len(values) + 1):
        for group in itertools.combinations(values, size):
            yield set(group)


def benchmarks():
    normalized = Decimal(100) * (1 + (Decimal(20) + 30) / 100) * Decimal('1.2') * Decimal('0.9')
    assert normalized == 162
    graph = {'g': ['x', 'y'], 'x': ['g'], 'y': ['g']}
    utility = lambda nodes: 10 if {'x', 'y'} <= nodes else 0
    candidates = [s for s in subsets(['x', 'y']) if len(s) <= 2 and reachable(graph, s)]
    optimum = max(candidates, key=lambda s: (utility(s), tuple(sorted(s))))
    current = set()
    while True:
        additions = [(utility(current | {n}) - utility(current), n) for n in ('x', 'y') if n not in current]
        if not additions or len(current) == 2:
            break
        gain, node = max(additions)
        if gain <= 0:
            break
        current.add(node)
    assert utility(current) == 0 and utility(optimum) == 10 and len(candidates) == 4
    paths = [{'a', 'x'}, {'a', 'y'}]
    union = set.union(*paths)
    assert sum(map(len, paths)) == 4 and len(union) == 3
    raw_delta = 4 - 5
    oriented_delta = -raw_delta
    assert raw_delta == -1 and oriented_delta == 1
    # Check the tiny oracle itself handles unreachable nodes and a free root.
    assert not reachable(graph, {'missing'}) and reachable(graph, set())
    return {'classification': 'synthetic-independent-not-game-outputs', 'checks_passed': 4,
            'units': {'base': 100, 'inc_percentage_points': [20, 30], 'more_factors': [1.2, 0.9], 'result': str(normalized)},
            'synergy': {'graph': graph, 'budget': 2, 'objective': '10 iff x and y are both selected; otherwise 0',
                        'candidates_enumerated': len(candidates), 'greedy_policy': 'accept only strictly positive single-node immediate gains',
                        'greedy_nodes': sorted(current), 'greedy_value': utility(current),
                        'exact_nodes': sorted(optimum), 'exact_value': utility(optimum)},
            'shared_path': {'paths': [sorted(s) for s in paths], 'separate_cost': 4, 'union': sorted(union), 'union_cost': 3},
            'metric_direction': {'metric': 'delay', 'direction': 'minimize', 'a': 5, 'b': 4,
                                 'raw_delta_b_minus_a': raw_delta, 'oriented_improvement': oriented_delta}}


def finding_ledger():
    rows = [
        ('P01', 'adopt-pattern', 'high', 'Source-aware calculation explanations', ['S08', 'S10', 'S11'], ['stats.py', 'character.py'],
         'Emit selected-metric provenance and omitted-effect reasons.', 'No copied game formulas; do not replace existing verified stat assembly.'),
        ('P02', 'adopt-pattern', 'high', 'Persist explicit scenario assumptions', ['S13', 'S14'], ['evaluate.py', 'future build manifest'],
         'Start with one supported scenario and context identity.', 'Configured state is not evidence of actual uptime.'),
        ('P03', 'adopt-pattern', 'high', 'Keep full build state separate from passive code', ['S15'], ['buildcode.py', 'future build manifest'],
         'Preserve native POV1 plus versioned supported gear/skill/scenario state.', 'PoB XML is not compatible with POV1 or a proposed Valheiman manifest.'),
        ('P04', 'adopt-pattern', 'high', 'Evaluate complete path packages and choices', ['S04', 'S05', 'S06'], ['evaluate.py', 'passives.py'],
         'Show total delta, incremental cost and per-point change after legality checks.', 'Local path impact is not a global optimum; overlapping paths require union accounting.'),
        ('P05', 'defer-until-items', 'medium', 'Use local weights only for screening', ['S07', 'S22'], ['future item evaluator'],
         'Shortlist item/affix candidates, then fully recalculate finalists.', 'Synergies, caps and trade-offs make marginal weights context-dependent.'),
        ('P06', 'adopt-test-pattern', 'high', 'Build and interaction regression fixtures', ['S17', 'S18', 'S19', 'S20'], ['tests', 'native probes', 'mutation gate'],
         'Add explicit complete-input fixtures and generated-report/data checks.', 'Saved expected outputs are regression evidence, not an independent game oracle.'),
        ('P07', 'research-mechanics-first', 'high', 'Access-changing jewel dependencies', ['S03', 'S15', 'S21'], ['passives.py', 'validate.py', 'future jewel model'],
         'Trace native access grants and add removal/replacement tests.', 'PoE jewel mechanics cannot establish Dunin legality.'),
        ('P08', 'defer-until-profiled', 'medium', 'Memoization and bounded background work', ['S02', 'S04'], ['future search engine'],
         'Test cold/warm equivalence and context invalidation before caching.', 'Never reuse by mod identity alone across different contexts.'),
        ('P09', 'do-not-integrate-by-default', 'high', 'Reference architecture is preferable to a runtime bridge', ['S16', 'S03', 'S23'], ['existing Python engine'],
         'Adapt focused ideas; retain Valheiman formulas and units.', 'The headless wrapper still loads the PoB application and PoE data model.'),
        ('P10', 'reuse-notice', 'when-copying-code', 'Preserve source notices when actually reusing implementation', ['S24'], ['future copied or ported files'],
         'Record upstream revision and retain applicable notices.', 'Top-level source notice does not establish rights to every game asset.'),
    ]
    return {'schema_version': 1, 'pob_commit': COMMIT, 'findings': [
        dict(id=i, disposition=d, priority=p, title=t, source_ids=s, valheiman_targets=v,
             next_action=a, limitation=l, status='research-proposal-not-implemented')
        for i, d, p, t, s, v, a, l in rows]}


def verify_vault(source_ids):
    notes = list(VAULT.glob('*.md'))
    ids = set()
    wiki_count = 0
    for note in notes:
        text = note.read_text(encoding='utf-8')
        assert text.startswith('---\n'), note
        match = re.search(r'^id: (.+)$', text, re.M)
        assert match and match[1] not in ids, note
        ids.add(match[1])
        for target in re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', text):
            assert (VAULT / (target + '.md')).is_file(), (note, target)
            wiki_count += 1
        for target in re.findall(r'\]\(([^)]+)\)', text):
            if target.startswith(('https://', '#')):
                continue
            assert (note.parent / target.split('#')[0]).is_file(), (note, target)
    for finding in json.loads((VAULT / 'evidence/findings.json').read_text())['findings']:
        assert set(finding['source_ids']) <= source_ids, finding['id']
    for file in (VAULT / 'evidence').glob('*.json'):
        json.loads(file.read_text(encoding='utf-8'))
    return {'markdown_notes': len(notes), 'unique_note_ids': len(ids), 'wikilinks_checked': wiki_count,
            'relative_links': 'PASS', 'json': 'PASS', 'source_references': 'PASS'}


def main(repo):
    actual = subprocess.check_output(['git', '-C', str(repo), 'rev-parse', 'HEAD'], text=True).strip()
    assert actual == COMMIT, ('unexpected source revision', actual)
    assert not subprocess.check_output(['git', '-C', str(repo), 'status', '--porcelain'], text=True).strip()
    (VAULT / 'evidence').mkdir(exist_ok=True)
    sources = []
    for sid, path, anchor, purpose in SOURCES:
        raw = (repo / path).read_bytes()
        lines = raw.decode('utf-8-sig').splitlines()
        locations = [i for i, line in enumerate(lines, 1) if anchor in line]
        assert locations, ('missing source anchor', sid, path, anchor)
        start = locations[0]
        sources.append(dict(id=sid, path=path, symbol_or_anchor=anchor, line=start,
                            url=f'{REPO_URL}/blob/{COMMIT}/{path}#L{start}', purpose=purpose,
                            sha256=hashlib.sha256(raw).hexdigest(), bytes=len(raw)))
    dump('sources.json', {'schema_version': 1, 'captured_utc': datetime.now(timezone.utc).isoformat(),
                           'repository': REPO_URL, 'branch_observed': 'dev', 'commit': COMMIT,
                           'method': 'static source inspection; no upstream code executed', 'sources': sources})
    dump('benchmarks.json', benchmarks())
    dump('findings.json', finding_ledger())
    source_note = ['---', 'id: source-registry', 'type: sources', 'status: pinned-and-hashed',
                   'tags: [pob, sources, reproducibility]', '---', '', '# Source registry', '',
                   f'Revision: `{COMMIT}`. Hashes and precise anchors: [sources.json](evidence/sources.json).', '',
                   'Implementation observations take precedence over potentially older documentation. These links establish PoB behavior; all Valheiman adaptations are proposals.', '']
    for source in sources:
        source_note += [f'## {source["id"]}', '', f'[{source["path"]}]({source["url"]}) — {source["purpose"]}.', '',
                        f'Anchor: `{source["symbol_or_anchor"]}`; line {source["line"]}.', '']
    source_note += ['## Local Valheiman comparison context', '',
                    'The comparison uses the prior supplementary vault, captured at 2026-11-03T00:48:09Z, and its source manifest. It is a dated reference, not a fresh audit of Claude\'s active repository.', '',
                    'Known context: Python stat and character assembly; passive-only evaluation; exact routing; native POV1 codec; feasibility/legality layers; full gear/jewel/scenario integration incomplete in that capture.', '',
                    '## Reproduce package checks', '',
                    'Run `python -B Path-of-Building-Research/analysis/build_evidence.py pob-source` from the parent directory with Python 3. The checkout must be at the pinned commit with the referenced sparse files present and no working-tree changes.', '',
                    'The script reads the checkout and writes only this vault\'s evidence and source index. It runs independent examples, not PoB or Valheiman code. Re-running replaces evidence timestamps. Package verification does not assert every linked GitHub page was fetched in a browser.', '',
                    '## Excluded work', '',
                    'No PoB runtime, LuaJIT installation, PoB tests, performance benchmark, game session, full source port, or modification/message to Claude. The sparse read-only checkout is outside the distributable vault. No raw Valheiman tables or community build codes are bundled.', '']
    (VAULT / '90-Sources.md').write_text('\n'.join(source_note), encoding='utf-8')
    # Create the verification target before validating links to it.
    dump('package-checks.json', {})
    result = verify_vault({s['id'] for s in sources})
    result.update(pob_commit=COMMIT, source_anchors_checked=len(sources), synthetic_checks_passed=4,
                  upstream_runtime_executed=False, claude_repository_modified=False)
    dump('package-checks.json', result)
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('repo', type=Path)
    main(parser.parse_args().repo)
