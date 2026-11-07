# 整数基础批次：公开来源与数学条件交叉核查

核查日期：2026-10-27。这里只核对标准事实、定义条件与证明义务，不收录第三方题目、解答或连续正文。

## 访问与许可边界

已先读既有来源台账，并按 cloud-environment-runtime 技能读取网络参考、启动策略与运行时状态。启动策略为 restricted，所用 github.com 与 raw.githubusercontent.com 在允许列表内；运行时策略状态为 unknown，不据此声称策略执行已验证。全部请求保持继承代理和 TLS 校验，无登录、无绕过。

共 16 次公开只读请求：HTTP 200 共 15 次、HTTP 404 共 1 次。唯一失败为猜测的 Judson 根 LICENSE 路径返回 404；读取公开目录后找到 COPYING。每次请求的时间、最终 URL、字节数与 SHA-256 见本页后部及配套 JSON。

## [INT-JUDSON] Abstract Algebra: Theory and Applications

作者：Thomas W. Judson。

版本：Annual Edition 2026；前言日期 August 4, 2026；本次固定提交 3069910e3ded72ff5e18837a97a0e810c92790e2。

公开入口：https://github.com/twjudson/aata

许可：GNU Free Documentation License；共同兼容范围为 GFDL-1.3-or-later。

COPYING 写 1.3 或以后版本；活动前言 shortlicense 写 1.2 或以后版本。两处都无不变章节、前封面及后封面文字；本次不隐去差异，1.3 或以后版本同时在两处授权范围内。

许可短摘：`Version 1.3 or any later version; no Invariant Sections`。

- **等价关系、等价类与划分**：活动正文列出自反、对称、传递三条；定义等价类，并证明等价类构成划分。可核对本书先定义关系、再定义整数等价类的逻辑次序。 定位：src/sets.xml，sets-subsection-equivalence-relations，源码行 1125–1157、1270–1329。
- **整数自然数对构造的证据边界**：本次取得章节没有被确认为自然数对整数构造及其全部运算良定义的直接来源；不将这一教材泛化为已经核验本书完整构造。 定位：src/sets.xml 与 src/integers.xml，本次检索范围。

只核对标准定义、条件与证明义务并作引用；不复制或改编外部题目、答案、插图或连续正文，不向书稿分发包收入第三方全文。

## [INT-LEAN] Lean 4 core: Init.Data.Int.Basic, Init.Data.Int.Lemmas, Init.Data.Int.Order

作者：Jeremy Avigad；Leonardo de Moura；Deniz Aydin；Floris van Doorn；Mario Carneiro。

版本：v4.24.0，固定发布标签；不是声称截至核查日期的最新版本。

公开入口：https://github.com/leanprover/lean4/tree/v4.24.0/src/Init/Data/Int

许可：Apache-2.0。

许可短摘：`Released under Apache 2.0 license as described in the file LICENSE.`。

- **整数表示边界**：官方 Int 用 ofNat 和 negSucc 两类构造。它是独立的整数表示参照，不是自然数对商集构造的直接实现。 定位：Basic.lean，inductive Int，行 45–56。
- **取负、零积与乘法符号律**：双重取负恢复原数；任意整数与零相乘等于零；单一负号可移至积外，两个负号消去。所述代数恒等式本身不要求因子非零。 定位：Lemmas.lean：Int.neg_neg（102），Int.mul_zero/zero_mul（461/463），Int.neg_mul/mul_neg/neg_mul_neg（524/528/531）。
- **同加与取负的序关系**：同加一个整数保留并反映非严格比较；取负反转非严格或严格比较。 定位：Order.lean：Int.add_le_add_iff_left/right（275/278），Int.neg_le_neg_iff（297），Int.neg_lt_neg_iff（323）。
- **零、正、负因子的比较条件**：非负因子保留非严格比较，正因子保留严格比较；非正因子反转非严格比较，负因子反转严格比较。零因子两边均为零，因此不能保留严格比较或反映原比较。 定位：Order.lean：mul_lt_mul_of_pos_left/right（501/507），mul_le_mul_of_nonneg_left/right（514/524），mul_le_mul_of_nonpos_right/left（542/548），mul_lt_mul_of_neg_left/right（1156/1163）。
- **严格与非严格符号结论**：两个严格负数的积严格为正；两个非正数的积只能保证非负，零情形不能遗漏。 定位：Order.lean：mul_nonneg（490），mul_pos（495），mul_neg_of_pos_of_neg（1143），mul_neg_of_neg_of_pos（1147），mul_nonneg_of_nonpos_of_nonpos（1151），mul_pos_of_neg_of_neg（1170）。

仅阅读公开源码与定理条件；未安装、编译或运行本书对应 Lean 证明，不声明本书已获形式化验证。

只核对标准定义、条件与证明义务并作引用；不复制或改编外部题目、答案、插图或连续正文，不向书稿分发包收入第三方全文。

## [INT-MATHLIB] mathlib: MonoidLocalization.Basic and GrothendieckGroup

作者：Amelia Livingston；Alex J. Best；Yaël Dillies。

版本：master 活动源码，2026-10-27 实际下载快照；未固定提交，精确版本以逐文件 SHA-256 标识，不声称已读取整个一致构建。。

公开入口：https://github.com/leanprover-community/mathlib4/tree/master/Mathlib/GroupTheory/MonoidLocalization

许可：Apache-2.0。

许可短摘：`Released under Apache 2.0 license as described in the file LICENSE.`。

- **自然数对构造的群完备化参照**：群完备化取全子幺半群处的局部化，源码包含 to_additive 对应。一般关系保留额外见证因子；消去条件才允许约成两边交叉相等。对自然数加法这一可消去结构，独立翻译得 (a,b) 等价于 (c,d) 当且仅当 a+d=c+b。该特化为人工数学核对，不声称已运行生成的加法 Lean 定义。 定位：GrothendieckGroup.lean：GrothendieckGroup、of_injective；Basic.lean：r_iff_exists（191），mk_eq_mk_iff'（798），其前置 IsCancelMul 假设（791）。
- **代表元无关是定义下降到等价类的前提**：单输入定义须在等价代表元上同值；双输入须对两个输入分别更换代表元后同值。仅写出代表元公式不能代替这项证明。 定位：Basic.lean：liftOn（280），liftOn₂（303），源码行 272–308。
- **嵌入需消去条件**：源码明确一般交换幺半群映射至群完备化不自动单射；自然数嵌入的证明应使用已建立的自然数加法消去，而非把任意商映射当作单射。 定位：GrothendieckGroup.lean：of 文档及 of_injective。

此来源核对一般群完备化及良定义框架；不直接证明本书自然数对整数的乘法与序关系。该两项在下列独立数学审查中逐项核对。未运行 Lean/mathlib 编译或形式证明。

只核对标准定义、条件与证明义务并作引用；不复制或改编外部题目、答案、插图或连续正文，不向书稿分发包收入第三方全文。

## 独立数学核对（本项目原创审查笔记）

以下是对拟写规则的人工代数核对，不是外部教材原文，也不是已运行的形式证明。自然数包含零，并已具备交换、结合、分配、加法消去和序反映等前置结论。

### IC01 等价关系传递性

若 a+d=c+b 且 c+f=e+d，则 a+d+f=c+b+f=e+d+b。用自然数结合/交换律重排，再消去同一 d，得 a+f=e+b。不使用尚未定义的整数减法。

### IC02 加法良定义

设 a+b'=a'+b，c+d'=c'+d。两式相加并重排，得 (a+c)+(b'+d')=(a'+c')+(b+d)。因此按分量相加的结果等价。

### IC03 取负良定义

(a,b) 的负元取 (b,a)。由 a+b'=a'+b，经交换对称得 b+a'=b'+a，所以更换代表元不改变负元等价类。

### IC04 乘法良定义

乘法代表元公式为 (a,b)(c,d)=(ac+bd,ad+bc)。先只换第一对，假设 a+b'=a'+b。待证的交叉和左侧 ac+bd+a'd+b'c=c(a+b')+d(b+a')，右侧 a'c+b'd+ad+bc=c(a'+b)+d(b'+a)，两侧由假设及其对称式相等。再利用自然数交换律直接核对代表元乘法交换，便可同样更换第二对；等价关系传递性合并两次更换。没有使用整数乘法已良定义或整数分配律。

### IC05 序关系良定义

定义 [(a,b)]≤[(c,d)] 当且仅当 a+d≤c+b。若 a+b'=a'+b、c+d'=c'+d，在原比较两边同加 b'+d'，重排替换后得到 (a'+d')+(b+d)≤(c'+b')+(b+d)。自然数同加的保留与反映允许消去共同 b+d，得新代表元的比较。逆向同理。严格比较亦使用自然数严格序的同加反映。

### IC06 零因子与负因子边界

正因子保留严格比较；负因子反转严格比较。非负/非正因子只能分别保证保留/反转非严格比较。零因子使两边同时为零，因此不能从乘后相等、≤或≥反推出原比较，也不能把严格不等式保持为严格不等式。两个非正数的积非负；若要严格正，两个因子都须严格负。

### IC07 符号律证明依赖

先建立整数运算良定义、加法逆元唯一性与分配律；由 x(-y)+xy=x((-y)+y)=0，才推出 x(-y)=-(xy)。双负乘积由该式及双重取负推出。不能用“负负得正”作为乘法良定义的依据再反向援引它。

## 建议的短引用

- 等价关系与等价类定义之后引用 [INT-JUDSON]，定位 sets-subsection-equivalence-relations；不要把它写成自然数对整数构造的完整来源。
- 自然数对构造及良定义说明后引用 [INT-MATHLIB]，注明为“群完备化与代表元无关性的框架参照”；正文仍逐步证明自然数特化与乘法、序的良定义。
- 整数符号律、零与负因子比较条件之后引用 [INT-LEAN]，保留 v4.24.0 和相应定理名，并明说“源码条件交叉核对，未运行形式验证”。

## 实际请求、许可证据与内容哈希

以下定位的行号只指实际下载的源码快照，不是印刷页码。mathlib master 为活动分支，哈希用于识别本次读取的确切内容；不声称整个仓库处于已验证的一致构建。

### lean_basic

https://raw.githubusercontent.com/leanprover/lean4/v4.24.0/src/Init/Data/Int/Basic.lean

访问：2026-10-27T14:42:19.952899+00:00；HTTP 200；状态 verified_http_200。

字节数：12478；SHA-256：`8cc0f7dd682be29c06b2f33e14a998087e02d0b4f9eb1b5f7739f1828e49d083`。

### lean_order

https://raw.githubusercontent.com/leanprover/lean4/v4.24.0/src/Init/Data/Int/Order.lean

访问：2026-10-27T14:42:19.953577+00:00；HTTP 200；状态 verified_http_200。

字节数：59747；SHA-256：`1b3b31b6097a4c2e7109f95b3d68b0d5e638628e89d0f21a90645851237dc20e`。

### lean_license

https://raw.githubusercontent.com/leanprover/lean4/v4.24.0/LICENSE

访问：2026-10-27T14:42:19.954108+00:00；HTTP 200；状态 verified_http_200。

字节数：9160；SHA-256：`8b28515ffffc5c0fe2807d8ae3735b00b324d9b7ce807dd63ff6ac8922fbce7e`。

### judson_readme

https://raw.githubusercontent.com/twjudson/aata/master/README.md

访问：2026-10-27T14:42:19.954469+00:00；HTTP 200；状态 verified_http_200。

字节数：445；SHA-256：`103a09088e2c074d7c7f8e1d67c8b0a83bf7e035c97f242424b9a6db68e8318b`。

### judson_license

https://raw.githubusercontent.com/twjudson/aata/master/LICENSE

访问：2026-10-27T14:42:20.354647+00:00；HTTP 404；状态 http_error。

错误：HTTP Error 404: Not Found。

### judson_tree

https://github.com/twjudson/aata/tree/master

访问：2026-10-27T14:42:31.329869+00:00；HTTP 200；状态 verified_http_200。

字节数：267329；SHA-256：`cd6fac2f4043221862e23cf3239471d186d99bd3e5921c9729cef635a0898672`。

### judson_src

https://github.com/twjudson/aata/tree/master/src

访问：2026-10-27T14:42:39.214748+00:00；HTTP 200；状态 verified_http_200。

字节数：288490；SHA-256：`8d59a8d7528b9c981335d399864e3d32e2ec32154135a9dea5ec9967cedb16f1`。

### judson_sets

https://raw.githubusercontent.com/twjudson/aata/3069910e3ded72ff5e18837a97a0e810c92790e2/src/sets.xml

访问：2026-10-27T14:42:54.411196+00:00；HTTP 200；状态 verified_http_200。

字节数：97708；SHA-256：`fa1d972edf851618fd869a7a1e5ff1dbcf7a9e5135f603087aff4bc418131b15`。

### judson_integers

https://raw.githubusercontent.com/twjudson/aata/3069910e3ded72ff5e18837a97a0e810c92790e2/src/integers.xml

访问：2026-10-27T14:42:54.411935+00:00；HTTP 200；状态 verified_http_200。

字节数：63296；SHA-256：`0a01f88637265349a34cd2aac96aa6170deae6a42fa0dd5c91f9694bdcafe8a1`。

### judson_front

https://raw.githubusercontent.com/twjudson/aata/3069910e3ded72ff5e18837a97a0e810c92790e2/src/frontmatter.xml

访问：2026-10-27T14:42:54.412652+00:00；HTTP 200；状态 verified_http_200。

字节数：12931；SHA-256：`addf82ea52f863a28a6cf9372e7a42945c77cf36448ed99ce709a53dab6cfa23`。

### judson_copying

https://raw.githubusercontent.com/twjudson/aata/3069910e3ded72ff5e18837a97a0e810c92790e2/COPYING

访问：2026-10-27T14:42:54.413434+00:00；HTTP 200；状态 verified_http_200。

字节数：427；SHA-256：`b7d47749512a424173f6a20daeea7b00f36b9f5ef95c25930fdbc3bd549b8983`。

### judson_bookinfo

https://raw.githubusercontent.com/twjudson/aata/3069910e3ded72ff5e18837a97a0e810c92790e2/src/bookinfo.xml

访问：2026-10-27T14:42:54.750854+00:00；HTTP 200；状态 verified_http_200。

字节数：3289；SHA-256：`22595213d6307f7e31d0f7a07b26908786e9ee865f6114f61f0f5bafa2c0d1ea`。

### lean_lemmas

https://raw.githubusercontent.com/leanprover/lean4/v4.24.0/src/Init/Data/Int/Lemmas.lean

访问：2026-10-27T14:42:54.786019+00:00；HTTP 200；状态 verified_http_200。

字节数：26132；SHA-256：`b58b2cbf8e8310b49d950d3d634eb133dc688752b1b263cccde42960eb480034`。

### mathlib_groth

https://raw.githubusercontent.com/leanprover-community/mathlib4/master/Mathlib/GroupTheory/MonoidLocalization/GrothendieckGroup.lean

访问：2026-10-27T14:43:32.583399+00:00；HTTP 200；状态 verified_http_200。

字节数：3622；SHA-256：`fc8a0d15f6d72486f8c05ffe8ff7ca523bb10d0ea8781befb26bc1cc53e31712`。

### mathlib_license

https://raw.githubusercontent.com/leanprover-community/mathlib4/master/LICENSE

访问：2026-10-27T14:43:32.583933+00:00；HTTP 200；状态 verified_http_200。

字节数：11357；SHA-256：`b40930bbcf80744c86c46a12bc9da056641d722716c378f5659b9e555ef833e1`。

### mathlib_basic

https://raw.githubusercontent.com/leanprover-community/mathlib4/master/Mathlib/GroupTheory/MonoidLocalization/Basic.lean

访问：2026-10-27T14:43:45.860228+00:00；HTTP 200；状态 verified_http_200。

字节数：41731；SHA-256：`a28224156f8d73ff6b8c86265c210809085da9faef8462ab5279c33141a33590`。

## 尚未建立的结论

- 未运行 Lean 或 mathlib 编译、证明检查；不宣称书稿形式化验证完成。
- 未核验任何外部习题及答案并收入书稿。
- 未取得出版PDF，不猜测页码；定位使用XML标识、定理名和实际下载源码行号。
- mathlib 群完备化不是本书整数乘法和序关系证明的直接替代；本书须自足写出相关证明。
- Judson 本次只用于等价关系/等价类框架，不声称所读整数章包含全部自然数对构造。

第三方全文仅在 /tmp/integratedmath-integers-audit 暂存供核查，不写入仓库或最终分发包。永久产物仅本JSON及配套Markdown。
