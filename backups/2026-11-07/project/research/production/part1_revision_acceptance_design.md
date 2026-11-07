# 第一部分修订：专题来源门槛与历史状态

日期：2026-11-05。工作目录：`/workspace/IntegratedMath-part1-publish`。本方案不改原`IntegratedMath-book`、正文、生产JSON、Git历史或远程。

## 旧验收为什么不足

de08a8a对应的旧验收器只要求G节的`reference_entries`指向存在的本地锚点；没有检查参考资料是否属于该节专题、是否实际取得并读过内容。旧来源报告已经承认书评、开放问题、哲学、文学等候选页面未取得，普通逻辑资料只能支持量词或反例，不能兑现这些专题的已核验入口要求。因而原`accepted`是当时工具给出的历史记录，不是当前完整部分仍已通过的依据。

应保留旧源稿、scope、math/ped/build/visual/acceptance报告、原来源报告、工具版本与实际产物。以旧Git提交和文件SHA-256定位历史快照，另写“专题来源门槛未被旧工具检查，旧全范围完成声明不再适用”的说明；不能覆盖旧报告日期、偷偷把旧accepted改成过去就pending，也不能将旧视觉查看记成新PDF的查看。主代理负责保存dist和历史快照；本代理不移动或改写这些文件。

## 新门槛独立于其他阶段

保留scope、math、pedagogy、build、visual各自结果，新增`full_scope_sources_accepted`。只有所有阶段都通过，完整部分才accepted；专题来源缺失时，数学推导或版面可以分别通过，但部分完成、章节完成和push节点都不得提升。输出增加`source_review`和逐节`topic_source_status`，不把一个来源问题写成“数学已被证明错误”。作者审阅仍独立pending。

`Validator.validate(args)`支持可选`args.source_review`，缺省为`research/production/part1_topic_sources.json`，因此旧台账helper无需先改调用参数也会执行新门槛。命令行新增`--source-review`。

## 范围计划：每节新增字段

```json
{
  "code": "00A30",
  "topic_source_status": "pending",
  "source_requirements": [{
    "id": "00A30-topic-1",
    "topic": "数学哲学：对象、证明和公理的认识论问题入口",
    "objective_ids": ["00A30-1"],
    "relevance": "topic_specific"
  }]
}
```

G必须逐项声明非空来源要求，并覆盖其导读目标；要求必须为`topic_specific`。每个要求绑定本节目标，不能用另一个节的需求代替。普通逻辑反例可以作背景，但不能据此满足数学哲学、文学、书评等专题要求。没有足够专题资料时保留`topic_source_status: "pending"`，不要为了通过改成general_method或缩掉已经要求的专题入口。

T/S的原创推导、例题、单位模型以及公开采用规则，不要求外部文献中出现相同例题或相同证明。合法的scope状态是`source_requirements: []`和`topic_source_status: "original_work_reviewed_separately"`；来源JSON中对应节同样填写该状态以及`requirements: []`。这表示由独立math/ped门槛负责审阅，不表示外部来源已verified。完整部分仍必须数学与教学审阅通过。

若T/S实际依赖外引定理、历史事实、实测数据等，则不能使用空需求豁免。用可选`external_source_claims`逐项声明`{"claim":"外部事实", "requirement_id":"对应来源需求ID", "objective_ids":["受该事实支持的目标"]}`，并登记非空来源要求；工具检查每项映射和真实来源证据。T/S的非空来源要求只需覆盖实际外部依赖，不必覆盖其余原创推导目标。空需求与非空external_source_claims并存会被拒绝。

未声明外部依赖的情况仍须math/ped审阅者核对正文；工具不能从字符串自动识别被隐瞒的外引事实。单纯列为对照阅读的参考书不自动把原创证明变成外引结论，公开采用的规则也不冒充本书或外文献已完成的证明。

这两个新增字段在source阶段检查，不使其他阶段因“来源尚缺”本身失败。计划或源稿实际修改仍会使旧math/ped报告hash过期，这是必要的版本绑定。

## 新来源JSON契约

```json
{
  "schema_version": 1, "target_type": "part", "target_id": "00-XX", "scope": "complete_part",
  "status": "pending",
  "plan_sha256": "当前scope文件SHA-256",
  "source_sha256": {"计划全部source_files": "当前hash"},
  "sources": [{
    "id": "P1-PHIL-VERIFIED",
    "title": "实际取得的作品题名",
    "author_or_publisher": "已核对的作者或出版者",
    "version": "已核对的版次、修订日期或不可变版本",
    "public_url": "https://example.org/actual-source",
    "access": {
      "status": "retrieved",
      "method": "public_https",
      "retrieved_at": "2026-11-05T00:00:00+00:00",
      "document_sha256": "实际取得内容的SHA-256",
      "evidence": [{"path": "research/production/source_access_record.json", "sha256": "证据文件hash"}]
    },
    "content_review": {
      "status": "verified",
      "reviewer": "实际阅读者稳定身份",
      "reviewed_at": "2026-11-05T00:00:00+00:00",
      "document_sha256": "与access同一个内容hash",
      "evidence": [{"path": "research/production/source_content_review.md", "sha256": "实质核验报告hash"}],
      "coverage": [{
        "section_code": "00A30", "requirement_id": "00A30-topic-1",
        "objective_ids": ["00A30-1"], "relevance": "topic_specific",
        "source_location": "实际读过的页码、节名或可定位段落",
        "verified_claim": "此处具体支持本书什么专题说明或入口判断",
        "limitations": "只核验所列内容；哪些章节、证明或最新研究状态尚未核验"
      }]
    }
  }],
  "sections": [{
    "code": "00A30", "topic_source_status": "pending",
    "requirements": [{
      "requirement_id": "00A30-topic-1", "status": "pending", "source_ids": []
    }]
  }]
}
```

sections必须恰好覆盖33节；每节requirements恰好对应计划中的需求ID。有来源需求的节通过要求为：scope节状态verified、来源JSON节状态verified、全部需求status verified，且每个需求至少有一个来源的实际内容核验覆盖全部对应目标。原创T/S可按上述独立审阅状态使用空需求，不会被标为来源verified。`access.status`允许`retrieved`、`available_local`；method允许`public_https`、`local_cache`、`user_provided`。本地旧材料须保留原取得日期，不伪装新访问；本地报告证据hash必须可核对。外部材料不必收入发布ZIP，许可未知不等于可转载。

非空URL、HTTP 200、下载hash、README或许可页本身都不能代替专题内容核验。工具不联网，也不把返回状态转换为verified。通过还需要命名阅读者、阅读日期、同一内容hash、专题/目标映射、可定位内容、具体支持的判断、核验边界和独立的实质报告文件。取得证据与内容审阅报告不能是同一个文件；审核者不能只将HTTP响应记录改名为内容报告。

工具只能核对这些明确签署与文件身份，不能凭字符串自动理解一份来源是否真正属于数学哲学或文学。因此主编/独立审阅仍须检查`verified_claim`和报告实际内容；本门槛拒绝明示的general_method替代，却不声称能识破所有虚假的人工作证。

允许未完成来源记录保留在sources中供继续调查；它们不会使已验证的其他节失效，但引用这些记录的节保持pending。完整部分的来源门槛要求全部G及实际外部依赖验证通过，其余原创T/S采用独立审阅状态。来源JSON总status可为`requirements_satisfied`（兼容旧值`verified`）；验收器输出总来源状态为`requirements_satisfied`，逐节保留`verified`与`original_work_reviewed_separately`的区别。

## 操作顺序

1. 主代理保留旧快照并标识历史过度声明，更新当前文稿与范围，登记每节真实来源状态。
2. 来源已取得的节逐项写内容核验报告；不可访问或尚未读过的节继续pending，不能批量补verified。
3. 冻结新稿与scope后，重新做本轮math/ped审读、实际构建及视觉检查；各阶段据自身证据记通过。
4. 执行新验收器；即使四类阶段通过，专题来源未全齐仍输出pending。只发布如实标识为修订审阅稿的产物，不声称完整部分全部验收。
5. 来源补全时重新绑定当前版本、重跑门槛；不以历史push成功证明当前完成。

## 测试记录

实际检查时间：2026-11-05T09:46:29.148064+00:00。执行`python -m py_compile tools/validate_part1_acceptance.py`与`python /tmp/test_part1_revision_sources.py`，均退出0。所有测试写入独立临时目录，没有修改真实来源状态或真实验收JSON。

13个集成场景：完整合成来源签署accepted；缺来源台账、缺来源需求、G计划改general_method、一般来源替代专题、仅HTTP200没有内容审阅、取得/内容hash不符、以取得记录代替内容报告、缺精确位置、scope仍pending、目标不匹配、正文取得被阻断、漏节记录，这12种均pending。所有12个拒绝场景中math、pedagogy、build、visual各自仍为true，验证来源门槛确实独立。

另做2个真实数据来源单元场景：使用`part1_revision_sources.json`的CROSSREF-FORMAT真实取得记录及`part1_revision_sources.md`的实际内容核验，将目标严格限定为Work/Contributor中作者、编者、译者字段的区别，校验通过；把同一记录改用于00A30数学哲学需求，因专题/需求映射不符而拒绝。该单元测试不将任何真实00B节提升完成，也不宣称Crossref元数据文档是数学哲学、文学或十类文集的完整专题来源。

检查时文件快照如下；后续scope或报告修改应重新测试/绑定。

| 文件 | SHA-256 |
|---|---|
| `tools/validate_part1_acceptance.py` | `ca3006f300c5d26d432c15e9c8579644e05a6e65d0763ce21307afb6c6fd6539` |
| `research/production/part1_scope_plan.json` | `3aeb1cf9016bff206f29503d84704c43a221c37296442bb681c55ae7e2f2fee7` |
| `research/production/part1_revision_sources.json` | `ab060574581da3925342ef6ba33c6c898ff66b05f7e4b4e47fd24d0630c27f2d` |
| `research/production/part1_revision_sources.md` | `4751c128a03776da03c6c9a60d22a9af92b87207ae83f46feea8956fb0247cb5` |

历史实施记录：初次曾向scope的33节增补来源需求和pending状态，保留原学习目标和题答。该初版对T/S的逐目标外部来源要求过宽，本轮已撤掉；主代理负责把原创T/S改为空需求及独立审阅状态。本代理本次只改工具和本说明，不修改scope。G目标增补仍须同步其source_requirements.objective_ids。


## T/S原创工作边界修正及回归测试

时间：2026-11-05T09:51:15.574771+00:00。已撤销最初对所有T/S学习目标都要求外部来源对应的过度条件；G规则保持不变。本轮只改校验器和本说明，scope由主代理修改。

实际执行`python -m py_compile tools/validate_part1_acceptance.py`与`python /tmp/test_part1_original_source_exemption.py`，均退出0。旧13个来源门槛集成场景继续通过；新增6种检查通过：

- 原创T的空source_requirements与独立审阅状态可通过来源门槛；结果明确external_sources_verified=false。
- 原创S采用相同合法状态亦通过，不要求其例题出现在外部文献。
- G使用空需求，即使其他阶段全通过仍pending。
- 显式external_source_claims非空却试图采用原创豁免时pending。
- 混合S节仅为实际外部依赖目标提供已验证来源，其余原创目标由独立math/ped审阅，可通过。
- 来源需求已满足但缺独立数学审阅时，来源阶段可通过，完整部分仍pending。

合成测试不授予任何真实节完成。当前工具SHA-256：`f69009bae9423f9758fbba4c1d702b37818e6aa34289d80c10b27e39b4cc3b70`。

来源JSON里原创T/S的节记录必须同时改为`topic_source_status: "original_work_reviewed_separately"`及`requirements: []`，不能仅改scope。总来源状态通过时输出`requirements_satisfied`；每节是否有外部来源verified保留原有区别。与真实外引事实有关的正文检查仍属于实际独立审读职责，不能通过隐瞒external_source_claims获得语义保证。
