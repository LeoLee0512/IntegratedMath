# 00A30 数学哲学：限定来源阅读与映射建议

审读时间：2026-11-05T16:42:56.139796+00:00。本记录只提出后续修订建议；未改冻结的第一部分正文、scope、来源账、验收状态或构建。正式 00A30 仍 pending。

结论：已取得并针对性阅读 Bertrand Russell 的 *Introduction to Mathematical Philosophy* 历史文本，实际内容足以作为 00A30-1「数学陈述与认识边界」的一个专题导读入口，尤其支持论证起点、未定义项与定义、公理解释和给定假设内推导的区分。它不能充当现代数学哲学全景、学派裁决、当前共识或本书数学命题的证明。建议根代理独立核读后，在下一版补入明确的历史限定及固定引用，再决定该单项 requirement 是否 verified；本记录不自动改变任何 gate。

## 身份、取得链与版本

实际 GitHub 仓库搜索仅得到相关 GITenberg 仓库；随后读取仓库目录，确认 commit `7f4e90716794406bb99e227bedc1c6c465bc53b2`，根目录中的 README.rst、metadata.yaml、LICENSE，以及子目录中精确的 `41654-t/41654-t.tex`。七次公开请求均 HTTP 200；完整 URL、UTC 时间、字节数和 SHA-256 见同名 JSON。没有请求 Stanford 或其他曾 CONNECT 403 的站点，没有代理镜像、额外代理、登录或大型 clone，也没有访问 Gutenberg 或 Internet Archive 原站。本次是用户明确允许的 GITenberg 档案调查，不把它包装为被封来源的替代访问。

仓库 README 自述它是此书的源文件档案，metadata 给出作者 Russell、书名、Project Gutenberg 图书号 41654、Mathematics -- Philosophy 主题。已核的是这个公开档案的自述及其实际文本之间的一致性；它不是作者机构的官方现代校订版，也未核对纸本扫描。固定版本链接：

- [实际 TEX 正文](https://github.com/GITenberg/Introduction-to-Mathematical-Philosophy_41654/blob/7f4e90716794406bb99e227bedc1c6c465bc53b2/41654-t/41654-t.tex)
- [元数据](https://github.com/GITenberg/Introduction-to-Mathematical-Philosophy_41654/blob/7f4e90716794406bb99e227bedc1c6c465bc53b2/metadata.yaml)、[README](https://github.com/GITenberg/Introduction-to-Mathematical-Philosophy_41654/blob/7f4e90716794406bb99e227bedc1c6c465bc53b2/README.rst)、[仓库 LICENSE](https://github.com/GITenberg/Introduction-to-Mathematical-Philosophy_41654/blob/7f4e90716794406bb99e227bedc1c6c465bc53b2/LICENSE)

文本扉页行 625–629 声明初版 1919 年 5 月、第二版 1920 年 4 月，并保留历史版权页文字。这是所读电子档案所载版次，未独立鉴定纸本。metadata 的 `gutenberg_issued` 为 2012-12-18，实际 TEX 页首行 539 记电子书 Release Date 为 2013-02-17，两者均保留，不混写成一个日期。metadata 的 `_version: 0.1.0` 是档案元数据版本，不是 Russell 著作版次。实际文本源头自述为 OCR 加校对；本次没有追溯读取扫描底本。固定 commit 只锁定本次档案内容，不证明它是最新学术版本。

## 实际阅读范围与内容支持

使用原始字节 SHA-256 固定内容；TEX 为 ISO-8859-1，含 CRLF，行号按原文件逐行计数。正文全文已取得，但只将下列实际读过的段落列作内容证据，不宣称全文审读。

| 原文件行段 | 阅读内容的原创概述 | 对本节的限定支持 |
| --- | --- | --- |
| 625–686 | 所载版次与作者序言；作者自己限制本书为引论，并区分已有确定结果与仍待探讨的问题 | 适合标为历史导读，不能据此宣称争论终结 |
| 769–810，印刷页 1–2 | 作者区分从采用的起点向后推演与向前分析起点的概念和原则，并说明区别也在研究兴趣和阶段 | 直接对应本节「在规则下推出」与「反思所取起点」的区别；不是一切哲学问题的定义 |
| 863–889，印刷页 3–4 | 熟悉数的使用不等于已经分析其定义；有限的定义过程须暂从未定义的项开始，作者没有断言存在永远不可定义的绝对终点 | 支持把对象、定义和起点分开说明，不把术语熟悉当作理由充分 |
| 923–1017，印刷页 5–7 | 作者介绍 Peano 的原始项和五项前提，并说明在相应假设及逻辑推导条件下得到算术结论 | 只读为该历史作者呈现的条件结构；不将其关于全部数学归约的宏大判断当作现代定理 |
| 1018–1159，印刷页 7–10 | 作者用不同对象及后继解释说明同一组前提可有不同指称解释，继而区别满足形式性质、存在实例及日常计数意义 | 真实涉及对象与公理解释的哲学问题，足以补量词教材所不具备的专题入口；不把这段历史阐述改写成现代一阶模型论/范畴性定理 |

另实读 README 与 metadata 全文、仓库 LICENSE 全文、作品嵌入许可行 9333–9694，以及档案页首、转录说明与版本标记。对 Chapter I 的未列行段、后续章节、外部 Frege/Peano 著作、Russell 后续立场变迁与当代哲学争论均未作核验。

## 许可与地域边界

metadata 明确仅称美国公有领域；嵌入作品许可行 9352–9367 也按美国版权和 Gutenberg 商标条件表述。嵌入许可 1.C/1.D（行 9408–9432）将美国情况与其他地域区分，明确不对美国以外版权地位作表示。不能从 README 的简写推断全球公有领域。

仓库根 LICENSE 含一个带星号的「特定作品有版权并获许可」模板段，末尾又说明该段只适用于有版权作品；实际作品 TEX 的 1.C 和 1.D 之间没有该段。这是根通用模板与作品特定文本的差异，不能据此编造作者授权或消除地域限制。所载历史版权页文字也不能单独代替当前权利判断。保留这项差异；如将来需要转载原书，需按具体地区和实际用途另核，当前没有作这种授权。

本轮用途严格为链接、书目信息、哈希、阅读位置及原创概述；不复制外部正文到本书或报告，不把本地缓存加入发布包，不提供全球再分发许可。原文件现保存在 Git 忽略的 `local-inputs/part1-math-philosophy-source-cache/` 供独立复核，已用 `git check-ignore` 确认；缓存不加入发布包，路径不是出版附件。

## 最小映射建议（未应用）

- 候选 source id：`SRC-S5-RUSSELL-IMP-HISTORICAL`；建议书目标签 S5（现正式附录仅到 S4）。
- 唯一新增 requirement 映射：`00A30-topic-source` → `00A30-1`，类型 `topic_specific`。S2 继续只承担量词逻辑核对，S3 继续只承担分类，不给它们扩大含义。
- 内容状态建议：`content_verified_for_limited_historical_reading`；正式 scope/ledger 当前仍 `pending`，等待下一版实质补入入口与独立核读、重建和重新签署。不得只换 hash 沿用旧签。
- 可补的原创导读段建议：历史阅读可从 Russell《Introduction to Mathematical Philosophy》第一章开始：他区分采用起点进行推导与分析这些起点，又借原始项的不同解释讨论形式条件与对象意义的关系。这里把它作为 1919/1920 年著作所载的一种问题提出方式；不由此宣布某种数学哲学立场正确，也不把其中关于数学基础的历史判断用作本书定理。量词例子的具体逻辑核对仍见 S2。
- 可补的书目内容：作者、书名、所载第二版 1920 年、GITenberg/PG 41654 固定档案 commit、Chapter I 指定行段链接、美国公有领域的档案声明及美国以外权利未核说明。不得写成「现代数学哲学已全部核验」或「全球公有领域」。

仍未解决：哲学诸学派的现代比较、真理概念的完整讨论、所有哲学争点、全球再分发权利。它们并非本节已定的窄范围目标；若后续扩大目标，应重新评估来源充分性。00A17、00A27、00A64及其他现存来源缺口完全不因本项而改变。是否与已提出的 00-02 方案同批应用应由主代理决定，不在此累计修改正式计数。

## 本次读取基线

- `research/production/part1_scope_plan.json`：`9d542b4dba6cdbefed6a8529a2f3d4b3562dff9d62f3800d692e64435ade21de`
- `research/production/part1_topic_sources.json`：`9d8872b38cb3602a73921c3f6c27c3bdca56f56ee8ac63edf9da775311121ea6`
- `manuscript/review_ch01/chapter.md`：`a1e669471959aa04c677b458d42e87f077f80ab392da896ad408ae6db2c59a63`
- `manuscript/review_ch01/appendices.md`：`68fd1f27e531edcb078b0ec79192ba56eaa6bf17a97660325f8b9bbb39066783`

实际 TEX SHA-256：`a072130ccd13cf563c0f99478fa98cf6169387726e1ff5492263edd134b6930f`。报告签署绑定与请求证据详见 `/workspace/IntegratedMath-book/research/production/part1_math_philosophy_followup.json`。
