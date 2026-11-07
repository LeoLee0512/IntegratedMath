# B2.7 一元一次不等式与有理区间：独立数学复核

审阅者：Astra/high独立数学代理。日期：2026-10-29。结论：当前冻结正文和8题完整答案数学通过；无待处理数学阻断。

## 命题、域与边界复核

不等式先指定D⊆Q及L,R:D→Q，原式必须在每个允许输入处有定义；同域等价由解集相等与逐输入双向条件互相推出。空D的全称成立不被误当成存在解。交并在首次使用前以有理数子集成员定义，“或”为至少一个、允许同时成立；同域复合条件的两个包含方向均给出。

四种有限端点区间均按Q中比较定义；同端点仅全闭给单点，其余为空，反序端点均空。无界端的∞只作记号，既非有理数也非额外成员。受限D与全Q结果相交，离散D不会被未经许可补成区间。

LIQ1按RO4/RO6/RO8分别说明平移、正乘除、负乘除的两个方向和非零条件。零乘数对≤可增解、对<可丢解，明确不照搬方程同乘保持原解的结论。变号M分D+、D−、D0，穷尽互斥；零支必须核原条件，不能除零。1/(x−1)>0例保留原域x≠1并得x>1。

LIQ2对a正负及a=0时b与c的三种关系完整分类，商仅在非零分支引入；端点因等式at+b=c而仅被非严格条件收入，仍须检查属于D。LIQ3先同域归约(a−c)x与d−b，再按合并系数分类，不用原a的符号代替差的符号。LIQ4的交并依成员证明，例题严格端点与空交正确。

本审阅与教学审阅均指出“等号左边原系数”不适合此不等式语境，作者已改为“原不等式左侧系数”，实际复核通过。作者另报告在答案落盘前已将题8末段支序口误改为显式x<1全满足、x>1无解；本审阅读到的完整答案已正确，不将其冒称为自己发现的错误。未发现其他待修数学问题。

## 八题逐题核查

| 题 | 独立核验结果 |
| --- | --- |
| 1 | I=[−1,2)，有限D交集{−1,0}；同端点全闭为{1}、含严格端为空、[2,1]为空；∞不是成员。 |
| 2 | 5−2x≤1给x≥2，严格版x>2；除负数反向，端点2正确。乘零分别增解/丢解，见证2/0正确。 |
| 3 | 内部表达式为x/3+1/6，乘−2后为−2x/3−1/3；≤1给x≥−2，<1给x>−2，固定分母非零及全部反向步骤正确。 |
| 4 | 四式依次给D、空、空、D；空D全部空且不推出存在输入。 |
| 5 | t>1给x≤1或x<1，t<1反向，t=1给Q/空；x=1在任意t下取等，严格式均排除。 |
| 6 | h=a−c、k=d−b全分类正确；具体h=2,k=3，D内{−1,0,1}。原式四行代入数值全部核对无误。 |
| 7 | 同时条件交为[−1,2)，至少一条为(−∞,−1)∪[2,+∞)；端点代入和一般包含式“或”说明正确。 |
| 8 | 原域Q中x≠1，x>1分支化为假2≤−1，x<1分支化为真2≥−1；各步可逆，合并全解x<1，x=0提供合法反例，端点1因未定义而排除。 |


## 实际阅读与依赖边界

本批四稿均已完整阅读：B2.7正文412行、答案275行，B2.8正文324行、答案335行；两组题目与全部16份答案逐项对应。本报告不是基于作者或另一审阅者的通过声明。随后重新检查了修订位置、当前文件哈希和题答锚点；来源附录锚点由构建程序提供。

复核实际依赖接口：functions_definition公开采用按元素判等及按条件取子集的朴素集合背景，并未声称从公理构造全部集合；linear_equations的表达式有定义、共同D及双向解集等价仍适用。rationals_order的RO2提供三歧性、反对称和严格/非严格混合传递，RO4/RO5提供平移与取反，RO6/RO8明确正负乘除和零因子的区别。rationals_absolute的RAB1给非负性与零判据，RAB3仅给非严格两侧界且允许负上界，RAB4给绝对值乘积，RAB7给有理距离。新稿没有把尚未证明的实数完备性、连续数轴或几何事实当作推导依据。

## 精确代码与有限核算

实际阅读tools/rational_inequalities.py及主验证器。两个solve接口只接受int/Fraction（bool和float不接受），先核四种关系，再按a=0、a正负和绝对值阈值分支求解。区间联合以不可变tuple记录，有限端点为Fraction，None仅是无界标记；空tuple为空集，同端点全闭记录为单点。a≠0的绝对值正阈值分支用正数abs(a)产生有序端点；r=0分别给空、单点、全域、删中心的双开射线。

contains只核其数值输入，并信任求解器产生的区间记录，不是任意记录校验器。内部compare仅核比较符号；不得把它描述成验证任意数值对象的公开解析接口。代码不解析题目表达式、不自动筛选D、不实现一般区间交并规范化，也不证明书中一般定理。

已读主验证器实际JSON输出，核对其中三份源码哈希与当前文件一致：SymPy 1.14.0对500组线性、500组绝对值条件进行1000次完整实区间联合比较，另有10616次有理成员、760次有限端点、36次非法系数、12次非法关系、6次非法成员值和2次显式D筛选检查，6个显式例均通过。这是主验证器的现存运行记录，不冒称本审阅者重新进行了该次SymPy运行。有限端点均为有理数，外部实集合比较后限制到Q是实现证据；书稿的先修及证明仍完全在Q内。

本审阅者另实际运行独立Fraction oracle：七值系数集合{-3,-1,-1/2,0,1/2,1,3}的三位置笛卡尔积，每种四关系，得到1372组线性和1372组绝对值。独立使用operator比较原表达式，收集原表达式阈值点、绝对值转折点及返回端点，检查全部分割点、相邻中点及两端外侧代表点。它不调用生产compare，也独立检查区间成员与contains一致。实际通过11480点、2548区间记录、54非法输入及7显式例。392个a=0、392个第三参数为零、1176个第三参数负值计数跨两类求解器；不能把后两项都称作“绝对值半径”计数。有限枚举及代表点检查不是任意系数上的一般证明。

## 来源与批准范围

实际阅读本地来源审计Markdown及JSON的来源、条件、分类和限制记录。审计有15次成功公开请求，分属OpenStax与mathlib两个系列；本审阅者没有重新联网取证。OpenStax许可记录为CC-BY-NC-SA-4.0，mathlib为Apache-2.0；只据其核条件，没有复制外部题目或图像。审计明确排除“绝对值总严格为正”的局部误述，保留mathlib零逆元约定与本书除零无定义的差异；@[to_additive]源码阅读不等于Lean编译或本书形式验证。

结论只覆盖下列哈希对应的数学文本、16份解答和实现边界。未作最终PDF逐页排版批准，也未批准发布、合并或完整分类章完成；若正文或题答再改，须按差异重审并更新绑定。

## 绑定的四份稿件

| 文件 | SHA-256 |
| --- | --- |
| `manuscript/foundations/linear_inequalities.md` | `89a72b6ff336ee06f23c19fef9f689d5c091182ce61f09b1f914408f6ca038a6` |
| `manuscript/foundations/linear_inequalities_answers.md` | `a5a1878a6e9175bc09a02598fa23035aef867b6817769dfbace506ba3085747c` |
| `manuscript/foundations/absolute_inequalities.md` | `766c49a4d2ef4ab13bab56aebd663c827b2ba49d1b1f1f26ba772f8787bf75c5` |
| `manuscript/foundations/absolute_inequalities_answers.md` | `c0673fd63b78f46fefac4581057de06c7790b282786ceff9d35dfeb76bc7dc88` |

## 依赖与审计证据哈希

| 文件 | SHA-256 |
| --- | --- |
| `manuscript/foundations/functions_definition.md` | `1dee6ffb8bada53f6f09ea4ad908c0a03fd06c937fb685538566175cb9655650` |
| `manuscript/foundations/linear_equations.md` | `46f013a3d82fa47fc1fdaf73325ed90baf6f7a92bb73e27f1bac98642eed70b4` |
| `manuscript/foundations/rationals_order.md` | `db52d14c0642912bc281e22e1846f778bc9aa876d1a6ba22e04d5eb3ae28f3ba` |
| `manuscript/foundations/rationals_absolute.md` | `fe10f17f72f2128cd1ad9230b381fd3da2a000fb36b99c7bf097f9522b87b406` |
| `tools/linear_equation_solvers.py` | `c3ec0ab4a892397d3d0af59a1acd367bf1f1cfea80e3e14bd6b2b6cd790b74c9` |
| `tools/rational_inequalities.py` | `c4c54bceea7c55549a1d27cfecb35bdc8e082e9123ef20c309b20d140d72c254` |
| `tools/validate_rational_inequalities.py` | `6ddee0e0db7d39d9f12e95625978bae63b374098c5a5fc06819a93e399efbfd6` |
| `research/production/rational_inequalities_validation.json` | `dd7c94ca40a8c59d92ee9cce805019d9980a67c7798142082ec64ed95835adbb` |
| `research/production/linear_inequalities_sources_2026-10-29.md` | `6de00de991d757736e19c6823a9b04ed7a5944bdb0984df9c503368cc876b1f6` |
| `research/production/linear_inequalities_sources_2026-10-29.json` | `6c7814d77d7b01d80c822f8d1f7825cc8bf2289a18ad250fcad37580a707cf7c` |
| `research/production/absolute_inequalities_math_review.md` | `b9aae99f752e209d3b742b1c8ec450898b125e34847a437b438f42dd21d3ee3b` |

## 独立oracle重放位置

完整脚本和实际输出附于同批 `research/production/absolute_inequalities_math_review.md` 的“独立oracle完整可重放脚本”，上表绑定该报告SHA-256，避免只记录无法检查的计数。该脚本同时覆盖本单元1372组线性参数和绝对值单元1372组参数。脚本SHA-256为 `f662cebe6b4c4fb5418fc712d6a06438ed03b50b3ec822994e86d57a4aa8ec2e`。数学结论来自前述全文证明核验，有限代码证据只提供额外支持。
