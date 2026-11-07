# 下一有界批：连续复合与区间介值基础计划

日期：2026-11-05。计划人：`/root/part1_pedagogy`。状态：**计划已具体化；主代理已确认当前 pack 完成并解除冻结，授权开始两单元写作**。本计划由本代理落实B4.8两稿，主代理另写B4.9两稿；不改builder、ledger、验收记录或既有ZIP。本计划不是新单元已经写成或通过审校的证据。

## 1. 最小范围与学习路径

建议拆为两个连续阅读单元，避免把函数类型核查与完备性存在证明挤在同一个证明段中：

| 暂定单元 | 限定目标 | 未来稿件与锚前缀 | 预计正文与练习 |
| --- | --- | --- | --- |
| B4.8 连续复合与局部定义域 | 明确目标集合、实际像与复合域；直接证明连续复合；解释只有局部映入外层域时的合法限制和延拓 | `manuscript/foundations/real_continuous_composition.md`、`real_continuous_composition_answers.md`；`ccomp-*` | 约10—14页；8题及独立完整答案另计 |
| B4.9 区间上的介值定理 | 先处理端点与退化，再用实数上确界直接证明目标y的介值结论，零点作为特例 | `manuscript/foundations/real_intermediate_value.md`、`real_intermediate_value_answers.md`；`ivt-*` | 约12—18页；8题及独立完整答案另计 |

两者主归第146章26Axx的一元实函数连续性叶 **26A15**，交叉 **97I20** 函数教学。已核 `data/msc_taxonomy.json` 的原代码归属及 `data/catalog_titles_zh.json` 的26A15、97I20中英文短标题。26A15标题还包括连续模、半连续与间断等方向，本计划只承担上述两个限定目标，不把整叶或第146章登记完成；97I30为数列与级数教育，不机械沿用。

已经读过 `LEARNING_PATH.md`，核对 `data/production/prerequisites.json` 的 `single-analysis` 模块仍以functions、induction-counting、number-systems为广义入口，状态为partial_draft。所读路径快照的主进度仍写至B4.4，不能把该历史摘要当成新增B4.5—B4.7是否实际存在的判据：当前柯西、函数点极限、连续两稿已实际落盘，本计划以当前锚点和文件快照核查具体先修；待当前包完成后由主代理另行同步路径与台账。本次不改这些文件。

最小依赖图：

- 函数三项记录、限制、实数绝对值与B4.7连续 → B4.8连续复合。
- 实数上确界、全序与B4.7连续 → B4.9局部保号、直接上确界介值及零点特例。
- B4.9不需要先引用B4.8复合定理；教学上可顺读，证明依赖上保持独立。两者均不依赖BW、柯西判据、序列判别或平面几何。

排除：极限的复合总定理、数列连续判别、紧致性、极值定理、一致连续性、一般连通空间、导数、积分、一般反函数连续性、一般多项式或初等函数总理论。无必需新图、算法或数值代码；不把介值存在证明称为可执行求根算法。旧 `local-inputs/pending-batch33/` 的连续/介值候选未被本计划阅读或复用，也不继承其签署状态。

## 2. 已读、可定位的具体先修

以下路径均在 `manuscript/foundations/`；开写时再核冻结散列和对应命题条件。

| 接口 | 实际锚点 | 所需结论 |
| --- | --- | --- |
| 函数、目标与像 | `functions_definition.md#fun-definition`、`#fun-image`、`#fun-sets` | 函数是域/目标/图三项记录；像是目标的子集；每点有唯一输出；条件子集 |
| 相等、限制与严格类型复合 | `functions_composition.md#fc-equality`、`#fc-restriction`、`#fc-composition` | 限制保留目标；复合要求内层目标恰为外层域，实际像包含不自动更改原函数数据 |
| 连续主定义与孤立点 | `real_function_continuity.md#cont-definition`、`#cont-isolated-limit` | 连续只在域内点定义，不去心，不要求积点；孤立点直接连续 |
| 限制和有限运算 | `real_function_continuity.md#cont-basic-restriction`、`#cont-algebra`、`#cont-quotient` | 限制继承连续；和差常数倍乘积绝对值；商明确非零分母域 |
| 点极限的边界 | `real_function_limits.md#flim-domain-cluster`、`#flim-definition`、`#flim-uniqueness` | 仅用于辨别“连续复合”与“去心极限复合”的区别，不用未写的后者作证明 |
| 实数序、代数与误差 | `dedekind_additive_order.md#cutgroup-translation`、`#cutgroup-negation-subtraction`；`dedekind_ring_order.md#cutring-distributive`、`#cutring-multiplication-order`；`dedekind_division_field.md#cutdiv-definition`、`#cutdiv-order`；`real_absolute_distance.md#realabs-definition-bounds`、`#realabs-products-triangle`、`#realabs-error-root` | 正半径二分、有限min、局部保号、实区间及多项有限代数式 |
| 上确界及同域保留 | `dedekind_cuts_order.md#cut-supremum`（DC4）；`dedekind_division_field.md#cutdiv-complete-field`（DQ4） | 每个非空有上界实数子集有最小上界；若t<sup S，则t不是上界，有s∈S满足t<s≤sup S |

已在前一轮数学审读实际阅读DC4完整并集构造及DQ4的同一底层集合/包含序保留论证；本轮重新核文件身份。上确界由分割构造取得，不由待证的介值或连续图像取得。B3形式集合论课程仍未完成；现有条件子集和函数图背景按既有公开约定使用，不新增任意选择原则。

## 3. B4.8的最小证明任务

### CC0 类型准备：`ccomp-types`

先固定D,E⊆R，给定实值函数g:D→R、f:E→R以及实际像包含g(D)⊆E。对每个x∈D，先由g取得唯一实输出g(x)，像包含保证它在E内，再由f取得唯一实输出f(g(x))；因此逐点规则定义新函数h:D→R，h(x)=f(g(x))。连续仍只对已定义的实值函数使用，不额外扩展目标为E的函数的连续术语。

这不是直接把原g送入FC3：原g的目标为R，外层域为E，E≠R时类型并不匹配。另定义g_E:D→E，保持g的图；像包含保证该三项记录合法，每输入仍有唯一输出。新g_E与g在E≠R时不是同一个函数；但FC3允许f∘g_E:D→R，而其输出逐点等于h。两端集合也相同，由FC1得到h=f∘g_E。这说明新逐点函数与严格类型复合相容，不偷改原g的记录，也不要求g_E满射。

D空时h为空域函数且全域连续为空真；E空而D非空时像包含条件不能成立，不从空集取输入。

### CC1 直接连续复合：`ccomp-theorem`

条件：g:D→R、f:E→R、g(D)⊆E，c∈D，g在c连续，f在g(c)相对E连续；h按CC0新定义。先核g(c)∈E，使外层中心值合法。证明顺序：

1. 给ε>0，由f在g(c)连续取η>0，使y∈E且|y−g(c)|<η时，|f(y)−f(g(c))|<ε。
2. 由g连续取δ>0，使x∈D且|x−c|<δ时，|g(x)−g(c)|<η。
3. 对任意这样的x，明确y=g(x)∈E，把第二步误差送入第一步，得到|h(x)−h(c)|=|f(g(x))−f(g(c))|<ε。

η是外层输入半径，也是内层输出容差；δ最后才确定，均不依赖随后任取的x。允许g(x)=g(c)，此时外层输出差恰为零，不能错误添加去心条件g(x)≠g(c)。c或g(c)孤立时定义同样可用，无须积点论证。

### CC2 局部映入与局部一致：`ccomp-local-domain`

已给g₀:D→R、f:E→R、c∈D。若只知道g₀(c)∈E，不足以保证全域或任何完整相对邻域都能输入f。应区分三种安排：

- **全域映入：** g₀(D)⊆E，按CC0在D上逐点定义h；另作g_E时它等于严格类型复合f∘g_E。
- **自然可复合域：** H={x∈D:g₀(x)∈E}，逐点定义h_H:H→R、h_H(x)=f(g₀(x))。若g₀(c)∈E，c∈H；g₀在c连续则限制到H仍连续，再用CC1可得相对H的连续。这个结论不声称H含有c的整个相对D邻域。
- **确有局部映入：** 明示存在r₀>0，令U={x∈D:|x−c|<r₀}，满足g₀(U)⊆E。U含c；限制g₀|_U:U→R后按CC0逐点定义h:U→R、h(x)=f(g₀(x))，仅先定义于U。若g₀及f满足连续条件，则h在c相对U连续。对于任何已另行合法定义的F:D→R，若F|_U=h，则用min(r₀,δ_h)证明F在c连续。

第三种不自动定义远处的复合，第二种也不自动推出第三种。局部一致必须包括中心点；只在去心邻域相同可保点极限，未必保连续。用中心点值被改动的常零函数作反例。

最小具体对照：g₀(x)=x、D=R、E=[0,∞)、c=0；g₀(c)∈E但任意半径有负输入不进E。自然域H=[0,∞)，不能把自然域上的h_H写成原D上的同一个函数。正例用g₀(x)=1+x²映入E=(0,∞)，f(y)=1/y，确认全域无零分母后得1/(1+x²)连续；不引入三角函数等尚未写成对象。

### B4.8八题及完整答案要求

| 题号 / 拟锚 | 原创题任务 | 解答必须给出的核查 |
| --- | --- | --- |
| 1 `ccomp-q01/a01` | g₀(x)=x²:D=R→R与f:E=[0,∞)→R、f(y)=y+1的类型检查 | 核g₀实际像包含于E，构造g_E并核输出唯一；解释原目标R与E不同；合法复合为x²+1，不要求证明满射 |
| 2 `ccomp-q02/a02` | 重建CC1的直接证明 | ε→η→δ顺序、y=g(x)∈E、中心与重复内层值、孤立点均包括；禁止用序列判据代替 |
| 3 `ccomp-q03/a03` | 证明1/(1+x²)在R上连续 | 内层实值且实际像为正、外层倒数相对正域连续、实际复合域R、各中心值合法 |
| 4 `ccomp-q04/a04` | g₀(x)=x²、E=(0,∞)、c=1的局部映入 | r₀=1/2推出x>1/2所以x²>0；在U定义复合；另给F(0)=7、x≠0时F(x)=1/x²，仅证明其在1连续而不偷称全域连续 |
| 5 `ccomp-q05/a05` | g₀(x)=x、E=[0,∞)、c=0，外层f(y)=y² | 自然域H=[0,∞)，任意r内负点说明无完整局部映入；相对H的复合连续不等于原D上同一函数已定义 |
| 6 `ccomp-q06/a06` | 检查复合连续条件的充分性与反向失败 | 外层恒零、内层阶跃说明复合连续不迫内层连续；内层恒零、外层仅0处为1说明不迫外层在0连续；分别核全域与输出，不能由反向失败否定CC1 |
| 7 `ccomp-q07/a07` | D={0}∪[1,2]、E={0,1}，g:D→R，g(0)=0、g(x)=1在[1,2]；f(0)=7、f(1)=−3 | 内层每点连续用隔离/排除0半径；外层两点各有隔离半径1/2；输出复合在D连续，不虚构去心极限 |
| 8 `ccomp-q08/a08` | 局部一致延拓与只去心一致的区别 | 证明CC2的min半径传递；中心改值反例；另说明若把CC1外层连续替换为“外层去心极限存在”，内层恒等于该中心会使所猜复合极限失效，不扩写一般极限复合定理 |

## 4. B4.9的落实范围与证明任务

**计划演变。** 初稿建议将局部保号、零点引理、弱介值、一般区间像性质依次展开，八题包括完整重建sup证明。主代理实际稿改为直接目标y的上确界证明，把保号估计写入四步而不另设引理；一般区间像定理留待后续，练习集中于上确界见证、条件反例、三次方程、平方根重证和一个精确像。以下以实际两稿为准：`real_intermediate_value.md`、`real_intermediate_value_answers.md`。实际叙述先声明包含端点/退化的总定理，证明先处理严格端值，再集中处理边界；没有把严格端值条件用于零长度区间。

### 对象与总命题：`ivt-interval`

所有a,b,c,x,y,ε,δ为实数，a≤b；[a,b]={x∈R:a≤x≤b}，a=b是单点域。函数f:[a,b]→R在每个域内点连续，端点只检查区间内输入。总命题IV1对min(f(a),f(b))≤y≤max(f(a),f(b))断言存在c∈[a,b]使f(c)=y；二元min/max来自全序，不是整域极值。严格夹值才保证解在开区间，结论不负责唯一或计算。

### 完备性接口：`ivt-supremum-tool`

对非空有上界的S，由DC4/DQ4取c=sup S。先从最小上界定义证明：每个h>0都有s∈S满足c−h<s≤c；否则c−h也是上界，推出h≤0而矛盾。用[0,1)的上确界为1但1不在集合中说明上确界不自动是最大元；对任意候选u<1分别用成员0或(u+1)/2排除其上界资格。

### 直接上确界证明：`ivt-proof`

先设f(a)<y<f(b)，由端值不同推出a<b。令S={x∈[a,b]:f(x)≤y}。a∈S且b是上界，取c=sup S；核a≤c≤b，故f(c)合法。证明顺序为：

1. 在a对误差(y−f(a))/2取半径δ，令t=min(δ/2,(b−a)/2)>0、x=a+t；核a<x<b与邻近条件，得f(x)<y，故x∈S，进而c≥x>a。
2. 在b对误差(f(b)−y)/2取半径δ，令t=min(δ/2,(b−a)/2)>0、u=b−t。所有域内x>u都有f(x)>y，所以u为S上界，得c≤u<b。这里不用预设c∈S。
3. 若f(c)<y，在c对误差(y−f(c))/2取δ，令t=min(δ/2,(b−c)/2)>0、x=c+t；核x仍在区间且f(x)<y，故x∈S而x>c，矛盾。
4. 若f(c)>y，在c对误差(f(c)−y)/2取δ，令h=min(δ/2,(c−a)/2)>0。由见证规则取c−h<s≤c的s∈S，得到|s−c|<δ且f(s)>y，与成员定义矛盾。允许s=c，连续不去心。

实数全序只剩f(c)=y，前两步已给a<c<b。局部保号的半误差估计均在使用处给出，不新增未证命题；不假定S是区间，不假定f单调。完备性只在非空有界后取sup，不依赖紧致、极值、BW、二分数列、序列判据、复合定理或先有零点。

### 边界、逆端值与示例：`ivt-boundaries`、`ivt-example`

若y等于任一端值就取该端点；f(a)=f(b)时允许目标只能等于共同值，涵盖a=b，但不强迫内部恒值。若f(b)<y<f(a)，用同域g=−f（CT3）及目标−y，核−f(a)<−y<−f(b)，应用已证方向并消去负号。

例F(x)=x³−2于[1,2]：有限乘加给连续，端值−1与6给内部零点。另用(v−u)(v²+vu+u²)>0对1≤u<v≤2证明唯一。存在与唯一的依据分开，不提供未经误差证明的小数算法。

### B4.9实际八题及答案核查

| 题号 / 实际锚 | 原创题任务 | 解答必须给出的核查 |
| --- | --- | --- |
| 1 `ivt-q01/a01` | 端点、单点区间与相等端值 | a=b时目标迫为f(a)；等端值可以选端点，不推出恒函数；x²在[-1,1]反例；严格目标排除端点但不保证唯一 |
| 2 `ivt-q02/a02` | 上确界见证与最大元区别 | 每h>0给c−h<s≤c的完整反证；[0,1)上确界为1的两分支验证；不能先断言c∈S |
| 3 `ivt-q03/a03` | 阶跃删去连续条件 | [-1,1]负侧−1、非负侧1，端点异号却无零；固定误差1，坏点−min(δ/2,1/2)在域内且误差2 |
| 4 `ivt-q04/a04` | 删去完整区间定义域 | D=[−1,0)∪(0,1]，符号常值；每c≠0取δ=|c|/2分别排除另一侧，证明全域相对连续；0未定义，所以不能应用闭区间IV1 |
| 5 `ivt-q05/a05` | x³=2在[1,2]存在唯一 | CT2/CT3逐次乘加，端值−1/6，内点性；展开立方差并证两因子正，唯一性不归给IV1 |
| 6 `ivt-q06/a06` | 零点数量与端点符号 | x²−1端值同正却两根；x(x²−1)端值异号却三根；零积给完整根集，反例区分必要与充分 |
| 7 `ivt-q07/a07` | 从IV1重证非负平方根 | a≥0，域[0,a+1]合法，端值−a≤0与a²+a+1>0；a=0可取端点；非负根唯一用平方差；存在步骤不引用旧平方根，避免循环 |
| 8 `ivt-q08/a08` | 端值区间与实际像区别 | x²在[-1,1]的像⊆[0,1]用绝对值及因式非负；反向用已完成题7取非负平方根并证≤1；端值区间仅{1}，IV1只给端值区间⊆实际像 |

题7与早期 `real_square_roots.md#realsqrt-existence` 的关系仅是后置的另一证明；早期平方根不是IV1的前提，题8可以引用本单元已经证明的题7。实际稿未证明一般连续区间像仍为区间，故不将初始建议的该目标登记完成。当前范围不扩大至极值或紧致。

各单元八题必须全部独立写完整答案并双向链接。两单元草稿现已落盘；上述表格用于逐题审核，不以计划或作者自检代替独立数学、教学与产物验收。可以调整原创常数以改善阅读，但不能删除端点、零分母、域或量词检查。

## 5. 实际来源缓存与本次阅读

本轮新增网络请求为0。实际读取已存在、可读的官方固定提交缓存，而非引用旧报告假装已读原文。统一版本：Jiří Lebl，*Basic Analysis I*，6.3，提交`e21ec524ca7d54f800c693b948020c188d21d01f`。

| 原生资源 | 缓存路径 | 字节数 / 本次重新核算SHA-256 |
| --- | --- | --- |
| [ch-contfunc.tex](https://raw.githubusercontent.com/jirilebl/ra/e21ec524ca7d54f800c693b948020c188d21d01f/ch-contfunc.tex) | `/tmp/part1_audit-function-limits-ch-contfunc.tex` | 119775 / `3fe56fe7261f3db0dfb0dbabe8e807b0781c41255c2b9cb463f4868fbb13c14d` |
| [realanal.tex](https://raw.githubusercontent.com/jirilebl/ra/e21ec524ca7d54f800c693b948020c188d21d01f/realanal.tex) | `/tmp/part1_audit-function-limits-realanal.tex` | 18862 / `a355edf1ff287d98d13bfc50fa9cfcd541b42b8210f0172dfb5dadafb58a47ee` |
| [LICENSE.md](https://raw.githubusercontent.com/jirilebl/ra/e21ec524ca7d54f800c693b948020c188d21d01f/LICENSE.md) | `/tmp/part1_audit-function-limits-LICENSE.md` | 467 / `682fedaab34d7d47962da7276284e608f43881c07c3c887cb66368688748c13d` |

这三个缓存原先HTTP200的取得时间分别见本轮既有 `research/production/real_function_limits_plan.md`；本计划不把缓存复读时间改称新请求时间。本次实际阅读者为 `/root/part1_pedagogy`：

- `ch-contfunc.tex`第999—1038行：连续复合的对象类型、条件、序列法证明及复合例。标准条件支持CC1；源书使用序列判据，本书计划另给直接ε→η→δ证明。源书三角函数例不迁移。
- 同文件第1567—1720行：严格异号零点引理、二分数列证明、两方向严格介值及区间限制。标准结论支持IV1—IV2的介值结论；源书证明用单调数列和连续序列传递，本计划不用这条证明链，拟原创直接sup S论证。不把源书的求根近似说明当成本书已实现算法。
- `realanal.tex`第374—410行实际确认作者、版本6.3与2009—2026版权；`LICENSE.md`全文实际读过。许可为CC BY-SA 4.0或CC BY-NC-SA 4.0双许可，不是公有领域。

另已全文阅读来源代理的 `/tmp/continuity-next-source-review.md`，其对序列证明依赖、严格端点和本书原创sup路线的区分与上述记录一致。来源核验只覆盖上述标准命题条件及证据边界，不声称完整读完3444行原章，也不把源书极值、一致连续部分当作本批已教内容。本书正文、例子、习题与答案必须独立编写；外部TeX正文不收入分发包。缓存若丢失需重新取得同固定URL并核哈希，不能仅凭计划表重建不存在的阅读。

## 6. 计划时的当前接口快照与验收条件

| 当前文件 | SHA-256 |
| --- | --- |
| `LEARNING_PATH.md` | `af6e679da454cffdd5cb096e48afad157d767b284ed7d486a1f24cec599b8925` |
| `data/production/prerequisites.json` | `32156fc6c6b9bef7fa10fe1d0f6217f96955e7d19793155902c34c6923f61eb0` |
| `manuscript/foundations/real_function_limits.md` | `93e6559645e147597cb9950108febd90e14a3417e614e231ca014bd1b901241b` |
| `manuscript/foundations/real_function_limits_answers.md` | `ab47e47ddfc0ba5a5270e16a535b916ced6e572c8064687307ca18823b4bde1b` |
| `manuscript/foundations/real_function_continuity.md` | `c28fe5c66a2895d0db3ad9cfbc2ada9f3e9f8e7942faaa80802529312d19a21b` |
| `manuscript/foundations/real_function_continuity_answers.md` | `859e8bbb937f3ce8d4a12beb70956e49984a06da635284bd3d8170ae7a3007aa` |
| `manuscript/foundations/functions_definition.md` | `1dee6ffb8bada53f6f09ea4ad908c0a03fd06c937fb685538566175cb9655650` |
| `manuscript/foundations/functions_composition.md` | `806b32944f8253b2e2af3b2a551a25cc0ce6bf17ce51cc6b50216cf28e58a94a` |
| `manuscript/foundations/dedekind_cuts_order.md` | `a244695551c88b167daac9ddf76c8becc5e70411ea5e30063af9cf8e7ce22ee4` |
| `manuscript/foundations/dedekind_division_field.md` | `f69f9304027ec15fbeb50ebddc1198e203d1676e7bd014b721f146aa9b1db610` |

这些散列表示本计划所核接口快照，不冻结主代理正在完成的包流程。主代理已明确通知“snapshot已完成正式解除freeze”，并授权B4.8直接写入manuscript；开写核真实先修稿，不借旧计划散列替代当前正文。

后续正文必须分离作者与独立数学/教学审读身份，逐项检查类型、域内点、孤立点、端点、退化区间和全称量词；构建、链接、公式、PDF实际页面检验以及最终归档另走本批接口。未完成这些步骤前只记draft/pending，不写accepted、整叶完成或全部分析课程完成。本计划只界定随后已授权的两单元写作；不自行触发台账、工具、发布或归档变更。
