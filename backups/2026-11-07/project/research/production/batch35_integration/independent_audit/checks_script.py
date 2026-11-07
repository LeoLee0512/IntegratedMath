from pathlib import Path
import ast, hashlib, json, re
from urllib.parse import urlsplit
R=Path('/workspace/IntegratedMath-book'); G=Path('/tmp/frc-rfs-flc75-registration'); B=Path('/tmp/batch35-builder-candidate'); O=Path('/tmp/batch35-independent-audit'); O.mkdir(exist_ok=True)
H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def metadata(p,names):
 names=set(names)|{'CH01'}
 t=ast.parse(p.read_text()); nodes=[]
 for n in t.body:
  if isinstance(n,ast.Assign) and any(isinstance(x,ast.Name) and x.id in names for x in n.targets):nodes.append(n)
  elif isinstance(n,ast.AugAssign) and isinstance(n.target,ast.Name) and n.target.id in names:nodes.append(n)
 ns={};exec(compile(ast.Module(body=nodes,type_ignores=[]),str(p),'exec'),ns);return ns
for folder in [G,B]:
 for p,h in json.loads((folder/'candidate_hashes.json').read_text()).items():assert H(folder/p)==h,(folder,p)
reg=json.loads((G/'registration.json').read_text());baseline=reg['baseline_sha256']
for p,h in baseline.items():assert H(R/p)==h,('baseline changed',p)
old=metadata(R/'tools/build_production_ledger.py',{'BRIDGE','MODULES','UNIT_SPECS'});new=metadata(G/'build_production_ledger.py',{'BRIDGE','MODULES','UNIT_SPECS'})
assert len(old['UNIT_SPECS'])==72 and len(new['UNIT_SPECS'])==75
assert new['UNIT_SPECS'][:72]==old['UNIT_SPECS'];assert new['BRIDGE'][:144]==old['BRIDGE'] and len(new['BRIDGE'])==150
for a,b in zip(old['MODULES'],new['MODULES']):
 assert a[:2]+a[3:]==b[:2]+b[3:]
 assert a[2]==b[2] or a[0]=='real-algebra-equations'
oa=json.loads((R/'research/production/accepted_reviews.json').read_text())['reviews'];na=json.loads((G/'accepted_reviews.json').read_text())['reviews']
assert len(oa)==144 and len(na)==150 and na[:144]==oa
names={'UNITS','EDUCATION_UNITS','ANALYSIS_UNITS','B3_UNITS','FINITE_COORDINATE_UNITS','CLASSIFIED_UNITS'}
bo=metadata(R/'tools/build_learning_batch.py',names);bn=metadata(B/'build_learning_batch.py',names)
assert len(bn['UNITS'])==75 and bn['UNITS'][:72]==bo['UNITS']
for name in ['EDUCATION_UNITS','ANALYSIS_UNITS','B3_UNITS']:assert bn[name]==bo[name]
assert [(Path(s['body']).stem,s['anchor']) for s in new['UNIT_SPECS']]==[tuple(u[:2]) for u in bn['UNITS']]
tax={x['code']:x for x in json.loads((R/'data/msc_taxonomy.json').read_text())['entries']}
chap={x['code']:x for x in json.loads((R/'data/production/chapters.json').read_text())['entries']}
parts={x['code']:x for x in json.loads((R/'data/production/parts.json').read_text())['entries']}
sourcefun=next(n for n in ast.parse((B/'build_learning_batch.py').read_text()).body if isinstance(n,ast.FunctionDef) and n.name=='source_hashes')
source_literals={n.value for n in ast.walk(sourcefun) if isinstance(n,ast.Constant) and isinstance(n.value,str)}
order={s['body']:i for i,s in enumerate(new['UNIT_SPECS'])};details=[]
for s in new['UNIT_SPECS'][-3:]:
 assert chap[s['parent_code']]['number']==s['parent_chapter_number'];assert tax[s['parent_code']]['parent_code']==s['part_code']
 assert all(tax[c]['parent_code']==s['parent_code'] for c in s['msc_leaf_codes'])
 body=(R/s['body']).read_text();ans=(R/s['answers']).read_text()
 for p,a in s['prerequisites']:
  assert (R/p).read_text().count('{#'+a+'}')==1,(s['anchor'],a)
  assert order[p]<order[s['body']],('forward prerequisite',s['anchor'],p)
 for a in s['definitions']+[x[1] for x in s['proved']]:assert body.count('{#'+a+'}')==1
 for i in range(1,9):assert body.count('{#'+s['questions']+f'{i:02}'+'}')==1 and ans.count('{#'+s['answer_prefix']+f'{i:02}'+'}')==1
 for p in s['source_records']:assert (R/p).is_file() and p in source_literals,p
 reviews=[x for x in na[144:] if x['target_id']==s['anchor']]
 assert {x['stage'] for x in reviews}=={'math-reviewed','pedagogy-reviewed'} and len({x['reviewer'] for x in reviews})==2
 for x in reviews:
  assert x['status']=='accepted' and not x['blocking_issues']
  assert set(x['source_sha256'])=={s['body'],s['answers']}
  for p,h in x['source_sha256'].items():assert H(R/p)==h
  for e in x['evidence']:
   assert H(R/e['path'])==e['sha256']
   report=(R/e['path']).read_text();assert all(h in report for h in x['source_sha256'].values())
 details.append({'unit':s['anchor'],'code':s['code'],'number':s['number'],'part_number':parts[s['part_code']]['number'],'chapter_number':s['parent_chapter_number'],'leaf':s['msc_leaf_codes'],'prerequisites':len(s['prerequisites']),'source_records':[{ 'path':p,'sha256':H(R/p)} for p in s['source_records']],'reviews':reviews})
v=ast.parse((B/'validate_learning_batch.py').read_text());oldv=ast.parse((R/'tools/validate_learning_batch.py').read_text())
f=next(n for n in v.body if isinstance(n,ast.FunctionDef) and n.name=='is_local_markdown_fragment')
of=next(n for n in oldv.body if isinstance(n,ast.FunctionDef) and n.name==f.name);assert ast.dump(f)==ast.dump(of)
ns={'re':re,'urlsplit':urlsplit};exec(compile(ast.Module(body=[f],type_ignores=[]),'url_check','exec'),ns)
urlcases={'https://github.com/r/x/blob/abc/README.md#abstract':False,'http://example.org/source.md#x':False,'manuscript/chapter.md#x':True,'../chapter.md#x':True,'/workspace/chapter.md#x':True,'file:///tmp/chapter.md#x':True,'//example.org/source.md#x':True,'https:///source.md#x':True,'#valid-anchor':False}
for u,wanted in urlcases.items():assert ns[f.name](u)==wanted,(u,wanted)
assert '.md#' in (R/'tools/validate_learning_batch.py').read_text()
# The pre-existing independent anchors and portable URL constraints also remain unchanged.
def funcs(t):return {n.name:ast.dump(n,include_attributes=False) for n in t.body if isinstance(n,ast.FunctionDef)}
changes={}
for name,allowed in [('build_learning_batch.py',{'source_hashes','compose_body','main','check_batch34_prerequisites'}),('validate_learning_batch.py',{'render_contacts','main'}),('build_production_ledger.py',{'prerequisite_data','build'})]:
 p=B/name if name!='build_production_ledger.py' else G/name
 a=funcs(ast.parse((R/'tools'/name).read_text()));b=funcs(ast.parse(p.read_text()))
 changed=[n for n in a if a[n]!=b.get(n)];assert set(changed)<=allowed,(name,changed);changes[name]=changed
out={'status':'static_integration_checks_passed_not_build_acceptance','formal_files_modified':False,'build_or_ledger_run':False,'old_units_preserved':72,'old_bridge_paths_preserved':144,'old_reviews_preserved':144,'candidate_units':75,'candidate_text_reviews':150,'expected_total_pairs':75*8+27,'baseline_files_rehashed':len(baseline),'new_units':details,'external_md_fragment_cases':urlcases,'changed_functions':changes,'candidate_sha256':{str(p):H(p) for p in [G/'build_production_ledger.py',G/'accepted_reviews.json',B/'build_learning_batch.py',B/'validate_learning_batch.py']}}
(O/'checks.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['status','baseline_files_rehashed','old_units_preserved','old_bridge_paths_preserved','old_reviews_preserved','candidate_units','candidate_text_reviews','expected_total_pairs','changed_functions']},ensure_ascii=False,indent=2))
