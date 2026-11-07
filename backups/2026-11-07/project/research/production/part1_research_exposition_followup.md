# 00-02：Stacks原生研究阐述来源核读与映射建议

日期：2026-11-05（UTC）。核读者：`/root/part1_sources`。**取得并实读了新的专题正文证据；可以提出00-02限定目标的来源映射修订，尚未改正文、scope或验收账。** 主代理解除冻结后，本报告及JSON保存至研究记录；既有ZIP与第一部分验收账未改。原始文献缓存另保存在已确认Git忽略的`local-inputs/part1-research-exposition-source-cache/`，不纳入源码分发。

## 先核现有缺口

已读当前`part1_scope_plan.json`与`part1_topic_sources.json`。scope哈希`9d542b4dba6cdbefed6a8529a2f3d4b3562dff9d62f3800d692e64435ade21de`；00-02仅有目标`00-02-1`“研究材料的核验边界”，对应`00-02-topic-source`、`topic_specific`。既有pending理由是只曾实读Stacks README，没有具体研究阐述的条件、结论及证明位置。本次针对这个缺口，不把目标扩大为本书证明代数几何。

正文现要求读者分开记录“对象、假设、结论、证明位置”，明确集合、抽象代数与几何背景未在第一章建立。这与以下真实材料的有限阅读任务匹配；Stacks是专门领域的研究性教材/综合阐述示例，不据此改其数学内容的MSC归属，也不声称它是原始研究论文或所有数学的综述。

## 合法取得路径与固定身份

网络前读cloud runtime技能及networking参考，检查`/etc/codex/network-policy.json`和当前environment status：restricted、enforced、observations_current=true；GitHub与raw原生域允许。未读凭据、未改代理或TLS、未请求既有403域、未用镜像、未clone。

先取官方仓库根目录与已知README，均HTTP200；根目录实际列出本轮使用文件，并给出`currentOid=a04446e57ec1fbc252a871afcec7752fb2807b14`。随后全部专题、许可和约定文件使用该固定提交的原生raw URL，未猜测文件名。共9次公开请求，均200；逐请求UTC、URL、字节数和SHA见JSON及伴随JSON的`requests`（保留临时取得路径，并补记持久本地缓存路径）。没有向README中的邮箱发送消息。

固定入口：

- [Schemes专题原文503—590行](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/schemes.tex#L503-L590)
- [标准开集引理陈述与证明519—564行](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/schemes.tex#L519-L564)
- [全局数学约定](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/conventions.tex)
- [项目Introduction及许可声明](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/introduction.tex)
- [COPYING许可全文](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/COPYING)

`schemes.tex`实际取回时间2026-11-05T16:17:32.758117+00:00，174402字节，SHA-256 `08475a01cf0ddf69734fd7ebc0d14d3831148c25a2ef82aaafdb65666f8fce47`。这里以提交和响应哈希固定版本，不假造出版年份或把活动项目当成静态版次。

## 实际阅读与可以核对的事实

实读`introduction.tex`全文：项目目标是从交换代数经概形、代数空间建立代数叠的基础，强调跨章引用；另有贡献归属说明。实读`conventions.tex`全文：ring约定是含单位元的交换环，允许零环；模为幺模；集合论采用ZF加选择公理；自然数从1开始。不能把书中本地自然数记号或未声明的非交换环默认带进这一材料。

实读`schemes.tex`1—235行：局部环空间、态射及茎上的局部环同态条件；环层空间同构的引理有单独陈述和证明。进一步完整实读503—590行，重点为`lemma-standard-open`（标签必须连同Schemes章节使用，不与Algebra同名标签混同）。

可制作一个**原创的阅读记录表**，无需复制源书正文：

| 阅读字段 | 实际可核定位与内容 |
| --- | --- |
| 研究对象 | Schemes503—517：交换环的谱、标准开集D(f)、局部化，服务于仿射概形结构层的构造。 |
| 全局假设 | Conventions51—54补足ring与module的约定；Schemes521以下再列R、f及各分支需要的g、M等输入。 |
| 局部假设 | 引理第一部分另需`D(g)⊆D(f)`，不能删去；第三部分讨论有限给定的gᵢ。 |
| 结论 | 519—536：包含关系导出局部化中的可逆性及规范映射；任意标准开集的开覆盖有有限标准开细化；标准开覆盖与局部化后的单位理想条件对应。 |
| 证明位置 | 538—564完整proof环境：先用局部化谱/素理想判定可逆性，再用局部化泛性质取得映射；有限细化引用拟紧性和标准开基；第三结论引用另一代数引理。 |
| 未核边界 | 被引Algebra、Sheaves引理及EGA正文未取回逐读，因而这次没有从基础重证每个被引结论；只确认真实陈述、证明文本和依赖位置存在且相匹配。 |

这份材料提供了README所没有的真实对象、条件、结论、证明和依赖链。它还适合说明：看到proof环境不等于读者已掌握所有证明先修；必须沿章节限定的引用继续核查。第一章读者在此可以学习登记这些字段，不被要求立即理解局部化、层或概形的全部技术。

## 原创概述可写到什么程度

建议新增的最小入口说明可表达为：

> Stacks的Schemes章“Affine schemes”标准开集引理是一个具体研究阐述样本。可分别定位其交换环/模约定、标准开集条件、局部化及覆盖结论，以及证明所引的代数和层论条目。本节只示范如何记录这些字段与未核先修，不把其中结论记为本书已证。

上段是本次原创建议，不是来源译文。不要把“本次阅读核对”写成“已审定Stacks全部数学”“初学者已经读懂”“证明无任何外引”或“最新研究状态已核”。也不能顺带替00A17/27/30/64或00B各文献类型补通过。

## 许可的实际证据及边界

实读COPYING全部397行，文本为GNU Free Documentation License 1.2；`introduction.tex`16—23行的项目文档许可通知写明1.2或后续版本、无Invariant Sections及封面/封底固定文本。COPYING哈希`4b2c8fc390f802cd92f0622dc00a708a588bec54d0145d2ee135d6d7672bfe85`；Introduction哈希`43abd6493bf48325878d6573966e97025770d4b4e12db1dda31da7fd181d4acf`。

Schemes文件开头没有重复上述许可通知。本次据项目COPYING与Introduction记录项目文档许可，不把任意代码类文件的许可自动移到教材；也不由此宣布章节可无条件转载。为查清组织结构另取得preamble和类文件，只读了preamble开头、类文件关键词结果，没有以这两份文件作为数学或完整许可审读证据。

本次用途严格为链接、短书目信息及原创事实概述，原始TeX缓存不加入书稿ZIP；未复制题解、图或长段正文。若以后要分发章节、长篇翻译或改编，需按其具体授权另行处理GFDL要求；此次不实施该行为。

## 映射建议与保持未改的状态

伴随JSON提出新来源ID `SRC-S4-STACKS-SCHEMES`，仅覆盖`00-02-topic-source`和`00-02-1`。从内容证据看，原“只有README”的实质缺口已具备补齐材料；建议主代理采用上述固定入口和限定边界，再更新正式来源映射、重新绑定正文/scope哈希并独立复核后，将该需求改为verified。

**当前正式ledger仍为pending，本报告没有自动改状态。** 其他来源缺口、完整第一部分pending以及作者待审不受此建议影响。也不重写旧README核验日期：这是2026-11-05T16:17之后新取得并实际阅读的证据，旧记录保持其当时边界。

机器记录：`research/production/part1_research_exposition_followup.json`；原始文献缓存：`local-inputs/part1-research-exposition-source-cache/`。目录证据只保留实际文件路径、提交与响应哈希；未复制网页其他会话字段。临时原始取得证据仍在`/tmp/stacks-00-02-evidence/`。
