"""Prepared for /root to review and execute after batch30 commit/snapshot.
This file has NOT been executed by its preparer. Preflight all inputs before writes.
"""
from pathlib import Path
from datetime import datetime, timezone
import ast
import copy
import hashlib
import json
import shutil
import subprocess
import sys

sys.dont_write_bytecode = True
repo = Path('/workspace/IntegratedMath-book')
candidate = Path('/tmp/batch31-integration')
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
def target(relative):
    path = repo / relative
    assert path.resolve().is_relative_to(repo.resolve()), relative
    return path
def copy_verified(source, relative, expected):
    assert sha(source) == expected, source
    destination = target(relative)
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    assert sha(destination) == expected, destination
    return {'path': relative, 'sha256': expected}
# Entire preflight is read-only. Require committed batch30 and its real snapshot.
head = subprocess.check_output(['git', '-C', str(repo), 'rev-parse', 'HEAD'], text=True).strip()
assert not subprocess.check_output(['git', '-C', str(repo), 'status', '--porcelain'], text=True).strip(), 'Commit/snapshot batch30 before installing31'
snapshot = repo / 'local-inputs/snapshots' / head[:7] / 'snapshot_manifest.json'
assert snapshot.is_file(), snapshot
snapshot_record = json.loads(snapshot.read_text())
assert snapshot_record['commit'] == head and snapshot_record['status'] == 'verified_local_snapshot'
assert len(snapshot_record['files']) == 6
for record in snapshot_record['files']:
    frozen = snapshot.parent / record['path']
    assert frozen.is_file() and sha(frozen) == record['sha256'] and frozen.stat().st_size == record['bytes'], frozen
delivery = json.loads((candidate / 'DELIVERY.json').read_text())
assert delivery['status'] == 'READY_for_root_review_and_integration'
for relative, expected in delivery['files'].items():
    assert sha(candidate / relative) == expected, relative
names = ['build_learning_batch.py', 'validate_learning_batch.py',
         'build_production_ledger.py', 'draw_foundations_batch.py']
for name in names:
    assert (repo / 'tools' / name).read_bytes() == (candidate / 'base_tools' / name).read_bytes(), name
for name, expected in json.loads((candidate / 'metadata_baseline_sha256.json').read_text()).items():
    assert sha(repo / name) == expected, name
source_json = candidate / 'research/production/real_sequences_order_subsequences_sources_2026-10-30.json'
source_md = source_json.with_suffix('.md')
assert not target('research/production/' + source_json.name).exists()
assert not target('research/production/' + source_md.name).exists()
audit = json.loads(source_json.read_text())
original_audit = copy.deepcopy(audit)
records = (audit['manuscript_binding']['manuscripts']
           + audit['manuscript_binding']['review_reports']
           + audit['manuscript_binding']['planning_evidence'])
for record in records:
    assert sha(Path(record['observed_path'])) == record['sha256']
    assert not target(record['intended_repository_path']).exists(), record['intended_repository_path']
for record in audit['original_source_audit']['sources']:
    cache = Path(record['cache_path'])
    assert sha(cache) == record['sha256'] and cache.stat().st_size == record['bytes']
for record in audit['original_log_binding']:
    assert sha(Path(record['path'])) == record['sha256']
assert (candidate / 'tools/draw_foundations_batch.py').read_bytes() == (candidate / 'base_tools/draw_foundations_batch.py').read_bytes()
accepted_path = repo / 'research/production/accepted_reviews.json'
accepted = json.loads(accepted_path.read_text())
assert len(accepted['reviews']) == 122
assert not any(x.get('target_id') in ['seqorder-unit', 'subseq-unit'] for x in accepted['reviews'])
for stem, target_id, reviewer in [('real_sequences_order', 'seqorder-unit', 'review22'),
                                  ('real_subsequences_bw', 'subseq-unit', 'plan_multiplication')]:
    hashes = [sha(Path('/tmp') / (stem + suffix + '.md')) for suffix in ['', '_answers']]
    for report in [stem + '_math_review.md', 'real_sequences_order_subsequences_pedagogy_review.md']:
        assert all(digest in (Path('/tmp') / report).read_text() for digest in hashes), report
for record in audit['current_prerequisite_recheck']:
    observed = next((Path(r['observed_path']) for r in audit['manuscript_binding']['manuscripts'] if r['intended_repository_path'] == record['intended_repository_path']), repo / record['intended_repository_path'])
    assert sha(observed) == record['sha256'], record['intended_repository_path']
print('Read-only preflight passed; installing the frozen31 candidate now.')

# Mutations begin here, only after every precondition above succeeded.
now = datetime.now(timezone.utc).isoformat()
installed = []
for name in names:
    source = candidate / 'tools' / name
    installed.append(copy_verified(source, 'tools/' + name, sha(source)))
for record in records:
    installed.append(copy_verified(Path(record['observed_path']), record['intended_repository_path'], record['sha256']))
for name in ['README.md', 'LEARNING_PATH.md']:
    source = candidate / 'metadata' / name
    installed.append(copy_verified(source, name, sha(source)))
for name in ['structural_check.json', 'DELIVERY.json']:
    source = candidate / name
    installed.append(copy_verified(source, 'research/production/batch31_' + name, sha(source)))

# Preserve source caches and original fetch logs locally with original bytes and dates.
# Do not change fetched_at fields or rewrite the embedded original source record.
durable = []
for record in audit['original_source_audit']['sources']:
    durable.append(copy_verified(Path(record['cache_path']),
        'local-inputs/pending-batch31/source-cache/' + record['id'], record['sha256']))
for index, record in enumerate(audit['original_log_binding']):
    durable.append(copy_verified(Path(record['path']),
        'local-inputs/pending-batch31/fetch-logs/' + str(index+1) + '-' + Path(record['path']).name,
        record['sha256']))
original_source = audit['original_log_binding'][0]
durable.append(copy_verified(Path(original_source['path']),
    'local-inputs/pending-batch31/original_plan_source_record.json', original_source['sha256']))
audit['root_integration'] = {
    'actor': '/root', 'checked_at_utc': now, 'prior_commit': head,
    'prior_snapshot_manifest': str(snapshot.relative_to(repo)),
    'candidate_json_sha256': sha(source_json), 'candidate_markdown_sha256': sha(source_md),
    'installed_files': installed, 'durable_local_evidence': durable,
    'existing_draw_module_byte_identical_to_prior': True,
    'new_network_requests': 0,
    'scope': 'Actual installation and byte verification only; no build or PDF acceptance. Original source-fetch history, retained unchanged, including earlier concept-review chronology.'}
audit['manuscript_binding']['formal_installation_verified'] = True
audit['formal_installation_verified'] = True
assert audit['original_source_audit']['sources'] == original_audit['original_source_audit']['sources']
assert audit['original_source_audit'] == original_audit['original_source_audit']
assert audit['original_log_binding'] == original_audit['original_log_binding']
source_json_target = target('research/production/real_sequences_order_subsequences_sources_2026-10-30.json')
source_json_target.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + '\n')
source_md_target = target('research/production/real_sequences_order_subsequences_sources_2026-10-30.md')
source_md_target.write_text(source_md.read_text() + '\n\n## 主编正式安装复核\n\n'
    + now + '，/root完成四稿、三份正文审阅、计划与概念报告的正式字节核验。四工具及两metadata严格对照已封存第30批精确基线；既有绘图模块字节不变。三个公开缓存及原HTTP对象完整保留，原取回时间未改。本批不新增图、数值代码或编号附录。候选隔离结构为63单元518题答21图28附录，7草稿章31草稿叶0完成；第28部分第242章40A05增至四个数列单元，B3仍未写。正式构建与PDF验收待进行，未将下游接受反写进来源。\n')

# Text acceptance only, authorized by root's actual full reading of these reports.
for stem, target_id, reviewer in [('real_sequences_order', 'seqorder-unit', 'review22'),
                                  ('real_subsequences_bw', 'subseq-unit', 'plan_multiplication')]:
    for stage, report_name, actor in [('math-reviewed', stem + '_math_review.md', reviewer),
                                     ('pedagogy-reviewed', 'real_sequences_order_subsequences_pedagogy_review.md', 'visual21_front')]:
        paths = ['manuscript/foundations/' + stem + suffix + '.md' for suffix in ['', '_answers']]
        report = 'research/production/' + report_name
        accepted['reviews'].append({
            'target_type': 'unit', 'target_id': target_id, 'stage': stage,
            'scope': 'unit', 'status': 'accepted',
            'reviewer': actor + '; root full text reading and exact migration review',
            'reviewed_at': now, 'source_sha256': {path: sha(repo / path) for path in paths},
            'evidence': [{'path': report, 'sha256': sha(repo / report)}],
            'blocking_issues': [],
            'limits': 'Independent full text and eight solutions reviewed; formal build and rendered-page acceptance pending; no complete classification chapter.'})
assert len(accepted['reviews']) == 126
accepted_path.write_text(json.dumps(accepted, ensure_ascii=False, indent=2) + '\n')
with (repo / 'PRODUCTION_PLAN.md').open('a') as handle:
    handle.write('\n第30批已本地提交并封存于 ' + head[:7]
        + '。第31批B4.3—B4.4数列序与子列四稿及完整题答已安装，63单元、518题答、21图、28附录仅文本与隔离结构审通过；第28部分第242章40A05四个数列单元，累计7草稿章31草稿叶0整章完成。比较、夹逼、单调收敛、最小指标递归的单调子列与实数数列BW已写；柯西、上/下极限、函数极限与级数仍未写。single-analysis仅部分草稿，B3课程仍未写，采用固定递归原则不等于形式基础完成。正式构建与PDF页面验收待完成。\n')
print('Installed31: four manuscripts, five review/plan reports, independent source pair, four tools and metadata; 126 text review records. Build/PDF acceptance pending.')
