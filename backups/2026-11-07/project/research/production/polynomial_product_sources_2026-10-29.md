# 多项式乘法、求值与次数：公开来源审计 {#poly-product-sources}

来源条件已核，B2.15/B2.16四稿正式路径、锚点及SHA已登记；独立审阅、构建视觉和最终验收另记。整章、分类叶及模块保持部分草稿。

## 实际访问与许可

复用11条原成功请求，逐一重验字节数与SHA-256；新增2条实际请求：Degree/Operations.lean HTTP200，Eval/Basic.lean HTTP404（14字节错误正文已保存）。随后在原Eval/Defs.lean缓存找到eval_mul；原时间与本次复核时间分开保存在JSON。此前Degree/Defs.lean历史404不重复计入本次选用记录。

OpenStax固定commit ad40c7e3c9a909cde81a24c526f52fe26a51fb14，作者Lynn Marecek、Andrea Honeycutt Mathis，CC-BY-NC-SA-4.0。mathlib固定v4.24.0，相关多项式文件署名Chris Hughes、Johannes Hölzl、Kim Morrison、Jens Wagemaker，有限和文件署名Johannes Hölzl，Apache-2.0。只核数学条件；不复制外部题目、段落、图像或实现。未编译Lean、未形式化书稿。

## 逐条定位与条件

- [Multiply Monomials](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81385/index.cnxml#L55)，lines 55–56。条件：非负整数指数的单项式；本章已把形式表达式乘法视为可操作对象。 本书边界：用指数相加解释移位动机，不能取代本书系数对象乘法的定义与良定义证明。
- [Multiply a Polynomial by a Monomial](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81385/index.cnxml#L132)，lines 132–133。条件：默认表达式分配律。 本书边界：本书应先定义记录移位与数乘，用已证有限和事实证明求值，不把分配律当尚未构造的多项式乘法公理。
- [FOIL limitation](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81385/index.cnxml#L539)，lines 539–539。条件：FOIL只适用二项式；分配与竖式用于一般多项式。 本书边界：卷积是逐指标收集同次项；例题应含中间零和三项以上，防止把FOIL当通法。
- [Multiply a Polynomial by a Polynomial](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81385/index.cnxml#L610)，lines 610–611。条件：表达式教学而非规范代表构造。 本书边界：取一般分配/竖式作为教学参照，不复制其题目、段落或图片，不借它证明有限索引重排。
- [Polynomial structure](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Basic.lean#L61)，lines 61–65。条件：[Semiring R]；系数为 AddMonoidAlgebra R N。 本书边界：库的多项式类型依赖已建半环及有限支持代数；本书仅有规范记录与已证加法数乘，不能把整套实例借入。
- [private mul](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Basic.lean#L110)，lines 110–111。条件：[Semiring R]；底层AddMonoidAlgebra乘法。 本书边界：本书必须独立定义候选系数、证明有限支撑、规范化与表示无关。
- [monomial_mul_monomial](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Basic.lean#L411)，lines 411–414。条件：[Semiring R]；库乘法已经定义。 本书边界：单项式乘积指数相加、系数相乘；本书可在正式乘法后推出对应结论。
- [coeff_mul](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Coeff.lean#L102)，lines 102–109。条件：[Semiring R]；有限反对角集 i+j=n；已有有限集合求和与卷积。 本书边界：等价的前缀式为 sum(i=0..n) cP(i)cQ(n−i)，每项i≤n，差有定义。该等价在本书需有限索引证明，不能仅引用库转换。
- [mul_coeff_zero / mul_coeff_one](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Coeff.lean#L111)，lines 111–117。条件：[Semiring R]。 本书边界：核对常数项与一次项作为诊断，不以几个系数核对代替全指标公式。
- [coeff_mul_X_pow / coeff_mul_X_pow'](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Coeff.lean#L220)，lines 220–237。条件：[Semiring R]，库已有X的多项式幂。 本书边界：来源给一般幂移位，并仅在h≤k分支读取自然差k−h；本批只独立定义单步S并证明c_SP(0)=0与c_SP(j+1)=c_P(j)，未定义一般S_h或X^h，也不以尚未建立的多项式幂乘法定义移位。
- [eval₂_mul_noncomm](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Eval/Defs.lean#L136)，lines 136–141。条件：源Semiring R、目标Semiring S、环同态f；要求每个q系数的像与x交换。 本书边界：任意非交换目标并非无条件保乘；本书Q的交换律满足需求，但仍须独立证明有限卷积求值恒等式。
- [eval₂_mul](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Eval/Defs.lean#L191)，lines 191–195。条件：目标CommSemiring S；源Semiring R；f环同态。 本书边界：来源通过交换条件得到保乘，不能把此结论反向当本书乘法定义或形式相等判据。
- [eval_mul / evalRingHom](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Eval/Defs.lean#L578)，lines 578–586。条件：R为CommSemiring。 本书边界：有理数取值时 E_(PQ)(t)=E_P(t)E_Q(t)，包含t=0；本书0^0=1由离散幂定义保障常数项。
- [degree / natDegree](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Degree/Definitions.lean#L44)，lines 44–53。条件：degree值域WithBot N，degree(0)=bottom；natDegree(0)=0。 本书边界：本书零次数未定义，两种库接口都不能在零对象上直接替代书稿次数。
- [degree_mul' / natDegree_mul' / leadingCoeff_mul'](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Degree/Operations.lean#L304)，lines 304–329。条件：[Semiring R] 且两个首项系数乘积非零。 本书边界：首项乘积非零是精确条件；不能在任意有零因子的系数环中无条件声称次数相加。本书Q由已证零乘积判据推出。
- [degree_mul](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Degree/Operations.lean#L666)，lines 666–674。条件：[Semiring R] [NoZeroDivisors R]；WithBot次数。 本书边界：库对零因子分支用bottom加法；本书先分别证明零乘积，再限定P,Q非零证明PQ非零及deg(PQ)=degP+degQ。
- [leadingCoeff_mul](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Degree/Operations.lean#L688)，lines 688–694。条件：[Semiring R] [NoZeroDivisors R]；零输入分支显式处理。 本书边界：库的最高系数乘法公式依赖无零因子；本书Q可独立逐卷积证明，不能引用该公式省去次数证明。
- [sum_mul / mul_sum / sum_mul_sum](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/BigOperators/Ring/Finset.lean#L49)，lines 49–57。条件：该节NonUnitalNonAssocSemiring背景，有限集合求和已建。 本书边界：可以复核有限分配式；本书已有前缀SUM2即可独立归纳，不能直接借一般双重重排。
- [prefix successor / padding / concatenation via to_additive](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/BigOperators/Group/Finset/Basic.lean#L527)，lines 527–552。条件：原声明在交换乘法幺半群中，to_additive给加法对应。 本书边界：本书实际应引用已证SUM1—5并按新增需求证明单步移位、反向前缀或三角形求和，不把一般有限重排作为隐藏先修。

## 本书必须补足的证明

1. 与next18方案对齐，只定义单步S(P)：前接一个0再规范化。候选长度n+1≥2；逐指标证明c_SP(0)=0及c_SP(j+1)=cP(j)，并核零输入、表示无关及加法数乘相容。无需新增一般移位S_h。
2. 用SUM4、SUM2及数值幂递推证明E_(SP)(t)=t E_P(t)，包括P=0、t=0；仅单步移位不需一般幂加法或多重索引。
3. 若定义d_k=sum(i∈I_(k+1)) cP(i)cQ(k−i)，应明确i<k+1蕴含i≤k，自然差仅在此条件下使用；I_(k+1)总非空，k=0公式单项。
4. 采用next18指定候选长度L=n+m≥2，故意容许最后一个零，避免入口引入n+m−1的自然差；全系数公式及规范化保证任何更长合法候选相同。最短长度仅作后续诊断，不作定义先修。
5. 所需支撑界仅为k≥n+m时：若i<n且k−i<m，则i+(k−i)<n+m与k≥n+m矛盾；否则至少一个补零系数为0。各项零由SUM3，不能仅画格点图替代。
6. 代表无关：等价输入记录给相同全部cP,cQ，所以每个d_k由SUM1一致；不同合法候选长度补零相同，经PR3给同一规范对象。不以求值函数相同证明正式相等。
7. 若用移位累加定义乘法，定义多项式前缀和需显式有限递归，不能把仅为Q定义的SUM直接用于多项式；也可直接在共同有限长度上逐系数累加避免新集合值求和接口。
8. 采用常数项分解Q=C(a)+ST，并按Q可表示的正记录长度归纳求值保乘；尾记录规范化后可能缩短或变零，归纳性质必须是可由该长度表示，而非规范长度恰好。单项记录单独取T=0，不规范化空记录。
9. 交换律从反向前缀恒等式sum_(i=0)^k f(i)=sum_(j=0)^k f(k−j)及有理乘法交换证明。反向求和若前文未证，必须新增有限归纳证明；不能宣称一般重排已可用。
10. 先由卷积单步索引证明(SP)Q=S(PQ)，再由交换得P(SQ)=S(PQ)；不能把S解释成乘X而偷用待证结合律。结合按第三因子的原记录长度及R=C(a)+ST归纳，两边由已证分配、标量与移位化为a(PQ)+S((PQ)T)和a(PQ)+S(P(QT))，再用归纳假设。无需双重/三角换序，也不用求值反推相等。
11. 次数：P,Q非零，令d,e为已定义最高指标；超过d+e所有卷积项零，在d+e处只有i=d可能非零，故系数=cP(d)cQ(e)≠0。需逐项分i<d、i=d、i>d，用有理零乘积判据证明非零与次数相加。
12. 任一输入为零时先得乘积为零，不写deg0。不要套用natDegree乘积恒等式消除零分支；库natDegree(0)=0会令任意非零Q的此类无条件等式失败。
13. 保持范围边界：没有本批证明就不宣布完整环公理、向量空间/模、根数上界、因式定理、多项式除法、插值、多项式函数反向识别。所有拟新增锚与题答须等实际正文再登记。

## 待办

已与下一批方案对齐：n+m卷积、单步移位、一维倒序及常数项分解长度归纳。实际正文与题答已登记，后续独立审阅和构建视觉验收仍按当前哈希另记。不得以该来源预研授予任何完成状态。

实际接口已与正式四稿逐锚及逐SHA核对。已登记B2.15/B2.16，主97H20、第528章，12E05仅交叉；37单元、296基础题加绪论14题共310题。图数15待构建单独核，不由台账推断。本来源记录不授予完成状态。

## 实际稿接口

B2.15：`manuscript/foundations/polynomial_multiplication.md` / `manuscript/foundations/polynomial_multiplication_answers.md`；正文锚`polymul-unit`；各8对题答。

命题：PM1 `polymul-shift`（移位系数、线性及常数项分解）；PM2 `polymul-reversal`（一维有限倒序与自然差指标恒等式）；PM3 `polymul-definition`（有限卷积乘法存在、全指标公式及表示无关）；PM4 `polymul-laws`（常量、零、单位、分配、数乘与交换）；PM5 `polymul-product-shift`（左右移位与乘法相容）。

精确先修：`polyrec-normalization`, `polyrec-equality`, `polyrec-definition`, `polyops-definition`, `polyops-addition`, `polyops-scalars`, `sum-definition`, `sum-extensionality`, `sum-linearity`, `sum-constant`, `sum-concatenation`, `sum-padding`, `b1-induction`, `ord-predecessor`, `ord-trichotomy`, `ord-addition-order`, `sub-definition`, `polyrec-evaluation`, `pow-addition`, `b1-addition-associative`, `sum-indices`, `ord-partial-order`, `ord-successor-comparison`, `radd-laws`, `rmul-laws`, `rmul-distributive`。

正文SHA-256：`048a6c96c9297cae0a4c2ee3e040a5265640515c31433dd06d615690af0f249d`；答案SHA-256：`4bab95e111a375b72a1b6b66675e447714f3158261790218209f508b46fc6cc1`。

B2.16：`manuscript/foundations/polynomial_product_structure.md` / `manuscript/foundations/polynomial_product_structure_answers.md`；正文锚`polyprod-unit`；各8对题答。

命题：PL1 `polyprod-associativity`（按原记录可表示长度证明乘法结合）；PL2 `polyprod-evaluation`（移位求值及求值保持乘积）；PL3 `polyprod-degree`（最高系数、非零积次数及零积消去推论）；PL4 `polyprod-factorization-entry`（形式符号与常量的运算相容及平方差）。

精确先修：`b1-induction`, `ord-predecessor`, `ord-partial-order`, `ord-successor-comparison`, `ord-trichotomy`, `ord-addition-order`, `sub-definition`, `polyrec-normalization`, `polyrec-equality`, `polyrec-degree`, `polyrec-evaluation`, `polyrec-special-values`, `polyops-addition`, `polyops-subtraction`, `polyops-scalars`, `polyops-evaluation`, `polymul-shift`, `polymul-definition`, `polymul-laws`, `polymul-product-shift`, `sum-extensionality`, `sum-linearity`, `sum-constant`, `sum-concatenation`, `sum-padding`, `pow-definition`, `pow-zero`, `rmul-distributive`, `rmul-zero-product`, `polyops-definition`, `radd-laws`, `radd-opposite`, `radd-cancellation`, `rmul-laws`, `rmul-signs`。

正文SHA-256：`8dce7a9623ccac953c71113623156c6e0faca5abf82900fdfe3a6f6413e115b8`；答案SHA-256：`2342e21afec69515c80f6b8b5063ce0f404efbd8de1c991767fd6be4bbe1c1c2`。

临时副本台账已通过：37单元、296基础题+绪论14题=310题、43模块无环、5章28叶部分草稿、0部分完成、push未到期。旧35规格及正式生产JSON不变，12E05仍未写。验证结果及四稿哈希见JSON的`temporary_ledger_validation`。

正式接口续核：110处引用锚点与当前文件SHA一致。主实现诊断报告`research/production/rational_polynomial_product_validation.json`状态passed，绑定当前五份API/依赖文件；{"records": 84, "pairs": 7056, "evaluations": 35280, "padding": 21168, "scalings": 21168, "triples": 1728, "rejections": 33, "immutability": 84}。独立SymPy QQ核对属于有限实现诊断，不代替一般证明；输入范围、时刻、报告及依赖SHA详见JSON的`implementation_diagnostics`。原网络请求时间保持不变，本次安装未新增fetch。

正式安装后的临时台账再次通过上述37单元/310题/43无环模块/5章28叶部分草稿/0部分完成检查；对照17批提交，原35规格及CH01不变，正式生产JSON未写。详情见JSON的`formal_install_temporary_ledger_check`。
