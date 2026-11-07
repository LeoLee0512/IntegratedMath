# 第一部分真实讲座摘要、活动与书评：有界后续核读

实际阅读者：`/root/part1_sources`。记录时间：2026-11-05T17:35:20.037040+00:00。

本轮取得 JuliaCon 2025 官方活动日期和多场主旨报告的摘要正文。其中 John Urschel 的高斯消去算法讲座可成为00B05的真实专题入口；尚未取得对应全文，不认证摘要中的数学断言。未取得把此前 LieGroups.jl 特定论文与该次活动明确相连的报告条目，亦未取得合格数学书评正文。正式7G verified、11G pending、15T/S独立审读账及正文均未改。

## 原目标及判断边界

本轮重新读取现有scope与第2章第24节，scope SHA256 `ad5113c1d34c24e17a637f2bc312f7ee96df86be9e09e68f30cfcdf4bf12d6a9`。00B05-1原文为“辨认讲座摘要的信息边界，由报告人和题名寻找全文而不宣称已读证明”，requirement为`00B05-topic-source`。不新增“必须找到了全文”这一隐藏条件，也不把“已给出检索线索”冒写为“已经取得全文”。本轮只提议原目标下的真实实例与操作导读，待下一版正式修订、独立复核与全部绑定重建后，才可决定该项状态。

| 原目标中的动作 | 实际证据与覆盖判断 |
| --- | --- |
| 辨认讲座摘要及其信息边界 | 已完整读官方2025/keynotes.md各摘要。John Urschel条目为报告人、题名、主题概述；不是逐步证明，也未给对应全文DOI/完整作者名单。能够直接支撑这一动作。 |
| 由报告人和题名寻找全文 | 同条目给姓名、题名及报告人机构主页入口，可据这两个检索键提出可复查的查找步骤。没有取得对应全文；机构主页不在本会话允许域名内，本轮未请求。可教“怎样继续找、怎样记录未找到”，不能说检索已成功，也不能把下面另一篇LieGroups文章接上。 |
| 不宣称已读证明 | 本轮确实只读了摘要。记录为“已读报告摘要，全文及证明尚未核”。摘要关于消去法、稳定性与进展的表述仅作为该报告内容，不升级为本书已证明的定理、最新开放状态或综述共识。 |

**建议结论：** 该页面足以提供00B05所缺的真实摘要专题入口；配合下列原创导读，可以覆盖G层级已声明的阅读和检索动作。完整论文取得不是这个目标的必要条件。但本轮未把正式source requirement改为verified；若主代理要求真实全文对应链作为额外实践，该部分只能保持未核，不能无证填补。

## 来源身份、固定版本与实际阅读

原生仓库[JuliaCon/www.juliacon.org](https://github.com/JuliaCon/www.juliacon.org)根目录确认年份目录及文件位置。README全文说明本仓库为juliacon.org网站源文件、franklin分支生成并部署至GitHub Pages；这是活动组织方自己的原生发布源，不是被拒绝网站的第三方镜像。固定版本`85ad651a4f9e3480f5d0753fd201f9019b14870e`。

- [README.md](https://github.com/JuliaCon/www.juliacon.org/blob/85ad651a4f9e3480f5d0753fd201f9019b14870e/README.md)：实际全文阅读，身份与部署说明在1–7行；未执行安装或预览命令。
- [2025/index.md](https://github.com/JuliaCon/www.juliacon.org/blob/85ad651a4f9e3480f5d0753fd201f9019b14870e/2025/index.md)：实际读1–155行。第8行活动日期2025-07-22—26；第67行把22—25日的报告/工作坊与26日hackathon分开。第50行列Urschel题名，第57行指向keynotes。后部混有2024营销文字，未据此归定2025单场信息。
- [2025/keynotes.md](https://github.com/JuliaCon/www.juliacon.org/blob/85ad651a4f9e3480f5d0753fd201f9019b14870e/2025/keynotes.md)：75行全文实际读。第65行给John Urschel及MIT主页入口，第67行为 *80 Years of Computing with the Elimination Algorithm*，第69行为真实摘要。它概述线性方程组、消去法数值稳定性、历史与进展、Julia的作用。这里有多场报告的摘要，不是仅有题名的日程。
- [2025/schedule.md](https://github.com/JuliaCon/www.juliacon.org/blob/85ad651a4f9e3480f5d0753fd201f9019b14870e/2025/schedule.md)：全文实际读，只有Pretalx日程链接，没有本地单场摘要。Pretalx不在当前允许域名内，**未请求**；不能记成实际HTTP403。
- [2025/minisymposia.md](https://github.com/JuliaCon/www.juliacon.org/blob/85ad651a4f9e3480f5d0753fd201f9019b14870e/2025/minisymposia.md)：87行全文实际读。是主题征稿/介绍，不是LieGroups特定报告的接受记录。未用主题相近替代对应链。
- [imprint.md](https://github.com/JuliaCon/www.juliacon.org/blob/85ad651a4f9e3480f5d0753fd201f9019b14870e/imprint.md)：37行全文实际读，说明组织方及标识/商标保留权利；没有给予摘要正文的通用开放再分发许可。

**许可边界：** 已见根目录未列独立LICENSE；已读README和imprint未给摘要正文的明确开放许可。因此不能把“GitHub公开可读”等同“公共领域/CC开放许可”。本书拟使用固定链接、必要报告人/题名信息和原创阅读概述，不收入原文摘要或网站图片，不转载连续外部正文。原文件仅保存在Git忽略的本地核验缓存。

## 可供下一版选择的原创导读段（尚未写入正文）

> 一个真实例子是JuliaCon 2025官方主旨报告页中的John Urschel报告《80 Years of Computing with the Elimination Algorithm》（题名意为“用消去算法计算的八十年”）。已读的摘要介绍了报告将讨论的线性方程组计算、稳定性问题和历史进展，没有给出这些内容的完整证明。先在核验卡写下报告人、原题名、活动及摘要位置；再用“John Urschel”和这个原题名作为查找全文的线索，优先核对报告页、作者作品目录及候选论文的作者、内容和版本。网页给出的报告人主页只是进一步查找的入口，不等于论文全文。若尚未找到对应全文，就写“已读讲座摘要；对应全文、完整作者名单与证明未核”，不能把报告人直接写成某篇论文的唯一作者。我们本次正处在这个阶段；也不能用另一篇题目不同的会议文章填补这张卡。

提议来源条目编号可用`C2-S3`，记录上述固定版本keynotes.md第65–69行，附读取日期及许可边界。是否采用编号由主代理统一；本轮未注册新source id或改变现有引用。

## LieGroups.jl链：新核到什么，仍缺什么

此前实际取得的出版论文 *Groups and smooth geometry using LieGroups.jl*，DOI `10.21105/jcon.00195`，出版deposit XML日期2026-01-13；这些旧核验详见`part1_remaining_sources_followup_2026-11-05`，本轮没有重新下载publisher PDF/XML，也没有声称重读全部证明。

从该篇已读review issue195所列作者仓库及分支进入真实目录，固定作者源稿版本`414d7b61c4446dfefab894951109a2e79d83ff6f`：

- `paper/paper.yml`全文实际读：题名和两作者对应；第22行date字段是2025-11-15。这个源稿日期不等于会议日期，也不覆盖publisher的2026-01-13出版日。
- `paper/paper.tex`实际读第1–100行及全文关键词定位：第43–50行是**文章摘要**，不是官方活动报告条目。稿件说明LieGroups.jl0.1.9及文章结构。未从所读位置找到对应讲座日期/编号；关键词定位不能当作全篇数学审读。
- `Readme.md`全文实际读，只见包介绍等信息，没有把该篇与具体场次相连。
- `LICENSE`全文实际读：LieGroups.jl package采用MIT Expat，包含署名许可保留条件。此许可不能自动套给JuliaCon网站摘要、publisher PDF或外部材料。源稿仅供本地阅读定位；本轮不转载。

因此00B20仍为partial支持、正式pending。JuliaCon2025官方总体日期虽已核，但仍缺**这篇论文与该次活动的明确关系**。不能从“JuliaCon2025Procedings”分支名、源稿日期、期刊出版年或主题相似性补造报告身份；也不能把Urschel报告与Bergmann/Baran论文拼接。00B05的真实摘要是独立候选，不解决00B20的这项缺口。

## 00A17有界检索：仍未取得书评正文

本轮4个公开GitHub仓库搜索响应均200，实际检查首屏结果；搜索不是全文证明。窄查询返回汇编语言书评仓库，与所需数学书评不符；宽查询含资料列表、机器学习书代码和汇编档案，没有仅凭名称采纳这些作品。

唯一继续检查的候选为`planetmath/00_General`，实际根目录固定commit`f6b6fd1a507bf68001255dd23e173d82e41fb9ff`。完整读取README：第15行确有00A17“External book reviews”，但这是分类列表，不是书评正文；所见133项根目录没有00A17书评条目。不能因此认证整个PlanetMath从无书评，本轮只是没有取得可用原作。已取得LICENSE，实际只读前35行辨明为CC BY-SA 3.0 Unported，不宣称阅读全文或审核全部条款。未复制分类表为专题证据，未使用搜索结果中的第三方收集/转载库作为被拒绝AMS/MAA内容的替代。

00A17-topic-source仍pending。此前JOSE整书预审未继续的结果仍成立，不把它改写成完成了书评。00B15/25/30/50/55/60/99等其他未满足需求没有新增充足证据，原缺口不变。

## 访问与冻结边界

本轮累计22次公开GitHub/raw只读请求，均HTTP200；逐条URL、UTC取得时间、响应SHA256和字节数在同名JSON。当前网络政策restricted/enforced；依cloud runtime networking要求读取策略并确认允许域名。不重试AMS/MAA/Stanford/Clay/Charleston/api.github.com，不访问Pretalx或MIT主页，不登录、不读取凭据、不改网络策略、不取第三方镜像、不大克隆。没有执行源文件内的安装或外部通信步骤。

固定源码和净化的目录/搜索结果保存在`local-inputs/part1-jcon-event-followup-cache/`（已用git check-ignore确认忽略）；报告不分发这些外部正文。正式scope/source账哈希仍按本报告JSON绑定，7/11状态原样。其他代理并行产生的工作区变更不属于本次调查。
