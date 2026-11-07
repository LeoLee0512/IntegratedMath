"""Read-only gate checks. Changed bindings are simulated in memory only."""
from pathlib import Path
from copy import deepcopy
import hashlib
import json
import sys

ROOT = Path('/workspace/IntegratedMath-book')
sys.path.insert(0, str(ROOT / 'tools'))
from validate_part1_acceptance import Validator

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def outcome(call):
    try:
        result = call()
        return {'passed': True, 'result': result}
    except Exception as exc:
        return {'passed': False, 'reason': str(exc)}

plan_path = 'research/production/part1_scope_plan.json'
ledger_path = 'research/production/part1_topic_sources.json'
follow = json.loads((ROOT/'research/production/part1_research_exposition_followup.json').read_text())
v = Validator(ROOT)
v.scope_plan(plan_path)
planned = deepcopy(v.section_plans['00-02'])
ledger = json.loads((ROOT/ledger_path).read_text())
old = next(x for x in ledger['sections'] if x['code'] == '00-02')
source = deepcopy(follow['proposed_source'])
access_evidence = 'research/production/part1_research_exposition_followup.json'
content_evidence = 'research/production/part1_research_exposition_followup.md'
source['access']['evidence'] = [{'path': access_evidence, 'sha256': sha(ROOT/access_evidence)}]
source['content_review'].update(
    reviewed_at=follow['reviewed_at_utc'],
    document_sha256=source['access']['document_sha256'],
    evidence=[{'path': content_evidence, 'sha256': sha(ROOT/content_evidence)}])
reviewed = {'code': '00-02', 'topic_source_status': 'verified', 'requirements': [
    {'requirement_id': '00-02-topic-source', 'status': 'verified',
     'source_ids': [source['id']]}]}
source_map = {source['id']: source}
results = {}
results['mapping_only_without_scope_update'] = outcome(lambda: v.topic_source_section(planned, reviewed, source_map))
planned['topic_source_status'] = 'verified'
results['complete_limited_source_mapping'] = outcome(lambda: v.topic_source_section(planned, reviewed, source_map))
bad = deepcopy(source)
bad['content_review']['coverage'][0]['relevance'] = 'general_method'
results['general_method_rejected'] = outcome(lambda: v.topic_source_section(planned, reviewed, {bad['id']:bad}))
bad = deepcopy(source)
bad['content_review']['coverage'][0]['objective_ids'] = ['00A30-1']
results['wrong_objective_rejected'] = outcome(lambda: v.topic_source_section(planned, reviewed, {bad['id']:bad}))
bad = deepcopy(source)
bad['content_review']['evidence'] = bad['access']['evidence']
results['access_as_content_review_rejected'] = outcome(lambda: v.topic_source_section(planned, reviewed, {bad['id']:bad}))

for mode in ['source_only', 'scope_only']:
    trial = Validator(ROOT)
    trial.scope_plan(plan_path)
    if mode == 'source_only':
        trial.sources['manuscript/review_ch01/part_opening.md'] = '0'*64
    else:
        trial.plan_hash = '0'*64
    checks = {}
    for stage in ['math','pedagogy']:
        checks[stage] = outcome(lambda stage=stage: trial.review('research/production/part1_'+stage+'_review.json', stage))
    checks['sources'] = outcome(lambda: trial.source_review(ledger_path))
    checks['build'] = outcome(lambda: trial.build_review('research/production/part1_build_review.json'))
    checks['visual'] = outcome(lambda: trial.visual_review('research/production/part1_visual_review.json'))
    results[mode+'_binding_simulation'] = checks

assert results['complete_limited_source_mapping']['passed']
for key in ['mapping_only_without_scope_update','general_method_rejected','wrong_objective_rejected','access_as_content_review_rejected']:
    assert not results[key]['passed'], key
for mode in ['source_only','scope_only']:
    assert all(not row['passed'] for row in results[mode+'_binding_simulation'].values())
results['boundary'] = 'Only the individual 00-02 requirement is tested as satisfiable; no complete-part attestation is issued or rewritten. Zero hashes simulate changed snapshots, not actual source revisions.'
results['input_hashes'] = {p: sha(ROOT/p) for p in [plan_path,ledger_path,access_evidence,content_evidence,'tools/validate_part1_acceptance.py','manuscript/review_ch01/part_opening.md']}
print(json.dumps(results, ensure_ascii=False, indent=2))
