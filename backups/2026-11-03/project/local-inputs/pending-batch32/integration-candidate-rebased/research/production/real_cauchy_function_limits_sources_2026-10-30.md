# 柯西判据与实函数点极限来源审计 {#real-cauchy-function-limits-sources}

整合者 `/root/prepare22_build` 已实际全文读第32批计划、原来源JSON全部字段、作者来源报告和独立概念报告，并实际重读以下公开缓存范围。四稿1128行及16全解、三份最终数学／教学报告现已实际全文读完并绑定；没有正式安装或整批通过声明。

## 来源、许可与真实历史

四项来源均为 Jiří Lebl 的 *Basic Analysis I*，version6.3，固定提交 `e21ec524ca7d54f800c693b948020c188d21d01f`。front matter实际280—295及378—458行核作者、版本及版权，LICENSE全部15行明确双许可CC-BY-SA4.0或CC-BY-NC-SA4.0，不能称为公有领域。

| 真实来源 | 原HTTP200取回时间 | 缓存SHA-256 |
|---|---|---|
| [Sequences and Series](https://github.com/jirilebl/ra/blob/e21ec524ca7d54f800c693b948020c188d21d01f/ch-seq-ser.tex)，165039字节 | 2026-10-30T03:58:03.768311+00:00 | `18657062b4a851fc7cd1ced849e7791e893e2e9968288850ac3c0a8a5c5bd1ce` |
| [Continuous Functions / Limits of functions](https://github.com/jirilebl/ra/blob/e21ec524ca7d54f800c693b948020c188d21d01f/ch-contfunc.tex)，119775字节 | 2026-10-30T04:28:49.987178+00:00 | `3fe56fe7261f3db0dfb0dbabe8e807b0781c41255c2b9cb463f4868fbb13c14d` |
| front matter，18862字节 | 2026-10-29T19:51:54.424412+00:00 | `a355edf1ff287d98d13bfc50fa9cfcd541b42b8210f0172dfb5dadafb58a47ee` |
| LICENSE，467字节 | 2026-10-29T19:51:08.949458+00:00 | `682fedaab34d7d47962da7276284e608f43881c07c3c887cb66368688748c13d` |

四缓存已实际重核字节数与散列，原HTTP对象与响应信息保留于JSON。作者来源核查真实新增一次函数章HTTP请求；本整合者零新请求，未把重读算作抓取。计划末尾“函数来源尚未取回”保留为早先历史，后来的来源报告与原HTTP记录说明实际取回时点。

仅核标准数学事实、假设及证明路线差异；正文、题解独立编写，不复制来源表达、题目、图或代码。原书作者／许可仍明确署名；若日后改编其表达须按选定适用许可处理，缓存不自动随教材分发。来源直接使用已给定实数，不构成本书分割实数构造的外部证明。

## 实际读段与本书应兑现的义务

| 主题 | 实际核读与路线区别 |
|---|---|
| CA1双指标定义 | 序列章2681—2908：先误差、再共同阈值、最后任意两个尾指标；源书从1起，本书从0起。完整否定固定一个正误差，不能以对角或相邻差替代双指标条件 |
| CA2必要性与有界 | 同段：收敛用同一半误差控制两项；源书有限前缀直接取最大值，本书须调用SA1适用于任意全列的固定状态前缀界，并处理N=0，不能循环先用收敛 |
| CA3一个子列控制全列 | 本书独立估计固定一次j=max(N,J)，已证SS1给k_j≥j，再比较所有尾项；不逐项重新选择实输入 |
| CA4柯西判据 | 源书充分性使用liminf/limsup；本书以CA2有界、已有SS3实数数列BW、CA3组成非循环证明。源书调和级数相邻差警示只核边界，不移入尚未证明的级数例 |
| FL1聚点与穿孔极限 | 函数章1—252，尤其24—35及80—115：中心不必属于域，域非空不替代聚点，固定候选L的否定不等于无任何极限；孤立点说明裸条件真空，不能伪称真正极限唯一 |
| FL2唯一性与基本例 | 118—143聚点给实际共同半径内见证；本书直接常数、恒等、仿射估计且分零系数，不引用连续性 |
| FL3局部条件 | 440—501直接限制域与局部性；本书局部相等双向、穿孔近域界与非零下界，不扩大为全域或中心值条件 |
| FL4运算与实际商域 | 320—438来源以序列刻画得运算并留证明练习，395—426还要求整个原穿孔域分母非零。本书直接epsilon–delta、有限个正半径合并，定义实际D_g并先证其聚点，限制分子后才用乘积。零分子误差e=0时e/Q≤e/d不能写严格 |

函数章51—76和203—252从每个缩小半径任选一个实点。当前书内不使用该逆序列刻画，也不把自然最小元或有理稠密性当作任意实域无限选点的依据。比较、夹逼、左右极限、函数复合、连续性、微积分及级数不在本单元范围；商分母极限非零是定理适用条件，不是零极限时必发散的判据。

## 角色与整合边界

计划与作者来源报告由 `/root/review22` 写，该代理也是CA作者；来源核查不能冒称独立审查其自著CA正文。真正独立概念报告为 `/root/plan_multiplication`，实际SHA `604eaabbfafcee2f9abcfd05770c27c04aad173ac7cfb19c323bb8cd9cea0459`；作者来源报告另名 `real_cauchy_function_limits_source_review.md`，SHA `75d73821da501975736097c1de6879a7b470ff3f9ca87d94527f6bb18cacceb9`。已按恢复后的实际原字节核验，两个角色文件没有混用。

B4.5仍属第28部分40-XX／第242章40Axx／主40A05，交叉26A03、97I30；B4.6转入实际第18部分26-XX／第146章26Axx／主26A03，交叉97I20。按先修路线出现第18部分不更改MSC编号或目录顺序。FL不依赖CA作为定理前提。实际隔离合成、Pandoc原审计及分类台账核验为65单元534题答、21图28附录、8草稿章32草稿叶0整章完成；不是正式PDF通过。本批没有新图、数值代码或编号附录；B3形式基础与single-analysis整模块仍未完成。基线只绑定第31批冻结候选，尚不假称正式第31批安装已核。


## 最终文本与报告绑定

实际核验 2026-10-30T04:57:15.659754+00:00。两份数学审均由非作者plan_multiplication完成，教学审由visual21_front完成。未修改三报告中的初查缺锚历史；当前真实首标题另核。

| 文件 | SHA-256 |
|---|---|
| `/tmp/real_sequences_cauchy.md` | `03dcdda8e456244ae0ddce055f3cf57cdab9b843c5bf4f7fb3ed12a1c62d5b93` |
| `/tmp/real_sequences_cauchy_answers.md` | `346a6225efd2652d09c38f47f577a823155668b2f48dc2b8e277461bf776565c` |
| `/tmp/real_function_limits.md` | `3b71dc172ab18a73bedd72e7cc9036ae7d053699ade02db83e77f2f531993ce8` |
| `/tmp/real_function_limits_answers.md` | `532ed11bd537ed577bf73ba713ff38cdfbdf18f9dd946449c3c8d4ffc942d37a` |
| `/tmp/real_sequences_cauchy_math_review.md` | `eb4cfbae7fa43a013c23721ba6cb13531d818800961c47c407e6ba6f0a56a7f1` |
| `/tmp/real_function_limits_math_review.md` | `d924a09b851ffe540ee950677c1e90fc54d784e8160de437187a2753a7b04af9` |
| `/tmp/real_cauchy_function_limits_pedagogy_review.md` | `1cbaf1421839e0e55ef1b70c3b52fe77f1d1aa5f1cccd83cae09ff40638a34fc` |
| `/tmp/real_cauchy_function_limits_plan.md` | `6a56e655f0c3d9859c644226eec232ff91e08fba33463413e1d9902464053e53` |
| `/tmp/real_cauchy_function_limits_concept_review.md` | `604eaabbfafcee2f9abcfd05770c27c04aad173ac7cfb19c323bb8cd9cea0459` |
| `/tmp/real_cauchy_function_limits_source_review.md` | `75d73821da501975736097c1de6879a7b470ff3f9ca87d94527f6bb18cacceb9` |

CA与FL精确先修分别31/18项；FL不引用数列稿或CA，按学习次序相邻不产生逻辑依赖。已按真实分类目录核26-XX／26Axx／26A03及40-XX／40Axx／40A05。第31批四工具及两metadata冻结候选字节已核，包含主编30排版与范围守卫修复、31新来源段主动拆段；未假称正式31安装。本批同样拆分新引用的版本、固定提交和链接说明，并将章引言写成中文误差—半径，三章部分范围守卫保持完整；本批绘图模块原字节不变。正式安装、构建与PDF视觉验收仍待主编执行，来源不登记下游总通过。
