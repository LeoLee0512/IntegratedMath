from pathlib import Path
import ast,copy,datetime,difflib,hashlib,json,pprint,re,shutil
R=Path('/workspace/IntegratedMath-book');B=Path('/tmp/frc73-registration');O=Path('/tmp/frc-rfs74-registration');H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P='research/production/';F='manuscript/foundations/'
assert H(B/'build_production_ledger.py')=='e7d1d0b3e20e890c95bcebb4b9a50e09227afeea2693e85896c2bdc34991d54d'
assert H(B/'accepted_reviews.json')=='05e09a25c6afd3c31e96e75a3a391ac6f06fd018b559e8b6e60b54ce81095eca'
oldmeta=json.loads((B/'registration.json').read_text());assert all(H(R/p)==h for p,h in oldmeta['baseline_sha256'].items())
body=F+'finite_real_sums.md';ans=F+'finite_real_sums_answers.md';src=P+'finite_real_sums_sources.json';plan=P+'finite_real_sums_linear_combinations_plan.md';math=P+'finite_real_sums_math_review.md';ped=P+'finite_real_sums_pedagogy_review.md';author=P+'finite_real_sums_author_check.md'
bind={body:'297dab2fc25bb32819ba662960ddd550a324d2594c8bf7a4e082c7b3f5ff573e',ans:'36ef43e22726ddec1cb2d79028272f284004a4aeadb3dc53620b0c15f3cb838f'};assert all(H(R/p)==h for p,h in bind.items())
for p in[math,ped]:assert all(h in(R/p).read_text()for h in bind.values())
sourcedata=json.loads((R/src).read_text());assert H(R/plan)==sourcedata['plan']['sha256'];assert all(H(R/x['cache_path'])==x['sha256']for x in sourcedata['records']);assert all(H(R/x['intended_path'])==x['sha256']for x in sourcedata['manuscripts'])
base=O/'frc73-base';base.mkdir(exist_ok=True)
for p in B.iterdir():
 if p.is_file():shutil.copyfile(p,base/p.name)
anchors={}
for p in(R/'manuscript').rglob('*.md'):
 for a in re.findall(r'\{#([^}]+)\}',p.read_text()):anchors.setdefault(a,[]).append(str(p.relative_to(R)))
pr=[]
for a in re.findall(r'\]\(#([^)]*)\)',(R/body).read_text()):
 assert len(anchors[a])==1,(a,anchors[a])
 if a.startswith('rfs-'):continue
 pair=[anchors[a][0],a]
 if pair not in pr:pr.append(pair)
# RFS6 explicitly uses i composed with q/b; the math report verifies FC3's type rule.
composition=[F+'functions_composition.md','fc-composition']
assert anchors['fc-composition']==[composition[0]]
if composition not in pr:pr.append(composition)
# Unlike FRC's comparison, old rational sum definitions ARE needed only by RFS6.
compat=[x for x in pr if x[1]in['sum-definition','sum-extensionality']]
spec=dict(parent_code='97Hxx',parent_chapter_number=528,part_code='97-XX',msc_leaf_codes=['97H20'],msc_cross_reference_codes=[],module_ids=['real-algebra-equations'],code='B2.39',number=74,title='有限实数和：递归、逐项规则与拼接',anchor='rfs-unit',body=body,answers=ans,goals=['从固定状态N×R更新构造唯一实数前缀和，区分空和、单项和及索引和值类型','证明前缀一致性、有限表零延拓合法及任意延拓同值','完整归纳证明逐项相加与固定实数缩放，逐步重组四项并核零负标量','核自然差与后段索引后证明连续拼接和尾补零，区分和值和函数记录相等','证明有理嵌入与新实数和相容，并用合法反例辨认逐项乘积错误'],definitions=['rfs-definition','rfs-prefix-table','rfs-linearity','rfs-concatenation'],proved=[['RFS1','rfs-definition','固定状态递归给实数部分和存在唯一'],['RFS2','rfs-prefix-table','前缀相等决定和值及有限表延拓独立'],['RFS3','rfs-linearity','逐项相加与固定实数缩放及有限表相容'],['RFS4','rfs-concatenation','移位与连续表拼接的完整索引及和值公式'],['RFS5','rfs-padding','零表和为零与尾补零保和值'],['RFS6','rfs-rational-compatibility','有理序列及有限表嵌入与实数和相容']],questions='rfs-q',answer_prefix='rfs-a',not_covered=['无限级数、部分和极限及任意有限重排','双重求和与换序、抽象群求和、一般向量和递归','有限坐标向量线性组合、基、维数与抽象线性空间','整个97H20初等代数教育、97Hxx及实数代数模块'],prerequisites=pr,adopted_external=[[F+'natural_numbers.md','b1-recursion-principle','公开采用的固定更新递归原则，用于N×R；不声称此处证明集合论递归定理'],[F+'natural_numbers.md','b1-induction','公开采用普通归纳原则以证明部分和规律'],[F+'functions_definition.md','fun-pairs','给定集合与集合积背景']],source_records=[plan,src,author,math,ped])
for a in spec['definitions']+[x[1]for x in spec['proved']]+[spec['anchor']]:assert '{#'+a+'}'in(R/body).read_text()
for i in range(1,9):
 for p,pre in[(body,'rfs-q'),(ans,'rfs-a')]:assert(R/p).read_text().count('{#'+pre+f'{i:02}'+'}')==1
entries=json.loads((R/'data/msc_taxonomy.json').read_text())['entries'];ix={x['code']:x for x in entries};chap={x['code']:i+1 for i,x in enumerate(x for x in entries if x['level']=='intermediate')};assert ix['97H20']['parent_code']=='97Hxx'and chap['97Hxx']==528 and ix['97Hxx']['parent_code']=='97-XX'
oldreviews=json.loads((B/'accepted_reviews.json').read_text());newreviews=[]
for stage,who,p in [('math-reviewed','/root/part1_audit',math),('pedagogy-reviewed','/root',ped)]:newreviews.append(dict(target_type='unit',target_id='rfs-unit',stage=stage,scope='unit',status='accepted',reviewer=who,reviewed_at='2026-11-05',source_sha256=bind,evidence=[dict(path=p,sha256=H(R/p))],blocking_issues=[],limits='仅有限实数和最终两稿及八题全解的真实独立文字审阅；已审稿与正式安装稿hash一致。保留原报告日精度；非有限坐标线性组合、整章/模块、构建或视觉验收。'))
reviews={**oldreviews,'reviews':oldreviews['reviews']+newreviews};before=(B/'build_production_ledger.py').read_text();text=before
oldtitle='实数方程与配方界';newtitle='实数代数：有限和、方程与配方界'
def replace(old,new):
 global text
 assert text.count(old)==1,(old,text.count(old));text=text.replace(old,new)
replace('# Each tuple: module id, stage, title, prerequisite module ids, MSC locating tags.',"# RFS candidate follows FRC in reading order; B2.39 is the stable learning identifier.\nBRIDGE += "+repr([body,ans])+"\n# Each tuple: module id, stage, title, prerequisite module ids, MSC locating tags.")
replace("('real-algebra-equations','B2','"+oldtitle+"'","('real-algebra-equations','B2','"+newtitle+"'")
replace("'real-algebra-equations':BRIDGE[108:110:2]","'real-algebra-equations':BRIDGE[108:110:2]+BRIDGE[146:148:2]")
replace("'unwritten_topics': ['实数有限和与线性组合', '抽象向量空间与一般线性映射'", "'unwritten_topics': ['向量线性组合（实数有限和接口由另模块B2.39提供）', '抽象向量空间与一般线性映射'")
replace("'scope': 'registered_real_quadratic_unit_draft' if existing(root, planned) else 'none'","'scope': 'registered_real_algebra_units_draft' if existing(root, planned) else 'none'")
replace("'written_topics': ['实数配方及判别式恒等式', '双向仿射换元与全部参数解集', '配方全局界与唯一达到输入'] if existing(root, planned) else []", "'written_topics': [topic for path, topics in [(BRIDGE[108], ['实数配方及判别式恒等式', '双向仿射换元与全部参数解集', '配方全局界与唯一达到输入']), (BRIDGE[146], ['B2.39固定状态递归实数有限和、前缀与延拓、逐项规则、连续拼接、补零及有理嵌入相容'])] if existing(root, [path]) for topic in topics]")
replace("'unwritten_topics': ['一般实形式多项式系统', '高次实方程和一般不等式系统', '微分与一般极值理论']", "'unwritten_topics': ['一般实形式多项式系统', '高次实方程和一般不等式系统', '任意实数有限和重排、双重和与无限级数', '向量线性组合与抽象线性空间', '微分与一般极值理论']")
replace("'note': '仅B2.34实际教学目标；这是学习模块，不新增分类章或叶。'", "'note': '仅B2.34与B2.39实际教学目标；B2.39主归97H20而非方程叶97H30，沿既有模块扩充实数代数局部，不新增模块、分类章或叶。'")
replace("'realquad-completion', 'realquad-discriminant', 'realquad-solutions', 'realquad-bounds']]", "'realquad-completion', 'realquad-discriminant', 'realquad-solutions', 'realquad-bounds']] + [\n                anchor_ref(root, BRIDGE[146], a) for a in ['rfs-definition','rfs-prefix-table','rfs-linearity','rfs-concatenation','rfs-padding','rfs-rational-compatibility']]")
replace("'entry_domain': '已构造的实数有序域及非负平方根；全部实数候选域'", "'entry_domain': 'B2.34使用实数有序域及非负平方根；B2.39只用自然规则、函数与实数加乘接口，不以平方根或二次方程为先修'")
replace("'note': '单向依赖functions的集合函数语言和number-systems的实数运算/平方根；不反向改变旧functions模块依赖。精确先修按单元锚定位，B2.34不依赖B2.31或B2.33；旧有理配方仅为结构对照。'", "'note': '保留单向依赖functions与number-systems；不把实数和塞回早期有理functions模块造成先修混淆。各单元精确锚独立登记；B2.34不依赖B2.31或B2.33，B2.39也不依赖B2.34或FRC。RFS6的旧有理求和定义仅用于嵌入相容，不能代替新实数和的构造。'")
replace('def anchor_ref(root, path, anchor):','# RFS only; finite coordinate linear combinations remain unregistered.\nUNIT_SPECS += '+pprint.pformat([spec],width=100,sort_dicts=False)+'\n\ndef anchor_ref(root, path, anchor):')
replace('实数二次方程与配方界十五个教学桥接；一般多项式除法','实数二次方程与配方界，以及B2.39有限实数和的递归、逐项规则、拼接及嵌入相容共十六个教学桥接；一般多项式除法')
ast.parse(text)
def defs(s,p):
 ns={'__name__':'registration_definitions_only','__file__':str(p)};exec(compile(s,str(p),'exec'),ns);return ns
old=defs(before,B/'build_production_ledger.py');new=defs(text,O/'build_production_ledger.py');formal=defs((R/'tools/build_production_ledger.py').read_text(),R/'tools/build_production_ledger.py')
assert len(new['UNIT_SPECS'])==74 and new['UNIT_SPECS'][:73]==old['UNIT_SPECS']and new['UNIT_SPECS'][:72]==formal['UNIT_SPECS'];assert new['BRIDGE'][:146]==old['BRIDGE']and len(new['BRIDGE'])==148
assert len(reviews['reviews'])==148 and reviews['reviews'][:146]==oldreviews['reviews'];assert reviews['reviews'][:144]==json.loads((R/P/'accepted_reviews.json').read_text())['reviews']
assert [m[:2]+m[3:]for m in old['MODULES']]==[m[:2]+m[3:]for m in new['MODULES']]
module_changes=[(a,b)for a,b in zip(old['MODULES'],new['MODULES'])if a!=b];assert len(module_changes)==1 and module_changes[0][0][0]=='real-algebra-equations'and module_changes[0][1][2]==newtitle
u=new['unit_records'](R)[-1];assert u['code']=='B2.39'and u['parent_chapter_number']==528 and u['unit_id']=='rfs-unit'and u['exercise_answer_separation']['paired_ids_verified'];assert all(x['status']=='present'for x in u['learning_entry']['prerequisite_definition_anchors']);assert u['stages']['build-verified']['status']=='pending'
for rev in newreviews:assert rev['source_sha256']=={p:H(R/p)for p in u['source_files']}and all(H(R/e['path'])==e['sha256']for e in rev['evidence'])
(O/'build_production_ledger.py').write_text(text);(O/'accepted_reviews.json').write_text(json.dumps(reviews,ensure_ascii=False,indent=2)+'\n')
for name,a,b in [('rfs_delta.diff',before,text),('build_production_ledger.diff',(R/'tools/build_production_ledger.py').read_text(),text),('accepted_reviews_rfs_delta.diff',json.dumps(oldreviews,ensure_ascii=False,indent=2)+'\n',json.dumps(reviews,ensure_ascii=False,indent=2)+'\n')]:
 (O/name).write_text(''.join(difflib.unified_diff(a.splitlines(True),b.splitlines(True),fromfile='base/'+name,tofile='proposed74/'+name)))
basehash=oldmeta['baseline_sha256']|{p:H(R/p)for p in[body,ans,src,plan,math,ped,author]+[p for p,a in pr]}
meta=dict(prepared_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),prepared_by='/root/part1_sources',status='temporary_candidate_not_applied',baseline_units=72,prior_candidate_units=73,expected_units=74,expected_foundation_pairs=592,expected_total_pairs=619,expected_text_reviews=148,unit_specs=oldmeta['unit_specs']+[spec],new_reviews=oldmeta['new_reviews']+newreviews,baseline_sha256=basehash,prior_candidate_sha256={n:H(B/n)for n in['build_production_ledger.py','accepted_reviews.json','registration.json']},module_title_change={'id':'real-algebra-equations','from':oldtitle,'to':newtitle,'root_approved':True,'id_stage_tags_and_edges_unchanged':True},rfs_compatibility_only_prerequisites=compat,excluded_drafts=['有限坐标向量线性组合'],naming='FRC B4.L1 then RFS B2.39 in reading order; ordinal registration numbers73,74; old learning codes unchanged')
(O/'registration.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
checks=dict(syntax='passed',old73_specs_preserved=True,formal72_specs_preserved=True,old146_bridge_paths_preserved=True,old146_text_reviews_preserved=True,module_ids_stages_tags_edges_unchanged=True,one_module_display_title_changed=meta['module_title_change'],prerequisite_anchors_checked=len(pr),rfs_rational_definitions_used_only_for_RFS6=True,source_caches_match_hashes=True,review_reports_bind_installed_bytes=True,expected_units=74,expected_total_pairs=619,expected_text_reviews=148,formal_build_executed=False,formal_ledger_generation_executed=False,formal_files_modified=False,unfrozen_drafts_registered=False)
assert all(H(R/p)==h for p,h in basehash.items());(O/'checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n');print(json.dumps(checks,ensure_ascii=False,indent=2))
