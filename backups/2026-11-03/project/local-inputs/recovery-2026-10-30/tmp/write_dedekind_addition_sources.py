from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,re,copy
root=Path('/workspace/IntegratedMath-book');base=Path('/tmp/dedekind-addition-source-audit');now=datetime.now(timezone.utc).isoformat()
h=lambda p:sha256(Path(p).read_bytes()).hexdigest()
prior=json.loads(Path('/tmp/rational_gaps_cuts_sources.json').read_text());powers=json.loads(Path('/tmp/powers-polynomials-source-audit/requests.json').read_text())
new=json.loads((base/'requests.json').read_text());records={r['request_id']:r for r in prior['requests']+prior['reused_requests']}
records.update({r['request_id']:r for r in powers});reused=[]
ids=['mathlib_lower_basic','mathlib_field_basic','mathlib_archim_basic','mathlib_group_defs','mathlib_license','dedekind_tex','dedekind_license','dedekind_metadata','lebl_reals','lebl_license']
for ident in ids:
 r=copy.deepcopy(records[ident]);r.setdefault('cache_path','/tmp/powers-polynomials-source-audit/'+ident)
 r['reused_from_log']='/tmp/powers-polynomials-source-audit/requests.json' if ident in ['mathlib_group_defs','mathlib_license'] else '/tmp/rational-gaps-cuts-source-audit/requests.json'
 r['cache_rechecked_at_utc']=now;r['new_network_fetch_this_batch']=False;reused.append(r)
requests=new+reused;byid={r['request_id']:r for r in requests}
for r in requests:assert h(r['cache_path'])==r['sha256'] and Path(r['cache_path']).stat().st_size==r['bytes']
sources=[]
old_sources={s['id']:s for s in prior['sources']}
for ident in ids:
 if ident in old_sources:s=copy.deepcopy(old_sources[ident])
 else:s=dict(id=ident,title='Mathlib/Algebra/Group/Defs.lean',author='Jeremy Avigad; Leonardo de Moura; Simon Hudon; Mario Carneiro',version='mathlib v4.24.0',license='Apache-2.0',role='Additive structure definitions; the listed laws are assumptions until constructed and proved for cuts')
 r=byid[ident];s.update(url=r['url'],cache_path=r['cache_path'],sha256=r['sha256'],bytes=r['bytes'],original_fetch_at_utc=r['checked_at_utc'],reused_cached_bytes=True);sources.append(s)
r=new[0];sources.append(dict(id=r['request_id'],title='Mathlib/Algebra/Order/UpperLower.lean',author='Yaël Dillies',version='mathlib v4.24.0',license='Apache-2.0; file header plus reused LICENSE',role='Pointwise lower-set operations and reflection; crucial closed-endpoint zero differs from book cuts',url=r['url'],cache_path=r['cache_path'],sha256=r['sha256'],bytes=r['bytes'],original_fetch_at_utc=r['checked_at_utc'],reused_cached_bytes=False))
# Replace old source-use descriptions with current, limited roles while retaining originals separately.
for s in sources:
 s['previous_role_as_recorded']=s.pop('role')
 s['use_this_batch']='Version/conditions comparison only; no passage, exercise, diagram or Lean code copied into book.'
checks=[]
def loc(i,group,sid,start,end,name,assumes,difference):
 text=Path(byid[sid]['cache_path']).read_bytes().decode('latin-1' if sid=='dedekind_tex' else 'utf-8').splitlines();assert 1<=start<=end<=len(text)
 checks.append(dict(id=i,planned_group=group,source_id=sid,start_line=start,end_line=end,actual_locator=name,source_assumptions=assumes,book_difference_and_obligation=difference))
loc('strict_lower','DA1–DA3','mathlib_lower_basic',323,338,'isLowerSet_iff_forall_lt / isLowerSet_iff_Iio_subset','PartialOrder; weak closure is equivalent to strict closure via equality case.','Book lower closure is strict q<a; this matches after checking equality separately. Nonempty/proper/no-max are additional conditions, not consequences of lower closure.')
loc('complement','DA3','mathlib_lower_basic',38,52,'IsLowerSet.compl / IsUpperSet.compl','Set complement of a lower set is an upper set, for the existing ambient order.','Complement alone is not a negative cut. Reflection turns upper into lower but does not remove a possible maximum.')
loc('midpoint','DA3','mathlib_field_basic',23,25,'LinearOrderedSemifield assumptions','Already given ordered semifield structure.','Applicable to established Q, not to not-yet-constructed cut arithmetic.')
loc('midpoint_bounds','DA3','mathlib_field_basic',132,134,'left_lt_add_div_two / add_div_two_lt_right','Given a<b, midpoint strictly between; no completeness.','For q<−r choose (q−r)/2, keeping the same complement witness; this proves no maximum for the strict negative cut.')
loc('rational_natural_bound','DA1','mathlib_archim_basic',358,400,'archimedean_iff_nat_lt and Archimedean Q','Field/order structure; library rational proof uses rational ceiling in an intermediary step.','Book already has QG1 explicit rational-record bound; use it on (b0−a0)/δ to get a natural exit bound, without real Archimedean property, floor or cut arithmetic.')
loc('pointwise_ambient_assumptions','DA2/DG1','mathlib_order_upperlower',38,46,'OrderedCommGroup variable block, translation image','CommGroup, PartialOrder, IsOrderedMonoid; multiplicative text marked to_additive.','Read source annotations only, no Lean elaboration/compilation. The additive specialization may be applied to Q whose additive laws are proved. It does not assume or prove that newly constructed cuts form a group.')
loc('pointwise_lower_closure','DA2','mathlib_order_upperlower',53,67,'IsLowerSet.mul_left / mul_right with to_additive','Pointwise operation on arbitrary subsets; lower closure when the indicated factor is lower, in the prior ordered-group context.','Book proves exact-sum lower closure using a′=p−b; it must separately prove nonempty, proper and no maximum. Do not treat library lower closure as cut closure.')
loc('reflection','DA3','mathlib_order_upperlower',69,73,'IsUpperSet.inv / IsLowerSet.inv with to_additive','Reflection/inverse changes upper to lower and lower to upper in an ordered group.','Source guarantees only lower closure of reflected complement. Book N(A)={q:∃r∉A,q<−r} has an additional strict rounding step. For A=i(0), raw reflected complement is {q≤0} and fails no-maximum.')
loc('exact_pointwise_sum','DA2','mathlib_order_upperlower',153,173,'LowerSet One / Mul / coe_mul, to_additive annotations','Bundled lower sets use image2 of ambient operation; all lower sets allowed.','Image2 corresponds to exact rational sum witnesses, but neither the restricted type nor its zero is the book type. Exact and strict sum witness equivalence must be proved from no-max/downward closure.')
loc('closed_zero_trap','DG1','mathlib_order_upperlower',155,157,'LowerSet One defined by Iic 1, to_additive','Additive translation of this definition gives the CLOSED lower segment Iic 0.','Book 0_R=i(0)=Iio(0) excludes rational zero. Cannot cite library zero/unit proof as the book proof; use an internal larger a and z=q−a<0 in the reverse inclusion.')
loc('lower_monoid','DG1/DG2','mathlib_order_upperlower',188,206,'LowerSet commSemigroup / one_mul / CommMonoid, to_additive','Commutative monoid of all lower sets, with closed principal unit. No cut inverse construction here.','Only a comparison for inherited associativity/commutativity. Book nested witness proofs establish these on restricted cuts; DA1 is still required for inverse reverse inclusion. Arbitrary lower sets do not all have additive inverses.')
loc('group_associative_commutative','DG1','mathlib_group_defs',187,209,'AddSemigroup and AddCommMagma declarations','add_assoc and add_comm are fields required of structures.','They name obligations, not automatic theorems of the new cut operation. Prove by two-direction witness regrouping using only old Q laws.')
loc('group_inverse','DG2','mathlib_group_defs',1095,1103,'AddGroup declaration and neg_add_cancel field','Existing SubNegMonoid plus a neg_add_cancel proof; subtraction convention discussed.','Book must prove A⊕N(A)=0_R in both directions before using inverse uniqueness, double negation or cancellation.')
loc('commutative_group_name','DG2–DG4','mathlib_group_defs',1167,1168,'AddCommGroup declaration','AddGroup plus AddCommMonoid.','After the laws are proved, the name describes the concrete structure. It is not a prior abstract axiom or a claim of ordered field / multiplication.')
loc('modern_cut_context','DA1–DA4','lebl_reals',1053,1067,'exercise:Dedekind','Existing complete R, lower rational subset bounded above, sup_R A not a member.','This source characterizes cuts after R already exists. Do not obtain small rational boundary gaps from an assumed real supremum/density. Book uses Q grid and natural least index instead.')
loc('reject_complete_real_route','DA1','lebl_reals',693,723,'thm:arch and proof','Real Archimedean property is proved using sup_R N; Q density in R is subsequently derived.','This route would assume the target ambient real structure. Book needs Q-only Archimedean bound and least natural index, and does not call cut-supremum either.')
loc('history_addition','DA2/history','dedekind_tex',1006,1025,'Part I §VI Operations with Real Numbers','Two-sided historical cuts; C1 membership uses c≤a1+b1; endpoint may be assigned to the first side.','Not literally the modern strict-cut definition. For BOOK cuts, exact, ≤-witness and <-witness versions can be connected by lower closure and no maximum; the historical endpoint convention cannot simply be dropped.')
loc('history_rational_compatibility','DA4','dedekind_tex',1025,1045,'§VI rational addition compatibility and halving positive gap','Rational endpoints and two-sided cuts; splits positive p into two halves to produce members.','Book independently uses h=(r+s−q)/2 and exact witnesses r−h,s−h; prove both inclusions for strict principal lower sets.')
loc('history_not_full_proof','DG2–DG4 exclusion','dedekind_tex',1047,1062,'§VI statement about other operations','Author says other operations may likewise be defined and discusses scope, without supplying this book strict-negation/grid inverse proof.','Do not cite this paragraph as a complete proof of strict negative cuts, ε-grid lemma, inverse law, order translation, or subsequent multiplication/root existence.')

# Locate actual prior anchors, explicitly distinguishing frozen /tmp batch21 from formal files.
plan=Path('/tmp/dedekind_addition_plan.md');concept=Path('/tmp/dedekind_addition_concept_review.md')
part=plan.read_text().split('精确接口：')[1].split('依赖方向固定')[0]
wanted=list(dict.fromkeys(re.findall(r'`([a-z][a-z0-9-]+)`',part)))
found={}
for p in (root/'manuscript').rglob('*.md'):
 for n,line in enumerate(p.read_text().splitlines(),1):
  for a in re.findall(r'\{#([^}]+)\}',line):found.setdefault(a,[]).append((p,n,line,'formal_manuscript'))
for name in ['rational_gaps_bounds.md','dedekind_cuts_order.md']:
 p=Path('/tmp')/name
 for n,line in enumerate(p.read_text().splitlines(),1):
  for a in re.findall(r'\{#([^}]+)\}',line):
   if a not in found:found[a]=[(p,n,line,'frozen_batch21_candidate_not_claimed_formal')]
prereqs=[]
for a in wanted:
 assert len(found.get(a,[]))==1,(a,found.get(a));p,n,line,status=found[a][0]
 prereqs.append(dict(anchor=a,path=str(p),line=n,heading=line,sha256=h(p),actual_location_status=status))
obligations=[
('DA1','cutadd-grid','Separate each internal a from external b by rational trichotomy and lower closure. For epsilon>0 set delta=epsilon/2; choose a0∈A,b0∉A and QG1 positive natural N with eta(N)delta>b0−a0. E={n:a0+eta(n)delta∉A} is nonempty, excludes 0. Use ord-a07 least m; m=k+1 gives k∉E. Then u in, v out, v−u=delta strictly between 0 and epsilon. No cut arithmetic, cut supremum, real density or simultaneous choices.'),
('DA1 computational boundary','cutadd-grid','Well-ordering yields a least member of a specified nonempty natural set under classical logic. An arbitrary cut supplies no decidable membership predicate, so no general executable first-exit search, computed real boundary, or terminating cut API is inferred. A rational principal-cut example may have an independent decision procedure.'),
('DA2 closure','cutadd-definition','A⊕B={q:∃a∈A,b∈B,q=a+b}. Internal a0+b0 gives nonempty; external r+s is outside because all a+b<r+s; p<q=a+b uses a′=p−b<a; increasing a gives no maximum. Only after four conditions declare R×R→R, with exterior equality giving a unique output subset.'),
('DA2 witness conventions','cutadd-definition','For book cuts, q=a+b can be strengthened to q<a1+b by increasing a. Conversely q<a+b gives exact q=(q−b)+b with q−b<a. A weak q≤a+b version also needs equality or lower closure. Historical cuts that admit endpoint maxima are not silently equivalent to this restricted convention.'),
('DA3','cutadd-negation','N(A)={q:∃r∉A,q<−r}. External r0 gives −r0−1 inside; internal a0 makes −a0 outside; same external witness gives lower closure; midpoint (q−r)/2 gives no maximum. Do not identify it with raw −A or raw reflection of complement. For i(0), raw reflected complement {q≤0} has maximum 0.'),
('DA4 addition','cutadd-rational','i(r)⊕i(s)=i(r+s): forward sum of strict inequalities; backward q<r+s, h=(r+s−q)/2>0, a=r−h,b=s−h, a+b=q. Covers negative and zero endpoints with exact rational arithmetic.'),
('DA4 negation','cutadd-rational','N(i(r))=i(−r): external t means t≥r so q<−t≤−r; converse use external t=r. Principal compatibility does not prove all-cut laws since nonprincipal cuts exist.'),
('DG1','cutgroup-laws','Exchange witnesses; expand both nested sum memberships before using rational associativity. A⊕i(0)⊆A follows from z<0. Reverse uses q<a∈A then z=q−a<0; rational zero is NOT in i(0).'),
('DG2 inverse existence','cutgroup-inverses','Forward q=a+c with c<−r, r∉A, a<r gives q<a−r<0. Reverse any x<0: DA1 with epsilon=−x yields v−u<−x, hence c=x−u<−v, so c∈N(A) and x=u+c. A nonstrict gap may yield equality and fail the negative-cut witness; strictness is essential.'),
('DG2 consequences','cutgroup-inverses','After both inverse inclusions, use already established association, commutation and unit to prove inverse uniqueness. Then N(N(A))=A, cancellation, and group terminology. Do not assume any of these in DA1 or in inverse existence.'),
('DG3','cutgroup-translation','Weak monotonicity follows from member inclusion. Reflection requires adding N(C) after inverse law. Strict preservation follows from weak preservation plus equality cancellation; strict reflection similarly excludes equality. Translation T_C has two-sided inverse T_N(C), a function on established cut set R.'),
('DG4','cutgroup-negation-subtraction','A⊆B gives r∉B⇒r∉A, hence N(B)⊆N(A). Reflection uses double negation only after DG2. Prove inverse of sum by actual parenthesized rearrangement and uniqueness. Define A⊖B=A⊕N(B), then solve A⊕X=B uniquely and derive order-by-difference from translation.'),
('Background and endpoint scope','cutadd-unit/cutgroup-unit','Use existing Q and cut-set P(Q) background, products and conditional subsets. No new unrestricted object collection or choice axiom. All witnesses are selected for one given input/claim; no global choice function. No real multiplication, inverse/division, roots, limits, or complete ordered-field claim.'),
]
observations=[
 dict(item='ord-a07 actual proof',path='manuscript/foundations/natural_order_answers.md',start_line=169,end_line=185,conclusion='Nonempty natural set has unique least element, proved by strong induction and classical contradiction; not a newly adopted axiom.'),
 dict(item='grid proof mapping',source_status='independent derivation from actual QG1, ord-a07 and rational arithmetic; no exact external theorem claimed',claim='0<v−u<epsilon with one interior and one exterior rational'),
 dict(item='strict negative-cut source gap',source_status='no inspected external source gives the complete exact N(A) construction plus endpoint check and inverse proof',claim='Book must carry the full four-condition and epsilon-grid proof; related library reflection proves only closure direction'),
 dict(item='ordered cut group laws',source_status='independent construction proof; abstract source declarations only describe required laws',claim='Do not use an already-given OrderedAddCommGroup instance to establish the structure being constructed')]
audit=dict(schema_version=1,status='batch22_source_preflight_only',citation_anchor='dedekind-addition-sources',checked_at_utc=now,
 scope='B2.23 DA1–DA4 rational grid witnesses / exact cut sums / strict negative cut / rational compatibility; B2.24 DG1–DG4 additive laws / inverse / order translation / subtraction. No formal batch22 edits or acceptance.',
 plan=dict(path=str(plan),sha256=h(plan),concept_review_path=str(concept),concept_review_sha256=h(concept),primary_msc='97F50',chapter=526,cross_references=['06F20','06A05']),
 access=dict(policy='Current inherited restricted/enforced public HTTPS proxy context from batch21; no changes or bypass. raw.githubusercontent.com is allowed.',new_http_requests=len(new),new_http_200=sum(x['http_status']==200 for x in new),new_git_queries=0,reused_cache_records=len(reused),new_fetch_for_reused_records=0,new_request_log=str(base/'requests.json'),new_request_log_sha256=h(base/'requests.json'),reason_for_one_new_request='Previously inspected mathlib directory showed Algebra/Order/UpperLower.lean; needed actual text for pointwise operation/endpoint assumptions; no repeated blind search'),
 new_requests=new,reused_requests=reused,sources=sources,checked_source_locators=checks,existing_prerequisite_anchors=prereqs,independent_derivation_observations=observations,
 book_proof_obligations=[dict(group=g,anchor=a,obligation=t) for g,a,t in obligations],
 adopted_vs_proved=dict(adopted='Only prior explicit classical logic and set background including batch21 P(Q), products and conditional subsets; no new Archimedean/completeness or group axiom for cuts.',proved_before_use='QG1 and ord-a07 must be linked to their actual files; book proves cut closure, unit, inverse and order laws before using them.',not_adopted=['Existing complete real field or rational density in it','mathlib full lower-set closed zero Iic(0)','Historical two-sided endpoint identification without translation','Decidable membership or a first-exit algorithm for arbitrary cuts','Choice functions, cut multiplication, real square roots or limits']),
 critical_mismatches=['Book strict i(0)=Iio(0) versus library all-LowerSet additive zero Iic(0).','Historical C1 uses weak sum witness and allows endpoint allocation; book exact/strict sum equivalence uses no maximum.','Pointwise reflection of complement can include a largest endpoint; the book strict q<−r definition removes it.','Abstract group laws and already-built R sources cannot be premises of the same cut construction.'],
 source_availability='All listed bytes actually read and SHA checked. One new public 200; ten cached records reused at original fetch dates. Exact grid and strict-negation inverse proof not located externally in inspected sources and explicitly recorded as independent book derivation.',
 licenses='Mathlib Apache-2.0. Lebl dual CC-BY-SA-4.0 / CC-BY-NC-SA-4.0. Dedekind ebook metadata: public domain in USA, with Project Gutenberg license; no global public-domain claim. License caches and metadata preserve original URLs and hashes.',
 use='Original factual/condition summaries only; no external proof prose, exercises, diagrams or Lean source copied into manuscript. Latin-1 for Dedekind TeX as declared inputenc; hashes use original bytes. No Lean compilation.',
 limits=['Plan/concept/source review is not manuscript acceptance.','No claim of direct external textual evidence for exact epsilon-grid or strict negative-cut inverse argument.','No general cut API, member-decision algorithm, real multiplication, ordered-field completion or root existence.'],repo_mutations=[])
Path('/tmp/dedekind_addition_sources.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
md=['# 第22批来源预研：分割加法、相反数与次序平移','',f'核验时间：{now}。仅 `/tmp`。统一锚 `dedekind-addition-sources`。',audit['scope'],'','主归属97F50、第526章；06F20、06A05仅交叉。计划与概念审查SHA见JSON，不能据计划预发正文验收。','', '## 已核结论与证据边界','',audit['source_availability'],'',*['- '+x for x in audit['critical_mismatches']],'','## 访问、版本与许可','',audit['licenses'],audit['use'],'']
for s in sources:
 md += [f"### {s['id']}",'',f"{s['author']}，{s['title']}；{s['version']}。",f"URL：{s['url']}",f"许可：{s['license']}",f"原请求时间：{s['original_fetch_at_utc']}；本批复用：{s['reused_cached_bytes']}。",f"SHA-256：`{s['sha256']}`；缓存 `{s['cache_path']}`。",'']
md+=['## 实际读到的位置与条件差异','']
for c in checks:
 md += [f"### {c['planned_group']} / {c['id']}",'',f"`{c['source_id']}` 第{c['start_line']}—{c['end_line']}行：`{c['actual_locator']}`。",f"来源条件：{c['source_assumptions']}",f"本书义务：{c['book_difference_and_obligation']}",'']
md+=['## 独立推导义务：不能由引用省略','']
for g,a,t in obligations:md += [f'- **{g}** `#{a}`：{t}','']
md+=['## 网格最小指标的实际先修与算法边界','', '已逐行读 `natural_order_answers.md` 第169—185行：假设非空自然集合无最小元，以已证强归纳推出所有自然数均不属于它，再与非空见证矛盾；唯一性由反对称。因此这是已证明的结论，不是本批新采用的良序公理。', '','DA1的E是条件子集：先有N∈E、0∉E，再取最小正m的前驱k，得u在内、v在外、v−u=ε/2。推理只说明见证存在，不提供任意分割的成员判断程序。具体i(3/2)示例中u=5/4、v=3/2、ε=1/2，外点可以正好落在有理端点。','', '## 真实先修位置','']
for p in prereqs:md += [f"- `#{p['anchor']}` → `{p['path']}:{p['line']}`；状态 `{p['actual_location_status']}`；SHA `{p['sha256']}`。"]
md+=['', '## 采用与未采用','',audit['adopted_vs_proved']['adopted'],'',*['- 不采用：'+x for x in audit['adopted_vs_proved']['not_adopted']],'','## 限制','',*['- '+x for x in audit['limits']],'', '本次不修改第20、21批正式文件、冻结来源、图像、ledger或验收。新增网络请求只有上述数学库文件一次；原第21批版本查询与许可时间不改写成新抓取。','']
Path('/tmp/dedekind_addition_sources.md').write_text('\n'.join(md))
print(json.dumps(dict(sources=len(sources),locators=len(checks),prerequisite_anchors=len(prereqs),obligations=len(obligations),new_requests=len(new),reused=len(reused),json_sha256=h('/tmp/dedekind_addition_sources.json'),md_sha256=h('/tmp/dedekind_addition_sources.md')),indent=2))
