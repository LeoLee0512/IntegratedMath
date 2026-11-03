# B2.11 有理数的非负整数幂：独立数学复核

审阅者：Astra/high独立数学代理。日期：2026-10-29。结论：本单元正文与8题完整答案数学通过，无待解决数学阻断。已实际读完同批四稿与16全解；两作者确认冻结。

## 递归、指数律与边界

实际核对B1.1任意对象范围X上的固定更新递归原则，而非只限自然数值的递归。新定义固定a∈Q，取X=Q、初值1、T_a(z)=za，先核乘法封闭与输出唯一，再取得P_a:N→Q；存在性没有被归纳唯一性取代。0^0=1明确属于这一离散非负整数幂的初值约定，不由约去零推得，不给0/0赋值，也未涉及极限。旧a^{-1}仍是非零条件下的倒数记号。

POW1分别处理一次幂、1的幂、零底数后继幂及非零底数非零幂；零判据的反向使用正自然数存在前驱，覆盖n=1而未错误假设0^0=0。POW2固定a,m对n归纳，索引的自然加法与值的有理乘法清楚分开；POW3独立归纳并明确交换中间b^n与a，没有预用一般乘积重排。POW4在POW2之后对外层指数归纳，用mn+m=m(n+1)，无循环引用。a=0、m=0、n=0均由相同证明覆盖，未无故施加非零底数条件。

η=j∘ι的中间域/目标均为Z，符合既有严格复合约定；单射与保0、1、加、乘来自两层既有嵌入，并非未加说明地把N、Z、Q底层对象等同。POW5准确针对旧b≥2自然幂，先嵌入旧乘法再递推新幂。负号与底数括号分清，偶奇指数公式不消去可能为零的a；偶数指数零边界值为1，正指数零底数值为0。

## 八题完整答案

| 题 | 实际逐项核验 |
| --- | --- |
| 1 | 连乘值1,−2/3,4/9,−8/27正确；0^0与0/0操作区别清楚，所有分母非零。 |
| 2 | 唯一性归纳任意n成立，再核同域N同目标Q以用FC1；另说明存在性须依递归原则，a=0亦不除零。 |
| 3 | 全参数指数加法证明分固定a,m与归纳n，后继索引及结合律逐步展开；a=m=n=0两边1。 |
| 4 | 四因子重排所用交换明确；a=−3/2,b=2/5两路均−27/125，约分因子8非零。 |
| 5 | 幂的幂使用已证POW2；((−1/2)^2)^3=1/64，而五次幂−1/32，括号/指数运算不混同。 |
| 6 | 非零幂归纳、零判据的两个方向及正指数前驱齐全；(0^0)^0和0^(0·0)均1。 |
| 7 | (−1)偶/奇指数、(−a)^n乘积展开正确；a=0与k=0单独核查，不取消任何零因子。 |
| 8 | 旧自然幂与新有理幂兼容从保1/乘法归纳；b=10,n=2得η(100)，平方和反例4≠2。 |

## 修订闭环

全文读取实际正文与八份解答后，再核最终三处增补：先修列入严格函数复合；POW4例给出1/4平方到1/16、立方到1/64的中间乘法；答案5拆行并展开同一计算。最终稿全部等式与条件正确，无剩余数学阻断。未以计划中的预写答案代替正式稿阅读。

## 实际依赖与范围

已完整读取本批四份实际稿件及16题完整答案，核对最终修订；批准只绑定下列最终哈希，不把预备计划或其他代理的意见视为全文证据。实际检查的既有接口包括B1.1归纳/固定更新递归、自然数后继比较及加法保序反映、条件减法、旧位值自然幂与非空自然数和、有理加乘/零乘积/非零除法、两层嵌入及三数据函数的逐点相等与严格复合。B1.1原则是书中公开采用的基础，没有被说成已完成集合论构造。有限表仍是固定域I_n、固定目标Q的函数；不同长度表即使同和值也不因而相等。

本批只涵盖Q底数的自然指数与有理有限前缀和。没有负/分数/实指数、无限和及收敛、一般有限置换、双三重求和换序、卷积或正式多项式对象；当前两单元不能视为97H20或第528章全部完成。

## 实现与主验证器

已全文读取tools/rational_powers_sums.py与validate_rational_powers_sums.py，核对主JSON记录的源码哈希。rational复用既有精确输入检查，只接受exact int/Fraction，拒bool和float。power先验证底数和exact int非负指数，再从Fraction(1)连乘；即使指数0也先拒非法底数。partial_sums先验证整张list/tuple表，再输出长度n+1的不可变元组(S0,…,Sn)，S0为Fraction(0)。finite_sum取最后累计值，空表为0。segment_sum先验证整张表，再核0≤start≤len、count≥0、start+count≤len；末端空段合法，段外非法项仍拒。Fraction(2)作为指数被拒属于API表示约定，不是在数学上否定该数为自然数；任意迭代器和回调不属于API输入。

主验证器以Fraction内置整数幂、对独立切片的标准精确sum作oracle。实际JSON记录：50次幂，245次指数加法、245次幂的幂、175次乘积幂，781张表、3711前缀、10791连续段、3711分割、3124尾补零、3905缩放、16276逐项加、68非法输入拒绝与781输入不变性检查，另有六个明确示例。本审阅读取了该实际记录与程序，没有冒称重新执行该次主验证器运行。

## 独立有限oracle

本审阅实际执行独立脚本：幂的预期用整数分子、分母各自二分求幂，未调用Fraction幂；求和预期先取所有分母的乘积，再在整数中累计通分后的分子，最后仅构造一次Fraction，不照抄被测逐项有理累加过程。七个底数、指数0…12共91次幂；另1029次三条指数律检查。五值项集合、长度0…5给3906张表；22461前缀、76416合法连续段、22461拼接、11718缩放、16276逐项加全部一致。68次非法输入拒绝涵盖bool/float、非法自然指数、容器与段边界，并明确测试空段之外的坏项也被拒。

完整可重放代码与实际输出附于finite_sums_math_review.md，脚本SHA-256为124ce52897eed02df3478ceddbdf35879388b098c37ac592ad2ed0c98c9f7ade。该独立脚本不另声称覆盖主验证器的尾补零与输入不变性计数。所有有限枚举只支持实现与边界检查，不是一般数学命题的证明；一般结论来自本批逐步归纳与逐题证明。

## 来源与批准边界

已全文读取本地powers_sums_sources_2026-10-29.md和JSON，不重新联网。审计保留20次真实访问（19次HTTP200、一次候选多项式路径404及后续正确路径），并明确区分当前幂/有限和与未来多项式预读。OpenStax固定提交、CC-BY-NC-SA-4.0；mathlib v4.24.0、Apache-2.0。OpenStax的零指数条款要求非零底数，不被冒用为本书0^0约定依据；mathlib自然幂提供相应离散语境，但只是源码阅读，没有Lean编译或本书形式验证。来源预备诊断计数不是本模块测试计数，未混用。

本报告不批准最终PDF逐页视觉效果、发布、合并或推送。图注中数学值与含义已读，图和版式验收仍属另一个环节；冻结稿改变须按差异重新绑定。

最终稿行数依次为幂正文422、幂答案319、有限和正文467、有限和答案322。四稿题答互链与先修引用已检查，唯一不在manuscript目录内的来源锚powers-sums-sources由构建程序提供。来源最后登记POW1—5/SUM1—5及η接口已读回；常量和的mathlib nsmul与本书η(n)c区别得到明确，不把库的一般标量作用当作本书先修。

最终构建后追加复核：有限和图注把纯文本S_n、n、S_0改成数学模式 $S_n$、$n$、$S_0$。已实际读回，并将该处反向还原后得到上一冻结正文哈希e8ed699b9cd3b8428e9286b3f18cf4c90720fcc55c5b2b6c93aad071df4359b0，证实没有其他正文差异；图注的数学定义与数值未改变。此处只复核源文本，不授予PDF视觉批准。

## 四稿最终哈希

| 文件 | SHA-256 |
| --- | --- |
| `manuscript/foundations/rational_powers.md` | `581010522535b41a771d0dd920531b37669b379ea64ce6001028620988bb3ee2` |
| `manuscript/foundations/rational_powers_answers.md` | `fe64ec1b757dedb07583460db31afe240c9a1c0845c78a10603787ba2acef102` |
| `manuscript/foundations/finite_sums.md` | `ea736adc9c09e27a9443cd24a11af4c3a1f1fcad72824a8f7430b3a4b670ea23` |
| `manuscript/foundations/finite_sums_answers.md` | `127a6dd135315f2ccf2f9e4931e0e0c5f8c3a4adfb511b4f962cd70f552b4704` |

## 依赖、代码与来源审计绑定

| 文件 | SHA-256 |
| --- | --- |
| `manuscript/foundations/functions_composition.md` | `806b32944f8253b2e2af3b2a551a25cc0ce6bf17ce51cc6b50216cf28e58a94a` |
| `manuscript/foundations/functions_definition.md` | `1dee6ffb8bada53f6f09ea4ad908c0a03fd06c937fb685538566175cb9655650` |
| `manuscript/foundations/integers_addition_order.md` | `bd18f2b22e9a8b2ef116c5835140eb79beacc4499e489dbfc8e6a38c89778672` |
| `manuscript/foundations/integers_multiplication.md` | `4bc038ace8d4fe782843098e3f171cf1e2b78b3e79a8169baea9d4bbdfa52bba` |
| `manuscript/foundations/natural_numbers.md` | `709c9ebf1f580c8bf7af17b494ecd07505dd33f65ccfe49482675fe7712880f3` |
| `manuscript/foundations/natural_order.md` | `4ad8e874bedda7f4c15739fd47344903ec71bd9a5b538c71bde0f9827b091435` |
| `manuscript/foundations/natural_subtraction.md` | `92d1ac5e3cf6c07f61afd8f84e1e96d0556bf62d752e1d2a854121b66c412247` |
| `manuscript/foundations/place_value.md` | `93c1182d304b216a0a3b73cf4e4b2fd23dd370f31a9db8ffcd85c08eadf0fb45` |
| `manuscript/foundations/positional_representation.md` | `d1967565dd6e58c8980da21d33ba071dba401e8621141d5f15b9074153f82c09` |
| `manuscript/foundations/rationals_addition.md` | `9b349aec9a9df0c7c45c9d33e7d0cfa483dc22432f0250baa23ab2a6d02b417b` |
| `manuscript/foundations/rationals_construction.md` | `0833130ad2bd8f24598a8c8fdfd3ce38e03874036fceac57b019d6d9c7da45a0` |
| `manuscript/foundations/rationals_division.md` | `b2adb43e3d4b0fbe5c57dd6b745cfa1550f050321a2208df618a666ca8ecfc64` |
| `manuscript/foundations/rationals_multiplication.md` | `033ed077c363d91143247bebedb790d4c444b5574c5085509a2b6c207d0b9c20` |
| `tools/linear_equation_solvers.py` | `c3ec0ab4a892397d3d0af59a1acd367bf1f1cfea80e3e14bd6b2b6cd790b74c9` |
| `tools/rational_powers_sums.py` | `fad8cf2a22151b4d584ba09ea3464526668cf34d2737afdf0374f241f16cfda4` |
| `tools/validate_rational_powers_sums.py` | `9318a2df81bf07d952cc8e5db1f6dd4f41b05a3ad67384719200267eec88ce0e` |
| `research/production/rational_powers_sums_validation.json` | `9e845a9d8b0d9253178a6dd222297c7da6d7ec290fdf3de78dbdb786997ab121` |
| `research/production/powers_sums_sources_2026-10-29.md` | `bb77d0334f86315d1cb34a725d0e86470be8fe8f427eb386e22c7f93a2546b79` |
| `research/production/powers_sums_sources_2026-10-29.json` | `e3758d928704f77b435e1f581d2a4c1ddafdd5bc6a2d92dd96131baa0843a03d` |
| `research/production/finite_sums_math_review.md` | `894b8e0e1ac616be0badc89d60d5fd5b09203d817674b27956162ae36f77b215` |
