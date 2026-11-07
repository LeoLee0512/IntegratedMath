import json,hashlib,re,difflib,copy
from pathlib import Path
from datetime import datetime,timezone
R=Path('/workspace/IntegratedMath-book'); P=Path('/tmp/part1-abstract-proposed')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((P/'manifest.json').read_text()); checks={}; artifacts={}
for path,h in m['base_hashes'].items():
 assert sha(R/path)==h==sha(P/'base'/path)
 assert sha(P/path)==m['proposed_hashes'][path]
 artifacts[path]={'base_sha256':h,'proposal_sha256':sha(P/path)}
checks['four_baselines_equal_current_formal_bytes']=True
for path,h in m['supporting_evidence_hashes'].items():assert sha(R/path)==h
checks['supporting_evidence_hashes_match']=True
oldscope=json.loads((R/'research/production/part1_scope_plan.json').read_text());newscope=json.loads((P/'research/production/part1_scope_plan.json').read_text());restored=copy.deepcopy(newscope)
ss=[s for s in restored['sections'] if s['code']=='00B05'];assert len(ss)==1 and ss[0]['topic_source_status']=='verified';ss[0]['topic_source_status']='pending';assert restored==oldscope
checks['scope_only_00B05_status_changes_all_objectives_unchanged']=True
old=json.loads((R/'research/production/part1_topic_sources.json').read_text());new=json.loads((P/'research/production/part1_topic_sources.json').read_text())
assert new['sources'][:-1]==old['sources'] and len(new['sources'])==len(old['sources'])+1
assert [s for s in old['sections'] if s['code']!='00B05']==[s for s in new['sections'] if s['code']!='00B05']
assert new['blocking_issues']==[x for x in old['blocking_issues'] if x['section_code']!='00B05']
assert new['status']=='pending' and len(new['blocking_issues'])==10
assert new['revision_history'][:-1]==old['revision_history']
checks['old_source_records_and_other32_section_states_unchanged']=True
checks['pending10_and_previous_history_preserved']=True
assert new['plan_sha256']==sha(P/'research/production/part1_scope_plan.json')
for path,h in new['source_sha256'].items():assert sha(P/path if (P/path).exists() else R/path)==h
checks['eight_projected_source_bindings_match']=True
for path in ['manuscript/review_ch01/part_opening.md','manuscript/review_ch01/chapter.md','manuscript/review_ch01/answers.md','manuscript/review_ch02/answers.md','tools/ch01_simulation.py','tools/draw_ch01_figures.py']:
 assert old['source_sha256'][path]==new['source_sha256'][path]==sha(R/path)
checks['mathematical_ch1_and_both_answer_files_unchanged']=True
ch='manuscript/review_ch02/chapter.md';b=(R/ch).read_text();n=(P/ch).read_text()
start='### 本章阅读核验练习 {#ch02-exercises}'
assert b[b.index(start):]==n[n.index(start):]
assert re.findall(r'\$.*?\$',b,re.S)==re.findall(r'\$.*?\$',n,re.S)
checks['chapter2_all7_exercises_and_math_delimiters_byte_identical']=True
app='manuscript/review_ch01/appendices.md';a=(P/app).read_text();base=(R/app).read_text()
assert re.findall(r'\]\(#[^)]+\)',a)==re.findall(r'\]\(#[^)]+\)',base)
assert '见第二章来源说明[C2-S3]' in a and '(#ch02-sources)' not in a
assert n.count('{#ch02-sources}')==1
checks['appendix_plaintext_reference_adds_no_cross_chapter_anchor']=True
for kind in ['math','pedagogy']:
 q=R/f'research/production/part1_{kind}_review.json';r=json.loads(q.read_text());assert r['plan_sha256']==sha(R/'research/production/part1_scope_plan.json')
 for path,h in r['source_sha256'].items():assert sha(R/path)==h
 for e in r['evidence']:assert sha(R/e['path'])==e['sha256']
 artifacts[f'research/production/part1_{kind}_review.json']={'sha256':sha(q),'role':'current baseline evidence only; does not sign proposed change'}
checks['current_math_ped_bound_baseline_and_evidence_valid']=True
out={'reviewer':'/root/part1_audit','reviewed_at':datetime.now(timezone.utc).isoformat(),'status':'proposal_delta_passed_not_applied','formal_signature_written':False,'scope':'independent mathematics and pedagogy exact delta only','checks':checks,'artifacts':artifacts,'proposal_manifest_sha256':sha(P/'manifest.json'),'source_ids_added':[new['sources'][-1]['id']],'blockers':[],'counts_proposed':new['counts'],'full_part_status':'pending','author_review':newscope['author_review']}
(P/'independent_math_pedagogy_delta_review.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
