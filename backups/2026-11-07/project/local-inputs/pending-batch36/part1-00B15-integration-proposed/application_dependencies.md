# 00B15 下一轮应用依赖清单（只读调查，未执行）

2026-11-05，/root/part1_sources。调查对象是当前正式 75 单元工具及本目录已准备的 00B15 候选；**仅供批次 35 封存后，在批次 36 一次整合时使用**。本记录不修改任何正式文件，不新增网络请求，不运行构建。行号是调查时的位置，后续以函数名/字符串确认，不作盲替换。

## 1. 最小实质输入及证据

| 文件 | 下一轮触达原因 |
| --- | --- |
| `manuscript/review_ch02/chapter.md` | 00B15 限定选读 + 来源说明 C2-S4；旧真实文档实践和题目逐字不动 |
| `manuscript/review_ch01/appendices.md` | 更新来源状态说明；只用“见第二章来源说明[C2-S4]”纯文字，不能引入独立第一章缺失的跨章锚 |
| `research/production/part1_scope_plan.json` | 仅 00B15 的 topic_source_status；所有目标、先修、27 组题答不变 |
| `research/production/part1_topic_sources.json` | 新 source、00B15 requirement、计数 9/9/15、删除该项 blocker、计划/八源绑定与真实应用事件；整个部分仍 pending |
| `research/production/part1_dedekind_00B15_{evidence.json,content_review.md,root_mapping_review.md,integration_review.md}` | 候选已包含的四份获取、内容、独立映射与整合记录，分别按实际 hash 持久化；不复制外部原文 |
| audit 本轮实际 delta 报告及其绑定记录 | 待 audit 完成再纳入；不能提前补“通过”或替换旧签 |

先核本目录 manifest 中四实质输入的 base hash；若已经变化，需要复核差异。保存旧 scope、ledger、数学/教学/构建/视觉记录及旧构建产物的既有封存。正式应用时将 proposal_only 及拟议事件改为实际事件，追加真实时间与基底；不能删旧历史，也不能把旧顶层 reviewed_at 冒充本轮整合审读。按最终实际字节重新计算 plan 和八源；候选当前绑定仅是预计值。

## 2. 后续工具中的固定计数与披露

| 当前位置 | 本次发现 | 下一轮应处理 |
| --- | --- | --- |
| `tools/build_learning_batch.py:1618` `check_batch35_prerequisites` | 当前针对 75 单元/当前批次；1637–1641 同时检查 ledger.counts 与 sections 的 8 verified、10 pending、15 original | 在下一批工具版本中改为 9/9/15，并保留双重校验，不能只改显示文字 |
| 同函数 1642–1654 | 现有 ten-gap 错误信息、00B05 在 plan/ledger 中 verified、摘要 source.content_review verified、plan hash 与八源精确绑定 | 保留 00B05 已核条件；增加 00B15 在 plan/ledger verified 和 `SRC-C2-DEDEKIND-ESSAYS` 实质记录存在/已核的检查。建议沿现有 validator 核证据/覆盖；至少不要只凭计数替换认定新来源存在 |
| `tools/build_learning_batch.py:1666` `compose_body` 导读 | 固定“第一部分10个G节的专题来源仍待核实” | 下一轮改为 9；整部分未完成披露必须保留 |
| `tools/validate_learning_batch.py:2636` | 导读必含字符串要求同一句“10个G节” | 与 builder 同步为 9；保留所有其余检查 |
| `tools/validate_learning_batch.py:31,2544` 与 builder:2654 | 导入/调用 check_batch35_prerequisites | 若批次 36 重命名 guard，一并更新调用；不能留下导入旧函数。改名不是本次来源变化的必要条件，可与下一批命名整合决定 |
| `tools/build_learning_batch.py:331–340` `source_hashes` | 已登记 scope/ledger 与过去来源记录，但没有新 Dedekind 四记录 | 将四个最终 research 路径及最终独立 delta 报告纳入输入清单，防止证据在构建后变更却未使批次报告过期 |

00B15 自身不改变单元数、练习总数、图数、目录部/章归属或既有 75 单元顺序。未来批次 36 若同时增加 FSP 等单元，其注册与数量变化属于另一独立变更；不能把此清单当作已授权注册未冻结新稿。不要全局替换数字 8、9、10、75 或“十”：十个 00Bxx 叶项仍是十个。

## 3. 八源及验收绑定传播

scope 的 source_files 仍是原八文件：第一章 part_opening/chapter/answers/appendices，第二章 chapter/answers，ch01_simulation.py 与 draw_ch01_figures.py。本来源补充只改变其中 **第一章 appendices 与第二章 chapter**；其余六个内容哈希应保持原值。scope 自身因单项状态改变而产生新 hash。

- `part1_topic_sources.json` 的 plan_sha256/source_sha256 随之更新；新 access JSON 和 content/root MD 使用不同证据路径及各自真实 hash。整账 status 仍 pending，九个 blocker 原样保留。
- `part1_math_review.json`、`part1_pedagogy_review.json` 都被 `validate_part1_acceptance.py:112–114` 精确绑定计划与八源。需独立实际 delta 审读后才形成新签；旧整稿审读历史保留，不仅替换 hash。
- `part1_build_review.json` 同样绑定计划、八源、实际工具输入、MD/HTML/PDF/ZIP及检查；旧报告不能代表新版。`part1_visual_review.json` 还依赖已通过构建和实际 PDF/截图 hash，旧看页不能直接沿用给新 PDF。
- `tools/validate_part1_acceptance.py` 的专题 gate 逐项目核来源、要求所有 G 满足；它没有应该改成“9项即可整体完成”的阈值。**不要放宽该 validator**：九项 pending 存在时，完整第一部分仍不通过。
- `tools/part1_ledger.py:refresh_part1` 每次使用当前计划/四审签/来源账重新验收；完整 part/chapter/section 的完成状态仍不得提升。没有必要为仅此来源补充改 foundation `accepted_reviews.json` 的旧 150 个审签。

## 4. 构建复用、验收和包装的失效链

第一章附录属于 `tools/review_artifacts.py:source_hashes` 的 review_ch01 全部 Markdown 输入，也是 `build_ch01_review.py:52` 真实装入正文的文件。因此它不是“只有元数据变化”。

- `build_learning_batch.py:reuse_legacy_snapshot` 逐哈希检查旧第一章输入；改附录会使 `--incremental` 的 legacy reuse 失败。下一轮需要一次新第一章构建/校验，不能绕过失败复用旧 PDF。
- 常规 `build_learning_batch.py` 主流程在不带复用参数时先执行 legacy 构建/校验。若由 root 先独立完成同一最终输入的 legacy 构建，可以依据真实新 manifest 再选择受校验的复用路径；不能对旧输入直接加 `--reuse-legacy-validation` 强行续跑。
- `build/learning_batch/build_inputs.json`、legacy snapshot、`data/production/batch_validation.json` 随当前完整 source_hashes/artifact_hashes 更新。旧截图/PDF、页数、批次视觉记录须按本轮实际输出检查；无法预先认定增补段落不影响后续分页。
- `tools/build_part1_review.py:source_hashes` 直接绑定计划和八源；若此次还交付独立 dist/part1 版本，同样必须实际重建/看页。若本轮只交付基础续写包，就明确独立 Part1 旧构建签已过期，不能更新 hash 假装完成。
- `tools/package_learning_batch.py:16` 检查批次报告的源/产物精确映射；随后检查实际视觉绑定，最后验 ZIP 每个成员。新增 research 记录会被其现有 production/*.md/json 模式包含，不需上传外部缓存。不复用旧 ZIP 或旧 package_validation。
- `build_production_ledger.py:aggregate_build_reviews` 在实际视觉通过后才导入 batch build stage，并检查每项输入 hash。因此新报告/新产物准备完再刷新生产账/receipt；不从 old batch report 预先生成 accepted。

建议一次整合顺序：封存35 → 审完最终00B15与下一批单元差异 → 同时落全部正式输入/证据/guard/披露 → 算最终源hash并独立审签 → 一次完整构建/自动检查 → 按实际PDF看页 → 包装/刷新生产账/核包。构建后的记录更新若属于 source_hashes 输入，会再次使报告失效，故应在构建前冻结。

## 5. 单独发现：editorial_plan 的旧当前状态

只读发现 `data/editorial_plan.json:839–875` 仍含旧 4/14 计数、旧 scope/source hash、旧 50/267/218 页声明，并将这些写作 current_part/completion_note；它与当前正式 8/10 ledger 已不一致。此不是本提案引入，也不是来源充分性的额外阻断，但会进入 `package_learning_batch.py` 的文件清单。

本轮未更改该文件。建议 root 在批次 36 集中整合时明确处置：若它继续作“当前”编辑状态，更新对应来源状态/代码列表/计划与账哈希，并将旧构建页数移为有日期的历史事实；全 part 保持 pending、作者待审。不要把这个旧4/14快照误当本轮8/10基线，也不要只改4→9而留下14和旧hash。应保留原文件历史；此项待 root 决定，不擅自扩大本候选四实质文件范围。

调查结束：无正式修改、无工具修改、无构建、无网络请求。当前候选 diff/manifest 不因本清单而重写。
