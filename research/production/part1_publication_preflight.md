> **历史失效说明（2026-11-05修订）**：以下为de08a8a旧稿的发布准备记录，不证明本轮改稿、源文件、远端差异或推送已通过。原样版本保存在[历史归档](history/de08a8a/research/production/part1_publication_preflight.md)。当前发布状态须以本轮实际核验及推送回执为准。

# 第一部分源码发布准备审计

审计时间：2026-11-05T08:27:41.879962+00:00。审计者：`/root/part1_sources`。只读审计，仅写本报告；没有联网、提交、拉取、推送、移动工作区或读取凭据。

## 结论

在已经提供的5个远端文件中，逐块阅读远端→本地完整差异，**未发现本地稿会删掉远端新增而本地未知的用户内容**。远端第1章正文和答案恰好对应2026-10-27 R1—R4初审前的已知快照；本地保留其章节、例题、14道题、解答结论与原有权利说明，增加已复核的教学桥接和本轮G导读定位。开篇“第2章本次不写”被当前第二章草稿/验收边界替换，这是本轮范围更新，不是遗失远端独有段落。

**这一结论只覆盖指定5文件，不是远端全树无冲突认证。** 新增工具、样式、数据、README等路径在本次提供的远端快照中没有逐一取得，发布准备时须按精确路径再次比较。`backups/`完整保留、未触及其他根目录文件，须由最终暂存差异和远端基底树核查，不能由本报告的5文件比较代替。

## 基底与比较方法

- 远端工作分支tip（父代理本轮ls-remote确认）：`229f3f86cdcdef15eb8ec8fb519c44d31e58146d`。本代理未重查网络，固定远端内容来自`local-inputs/part1-remote-comparison/`。
- 本地主工作区：`/workspace/IntegratedMath-book`，HEAD：`a9363f607a818f69d77e8723ac3d3e5666ca4026`；本地工作树含未提交修改与其他基础批次草稿。
- 依次比较远端文件→本地HEAD、远端文件→当前工作文件，并逐段对照历史`research/production/ch01_review_2026-10-27.md`及本轮独立审读记录。未只依赖diff行数。
- 本地未拥有远端tip对象这一前提来自父代理；本报告不推断两条历史祖先关系。以远端tip为唯一父提交准备普通后继提交，既有远端文件保留，然后仅应用明确源码路径差异，是可审查的处理方向；本轮不执行。

## 五文件差异逐项判读

### EDITORIAL_POLICY.md

远端101行版本与本地的共同部分相同。本地末尾新增“2026-10-27 全书持续生产授权”：持续按先修生产、第一章补强后进入第26章、保持分类与未写状态、当时限定本地写作。这一段已在本地HEAD中，不是本轮临时新增。没有删除远端原“先提建议并明确同意”、权利边界、T/S/G或发布历史规则。

发布时不能把这段历史授权中的“本轮不据此推送”伪装成新推送授权；实际新动作依当前用户授权。若纳入政策，应保留其日期/历史语境。它不是构建器的硬依赖；亦无需为发布第一部分搬入其提到的整套第26章文件。

### manuscript/review_ch01/part_opening.md

远端首段明确“第2章对应会议文集与论文汇编，本次不写”；本地HEAD曾改为接续自然数基础且第2章待写；本轮工作树改为第2章新增正文和整体完成状态由审校台账确定，并保留其他部分基础单元的独立路线。两个直属节依旧归00-XX，未并入第1章。

本轮新增“阅读入口与边界”：00-01回链第3/4节及S1；00-02说明对象/假设/结论/证明定位和S3；区分阐述层次与汇编形式；以S4 Stacks README作研究对象定位，公开抽象代数等先修未在本章建立。既有两节原文均保留，没有以新增介绍替换远端数学论证。

### manuscript/review_ch01/chapter.md

远端SHA256与2026-10-27初审快照一致。逐块差异分成两组：

1. **本地HEAD已有修订**：R4把解限定在允许范围，明确自然数答案在整数中做减法；R2解释字母并置、纯数字位值与u+u=2u的分配律依据；R1解释分子/分母及乘逆元，按交换、结合、逆元、单位元推出约分，零分支保留；另明示零与一不同。其内容与历史复核记录对应。
2. **本轮补充**：新增20—40页规划与三段连续阅读安排；六个G节分别加入先修、目标、相邻主题及不覆盖范围。00A17明示假设性书评例非真实书评；00A27不宣称实时问题清单；00A30/S2只支持量词；00A64不把逻辑来源当文学研究书目；00A99不把余类当可信度认证。其余修改是把既有“第X节”变成原锚点链接（术语表、模型、例题和习题等），没有改变题目条件或答案。

未删除远端任何节、证明结论、例题或题目。被替换的约分“口诀”与同类项直观说明分别升级为完整依据，而非移除数学内容。R1—R4修订已在2026-10-27旧复核中说明；本轮完整部分审校仍须绑定新快照。

### manuscript/review_ch01/answers.md

远端SHA256与2026-10-27初审答案快照一致。HEAD已有R3把题1“左侧相反数化简”和“右侧数值计算”拆成两步；答案2加自然数范围与第5节锚点（R4）；答案7明确调用第14节逆元证明、第二因子替换及非零条件（R1）。本轮其余差异仅将答案4/6/9/10/12/13/14原节号改为稳定回链。14份解答及结论均保留，无远端独有答案被丢弃。

### manuscript/review_ch01/appendices.md

远端与本地HEAD相同。本轮只追加来源核验边界与S4：S1/S2本次重取元数据，具体模块内容仍用2026-10-21旧核验；书评/开放问题/哲学/文学候选被代理阻断，不冒充已读；Stacks只读README、未审定深定理或许可。原S1—S3、四图清单与模拟附录没有删除或扩大转载授权。

## R1—R4与本轮补充的可追溯分界

| 变化 | 所属阶段 | 证据 |
|---|---|---|
| 分式记号、逆元约分、答案7复用 | 2026-10-27 R1 | 旧审阅“修订后复核”与本地HEAD |
| 字母并置、u+u=2u依据 | 2026-10-27 R2 | 同上 |
| 答案1拆开左右两侧化简 | 2026-10-27 R3 | 同上 |
| 解的范围、整数运算桥接、答案2范围 | 2026-10-27 R4 | 同上 |
| 零与一不同 | 2026-10-27附带精确化 | 同上 |
| G先修/范围/邻类/S1—S4定位、阅读安排、电子回链 | 2026-11-05本轮 | 当前工作树相对HEAD |
| 第2章10节及6题答案、33节范围计划、新构建与验收 | 2026-11-05本轮新增 | 5文件之外的独立新增文件，不在远端逐diff范围内 |

## 可重建第一部分的确切最小源码闭包

以下18个路径是当前独立构建器+全范围验收器的最小源码文件集合。**集合不等于18个文件全部需要重写远端**：远端已有且字节相同的保持不动；已有但不同者逐diff处理；缺失者才新增。三份分类台账必须作为相互匹配的一组使用，不能混合不同快照。

```text
manuscript/review_ch01/part_opening.md
manuscript/review_ch01/chapter.md
manuscript/review_ch01/answers.md
manuscript/review_ch01/appendices.md
manuscript/review_ch02/chapter.md
manuscript/review_ch02/answers.md
research/production/part1_scope_plan.json
tools/build_part1_review.py
tools/validate_part1_review.py
tools/validate_part1_acceptance.py
tools/build_full_catalog.py
tools/ch01_simulation.py
tools/draw_ch01_figures.py
tools/pdf_header.tex
tools/style.css
data/msc_taxonomy.json
data/catalog_titles.json
data/catalog_titles_zh.json
```

其中计划source_files恰为六份稿件、模拟代码和绘图代码共8个文件。新构建器直接需要`dist/综合数学_完整数学目录.md`和四个`figures/ch01_*.png`，但不会自行生成它们，因此干净源码检出的构建顺序应明确为：

```bash
python tools/build_full_catalog.py
python tools/draw_ch01_figures.py
python tools/build_part1_review.py
python tools/validate_part1_review.py --package
```

这些是后续在干净验证环境运行的命令说明；本审计没有执行。没有用户原PDF时，目录工具自动使用完整性检查的`catalog_titles.json`缓存，再核对中文翻译与分类身份；无需上传MSC原始PDF、抽取全文或额外翻译中间块。绘图脚本生成四张原创图，无需复制旧产物。以上命令只要求已有Python环境、pandoc、XeLaTeX、PyMuPDF、Pillow、matplotlib，以及Noto CJK/DejaVu字体和所用LaTeX包；本审计不安装。`--check-deps`检查不覆盖matplotlib、字体与全部TeX包，因此最终仍以真实干净构建为准。

目前build_part1_review的哈希清单含生成目录、图像和部分构建脚本，**不含目录生成器build_full_catalog.py及验收器validate_part1_acceptance.py**。两者仍是发布源码依赖，应在发布文件清单/源码receipt另存哈希；不能因为不在build manifest内就漏发。

## 来源与审校证据的最小随附文件

为使正文所引旧/新核验和完成声明可追溯，还应保留以下文本/JSON；它们不是额外教材批次：

```text
research/ch01_source_checks.json
research/ch01_source_checks.md
research/production/ch01_review_2026-10-27.md
research/production/part1_sources_2026-11-05.json
research/production/part1_sources_2026-11-05.md
research/production/part1_ch02_draft_scope.md
research/production/part1_math_review.json
research/production/part1_math_review.md
research/production/part1_pedagogy_review.json
research/production/part1_pedagogy_review.md
research/production/part1_acceptance_interface.md
research/production/part1_acceptance_tool_checks.md
research/production/part1_publication_preflight.md
```

第2章Crossref资料的URL、版本、请求字节/哈希和deprecated边界目前写在`part1_ch02_draft_scope.md`，因此不能只带正文而丢掉该证据。R1—R4旧记录支持差异来源，不代替本轮33节审校。scope_audit、resume_inventory和ch01_independent_review可作为历史过程记录附带，非最小运行依赖；要保留其快照/缺口日期，不能把早期pending描述当当前最终状态。

正式里程碑还需最终`part1_acceptance.json`、构建/视觉报告及其文字证据（按最终receipt的evidence递归确认），以及单独的source-only发布清单/回执。此时构建/视觉证据尚由其他执行者继续产生，本报告不猜测其最终哈希或声称已验收。计划、math/ped报告必须保持与最终源码字节绑定。

**源码发布与完整本地验收分开。** `validate_part1_acceptance.py`会实际读取PDF、HTML、ZIP及截图；源码检出没有这些产物时返回pending是预期行为。不得为了让远端源码检出立即accepted而上传禁止的PDF/ZIP/截图，也不得改验收器跳过证据。源码receipt可以记载本地完整验收的结论与产物哈希，明示产物未进入本次Git提交；之后读者按源码重建并重新完成视觉验收。任何重建的产物与旧哈希不符，都须形成新证据，不能沿用旧accepted。

## 无需带入的本地全量生产系统与其他批次

父代理已确认本次以独立part1计划与receipt记载里程碑，因此**最小发布不需要**`tools/part1_ledger.py`、`tools/build_production_ledger.py`或`data/production/*.json`的整套本地覆盖。part1_ledger仅为全量生成器接入辅助，不是独立build/validate的import依赖；本地照常保留，不移除、不迁移。

如果另行决定在远端接入全量生成器，不能只发当前build_production_ledger.py而漏part1_ledger.py（其3473行硬导入）；也不能仅搬辅助模块就声称63部分台账全部同步。全量生成器登记了大量基础单元与审阅路径，直接覆盖可能生成源文件缺失或跨批次状态变化，须单独审计。

本次不带未提交batch31的real_sequences_order、real_subsequences_bw等正文/审校，亦不复制build_learning_batch.py、validate_learning_batch.py、accepted_reviews.json及全量chapters/sections/units/prerequisites的当前变更。README/PRODUCTION_PLAN/LEARNING_PATH已有本地综合批次改动，不能整文件直接覆盖远端；若需第一部分入口，仅在远端版本基础上增加独立part1命令和状态段。不会因此改写本地主工作区这些文件或把batch31变成已发布。

## 远端保存与禁止进入本次提交的内容

- 以指定远端tip为基底作普通后继提交；实际提交前再次确认目标tip。若远端移动，重新基于新tip核对，不强推、不把本地HEAD当远端替代。
- 不执行全树同步或带delete的拷贝；只应用明确源码路径。所有远端`backups/**`保持文件字节、路径和已有历史，不在根目录再复制一份；本地主工作区保持原位。
- 不新增或修改`dist/**`、`build/**`、生成PNG、PDF、HTML、ZIP、缓存、`local-inputs/**`或用户原始附件。远端历史已有二进制不属于本轮清理范围，保持不动。
- 本地`.gitignore`已忽略dist/build/local-inputs及四张生成图；若远端已有不同规则，须保留并最小追加所需规则，不整文件盲覆盖。
- 最终检查必须覆盖全部拟发布路径及其模式/哈希，并证明backups树未变、没有带入batch31或本地机器文件。当前只检查5个远端文本，不能替最终暂存审查。

## 本次五文件身份

| 文件 | 远端SHA-256 | 本地工作树SHA-256 |
|---|---|---|
| `EDITORIAL_POLICY.md` | `cbaf60a5d7f2268d01cd4aee3bf25cd9ec15f68542f259c71b619bd2236d151f` | `8e7ec826e63ea6f64de5b47fb1ecd68917e5a10c63357aab960c029c042d9b11` |
| `manuscript/review_ch01/part_opening.md` | `73b5b14fd411e735f8e999bf4bca0ba2fe0ddc40574422fc2de6fd593fb1cf93` | `5130b7cdb3ddc654aeb94adbbe2923ae21c3ce9a66681f1a58c60754333a2acd` |
| `manuscript/review_ch01/chapter.md` | `f8bc321bfc7dcba70cc6371f1678bf330355eb2611e3bda3ae9055c4a608d86f` | `c04082871e3595819417e02ae730429790e8a5db2f233ce85caae7351293cacb` |
| `manuscript/review_ch01/appendices.md` | `1fe9c2d9ae018a188b76162ebb156227ad76d09358e44cb97b4d657d0494cb8e` | `d16702d5411e5270a02963ae046a38c944b64e35d45adba3b4fffac86a4a2ae9` |
| `manuscript/review_ch01/answers.md` | `63381460c90e3a6df6ec6e6695381857cf4679d014955455730d0fd1255cb998` | `506ea09593899622099c9fb3ac9821a407630ccb50dfba5cade93a5f117e0251` |

上述哈希绑定本次审计快照。之后任何正文或计划变更都应重新核对受影响差异与审阅证据。此报告不构成已推送、已提交、已保全完整远端树或已完成视觉验收的声明。
