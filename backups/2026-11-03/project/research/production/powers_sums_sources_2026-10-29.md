# 非负整数幂与有限和：公开来源审计（2026-10-29）

范围：B2.11有理数的非负整数幂、B2.12有限和。当前是来源审计，不是书稿审阅或完成判定。多项式仍为未来工作，本批未收入其对象、运算、求值或相关分类覆盖。

## 真实访问记录

从已实核临时计划正式化，保留原核查时间2026-10-29T17:36:24.461240+00:00以及逐请求访问时刻；没有在正式化时重新抓取。20次实际请求中19次HTTP 200，1次候选Polynomial/Degree/Defs.lean返回404，正确Definitions.lean随后另取200。失败下载器只保存HTTP状态，未保存异常字符串或响应正文，故不补造错误原文。20条原记录全部保留于JSON，成功响应字节数/SHA-256已核。

公开访问沿继承代理和TLS验证，环境运行、策略enforced且观测当前，无认证、凭据或远程Git操作。

### POWSUM-OPENSTAX：Intermediate Algebra 2e

版本：osbooks-prealgebra-bundle commit ad40c7e3c9a909cde81a24c526f52fe26a51fb14。许可：CC-BY-NC-SA-4.0。只核数学条件与术语，不复制正文、外部题答或图。非商业与相同方式共享限制不可误写为CC BY；图片有独立例外，本批不转载。

作者：Lynn Marecek、Andrea Honeycutt Mathis。

- [m81384，fs-id1167835595382，Exponential Notation](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81384/index.cnxml#L51)（modules/m81384/index.cnxml，行51–65）：按重复乘法介绍指数；本书须递归定义所有n∈N含0，而不能由正次数的省略号自动推出零次数。
- [m81384，Product Property for Exponents](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81384/index.cnxml#L94)（modules/m81384/index.cnxml，行94–100）：同底乘法合并指数的代数形式。源涉及更广的实底数/整数指数语境；本批仅Q底数和非负整数指数，用归纳证明。
- [m81384，fs-id1167826869964 / fs-id1167831969999](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81384/index.cnxml#L401)（modules/m81384/index.cnxml，行401–412）：零指数条款明确只限非零底数，教材声明被取零次幂的变量非零。它不为本书0^0=1约定提供依据；本书由离散递归单独明确规定，且不据此允许0/0。
- [m81384，fs-id1167830898684](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81384/index.cnxml#L860)（modules/m81384/index.cnxml，行860–865）：幂的幂合并指数。框中写实底数和整数指数，未逐项重述负指数非零条件；本书不照搬扩大范围，本批只n,m∈N。
- [m81384，fs-id1167826996996](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81384/index.cnxml#L991)（modules/m81384/index.cnxml，行991–997）：乘积的非负整数幂逐因子取幂；本书归纳时明确用有理乘法交换结合，不暗示任意非交换对象同样成立。

### POWSUM-MATHLIB：mathlib natural powers and finite sums

版本：mathlib4 v4.24.0。许可：Apache-2.0。阅读源码与前提，不复制实现，未运行Lean编译，也未形式化书稿。to_additive源注解与生成声明的对应不声称为本地编译结果。

逐文件作者见JSON及实际文件头：Jeremy Avigad、Leonardo de Moura、Simon Hudon、Mario Carneiro、Johannes Hölzl。

- [Monoid.npow_zero / npow_succ / pow_zero / pow_succ](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Group/Defs.lean#L586)（Mathlib/Algebra/Group/Defs.lean，行586–619）：自然数幂的零次值为1，对每个底数成立，含带零的乘法结构中的0；后继由右乘底数给出。该约定是离散幂，不是除法或极限规则。
- [one_pow / pow_add / pow_mul](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Group/Defs.lean#L650)（Mathlib/Algebra/Group/Defs.lean，行650–667）：幺半群背景即可对自然数指数归纳证明；pow_add与pow_mul写出零分支及后继分支，无非零底数假设。
- [CommMonoid / mul_pow](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Group/Basic.lean#L204)（Mathlib/Algebra/Group/Basic.lean，行204–214）：乘积幂要求可交换乘法背景。书稿的Q已具备，但不能把来源条件删去后推广。
- [Finset求和的AddCommMonoid背景](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/BigOperators/Group/Finset/Defs.lean#L19)（Mathlib/Algebra/BigOperators/Group/Finset/Defs.lean，行19–25）：有限集合求和预先使用可交换加法结构；不等于本书未经定义的任意求和符号。书稿先定义有序前缀和，再证明要用的有限性质。
- [prod_empty，@[to_additive]](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/BigOperators/Group/Finset/Defs.lean#L347)（Mathlib/Algebra/BigOperators/Group/Finset/Defs.lean，行347–356）：加法对应空和为零；这里读取了to_additive源注解，未运行Lean编译验证生成定理。
- [prod_range_succ / eventually_constant_prod / prod_range_add，@[to_additive]](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/BigOperators/Group/Finset/Basic.lean#L522)（Mathlib/Algebra/BigOperators/Group/Finset/Basic.lean，行522–552）：加法对应前n项和的后继、零尾稳定和前缀拼接偏移。范围range n按i<n定义；n>0时才可写0,…,n−1，空范围和为0；本书须证明索引边界而不是把上界n误作末项。
- [prod_mul_distrib，@[to_additive]](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/BigOperators/Group/Finset/Basic.lean#L303)（Mathlib/Algebra/BigOperators/Group/Finset/Basic.lean，行303–305）：加法对应逐项相加的和等于两和之和；本书用归纳和有理加法交换结合独立证明。
- [sum_mul / mul_sum](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/BigOperators/Ring/Finset.lean#L46)（Mathlib/Algebra/BigOperators/Ring/Finset.lean，行46–54）：有限和左右乘常数的分配，源背景具有加法交换与左右分配；本书以有理数规律和前缀长度归纳独立证明，不把后续矩形双和自动列为本批成果。

- [prod_const / pow_eq_prod_const，@[to_additive]](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/BigOperators/Group/Finset/Basic.lean#L628)（Mathlib/Algebra/BigOperators/Group/Finset/Basic.lean，行628–645）：加法对应常量有限和为项数次重复加法；库用自然数标量作用nsmul。本书尚未定义一般标量作用，故另用η(0)=0、η(n+1)=η(n)+1及分配律归纳证明SUM3的η(n)c，不能把自然数n直接当成Q对象。

## 现有递归前提与独立推导

本书natural_numbers.md #b1-recursion-principle已经明确采用任意对象范围X和固定更新T:X→X；它不是只允许自然数值，也没有直接给出依赖当前索引的更新形式。原稿锚与哈希见JSON。

1. 幂：固定a∈Q，取已采用递归原则的X=Q、初值1、更新T(z)=za。必须先核乘法封闭/唯一，获得唯一p_a:N→Q，定义a^n=p_a(n)。明示a^0=1包括0^0=1，这是离散自然数幂的约定，不能由a^m/a^m在a=0时推导，也不允许0/0。
2. 指数律：a^(m+n)=a^m a^n对n归纳；(a^m)^n=a^(mn)对n归纳，调用自然数乘法后继及前式；(ab)^n=a^n b^n对n归纳并显式使用有理乘法交换结合。n=0、m=0、a=0都在起始/后继中覆盖。0^n=0只对n>0；1^n=1对n≥0。负底数括号与负号位置先说明。
3. 有限和：给u:N→Q，原递归只允许固定状态更新，取X=N×Q，初值(0,0)，T(i,s)=(i+1,s+u(i))。T处处定义且值在X；递归得F(n)，归纳首分量为n，第二分量记Σ_n u，于是Σ_0u=0，Σ_(n+1)u=Σ_nu+u(n)。这合法使用原任意X原则，不暗增索引依赖递归公理。
4. 边界：Σ_n指前n项、索引0≤i<n，不是0至n；含末项n要写Σ_(n+1)。空表n=0和为0。有限表可先零延拓到N，但须证明只要前n项一致，Σ_n便相同，因而不依赖任意表外扩展。
5. 和式基本律：零序列、逐项和、常数倍分别按前缀长度归纳；结合、交换和左右分配只用于当前两个有理数，不能直接当作任意有限重排已经证明。若教逐项取负，也用递归或和的相反数唯一证明。
6. 拼接：对后段长度m归纳，证明Σ_(n+m)u=Σ_nu+Σ_m(i↦u(n+i))，逐项处理索引n+(i+1)与(n+i)+1。若u(i)=0对i≥N，则N之后任意更长前缀和相同；空前段、空后段、零尾与不同可用上界全部覆盖。

7. 实际POW5还核新旧幂兼容：η=j∘ι:N→Q，其中ι由int-embedding进入Z，j由rat-integers进入Q；逐层单射及保零、一、加、乘来自int-addition-laws、imul-basic-laws、radd-integers、rmul-integers。旧pos-value-lemmas对自然b≥2给B0=1、B(n+1)=B(n)b，按n归纳得η(Bn)=η(b)^n。自然指数n与有理系数η(n)分别标明；该接口复用已写证明，没有新增外部访问。

8. 实际SUM3固定c∈Q并对项数n归纳，空和与η(0)c同为0；后继由Σ_(n+1)=Σ_n+c=(η(n)+1)c=η(n+1)c。此处只用明确的N→Q嵌入和分配律，c=0或负数无需除法。索引I_n按j<n定义，n=0时不写无定义的自然差n−1。

## 边界与分类

OpenStax零指数条款只对非零底数陈述；本书采用对所有有理底数的离散递归，因而明确规定0^0=1。这个约定不能用于除零，也不声明实指数极限中的任何规则。正次零幂仍为零，n=0须单列。

有限和按前n项定义，索引为自然数j<n；只有n>0时才可写至n−1，n=0时不形成未定义的自然差，空和为零。带索引更新经N×Q状态对实现，并证明第一分量确为索引。有限表外延拓需用前缀一致性证明与前n项和无关；拼接和尾零是有界归纳结论，不授权任意双三索引重排。若把自然数项数用于有理乘法，须先给出N→Q嵌入接口，不混用索引数和有理系数。

主归属第63部分、第528章97Hxx的97H20。函数模块中只增加这两个有限教学目标，43模块先修图不需新增节点。正文实际题答齐备后应为33单元、264基础题加绪论14题共278题；主97H20首次有正文，5章/28末级有草稿。章、叶与63部分均不因单元通过而完成，push未到期；正式JSON等待主线程最终QA。

## 有限诊断与未来资料隔离

预备审计的精确检查：幂加法及幂迭代882次，乘积幂567次，前缀拼接9000次，和式线性3600次；全部通过。它们只检查有限输入下的计划公式，不能替代一般归纳证明，也不冒充当前新稿或伴生实现的测试。

为保留真实访问历史，JSON继续列出此前多项式、系数、求值、次数、有限支撑及双索引重排的请求；每条另标current或preparatory范围。那些资料不属于本批引用证明目标，不登记“多项式已写”或环论覆盖。最初下载标签不代替真实标题：openstax_products实际为m81384指数性质；openstax_powers实为m81383多项式加减，后者本批未采用。

两单元正文、证明组织、题答独立编写，不复制OpenStax题目、图或连续文本，也不复制mathlib实现。实际定义、命题与先修锚已按作者正文核对并登记于JSON；锚存在不等于书稿通过审阅。

## 实际单元接口与临时台账核验

B2.11（pow-unit）：POW1 #pow-zero 零次、一次、单位底数和幂为零的完整判据；POW2 #pow-addition 同底数乘法的指数加法规律；POW3 #pow-product 可交换有理乘法下乘积的幂；POW4 #pow-iteration 幂的幂与自然指数乘法；POW5 #pow-compatibility 自然数嵌入有理数后新旧位值幂相容。各8道题与8个独立答案锚存在并配对。

B2.12（sum-unit）：SUM1 #sum-extensionality 前n项一致决定前缀和及有限表延拓独立；SUM2 #sum-linearity 逐项相加与有理常数缩放的有限和规则；SUM3 #sum-constant 常量有限和等于嵌入项数乘常量；SUM4 #sum-concatenation 移位序列及连续有限表拼接的和值公式；SUM5 #sum-padding 尾补任意有限个零保持和值。各8道题与8个独立答案锚存在并配对。

η接口位于rational_powers.md #pow-compatibility，定义为j与ι的严格复合，保零、一、加、乘且单射；有限和SUM3显式使用η(n)c，不把n从索引类型悄悄换成有理数。

临时生成目录/tmp/powers-sums-ledger-check-5rc_2ztt已核33单元、264基础题加绪论14题共278题，5章/28末级有草稿、0章或部分完成，43模块无环；63部分push均not_due。对6836ad6比对旧31条UNIT_SPECS、43条MODULES、62个旧BRIDGE路径与CH01接口逐项不变，新增先修均指向此前单元。正式data/production七份JSON在检查前后哈希不变。临时副本不含构建PDF，不能把本次台账与锚检查当作最终构建或视觉验收。
