# B3后续有限计数桥接：独立未注册计划

日期2026-11-05。规划者/root/part1_build。本文件仅记录后续候选单元，不新增正文，不注册当前第33批69单元，不改变冻结源码、构建清单或accepted_reviews。编号由主代理随后确定，不因计划存在给任何MSC节标完成。

## 已实际读取的先修与不可重复计数的内容

本轮通读B1.1 natural_numbers及答案、B1.3 natural_order及答案，核读B2.11 rational_powers与B2.12 finite_sums正文；有限和答案重点核索引、递归、前缀、线性、拼接与补零；幂答案只按题目/证明范围复核，不宣称重新完整数学审校。另查看函数双射/逆函数相关接口及实坐标平面开篇。文件字节见末尾。

- B1.1公开采用P1—P5与固定更新递归原则，普通归纳的起点、任意步、固定参数和条件句归纳已教，加法交换结合有完整证明，答案8证明消去律。
- B1.3正文O10已经由普通归纳证明强归纳，O11证明自然值严格下降的次数界；题7答案ord-a07完整证明任意非空自然子集的唯一最小元，依赖为普通归纳→强归纳→最小元。不能再宣称首次证明强归纳/良序，不能用良序倒证旧强归纳。
- B2.11已有非负整数幂的固定递归、三条幂律、零底数/零指数边界及自然嵌入相容性，未教阶乘或二项式计数。
- B2.12已有I_n={j∈N:j<n}、空表、有理表、带步数状态递归、延拓独立、线性、连续拼接、尾补零；末尾明确尚无一般有限置换重排和多重求和换序。不能把既有求和规则算成B3新目标。
- B2.3明确未引入基数或抽屉原理。B2.35已有R×R坐标平面及逐分量运算；从二坐标推广任意有限索引仍需新定义和证明，不能只改上标。

## 一个有界单元及真实分类

暂题：**有限索引、计数唯一性与重编号**。建议锚前缀fct，最终编号与命名由作者/主代理确定。本单元第一次证明：有限集合的元素个数不随无漏无重编号而改变；区分索引数量、不同坐标值数量和线性维数。

主归03E10“Ordinal and cardinal numbers／序数与基数”的有限基数局部，第8章03Exx、第3部分03-XX、当前目录第161节；交叉97E60“集合、关系与集合论（教育方面）”（第525章、第5927节）。05A05“Permutations, words, matrices／置换、字、矩阵”（第12章、第218节）只记录有限置换接口。05A10为阶乘/二项式系数，不属本单元目标；15A03为后续向量空间/线性相关/秩用途，不计当前完成。已实读原MSC解析台账、中文目录及生产目录核实上述名称和编号，不新造章号；分类记录不是数学论证来源。

正文建议12—18页、答案另计，统一排版后实测。若超预算，删扩展练习，不压缩关键量词和空集分支。不追加阶乘、二项式定理、一般加乘计数、无限基数、维数定理。

## 精确先修和采用边界

1. B1.1 b1-induction、b1-peano-rules；B1.3 ord-predecessor、ord-successor-comparison、ord-trichotomy、ord-partial-order。最小元已证接口ord-a07若进入主链，正文须显式链接并概述条件，不要求读者自行找到答案。
2. B2.1 fun-sets、fun-definition、fun-empty；B2.2 fc-equality、fc-restriction、fc-composition、fc-identity；B2.3 bij-injective、bij-surjective、bij-bijective、bij-composition；B2.4 inv-reverse-graph、inv-two-sided。复合写准确目标；改目标为子集要重新检查每个输出。
3. B2.12 sum-indices只复用I_n与零长度表。计数主链无需有理求和、实数、自然减法或除法，不以高阶数系作必需先修。
4. B3.1/B3.2量词和集合运算可回访，但目前未注册，不能声称已进入第33批PDF。仍采用集合外延、给定集合的条件子集背景，不声称重建ZFC自然数或选择公理。

## 新目标、候选锚点与完整证明义务

**FCT1，fct-swap：有界索引交换。** 给t∈I_(k+1)，定义交换t与k、其余固定的τ:I_(k+1)→I_(k+1)；t=k时为恒等。逐分支证明τ∘τ=id，所以双射。只是一个明确交换，不引用“全部置换可分解为交换”。

**FCT2，fct-injection-bound：单射索引数不增。** 对所有m,n∈N，存在单射I_m→I_n当且仅当m≤n。必要方向对目标长度n归纳，性质包含任意m与任意单射的量词。n=0时m>0会使输入0没有空目标输出。n=k+1时m=0直接成立；否则m=l+1。给单射f，用FCT1把f(l)交换到k；限制域为I_l，单射性保证这些输入都不命中k。明确改目标为I_k，得到新单射。归纳给l≤k，再取后继得m≤n。充分方向用I_m⊆I_n包含映射。不能以“删一个自然少一个”替代范围和类型检查。

**FCT3，fct-cardinality：有限及个数唯一。** 定义A有限为存在n与双射e:I_n→A；先称n为编号长度，不预先使用唯一的|A|。两编号e:I_m→A、d:I_n→A下，构造d⁻¹∘e及e⁻¹∘d，FCT2给m≤n、n≤m，反对称得m=n，之后才定义|A|。证明|A|=0等价A为空，已给双射保持有限及个数；空函数不排除。

**FCT4，fct-equal-size：同规模有限函数单满射等价。** 先证I_n自映射单射必满。若漏t，n=0不可能有t；n=k+1时交换t与k，改目标为I_k得到I_(k+1)→I_k单射，违反FCT2。再证满射必单：每个目标y的原像为非空自然子集，引用ord-a07取唯一最小元，明确规定g(y)。由f∘g=id得g单射，刚证结果给g满射，结合f∘g=id证明f单射。此为确定的最小元规则，不是任意选择公理。最后通过给定编号转移到两个同规模有限集合。抽屉推论m>n时任何I_m→I_n函数必碰撞，来自FCT2和单射定义的否定，不另藏假设。

**FCT5，fct-reindex：表的可逆重编号。** 给具体表x:I_n→X与置换σ:I_n→I_n，定义新表x∘σ，用σ⁻¹写出恢复公式并核复合次序。重复坐标值不影响编号；任意索引映射未必可恢复。这里不声称新旧表作为函数相等，也不宣称一般有限求和重排已证明。

## 八题梯度及独立完整答案要求

| 题 | 任务 | 答案必须检查 |
|---|---|---|
| 1 | I_0/I_1/I_3及表(2,2,5) | 三位置与两不同值；空表无第零项 |
| 2 | I_4交换1与3 | 完整输出表、τ²=id及t=k边界 |
| 3 | 归纳量词诊断 | FCT2的任意m/f；只固定m不能直接覆盖缩小后的l |
| 4 | 具体单射I_3→I_5的后继步骤 | 交换末项像、限制域、改目标，两个新函数类型 |
| 5 | 两编号不能给不同个数 | 逆复合、两个不等式、反对称，包含空集 |
| 6 | 抽屉与缺条件反例 | I_4→I_3必碰撞；I_2→I_3单不满，I_3→I_2满不单 |
| 7 | 满射的最小原像 | 有限实例的完整g、fg=id；一般证明不能只说任选原像 |
| 8 | 重编号及错误恢复 | 含重复值三项表、非自逆3循环、σ⁻¹恢复；非双射重编号丢信息的两张不同原表 |

主链全部置于正文，不藏在习题里；最小原像配独立例题和类型图。答案逐题完整并保留题答往返锚点。所有目标是待写/待独立审阅，不是计划签署即验收。

## 通往有限实数坐标与线性代数的实际接口

交付仅为有限索引、编号长度唯一和可逆重编号。下一单元再定义任意长度实数表x:I_n→R、逐坐标加法/数乘及标准坐标记录，逐条把实数域规则提升为逐点等式，检查n=0唯一空表。若定义所有这些表组成R^n，须当时公开函数集合存在背景，本计划不偷偷提供集合论定理。

已有B2.35的R²是有序对模型，后续须用明确双射连接到I_2→R表模型，不宣称底层记录自动同一。现有一般有限和在Q中证明，实线性组合需要实数值递归和线性规则的新证明，或先完整证明适用的代数结构版本；不能直接把Q换成R。一般置换重排、矩形双重和换序可另作有界接口服务矩阵乘法，不挤入计数单元。

编号长度唯一只说明槽位数量，不证明线性基等长。R^m和R^n的集合等势也不能决定线性维数；有限生成族、交换引理、秩和线性相关需另有线性证明，不用抽屉一句话替代维数定理。

## 来源及状态

本次只核本书已有证明和真实分类台账，没有访问或宣称核读新的外部数学来源。写作时仍须另取得有限集计数/抽屉原理具体来源，记录版本、实读段落、许可及采用差异；当前source状态待核。计划中证明路线和教学组织原创，不转载外部内容。当前没有新正文、答案、终审、构建或视觉通过状态。

## 本次读取文件身份

以下绑定比较基线，不是下一批最终输入清单；读取范围如前述，hash清单不意味着所列文件全部重新终审。

- `manuscript/foundations/natural_numbers.md` — `709c9ebf1f580c8bf7af17b494ecd07505dd33f65ccfe49482675fe7712880f3`
- `manuscript/foundations/natural_numbers_answers.md` — `402eeac5b267f46d22aebb06979d5d9a511e1a3b5e4b1cf67329c58e149dc84a`
- `manuscript/foundations/natural_order.md` — `4ad8e874bedda7f4c15739fd47344903ec71bd9a5b538c71bde0f9827b091435`
- `manuscript/foundations/natural_order_answers.md` — `ba046797e6a2ebf8b06cf1795fb6a1b03f92922e0e4caaf98f3a4d5d58c0f1d8`
- `manuscript/foundations/finite_sums.md` — `ea736adc9c09e27a9443cd24a11af4c3a1f1fcad72824a8f7430b3a4b670ea23`
- `manuscript/foundations/finite_sums_answers.md` — `127a6dd135315f2ccf2f9e4931e0e0c5f8c3a4adfb511b4f962cd70f552b4704`
- `manuscript/foundations/rational_powers.md` — `581010522535b41a771d0dd920531b37669b379ea64ce6001028620988bb3ee2`
- `manuscript/foundations/rational_powers_answers.md` — `fe64ec1b757dedb07583460db31afe240c9a1c0845c78a10603787ba2acef102`
- `manuscript/foundations/functions_bijections.md` — `b8eea358d984c1a13e27b83d24c872ae8f6ef1ca966fd1159788860cb35b79db`
- `manuscript/foundations/functions_inverse.md` — `28ffc4f4746286d1407bbe873d9e508d81e7ca82393c76cbf818131e819b9270`
- `manuscript/foundations/real_plane_affine.md` — `109fca79b231763511ec4142ef83cb09910f9fe43432de277d1cee3a78d69383`
- `data/msc_taxonomy.json` — `472a0c2369b943772b0527eda596660cda5fb9fd605c8d1571ff4cb537f13572`
- `data/catalog_titles_zh.json` — `00cae1c8d29e28d4d84a1fcfd2f54313abd7fdc5c11cd2ba79b061f0796d59d7`
- `data/production/sections.json` — `dfa0a63640a53dbb3f8f6998de9441a8bb9844cc09bee1157c9e83a39ff1ed6b`
- `research/production/sets_inclusion_operations_plan.md` — `7366227d397982ca4478f18ca51ff9decc66e488a83ca5b4711639ec6c79c66c`
