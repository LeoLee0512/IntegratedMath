from pathlib import Path
import ast,copy,datetime,hashlib,json,re,sys,types
R=Path('/workspace/IntegratedMath-book');O=Path('/tmp/batch35-builder-candidate');G=Path('/tmp/frc-rfs-flc75-registration');H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
b=ast.parse((O/'build_learning_batch.py').read_text());v=ast.parse((O/'validate_learning_batch.py').read_text());nodes=[]
names={'UNITS','EDUCATION_UNITS','ANALYSIS_UNITS','B3_UNITS','FINITE_COORDINATE_UNITS','CLASSIFIED_UNITS'}
for n in b.body:
 if isinstance(n,ast.Assign)and any(isinstance(t,ast.Name)and t.id in names for t in n.targets):nodes.append(n)
 if isinstance(n,ast.AugAssign)and isinstance(n.target,ast.Name)and n.target.id in names:nodes.append(n)
 if isinstance(n,ast.FunctionDef)and n.name in ['hashes','check_batch35_prerequisites']:nodes.append(n)
ns={'ROOT':R,'Path':Path,'hashlib':hashlib,'json':json};exec(compile(ast.Module(body=nodes,type_ignores=[]),'exact_guard_metadata','exec'),ns)
def register(p):
 m=types.ModuleType('build_production_ledger');m.__file__=str(p);exec(compile(p.read_text(),str(p),'exec'),m.__dict__);sys.modules[m.__name__]=m;return m
m=register(G/'build_production_ledger.py');original=copy.deepcopy(m.UNIT_SPECS);ns['check_batch35_prerequisites']();results={'actual75_candidate_with_actual_8_10_ledger':'passed'}
def reject(name,fn):
 try:fn()
 except (ValueError,AssertionError)as e:results[name]={'rejected':True,'message':str(e)}
 else:raise AssertionError(name+' did not reject')
register(R/'tools/build_production_ledger.py');reject('actual_current72_registration',ns['check_batch35_prerequisites'])
m=register(G/'build_production_ledger.py');m.UNIT_SPECS[-3],m.UNIT_SPECS[-2]=m.UNIT_SPECS[-2],m.UNIT_SPECS[-3];reject('75_registration_with_RFS_before_FRC',ns['check_batch35_prerequisites'])
m.UNIT_SPECS=copy.deepcopy(original);m.UNIT_SPECS[-2]['part_code']='15-XX';reject('RFS_wrongly_in_part15',ns['check_batch35_prerequisites']);m.UNIT_SPECS=copy.deepcopy(original);ns['check_batch35_prerequisites']()
# Extract only three new literal introduction paragraphs; do not invoke compose_body/main.
compose=next(x for x in b.body if isinstance(x,ast.FunctionDef)and x.name=='compose_body');intros={}
for n in ast.walk(compose):
 if isinstance(n,ast.If)and isinstance(n.test,ast.Compare)and isinstance(n.test.left,ast.Name)and n.test.left.id=='stem'and len(n.test.comparators)==1 and isinstance(n.test.comparators[0],ast.Constant):
  stem=n.test.comparators[0].value
  if stem in [x[0]for x in ns['UNITS'][-3:]]:
   assert len(n.body)==1 and isinstance(n.body[0],ast.AugAssign);intros[stem]=ast.literal_eval(n.body[0].value)
text=''.join(intros[stem]+'\n'+(R/'manuscript/foundations'/f'{stem}.md').read_text()for stem,*_ in ns['UNITS'][-3:])+'\n# 附录一 参考答案\n'
assert re.findall(r'^# 第(\d+)部分 ',text,re.M)==['11','63','11'];assert re.findall(r'^# 第(\d+)章 ',text,re.M)==['84','528','84']
main=next(x for x in v.body if isinstance(x,ast.FunctionDef)and x.name=='main')
loops=[]
for n in ast.walk(main):
 if isinstance(n,ast.For)and isinstance(n.target,ast.Tuple):
  vals=[t.id for t in n.target.elts if isinstance(t,ast.Name)]
  if vals==['_stem','anchor']or vals==['anchor','part_anchor','next_part']:loops.append(n)
assert len(loops)==2
code=compile(ast.Module(body=loops,type_ignores=[]),'exact_validator_new_segment_loops','exec')
def require(ok,message):
 if not ok:raise AssertionError(message)
def positions(text):
 segs=['84','528-rfs-continuation','84-combinations-continuation'];starts={s:text.index('{#chapter-'+s+'}')for s in segs};answer=text.index('# 附录一 ');ends={s:starts[segs[i+1]]if i+1<len(segs)else answer for i,s in enumerate(segs)}
 env={'text':text,'answers':answer,'UNITS':ns['UNITS'][-3:],'CLASSIFIED_UNITS':ns['CLASSIFIED_UNITS'],'chapter_starts':starts,'chapter_ends':ends,'require':require};exec(code,env)
positions(text);results['actual_intro_and_three_source_text_positions']='passed'
header='# 第63部分 数学教育（续，MSC 97-XX） {#part-97-real-sums-continuation}\n';assert text.count(header)==1
bad=text.replace(header,'');bad=bad.replace('# 第11部分 线性与多重线性代数、矩阵理论（续，MSC 15-XX）',header+'\n# 第11部分 线性与多重线性代数、矩阵理论（续，MSC 15-XX）');reject('RFS_part_return_moved_after_its_unit',lambda:positions(bad))
for stem,anchor,prefix,_ in ns['UNITS'][-3:]:
 src=(R/'manuscript/foundations'/f'{stem}.md').read_text();ans=(R/'manuscript/foundations'/f'{stem}_answers.md').read_text()
 assert all(src.count('{#'+prefix+f'-q{i:02}'+'}')==1 and ans.count('{#'+prefix+f'-a{i:02}'+'}')==1 for i in range(1,9))
 assert text.count('{#'+prefix+'-sources}')==1
results['actual_three_units_24_pairs_and_three_unique_source_anchors']='passed'
report={'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Only exact guard and two placement loops extracted from AST, registration definitions and literal new introductory paragraphs; no compose/main/builder/validator/render','results':results,'builder_sha256':H(O/'build_learning_batch.py'),'validator_sha256':H(O/'validate_learning_batch.py'),'registration_tool_sha256':H(G/'build_production_ledger.py'),'actual_scope_sha256':H(R/'research/production/part1_scope_plan.json'),'actual_topic_ledger_sha256':H(R/'research/production/part1_topic_sources.json'),'formal_files_modified':False,'full_build_or_validator_executed':False}
(O/'isolated_checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False,indent=2))
