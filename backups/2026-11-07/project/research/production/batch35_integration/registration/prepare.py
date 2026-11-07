from pathlib import Path
import ast,datetime,difflib,hashlib,json,pprint,re,shutil
R=Path('/workspace/IntegratedMath-book');B=Path('/tmp/frc-rfs74-registration');O=Path('/tmp/frc-rfs-flc75-registration');H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P='research/production/';F='manuscript/foundations/'
assert H(B/'build_production_ledger.py')=='b0662c401fa9178c933e3ca6dd8514ec542e4b11b952c752273cfc1e5436b0e3'
assert H(B/'accepted_reviews.json')=='e7d81c9982bfb5f788b9f92b11aa413443432c99383759316cd6b8beefb84a85'
oldmeta=json.loads((B/'registration.json').read_text())
refresh={'tools/validate_learning_batch.py':{'previous':'10e0078b2c6a173f67162f40dd2febb2ceb86eb0bff3307961c6337b458e08f4','current':'14a36b325d52d9d1d8f3e3e597734aea399fa5f2969dd84cb8be85b14756ebaf','reason':'Read exact formal delta: URL-aware .md# validation preserves external HTTP(S) citations while rejecting leaked local links; no registration/source changes'}}
for p,h in oldmeta['baseline_sha256'].items():
 if p in refresh:assert h==refresh[p]['previous']and H(R/p)==refresh[p]['current']
 else:assert H(R/p)==h,p

body=F+'finite_coordinate_combinations.md';ans=F+'finite_coordinate_combinations_answers.md';src=P+'finite_coordinate_combinations_sources.json';plan=P+'finite_coordinate_combinations_plan.md';math=P+'finite_coordinate_combinations_math_review.md';ped=P+'finite_coordinate_combinations_pedagogy_review.md';author=P+'finite_coordinate_combinations_author_check.md';pres='local-inputs/pending-batch35/finite-linear-combinations-cache-preservation.json'
bind={body:'ca4a3c59579c94c587d520ee0b7f1333717de8b33d0969c1a4f96ccb7ae41cdd',ans:'a1d9e1db6dd0dac684b7719863b54d12b6bcc46ea771cbc94dd1836bda2cad8e'};assert all(H(R/p)==h for p,h in bind.items())
for p in [math,ped]:assert all(h in(R/p).read_text()for h in bind.values())
sourcedata=json.loads((R/src).read_text());preserved=json.loads((R/pres).read_text());assert H(R/plan)==sourcedata['plan']['sha256'];assert all(H(R/x['intended_path'])==x['sha256']for x in sourcedata['manuscripts'])
for name,h in preserved['files'].items():assert H(R/preserved['preserved_location']/name)==h
for row in sourcedata['records']:
 p=Path(row['cache']);p=R/p if not p.is_absolute()else R/preserved['preserved_location']/p.name
 assert H(p)==row['sha256']
for path,h in sourcedata['prerequisite_files'].items():assert H(R/F/Path(path).name)==h
base=O/'frc-rfs74-base';base.mkdir(exist_ok=True)
for p in B.iterdir():
 if p.is_file():shutil.copyfile(p,base/p.name)
anchors={}
for p in (R/'manuscript').rglob('*.md'):
 for a in re.findall(r'\{#([^}]+)\}',p.read_text()):anchors.setdefault(a,[]).append(str(p.relative_to(R)))
pr=[]
for a in re.findall(r'\]\(#([^)]*)\)',(R/body).read_text()):
 assert len(anchors[a])==1,(a,anchors[a])
 if a.startswith('flc-'):continue
 pair=[anchors[a][0],a]
 if pair not in pr:pr.append(pair)
rfs=[x for x in pr if x[0]==F+'finite_real_sums.md'];frc=[x for x in pr if x[0]==F+'finite_real_coordinates.md'];assert {a for p,a in rfs}=={'rfs-definition','rfs-prefix-table','rfs-linearity','rfs-concatenation','rfs-padding'}
spec=dict(parent_code='15Axx',parent_chapter_number=84,part_code='15-XX',msc_leaf_codes=['15A03'],msc_cross_reference_codes=[],module_ids=['linear-algebra'],code='B4.L2',number=75,title='有限坐标向量的线性组合',anchor='flc-unit',body=body,answers=ans,goals=['区分向量项数m与坐标数n，以合法的加权实数表和构造唯一组合向量','分别核两个零参数及一项两项与既有运算相容，不预用一般向量求和','逐坐标证明系数相加、两位置共同缩放及同型向量项相加','核同步拼接和固定坐标重编号，区分项索引与坐标索引并避免未经证明的重排换序','用具体表辨认表示不唯一和不可达，不提前使用张成、基、维数'],definitions=['flc-data','flc-definition'],proved=[['FLC1','flc-definition','加权实数表定义组合的合法唯一性、两零参数及一两项相容'],['FLC2','flc-coefficients','同向量表的系数逐项相加'],['FLC3','flc-scaling','共同标量放在系数或向量项两处的缩放及零数据'],['FLC4','flc-vector-addition','同型向量项逐点相加'],['FLC5','flc-concatenation','同切点同步拼接的组合公式'],['FLC6','flc-reindex','坐标重编号保持组合与双逆恢复，不重排向量项']],questions='flc-q',answer_prefix='flc-a',not_covered=['一般向量和递归、任意向量项置换不变及双重求和换序','张成、抽象向量空间、线性相关、基、维数、秩及lineability','矩阵、行列式及一般线性映射理论','整个15A03、第84章与linear-algebra模块'],prerequisites=pr,adopted_external=[[F+'finite_real_coordinates.md','frc-model','沿FRC公开采用的给定集合间函数集合存在和逐输入合法唯一构造背景；不新增集合公理证明']],source_records=[plan,src,author,math,ped])
for a in spec['definitions']+[x[1]for x in spec['proved']]+[spec['anchor']]:assert '{#'+a+'}'in(R/body).read_text()
for i in range(1,9):
 for p,pre in[(body,'flc-q'),(ans,'flc-a')]:assert(R/p).read_text().count('{#'+pre+f'{i:02}'+'}')==1
entries=json.loads((R/'data/msc_taxonomy.json').read_text())['entries'];ix={x['code']:x for x in entries};chap={x['code']:i+1 for i,x in enumerate(x for x in entries if x['level']=='intermediate')};assert ix['15A03']['parent_code']=='15Axx'and chap['15Axx']==84 and ix['15Axx']['parent_code']=='15-XX'
oldreviews=json.loads((B/'accepted_reviews.json').read_text());newreviews=[]
for stage,who,p in [('math-reviewed','/root/part1_audit',math),('pedagogy-reviewed','/root',ped)]:newreviews.append(dict(target_type='unit',target_id='flc-unit',stage=stage,scope='unit',status='accepted',reviewer=who,reviewed_at='2026-11-05',source_sha256=bind,evidence=[dict(path=p,sha256=H(R/p))],blocking_issues=[],limits='仅FLC最终两稿与八题全解的真实独立文本审阅；临时实读稿与正式安装稿字节一致。保留报告日精度；不授予分类叶/整章/模块完成或构建/视觉接受。'))
reviews={**oldreviews,'reviews':oldreviews['reviews']+newreviews};before=(B/'build_production_ledger.py').read_text();text=before
def replace(old,new):
 global text
 assert text.count(old)==1,(old,text.count(old));text=text.replace(old,new)
replace('# Each tuple: module id, stage, title, prerequisite module ids, MSC locating tags.',"# FLC candidate consumes precise FRC and RFS interfaces; keeps old learning identifiers.\nBRIDGE += "+repr([body,ans])+"\n# Each tuple: module id, stage, title, prerequisite module ids, MSC locating tags.")
replace("'linear-algebra':BRIDGE[144:146:2]","'linear-algebra':BRIDGE[144:146:2]+BRIDGE[148:150:2]")
replace("'scope': 'registered_real_coordinate_entry_unit_draft' if existing(root, planned) else 'none'", "'scope': 'registered_real_coordinate_and_combination_units_draft' if existing(root, planned) else 'none'")
replace("'written_topics': ['B4.L1有限实数坐标函数表、逐坐标运算规律、消去条件、重编号及二维模型连接'] if existing(root, planned) else []", "'written_topics': [topic for path, topics in [(BRIDGE[144], ['B4.L1有限实数坐标函数表、逐坐标运算规律、消去条件、重编号及二维模型连接']), (BRIDGE[148], ['B4.L2加权实数表构造有限坐标组合、两零参数、五项运算规则及具体表示边界'])] if existing(root, [path]) for topic in topics]")
replace("'unwritten_topics': ['向量线性组合（实数有限和接口由另模块B2.39提供）', '抽象向量空间与一般线性映射'", "'unwritten_topics': ['一般向量和递归、任意项重排与双重和换序', '张成、抽象向量空间与一般线性映射'")
replace("'boundary': '只登记15A03有限坐标入口；B4.L1为线性代数学习号，旧B4.1—B4.10分析编号不改；不授予模块或第84章完成'", "'boundary': '只登记15A03的B4.L1有限坐标和B4.L2具体线性组合局部；旧B4.1—B4.10分析编号不改；不授予模块或第84章完成'")
replace("['frc-model','frc-operations','frc-additive-laws','frc-scalar-laws','frc-cancellation','frc-reindex','frc-plane-compatibility']]", "['frc-model','frc-operations','frc-additive-laws','frc-scalar-laws','frc-cancellation','frc-reindex','frc-plane-compatibility']] + [\n                anchor_ref(root, BRIDGE[148], anchor) for anchor in ['flc-data','flc-definition','flc-coefficients','flc-scaling','flc-vector-addition','flc-concatenation','flc-reindex']]")
replace("'exact_unit_prerequisites': '见B4.L1逐锚登记；含实数域、经典量词否定、FCT5与旧二维模型，不能以模块概略图代替'", "'exact_unit_prerequisites': 'B4.L1沿原逐锚入口；B4.L2必须先有B4.L1及B2.39的实数和接口。模块图是概略规划，不能替代每单元精确先修，也不把整个实数方程模块当B4.L1先修'")
replace("'real_finite_sums_or_dimension_theorem_used': False", "'unit_dependency_interfaces': {'B4.L2': {'B4.L1': ['frc-model','frc-operations','frc-additive-laws','frc-scalar-laws','frc-reindex'], 'B2.39': ['rfs-definition','rfs-prefix-table','rfs-linearity','rfs-concatenation','rfs-padding']}, 'B2.39_module': 'real-algebra-equations'},\n                'real_finite_sums_used_by_B4_L2': True,\n                'dimension_theorem_used': False")
replace("'向量线性组合与抽象线性空间'", "'抽象线性空间（具体坐标组合由另模块B4.L2提供）'")
replace('def anchor_ref(root, path, anchor):','# FLC final reviewed source only; no further units pre-registered.\nUNIT_SPECS += '+pprint.pformat([spec],width=100,sort_dicts=False)+'\n\ndef anchor_ref(root, path, anchor):')
replace("status='finite_real_coordinate_entry_chapter_pending'", "status='finite_real_coordinate_combination_entries_chapter_pending'")
replace('仅B4.L1有限实数坐标与逐坐标运算、带条件消去、置换重编号及二维模型连接；实数有限和、抽象向量空间、线性相关、基、维数、秩、lineability、矩阵、一般线性映射、行列式及其余基础线性代数待写，第84章未完成','仅B4.L1有限实数坐标与逐坐标运算、带条件消去、置换重编号和二维模型连接，以及B4.L2有限坐标线性组合的构造与规则；实数有限和先修由第528章B2.39提供。张成、抽象向量空间、线性相关、基、维数、秩、lineability、矩阵、一般线性映射、行列式及其余基础线性代数待写，第84章未完成')
ast.parse(text)
def defs(s,p):
 ns={'__name__':'registration_definitions_only','__file__':str(p)};exec(compile(s,str(p),'exec'),ns);return ns
old=defs(before,B/'build_production_ledger.py');new=defs(text,O/'build_production_ledger.py');formal=defs((R/'tools/build_production_ledger.py').read_text(),R/'tools/build_production_ledger.py')
assert len(new['UNIT_SPECS'])==75 and new['UNIT_SPECS'][:74]==old['UNIT_SPECS']and new['UNIT_SPECS'][:72]==formal['UNIT_SPECS'];assert new['BRIDGE'][:148]==old['BRIDGE']and len(new['BRIDGE'])==150;assert new['MODULES']==old['MODULES'];assert len(reviews['reviews'])==150 and reviews['reviews'][:148]==oldreviews['reviews'];assert reviews['reviews'][:144]==json.loads((R/P/'accepted_reviews.json').read_text())['reviews']
u=new['unit_records'](R)[-1];assert u['code']=='B4.L2'and u['parent_chapter_number']==84 and u['unit_id']=='flc-unit'and u['exercise_answer_separation']['paired_ids_verified'];assert all(x['status']=='present'for x in u['learning_entry']['prerequisite_definition_anchors']);assert u['stages']['build-verified']['status']=='pending'
for rev in newreviews:assert rev['source_sha256']=={p:H(R/p)for p in u['source_files']}and all(H(R/e['path'])==e['sha256']for e in rev['evidence'])
(O/'build_production_ledger.py').write_text(text);(O/'accepted_reviews.json').write_text(json.dumps(reviews,ensure_ascii=False,indent=2)+'\n')
for name,a,b in [('flc_delta.diff',before,text),('build_production_ledger.diff',(R/'tools/build_production_ledger.py').read_text(),text),('accepted_reviews_flc_delta.diff',json.dumps(oldreviews,ensure_ascii=False,indent=2)+'\n',json.dumps(reviews,ensure_ascii=False,indent=2)+'\n')]:
 (O/name).write_text(''.join(difflib.unified_diff(a.splitlines(True),b.splitlines(True),fromfile='base/'+name,tofile='proposed75/'+name)))
basehash=oldmeta['baseline_sha256']|{p:v['current']for p,v in refresh.items()}|{p:H(R/p)for p in[body,ans,src,plan,math,ped,author,pres]+[p for p,a in pr]}
meta=dict(prepared_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),prepared_by='/root/part1_sources',status='temporary_candidate_not_applied',baseline_units=72,prior_candidate_units=74,expected_units=75,expected_foundation_pairs=600,expected_total_pairs=627,expected_text_reviews=150,unit_specs=oldmeta['unit_specs']+[spec],new_reviews=oldmeta['new_reviews']+newreviews,baseline_sha256=basehash,baseline_refresh=refresh,prior_candidate_sha256={n:H(B/n)for n in['build_production_ledger.py','accepted_reviews.json','registration.json']},module_title_change_inherited=oldmeta['module_title_change'],module_graph_decision={'new_edges':[],'root_approved':True,'reason':'Existing module graph explicitly broad; exact per-unit anchors and B4.L2→B2.39 interface mapping carry actual dependency without imposing whole real-algebra-equations module on B4.L1','FLC_RFS_interfaces':rfs,'FLC_FRC_interfaces':frc},cache_preservation={'record':pres,'sha256':H(R/pres),'original_source_metadata_unchanged':True,'raw_text_in_candidate':False,'local_verification_only_not_publication_dependency':True},excluded_drafts=[],naming='B4.L1, B2.39, B4.L2 in exact reading order; ordinal73,74,75; all previous codes unchanged')
(O/'registration.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
checks=dict(syntax='passed',old74_specs_preserved=True,formal72_specs_preserved=True,old148_bridge_paths_preserved=True,old148_text_reviews_preserved=True,module_graph_including_titles_unchanged_from74=True,module_title_change_from72_inherited_only=oldmeta['module_title_change'],FLC_RFS_dependency_interfaces_explicit=True,prerequisite_anchors_checked=len(pr),source_original_and_preserved_cache_hashes_match=True,review_reports_bind_installed_bytes=True,review_dates_retained_as_day_only=True,expected_units=75,expected_total_pairs=627,expected_text_reviews=150,formal_build_executed=False,formal_ledger_generation_executed=False,formal_files_modified=False,external_originals_copied_to_candidate=False)
assert all(H(R/p)==h for p,h in basehash.items());(O/'checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n');print(json.dumps(checks,ensure_ascii=False,indent=2))
