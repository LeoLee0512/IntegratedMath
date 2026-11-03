# 多项式记录、加法与缩放：临时来源审计

状态：planned，仅/tmp。本批目标限B2.13规范系数记录/非零次数/求值与B2.14逐系数加法/缩放/求值兼容，未注册正文或台账。来源锚拟poly-basic-sources。

## 原访问字节的复核

本次没有新增网络请求。选用原公开记录14条：13条HTTP 200的保存字节逐一重验SHA-256，另保留Degree/Defs.lean的404发现记录；正确Degree/Definitions.lean随后成功。404原下载器未保存响应正文/异常字符串，不补造原文。逐请求原UTC时间、URL、字节数、哈希详见JSON；原核查时刻为2026-10-29T17:36:24.461240+00:00，本次本地重读时刻单独记为cache_reviewed_at_utc。

两独立来源系列如下；所用模型、范围与许可分别核对。

### POLY-OPENSTAX：Intermediate Algebra 2e

版本：osbooks-prealgebra-bundle commit ad40c7e3c9a909cde81a24c526f52fe26a51fb14。许可：CC-BY-NC-SA-4.0。只核数学条件与术语；原创正文题答不复制外部问题、连续段落或图像。许可不可误写CC BY，图片例外未采用。

作者：Lynn Marecek、Andrea Honeycutt Mathis。

- [m81383，Monomial / Polynomials](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81383/index.cnxml#L51)（modules/m81383/index.cnxml，行51–76）：来源按有限项表达式及非负整数指数介绍多项式；本书另以非空有限系数记录的唯一规范代表定义对象，不把未定义的多项式乘方混入入口。
- [m81383，Degree of a Polynomial](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81383/index.cnxml#L117)（modules/m81383/index.cnxml，行117–124）：来源笼统写常数次数0以及最高项次数，没有在此区分零多项式。书稿只对非零规范记录定义次数，零次数未定义；不能将原文常数措辞直接用于零。
- [m81383，同类项](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81383/index.cnxml#L232)（modules/m81383/index.cnxml，行232–234）：同变量同指数位置的系数相加减；书稿用补零系数公式精确表达，不能删中间零或把记录长度当次数。
- [m81383，多项式加减](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81383/index.cnxml#L337)（modules/m81383/index.cnxml，行337–338）：来源以交换律重排同类项；本书不借未经证明的一般有限重排，而在共同正长度上逐系数定义并用前缀和线性律证明求值兼容。
- [m81383，Polynomial Function](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81383/index.cnxml#L609)（modules/m81383/index.cnxml，行609–615）：多项式可给出求值函数；本书正式对象相等由系数判据决定。正式相等推出Q→Q求值函数相等，反向本批未证，不错误宣称反向为假。
- [m81385，Distributive Property](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81385/index.cnxml#L132)（modules/m81385/index.cnxml，行132–134）：来源一般单项式乘多项式的分配说明，只核常数缩放的代数动机；本批不引入多项式乘法。
- [m81384，Zero Exponent Property](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81384/index.cnxml#L401)（modules/m81384/index.cnxml，行401–412）：来源的零指数限定非零底数；本书已在B2.11明确所有有理底数的离散零次幂为1。因此t=0求值时常数项用0^0=1，由本书定义而非来源扩大条件。

### POLY-MATHLIB：mathlib formal polynomial coefficients, scalar operations, degrees and evaluation

版本：mathlib4 v4.24.0。许可：Apache-2.0。只读源码核验条件，不复制实现，未编译Lean，未把本书形式化；to_additive对应按源注解阅读。

逐文件作者见JSON；多项式文件署名Chris Hughes、Johannes Hölzl、Kim Morrison、Jens Wagemaker。

- [Finsupp结构](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Data/Finsupp/Defs.lean#L84)（Mathlib/Data/Finsupp/Defs.lean，行84–94）：源以函数加有限非零支持记录系数；本书以非空有限记录及规范化表示。两模型数学相容，但不照搬有限支持抽象定义、任意有限集合最大元或库中全部实例作为先修。
- [Polynomial结构](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Basic.lean#L61)（Mathlib/Algebra/Polynomial/Basic.lean，行61–65）：形式多项式包装AddMonoidAlgebra R N，已带Semiring R背景。此结构不直接是R→R求值函数；本书不因引用它而宣布多项式环已构造。
- [coeff / coeff_injective / coeff_inj](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Basic.lean#L569)（Mathlib/Algebra/Polynomial/Basic.lean，行569–582）：系数函数决定形式多项式；书稿用补零函数c_A:N→Q与规范代表唯一证明对应结论。
- [ext_iff / ext](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Basic.lean#L703)（Mathlib/Algebra/Polynomial/Basic.lean，行703–710）：形式相等逐系数判断；不是在有限几个输入处取值相同的判据，也未借此证明任意系数域上的求值函数映射单射。
- [degree / natDegree](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Degree/Definitions.lean#L44)（Mathlib/Algebra/Polynomial/Degree/Definitions.lean，行44–53）：degree采用WithBot N，零为⊥；natDegree则把零另置0。书稿只定义非零多项式次数，不能在零对象处混用两接口。
- [degree_zero / natDegree_zero / degree_eq_bot](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Degree/Definitions.lean#L75)（Mathlib/Algebra/Polynomial/Degree/Definitions.lean，行75–89）：再次核明零次数两接口；本书空非零系数位置集合没有最大者，零不能套非零最大指标定义。
- [degree_C](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Degree/Definitions.lean#L148)（Mathlib/Algebra/Polynomial/Degree/Definitions.lean，行148–149）：非零常数degree为0，声明明确a≠0；对应书稿非零一项记录次数0。
- [coeff_add / coeff_smul](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Coeff.lean#L34)（Mathlib/Algebra/Polynomial/Coeff.lean，行34–46）：加法逐系数；数乘在SMulZeroClass条件下逐系数。书稿专取Q数值缩放，通过有理乘法及零律证明，不借库的模或半环实例给书稿省略论证。
- [support_smul](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Coeff.lean#L48)（Mathlib/Algebra/Polynomial/Coeff.lean，行48–52）：缩放不创造原来为零的位置；非零有理标量保持最高非零系数还需本书零乘积判据，不把包含关系误读为无条件支持相等。
- [eval / eval_eq_sum](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Eval/Defs.lean#L237)（Mathlib/Algebra/Polynomial/Eval/Defs.lean，行237–245）：求值是独立操作，按系数与输入自然幂作有限和；本书用有限记录长度与SUM1/5证明尾零和代表选择无关。
- [eval_C / eval_monomial / eval_zero / eval_add / eval_one](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Eval/Defs.lean#L270)（Mathlib/Algebra/Polynomial/Eval/Defs.lean，行270–300）：常数、零、一及加法求值关系；书稿用既有有理幂、有限和及逐系数式独立证明，不复制库的更强代数结构。
- [eval_C_mul](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Eval/Defs.lean#L302)（Mathlib/Algebra/Polynomial/Eval/Defs.lean，行302–306）：库把常数倍写成常数多项式的乘积，并证明求值可提取常数。本书尚无多项式乘法，仅用逐系数数乘和SUM2证明相同数值事实，不以此条引入乘法对象。
- [smul_eq_C_mul](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Coeff.lean#L317)（Mathlib/Algebra/Polynomial/Coeff.lean，行317–317）：库中数乘与常数多项式乘积相等，是已建乘法后的联系；本书本批只定义前者，不使用后者作为定义或先修。
- [degree_add_le](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Degree/Definitions.lean#L325)（Mathlib/Algebra/Polynomial/Degree/Definitions.lean，行325–335）：库在含底元素的次数类型上无条件给上界；本书零次数未定义，先分P=0、Q=0、P+Q=0，再在有定义范围写最大次数上界。
- [prod_range_succ / eventually_constant_prod / prod_range_add，@[to_additive]](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/BigOperators/Group/Finset/Basic.lean#L522)（Mathlib/Algebra/BigOperators/Group/Finset/Basic.lean，行522–552）：有限前缀后继、零尾稳定与拼接的加法对应供复核；本书实际先修是已写SUM1—5，不调用一般双索引重排。

## 自有模型与必要证明

1. 原记录(A,n)要求n≥1，A:I_n→Q，I_n={i∈N:i<n}。补零系数c_A(i)在i<n取A(i)，在i≥n取0，分支覆盖并互斥。函数三数据仍保存声明域/目标；原记录(1,2)与(1,2,0)长度不同，不能作为原记录强行说相等。
2. 全体有限有理记录组成集合是公开采用的背景；规范记录可从该集合按条件选取。各个固定长度记录的可构造性不能冒充全体记录集合已从前文集合公理证明。采用唯一规范代表模型，不另引入商集。
3. A~B定义为∀i∈N,c_A(i)=c_B(i)。反身、对称、传递逐位置证。令L=max(n,m)（只比较两个自然数），i<L时核对应项，i≥L时两侧0；严格覆盖i=L，不能写成仅i>L。较短者补L−n个零只在n≤L下使用自然差。
4. 对非空记录长度从1开始归纳，证明它或全零，或有唯一最大非零指标。后继末项非零则取新末指标；末项零且前缀非零沿用归纳指标；全零前缀加零仍全零。不得无依据取任意非空集合最大元；若辅助证明允许0长度，明确那不是合法原多项式记录。
5. norm(A)：全零返回(0)，否则截到最大非零指标d。逐位置证明补零系数不变。两个规范记录等价时先分零；非零且末指标不同，在较大指标处一侧非零另一侧补零矛盾；所以长度相同，所有项相同。由此A~B iff norm(A)=norm(B)，并得规范化幂等。
6. 正式多项式就是规范记录P。P=Q iff全部补零系数相同。零为(0)，常数a为(a)；非零常数次数0，非零P的次数为末非零指标，零次数不定义。中间或开头的零保留位置，不可像尾零一样删掉。
7. E_A(t)=Σ_(i∈I_n) c_A(i)t^i，t∈Q，所有幂与有限和已定义。补零只添0·t^i，SUM5保持值；任意等价记录先补同一正长度，再由SUM1得逐点值同。因此E_P:Q→Q合法且与原始表示无关；不用选择或根数界。
8. t=0时第0项为c_P(0)·0^0=c_P(0)，所有正指数项为0；用SUM4把首项与尾段分开，再用零和公式。t=1时每个1^i=1，得系数总和。P是记录，c_P(i)是第i系数，E_P(t)是输入处取值，三者不同；常数系数记号不可混为未定义的多项式函数值。
9. 正式相等推出标准求值函数相等（同域同目标Q）。全Q上的反向识别实际上成立，但本批不证明，不能谎称不同Q系数多项式可能在全Q处处同值；有限样本相同则用明确反例说明不足，不借非零多项式根数上界。
10. B2.14共同长度L≥max(n,m)，所以L≥1；数乘也取L≥原正长度。若仅要求非零系数指标<L，两零对象会允许L=0，生成非法空记录。先逐项形成候选再规范化，分别核i<L和i≥L的系数公式。
11. 不同共同正长度、不同尾零表示给出的加法/数乘候选逐补零系数相同，规范唯一保证同一正式结果。证明c_(P+Q)(i)=c_P(i)+c_Q(i)、c_(λP)(i)=λc_P(i)覆盖全部i；定义−P=(-1)P、P−Q=P+(−Q)。
12. 加法交换/结合/零/唯一相反数、标量1/0与复合和两分配，逐个系数化为Q规律再用正式相等判据。三多项式加法结合时可先取统一正长度，也可直接用已证全部系数公式，不能仅写因函数值相同而正式相等。
13. 求值保加、数乘、差只需共同正长度、SUM2与有理分配结合；先证明未经规范化的候选值，再用B2.13求值代表无关转回正式多项式。不涉及双重索引，也不构造多项式乘法。
14. 次数分支：先分P、Q和P+Q是否零。非零输入及非零和才写deg(P+Q)≤max(degP,degQ)；异次数时较高位不会抵消，所以和非零且度数等于较大者。同次数最高系数抵消后可能为零或降次，二者分开；非零λ与非零P时最高系数乘积非零，度数保持。λ=0或P=0归零，不计算deg0。
15. 本批形式X可定义为(0,1)，但X^i在多项式乘法尚未定义时只能是明确说明的记录记号，最好延后。数值t^i已合法。不得声称建立多项式环、一般向量空间、乘法卷积、因式定理、根数上界、二项式定理或多项式函数反向识别定理。

## 计划接口与先修

B2.13：polyrec-unit / polyrec-answers，PR1—6按尾零等价、最大非零指标、规范唯一、系数相等、求值良定义、零/一输入依次登记计划锚；定义为polyrec-records/definition/degree。8题前缀polyrec-q/a。正文文件名待作者确认，所有新锚标planned。

B2.14：polyops-unit / polyops-answers，PO1定义及良定义、PO2加法律与相反数、PO3标量规律、PO4求值兼容、PO5非零次数分支；减法另有polyops-subtraction。8题前缀polyops-q/a。现存先修逐锚与文件哈希已核，B2.14对B2.13的锚只是前向计划，不假报已存在。

主97H20第528章，12E05仅交叉。继续放在functions模块内部，不增无必要模块，不赋予12E05主覆盖或多项式环完成度。若两单元以后实际完成，预期35单元、280基础题加绪论14题共294题；5章28末级草稿、43模块、0部分完成、push未到期。当前正式台账不变。

有限精确诊断全部通过：{"normalization": 120, "tail_evaluation": 600, "equality_criterion": 14400, "addition_evaluation": 72000, "scaling_evaluation": 2400, "degree_cases": 14880}。输入为全部120个长度1至4、系数−1/0/1非空记录；五个有理取值和四个有理标量。诊断只核临时模型边界和公式，不代替证明，也不替作者或构建作验收。

原请求标签不代替标题：openstax_powers实际为m81383 Add and Subtract Polynomials；openstax_products实际为m81384 Properties of Exponents and Scientific Notation；openstax_multiply为m81385 Multiply Polynomials，本批只核常数缩放动机。
