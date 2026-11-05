# 第一部分修订：专题来源缺口与真实文档实践

记录时间：2026-11-05T09:40:07.315262+00:00。工作区：`/workspace/IntegratedMath-part1-publish`；审查基线：`de08a8a92dc04feeacf088c7566e4b79b2bc32fa`。只写研究记录和实践建议，未改正文或原book工作区。

## 必须修正的验收结论

**第一部分应标为pending，不能继续宣称全33节已按G/T/S目标完成。** 00A17、00A27、00A30、00A64四节仍缺实质专题来源。此前S2逻辑例题与S3分类定位不能替代这些来源；承认讲解范围有限，也不能把缺失的已核验专题入口当作已兑现。

编辑政策G最低要求为：“交代研究对象、典型问题、先修入口、与邻近主题的区别和已核验参考入口；明确本节不提供哪些证明”。这是内容完成条件。程序通过和反例推理正确不自动满足它。旧accepted可留作历史审计对象，但当前完成声明、范围状态及总验收必须更正；本报告不覆盖数学/教学审读者重新签署的职责。

## 本次网络实测

已读Cloud Environment网络规则并检查`/etc/codex/network-policy.json`；runtime此次观测current、策略restricted/enforced、未配置VPN。AMS、MAA、Clay、Stanford、Charleston原候选URL各试一次，全部在代理CONNECT阶段403，未取得源站正文。保持原代理和TLS，不登录、不读凭据、不找镜像绕过。403不能解释成网站不存在，也不能写作阅读成功。

| 原入口 | 状态 | 本次可作出的结论 |
|---|---|---|
| <https://www.ams.org/msc/msc2020.html> | CONNECT 403 | 未取得正文；状态与许可未核 |
| <https://maa.org/press/maa-reviews> | CONNECT 403 | 未取得正文；状态与许可未核 |
| <https://www.claymath.org/millennium-problems/> | CONNECT 403 | 未取得正文；状态与许可未核 |
| <https://plato.stanford.edu/entries/philosophy-mathematics/> | CONNECT 403 | 未取得正文；状态与许可未核 |
| <https://math.cofc.edu/faculty/kasman/MATHFICT/> | CONNECT 403 | 未取得正文；状态与许可未核 |

准确时间、错误文本和无正文哈希null见JSON。没有确认任何开放问题的最新状态。

## 哪些G仍缺实质来源

| 代码 | 已有证据能支持什么 | 尚缺什么 | 适当状态 |
|---|---|---|---|
| 00A17 外部书评 | S2支持反例逻辑，正文平方为一例为原创假设性评论。 | 未取得一篇真实外部书评，缺所评书的可核对版次、评论者、评论内容定位。 | 待专题来源补核，未按声明深度完成 |
| 00A27 未解问题清单 | S2支持反例/全称逻辑，S3证明存在此分类。 | 未取得真实问题清单/状态记录内容，不能核验具体问题的表述、记录时间和状态。 | 待专题来源补核，未按声明深度完成 |
| 00A30 数学哲学 | S2支持量词次序示例，S3支持分类定位。 | 未取得数学哲学专题来源；逻辑反例不是关于数学对象、真理、公理地位之争的文献入口。 | 待专题来源补核，未按声明深度完成 |
| 00A64 数学与文学 | S2支持量词辨析，S3支持分类定位；天平比喻为原创说明。 | 未取得数学与文学专题目录、作品或学术讨论；一般语言歧义不能独自兑现数学与文学导读的参考入口。 | 待专题来源补核，未按声明深度完成 |

修复不能把“需真实参考入口”改为“会写一种示范就算完成”：00A17应实读真实书评；00A27应实读真实问题/状态记录并注明时间边界；00A30应有数学哲学议题的真实文献；00A64应有数学与文学交叉的真实材料。当前无法取得时保持待补，不编造权威结论。

00-01与00A15已有S1真实教材/书目入口，使用时保留旧核验日期。00-02的Stacks README是研究项目入口层面的实读，不能冒充具体专著章节已经读过。00A99可用本地MSC分类记录说明余类定位，不能宣称本轮已重读AMS。它们不消除上述四节缺口。

第2章十个G节已有真实Crossref文档，可支持书目字段阅读方法；这份文档不是会议集、纪念文集、译文集或重印集的实际样本。下述实践可以补“实际查一份资料”的训练，但不能据此把尚未进行的真实文献类型案例阅读标为完成。第2章修订目标与实际内容仍需独立教学审读，不由本报告批量授予accepted。

## Crossref本次确实读到的内容

本次再次取得以下两份官方仓库文件，均HTTP 200，字节数和SHA256与此前`part1_ch02_draft_scope.md`记录一致：

- <https://raw.githubusercontent.com/CrossRef/rest-api-doc/master/api_format.md>；10677字节；SHA256 `70aa9d3fc20bbf8d2f4d35e756f40e65e8e1ebaaecec2eaf1e6e1098996ed5c1`。
- <https://raw.githubusercontent.com/CrossRef/rest-api-doc/master/README.md>；45347字节；SHA256 `7c1d9010cacd833645f7019ea6a8825b70fb3f33b5db98907c5d0637eec4663a`。

实际阅读api_format.md的Versioning、Work、Contributor、Update、License等段落；版本表末行v3，日期2018-05-15。README明确deprecated，因此这是一份真实的历史字段文档，不是现行API的完备规范。本次没有调用Crossref现行服务、取得具体论文记录或阅读该论文证明。

| 定位 | 核验到的字段意义（原创概述） | 不能推出的结论 |
|---|---|---|
| Versioning：`v3` | 所读文件版本表最后一行列v3，日期2018-05-15。 | 文件版本不是论文出版年，也不是2026年API现状确认。 |
| Work：`title`, `container-title` | title为作品题名数组；container-title为容纳作品的题名数组，在该表中为可选。 | 字段结构没有提供任何具体文章的题名值。 |
| Work：`created`, `deposited`, `indexed`, `issued` | created指DOI首次注册；deposited指元数据最近更新；indexed指最近索引，重新索引不保证元数据变化；issued取纸本与网络出版日期中较早者。 | 注册、元数据更新、索引和出版是不同事件；不把访问日或v3日期填为论文出版日。 |
| Work / Contributor：`author`, `editor`, `translator`, `family`, `given` | author/editor/translator在Work中分列，均为Contributor数组且在该表中可选；Contributor给出姓与名等字段。 | 角色不互相替代；空缺不是身份证据，姓名字段存在不证明已经读过本人作品。 |
| Work / Update：`update-to`, `DOI`, `updated`, `type` | Work的update-to指向Update数组；Update中DOI指被更新作品，updated给更新出版日期，type描述更新种类，如更正或撤稿。 | 文档中列举类型不是某真实论文已撤稿的证据。 |
| Work / License：`license`, `content-version`, `start`, `URL`, `delay-in-days` | Work的license为可选数组；License记录适用内容版本、开始日期、许可页面URL和生效延迟。 | 缺license不表示无版权；元数据、文档、文章全文各有权利边界。版本或生效时点不匹配时不能移用许可。 |

README的Documentation License段给出CC BY 4.0；这仅是所读文档声明，不能移用于所索引论文。练习只引用字段名、网址与必要的版本信息，说明和题答原创，不收入连续版权正文。

## 可加入第二章的原创实践建议（尚未改正文）

### 练习：核对一份真实文档，不补造论文

材料就是上面两份实际取得的Crossref文件；练习不另设虚构论文，不填假DOI。读者记录时须保留其版本和deprecated状态。

1. 打开CROSSREF-FORMAT，定位Versioning，记录最后一行版本和日期；再打开README，判断是否能把这份文档称为现行API指南。
2. 在Work及对应嵌套类型中，找到作品题名、载体题名、作者、编者、译者的字段名；说明哪些只能从具体记录取得值。
3. 比较created、deposited、indexed、issued，回答检索索引的日期能否替代论文出版日期。
4. 追到Update和License，分别记录更正关系的指向对象、许可适用版本和开始日期的字段；不填写不存在的具体论文信息。
5. 最后写出本次确实读过什么、尚未读过什么；回答有DOI、被索引或元数据格式合法能否证明论文结论正确。

### 独立答案建议

1. 版本表v3日期2018-05-15；README明示deprecated，因此只作历史元数据结构练习。访问日2026-11-05仅是本次获取日。
2. title/container-title分别标识作品与载体题名字段；author/editor/translator分列角色。本文档是字段说明，没有一篇由本次核实的文章题名、作者、页码或DOI值，不能补造。
3. created=首次DOI注册、deposited=元数据最近更新、indexed=最近索引、issued=最早纸本/网络出版日期；各事件不同，不能互相替换。
4. Update.DOI是被更新作品，updated为更新出版日期；License.content-version和start限制适用版本和开始时间，URL指向许可说明。列出correction/retraction两个类型不等于证明任何文章实际发生这些事件。
5. 已读两个真实文档中指定段落；未读任何由此检索到的数学文章或其证明，未调用现行API、未核对具体出版记录。DOI、索引与格式只能帮助定位，证明正确性须另读命题条件及推理。

可以附一张本次阅读核验卡：

| 核验项 | 本次应填内容 |
|---|---|
| 实际阅读对象 | Crossref Metadata API JSON Format及同仓库README |
| 版本/获取 | 文件版本v3（2018-05-15）；本次2026-11-05获取，二者不同 |
| 状态 | 已废弃的真实历史文档，选定字段已读 |
| 真实论文题名、作者、DOI | 本次没有取得具体记录，不填 |
| 数学证明核验 | 未进行 |
| 下一步 | 取得实际出版记录并核对原文；在此之前不声明已读研究内容 |

这是一项可由读者打开实际文件逐项复核的实践。它检验文献读取、身份与版本分辨，而不把出版元数据当成数学证明，也不冒充已完成真实会议/文学/哲学专题阅读。

## 修订后的状态建议

- 保留当前数学例题、代码和结构检查的真实结果；不要把来源缺口误写成发现所有数学推导错误。
- 至少将00A17、00A27、00A30、00A64保持待补；当前00-XX总状态降为pending，`full_scope_accepted=false`。
- 第2章实践由正文负责人采纳并将答案与题目分开；修改后重新绑定源稿哈希并做受影响独立审读。
- 在真实专题来源和其独立审读补齐前，不恢复第一部分全范围完成或用历史accepted继续宣传完成。
