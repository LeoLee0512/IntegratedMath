# 一次不等式、有理区间与绝对值条件来源审计（2026-10-29）

本记录覆盖B2.7、B2.8，正文来源锚为 `linear-inequalities-sources`。它审核来源与条件，不代替当前正文、16题全解的独立数学和教学审阅，也不授予整章或整部分完成。

## 访问证据与正式化边界

前期预备时已实际发出15次公开请求，全部HTTP 200。正式化时没有重新抓取，JSON逐项保留真实原访问时间、URL、响应字节数与SHA-256；`promotion`时间仅表示把临时审计转入正式来源记录。原始临时计划的SHA也保留。

网络工作前独立查询：首次state为unknown，再次查询为current/enforced/running后才经正常代理与TLS验证抓取。没有认证、凭据或远程Git操作。公开第三方全文只在 `/tmp`，不进入仓库或伴生包。

## 两个独立来源系列

### INEQ-OPENSTAX：Elementary Algebra 2e; Intermediate Algebra 2e

版本：osbooks-prealgebra-bundle commit ad40c7e3c9a909cde81a24c526f52fe26a51fb14。许可：CC-BY-NC-SA-4.0。只核事实条件和证明边界，不复制例题题干、连续段落、表格或图像；NC/SA许可不误写CC BY。

Elementary Algebra 2e作者：Lynn Marecek、MaryAnne Anthony-Smith、Andrea Honeycutt Mathis。
Intermediate Algebra 2e作者：Lynn Marecek、Andrea Honeycutt Mathis。

- [m82470：解与开闭端点](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m82470/index.cnxml#L66)（modules/m82470/index.cnxml，行66–81）：严格大于排除端点，非严格大于包含端点；原文实数数轴图不能直接视作全体有理数图。
- [m81366：加减、正负乘除性质](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81366/index.cnxml#L388)（modules/m81366/index.cnxml，行388–435）：同加减保向；正倍乘除保向、负倍乘除反向。教材列性质及实例，本书须用RO4/RO6/RO8作双向证明，并补a=0分支。
- [m81367：compound inequalities](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81367/index.cnxml#L40)（modules/m81367/index.cnxml，行40–50）：and要求两条件同时成立；or要求至少一个成立，不能把or误作排他或。集合交并符号如未教须先定义。
- [m81426：绝对值非负](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81426/index.cnxml#L54)（modules/m81426/index.cnxml，行54–58）：绝对值≥0，不是总严格为正。采用前文RAB1/RAB7的代数定义和距离，不能用未建立的实数数轴作证明。
- [m81426：负值与零值例子的措辞核查](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81426/index.cnxml#L108)（modules/m81426/index.cnxml，行108–146）：行122 incorrectly says always positive；同节57–58明为非负，128–146把零等式归为唯一解零。记为局部措辞错误，不能照用，r=0必须单列。
- [m81426：fs-id1167835331002](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81426/index.cnxml#L433)（modules/m81426/index.cnxml，行433–439）：正实数半径时小于/不大于绝对值界分别转为严格/非严格两侧界，连接词为且。书稿须证明两个方向并另外处理有理r≤0。
- [m81426：fs-id1167834423855](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81426/index.cnxml#L603)（modules/m81426/index.cnxml，行603–608）：正实数半径时大于/不小于条件转为两侧外部，连接词为或；不含/包含两个边界。书稿补r=0与r<0，不能直接套只声明正半径的来源公式。
- [m81426：抽样检查边界](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81426/index.cnxml#L438)（modules/m81426/index.cnxml，行438–439）：原文明确选若干测试点不是complete check；本书一般证明与有限核算分开。

### INEQ-MATHLIB：mathlib ordered-field inequalities, absolute values and generic intervals

版本：mathlib4 v4.24.0。许可：Apache-2.0。源码阅读与逻辑条件对照；不复制实现，未编译Lean也未形式化本书。

逐文件作者见JSON及原始文件头；包括Damiano Testa、Yuyang Zhao、Robert Y. Lewis、Jeremy Avigad、Leonardo de Moura、Mario Carneiro、Johannes Hölzl、Floris van Doorn、Johan Commelin。

- [GroupWithZero.inv_zero / inv_zero](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/GroupWithZero/Defs.lean#L199)（Mathlib/Algebra/GroupWithZero/Defs.lean，行199–212）：该库约定零的逆为零，除法按乘逆元总定义；本书把除零排除。因此只借用显式正/负除数的等价，不能把库中零除数计算带入书稿。
- [le_div_iff₀ / div_le_iff₀ / lt_div_iff₀ / div_lt_iff₀](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Order/GroupWithZero/Unbundled/Basic.lean#L1095)（Mathlib/Algebra/Order/GroupWithZero/Unbundled/Basic.lean，行1095–1109）：严格正除数条件下四种比较等价；源声明带显式0<c，不允许忽略符号。
- [div_le_iff_of_neg / le_div_iff_of_neg / div_lt_iff_of_neg / lt_div_iff_of_neg](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Order/Field/Basic.lean#L289)（Mathlib/Algebra/Order/Field/Basic.lean，行289–348）：有序域背景下c<0时比较方向反转；证明使用非零倒数与负因子反序。
- [Set.Ioo / Ico / Ioc / Icc / Iio / Iic / Ioi / Ici](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Order/Interval/Set/Defs.lean#L28)（Mathlib/Order/Interval/Set/Defs.lean，行28–76）：在任意预序类型α上按成员条件定义区间；取α=Q时是有理区间，不需要实数或完备性，∞只是无界记号。
- [mabs_le / le_mabs'，@[to_additive]](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Order/Group/Abs.lean#L59)（Mathlib/Algebra/Order/Group/Abs.lean，行59–63）：源直接写乘法版本，to_additive产生加法绝对值版本；对应|u|≤r iff −r≤u且u≤r，以及外侧析取。未运行Lean，不能声称已编译检验生成定理。
- [one_le_mabs，显式to_additive abs_nonneg](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Order/Group/Unbundled/Abs.lean#L102)（Mathlib/Algebra/Order/Group/Unbundled/Abs.lean，行102–107）：非负性生成声明用于交叉核查r负值情形；集合数系的前提仍由本书既有有理数证明提供。
- [le_mabs / lt_mabs，@[to_additive]](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Order/Group/Unbundled/Abs.lean#L191)（Mathlib/Algebra/Order/Group/Unbundled/Abs.lean，行191–199）：有序max对应r≤|u| iff r≤u或r≤−u，严格版本同理；外侧是析取，不是两条件同时满足。
- [mabs_eq_one / mabs_le_one / mabs_lt，@[to_additive]](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Order/Group/Unbundled/Abs.lean#L247)（Mathlib/Algebra/Order/Group/Unbundled/Abs.lean，行247–260）：对应|u|=0 iff u=0、|u|≤0 iff u=0、|u|<r iff −r<u且u<r；支持严格/非严格零界区别。

## 全部符号与边界分支

固定有理数a,b,c，在Q上解ax+b≤c或ax+b<c；t=(c−b)/a只在a≠0分支使用。

| 条件 | 非严格≤ | 严格< |
| --- | --- | --- |
| a>0 | x≤t | x<t |
| a<0 | x≥t | x>t |
| a=0 | b≤c时Q，否则空集 | b<c时Q，否则空集 |

对a,r∈Q，研究绝对值条件；以下所有区间均为Q中的集合。

| 半径 | 小于r | 不大于r | 等于r | 不小于r | 大于r |
| --- | --- | --- | --- | --- | --- |
| r<0 | 空集 | 空集 | 空集 | Q | Q |
| r=0 | 空集 | {a} | {a} | Q | Q中除a以外的元素 |
| r>0 | (a−r,a+r)_Q | [a−r,a+r]_Q | {a−r,a+r} | (−∞,a−r]_Q ∪ [a+r,+∞)_Q | (−∞,a−r)_Q ∪ (a+r,+∞)_Q |

若允许范围为D⊆Q，每项结果再与D取交。外侧使用“或”，内侧使用“且”；严格式与非严格式的端点分别检查。r=0不可被只针对正半径的来源公式省掉。

## 按本书先修独立复核的推理

1. 不等式问题连同D⊆Q及L,R:D→Q给出。解集为{x∈D:L(x)≤R(x)}等；等价要求同一D上逐输入双向。若给出的结果先在Q上求出，再与D取交；D空时所有解集为空。
2. 对ax+b≤c，先按RO4同减b；a>0用RO8保向、a<0用RO8反向、a=0直接判b≤c。严格版本将≤替换为<，但零系数仍必须判断b<c，不能沿用非严格条件。≥、>可先交换两侧，严格/非严格转换不改变端点含义。
3. 两边含未知数时合并为(a−d)x≤e−b等，先对新系数a−d分类，不根据原a的符号决定方向；任何除法都只在已证非零分支。
4. 定义[p,q]_Q={x∈Q:p≤x且x≤q}，其余三种组合按严格/非严格改写。p>q时均为空；p=q仅全闭区间为{p}，其余为空。单侧无界区间用x≤q等成员条件定义；±∞不是有理端点。
5. 首次定义S∩T={x:x∈S且x∈T}、S∪T={x:x∈S或x∈T}；或表示至少一边，可同时属于。每次交并结论以成员等价证明，不凭图像填色。
6. 令u=x−a。已有RAB3给|u|≤r iff −r≤u≤r；同加a得a−r≤x≤a+r。严格版本以u≥0或u<0的绝对值定义分支证明|u|<r iff −r<u<r，而不能只把符号机械替换。
7. 外部条件由全序和绝对值分支得|u|≥r iff u≤−r或u≥r，|u|>r iff u<−r或u>r。平移后是两条外侧射线的并；例如r>0时要求同时x≤a−r且x≥a+r反而无解，故连接词不可写且。
8. 先以|x−a|≥0处理r<0，五种关系见分支表；r=0由RAB1的零判据得内闭/等号为{a}，内严格为空，外非严格全Q，外严格Q\{a}；r>0再按端点得到正常内外区间。等号r>0为两点，r=0重合为一点，r<0无解。
9. RAB7的d(x,a)=|x−a|是有理数值距离；本批半径r∈Q。用“距离小于半径”描述相同条件，不借未写的实数完备性、连续线段、拓扑球或实距离空间定理。
10. 前文已有序律和绝对值双向界，这两单元应做明确复用、参数分支及解集教学，不重复构造有理数或把已证RAB3冒充新定理。

11. 实际B2.8还把|ax+b|与r的比较归约为距离条件：a=0先比较常数|b|与r；a≠0时令c=−b/a、ρ=r/|a|，RAB1给|a|>0，RAB4给|ax+b|=|a||x−c|，按正除数规则保持四种比较。负a也用正数|a|缩放，不误翻向；ρ正负零与r一致，最后与D取交。此为既有有理数定理的独立复核，不新增外部访问。

## 计算、权利与范围

预备审计实际采用Python Fraction对13122个一次式比较、3645个绝对值比较作精确交叉核算，均通过；输入为n/2（n从−4到4），含正负零与严格/非严格条件。这个有限检查核对分支表及边界，不替代任意有理数上的完整证明；正式化没有把它写成本批书稿测试或Lean编译。

OpenStax当前许可是CC BY-NC-SA4.0，不能误写CC BY；mathlib为Apache2。正文、证明组织、题答及图由本书独立编写，不复制来源题目、表格、连续段落、图或实现。已发现的OpenStax“绝对值总为正”局部措辞错误明确排除；mathlib把零逆定义为零的约定与本书禁止除零的约定分开。

分类保持第63部分97-XX、第528章97Hxx的97H30，97H20仅交叉；有理区间不赋予26A03、一般不等式或拓扑领域完成度。两个新增单元为第28、29单元，若题答实际全部存在则累计232基础题加绪论14题，共246题；正式计数与验收另核。0部分完成，push未到期。
