# 一次除式、不同有理根与恒等识别：公开来源审计 {#poly-linear-division-sources}

状态：来源条件已核，B2.17/B2.18正式四稿接口已逐锚及逐哈希登记。独立数学教学审阅、构建视觉和根最终QA另记；章节、分类叶和模块保持部分草稿。

## 实际访问、固定版本与许可

复用4条已核mathlib缓存；新增9次HTTP均200，另有1次公开git HEAD只读解析。OpenStax College Algebra书库HEAD实际返回463991614337632b0e02cbb6c76223cbb0d423d3，随后所有下载均固定该commit。请求UTC时间、字节数、SHA与缓存路径保留原记录；本次正式登记仅本地复读，新增fetch为0。

College Algebra 2e主编写者Jay Abramson，其他贡献作者见JSON；CC-BY-NC-SA-4.0由collection、preface与LICENSE核实。mathlib固定v4.24.0，多项式文件署名Chris Hughes、Johannes Hölzl、Kim Morrison、Jens Wagemaker，Roots另署Johan Commelin；Apache-2.0。只核事实、条件与算法，不复制外部题目、段落、图片或实现。未编译Lean，未形式化书稿。

原请求标签不代替标题：openstax_college_division对应m51276图像章节；openstax_college_zeros对应m51277除法；openstax_college_zero_theorems对应m51278零点定理。

## 固定位置与条件

- [The Division Algorithm (m51277)](https://github.com/openstax/osbooks-college-algebra-bundle/blob/463991614337632b0e02cbb6c76223cbb0d423d3/modules/m51277/index.cnxml#L378)，lines 378–435。条件：非零除数；该框先限定除数次数不大于被除式次数；余式为零或次数更低。 本书对照：只用作唯一商余的教材对照。本书专取X−C(a)，并独立覆盖零及常量被除式，不能借该框省略低次数输入或引入一般除法。
- [Synthetic division scope (m51277)](https://github.com/openstax/osbooks-college-algebra-bundle/blob/463991614337632b0e02cbb6c76223cbb0d423d3/modules/m51277/index.cnxml#L705)，lines 705–705。条件：首项系数为1的线性因子。 本书对照：本批综合除法限X−C(a)，a∈Q；非首一线性或高次除数不在本算法接口中。
- [Synthetic Division / steps (m51277)](https://github.com/openstax/osbooks-college-algebra-bundle/blob/463991614337632b0e02cbb6c76223cbb0d423d3/modules/m51277/index.cnxml#L757)，lines 757–801。条件：源说明x−k且k为实数，高到低处理系数。 本书对照：本书限有理a，升序系数记录必须倒序读取。缺次项须补零；除X−a使用a，除X+a使用−a。末格余数，其余为商的降序系数，输出须转回升序并规范化。
- [Remainder theorem (m51278)](https://github.com/openstax/osbooks-college-algebra-bundle/blob/463991614337632b0e02cbb6c76223cbb0d423d3/modules/m51278/index.cnxml#L101)，lines 101–200。条件：线性首一除数x−k；余式常量。 本书对照：代入a得到r=E_P(a)，使用已证求值保加乘与E_(X−C(a))(a)=0。书稿须区分数值r与常量多项式C(r)，且不使用一般除法存在作为未证前提。
- [Factor theorem and adjacent complex-root claim (m51278)](https://github.com/openstax/osbooks-college-algebra-bundle/blob/463991614337632b0e02cbb6c76223cbb0d423d3/modules/m51278/index.cnxml#L356)，lines 356–438。条件：x−k整除f当且仅当k是根；相邻文字另谈复数系统中n个根。 本书对照：本批仅a∈Q的因式/根等价。相邻复数n根的陈述不能移到Q，也不能解释为n个不同根；不据此宣称有理多项式必裂。
- [Fundamental theorem boundary (m51278)](https://github.com/openstax/osbooks-college-algebra-bundle/blob/463991614337632b0e02cbb6c76223cbb0d423d3/modules/m51278/index.cnxml#L1307)，lines 1307–1362。条件：源正式框n>0、复数根；随后n根明确允许重数。 本书对照：仅作排除范围核查：本批不采用代数基本定理、不引复数或实根存在定理；本批根数界统计不同有理根。
- [Multiplicity discussion (m51276)](https://github.com/openstax/osbooks-college-algebra-bundle/blob/463991614337632b0e02cbb6c76223cbb0d423d3/modules/m51276/index.cnxml#L950)，lines 950–989。条件：图像章节讨论因子重复与零点重数。 本书对照：原请求标签division实际为Graphs of Polynomial Functions。此处只核重数与不同根的差别；图像与触轴/穿轴叙述不引入当前书稿。
- [divModByMonicAux](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Div.lean#L82)，lines 82–108。条件：[Ring R]；首一除数，度数递降的良基递归；使用WithBot degree。 本书对照：库建一般首一多项式除法，强于本批线性范围；本书以原记录正长度归纳独立构造，不把度数递归或一般除法作为先修。
- [divByMonic / modByMonic](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Div.lean#L111)，lines 111–120。条件：[Ring R]；源有非首一输入的缺省定义。 本书对照：本书只定义固定D_a=X−C(a)的商余，不借库总化接口扩展到任意非首一除数。
- [modByMonic_add_div](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Div.lean#L239)，lines 239–240。条件：[Ring R]、Monic q。 本书对照：核余式+除数×商=被除式的方向；本书写P=D_a Q+C(r)，可由既有加法交换调整。
- [div_modByMonic_unique](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Div.lean#L318)，lines 318–336。条件：[Ring R]、Monic g，r+gq=f且degree r<degree g。 本书对照：首一除法唯一性不需要一般域。本书用先代入a得余数唯一、再D_a非零消去得商唯一；不以零余式的未定义次数处理边界。
- [coeff_divByMonic_X_sub_C_rec](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Div.lean#L420)，lines 420–428。条件：[Ring R]，q_n=p_(n+1)+a q_(n+1)。 本书对照：核综合除法递推的正号和下标。书稿须另给有限终端、常量/零输入与记录方向，不能把无限递推关系当唯一算法定义。
- [coeff_divByMonic_X_sub_C](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Div.lean#L430)，lines 430–438。条件：[Ring R]；有限区间Icc(n+1,natDegree p)。 本书对照：库闭式包含条件自然差和natDegree约定；本书不需复制此求和闭式，可用高到低有限递推，避免额外重排和零次数混用。
- [modByMonic_X_sub_C_eq_C_eval](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Div.lean#L549)，lines 549–567。条件：[CommRing R]；余式为C(p.eval a)。 本书对照：书稿Q满足数值交换规则，但必须从已经独立构造的线性商余式推导余式定理；不能循环用余式定理证明商余存在。
- [mul_divByMonic_eq_iff_isRoot / dvd_iff_isRoot](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Div.lean#L569)，lines 569–585。条件：[CommRing R]；a属于系数环，因式在同一多项式类型。 本书对照：本批a∈Q且商也为Q系数多项式。定义D_a整除P为存在Q使P=D_aQ后再证根等价；P=0时每个a是根，D_a整除0，商为0。
- [General polynomial division boundary](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/FieldDivision.lean#L282)，lines 282–304。条件：[Field R]，使用首项系数逆元构造一般除法。 本书对照：该源仅划界：线性首一除法不需要这一完整除法结构；本批不登记一般多项式长除法或欧几里得域。
- [degree / natDegree zero conventions](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Degree/Definitions.lean#L44)，lines 44–53。条件：degree(0)=bottom；natDegree(0)=0。 本书对照：本书零次数未定义。零被除式、零商、零余式和零差多项式都须单独分支，不移植库的零次数公式。
- [degree_mul](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Degree/Operations.lean#L666)，lines 666–674。条件：[Semiring R] [NoZeroDivisors R]；WithBot degree。 本书对照：本书已证非零积次数，D_a=(-a,1)非零次数1。P=D_aQ且P非零时先得Q非零，再得degP=1+degQ；自然差d−1只在d≥1后使用。
- [roots / roots_zero / card_roots](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Roots.lean#L43)，lines 43–77。条件：[CommRing R] [IsDomain R]；roots为含重数的多重集，0特设空多重集；degree界须P≠0。 本书对照：不能把roots(0)=空误读为零多项式没有根。书稿定义的求值零点对零多项式是所有Q；非零根数定理仅论互异有理输入列表。
- [mem_roots / mem_roots'](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Roots.lean#L100)，lines 100–108。条件：roots成员与IsRoot等价须P≠0；一般版本显式含P≠0。 本书对照：库的roots数据结构与求值根谓词有零边界差异；本书无需构造含重数根多重集。
- [card_le_degree_of_subset_roots / finite_setOf_isRoot](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Roots.lean#L122)，lines 122–131。条件：整环；有限集合界通过多重集根建立，非零才有有限根集。 本书对照：本书用互异列表归纳证d次非零多项式不可能有d+1个不同有理根，避免引入未教集合基数或多重集。
- [eq_of_infinite_eval_eq](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Roots.lean#L140)，lines 140–144。条件：整环；取值相等的输入集合无限。 本书对照：本书可用有限整数网格证明Q上的全输入取值相同推出正式相等，不借无限集合基数论。
- [zero_of_eval_zero / funext](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Roots.lean#L377)，lines 377–388。条件：[CommRing R] [IsDomain R] [Infinite R]。 本书对照：不能删掉无限性后推广到任意有限系数域或只给有限样本；本书标准求值函数均为Q→Q，使用自然数嵌入提供任意长互异列表。
- [eq_zero_of_natDegree_lt_card_of_eval_eq_zero](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Roots.lean#L592)，lines 592–615。条件：整环；有限索引、输入映射单射、所有输入取值0、样本数大于natDegree。 本书对照：这是有限网格路线的库对照。本书只用d+1个显式互异有理整数，按根数界得矛盾；无需调用该库的Fintype或基数结论。

## 独立证明与范围核对

1. 范围固定P∈有理系数规范多项式，a∈Q。定义D_a=X−C(a)=(-a,1)，由1≠0直接为二项规范记录，所以D_a≠0且deg D_a=1，a=0也成立。商为正式多项式Q，余数为有理数r；恒等式中余项写C(r)。
2. 存在性按P可由n+1项原记录表示作归纳。单项P=C(b)：取Q=0,r=b。长记录P=C(b)+S(T)，尾部原记录非空，T规范化后可能为0，但仍由较短原长度表示；归纳假设必须按可表示长度而非规范长度恰好。
3. 设T=D_a Q+C(r)。用XQ=S(Q)、乘法结合交换分配和XC(r)=D_a C(r)+C(ar)，逐步推P=D_a(S(Q)+C(r))+C(b+ar)。后继输出商S(Q)+C(r)，余数b+ar。不得以余式定理或一般除法存在为此步骤前提。
4. 对任何合法分解P=D_aQ+C(r)，在a求值，已证求值保加乘给E_P(a)=0·E_Q(a)+r=r。两分解先得r=r′，多项式加法消去得D_aQ=D_aQ′，D_a非零乘法消去给Q=Q′。存在和唯一合起来使尾零表示或算法路径无关。
5. PD实际算法采用固定状态(j,Q,r)而非将无限系数递推当定义。原记录(p_0,…,p_d)的初状态(0,0,p_d)，仅在j<d时读取p_(d−(j+1))并同时用旧状态更新Q′=S(Q)+C(r)、r′=p_(d−(j+1))+ar、j′=j+1；j≥d时保持。自然差条件、状态闭包、固定递归原则与d次终止在polydiv-synthetic逐项说明。
6. PD4将第j步绑定非空后缀P_j=N(p_(d−j),…,p_d)，用商余更新恒等式归纳证明P_j=D_aQ_j+C(r_j)。j=d后缀为原输入，PD3唯一性给任意尾零表示同一输出；不要求中间状态或步数相同。
7. 综合除法要保留中间缺次零，也允许原记录末尾有零；规范商不能删除开头/中间零，只有尾零可删。全零长输入返回商0、余0；a=0时余p_0、商去常数项后规范化，单项时商0。有限程序结果不能替代一般商余证明。
8. 定义a是P的有理根为E_P(a)=0；定义D_a为因式/整除为存在Q使P=D_aQ。因式⇒根用求值保乘；根⇒因式由余式唯一r=E_P(a)=0。P=0时所有有理a都是根和线性因式的参数，但不写deg0。
9. 根数定理仅说非零、次数d的P不可能在长度d+1的两两不同有理列表上全为0。d=0是非零常量，任意输入求值非零。d≥1且给定互异根列表时取第一项a，由因式定理P=D_aQ；P≠0先迫使Q≠0，次数公式再得d=1+degQ。
10. 其余根b满足b≠a，故b−a≠0。由0=E_P(b)=(b−a)E_Q(b)及有理零积判据得E_Q(b)=0；删去首项的列表仍互异，以degQ=d−1的归纳假设矛盾。不得把同一根反复列入当作额外不同根。
11. 自然数→整数嵌入iota和整数→有理嵌入j已分别单射，定义eta=j∘iota。eta(0),…,eta(d)在Q中互异；逐项理由是eta(i)=eta(k)⇒i=k，不需先证明一般无限集合的基数性质。
12. 标准求值函数E_P,E_Q都声明Q为域与目标。正式P=Q推出E_P=E_Q已在PR5建立。反向若函数相等而H=P−Q非零，置d=degH；对上述d+1个互异有理整数，求值保差给E_H=0，违背根数界，故H=0并由加法消去得P=Q。
13. RT3正式使用共同系数上界M：两对象在所有i>M处系数零，故允许任一或两者为零；若差H非零，其次数h≤M，而M+1个互异同值点变成H的不同根，违反RT2。不是无条件的有限采样判等。
14. RT4实际精确引用pow-compatibility中已建立的eta:N→Q单射及fc-equality函数三数据相等，不重新采用无限基数公理。RT答案7已把列表比较指标改为k,l以避免与整数到有理嵌入j重名；绑定的是修订后的正式答案哈希。
15. 反向识别不表示任意给定有限样本总能识别任意次数多项式；已知次数上界d时d+1个互异点才足够。若不声明次数上界，早先有限样本不足的反例仍成立。不得在根数定理建立前用求值反向证明乘法或除法的形式恒等式。
16. 本批不推断每个非恒定Q多项式有有理根，不推断有d个不同根或在Q完全分裂。重数、复根存在、实根连续性/介值定理、一般多项式除法、任意系数域扩展与插值构造均另需证明。

## 实际稿接口

B2.17：`manuscript/foundations/polynomial_linear_division.md` / `manuscript/foundations/polynomial_linear_division_answers.md`；主锚`polydiv-unit`；各8对题答。

命题：PD1 `polydiv-linear-divisor`（一次除式的非零性、次数与求值）；PD2 `polydiv-existence`（按原记录长度证明商余存在）；PD3 `polydiv-uniqueness`（余数求值公式与商余唯一性）；PD4 `polydiv-invariant`（综合除法后缀不变式及输出表示无关）。

精确先修：`polyrec-normalization`, `polyrec-equality`, `polyrec-degree`, `polyrec-evaluation`, `polyrec-special-values`, `polyops-addition`, `polyops-subtraction`, `polyops-scalars`, `polyops-evaluation`, `polymul-shift`, `polymul-laws`, `polyprod-associativity`, `polyprod-evaluation`, `polyprod-degree`, `polyprod-zero-cancellation`, `polyprod-factorization-entry`, `b1-induction`, `b1-recursion-principle`, `ord-predecessor`, `ord-successor-comparison`, `ord-cancellation`, `sub-definition`, `fun-pairs`, `ord-trichotomy`, `ord-addition-order`, `radd-laws`, `radd-cancellation`, `rmul-laws`, `rmul-distributive`。

正文SHA：`a1db7bbc2edc3a629570c62421b1152e0c968293596e665991d95e1ffcd107c3`；答案SHA：`5b91e0c85611d38b1b7f7b7a17f30319d5b9dbad4fe98c4bc59b9cf0181dc0eb`。

B2.18：`manuscript/foundations/polynomial_roots_identity.md` / `manuscript/foundations/polynomial_roots_identity_answers.md`；主锚`polyroot-unit`；各8对题答。

命题：RT1 `polyroot-factor`（有理根与一次因式等价）；RT2 `polyroot-bound`（非零多项式的不同有理根次数界）；RT3 `polyroot-finite-identity`（共同系数上界下的有限点判等）；RT4 `polyroot-standard-identity`（标准Q到Q求值函数与形式系数的恒等识别）。

精确先修：`polyrec-definition`, `polyrec-equality`, `polyrec-degree`, `polyrec-evaluation`, `polyrec-special-values`, `polyops-subtraction`, `polyops-evaluation`, `polymul-laws`, `polyprod-evaluation`, `polyprod-degree`, `polyprod-factorization-entry`, `polydiv-linear-divisor`, `polydiv-existence`, `polydiv-uniqueness`, `b1-induction`, `ord-cancellation`, `ord-successor-comparison`, `ord-trichotomy`, `sum-indices`, `pow-compatibility`, `fc-equality`, `radd-cancellation`, `rmul-zero-product`, `rord-laws`, `rord-integers`, `rord-translation`, `rord-negation`, `rord-multiplication`, `radd-laws`, `rmul-laws`, `polyops-definition`。

正文SHA：`d8d3c261a1e82ce8512fc74e8822d6d14bd7d321aa92166efcfb30f3ae6129d8`；答案SHA：`facd01a13eabf07e30881acf897b498e0cfb21f7a6c444ab407f955065de32fa`。

主97H20、第528章、第63部分；12E05仅交叉。39单元、312基础题+绪论14题=326题；43模块、5章28叶部分草稿、0部分完成。图数15保持不增，构建另核。

主实现报告`research/production/rational_polynomial_linear_division_validation.json`已核passed，绑定6份当前API/依赖哈希；计数{"records": 123, "divisions": 615, "padding": 1845, "suffixes": 2190, "nonconstant_degree": 550, "constant_zero": 65, "rejections": 43, "immutability": 123}。SymPy QQ精确诊断不替代一般证明，报告范围与SHA见JSON。

零多项式的每个有理输入都是根，库roots(0)=空多重集只是数据接口约定；本批仅计不同有理根，首一线性参数始终属于Q。标准函数识别使用全Q同域同目标；有限样本另有系数上界及互异性条件。一般多项式除法、重数、实复根存在与有理完全分裂仍未建立。

正式登记后的临时台账实跑通过以上计数与无环检查；原37规格及CH01不变，正式生产JSON未写，push未到期。证据见JSON的`temporary_ledger_validation`，不授予最终验收。
