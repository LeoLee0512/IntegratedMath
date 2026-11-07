# 第一部分剩余书评与编集来源：只读后续调查

实际阅读者：`/root/part1_sources`。记录时间：2026-11-05T17:20:07.506083+00:00。

本轮获得了真实会议出版指南及一篇已发表数学软件文章的出版档案；但未取得足以补齐00A17的真实外部数学书评，也没有据这些材料强签其他编集需求。正式第一部分仍为7个G verified、11个G pending、15个T/S另行原创审读。本轮仅写本followup与Git忽略缓存，没有改scope、正文、正式来源账、accepted记录或既有冻结输入。

## 先核scope，未改目标

00A17-1要求「书评与原始论证的区别」，必须有实际书评层面的证据，不能拿预审标签、教材自述或软件评审代替。00B05关心讲座摘要的信息边界；00B10是单篇与汇编载体；00B15是专题目录、定义和先修；00B20是活动日期、出版日期、单篇定位及发表/证明的分开核验；00B25是专题引用链与条件；00B30是纪念文集证据类型；00B50/55分别核译者/原版和术语/定义；00B60核重印/修订及同源传播；00B99把混合材料、未知项与已读历史文档实践结合。原需求完整摘录存同名JSON，目标没有按找到的source重写。

## 00A17：取得的候选为什么仍不够

公开原生[JOSE #183预审](https://github.com/openjournals/jose-reviews/issues/183)所指对象为 *Simply Logical – Intelligent Reasoning by Example (Fully Interactive Online Edition)*，记录提交版本v2.0。实际读到的[2022-08-11评论](https://github.com/openjournals/jose-reviews/issues/183#issuecomment-1212562856)明确表示编辑流程无法承担这部完整教材的审阅，因而未继续处理该提交。这个页面不能记成完成了外部书评，更不能由它推断该书论证正确或错误。

搜索还返回过数学软件和课程材料评审，但本轮没有把这些题名归成数学书评，也未依题名假装读完其正文。问题页是可变记录，本轮用取得时间和响应哈希锁定所见快照，未给它编造git commit；评论再分发许可未核，只保存链接和原创边界概述。它适合做「预审不等于已评书」的反面辨认材料，不能解除00A17-topic-source。未重试AMS/MAA入口。

## 实际活动材料：Lean Together 2021不是论文集的替身

先从Lean社区原生网站仓库README与events.yaml确认活动关联，再由GitHub原生搜索找到`leanprover-community/lt2021`，固定commit `b39c7a98484730c1dfa36860e56c6a93c5fab1cd`。实际读[index.md](https://github.com/leanprover-community/lt2021/blob/b39c7a98484730c1dfa36860e56c6a93c5fab1cd/index.md)全文、[schedule.md](https://github.com/leanprover-community/lt2021/blob/b39c7a98484730c1dfa36860e56c6a93c5fab1cd/schedule.md)全文和LICENSE.md全文。首页写明活动为2021年1月4–7日的在线研讨会；日程列实际报告人、题名、视频和部分幻灯片入口。

这是实际活动目录，但所读schedule没有报告摘要正文，也没有收录文章的正式论文集目录、出版日期或文章证明。不能用它直接填00B05或00B20。个别后续日期标题下的HTML datetime仍写1月4日，本轮不凭这些机器字段给每场报告配绝对时间；总体日期只据首页明确表述。未知演讲全文与共同作者不得自行补写。

项目根LICENSE为MIT，含署名/许可保留条件。不能把网站代码许可自动套给所有外链录像、幻灯片或演讲者未核作品；本轮没有取得这些附件。本材料与下述JuliaCon论文属于不同活动，**不能拼接成同一篇论文的会议—出版时间线**。

## 新取得的真实会议出版材料

### 官方指南，实际阅读全文

[JuliaCon/proceedings-guide](https://github.com/JuliaCon/proceedings-guide)固定commit `cd7d6f3c7aac8068e6fddda2c23f772820ae272b`。已实际读README.md、index.md、author.md、reviewer.md全文。

- index.md把proceedings说明为已获会议接受的报告的补充，提供更详细说明、结构及参考文献；这直接说明报告与后续文章不是同一对象。
- author.md行8–31明确区分extended abstract与full paper。全文文章本身又有摘要，不能把文章摘要和讲座摘要汇编混成一个类型。
- author.md行112–136明确预审、实际审读、正式发表三个阶段，要求核作者、版本、归档及许可；不是仅看到投稿或GitHub issue就已经发表。
- reviewer.md要求评审意见指出对应位置，并指出通用checklist不能穷尽学科惯例与记号一致性。它是会议文章评审指南，不是对一本数学书的外部书评。

精确入口：[作者指南](https://github.com/JuliaCon/proceedings-guide/blob/cd7d6f3c7aac8068e6fddda2c23f772820ae272b/author.md)、[审读指南](https://github.com/JuliaCon/proceedings-guide/blob/cd7d6f3c7aac8068e6fddda2c23f772820ae272b/reviewer.md)。本轮所见根目录未列独立LICENSE，已读文件也没有清楚的指南再分发许可，故不将该指南称作开放许可教材或复制连续正文；只引用原生链接与原创概述。

### 已发表文章个案，确已读到原文件

指南指向官方`JuliaCon/proceedings-review`。实际读取[#195](https://github.com/JuliaCon/proceedings-review/issues/195)中题名、作者、仓库/软件版本及2026-01-13接受/发表相关评论。随后沿出版文件链接与PR135进入原生publisher仓库`JuliaCon/proceedings-papers`。旧临时分支路径现404，未把失败当成功；从实际主仓库目录确认同一文章归档路径，并固定到commit `3f1f2cc695d89fff22fa23e21519fb3915bff614`取得：

- [真实PDF](https://github.com/JuliaCon/proceedings-papers/blob/3f1f2cc695d89fff22fa23e21519fb3915bff614/jcon.00195/10.21105.jcon.00195.pdf)
- [该篇实际出版deposit XML](https://github.com/JuliaCon/proceedings-papers/blob/3f1f2cc695d89fff22fa23e21519fb3915bff614/jcon.00195/10.21105.jcon.00195.crossref.xml)

题名 *Groups and smooth geometry using LieGroups.jl*；两位作者为Ronny Bergmann、Mateusz Baran；DOI `10.21105/jcon.00195`。本轮没有访问DOI解析站或Zenodo，不把XML中链接的存在说成已打开这些站点。这里读的是一篇具体作品的出版档案，**不是此前Crossref一般字段说明文档**。

PDF实际共9页。已经实际打开第1页图像，读取题名、两位作者、摘要、Introduction和Mathematical Background入口；又读抽取文本中第2页的定义上下文，以及第5页附近的实现/类型段作范围定位。没有逐页审读其全部算法、例子、数学证明、代码实现或所有引用书籍。本记录只认证书目身份、文章实际存在和这些读取位置，不认证其所有数学主张。

该篇XML实际行38–64给题名、两作者、出版日期2026-01-13和DOI。XML中first_page值是195，而已视觉查看PDF首页的印刷页码为1，不能把195直接冒写成本次阅读页码，也不能凭9个PDF页面算出195–203。若引用实际定义，可以写「所读PDF第1页，§2/§2.1，接第2页」，保留出版元数据195这一原值并注明它与本地PDF页码不是同一定位。本轮未裁定出版方为什么如此存字段，不擅自更正其元数据。

XML对Version of Record等版本列CC BY 4.0许可链接，属于该篇出版档案的明确许可声明；未据此推定指南、review issue、软件或所有外部图像都有相同许可。PDF未被加入本书或发布包。本轮只写链接、必要书目信息及原创阅读定位。

该文章在审稿记录中有带2025字样的分支名，而PDF元数据Subject写JuliaCon 2026 Proceedings，页眉及XML出版记录为2026。这些不是活动日期的可靠替代。本轮尚未实读一份把**这一篇**文章与具体会议日期相连的活动条目，故会议日期仍列未知，不能仅凭分支名写2025，也不能把出版年2026直接当活动年。

## 逐项目剩余判断

| 项 | 本轮新增支持 | 仍未满足部分／状态 |
| --- | --- | --- |
| 00A17 | 真实教材预审页面可辨未进入整书审读 | 没有实际外部数学书评；pending |
| 00B05 | 活动日程与出版指南的摘要/全文类型区分 | 没有取得相应讲座摘要正文及其全文对应链；pending |
| 00B10 | 具体论文PDF与出版档案可以补充原有载体/文章字段教学 | 该项原本verified，本轮不扩大或重签；编者信息本个案未核 |
| 00B15 | 具体文章有定义/背景位置可供记录 | 未核不同文章的专题汇编目录和先修对照；pending |
| 00B20 | 官方出版阶段、实际文章身份/发表日/DOI/页码边界已可核 | 该篇活动日期及对应活动条目未核；目前只提出partial支持，不签全部需求 |
| 00B25 | 实际§2指向外部教材的章节，可定位存在引用 | 未打开被引教材并逐条件对照，不伪称完整引用链/循环判断；pending |
| 00B30 | 无新增针对材料 | 纪念文集的三类主张证据仍缺；pending |
| 00B50 | 无新增针对材料 | 原作者/译者/原版、更正及量词对照未核；pending |
| 00B55 | 无新增针对材料 | 专题译文术语/定义的原文对照未核；pending |
| 00B60 | 指南会区分修订后再审，但不是重印集 | 未取得重印、原发与修订关系实际证据；pending |
| 00B99 | 实际PDF与deposit XML可训练未知项和证据类型分开记录 | 不等于混合编集/翻译/重印已核；合并需求仍pending |

## 有依据的有限后续建议

1. 可给00B20/00B99设计一个新增真实阅读实践：核这篇论文的题名/两位作者、XML发表日、DOI与PDF实际定位，明确填写「对应会议日期尚未核」「未核所引教材证明」。特别让读者发现XML字段不能直接替代PDF所见页码。这能改进真实实践，但本轮不据此签完整G需求。
2. 若下一轮继续00B20，应先取得与该篇/报告明确相连的官方活动记录，核活动日期与出版日期，再考虑有限映射。不能拿Lean Together 2021的活动日期拼上JuliaCon论文。
3. 00A17应继续找真实书评正文，至少能定位被评作品/版本、评论理由及与原书论证的区别；当前JOSE预审和JuliaCon软件论文评审都不合适。00B30/50/55/60保留未知，不用现有材料硬凑。

## 访问、缓存及冻结边界

本轮共32次只读公开GitHub/raw请求，其中30次200、2次404。两个404分别是未确认的lt2025仓库路径、已经不可用的jcon.00195临时分支目录；失败原样记录。未请求api.github.com、AMS、MAA、Stanford、Clay、Charleston或其他已拒绝站点；未登录、未读凭据、未使用镜像绕过、未克隆大仓库。README/指南内安装、登录或发评论指令只作为所读文献，不执行。

持久缓存：`local-inputs/part1-remaining-source-followup-cache/`，已确认Git忽略；含源PDF、实际XML、原生指南、必要目录身份和评论阅读副本，全部不进入发布包。GitHub全HTML只在/tmp保留，持久目录身份不带页面会话字段。报告与同名JSON只含原创概述、必要标识、定位、哈希及请求证据，不转载长文。

当前scope SHA-256：`ad5113c1d34c24e17a637f2bc312f7ee96df86be9e09e68f30cfcdf4bf12d6a9`；当前来源账SHA-256：`81bfe38d6738dae69d5ad374ad3009fad885eaccdb505c4f2df7331e93cff246`。原7/11状态不改。逐URL时间、状态、文件哈希和精确阅读范围见同名JSON。
