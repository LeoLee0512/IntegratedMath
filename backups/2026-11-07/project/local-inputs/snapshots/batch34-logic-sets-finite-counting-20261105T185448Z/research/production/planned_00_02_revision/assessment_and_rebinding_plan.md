# 00-02 独立来源充分性与最小重新绑定方案

审查者：`/root/part1_audit`。日期：2026-11-05。状态：**限定目标的证据充分；仅提出后续修订方案，正式来源账仍 pending。** 本轮仅写 `/tmp/part1-00-02-independent-review/`，不改第一部分源稿、计划、审签、收据或任何构建产物。

## 独立核读结论

实际读取正式 `part1_scope_plan.json`、`part1_topic_sources.json`、`part_opening.md` 与 `part1_research_exposition_followup.md/json`，再独立打开固定提交 `a04446e57ec1fbc252a871afcec7752fb2807b14` 的本地原生响应缓存：Schemes 503—590、Conventions 28—60、Introduction 16—44、COPYING 1—45。逐项核对 followup JSON 中八份持久缓存的真实 SHA-256，全部一致。没有重新联网请求，也未声称本审查者通读 COPYING 全文；来源代理的全文许可审读是另有署名的证据。

Schemes 原文确有 `lemma-standard-open`，并非仅项目说明：503—517 给 Spec(R)、D(f) 与对象背景；519—536 给带条件的引理；538—564 有完整 proof 环境和代数引理引用；566—590 说明层论依赖及标准覆盖。Conventions 明确交换含幺环、允许零环、幺模等约定。Introduction 自称从交换代数、概形与代数空间建立代数叠基础的 textbook，适宜称“研究性教材/综合阐述样本”，不宜称原始研究论文。

00-02 只有 G 目标 `00-02-1`“研究材料的核验边界”，需求 `00-02-topic-source` 明确 topic_specific。本次片段能真实示范：分别登记对象、全局/局部假设、结论、证明位置、所引先修及未核边界。故它足以补上原“只读 README”缺口，**在正式引用、映射和快照重新绑定并复核后，可把这一来源需求改 verified**。这不是审定引理所有数学细节，不是初学者已掌握概形理论，不是证明被引 Algebra/Sheaves/EGA，也不代表 Stacks 全项目或所有数学综述得到认证。其余 13 个 G 缺口不能借用该片段提升。

许可通知与 COPYING 对得上 GFDL 1.2-or-later、无 invariant/front/back cover texts。当前最小使用是固定链接、短书目信息和原创阅读说明；外部 TeX 缓存仍留 local-inputs，不能为了机器核 hash 将外部正文加入分发 ZIP。

## 最小正式改动面（必须等待第32批封存后）

1. 保全当前第一部分源稿、scope、来源账、math/ped/build/visual 收据及对应 dist/build/ZIP 的历史快照和 SHA。保留旧日期、旧 reviewer、旧13/14缺口判断当时的边界；旧产物可作为旧快照有效，不能写成新正文的已验收产物。
2. 在 `manuscript/review_ch01/part_opening.md` 的 00-02 阅读入口中加入固定 Schemes 定位和限制，采用来源代理 `/tmp/part1_00-02_minimal_revision_proposal.md/json` 的审定文本；不复制引理或长篇翻译，不改原目标、MSC、T/S/G 或其他章节。若当前 [S4] 仍指 README，明确新链接是专题正文实例、README只是项目说明，避免把两者混为同一核验。可用正文直接固定链接以最小化改稿；若确需更新附录 [S4]，`appendices.md` 也纳入差异审查与新快照，不能只改标签不重绑。
3. `part1_scope_plan.json` 只将 00-02 的 `topic_source_status` 改 verified；保留 `00-02-1`、`00-02-topic-source`、topic_specific、全部排除范围与33节清单。不要把源文件路径或原需求换成更容易通过的无关目标。
4. `part1_topic_sources.json` 新增 `SRC-S4-STACKS-SCHEMES`；仅映射该需求/目标。对应 section 和 requirement 改 verified，其余条目逐项保持；counts 更新为 G verified 5 / pending 13 / T-S original 15，整体 status 仍 pending，只删除 00-02 那条已补缺的现时 blocker。旧 README source 及历史记录保留。将顶层 `plan_sha256` 和八个来源快照重新计算为真实当前值，不照抄提案预设值。
5. 新 source 的 access evidence 绑定真实获取记录 `part1_research_exposition_followup.json`，content review evidence 绑定独立内容叙述 `.md`，两者不能是同一路径。补足 `content_review.reviewed_at`、`document_sha256` 与 evidence；其文档 SHA 必须等于实际 Schemes 响应 SHA。报告中目前 `proposed_source` 尚不是可直接接入的完整正式记录，需这些明确字段。内容 coverage 必须精确包含 `00-02`、`00-02-topic-source`、`00-02-1`、topic_specific、source_location/verified_claim/limitations。followup 报告自身若改字，必须先冻结其最终 hash 再绑定。

## 哪些现有 gate 会失效

| 改动或验证环节 | 当前实现的行为 | 安全处理 |
|---|---|---|
| 仅改 part_opening 正文 | `source_binding()` 要求八文件精确快照；旧 math/ped/source/build 均报 Exact source snapshot mismatch | 保留旧签，独立审读差异后建立新快照审签 |
| 仅把 scope 状态改 verified | 全 scope 文件 SHA 改变；旧 math/ped/source/build 均报 Scope plan hash mismatch | 即使数学正文不变，也须明确新计划与旧目标对照后重新签署，不只替换旧 JSON hash |
| 只加 ledger 映射，不改 scope | `topic_source_section()` 仍因 scope 的 pending 拒绝 00-02 | 不利用 ledger 单方面提升；两份声明须匹配 |
| 新来源只写 HTTP200/获取记录 | 缺实际 content review 或其 evidence 与 access 相同即拒绝 | 保留获取与内容核验两个不同证据路径 |
| 第一部分旧 build | 除 scope/source 绑定外，还核 build_input_sha256、PDF/HTML/MD/ZIP 产物及 ZIP 中实际源文件 | 重新构建；不能只改 build report 中的 hash 或 command 冒称已执行 |
| 第一部分旧 visual | 必须有当前有效 build；再核 exact artifact map、build_review SHA、截图 hash 与全部PDF页覆盖 | 新PDF实际看图后新签；未变纯目录PDF可在确证字节不变且原完整看图证据可核时明确继承依据，不伪造重看日期 |
| 旧 part1_acceptance / production ledger | 旧收据只是旧快照；`part1_ledger.refresh_part1()` 实际重跑 Validator，不信已有 accepted 字段 | 所有证据完成后重生成；新完整部分仍 sources pending13，不标整章/部分完成 |
| 全书旧 batch build 导入 | `aggregate_build_reviews()` 逐一核 aggregate source_sha256；其中 part_opening 一变，整份旧构建导入失败 | 旧基础单元数学/教学不因本改动消失，但所有依赖旧 aggregate 的 build 状态应如实 pending，直到新全书产物及页面重新验收 |
| 第32批正在进行的 builder/validator | `validate_learning_batch` 最前/最后都比较真实 source_hashes 与构建 manifest | 当前冻结期不能动ch01；先封存第32批，再启动独立版本修订 |

特别注意：即使 scope 只改一个来源状态而所有 PDF 正文不变，当前第一部分构建输入也包含 scope 文件；不能为节省工作关闭该 gate。来源 ledger 本身不直接属于现 build_input_sha256，但它改变的验收结论需要新 receipt；不因此把 ZIP 或总验收 hash 当成仍相同。

## 建议执行顺序

第32批 B4.5—7 完成全书构建/视觉/包验证并封存 → 保存第一部分现行历史快照 → 冻结最终来源报告与精确修订文案 → 应用最小正文/scope/source ledger 差异 → 两名独立且不同于作者的 math/ped 审阅者检查新增文字及scope差异、以原33节有效证据加明确差异审查形成新当前签署（未改32节无需假装重写证明）→ 执行来源逐节验证，预期00-02 verified但总来源仍13项pending → 重新构建第一部分并实际检查新PDF → 新 build/visual 报告按实物hash签署 → 重跑总验收、全量台账 → 按用户已授权的后续批次安排全书重新组装和视觉；在此之前旧全书构建仅保存为历史。

保护旧根 dist/author 的 `protected_sha256` 不可为获得通过而手改：第一部分 `check_build_inputs()` 会比较当前保护清单与其构建启动快照。若全书继续生产导致环境不一致，应重新启动对应第一部分构建，或保留明确pending原因，不能篡改原签署。

本方案不要求改验收器，不增减章节，也不增加作者批准门槛；作者审阅仍是独立 pending。通过单个 G 来源需求仅表示这个有限导读入口有真实内容支持，不等于完整数学教学。

## 可复跑验证

`check_gate_impact.py` 只读仓库，在内存模拟旧签的源/计划失配；输出 `gate_checks.json`。正例为00-02完整限定来源映射，反例包括仅映射不改scope、general_method、错误目标、获取记录冒充内容报告。所有预期均成立。两个失配模拟中 math/ped/source/build 逐项失败，visual因缺有效build失败；没有写正式receipt或修改签署来“通过”模拟。

本报告与模拟结果由审阅者保存于 `/tmp`，待主代理决定后续独立版本实施；当前正式来源状态和产物一律不动。
