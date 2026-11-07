from pathlib import Path
import hashlib,json,copy,datetime,difflib,sys
R=Path('/workspace/IntegratedMath-book');O=Path('/tmp/editorial-plan-current-8-10')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads((R/p).read_text())
now=datetime.datetime.now(datetime.timezone.utc).isoformat();base=R/'data/editorial_plan.json';basehash=sha(base);old=load('data/editorial_plan.json');new=copy.deepcopy(old)
sp='research/production/part1_scope_plan.json';lp='research/production/part1_topic_sources.json';scope=load(sp);ledger=load(lp)
assert ledger['counts']=={'G_topic_verified':8,'G_topic_pending':10,'T_S_original_work_reviewed_separately':15}
assert ledger['plan_sha256']==sha(R/sp)
actual={p:sha(R/p) for p in scope['source_files']};assert actual==ledger['source_sha256']
idx={x['code']:x for x in scope['sections']};lidx={x['code']:x for x in ledger['sections']}
assert len(idx)==len(new['sections'])==33
oldstates=[]
for s in new['sections']:
 t=idx[s['code']];q=lidx[s['code']];assert t['topic_source_status']==q['topic_source_status']
 assert s['depth']==t['depth'] and s['learning_targets']==[o['text'] for o in t['objectives']]
 assert s['source']==t['body_source']+'#'+t['anchor']
 if s['topic_source_status']!=q['topic_source_status']:oldstates.append({'code':s['code'],'status':s['status'],'topic_source_status':s['topic_source_status']})
 s['topic_source_status']=q['topic_source_status'];s['author_review']='pending';s['production_acceptance_status']='pending';s['completed_at_declared_depth']=False
 if s['topic_source_status']=='verified':s['status']='专题来源已核；完整部分验收未通过；待作者审阅'
 elif s['topic_source_status']=='pending':s['status']='修订导读稿；专题来源待补；待作者审阅'
 else:s['status']='原创数学与教学已独立审读；完整部分验收未通过；待作者审阅'
new['unlisted_sections']={'depth':None,'status':'未在本第一部分局部编辑计划逐节列出；不代表全书未规划或未写','count':5973,'count_basis':'6006个分类节减去本文件列出的第一部分33节，仅为本文件未列项数量','coverage_authority':'data/production/','authority_records':['data/production/parts.json','data/production/chapters.json','data/production/sections.json','data/production/units.json']}
new['completion_note']='第一部分33节为T2/S13/G18修订审阅稿；当前正式scope与来源账为8个G专题来源已核、10个G待补，15个T/S原创工作由独立数学与教学审读负责。当前数学、教学报告绑定本稿；独立Part1构建与视觉报告仍绑定较早源稿，不能据其旧页数和通过状态认证含00B05新入口的当前稿。旧4/14记录、旧页数及旧绑定完整保留于editorial_state_history。完整部分保持pending，作者审阅pending，完整部分完成数仍为0。全书实际覆盖与规划以根目录data/production为准，本文件未列出的5973节不等于全书未规划。'
p=new['current_part'];p['plan_sha256']=sha(R/sp);p['source_review_sha256']=sha(R/lp)
p['source_status_counts']={'verified_G':8,'pending_G':10,'original_T_S_reviewed_separately':15}
p['verified_G_codes']=[x['code'] for x in ledger['sections'] if x['topic_source_status']=='verified'];p['pending_G_codes']=[x['code'] for x in ledger['sections'] if x['topic_source_status']=='pending']
p['stages'].update(automated_build='pending_current_revision',visual='pending_current_revision',author='pending',sources='pending');p['author_review']='pending'
p['pdf_page_counts']=None;p['build_record']=None;p['visual_review']=None
p['status_note']='当前稿数学/教学报告已绑定当前计划和八源；专题来源10项仍pending。独立Part1既有构建/视觉签与当前计划和源稿不匹配，其历史状态另存，不把旧产物当成本稿验收。基础续写批次的构建/视觉状态另以data/production/batch_validation.json及其实际绑定为准；不自动替代独立Part1整体验收。'
p['report_bindings']={}
observed={sp:sha(R/sp),lp:sha(R/lp)}
for kind in ['math','pedagogy','build','visual']:
 name='research/production/part1_'+kind+'_review.json';j=load(name);bound=j.get('plan_sha256')==sha(R/sp) and j.get('source_sha256')==actual
 p['report_bindings'][kind]={'path':name,'sha256':sha(R/name),'recorded_status':j['status'],'matches_current_plan_and_eight_sources':bound,'applies_to_current_revision':bound,'interpretation':'现有独立审读记录，非本次重新审签' if bound else '仅为历史版本记录；当前独立Part1该阶段待更新'}
 observed[name]=sha(R/name)
 if kind in ['math','pedagogy']:assert bound and j['status']=='accepted'
 else:assert not bound
p['exercises']=len({(v['question'],v['answer']) for s in scope['sections'] for v in s['exercise_answer_pairs']});assert p['exercises']==27
parts=load('data/production/parts.json');assert parts['checks']['completed_parts']==0
new['coverage_authority']={'path':'data/production/','scope':'全书现行部/章/节/教学单元覆盖账；本文件仅为第一部分33节的局部编辑状态','completed_parts':0,'completed_parts_basis':'data/production/parts.json checks.completed_parts；本次只核该值，未新验全书完成'}
new.setdefault('editorial_state_history',[]).append({'archived_at':now,'original_updated_on':old['updated_on'],'original_file_sha256':basehash,'applies_to_current_revision':False,'description':'原文件曾将旧4/14来源状态、50/267/218页和旧计划/来源绑定放在current字段；原值保留为历史，不重新认证这些产物，不适用于当前00B05修订稿。','completion_note_as_recorded':old['completion_note'],'current_part_as_recorded':old['current_part'],'unlisted_sections_as_recorded':old['unlisted_sections'],'changed_section_statuses_as_recorded':oldstates})
new['updated_on']='2026-11-05'
(O/'base_editorial_plan.json').write_bytes(base.read_bytes());(O/'editorial_plan.json').write_text(json.dumps(new,ensure_ascii=False,indent=2)+'\n')
(O/'editorial_plan.diff').write_text(''.join(difflib.unified_diff(base.read_text().splitlines(True),(O/'editorial_plan.json').read_text().splitlines(True),fromfile='base/data/editorial_plan.json',tofile='proposed/data/editorial_plan.json')))
sys.path.insert(0,str(R/'tools'));from build_learning_batch import source_hashes
inputs=source_hashes();manifest=load('build/learning_batch/build_inputs.json');assert len(inputs)==327 and inputs==manifest['source_sha256'] and 'data/editorial_plan.json' not in inputs
assert sha(base)==basehash
assert new['historical_completion_statement']==old['historical_completion_statement']
for a,b in zip(old['sections'],new['sections']):
 assert {k:v for k,v in a.items() if k not in ['status','topic_source_status']}=={k:v for k,v in b.items() if k not in ['status','topic_source_status']}
checks={'status':'passed_read_only_candidate_checks','prepared_at':now,'base_sha256':basehash,'candidate_sha256':sha(O/'editorial_plan.json'),'diff_sha256':sha(O/'editorial_plan.diff'),'observed_source_and_review_hashes':observed,'section_count':33,'changed_section_codes':[x['code'] for x in oldstates],'counts':p['source_status_counts'],'all_depths_objectives_anchors_unchanged':True,'all_section_source_statuses_match_current_scope_and_ledger':True,'author_pending_all_33':True,'all_completion_flags_false':True,'completed_parts':0,'old_historical_completion_statement_unchanged':True,'old_current_part_and_pages_preserved_exactly_in_history':True,'build_input_count':327,'build_manifest_sha256':sha(R/'build/learning_batch/build_inputs.json'),'computed_inputs_equal_build_manifest':True,'editorial_plan_is_build_input':False,'source_map_sha256':hashlib.sha256(json.dumps(inputs,sort_keys=True).encode()).hexdigest(),'no_formal_changes':True,'no_builds_or_network_requests':True}
(O/'checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:checks[k] for k in ['base_sha256','candidate_sha256','diff_sha256','changed_section_codes','build_input_count']},indent=2))
