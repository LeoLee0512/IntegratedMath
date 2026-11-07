# B2.9 有理坐标与函数图：独立数学复核

审阅者：Astra/high独立数学代理。日期：2026-10-29。结论：正文和8题完整答案数学通过；已发现事项均修复，无待处理阻断。

## 定义与CO1—CO4

Q²明确是Q×Q的简记，点是有理有序对，不把数、点、点集合混作同一对象。轴成员按对应坐标为零双向证明；CO1两层三歧性给九种互斥且穷尽的符号组合，四象限不含轴点，四轴向部分不含原点。交并先以已有共同U的子集定义，再用于Q²，没有凭空形成“所有对象集合”。

CO2先假定函数合法和A,B⊆Q，逐成员证明G={(x,f(x)):x∈A}，域内判输出、域外直接排点而不求未定义值。第一坐标集合=A的反向确实使用输出存在；第二坐标集合=像逐向用见证输入。空图边界、不同目标同图和同像反例完整，未错误恢复目标。

CO3先G⊆A×B再检查每个a的纵坐标集合T_a单元素；将数集合T_a与点集合G∩V_a明确区分。正向分别用存在/唯一，反向从单元素取局部输出并核唯一，无需选择公理或延拓。空域迫图空，非空域空目标不能有单元素T_a；“至多一个”、越界和不同输入共输出均有精确例子。

CO4横轴交点要求合法输入且输出零；纵轴只有0∈A时才求f(0)。两图先交域再比较函数值，不要求两函数目标相同即可比较其Q²子集；公共点不等于函数相等。限制保留目标且删除不允许横坐标，原公式可在域外算数不恢复已删点。

## 具体发现及闭环修订

1. 指出图/轴本身是笛卡尔积的子集，不能写成积的成员。作者统一修正正文CO2、§7、题4题面，以及答案4的G2、答案5空图、答案6两轴；正确的“点属于积”保留。修订位置已逐项实际复读。
2. CO4两图交集证明出现两处裸“,quad”，已改为规范\quad，避免误显字母为乘积或变量。
3. “一般有理直线的定义留待下一单元”改为实际会写的“仿射图和一般一次关系的点集合”；“有理函数”改为“有理数上的函数”，避免与未来rational function专名混淆。
4. 新增逐步【依据】与题8四次求值已复核，结论与原成员证明一致。

## 八题完整答案逐项结果

| 题 | 核验结论 |
| --- | --- |
| 1 | 坐标交换P≠Q；参数唯一t=3,s=2并代回(5,3)；一般交换不变iff u=v双向成立。 |
| 2 | 九点各落一个指定符号类别；轴不进象限，原点不进轴向部分；穷尽与互斥均有证明。 |
| 3 | f图{(−1,0),(0,1),(2,3)}，像{0,1,3}，目标还含−2；(3,4)不在图且f(3)未定义。 |
| 4 | G1合法；G2漏输入1；G3在输入0多输出；G4第二坐标3越界。T0,T1与对应图完全一致。 |
| 5 | 全Q常值2的两函数图像相同但目标不同，函数不等；两空函数图/像同空但目标不同，仍不等。 |
| 6 | 横轴常值0、H−1常值−1合法；纵轴输入1缺记录、输入0多输出；改域{0}仅修复存在，唯一仍失败。 |
| 7 | 两规则在−1、2同输出0、3；在0分别1、−1，完整合法反例否定样本决定任意函数。 |
| 8 | f轴交点(2,0)、(0,−2)，与g共点仅(3,1)；共同域{0,3}已枚举完。限制S保Q目标，删除(0,−2)，与纵轴交空。 |


## 实际审阅与依赖核查

已完整阅读本批四份实际稿件及全部16题完整解答，随后逐项复读作者修订处，不以计划或其他代理的结论代替全文阅读。终稿规模：rational_coordinates.md 395行、rational_coordinates_answers.md 275行、affine_graphs.md 366行、affine_graphs_answers.md 281行。两作者已确认冻结；下方哈希才是本次通过的具体版本。检查四稿内部引用均可定位，来源锚coordinates-affine-sources由构建程序提供。

实际核对既有函数接口：有序对按分量相等、A×B的元素是有序对；函数仍为(A,B,G)，G⊆A×B并对每个输入存在且唯一输出，空域与空目标的边界保持F2。FC1要求域、目标和图，FC2限制保留目标。图可决定域与像，但不能凭图恢复未命中的目标元素。旧B2.7交并仅明说Q的子集，新B2.9已先推广到共同已给U再用于Q²。系统先修把共同解定义为同一有理数对同时满足所有条件；一次方程和有理非零除法提供参数分支及唯一性，次序的三歧性与乘法符号提供九类位置和单调证明。没有为新稿引入实数、完备性、欧氏平面公理或未经教学的矩阵/秩结论。

## 实现与主验证器范围

已全文阅读tools/rational_affine.py及tools/validate_rational_affine.py，并核当前验证JSON中三份源码哈希一致。六个API范围如下：affine_value精确求值；slope_through返回不同横坐标两点确定的(a,b)，同横坐标无论纵坐标相同或不同都拒绝；intercepts分别记录纵轴点与横轴unique/none/all，all特指整个有理横轴而非Q²；intersect_affine返回唯一点/空/重合；classify_linear_relation返回仿射/竖向/全Q²/空；finite_graph_test仅检验给定的有限域、有限目标和有限点集。

数值输入只接受int或Fraction，拒绝bool/float及其他类型，运算使用Fraction；所有除法都位于已核非零分支。有限图容器为list/tuple/set/frozenset，点为两项list/tuple；重复记录和相等分数合并为同一集合成员。全部实际输入先验证形状/类型，随后才判断越界点；格式正确但域外或目标外的记录返回False，而非法形状/数值抛ValueError。存在与唯一都检查，空域空图合法，包括空目标；非空域空目标失败。有限样本不能认证无限函数，也不能替代目标集合的声明；本模块没有自动限制任意D或解析任意题目表达式。

主JSON记录SymPy 1.14.0原式linsolve及精确成员检查：125次求值，500组不同横坐标两点，125组同横坐标拒绝，625组仿射交集及15625次成员，25组截点，125组一般一次关系及3125次成员，32768份有限图，106非法输入和3组重复/空图检查。另记录6个示例结果。这里报告的是已读取并核哈希的主验证器实际输出，不冒称由本审阅者重新执行了该次SymPy运行。

## 本审阅者独立有限oracle

已实际运行独立Fraction脚本，完整代码及输出附于affine_graphs_math_review.md。它不调用被测交点公式来构造预期，也不依赖SymPy：用独立两未知数Gauss–Jordan消元处理原始方程行；比较规范化后行条件及唯一解；对有限图独立穷举候选关系并计每个允许输入的配对数。

七值系数集合{−3,−1,−1/2,0,1/2,1,3}给2401组仿射交集：2058唯一、294无解、49重合。2401组两点中2058可唯一确定、343同横坐标被拒；49组截点，343次求值，343组一般关系及16807次原式成员均一致。有限图采用三个Fraction标签{−1/2,0,2}，对域/目标的全部8×8子集及环境9点的全部512子集，实际检查32768份记录，恰有170份合法函数。另有6个显式重复、空域、空目标、越界、多输出案例。总拒绝计数450包含343个同横坐标及107个非法类型/形状输入，不能把450都称作类型错误。

这些检查只是有限实现证据，不是任意有理参数的证明；一般数学结论来自逐步正文与题解审读。验证脚本的通用消元也不是向书稿增添新的先修要求。

## 来源审计及批准边界

已读本地coordinates_affine来源审计Markdown，并检查JSON的来源、访问摘要和范围记录；没有重新联网抓取。审计保留13次HTTP 200公开访问，OpenStax与mathlib两个来源系列；正式化没有冒充重新访问。OpenStax许可CC-BY-NC-SA-4.0、mathlib Apache-2.0，未复制外部题目或图像。mathlib相关图延拓包含Nonempty和choose!，本书按已有三数据图条件直接证明，没有引入这种任意延拓。未编译Lean，未形式化验证本书。

本审阅建议将来源记录中的非严格单调表述与实际教学范围分开，来源代理已修订：正文只教严格递增/递减与常值；非减/非增仅属相关延伸，不登记为本批已教目标。坐标模型不等于全部欧氏点，也不授予完整解析几何或分类章完成。

本结论仅覆盖下列哈希的数学文本、题答与实现边界。图注的代数坐标和样本声明已核，未给最终PDF逐页视觉批准；没有批准发布、合并或推送。若冻结文本改变，应复核相应差异并更新绑定。

## 四稿最终哈希

| 文件 | SHA-256 |
| --- | --- |
| `manuscript/foundations/rational_coordinates.md` | `13f253560a79cb0eaf336dbebd78cc4cb89ba43937bf9cad6f77dfa67d6c9e48` |
| `manuscript/foundations/rational_coordinates_answers.md` | `fe7b4f82a1a76cbd6ebb8d9ccdfa316da16ed63a70acbd68c1322a82c92f1eb6` |
| `manuscript/foundations/affine_graphs.md` | `1df31c69a925d64179d069cd450bd6a53c876fa55eae8727d394ba01b9438c92` |
| `manuscript/foundations/affine_graphs_answers.md` | `f41cc17b765ac4bc7d33fd6b8c7c9d1bbc7b1c6671f44e22d6f8400850ecbd09` |

## 依赖、源码与审计绑定

| 文件 | SHA-256 |
| --- | --- |
| `manuscript/foundations/functions_definition.md` | `1dee6ffb8bada53f6f09ea4ad908c0a03fd06c937fb685538566175cb9655650` |
| `manuscript/foundations/functions_composition.md` | `806b32944f8253b2e2af3b2a551a25cc0ce6bf17ce51cc6b50216cf28e58a94a` |
| `manuscript/foundations/rationals_order.md` | `db52d14c0642912bc281e22e1846f778bc9aa876d1a6ba22e04d5eb3ae28f3ba` |
| `manuscript/foundations/linear_equations.md` | `46f013a3d82fa47fc1fdaf73325ed90baf6f7a92bb73e27f1bac98642eed70b4` |
| `manuscript/foundations/linear_systems.md` | `a990e27b6c36e0b3f02e468696c89102b3c9e120a77730c8f43b804c8863c46b` |
| `manuscript/foundations/linear_inequalities.md` | `89a72b6ff336ee06f23c19fef9f689d5c091182ce61f09b1f914408f6ca038a6` |
| `tools/linear_equation_solvers.py` | `c3ec0ab4a892397d3d0af59a1acd367bf1f1cfea80e3e14bd6b2b6cd790b74c9` |
| `tools/rational_affine.py` | `e62a96b5f79062d7abf96e73a1795e645ce735932c9af2f57ec2376033261a8c` |
| `tools/validate_rational_affine.py` | `953eabd65e00889a2f1ee26ea41232ed4911ea5c0484eefa0f6d742eac1d9f6d` |
| `research/production/rational_affine_validation.json` | `1c031079d131160857b96ddab6415ef478d63ee6d20e22a203b3518eca428f9f` |
| `research/production/coordinates_affine_sources_2026-10-29.md` | `bdcfbae348b36e4bfa5a1bd00daf3b8e1d97e05cb03a231ab49bffea4858fcd2` |
| `research/production/coordinates_affine_sources_2026-10-29.json` | `292f8e7318dd100689b00cc9afe622f758f3fa8d4d3112e44b1c6ce77a24f45c` |
| `research/production/affine_graphs_math_review.md` | `d1cb15f66fb96174d580f2c1823614d820b9b23e5bb8c70cbe44a8ff968a4dbb` |

## 独立oracle重放位置

完整代码与实际输出见同批 `research/production/affine_graphs_math_review.md` 的“独立oracle完整脚本与实际输出”；上表绑定该报告哈希。脚本SHA-256为 `2902f96dfbe1cd681b16316fa033751a9a2e6071f356fec292eaa9d1a58e5be6`，包括本单元32768份有限图穷举和下单元精确消元检查。该证据可重放，但不替代全文一般证明。
