# Bézout、扩展欧几里得与互素：公开来源核查

核查日期：2026-10-27。范围为B1.12–B1.13，数学核对不依赖素数理论。

## 访问、独立性与许可范围

先读云运行技能、网络参考和本机策略；运行阶段为running，观测为当前，网络策略状态仍为unknown。使用允许列表中的raw.githubusercontent.com，保持代理与TLS验证，未登录、未绕过限制。7次真实请求全部HTTP 200。

Judson教材与Lean/mathlib资料提供两个来源系列；Lean与mathlib存在依赖，不能夸称三个完全独立的证明系统。此次Lean与mathlib均读取v4.24.0固定标签，Judson使用固定提交，不沿用旧master内容猜测版本。

## [BEZ-JUDSON] Abstract Algebra: Theory and Applications

作者：Thomas W. Judson。

版本：Annual Edition 2026；前言日期 August 4, 2026；本次固定提交 3069910e3ded72ff5e18837a97a0e810c92790e2。

公开入口：https://github.com/twjudson/aata

许可：GNU Free Documentation License；两处声明共同允许 GFDL-1.3-or-later。

许可短摘：`Version 1.3 or any later version; no Invariant Sections`。

根 COPYING 声明1.3或以后版本，活动前言声明1.2或以后版本；两者均无不变章节和封面文字要求。共同可用范围为1.3或以后版本，不隐去差异。

- **Bézout的原文范围**：定理明确要求两个输入均为非零整数；证明取正整数线性组合的最小元，并用带余除法建立其公因数性质。原文没有覆盖双零时正线性组合集合为空的情形。 定位：src/integers.xml：integers-theorem-gcd，行398–445。
- **互素时的线性组合**：推论陈述互素整数存在整数系数使线性组合为1。该推论的字面范围未要求两个输入均非零，但紧前定理限定两输入非零；本书应自行说明(0,±1)、(±1,0)这些边界，不能把省略当成已经展开的论证。 定位：src/integers.xml：integers-corollary-coprime，行451–459。
- **扩展算法的数学思想**：所读段说明递减余数及逐步回代得到原输入的整数线性组合；适合核对扩展欧几里得思想，不替代本书逐轮系数不变量、符号初始化、双零及单步有限性的证明。 定位：src/integers.xml：integers-subsection-euclidean-algorithm，行503–526。

仅核对事实、条件和证明结构；不转载或改编原题、答案、图像及连续正文；不在仓库或最终分发包保存第三方全文。

## [BEZ-LEAN] Lean 4 core: Init.Data.Int.Gcd

作者：Mario Carneiro；Markus Himmel。

版本：Lean v4.24.0 固定发布标签。

公开入口：https://github.com/leanprover/lean4/blob/v4.24.0/src/Init/Data/Int/Gcd.lean

许可：Apache-2.0。

许可短摘：`Released under Apache 2.0 license as described in the file LICENSE.`。

- **非负gcd及零输入**：gcd返回自然数，由输入绝对值定义；双零取0且只有双零时为0。至少一个输入非零时gcd严格为正。 定位：Init/Data/Int/Gcd.lean：gcd（41），zero_gcd/gcd_zero（57/58），gcd_eq_zero_iff（327），gcd_pos_iff（330）。
- **除以gcd后互素的条件**：前两版本分别要求左输入或右输入非零；统一版本要求0<gcd(i,j)。结论是两精确整除所得整数的gcd为1。不能去掉此前提而应用于双零。库的/为整数除法；此处gcd整除两输入，所以商为精确整数商。 定位：Init/Data/Int/Gcd.lean：gcd_ediv_gcd_ediv_gcd_of_ne_zero_left（399）、同名right版本（404）、gcd_ediv_gcd_ediv_gcd（409）。
- **互素的公因数表述**：gcd为1等价于每个共同整数因数都整除1。此刻画不限于正输入，也没有素数分解前提。 定位：Init/Data/Int/Gcd.lean：gcd_eq_one_iff（375）。

只阅读指定源码的声明及证明调用，没有运行Lean编译或本书形式化证明。

## [BEZ-MATHLIB] mathlib: Mathlib.Data.Int.GCD — extended GCD and Bézout

作者：Sangwoo Jo (aka Jason)；Guy Leroy；Johannes Hölzl；Mario Carneiro。

版本：mathlib4 v4.24.0 固定发布标签；与此前台账master快照区分。

公开入口：https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Data/Int/GCD.lean

许可：Apache-2.0。

许可短摘：`Released under Apache 2.0 license as described in the file LICENSE.`。

- **扩展算法及递降量**：算法保存两组余数与整数系数，余数更新为自然数取模，系数按旧系数减去商乘新系数更新。递降量为当前首个自然数余数，非零步用严格余数界；xgcdAux_P明确保存原输入线性组合不变量。 定位：Mathlib/Data/Int/GCD.lean：Nat.xgcdAux（40–46）、Nat.xgcd（58）、xgcdAux_P（112）。
- **自然数与全体整数的Bézout**：自然数输入得到整数系数。整数版本按两输入符号调整自然数系数，所读定理对所有整数x,y量化，无非零前提，包含单零、双零与负数。 定位：Mathlib/Data/Int/GCD.lean：Nat.gcd_eq_gcd_ab（126）；Int.gcdA（157）、Int.gcdB（162）、Int.gcd_eq_gcd_ab（167–176）。
- **零输入系数并非唯一规范**：自然数左输入0时系数为(0,1)，所以双零也取(0,1)；右输入0且左输入非零时系数为(1,0)。整数版本再按符号调整对应系数。书稿算法在双零采用(0,0)或(1,0)同样满足恒等式；核对结果应检查线性组合等式，不能要求系数逐项等于库的选择。 定位：Mathlib/Data/Int/GCD.lean：Nat.gcdA_zero_left（70）、gcdB_zero_left（75）、gcdA_zero_right（80）、gcdB_zero_right（87）及Int.gcdA/gcdB。
- **互素整数对的抽取**：要求gcd严格正，结论给出互素整数对及共同正因数的精确重构；双零不满足前提。 定位：Mathlib/Data/Int/GCD.lean：Int.exists_gcd_one（203）、exists_gcd_one'（208）。
- **互素消去而不依赖素数**：若a整除bc且gcd(a,c)=1，则a整除b；另一版本将互素对象换为a,b。源码证明直接展开Bézout线性组合并使用整除对和与乘积的封闭性，不依赖素数或唯一分解。 定位：Mathlib/Data/Int/GCD.lean：Int.dvd_of_dvd_mul_left_of_gcd_one（231）、Int.dvd_of_dvd_mul_right_of_gcd_one（242）。
- **线性组合判别的输入类型边界**：该声明的目标n类型为自然数，输入a,b为整数。可作为判别框架参考，不能称这一具体声明已经逐字覆盖任意有符号目标整数；本书如使用任意整数目标应自行补证。 定位：Mathlib/Data/Int/GCD.lean：Int.gcd_dvd_iff（213）。

已读源码与证明结构，未编译mathlib，未运行xgcd，也未证明本书程序与库返回系数逐项一致。Lean核心与mathlib属于相关形式化生态，不把两者当作两个完全独立数学来源；另一独立视角来自Judson教材。

## 独立数学核对

以下为本项目原创论证笔记，使用已建立的整数运算、gcd、公因数不变量及自然数下降。它们不是外部教材原文，也不表示已经运行机器证明。

### BC01 Bézout对所有整数的本地数学核对

任意整数a,b，令A=|a|、B=|b|。采用符号系数ε_a,ε_b∈{-1,0,1}满足A=ε_a a、B=ε_b b（零取0）。自然数欧几里得过程中维护每个当前余数都是A,B的整数线性组合；新余数R-qS由对应系数相减保持此性质。终止得到g=gcd(A,B)，故g=Ax+By=a(ε_a x)+b(ε_b y)。初始A=B=0时算法立即结束，取系数0,0可直接验证0=0。gcd的绝对值不变性连接到gcd(a,b)。这是原创证明核对，不冒称Judson原定理无条件。

### BC02 互素与线性组合为1的双向核对

gcd(a,b)=1时由全整数Bézout得ax+by=1。反向若有该等式，gcd(a,b)整除a,b，故整除1；它非负且不能为0，所以等于1。双零没有线性组合为1，故不是互素；gcd(0,b)=|b|说明零仅与1或-1互素。

### BC03 互素消去的直接证明

设gcd(d,a)=1且d|ac。取整数u,v使du+av=1，两边乘c，得c=d(uc)+(ac)v。右侧两项都被d整除，故d|c。这里只用Bézout、整数分配律和整除闭包，不用素数，也不需要另加d≠0；若d=0，互素迫使a=±1，而0|ac已迫使c=0。

### BC04 除以正gcd的约分

设a,b不同时为0，g=gcd(a,b)>0，写a=gu、b=gv，其中u,v为精确整数商。Bézout给g=ax+by=g(ux+vy)，由g≠0的整数乘法消去得1=ux+vy，故gcd(u,v)=1。双零时g=0，不允许把约分写成除以0。若原b>0，则v>0：v≤0将导致gv≤0，与b>0矛盾。

### BC05 正分母原始整数对的交叉乘积唯一性

设b,d为正整数，a,c为整数，gcd(a,b)=gcd(c,d)=1，且ad=bc。由b|ad及gcd(b,a)=1，用互素消去得b|d；由d|bc及gcd(d,c)=1同理得d|b。正整数互相整除推出b=d。再用b≠0在ab=cb中消去b，得a=c。这是本项目从已经核对的消去定理推得的原创论证，不声称所读外部文件中有同名完整定理。

### BC06 零分子和规范条件的作用

若正分母的原始对(a,b)满足a=0，则gcd(0,b)=b=1，故其规范对为(0,1)。去掉分母正条件时，同时变号的两对给出相同交叉乘积，不能推出两对字面相等；去掉互素条件时，共同倍乘也破坏唯一性。这些结论以整数对和交叉乘积表述，不预先依赖尚未定义的有理数除法。

## 建议的短引用

- B1.12 可引用 [BEZ-JUDSON] 的 integers-theorem-gcd，并注明其原陈述为双非零；全整数和系数不变量交叉核对用 [BEZ-MATHLIB] 的 Int.gcd_eq_gcd_ab、Nat.xgcdAux_P。
- 扩展算法正文应允许不同合法系数；双零系数与库不同不构成错误，应核验重构等式和非负gcd。
- B1.13 互素约分用 [BEZ-LEAN] 的 gcd_ediv_gcd_ediv_gcd，保留gcd>0条件；互素消去用 [BEZ-MATHLIB] 的两个 dvd_of_dvd_mul_*_of_gcd_one 版本。
- 正分母原始整数对唯一性按BC05自行给完整证明，并回引书内互素消去；不得把该本地推论标成已读取的外部同名定理。

## 请求记录与哈希

定位行号指固定源码，不是印刷页码。每次成功读取均核验以下字节数和SHA-256。

### judson_integers

https://raw.githubusercontent.com/twjudson/aata/3069910e3ded72ff5e18837a97a0e810c92790e2/src/integers.xml

访问：2026-10-27T15:37:07.281053+00:00；HTTP 200；verified_http_200。

字节数：63296；SHA-256：`0a01f88637265349a34cd2aac96aa6170deae6a42fa0dd5c91f9694bdcafe8a1`。

### judson_front

https://raw.githubusercontent.com/twjudson/aata/3069910e3ded72ff5e18837a97a0e810c92790e2/src/frontmatter.xml

访问：2026-10-27T15:37:07.281644+00:00；HTTP 200；verified_http_200。

字节数：12931；SHA-256：`addf82ea52f863a28a6cf9372e7a42945c77cf36448ed99ce709a53dab6cfa23`。

### judson_copying

https://raw.githubusercontent.com/twjudson/aata/3069910e3ded72ff5e18837a97a0e810c92790e2/COPYING

访问：2026-10-27T15:37:07.282126+00:00；HTTP 200；verified_http_200。

字节数：427；SHA-256：`b7d47749512a424173f6a20daeea7b00f36b9f5ef95c25930fdbc3bd549b8983`。

### lean_int_gcd

https://raw.githubusercontent.com/leanprover/lean4/v4.24.0/src/Init/Data/Int/Gcd.lean

访问：2026-10-27T15:37:07.282737+00:00；HTTP 200；verified_http_200。

字节数：30387；SHA-256：`5e70a3fc0098291ec090a592e50f69aec0d6325932b1cef1af3b0b877d4a5c67`。

### lean_license

https://raw.githubusercontent.com/leanprover/lean4/v4.24.0/LICENSE

访问：2026-10-27T15:37:07.566549+00:00；HTTP 200；verified_http_200。

字节数：9160；SHA-256：`8b28515ffffc5c0fe2807d8ae3735b00b324d9b7ce807dd63ff6ac8922fbce7e`。

### mathlib_int_gcd

https://raw.githubusercontent.com/leanprover-community/mathlib4/v4.24.0/Mathlib/Data/Int/GCD.lean

访问：2026-10-27T15:37:07.571727+00:00；HTTP 200；verified_http_200。

字节数：11775；SHA-256：`a5288dc1b1814d5fc41c8a3bdff90d3099d3d357f2f804b13ab83205796db63e`。

### mathlib_license

https://raw.githubusercontent.com/leanprover-community/mathlib4/v4.24.0/LICENSE

访问：2026-10-27T15:37:07.587002+00:00；HTTP 200；verified_http_200。

字节数：11357；SHA-256：`b40930bbcf80744c86c46a12bc9da056641d722716c378f5659b9e555ef833e1`。

## 核查限制

- 未编译或运行Lean/mathlib；未宣称本书通过形式化验证。
- 未声称扩展算法系数唯一，也未要求本书双零系数与mathlib逐项相同。
- 未将Judson双非零Bézout条件隐去。
- 正分母原始对的交叉乘积唯一性为本地从已核对的互素消去作出的独立推论，不冒称从外部找到该完整原文。
- 未读取出版PDF，定位仅使用固定源码的XML标识、定理名与实际行号，不猜页码。
- 未复制第三方题干、答案、图像或连续段落。

第三方完整文本只暂存/tmp/integratedmath-bezout-audit用于核查；仓库永久输出仅本JSON与配套Markdown元数据、短许可证据、独立摘要。
