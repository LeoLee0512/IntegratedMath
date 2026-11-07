# 有限坐标向量线性组合：B单元固定写作接口

2026-11-05，作者/root/part1_pedagogy。承接`/tmp/finite-real-sums-draft/finite_real_sums_linear_combinations_plan.md`中B范围；这里只固定未来稿件接口，A实数和独立数学审未结束前不写正文。FRC已独立数学/教学通过，RFS教学通过、数学待审。所有文件仅/tmp，不改34冻结输入。

主归第84章15Axx/15A03（Vector spaces, linear dependence, rank, lineability）的有限坐标线性组合局部。仅定义与运算规则，不定义张成、基、维数、线性相关或矩阵；分类仍partial。

## 对象和先修

沿FRC公开采用函数集合背景，V_n={x:I_n→R}。n为每个向量的坐标数，m为向量项数；给系数表a:I_m→R及向量表v:I_m→V_n。v_k是V_n中的函数记录，其第j坐标(v_k)_j仅在k<m且j<n时有定义。

精确锚：frc-model、frc-operations、frc-additive-laws、frc-scalar-laws（含零结论）、frc-cancellation、frc-reindex；rfs-definition、rfs-prefix-table、rfs-linearity、rfs-concatenation、rfs-padding；fun-definition、fun-pairs、fc-equality、fc-composition；cutsigned-associative、cutsigned-signs、cutring-distributive；sum-indices、ord-successor-comparison。

## 固定定义和目标

令C(a,v)∈V_n逐坐标满足C(a,v)_j=Sum_R(k↦a_k(v_k)_j)。对固定j，括号中函数的域为I_m、目标R，合法且唯一；所得数随j给I_n→R函数。可在完成定义后把有限向量表达式Σ_(0≤k<m)a_kv_k作为此对象的记号，不把它误说成已经递归定义过的一般向量和。

- FLC1（flc-definition）：合法性、m0得到0_n、n0得到唯一空向量、m1/m2退回既有标量乘/二元向量加法。
- FLC2（flc-coefficients）：同向量表的系数逐项相加，C(a+b,v)=C(a,v)+C(b,v)，逐坐标先用实数分配再RFS3。
- FLC3（flc-scaling）：共同实数c缩放，C(ca,v)=cC(a,v)，另明确向量表cv:I_m→V_n后证明C(a,cv)=cC(a,v)；后一条须用实数交换结合，不靠未定义“向量乘法”。零系数表给零向量，零向量表亦给零。
- FLC4（flc-vector-addition）：同系数且同型向量表v,w逐项相加，C(a,v+w)=C(a,v)+C(a,w)，逐坐标分配和RFS3。
- FLC5（flc-concatenation）：系数表及向量表同步按相同切点拼接，固定j的加权实数表等于两段加权表拼接，由RFS4得组合相加；不用置换/换序。
- FLC6（flc-reindex）：固定坐标置换σ:I_n→I_n，每项变成Tσ(v_k)，证明C(a,Tσv)=Tσ(C(a,v))，对j把同一有限实数表的项逐点识别；不置换向量项k。

## 八题定稿任务

1. m2/n2：v0=(1,−1)、v1=(2,3)、a=(3,−2)，逐坐标得到(−1,−9)，核二元表达式相容。
2. m0/n3与m3/n0各自输入和输出、空系数表配非空向量项表非法、坐标长度混杂非法；两个零参数不可互换解释。
3. 任意同型系数a,b逐坐标完整证明FLC2，说明每个内层求和的类型。
4. 共同缩放两位置完整证明，具体c0和负c检查；零系数表/零向量表全长度证明。
5. 向量项逐点相加规则一般证明；v_k+w_k须同一V_n，不能把不同长度的向量表强配。
6. m2段与p1段同步拼接具体例并给一般证明，明确k是项索引、j是坐标索引以及切点局部自然差条件。
7. v0=(1,1)、v1=(2,2)，系数(2,0)/(0,1)不同却同组合(2,2)；另逐坐标说明任意系数的组合两坐标相同，故(1,0)无法获得。不把此计算提前命名成基或维数结论。
8. n3/m2、σ=(2,0,1)的数值检查及一般坐标重编号证明与逆恢复，强调操作j而非k，未证明任意项重排。

## 实际来源发现与阅读

实际访问固定Beezer原生GitHub src目录HTTP200后，目录明确列出section-LC.xml；随后该固定raw文件HTTP200。元数据在`/tmp/finite-linear-combinations-source-cache/requests.json`，原文缓存同目录。已实际读section-LC.xml第1–125行，核心采用范围为1–29的列向量线性组合定义及输入/输出类型说明；源例也实际看过，但不采用其数字或练习，以上8题独立设计。该源仍复数、1起索引，未给本书零项数/零坐标、坐标函数构造及全套公式证明。COPYING与bookinfo已在FRC实际核读，后续作者sourceJSON要绑定本次内容，不把此前阅读当新网络请求。

正文待A数学审通过后写，并使用A最终冻结hash；本文件不构成B完成或验收。

## 执行更新（不抹去最初待审条件）

RFS随后已独立数学/教学通过，正文冻结SHA297dab2fc25bb32819ba662960ddd550a324d2594c8bf7a4e082c7b3f5ff573e、答案SHA36ef43e22726ddec1cb2d79028272f284004a4aeadb3dc53620b0c15f3cb838f；root明确准许开写B。当前B正文与8解已全部完成在本目录，目标/题目保持本计划，待独立审阅，未注册或构建。
