from pathlib import Path
import ast, copy, datetime, difflib, hashlib, json, pprint, re
R=Path('/workspace/IntegratedMath-book'); D=Path('/tmp/finite-coordinate-subspaces-draft'); O=Path('/tmp/fsp76-registration'); O.mkdir(exist_ok=True); BASE=O/'base'; BASE.mkdir(exist_ok=True)
H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def meta(text):
 t=ast.parse(text);ns={};nodes=[]
 for n in t.body:
  if isinstance(n,ast.Assign) and any(isinstance(x,ast.Name) and x.id in {'CH01','BRIDGE','MODULES','UNIT_SPECS'} for x in n.targets):nodes.append(n)
  elif isinstance(n,ast.AugAssign) and isinstance(n.target,ast.Name) and n.target.id in {'BRIDGE','UNIT_SPECS'}:nodes.append(n)
 exec(compile(ast.Module(body=nodes,type_ignores=[]),'metadata_only','exec'),ns);return ns
for p in ['tools/build_production_ledger.py','research/production/accepted_reviews.json']:
 target=BASE/Path(p).name
 if target.exists():assert H(target)==H(R/p),('baseline moved',p)
 else:target.write_bytes((R/p).read_bytes())
oldtext=(BASE/'build_production_ledger.py').read_text();old=meta(oldtext)
oldreviews=json.loads((BASE/'accepted_reviews.json').read_text())
assert len(old['UNIT_SPECS'])==75 and len(old['BRIDGE'])==150 and len(oldreviews['reviews'])==150
prefix='finite_coordinate_subspaces';body=f'manuscript/foundations/{prefix}.md';answers=f'manuscript/foundations/{prefix}_answers.md'
frozen={body:'d61775e91c706c45cf03b216ed16e0b03de8799926f51302815c51ffdf09fd97',answers:'93847c7812c470fb727c277edd5853ea64f0071b63ec4776c65ec9d8330f29dc'}
mapping=[]
for name in [prefix+'.md',prefix+'_answers.md',prefix+'_plan.md',prefix+'_sources.json',prefix+'_author_check.md',prefix+'_math_review.md',prefix+'_pedagogy_review.md']:
 intended=('manuscript/foundations/' if name in [prefix+'.md',prefix+'_answers.md'] else 'research/production/')+name
 assert not (R/intended).exists(),('must remain uninstalled for proposal',intended)
 mapping.append({'actual_path':str(D/name),'intended_path':intended,'sha256':H(D/name),'installed':False,'copy_policy':'future byte-for-byte copy; retain actual source metadata, no replacement of historical dates/paths'})
mapped={x['intended_path']:Path(x['actual_path']) for x in mapping}
for p,h in frozen.items():assert H(mapped[p])==h
assert H(D/(prefix+'_sources.json'))=='5294ed5cd06a2e10560d332d756e976d285ec73e9e3fb22a51664dc132e8d2e2'
assert H(D/(prefix+'_math_review.md'))=='e3b73d9a00a4ec19ef2fb1866960a6069949d901373458eb1a3280d8ab2ac11d'
assert H(D/(prefix+'_pedagogy_review.md'))=='ccac39e48c0a6c04dec335d80079ded55c474f599a1d7f88093e880d43250491'
anchors={}
for p in (R/'manuscript').rglob('*.md'):
 for a in re.findall(r'\{#([^}]+)\}',p.read_text()):anchors.setdefault(a,[]).append(str(p.relative_to(R)))
bodytext=mapped[body].read_text();anstext=mapped[answers].read_text()
preanchors=re.findall(r'\]\(#([^)]*)\)',bodytext.splitlines()[4])+['rfs-definition']
prereqs=[]
for a in preanchors:
 assert len(anchors.get(a,[]))==1,(a,anchors.get(a))
 prereqs.append([anchors[a][0],a])
sourcepaths=[x['intended_path'] for x in mapping if x['intended_path'].startswith('research/')]
spec={'parent_code':'15Axx','parent_chapter_number':84,'part_code':'15-XX','msc_leaf_codes':['15A03'],'msc_cross_reference_codes':[],'module_ids':['linear-algebra'],'code':'B4.L3','number':76,'title':'线性子空间与有限表的生成集合','anchor':'fsp-unit','body':body,'answers':answers,
 'goals':['在既有实V_n中定义三项子空间条件，证明非空版本、零坐标与空集边界并辨认闭合反例','以全量词长度归纳证明单项可能非零实数表和，不预用任意重排','由固定向量表的系数映射定义生成集合，给系数见证证明三项闭合及两空参数','构造单位系数表并逐坐标应用单项和引理，证明生成集合含每个合法向量项','对任意坐标数、子空间、向量表与系数表作项数归纳，用同步拼接证明包含意义下最小性','从已证含项与最小性推出同值集表生成相同，区别表记录、值集、生成集合及未定义维数'],
 'definitions':['fsp-subspace','fsp-generated-set'],
 'proved':[['FSP1','fsp-subspace','非空与三条件等价、负向量与差封闭及空集和V_0边界'],['FSP2','fsp-single-term-sum','指定位置可非零实数表和的完整长度归纳'],['FSP3','fsp-generated-set','有限表生成集合为子空间及空表/空坐标边界'],['FSP4','fsp-contains-entries','显式单位系数表证明含每个合法向量项'],['FSP5','fsp-minimality','全量词项数归纳证明最小子空间及唯一性'],['FSP6','fsp-same-range','同值集有限表生成相同，不依赖任意重排']],
 'questions':'fsp-q','answer_prefix':'fsp-a',
 'not_covered':['任意向量族的生成、子空间交与和、商空间及抽象向量空间理论','线性相关与无关、基、维数、秩、lineability、矩阵及高斯消元','任意有限项重排、双重求和换序与一般向量和递归','整个15A03、第84章及linear-algebra模块；不登记尚未写成和审签的后续单元'],
 'prerequisites':prereqs,
 'adopted_external':[[anchors['fun-sets'][0],'fun-sets','沿用给定集合与条件子集背景；不证明完整集合公理'],[anchors['frc-model'][0],'frc-model','沿FRC采用给定集合间函数记录集合及逐输入合法唯一构造背景'],[anchors['b1-induction'][0],'b1-induction','公开采用普通归纳原则，用于单项和及最小性；不重签为已构造规则']],
 'source_records':sourcepaths}
newtext=oldtext
def replace_once(a,b):
 global newtext
 assert newtext.count(a)==1,('replacement count',a,newtext.count(a));newtext=newtext.replace(a,b)
replace_once('# Each tuple: module id, stage, title, prerequisite module ids, MSC locating tags.',"# FSP proposal only: register after installing the exact reviewed temporary bytes.\nBRIDGE += "+repr([body,answers])+"\n# Each tuple: module id, stage, title, prerequisite module ids, MSC locating tags.")
replace_once("'linear-algebra':BRIDGE[144:146:2]+BRIDGE[148:150:2]","'linear-algebra':BRIDGE[144:146:2]+BRIDGE[148:150:2]+BRIDGE[150:152:2]")
replace_once("'scope': 'registered_real_coordinate_and_combination_units_draft'","'scope': 'registered_real_coordinate_combination_subspace_units_draft'")
replace_once("(BRIDGE[148], ['B4.L2加权实数表构造有限坐标组合、两零参数、五项运算规则及具体表示边界'])]","(BRIDGE[148], ['B4.L2加权实数表构造有限坐标组合、两零参数、五项运算规则及具体表示边界']), (BRIDGE[150], ['B4.L3具体V_n子空间三条件、单项和、有限表生成集合、含项与最小性、同值集不变'])]")
replace_once("'张成、抽象向量空间与一般线性映射'","'任意向量族的生成、子空间交与和、商空间、抽象向量空间与一般线性映射'")
replace_once('只登记15A03的B4.L1有限坐标和B4.L2具体线性组合局部','只登记15A03的B4.L1有限坐标、B4.L2具体线性组合及B4.L3具体子空间与有限表生成局部')
replace_once("for anchor in ['flc-data','flc-definition','flc-coefficients','flc-scaling','flc-vector-addition','flc-concatenation','flc-reindex']]", "for anchor in ['flc-data','flc-definition','flc-coefficients','flc-scaling','flc-vector-addition','flc-concatenation','flc-reindex']] + [\n                anchor_ref(root, BRIDGE[150], anchor) for anchor in ['fsp-subspace','fsp-single-term-sum','fsp-generated-set','fsp-contains-entries','fsp-minimality','fsp-same-range']]")
replace_once('B4.L2必须先有B4.L1及B2.39的实数和接口。模块图','B4.L2必须先有B4.L1及B2.39的实数和接口；B4.L3取既有FRC/RFS/FLC精确接口，先证单项和与最小性再证同值集不变。模块图')
interfaces={'B4.L1':['frc-model','frc-operations','frc-additive-laws','frc-scalar-laws'],'B2.39':['rfs-definition','rfs-prefix-table','rfs-concatenation','rfs-padding'],'B4.L2':['flc-definition','flc-coefficients','flc-scaling','flc-concatenation']}
replace_once("}, 'B2.39_module': 'real-algebra-equations'}", "}, 'B4.L3': "+repr(interfaces)+", 'B2.39_module': 'real-algebra-equations'}")
replace_once('def anchor_ref(root, path, anchor):', '# FSP reviewed finite-table subspace unit only; no FLI or later units pre-registered.\nUNIT_SPECS += '+pprint.pformat([spec],width=100,sort_dicts=False)+'\n\ndef anchor_ref(root, path, anchor):')
replace_once("status='finite_real_coordinate_combination_entries_chapter_pending'","status='finite_real_coordinate_combination_subspace_entries_chapter_pending'")
replace_once('以及B4.L2有限坐标线性组合的构造与规则；实数有限和先修由第528章B2.39提供。张成、抽象向量空间、线性相关','以及B4.L2有限坐标线性组合的构造与规则、B4.L3具体子空间与有限表生成的闭合/含项/最小性/同值集不变；实数有限和先修由第528章B2.39提供。任意向量族生成、子空间交与和、商空间、抽象向量空间、线性相关')
newreviews=copy.deepcopy(oldreviews);added=[]
for stage,reviewer,suffix in [('math-reviewed','/root/part1_audit','math_review'),('pedagogy-reviewed','/root','pedagogy_review')]:
 p=f'research/production/{prefix}_{suffix}.md';text=mapped[p].read_text()
 assert all(h in text for h in frozen.values())
 x={'target_type':'unit','target_id':'fsp-unit','stage':stage,'scope':'unit','status':'accepted','reviewer':reviewer,'reviewed_at':'2026-11-05','source_sha256':frozen.copy(),'evidence':[{'path':p,'sha256':H(mapped[p])}],'blocking_issues':[],'limits':'仅FSP最终临时两稿及八题全解的真实独立文字审阅。提案中正式路径尚未安装；须按映射逐字节安装并核hash后方可载入该审签。原读位置与日精度保留，不冒称重新全文审或build/visual通过；非完整15A03/第84章/模块。'}
 added.append(x)
newreviews['reviews']+=added
(O/'build_production_ledger.py').write_text(newtext);dump(O/'accepted_reviews.json',newreviews)
for name,olddata,newdata in [('build_production_ledger.py',oldtext,newtext),('accepted_reviews.json',(BASE/'accepted_reviews.json').read_text(),(O/'accepted_reviews.json').read_text())]:
 (O/(name+'.diff')).write_text(''.join(difflib.unified_diff(olddata.splitlines(True),newdata.splitlines(True),fromfile='formal75/'+name,tofile='proposed76/'+name)))
baseline={p:H(R/p) for p in ['tools/build_production_ledger.py','research/production/accepted_reviews.json','tools/build_learning_batch.py','tools/validate_learning_batch.py','data/msc_taxonomy.json','data/production/parts.json','data/production/chapters.json','research/production/part1_scope_plan.json','research/production/part1_topic_sources.json']}
for p,a in prereqs:baseline[p]=H(R/p)
source=json.loads((D/(prefix+'_sources.json')).read_text());caches=[]
for rec in source['records']:
 p=Path(rec['cache']);p=p if p.is_absolute() else R/p
 assert H(p)==rec['sha256'];caches.append({'actual_path':str(p),'sha256':H(p),'actual_read_ranges_in_original_record':rec['actual_read_ranges'],'scope':'hash rechecked here; full content reading was in the existing independent math/ped reports'})
new=meta(newtext);assert new['UNIT_SPECS'][:-1]==old['UNIT_SPECS'];assert new['BRIDGE'][:-2]==old['BRIDGE'];assert new['MODULES']==old['MODULES'];assert newreviews['reviews'][:-2]==oldreviews['reviews']
assert len(new['UNIT_SPECS'])==76 and len(new['BRIDGE'])==152 and len(newreviews['reviews'])==152
assert new['UNIT_SPECS'][-1]==spec and len(prereqs)==23
for i in range(1,9):assert bodytext.count('{#fsp-q'+f'{i:02}'+'}')==1 and anstext.count('{#fsp-a'+f'{i:02}'+'}')==1
for a in spec['definitions']+[x[1] for x in spec['proved']]:assert bodytext.count('{#'+a+'}')==1
order={s['body']:i for i,s in enumerate(new['UNIT_SPECS'])}
assert all(order[p]<75 for p,a in prereqs)
of={n.name:ast.dump(n,include_attributes=False) for n in ast.parse(oldtext).body if isinstance(n,ast.FunctionDef)};nf={n.name:ast.dump(n,include_attributes=False) for n in ast.parse(newtext).body if isinstance(n,ast.FunctionDef)}
changed=[n for n in of if of[n]!=nf.get(n)];assert set(changed)=={'prerequisite_data','build'}
taxonomy={x['code']:x for x in json.loads((R/'data/msc_taxonomy.json').read_text())['entries']};assert taxonomy['15A03']['parent_code']=='15Axx' and taxonomy['15Axx']['parent_code']=='15-XX'
chap=next(x for x in json.loads((R/'data/production/chapters.json').read_text())['entries'] if x['code']=='15Axx');assert chap['number']==84
checks={'status':'proposed_only_semantic_checks_passed','old75_specs_preserved':True,'old150_bridge_paths_preserved':True,'old150_reviews_preserved':True,'entire_MODULES_including_edges_unchanged':True,'candidate_units':76,'candidate_foundation_pairs':608,'candidate_total_pairs':635,'candidate_text_reviews':152,'new_prerequisite_anchors':23,'all_new_prerequisite_units_precede_FSP':True,'eight_pairs_and_six_proof_anchors_checked':True,'source_records_hash_bound_to_original_tmp_files':True,'actual_catalog_15A03_15Axx_15XX_and_chapter84_checked':True,'existing_functions_changed':changed,'all_other_existing_functions_AST_unchanged':True,'no_builder_or_validator_changes':True,'formal_files_modified':False,'formal_source_installation':False,'build_or_ledger_generation_executed':False,'FSP_text_reviews_only_no_build_acceptance':True,'FLI_or_other_later_units_registered':False}
dump(O/'checks.json',checks)
dump(O/'registration.json',{'prepared_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'prepared_by':'/root/part1_audit','status':'planned_not_applied','baseline_units':75,'expected_units':76,'expected_total_pairs':635,'expected_text_reviews':152,'unit_spec':spec,'new_reviews':added,'baseline_sha256':baseline,'actual_to_intended':mapping,'source_cache_identity':caches,'source_reading_policy':'Original sourceJSON actual /tmp locations and reading events retained byte-for-byte; this proposal does not retime or claim new source reading.','excluded':'FLI and all other subsequent drafts; possible future 77 proposal must extend this candidate explicitly and recheck baselines.'})
for p,h in baseline.items():assert H(R/p)==h,('formal baseline changed during preparation',p)
print(json.dumps(checks,ensure_ascii=False,indent=2))
