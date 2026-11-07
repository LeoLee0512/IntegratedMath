from pathlib import Path
import ast,collections,datetime,difflib,hashlib,json,shutil
R=Path('/workspace/IntegratedMath-book');O=Path('/tmp/batch35-builder-candidate');H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();bs=R/'tools/build_learning_batch.py';vs=R/'tools/validate_learning_batch.py';b0=bs.read_text();v0=vs.read_text();b=b0;v=v0
assert H(bs)=='efa3639ac6753e7b6fa45a5f3778121ce67b07962bc70f82329c7adbdb80efb1';assert H(vs)=='14a36b325d52d9d1d8f3e3e597734aea399fa5f2969dd84cb8be85b14756ebaf'
base=O/'base';base.mkdir(exist_ok=True)
for p in[bs,vs]:shutil.copyfile(p,base/p.name)
reg=json.loads(Path('/tmp/frc-rfs-flc75-registration/registration.json').read_text())
newunits=[('finite_real_coordinates','frc-unit','frc','finite_real_coordinates'),('finite_real_sums','rfs-unit','rfs','finite_real_sums'),('finite_coordinate_combinations','flc-unit','flc','finite_coordinate_combinations')]
def rep(w,old,new):
 global b,v
 s=b if w=='b'else v;assert s.count(old)==1,(w,old[:100],s.count(old));s=s.replace(old,new)
 if w=='b':b=s
 else:v=s
rep('b','EDUCATION_UNITS = {','UNITS += '+repr(newunits)+'\nEDUCATION_UNITS = {')
rep('b','CLASSIFIED_UNITS = {**EDUCATION_UNITS, **ANALYSIS_UNITS, **B3_UNITS}', '''FINITE_COORDINATE_UNITS = {
    "frc-unit": {"chapter": 84, "code": "15Axx", "section": "15A03", "learning_code": "B4.L1", "part_code": "15-XX", "segment": "84"},
    "rfs-unit": {"chapter": 528, "code": "97Hxx", "section": "97H20", "learning_code": "B2.39", "part_code": "97-XX", "segment": "528-rfs-continuation"},
    "flc-unit": {"chapter": 84, "code": "15Axx", "section": "15A03", "learning_code": "B4.L2", "part_code": "15-XX", "segment": "84-combinations-continuation"},
}
CLASSIFIED_UNITS = {**EDUCATION_UNITS, **ANALYSIS_UNITS, **B3_UNITS, **FINITE_COORDINATE_UNITS}''')
newpaths=[]
for spec in reg['unit_specs']:
 for p in spec['source_records']:
  if p not in newpaths:newpaths.append(p)
assert all((R/p).is_file()for p in newpaths);assert not any(p.startswith('local-inputs/')for p in newpaths)
rep('b','    return hashes(paths)\n\n\ndef artifact_hashes():','    paths += [ROOT / name for name in '+repr(newpaths)+']\n    return hashes(paths)\n\n\ndef artifact_hashes():')
b=b.replace('check_batch34_prerequisites','check_batch35_prerequisites');v=v.replace('check_batch34_prerequisites','check_batch35_prerequisites')
rep('b','if len(UNIT_SPECS) != 72 or actual != expected:','if len(UNIT_SPECS) != 75 or actual != expected:')
rep('b','Batch34 requires the reviewed 72-unit registration in matching order','Batch35 requires the reviewed 75-unit registration in matching order')
rep('b','    for spec in UNIT_SPECS[-3:]:\n        location = B3_UNITS[spec["anchor"]]','    for spec in UNIT_SPECS[69:]:\n        location = {**B3_UNITS, **FINITE_COORDINATE_UNITS}[spec["anchor"]]')
rep('b','or location["section"] not in spec["msc_leaf_codes"]):','or location["section"] not in spec["msc_leaf_codes"]\n                or ("part_code" in location and spec["part_code"] != location["part_code"])):')
rep('b','B3 display metadata disagrees with the actual registration','B3 or finite-coordinate display metadata disagrees with the actual registration')
rep('b','Batch34 ten-gap disclosure requires the applied 00B05 source revision','Batch35 ten-gap disclosure requires the applied 00B05 source revision')
b=b.replace('七十二个基础桥接单元','七十五个基础桥接单元');v=v.replace('七十二个基础桥接单元','七十五个基础桥接单元')
rep('b','第5章、第8章未完成。第26章、第242章仅有部分单元','第5章、第8章未完成。随后B4.L1进入第11部分第84章15A03有限实数坐标；B2.39回到第63部分第528章97H20建立有限实数和，再以B4.L2回到第11部分第84章建立有限坐标线性组合。第84章未完成，张成、基、维数、秩和矩阵仍待写。第26章、第242章仅有部分单元')
addition='''        if stem == "finite_real_coordinates":
            teaching += """

# 第11部分 线性与多重线性代数、矩阵理论（MSC 15-XX） {#part-15}

在逻辑、集合与有限计数入口之后，转入有限实数坐标。以下B4.L1与后续B4.L2是线性代数支线的学习编号；B4.1—B4.10仍表示前面的分析单元，编号不改。

# 第84章 基础线性代数（15Axx） {#chapter-84}

以下“有限实数坐标与逐坐标运算”的学习编号为B4.L1，主归15A03的有限坐标入口。它从已建立的实数域和函数记录出发，证明逐坐标运算、消去条件、重编号和旧二维模型相容；不调用尚未定义的实数有限和。第84章未完成；张成、抽象向量空间、线性相关、基、维数、秩、lineability、矩阵与行列式仍待后续。学习号不是分类号，章号保留原分类目录编号。

"""
        if stem == "finite_real_sums":
            teaching += """

# 第63部分 数学教育（续，MSC 97-XX） {#part-97-real-sums-continuation}

这里回到数学教育部分，补有限坐标组合需要的实数求和接口。这一回访是学习顺序安排，不改变单元的主分类。

# 第528章 代数教育（97Hxx，实数有限和续） {#chapter-528-rfs-continuation}

以下“有限实数和：递归、逐项规则与拼接”的学习编号为B2.39，主归97H20初等代数教育的有限求和局部。这是[第528章实数代数前段](#chapter-528-real-continuation)之后的同一分类章续写，不新增分类章或节。B2.39从自然递归、函数和实数加乘规则构造实数和值，不把旧有理求和公式直接改名。它不依赖B4.L1，但为后续B4.L2提供有限表和、逐项规则及连续拼接。第528章未完成；任意重排、双重和、无限级数与一般代数理论不在本单元内。

"""
        if stem == "finite_coordinate_combinations":
            teaching += """

# 第11部分 线性与多重线性代数、矩阵理论（续，MSC 15-XX） {#part-15-combinations-continuation}

实数求和接口建立后，回到有限坐标向量；向量项索引和一个向量内部的坐标索引必须分别核查。

# 第84章 基础线性代数（15Axx，续） {#chapter-84-combinations-continuation}

以下“有限坐标向量的线性组合”的学习编号为B4.L2，继续15A03的具体坐标组合局部。它使用[B4.L1的函数表与运算](#frc-unit)及[B2.39的实数有限和](#rfs-unit)，逐坐标定义组合，再证明规则和两个零参数的边界。这是[第84章前段](#chapter-84)后的同一分类章续写，不增加分类章或节。固定坐标重编号不等于任意向量项重排；张成、基、线性相关、维数、秩、矩阵和行列式仍未建立，第84章未完成。

"""
'''
needle='        teaching += "\\n\\n" + (FOUNDATIONS / (stem + ".md")).read_text()';rep('b',needle,addition+needle)
rep('v','len(UNITS) == 72 and len(PAIRS) == 603','len(UNITS) == 75 and len(PAIRS) == 627')
rep('v','Current batch registration counts must be 72 units, 603 exercise pairs and 21 figures','Current batch registration counts must be 75 units, 627 exercise pairs and 21 figures')
rep('v','["1", "2", "26", "526", "529", "528", "529", "528", "526", "528", "527", "242", "146", "5", "8"]','["1", "2", "26", "526", "529", "528", "529", "528", "526", "528", "527", "242", "146", "5", "8", "84", "528", "84"]')
rep('v','Teaching chapter order must follow prerequisites, with chapters 529, 528 and 526 continued','Teaching chapter order preserves the old sequence and appends 84, 528 continuation, 84 continuation')
rep('v','["1", "7", "63", "28", "18", "3"]','["1", "7", "63", "28", "18", "3", "11", "63", "11"]')
rep('v','Teaching parts follow the declared sequence: 1, 7, 63, 28, 18, then bounded B3 revisit in part 3','Teaching parts preserve 1, 7, 63, 28, 18, 3 and append explicit returns 11, 63, 11')
rep('v','"527", "242", "146", "5", "8"]\n        chapter_starts','"527", "242", "146", "5", "8", "84", "528-rfs-continuation", "84-combinations-continuation"]\n        chapter_starts')
rep('v','            require(int(segment.split("-")[0]) == parent','            if anchor in CLASSIFIED_UNITS:\n                segment = CLASSIFIED_UNITS[anchor].get("segment", segment)\n            require(int(segment.split("-")[0]) == parent')
partcheck='''        for anchor, part_anchor, next_part in [
                ("frc-unit", "part-15", "part-97-real-sums-continuation"),
                ("rfs-unit", "part-97-real-sums-continuation", "part-15-combinations-continuation"),
                ("flc-unit", "part-15-combinations-continuation", None)]:
            segment = CLASSIFIED_UNITS[anchor]["segment"]
            end = text.index("{#" + next_part + "}") if next_part else answers
            require(text.count("{#" + part_anchor + "}") == 1
                    and text.count("{#chapter-" + segment + "}") == 1
                    and text.index("{#" + part_anchor + "}") < chapter_starts[segment]
                    < text.index("{#" + anchor + "}") < end,
                    "Finite-coordinate unit must be inside its own declared part/chapter: " + anchor)
'''
rep('v','        for phrase in ["第26章、第242章仅有部分单元",',partcheck+'        for phrase in ["第26章、第242章仅有部分单元",')
rep('v','"第8章未完成", "B3.1",','"第8章未完成", "第84章未完成", "B4.L1", "B2.39", "B4.L2", "15A03", "两个零参数", "B3.1",')
rep('v','"fct-source-boundary"):', '"fct-source-boundary", "frc-sources", "rfs-sources", "flc-sources"):')
rep('v','or "有限索引、计数唯一性与重编号" in text','or "有限索引、计数唯一性与重编号" in text\n                    or "第84章基础线性代数" in text or "有限实数坐标与逐坐标运算" in text\n                    or "有限实数和：递归、逐项规则与拼接" in text or "有限坐标向量的线性组合" in text')
ast.parse(b);ast.parse(v)
(O/'build_learning_batch.py').write_text(b);(O/'validate_learning_batch.py').write_text(v)
for name,old,new in [('build_learning_batch.py',b0,b),('validate_learning_batch.py',v0,v)]:
 (O/(name+'.diff')).write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='current72/tools/'+name,tofile='proposed75/tools/'+name)))
def funcs(s):return{n.name:ast.dump(n,include_attributes=False)for n in ast.parse(s).body if isinstance(n,ast.FunctionDef)}
bf0,bf=funcs(b0),funcs(b);vf0,vf=funcs(v0),funcs(v)
changed_b=[n for n in bf0 if n in bf and bf[n]!=bf0[n]];changed_v=[n for n in vf0 if vf[n]!=vf0[n]]
assert set(changed_b)=={'source_hashes','compose_body','main'};assert set(bf0)-set(bf)=={'check_batch34_prerequisites'};assert set(bf)-set(bf0)=={'check_batch35_prerequisites'};assert set(changed_v)=={'render_contacts','main'};assert vf['is_local_markdown_fragment']==vf0['is_local_markdown_fragment']
req=lambda s:collections.Counter(ast.dump(n,include_attributes=False)for n in ast.walk(ast.parse(s))if isinstance(n,ast.Call)and isinstance(n.func,ast.Name)and n.func.id=='require')
oldreq,newreq=req(v0),req(v);assert sum((oldreq-newreq).values())==3;assert sum(newreq.values())==sum(oldreq.values())+1
# Evaluate literal assignments only, preserving all old units and classification maps.
def data(s):
 names={'UNITS','EDUCATION_UNITS','ANALYSIS_UNITS','B3_UNITS','FINITE_COORDINATE_UNITS','CLASSIFIED_UNITS','FIGURES'};nodes=[]
 for n in ast.parse(s).body:
  if isinstance(n,ast.Assign)and any(isinstance(t,ast.Name)and t.id in names for t in n.targets):nodes.append(n)
  if isinstance(n,ast.AugAssign)and isinstance(n.target,ast.Name)and n.target.id in names:nodes.append(n)
 ns={};exec(compile(ast.Module(body=nodes,type_ignores=[]),'literal_metadata','exec'),ns);return ns
old,new=data(b0),data(b);assert len(old['UNITS'])==72 and new['UNITS'][:72]==old['UNITS']and len(new['UNITS'])==75
for n in['EDUCATION_UNITS','ANALYSIS_UNITS','B3_UNITS','FIGURES']:assert old[n]==new[n]
# Source-path constants from the existing dependency function are all retained.
strings=lambda s:{n.value for n in ast.walk(next(n for n in ast.parse(s).body if isinstance(n,ast.FunctionDef)and n.name=='source_hashes'))if isinstance(n,ast.Constant)and isinstance(n.value,str)}
assert strings(b0)<=strings(b)
checks=dict(prepared_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='temporary_candidate_not_applied',syntax='passed',old72_UNITS_preserved=True,old_classification_maps_and_21_figures_preserved=True,all_old_source_path_constants_preserved=True,changed_existing_builder_functions=changed_b,renamed_guard='check_batch34_prerequisites -> check_batch35_prerequisites',changed_existing_validator_functions=changed_v,all_other_functions_ast_unchanged=True,external_HTTP_markdown_fragment_fix_preserved=True,old_require_calls=sum(oldreq.values()),new_require_calls=sum(newreq.values()),changed_old_require_calls=3,new_require_calls_for_part_chapter_containment=1,appended_units=newunits,new_source_records=newpaths,expected_counts={'units':75,'pairs':627,'figures':21,'part1_G_verified':8,'part1_G_pending':10},expected_new_parts=[11,63,11],expected_new_chapters=[84,528,84],baseline_sha256={'tools/build_learning_batch.py':H(bs),'tools/validate_learning_batch.py':H(vs)},candidate_sha256={'build_learning_batch.py':H(O/'build_learning_batch.py'),'validate_learning_batch.py':H(O/'validate_learning_batch.py')},build_executed=False,compose_executed=False,validator_executed=False,formal_files_modified=False)
(O/'checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n');print(json.dumps(checks,ensure_ascii=False,indent=2))
