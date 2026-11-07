# 有理平方、配方与二次方程：公开来源审计 {#rational-quadratic-sources}

状态：来源条件与正式两单元接口已核。B2.19/SQ与B2.20/QC主97H30、第528章，97H20仅交叉；独立审阅、构建视觉与最终验收各自绑定，不据登记授予完整章节状态。

## 固定来源与实际访问

复用4条200缓存；20批新增7次HTTP均200、无HTTP失败，无新git请求。OpenStax沿用19批已解析的固定commit463991614337632b0e02cbb6c76223cbb0d423d3；mathlib固定v4.24.0。原请求UTC、字节数、SHA与本地缓存路径逐条保留，未把复读时间当新fetch。

OpenStax College Algebra 2e主编写者Jay Abramson，其他贡献作者见已核preface；CC-BY-NC-SA-4.0由collection、preface、LICENSE交叉确认。mathlib各文件作者见JSON，Apache-2.0。只核条件与事实，不复制外部题目、段落、图像或实现；未编译Lean，未形式化书稿。

请求标签openstax_college_quadratics实际是m51255 Complex Numbers，保留为发现记录；m51256 Quadratic Equations才提供本批教材核查内容。

## 必须保留的条件差异

OpenStax判别式表的实系数上下文没有给出有理性分类所需的额外有理系数条件。本书全部参数与未知量属于Q，正判别式只在它是Q中的平方时给两个有理解；正而非Q平方仍无Q解。该来源表不能作为无条件实系数有理性定理引用。

mathlib的Rat.sqrt是全域可计算有理函数，是否真为平方根要再检验平方等于原数。本书sqrt_Q仅定义在确有非负有理平方根的S_Q上；不把库函数总化约定转成每个非负有理数都能开方。

## 逐条定位

- [m51255 title discovery](https://github.com/openstax/osbooks-college-algebra-bundle/blob/463991614337632b0e02cbb6c76223cbb0d423d3/modules/m51255/index.cnxml#L3)，lines 3–3。条件：实际标题Complex Numbers，原请求标签quadratics不是标题。 本书边界：仅保留发现记录；复数、负数开方及复平面不作为本批采用对象或先修。
- [Zero product / quadratic standard form](https://github.com/openstax/osbooks-college-algebra-bundle/blob/463991614337632b0e02cbb6c76223cbb0d423d3/modules/m51256/index.cnxml#L378)，lines 378–402。条件：来源a,b,c为实数，a≠0时才称标准二次方程。 本书边界：本书将全部参数和未知量限制Q；a=0必须先按一次/常量/恒零分支，不能把除以a的公式延伸到此。
- [Square root property](https://github.com/openstax/osbooks-college-algebra-bundle/blob/463991614337632b0e02cbb6c76223cbb0d423d3/modules/m51256/index.cnxml#L1397)，lines 1397–1480。条件：来源使用±√k，声明k为非零实数，且整书已有复数背景。 本书边界：不能据此定义任意有理q的平方根。本书先分负、零、正有理平方、正非平方，并只在S_Q上定义唯一非负sqrt_Q；零时两符号代表同一解。
- [Completing the square](https://github.com/openstax/osbooks-college-algebra-bundle/blob/463991614337632b0e02cbb6c76223cbb0d423d3/modules/m51256/index.cnxml#L1725)，lines 1725–1810。条件：先把非零首项系数化成1，再添半线性系数的平方。 本书边界：本书逐步核a≠0、2a≠0、4a≠0后证明恒等式；常量项变动、等式两侧同时变动和双向变形不可省略。
- [Derivation of quadratic formula](https://github.com/openstax/osbooks-college-algebra-bundle/blob/463991614337632b0e02cbb6c76223cbb0d423d3/modules/m51256/index.cnxml#L2327)，lines 2327–2380。条件：来源可先把a变正；使用实数公式环境。 本书边界：本书直接保留任意非零有理a并证明可逆仿射变换；无需a>0，负a时两根的大小排序会交换。
- [Quadratic formula](https://github.com/openstax/osbooks-college-algebra-bundle/blob/463991614337632b0e02cbb6c76223cbb0d423d3/modules/m51256/index.cnxml#L2622)，lines 2622–2680。条件：源框a,b,c∈R且a≠0，公式含未在本书定义的实/复根式。 本书边界：本书只在已给同域s∈Q且s²=Δ时写(-b±s)/(2a)，或在Δ∈S_Q时使用sqrt_Q(Δ)。不宣称正判别式自动有Q解。
- [Discriminant table: missing rational-coefficient qualification](https://github.com/openstax/osbooks-college-algebra-bundle/blob/463991614337632b0e02cbb6c76223cbb0d423d3/modules/m51256/index.cnxml#L2960)，lines 2960–3062。条件：相邻段落声明实系数，表却把Δ=0列作一个有理解、正平方列作两个有理解、正非平方列作两个无理解。 本书边界：这组有理/无理分类需要额外有理系数前提，不能从任意实系数直接推出。本书明确a,b,c∈Q，且平方指Q中存在平方见证；只报告Q中0/1/2解，不借此表宣告实根存在。
- [abs_mul_abs_self / sq_abs / abs_sq](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Order/Ring/Abs.lean#L65)，lines 65–76。条件：相关节Ring与LinearOrder；abs_sq另在IsOrderedRing条件下。 本书边界：核|x|²=x²及平方非负所用绝对值关系。本书仍用已证有理符号/次序分支证明平方非负；不把整套库顺序实例当作新公理。
- [abs comparison and squares](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Order/Ring/Abs.lean#L83)，lines 83–107。条件：[Ring α] [LinearOrder α] [IsStrictOrderedRing α]；比较的是|a|与|b|。 本书边界：不能把平方说成全Q严格递增。仅在u,v≥0时绝对值等于自身，得到平方的严格比较和单射；本书用(v−u)(v+u)及三歧性独立证明。
- [coprime_pow_left_iff / coprime_pow_right_iff](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Data/Nat/GCD/Basic.lean#L183)，lines 183–193。条件：自然数Coprime；指数n>0。 本书边界：取指数2可核互素平方仍互素。书稿直接在整数gcd上两用既有C4并用对称，不引素数分解，也不把自然gcd与整数符号约定混为同一接口。
- [Rat.mul_self_num / Rat.mul_self_den](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Data/Rat/Lemmas.lean#L151)，lines 151–157。条件：q为已规范化Rat，num整数、den正自然数，q.reduced记录互素。 本书边界：平方后规范分子、分母分别平方，证明明确使用互素乘积而无需素因子分解；本书以(p²,q²)正分母且互素，再用R5唯一性得到相同结论。
- [Rat.isSquare_iff](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Data/Rat/Lemmas.lean#L167)，lines 167–174。条件：IsSquare q当且仅当规范整数num与自然数den分别IsSquare。 本书边界：对应本书唯一规范代表(m,n)：存在u≥0、v>0使m=u²,n=v²。必须是规范代表；8/18本身分子分母非平方但等于4/9，不可对任意未约分记录套必要性。
- [isSquare_natCast_iff / isSquare_intCast_iff](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Data/Rat/Lemmas.lean#L176)，lines 176–182。条件：自然数或整数嵌入Q之后成为平方，当且仅当原整数体系内是平方。 本书边界：支持用整数平方间隙排除Q中的2与1/2；本书仍写0、1、≥2离散分支，不用2素数或未定义的实数√2作为理由。
- [num/den of coprime fractions / div_int_inj](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Data/Rat/Lemmas.lean#L244)，lines 244–260。条件：正整数分母及分子分母绝对值的自然互素；两份规范分数相等推出分量相等。 本书边界：本书R5已证同一有理数唯一正分母互素代表，平方判据可以使用该接口，不能把两任意分数相等误作各分量相等。
- [Rat.sqrt / sqrt_eq / exists_mul_self](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Data/Rat/Sqrt.lean#L22)，lines 22–38。条件：Rat.sqrt是以整数/自然数sqrt计算而得到的全域有理函数；是否真平方根需验证sqrt(x)²=x。 本书边界：它不等于本书只在S_Q上定义的sqrt_Q。库exists_mul_self显式加回平方校验；绝不能据函数名认为每个非负有理数都可在Q开方。未调用此库函数作为书稿证明。
- [discrim / discrim_eq_sq_of_quadratic_eq_zero](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/QuadraticDiscriminant.lean#L43)，lines 43–55。条件：discrim定义只需Ring；根推出Δ=(2ax+b)²需CommRing，无需先给平方根。 本书边界：本书先证明除法自由恒等式(2at+b)²−Δ=4aF(t)。由根产生同域平方见证是必要方向，不依赖预设Δ可开方。
- [quadratic_eq_zero_iff_discrim_eq_sq](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/QuadraticDiscriminant.lean#L59)，lines 59–66。条件：[CommRing R] [NeZero (2:R)] [NoZeroDivisors R]且a≠0。 本书边界：反向从平方等式回到原方程，需要4a非零并消去；本书Q的2≠0与零积法则须具体引用，不能漏掉a=0退化或特征2边界。
- [quadratic_ne_zero_of_discrim_ne_sq](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/QuadraticDiscriminant.lean#L68)，lines 68–71。条件：CommRing，假设对同一个R中每个s均Δ≠s²。 本书边界：无同域平方根则无同域方程根。本书Δ>0且Δ不属于S_Q也归无Q解；“正”不是有理解充分条件。
- [quadratic_eq_zero_iff](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/QuadraticDiscriminant.lean#L75)，lines 75–84。条件：[Field K] [NeZero (2:K)]，a≠0，明确s∈K且Δ=s*s。 本书边界：公式的根式实际是已存在的同域元素s。取K=Q恰符合本批条件；两候选可穷尽所有Q解，不以只代回候选替代逆向证明。
- [exists_quadratic_eq_zero / zero discriminant](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/QuadraticDiscriminant.lean#L86)，lines 86–98。条件：同Field/2非零条件；存在s使Δ=s²，或Δ=0。 本书边界：Δ=0时唯一候选−b/(2a)；正平方时有两候选，但其不同仍须由s>0、2a≠0证明。不能把零判别式叫两个不同解。
- [discrim_eq_zero_iff uniqueness](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/QuadraticDiscriminant.lean#L100)，lines 100–111。条件：同Field/2非零，a≠0。 本书边界：唯一同域解恰对应零判别式；本书完整分类还必须独立涵盖a=0的全Q解/无解/唯一线性解。
- [Global nonnegativity theorem boundary](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/QuadraticDiscriminant.lean#L115)，lines 115–137。条件：有序域定理discrim_le_zero证明调用Filter趋向无穷等工具。 本书边界：仅核排除范围：本书QC4不引用该更强证明链，只由F(t)=a(t−h)²+κ、平方非负及a符号推出Q上的界；h∈Q确保取得界，不需极限、连续性或完备性。

## 独立证明义务

1. 平方x²沿用POW1/有理乘法定义，不引新的幂对象。按x<0、x=0、x>0证明x²≥0及x²=0⇔x=0；负支使用(−x)²=x²和正负乘法律。
2. 由有理分配逐项证明v²−u²=(v−u)(v+u)。0≤u<v时两因子均正，得u²<v²；反向用三歧性排除相等及反向。全Q平方并非递增，例如−2<−1而4>1。
3. 任意有理x,y满足x²=y²⇔x=y或x=−y，来自平方差和有理零积；零时两支相同。用非负平方单射得非负根至多一个，但唯一性不能冒充存在性。
4. 定义S_Q为存在非负有理s满足s²=q的有理q集合，仅在S_Q上定义sqrt_Q。任意x²在S_Q，因为可选x或−x使其非负；S_Q包含0且包含于非负Q，但不等于所有非负Q。此处集合背景沿用既有按条件取子集及函数三数据约定，不采用实数构造。
5. 平方方程x²=q的四支：q<0无解；q=0仅0；q>0且q∈S_Q时恰为s及−s并证明两者不同；q>0且q不在S_Q无解。每个充分方向代回，每个必要方向用同平方正负两支或非负见证构造。
6. 互素平方小引理只用C4两次及gcd对称：gcd(p,q)=1⇒gcd(p,q²)=1⇒gcd(q²,p)=1⇒gcd(q²,p²)=1⇒gcd(p²,q²)=1；允许p=0，不暗添p,q非零或两份相同q彼此互素。
7. 取z唯一规范记录(m,n)，n>0。若z=s²且s有规范(p,q)，q>0，则乘法代表(p²,q²)正分母且由前条互素，R5唯一性给m=p²,n=q²。令u=|p|≥0,v=q>0并核|p|²=p²。必要性必须借规范唯一而不是直接比较任意代表。
8. 若存在整数u≥0,v>0且m=u²,n=v²，则合法代表[(u,v)]给非负有理s，其平方等于[(m,n)]；无需先证明(u,v)互素。零用(0,1)，负分子不可能为整数平方；8/18须先规范化为4/9。
9. 2不在S_Q：其规范代表(2,1)，若u≥0整数满足u²=2，将其写成自然嵌入；u<2时由离散次序只有0或1，u≥2时平方≥4，均矛盾。1/2同理由规范分母2排除。无需素数、唯一分解、实数平方根或浮点近似。
10. 有理参数a,b,c与未知t明确属于Q。先处理a=0：b≠0唯一−c/b；b=c=0全部Q；b=0且c≠0无解。此支不计算1/a、1/(2a)或1/(4a)，也不把降次后的零多项式赋次数。
11. a≠0时先核2、4在Q为正且2a、4a非零，定义h=−b/(2a)、κ=c−b²/(4a)。逐次分配、结合交换、符号与合法约分证明F(t)=a(t−h)²+κ。若写形式版，明确有理数乘与常量C对象，按既有形式运算独立核。
12. 定义Δ=b²−4ac，逐展开证明(2at+b)²−Δ=4aF(t)。必要方向代F=0；充分方向用4a≠0消去。t↦2at+b在Q上可逆，逆为(y−b)/(2a)，故平方方程解与原方程解一一对应。
13. a≠0时Δ<0无Q解；Δ=0唯一−b/(2a)；Δ>0且Δ∈S_Q时恰为(-b±sqrt_Q(Δ))/(2a)且两根不同；Δ>0非Q平方无Q解。负a允许，不能把“+s”分支固定当较大根。存在判别用Δ的唯一正分母互素记录与SQ4，不用教材实数根分类替代。
14. QC4只论有理定义域：a>0时F(t)≥κ，a<0时F(t)≤κ；等号由a非零和平方零判据恰为t=h。h确为Q中输入，所以界取得，不需连续实抛物线、导数、极限或完备性。
15. 实现按本批方案以整数二分构造integer_sqrt，不引math.isqrt作为额外可信前提。对n≥0采用0≤lo<hi、lo²≤n<hi²不变式（例如初值lo=0、hi=n+1，初值平方界需证明），hi−lo>1时选严格内部整数中点并按mid²≤n或>n更新。证明不变式保持、正整数差hi−lo严格减小，终态hi=lo+1给lo²≤n<(lo+1)²；仅lo²=n时判为平方。负输入拒绝或在有理平方接口先分支，规范分子分母分别检验。全部有理参数先校验，解集输出区分无解、全部Q与有限解。二分实现的证明与运行诊断由实现附录另记，本来源审计不替代实际运行记录；正式报告位置见后文。

## 采用背景与应证内容

仅沿用先前明确的自然数、集合与函数背景；C4、R5及有理运算/序已是书稿已证接口。SQ1—4、QC1—4已在正式正文逐项展开，独立文本审阅另记。外部源只作条件核对，不额外采用实数根式、素因子分解、极限或完备性。现有C4与R5定位/哈希已核；新稿接口已冻结并列于下文，最终构建与整体验收仍须单独通过。


## 正式稿与配套计算的实际接口

B2.19《有理平方与平方方程》，主锚 `sqrat-unit`，各八题与八份完整解答。

- `manuscript/foundations/rational_square_equations.md`：`8a1edd98b84ee307666dfe8e7c416bea4530e9332b7eed1e1c813c471a7a2598`
- `manuscript/foundations/rational_square_equations_answers.md`：`2b623ea4477353874f910d0867ca3fc9af8f6e92ed5f74e037450c756ae346c2`

SQ1 `sqrat-order`（平方符号与非负平方比较）；SQ2 `sqrat-root-uniqueness`（同平方两支及非负根唯一性）；SQ3 `sqrat-solutions`（有理平方方程完整分类）；SQ4 `sqrat-normal-form-test`（规范代表的有理平方判据）。

B2.20《配方与有理二次方程》，主锚 `quad-unit`，各八题与八份完整解答。

- `manuscript/foundations/rational_quadratic_equations.md`：`b3ce2e17a3c46c2b461091c75a49543dfb2cfb6bc6cc490ea2b8dde6befb3779`
- `manuscript/foundations/rational_quadratic_equations_answers.md`：`d49ee39b39ed6e318c7d345eb71db84171f9ee409e2771f4b58574264a5eeba0`

QC1 `quad-completion`（配方恒等式）；QC2 `quad-discriminant`（可逆判别式平方方程）；QC3 `quad-rational-solutions`（全部有理解与退化分支）；QC4 `quad-bound`（有理输入上的界与唯一等号）。

正式精确实现 `tools/rational_quadratics.py` 与算法说明已保存；二分平方界的不变式、中点严格内部、正整数差下降和零输入终止证明供附录逐项使用。程序报告绑定三份源码，主诊断通过4102个整数界、3059个分数输入、729组参数、35项类型拒绝及8算例；独立API报告另有不同oracle，不把有限程序数据当成全称证明。

新增图只画八个精确有理样本，界符号为κ；普通有理函数域和有限绘图数据分清。当前登记41单元、328基础题加绪论14题共342题、16图，5章28叶仍是部分草稿，43模块保持原先修框架，0顶层部分完成。原39单元规格不变。正式登记只有本地复读，未产生新来源下载。
