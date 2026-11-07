# 整数除法、整除与最大公因数：公开来源核查

核查日期：2026-10-27。用于B1.9–B1.11；不收录外部原题、答案或连续段落。

## 方法与范围

已读取云运行技能、网络参考与本机策略，并查询运行状态。启动策略为restricted，raw.githubusercontent.com在允许列表；运行时策略状态仍为unknown，故不宣称执行状态已验证。本轮全部请求经原代理、保留TLS验证，无登录、无绕过。

采用两个独立来源系列：固定提交的Judson教材与Lean 4 v4.24.0核心源码。共10次请求，9次HTTP 200、1次HTTP 404。404仅为不存在的Int/Dvd.lean路径，随后直接从已知导入链中的Bootstrap.lean读到整除声明。

## [DIV-JUDSON] Abstract Algebra: Theory and Applications

作者：Thomas W. Judson。

版本：Annual Edition 2026；前言日期 August 4, 2026；本次固定提交 3069910e3ded72ff5e18837a97a0e810c92790e2。

公开入口：https://github.com/twjudson/aata

许可：GNU Free Documentation License；两处声明共同允许 GFDL-1.3-or-later。

许可短摘：`Version 1.3 or any later version; no Invariant Sections`。

根 COPYING 声明1.3或以后版本，活动前言声明1.2或以后版本；两者均无不变章节和封面文字要求。共同可用范围为1.3或以后版本，不隐去差异。

- **正除数整数带余除法**：声明 a,b 为整数且 b>0；存在唯一整数 q,r 使 a=bq+r 且 0≤r<b。来源证明分别处理存在与唯一。本次不将正除数版本说成直接包含负除数的定理。 定位：src/integers.xml：integers-theorem-division_algorithm，行294–369。
- **整除允许零与负数**：整除按整数乘法见证定义，a|b 当且仅当存在整数k使b=ak；没有要求a或b非零，也没有要求a为正。 定位：src/integers.xml，带余除法定理之后的整除定义，行372–377。
- **最大公因数与双零边界**：来源将gcd描述为正的公因数，且其他任意公因数都整除它。本书非负gcd及gcd(0,0)=0的扩展不能直接归给这段定义；双零时不存在通常大小意义下最大的正公因数。 定位：src/integers.xml，行377–390。
- **Bézout恒等式与唯一性**：所读定理要求a,b都非零，说明存在整数系数使gcd为a,b的整数线性组合，并论证唯一性。本书覆盖单零或双零时，必须另证这些边界情形，不能把来源原陈述扩写成无条件原文。 定位：src/integers.xml：integers-theorem-gcd，行398–445。
- **欧几里得算法与回代**：正文以重复带余除法产生严格递减的正余数，并用回代恢复线性组合。可核对方法；本书仍需明确绝对值初始化、第二分量为零的停止条件、余数降到零及单步可执行性，不能将这一概述当成覆盖全部有符号输入的伪代码。 定位：src/integers.xml：integers-subsection-euclidean-algorithm，特别行503–526。

仅核对数学事实、条件与约定并引用；不转载、翻译或改编题干、答案、插图、连续段落；不在仓库及最终分发包保存第三方全文。

## [DIV-LEAN] Lean 4 core: integer DivMod, integer Gcd, natural-number Gcd

作者：Jeremy Avigad；Mario Carneiro；Kim Morrison；Markus Himmel；Leonardo de Moura。

版本：v4.24.0 固定发布标签；不声称为核查日期最新版本。

公开入口：https://github.com/leanprover/lean4/tree/v4.24.0/src/Init/Data

许可：Apache-2.0。

作者按文件头区分：

- `Init/Data/Int/DivMod/Basic.lean`：Jeremy Avigad；Mario Carneiro。
- `Init/Data/Int/DivMod/Bootstrap.lean`：Jeremy Avigad；Mario Carneiro。
- `Init/Data/Int/DivMod/Lemmas.lean`：Jeremy Avigad；Mario Carneiro；Kim Morrison；Markus Himmel。
- `Init/Data/Int/Gcd.lean`：Mario Carneiro；Markus Himmel。
- `Init/Data/Nat/Gcd.lean`：Jeremy Avigad；Leonardo de Moura；Mario Carneiro；Markus Himmel。

许可短摘：`Released under Apache 2.0 license as described in the file LICENSE.`。

- **Euclidean余数的符号约定**：所读E约定要求非零除数时余数非负且小于除数的自然数绝对值；重构恒等式为a=bq+r。不同于负除数时余数随除数为负的其他约定，不能直接用某语言默认除余而不检查。 定位：Int/DivMod/Basic.lean：E-rounding division；Bootstrap.lean：mul_ediv_add_emod（123）、emod_nonneg（214）；Lemmas.lean：emod_lt（754）。
- **正负除数的唯一性**：两个定理分别以b>0、b<0为前提，给出商余等于指定q,r与重构恒等式加余数范围的双向等价。负除数的上界是-b。 定位：Int/DivMod/Lemmas.lean：Int.ediv_emod_unique（804）、Int.ediv_emod_unique'（815）。
- **除数取负的商余变化**：除数变号时商取负、余数不变；与本书统一0≤r<|b|的约定一致。 定位：Bootstrap.lean：ediv_neg（146）；Lemmas.lean：emod_neg（729）。
- **程序全函数与零除数的界限**：库为程序全函数另定义a/0=0、a%0=a。该实现约定不提供0≤r<0的带余除法，也不构成本书允许零除数的数学依据。 定位：Int/DivMod/Basic.lean，行19–53。
- **整除定义与零、符号**：整除用整数乘法见证。任意整数整除0；0整除n当且仅当n=0；改变除数或被整除数的符号不改变整除关系。 定位：Int/DivMod/Bootstrap.lean：Int.dvd_def（26）、dvd_zero（28）、zero_dvd（47）、neg_dvd（55）、dvd_neg（59）。
- **整除与余数为零**：源码在其全函数余数约定下无条件写出整除与余数为零的等价；本书余数只定义于非零除数，因此本书版本必须保留除数非零条件。 定位：Int/DivMod/Bootstrap.lean：dvd_iff_emod_eq_zero（305）。
- **gcd非负规范、零和符号**：gcd由两整数绝对值的Nat.gcd定义，返回自然数。gcd(a,0)=|a|，符号变化不改变gcd，且gcd(a,b)=0当且仅当两输入都为0。非双零情形才严格为正。 定位：Int/Gcd.lean：gcd（41）、zero_gcd/gcd_zero（57/58）、neg_gcd/gcd_neg（67/68）、gcd_eq_zero_iff（327）、gcd_pos_iff（330）。
- **gcd的整除刻画**：返回值整除两输入，且一切整数公因数都整除它；gcd_eq_iff使用自然数g这一非负规范。它适合统一处理双零，而不是仅按通常数值大小取最大。 定位：Int/Gcd.lean：gcd_dvd_left/right（48/51）、dvd_coe_gcd_iff（94）、gcd_eq_iff（333）。
- **欧几里得递归、终止和不变量**：Nat.gcd模型在m=0时返回n，否则递归到(n%m,m)，以非零m条件下n%m<m证明第一参数严格下降。公因数刻画和加整数倍不变的定理与本书欧几里得不变量相互核对。本书若使用(a,b)→(b,r)，对应递降量是第二参数，应明确调整索引。 定位：Nat/Gcd.lean：gcd（33）、termination_by m（38）、gcd_rec（72）、gcd_dvd（85）、dvd_gcd（98）；Int/Gcd.lean：gcd_add_mul_right_right（223）及对称变体。

仅阅读指定版本源码、声明和证明结构，未运行Lean编译或本书形式化证明。未将源码运行时优化描述为本书程序的性能保证。

## 独立数学交叉核对

以下为本项目原创审查笔记，前置采用已经建立的整数运算、序、自然数下降与带余除法。不代表运行过机器证明。

### DC01 负被除数与负除数的构造核对

先对|a|与正b作自然数除法。若a<0且|a|=bu+v，v=0时取q=-u、r=0；0<v<b时取q=-(u+1)、r=b-v。两式分别重构a且余数合法。若原除数为负，先对|b|求商t，再取q=-t、同一r；由b=-|b|验证bq=|b|t。此为本项目独立核对，不转载来源证明。

### DC02 零与符号的整除见证

d|0取见证0；0|n若成立则n=0k=0，逆向同样取0。若n=dk，则n=(-d)(-k)、-n=d(-k)，故两处符号均可改变。允许0|0不等于允许零作带余除法的除数。

### DC03 整除/余数判别的定义域

本书余数R_b(n)只在b≠0时定义；因此b|n iff R_b(n)=0须先声明b≠0。零的整除关系另用存在整数见证定义处理。不能照搬库的无条件余数等价而遗漏本书定义域。

### DC04 欧几里得公因数不变量

设a=bq+r。若d|a且d|b，取a=du、b=dv，则r=a-bq=d(u-vq)，故d|r。若d|b且d|r，取b=dv、r=dw，则a=d(vq+w)，故d|a。此双向结论允许d=0，无需约掉d；因此(a,b)与(b,r)的整数公因数完全一致。

### DC05 gcd双零与终止边界

若按非负公因数g且所有公因数整除g定义，则双零时0本身是公因数，故g必须满足0|g，从而g=0；反之每个整数都整除0。这与数值最大不同。欧几里得算法可从(|a|,|b|)开始；b=0立即返回a，否则下一第二分量r满足0≤r<b，由自然数严格下降终止。每步除法也须由先前算法或明确计算模型保证有限完成。

### DC06 Bézout边界及回代依据

任一步若当前两数是原始输入的整数线性组合，余数a-qb仍为这种组合，因系数可相减并乘整数。终止得到的非负g因而有线性组合表达。若从绝对值开始，应先根据原数符号给出|a|和|b|各自的系数；单零时可直接用非零输入的符号系数，双零取系数(0,0)。Judson只直接陈述双非零版本，这些边界须本书自证。

## 建议的短引用

- B1.9 正除数存在唯一性后引用 [DIV-JUDSON] 的 integers-theorem-division_algorithm；统一非零除数与余数非负约定可用 [DIV-LEAN] 的两个 ediv_emod_unique 版本交叉核对。
- B1.10 整除定义后引用 [DIV-JUDSON] 整除定义及 [DIV-LEAN] dvd_def；零与符号边界参照 Bootstrap.lean 中 dvd_zero、zero_dvd、neg_dvd、dvd_neg。
- B1.11 非负规范及双零约定参照 [DIV-LEAN] Int.gcd、gcd_eq_zero_iff、gcd_eq_iff；欧几里得方法和Bézout参照 [DIV-JUDSON] 相应XML定理及子节。保持原文范围与本书自行补证的边界分开。
- 推荐表述“已核对公开源码中的条件与约定”，不要写“本书已通过Lean形式验证”。

## 实际请求记录

行号只指所列固定源码，不是出版页码。每个成功响应均记录实际字节数和SHA-256；许可证据也作为独立请求保留。

### lean_div_basic

https://raw.githubusercontent.com/leanprover/lean4/v4.24.0/src/Init/Data/Int/DivMod/Basic.lean

访问：2026-10-27T15:12:57.003611+00:00；HTTP 200；verified_http_200。

字节数：11432；SHA-256：`dfe8dc498a423cc91e2c7fd0a774d9177ca04118ffb0704a9fe3f1731a470d31`。

### lean_div_lemmas

https://raw.githubusercontent.com/leanprover/lean4/v4.24.0/src/Init/Data/Int/DivMod/Lemmas.lean

访问：2026-10-27T15:12:57.004556+00:00；HTTP 200；verified_http_200。

字节数：126698；SHA-256：`5342dd65e6f2160736b4c7d59de78a563caec9e8b28e7ca0276362f54f3fa57b`。

### lean_int_gcd

https://raw.githubusercontent.com/leanprover/lean4/v4.24.0/src/Init/Data/Int/Gcd.lean

访问：2026-10-27T15:12:57.006192+00:00；HTTP 200；verified_http_200。

字节数：30387；SHA-256：`5e70a3fc0098291ec090a592e50f69aec0d6325932b1cef1af3b0b877d4a5c67`。

### lean_nat_gcd

https://raw.githubusercontent.com/leanprover/lean4/v4.24.0/src/Init/Data/Nat/Gcd.lean

访问：2026-10-27T15:12:57.007353+00:00；HTTP 200；verified_http_200。

字节数：21111；SHA-256：`f827a14a65f9c67ce9ff3c4995462230efe3d10b6d83b38dfe46e23041570262`。

### lean_license

https://raw.githubusercontent.com/leanprover/lean4/v4.24.0/LICENSE

访问：2026-10-27T15:12:57.349435+00:00；HTTP 200；verified_http_200。

字节数：9160；SHA-256：`8b28515ffffc5c0fe2807d8ae3735b00b324d9b7ce807dd63ff6ac8922fbce7e`。

### judson_integers

https://raw.githubusercontent.com/twjudson/aata/3069910e3ded72ff5e18837a97a0e810c92790e2/src/integers.xml

访问：2026-10-27T15:12:57.350058+00:00；HTTP 200；verified_http_200。

字节数：63296；SHA-256：`0a01f88637265349a34cd2aac96aa6170deae6a42fa0dd5c91f9694bdcafe8a1`。

### judson_front

https://raw.githubusercontent.com/twjudson/aata/3069910e3ded72ff5e18837a97a0e810c92790e2/src/frontmatter.xml

访问：2026-10-27T15:12:57.372302+00:00；HTTP 200；verified_http_200。

字节数：12931；SHA-256：`addf82ea52f863a28a6cf9372e7a42945c77cf36448ed99ce709a53dab6cfa23`。

### judson_copying

https://raw.githubusercontent.com/twjudson/aata/3069910e3ded72ff5e18837a97a0e810c92790e2/COPYING

访问：2026-10-27T15:12:57.375757+00:00；HTTP 200；verified_http_200。

字节数：427；SHA-256：`b7d47749512a424173f6a20daeea7b00f36b9f5ef95c25930fdbc3bd549b8983`。

### lean_int_dvd

https://raw.githubusercontent.com/leanprover/lean4/v4.24.0/src/Init/Data/Int/Dvd.lean

访问：2026-10-27T15:14:22.162245+00:00；HTTP 404；http_error。

错误：HTTP Error 404: Not Found。

### lean_div_bootstrap

https://raw.githubusercontent.com/leanprover/lean4/v4.24.0/src/Init/Data/Int/DivMod/Bootstrap.lean

访问：2026-10-27T15:14:22.162943+00:00；HTTP 200；verified_http_200。

字节数：14839；SHA-256：`624060b933dbb36bbe5ac851ba2e136a6688af663282024ef72767c7b255070b`。

## 核查限制

- 未运行Lean或mathlib形式验证；本书仍须提供自足证明。
- 未检索或复制任何第三方题目和答案；未保存第三方全文到仓库或分发包。
- 未取得排版出版PDF，所有位置为固定源码的XML标识、声明名或行号，不猜页码。
- Judson正gcd及双非零Bézout范围不直接覆盖本书全部零边界。
- Lean零除数全函数约定不是本书的数学除法定义。
- 本轮使用两个独立来源系列：Judson教材与Lean核心库；未额外扩搜mathlib或未知预印本。

第三方文本仅暂存/tmp/integratedmath-divisibility-audit供检查；永久输出仅本JSON与配套Markdown，内容为元数据、许可短摘、独立摘要。
