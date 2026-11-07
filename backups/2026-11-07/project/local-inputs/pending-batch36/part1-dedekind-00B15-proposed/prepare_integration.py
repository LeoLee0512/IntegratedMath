from pathlib import Path
import hashlib,json,datetime,difflib,copy,re,shutil
R=Path('/workspace/IntegratedMath-book'); O=Path('/tmp/part1-00B15-integration-proposed'); E=Path('/tmp/part1-dedekind-00B15-proposed')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
scopep='research/production/part1_scope_plan.json'; ledgerp='research/production/part1_topic_sources.json'; ch='manuscript/review_ch02/chapter.md'; ap='manuscript/review_ch01/appendices.md'
assert sha(R/scopep)=='0f15545bb2a9a9a9e7f07a82fd0242f458a7d22da9670063f7175f66dd2a06de'
assert sha(R/ledgerp)=='a6fd1b499145de753c4fe2b0423655088b1422b9d3c21f9371ecbbec67cbfb5a'
assert sha(E/'root_mapping_review.md')=='bc5849dfd3a0e1c41f73e51638c358af16f993359a8e534293ba0eeeac7366d0'
scope=json.loads((R/scopep).read_text()); oldledger=json.loads((R/ledgerp).read_text()); ledger=copy.deepcopy(oldledger)
protected=scope['source_files']+[scopep,ledgerp]+['research/production/part1_'+s+'_review.json' for s in ['math','pedagogy','build','visual']]
before={p:sha(R/p) for p in protected}
for p in protected:
 d=O/'base'/p;d.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(R/p,d)
def write(p,t):
 d=O/'new'/p;d.parent.mkdir(parents=True,exist_ok=True);d.write_text(t)
def dump(p,j):write(p,json.dumps(j,ensure_ascii=False,indent=2)+'\n')
text=(R/ch).read_text(); marker='本节与[第28节](#sec-00B25)的专题会议论文集相邻。'
assert text.count(marker)==1
para='''**真实专题选读实践。** Dedekind的《Essays on the Theory of Numbers》是Beman英译的两篇同作者论文合刊，见[本章来源说明中的C2-S4](#ch02-sources)。目录中的两篇分别是《Continuity and Irrational Numbers》与《The Nature and Meaning of Numbers》。可以先选一个问题：“两篇分别从哪些对象和已有规则开始谈数？”第一篇先读§I，再定位§IV的cut（切割）定义：前者明确预设有理算术，而且$R$在这里表示有理数系统。第二篇先读§I的system（系统）与part（部分），再定位§II的transformation（映射）：这里先建立系统及元素的语言，并在这一论述中排除空系统。读者可以分别记下篇名、定义位置、明确假定与未读部分；此处只练习定位这些起点，不要求先掌握两篇的深层理论。

两篇围绕数的基础展开，目录和已读定义使它们适合上述专题选读；仅仅装订在一起并不足以说明各篇共享约定。其同作者英译合刊身份，也不使它成为多人会议论文集。这里没有核验两篇全文的数学证明或德文原篇与英译的逐句对应；历史文本排除空系统的约定不能替换本书允许空集的定义。

'''
text=text.replace(marker,para+marker)
text=text.replace('以及第24节的真实讲座摘要阅读','第24节的真实讲座摘要阅读，以及第26节的专题选读')
reference='''
- **[C2-S4]** Richard Dedekind，*Essays on the Theory of Numbers*，Wooster Woodruff Beman英译，The Open Court Publishing Company，Chicago，1901。两篇为 *Continuity and Irrational Numbers* 与 *The Nature and Meaning of Numbers*。[GITenberg档案固定版本](https://github.com/GITenberg/Essays-on-the-Theory-of-Numbers_21016/blob/7a0bcaf5e279121cb675058d7e323556343087d0/21016-t/21016-t.tex)。2026年11月5日从此前取得的缓存实际核读题名、目录，第一篇§I与§IV的定义入口，第二篇§I的¶1—3及§II的¶21等限定段落；未审完两篇，也未核对德文原版。[作品元数据](https://github.com/GITenberg/Essays-on-the-Theory-of-Numbers_21016/blob/7a0bcaf5e279121cb675058d7e323556343087d0/metadata.yaml)标示美国公有领域；[许可说明](https://github.com/GITenberg/Essays-on-the-Theory-of-Numbers_21016/blob/7a0bcaf5e279121cb675058d7e323556343087d0/LICENSE)另列地域与再分发条件，不据此声称全球公有领域。本书仅列固定链接、必要书目信息与原创阅读说明，不复制外部正文。获取记录与实际阅读范围见`research/production/part1_dedekind_00B15_evidence.json`及`part1_dedekind_00B15_content_review.md`，独立映射复核见`part1_dedekind_00B15_root_mapping_review.md`。
'''
lines=text.splitlines(True)
idx=next(i for i,l in enumerate(lines) if l.startswith('- **[C2-S3]**'))
lines.insert(idx+1,reference);text=''.join(lines)
write(ch,text)
text=(R/ap).read_text();old='本次再为第二章00B05补入真实讲座摘要入口，见第二章来源说明[C2-S3]。其对应全文与证明尚未取得或核验'
new='第二章00B05已有真实讲座摘要入口，见第二章来源说明[C2-S3]；本次为00B15补入同作者两篇专题论文英译合刊的限定选读入口，见第二章来源说明[C2-S4]。摘要对应全文与证明尚未取得或核验，专题选读也不等于两篇全文证明或德英翻译校勘已完成'
assert text.count(old)==1;text=text.replace(old,new).replace('本次摘要核读见C2-S3及对应研究记录。','摘要核读见C2-S3，专题选读核读见C2-S4及对应研究记录。');write(ap,text)
for s in scope['sections']:
 if s['code']=='00B15':s['topic_source_status']='verified'
dump(scopep,scope)
paths={}
for src,suffix in [('evidence.json','evidence.json'),('content_review.md','content_review.md'),('root_mapping_review.md','root_mapping_review.md')]:
 p='research/production/part1_dedekind_00B15_'+suffix;write(p,(E/src).read_text());paths[src]=p
req=next(x for x in scope['sections'] if x['code']=='00B15')['source_requirements'][0]
evidence=json.loads((E/'evidence.json').read_text());doc=evidence['documents'][0]
ref=lambda p:{'path':p,'sha256':sha(O/'new'/p)}
source={'id':'SRC-C2-DEDEKIND-ESSAYS','title':'Essays on the Theory of Numbers — two essays on foundations of number','author_or_publisher':'Richard Dedekind; English translation by Wooster Woodruff Beman; Open Court, Chicago, 1901','version':'7a0bcaf5e279121cb675058d7e323556343087d0','public_url':doc['url'].replace('raw.githubusercontent.com/GITenberg/Essays-on-the-Theory-of-Numbers_21016/','github.com/GITenberg/Essays-on-the-Theory-of-Numbers_21016/blob/'),'access':{'status':'retrieved','method':'local_cache','retrieved_at':doc['retrieved_at'],'document_sha256':doc['sha256'],'evidence':[ref(paths['evidence.json'])]},'content_review':{'status':'verified','reviewer':'/root/part1_sources; independently read and mapped by /root','reviewed_at':evidence['created_at'],'document_sha256':doc['sha256'],'coverage':[{'section_code':'00B15','requirement_id':req['id'],'objective_ids':req['objective_ids'],'relevance':'topic_specific','source_location':'TeX title/contents 205–330; essay I §I 424–519 and §IV 704–730; essay II §I paragraphs 1–3 from 1626, §II paragraph 21 from 1844; exact actual reading ranges in acquisition/content records','verified_claim':'真实两篇专题论文目录及所读定义支持选择同一问题、分别登记起点、术语和先修：第一篇预设有理算术且R指有理数；第二篇以system/part引入transformation并在该论述中排除空系统。同册不自动共享约定。','limitations':'同作者两篇英译合刊，不冒称多人会议或同行评审；未核两篇全部证明、德文原版或逐句翻译；不把历史约定替换本书允许空集的定义。'}],'evidence':[ref(paths['content_review.md']),ref(paths['root_mapping_review.md'])],'mapping_review_date':'2026-11-05'},'license':{'statement':'Work-specific metadata: Public domain in the USA.','actual_read':'metadata full; LICENSE 1–38 and 89–97, especially 1.C/1.D and starred-clause qualification; not full-license re-audit','scope_caveat':'No global public-domain claim. Local law and Project Gutenberg trademark/redistribution terms apply as described in source.','intended_use':'Fixed links, necessary bibliographic facts and original reading guidance only; no source text/files redistributed.'}}
ledger['sources'].append(source)
for x in ledger['sections']:
 if x['code']=='00B15':
  x['topic_source_status']='verified';q=x['requirements'][0];q.update(status='verified',source_ids=[source['id']],reason=source['content_review']['coverage'][0]['verified_claim'])
ledger['counts']={'G_topic_verified':9,'G_topic_pending':9,'T_S_original_work_reviewed_separately':15}
ledger['blocking_issues']=[x for x in ledger['blocking_issues'] if x['section_code']!='00B15']
ledger['boundaries'][0]='本拟议版本只新增00B15限定G专题映射；拟合计9个G verified、9个G pending，15个T/S另行原创审读；整个部分仍pending，正式应用前仍以原8/10账为准。'
ledger['boundaries'].append('00B15仅同作者两篇专题论文英译合刊的目录/定义/先修定位；不扩展00B50/55/60，不认证两篇全文数学证明或翻译准确性。')
ledger['plan_sha256']=sha(O/'new'/scopep)
for p in ledger['source_sha256']:
 ledger['source_sha256'][p]=sha(O/'new'/p) if (O/'new'/p).exists() else sha(R/p)
ledger['proposal_only']=True;ledger['proposal_prepared_at']=now
ledger['revision_history'].append({'prepared_at':now,'application_state':'proposal_only_not_applied','previous_plan_sha256':before[scopep],'previous_ledger_sha256':before[ledgerp],'changed_sections':['00B15'],'scope':'Only 00B15 original objective mapped; projected 9/9/15. Historical review timestamps and entries retained. No whole-part acceptance or new math/pedagogy/build/visual signature.'})
mappingp='research/production/part1_dedekind_00B15_integration_review.md'
write(mappingp,'# 00B15 拟议整合记录\n\n本文件仅记录 /tmp 差异准备，尚未应用，未替代数学、教学、构建或视觉审签。仅 00B15 原目标增加实际专题选读与 C2-S4，其他目标、27 题及其他九项缺口不变。旧8个G来源记录完整保留，原reviewed_at/updated_at及revision_history不重写；新增proposal_only及本次准备事件明确区分历史内容审读与未来正式应用。\n\n'+f'准备时间：{now}。拟scope SHA-256：{ledger["plan_sha256"]}。\n\n'+'拟议8源绑定：\n\n'+''.join(f'- {p}: `{h}`\n' for p,h in ledger['source_sha256'].items())+'\n内容/获取/根独立映射证据分别使用不同路径；原始证据逐字保留，其中提到的8/10和/tmp路径是当时核读事实。待正式应用时应保存现行旧账/旧签并追加真实应用事件；不能仅换旧数学/教学/构建/视觉报告的hash沿用旧签。\n')
ledger['evidence'].append(ref(mappingp));dump(ledgerp,ledger)
changed=[ch,ap,scopep,ledgerp];diff=''
for p in changed:
 diff+=''.join(difflib.unified_diff((R/p).read_text().splitlines(True),(O/'new'/p).read_text().splitlines(True),fromfile='base/'+p,tofile='proposed/'+p))
(O/'integration.diff').write_text(diff)
oldscope=json.loads((R/scopep).read_text())
for a,b in zip(oldscope['sections'],scope['sections']):
 c=copy.deepcopy(b)
 if c['code']=='00B15':c['topic_source_status']='pending'
 assert a==c
assert ledger['sources'][:-1]==oldledger['sources']
assert ledger['revision_history'][:-1]==oldledger['revision_history']
assert [(x['code'],x) for x in ledger['sections'] if x['code']!='00B15']==[(x['code'],x) for x in oldledger['sections'] if x['code']!='00B15']
assert ledger['blocking_issues']==[x for x in oldledger['blocking_issues'] if x['section_code']!='00B15']
assert all(sha(R/p)==h for p,h in before.items())
assert re.findall(r'\{#ch02-question-[^}]+\}',(R/ch).read_text())==re.findall(r'\{#ch02-question-[^}]+\}',(O/'new'/ch).read_text())
assert '#ch02-sources' not in (O/'new'/ap).read_text()
manifest={'status':'proposal_only_not_applied','prepared_at':now,'baseline_sha256':before,'new_sha256':{str(p.relative_to(O/'new')):sha(p) for p in sorted((O/'new').rglob('*')) if p.is_file()},'diff_sha256':sha(O/'integration.diff')};dumpname=O/'manifest.json';dumpname.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
checks={'status':'passed_bounded_static_checks_not_acceptance','formal_inputs_unchanged':True,'only_00B15_scope_status_changed':True,'all_original_objectives_prerequisites_exercises_unchanged':True,'old_sources_and_history_entries_unchanged':True,'other_32_section_records_unchanged':True,'remaining_nine_blockers_unchanged':True,'question_answer_pairs_unchanged':27,'projected_counts':ledger['counts'],'no_cross_chapter_anchor_in_ch1_appendix':True,'original_8_source_bindings_projected':ledger['source_sha256'],'not_run':['whole-part acceptance validator','builder','PDF/HTML rendering','math/pedagogy review','visual review']};(O/'checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n')
print(O);print('diff',sha(O/'integration.diff'));print('manifest',sha(dumpname))
