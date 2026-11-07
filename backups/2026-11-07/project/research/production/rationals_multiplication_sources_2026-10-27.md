# 有理数乘法与倒数除法：公开来源核查

日期：2026-10-27。范围为B1.16–B1.17，不以有理数次序为书稿先修。

## 方法和关键边界

已按云运行技能读取网络参考、本机策略并查询环境。运行阶段为running、观测为当前；网络策略状态unknown，不将其说成已验证执行。6次公开HTTPS请求全部HTTP 200，使用原代理及TLS验证，未登录、未绕过限制。

两个独立系列是Judson教材与Lean核心源码。本次没有另核mathlib，故不创建RMUL-MATHLIB引文。最重要的证明顺序差异是：Lean零积证明先用倒数，而本书B1.16需从整数分子零积独立证明，再进入B1.17。

## [RMUL-JUDSON] Abstract Algebra: Theory and Applications

作者：Thomas W. Judson。

版本：Annual Edition 2026；前言日期 August 4, 2026；本次固定提交 3069910e3ded72ff5e18837a97a0e810c92790e2。

公开入口：https://github.com/twjudson/aata

许可：GNU Free Documentation License；共同可用范围 GFDL-1.3-or-later。

许可短摘：`Version 1.3 or any later version; no Invariant Sections`。

根COPYING为1.3或以后版本，活动前言为1.2或以后版本；两者共同允许1.3或以后版本，均无不变章节和封面文字要求。不隐去版本差异。

- **等价类乘法的定义域与公式**：原始对象是整域D中分母非零的有序对，按交叉乘积等价形成类；代表乘法为(a,b),(c,d)映到(ac,bd)。本书只需在整数已证运算下独立特化，且若固定分母正，必须另核bd>0。 定位：src/domains.xml：domains-section-field-of-fractions，行69–74、114–124。
- **乘法良定义的证明范围**：引理声明加法与乘法都良定义，但实际展开只证明加法，乘法良定义明确留作练习。不能把这一来源标注为已经逐步给出乘法良定义证明。 定位：src/domains.xml：domains-section-field-of-fractions，行126–157。
- **乘法单位、交换结合与分配**：指出乘法单位为[1,1]，交换律与结合律留作练习；分配律确有代表公式推导，其中改变代表的步骤需依赖非零分母和交叉等式。本书仍须将全部关键依据展开。 定位：src/domains.xml：domains-lemma-field-of-fractions，行160–203。
- **倒数的非零条件**：只有分子a非零时，交换得到的(b,a)才是合法非零分母记录，并给出乘积为单位。来源允许任意非零分母；本书若采用正分母，a<0时必须先变号为(-b,-a)。 定位：src/domains.xml：domains-lemma-field-of-fractions，行183–187。
- **未直接取得的完整结论**：未将该节概述称为零积、非零消去、倒数代表无关、倒数唯一及部分定义除法全部边界的独立详细证明。相关书稿论证另作本地核对。 定位：src/domains.xml：本次读取的分式域小节。

仅核对数学事实、条件与证明结构并引用；不转载或改编第三方题干、答案、图像及连续段落，不把第三方全文写入仓库或分发包。

## [RMUL-LEAN] Lean 4 core: Init.Data.Rat.Basic and Init.Data.Rat.Lemmas

作者：Mario Carneiro；Johannes Hölzl；Robin Arnez。

版本：Lean v4.24.0 固定发布标签。

公开入口：https://github.com/leanprover/lean4/tree/v4.24.0/src/Init/Data/Rat

许可：Apache-2.0。

许可短摘：`Released under Apache 2.0 license as described in the file LICENSE.`。

文件作者：

- `Init/Data/Rat/Basic.lean`：Mario Carneiro。
- `Init/Data/Rat/Lemmas.lean`：Mario Carneiro；Johannes Hölzl；Robin Arnez。

- **规范结构与等价类构造不同**：Rat存整数分子、非零自然数分母及互素证据，分母因此为正。它直接存规范对，不是书稿任意代表的等价类集合；规范记录与类的对应需由书稿先前的存在唯一性连接。 定位：Init/Data/Rat/Basic.lean：structure Rat（23–34）。
- **乘法实现与未经约分公式的联系**：实现先对交叉的分子和分母做gcd约分，再乘；mul_def证明结果等于规范化后的(ac,bd)。本书可以直接乘后规范化，但不能宣称两算法内部过程或复杂度相同。 定位：Basic.lean：Rat.mul（158–173）；Lemmas.lean：mul_def（389）、mul_def'（403）。
- **乘法律与分配的已读证明**：所读源码给出零、单位、交换、结合、分配及负号规律。结合与分配证明在分子分母表示上展开整数运算；这里不需要有理数次序作为书稿前置。 定位：Lemmas.lean：mul_comm（406）、zero_mul/mul_zero（409/410）、one_mul/mul_one（411/412）、mul_assoc（435）、add_mul（441）、mul_add（448）、neg_mul/mul_neg（451/455）。
- **倒数按整数分子符号规范化**：实现依据整数分子正负分支维持分母正；非零分子时倒数分母为分子绝对值。这里检查的是整数符号，不能混称为书稿已建立有理数次序。 定位：Basic.lean：Rat.inv（181–191）；Lemmas.lean：inv_def（459）、num_inv（470）、den_inv（477）。
- **零倒数和零除数的程序总函数约定**：库显式定义inv(0)=0，并定义a/b=a*inv(b)，因而a/0=0。这是库的全函数约定，不是本书允许零作乘法逆元或除数的依据。本书零的倒数与零除数均不定义。 定位：Basic.lean：Rat.inv文档及定义（178–191）、Rat.div（210–215）；Lemmas.lean：inv_zero（486）、div_def（529）。
- **非零条件下的逆元与除法消去**：r乘其倒数等于1明确要求r≠0；倒数唯一的相关定理由乘积为1先推出非零。除法与乘法抵消同样明确要求除数非零，不能遗漏。 定位：Lemmas.lean：mul_inv_cancel（494）、inv_mul_cancel（500）、inv_eq_of_mul_eq_one（503）、div_mul_cancel（538）、mul_div_cancel（541）。
- **零积证明的依赖顺序不可照搬**：定理结论无额外假设，但所读证明先右乘倒数并调用非零逆元抵消。书稿B1.16在B1.17之前，不能用这一证明链；应从代表分子乘积为零及整数零积独立推导，再证明非零乘法消去。 定位：Lemmas.lean：Rat.mul_eq_zero（519–527）。
- **无条件源码恒等式不等于本书无条件定义**：这些源码版本可以包含零构造输入或零值，因为库采用全函数约定。书稿涉及倒数和除法时先检查定义域；不得把源码无条件的双重倒数或积的倒数公式原封不动套在零输入上。 定位：Lemmas.lean：mkRat_mul_mkRat（424）、inv_divInt（489）、inv_inv（507）、inv_mul_rev（510）。

仅读取固定源码的声明、实现与证明结构；未运行Lean编译或书稿机器证明，未声称配套程序与库逐步相同。

## 本项目独立数学核对

这些是原创审查笔记，不是外部原文，不代表已经运行机器证明。

### MC01 乘法良定义的独立整数证明

若ab'=a'b且cd'=c'd，四个分母均为正，则bd、b'd'为正；由整数交换结合律，(ac)(b'd')=(ab')(cd')=(a'b)(c'd)=(a'c')(bd)。这正是两候选乘积代表的交叉等式。没有借用尚未定义的有理数除法。

### MC02 分配律须比较类而不是强求记录相同

取合法代表r=[(a,b)]、s=[(c,d)]、t=[(e,f)]。r(s+t)可表示为(a(cf+de),bdf)，rs+rt可表示为(ab(cf+de),b²df)。两份整数对通常不同，但它们的交叉乘积相等，因而类相等。分母都正，所用只有整数分配、交换与结合；不能直接把不同代表写成逐分量相等。

### MC03 先于倒数的零积与消去

rs以(ac,bd)表示，由零类判据，rs=0当且仅当ac=0；整数零积给a=0或c=0，再由零类判据得r=0或s=0。若r≠0且rs=rt，已证分配及相反数规律给r(s-t)=0，故s-t=0，于是s=t。这条书内顺序完全不需要倒数或有理数次序。

### MC04 非零有理数倒数的合法构造

设r=[(a,b)]且b>0，r≠0由零判据给a≠0。若a>0，候选为[(b,a)]；若a<0，候选为[(-b,-a)]，后一分母正。两分支直接用已证有理数乘法公式和整数符号律验证与r的乘积为1。这里的正负判断全属于整数a，不使用有理数序。

### MC05 倒数代表无关与唯一性

若ru=1且rv=1，由交换结合与单位律，u=u(rv)=(ur)v=v。因此为任意代表按MC04构造的候选都相等，定义代表无关；同时得到唯一性。零没有乘法逆元，因为0u=0而0≠1（整数嵌入单射）。非零r的逆元也非零，否则乘积不可能为1。

### MC06 除法定义域与方程

仅在s≠0时把r/s定义为r乘以s的倒数。用逆元性质验证s(r/s)=r，用非零乘法消去证明该方程解唯一。0/s在s≠0时为0。若s=0，方程0x=r在r=0时所有有理数x都是解，在r≠0时无解；这两种情况都不能定义一个唯一商，故包括0/0在内一律不定义。

### MC07 书稿与源码的引用界限

可用Lean的零积结论核对结论正确性，但不可将其先用倒数的证明标为本书B1.16的依赖；可用非零逆元抵消定理核对B1.17条件，但不可借inv_zero或div a 0的总函数约定扩展书稿定义域。除法构造代码应明确拒绝零除数，不能仅凭与库某次输出一致就通过。

## 简短引用建议

- 乘法代表公式与分式域条件可引用 [RMUL-JUDSON] 的 domains-section-field-of-fractions；说明乘法良定义及交换结合的详细证明由本书独立补足。
- 规范化乘法及分配律可引用 [RMUL-LEAN] 的 mul_def、mul_assoc、add_mul、mul_add，注意规范结构与等价类不同。
- 零积可核对 [RMUL-LEAN] 的 mul_eq_zero 结论，书稿证明则按MC03；不能把倒数反向列为B1.16先修。
- 倒数与除法引用 [RMUL-LEAN] 的 mul_inv_cancel、inv_mul_cancel、div_mul_cancel，并逐条保留非零条件。
- 明确本书不定义零的倒数和零除法，源码总函数的inv_zero、div a 0规则不移入正文。

## 实际请求与内容哈希

下列行号定位均指实际固定源码，不是印刷页码。

### judson_domains

https://raw.githubusercontent.com/twjudson/aata/3069910e3ded72ff5e18837a97a0e810c92790e2/src/domains.xml

访问：2026-10-27T16:20:35.331366+00:00；HTTP 200；verified_http_200。

字节数：80443；SHA-256：`cdadd1a266f58008c8ae025c76cf8dfcdeaa821f985253d348c58114715fdd04`。

### judson_front

https://raw.githubusercontent.com/twjudson/aata/3069910e3ded72ff5e18837a97a0e810c92790e2/src/frontmatter.xml

访问：2026-10-27T16:20:35.331916+00:00；HTTP 200；verified_http_200。

字节数：12931；SHA-256：`addf82ea52f863a28a6cf9372e7a42945c77cf36448ed99ce709a53dab6cfa23`。

### judson_copying

https://raw.githubusercontent.com/twjudson/aata/3069910e3ded72ff5e18837a97a0e810c92790e2/COPYING

访问：2026-10-27T16:20:35.332286+00:00；HTTP 200；verified_http_200。

字节数：427；SHA-256：`b7d47749512a424173f6a20daeea7b00f36b9f5ef95c25930fdbc3bd549b8983`。

### lean_rat_basic

https://raw.githubusercontent.com/leanprover/lean4/v4.24.0/src/Init/Data/Rat/Basic.lean

访问：2026-10-27T16:20:35.332646+00:00；HTTP 200；verified_http_200。

字节数：12914；SHA-256：`f92a643905d91f93d10026264553362081b328b8755f9d7ff2f770bc3bdf0755`。

### lean_rat_lemmas

https://raw.githubusercontent.com/leanprover/lean4/v4.24.0/src/Init/Data/Rat/Lemmas.lean

访问：2026-10-27T16:20:35.635008+00:00；HTTP 200；verified_http_200。

字节数：45941；SHA-256：`79f153962f148a08747db7d5c142a9d1990e90aec7dd7d8a228788f2c8bcd2d5`。

### lean_license

https://raw.githubusercontent.com/leanprover/lean4/v4.24.0/LICENSE

访问：2026-10-27T16:20:35.645414+00:00；HTTP 200；verified_http_200。

字节数：9160；SHA-256：`8b28515ffffc5c0fe2807d8ae3735b00b324d9b7ce807dd63ff6ac8922fbce7e`。

## 核查限制

- 未运行Lean形式验证或本书配套计算程序；源码可读不是已编译证明。
- Judson把乘法良定义、交换与结合的详细核查留作练习；不得写成已取得其完整逐步证明。
- Lean的零积证明先用倒数，不是本书B1.16的可直接采用证明链。
- Lean的inv_zero与零除法总函数约定不属于本书部分定义的数学除法。
- 来源采用规范对或一般非零分母等价类，均须与本书正分母等价类表示明确区分。
- 未检索或搬用外部题干、答案、图像或连续段落。
- 未取得出版PDF，不猜页码，只记录实际固定源码位置。
- 不把本批来源审查说成已经写出有理数次序或相关大小比较。

第三方全文仅暂存/tmp/integratedmath-rationals-multiplication-audit；仓库只新增本JSON与配套Markdown，包含元数据、许可短摘和原创核对摘要。
