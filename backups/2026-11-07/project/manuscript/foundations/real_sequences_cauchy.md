## 基础单元 B4.5 实数柯西条件与收敛判据 {#cauchy-unit}

**位置与目标。** 本单元续第242章40A05，交叉26A03、97I30。任务是不用预先知道极限值，判断一个实数数列是否收敛。这里只证明实数数列的柯西判据，不建立一般度量空间、柯西列商构造或无穷级数；该章仍仅部分展开。

**精确先修。** 使用[数列与收敛的量词](#seq-definition)、[极限唯一](#seq-uniqueness)、[倒数基本例](#seq-basic-limits)、[有限前缀界](#seqlaw-bounded)、[夹逼误差版本](#seqorder-squeeze)、[严格子列指标增长](#subseq-indices)与[实数数列的博尔查诺—魏尔斯特拉斯定理](#subseq-bolzano-weierstrass)。这些完整证明是逻辑先修，不能只用定理名称替代其条件与论证。实数方面使用[绝对值三角不等式](#realabs-products-triangle)、[自然数嵌入及运算相容](#realarch-embedding)、[严格自然数界](#realarch-natural-bound)、[正倒数反序](#cutdiv-order)、[平方的次序](#realsqrt-square-order)、[平方根函数](#realsqrt-function)。选读题8还用[自然子集最小元](#ord-a07)、[非零自然数的唯一前驱](#ord-predecessor)、[二的无理根](#realsqrt-equations-irrational)、[有理数到实数的除法相容](#cutdiv-definition)。不以本单元待证结论反过来证明BW。

**记号。** $\mathbb N=\{0,1,2,\ldots\}$；$m,n,N,j$均为自然数。$\nu:\mathbb N\to\mathbb R$是前文已建保序嵌入，$i:\mathbb Q\to\mathbb R$是有理数嵌入，$\eta:\mathbb N\to\mathbb Q$满足$\nu=i\circ\eta$。数列$a:\mathbb N\to\mathbb R$的值写成$a_n$。误差$\varepsilon$是正实数，指标比较仍在自然数中进行。

### 1. 两个尾项都要受同一个起点控制 {#cauchy-definition}

**入口。** 若不知道一组逐次近似的最终值，就不能先把“与最终值的距离”代入计算。但可以比较两个近似值的距离。只比较相邻两次仍不够：每次走得小，不保证长时间累计走得小。需要约束起点以后的任意两项，允许它们相隔很远。

**定义。** 称实数列$a$为柯西列，当且仅当

$$
\begin{gathered}
\forall\varepsilon>0\ \exists N\in\mathbb N\ \forall m,n\in\mathbb N,\\
m\ge N\ \text{且}\ n\ge N\Longrightarrow |a_m-a_n|<\varepsilon.
\end{gathered}
$$

先任给$\varepsilon$，再确定一个$N$，然后才任取$m,n$。同一个$N$必须服务于所有这样的有序指标对，不能看到$m,n$以后重新选择起点。定义没有出现未知的极限值。

**否定。** 不是柯西列的准确含义是

$$
\begin{gathered}
\exists\varepsilon_0>0\ \forall N\in\mathbb N\ \exists m,n\in\mathbb N,\\
m\ge N,\quad n\ge N,\quad |a_m-a_n|\ge\varepsilon_0.
\end{gathered}
$$

依据是逐层否定量词，并将严格不等式的否定用实数全序写成弱反向不等式。误差$\varepsilon_0$固定，坏指标对可以依赖$N$。取$m=n$所得零距离符合定义，但定义要求的还有所有不同指标对；用对角线上的等式不能证明全称命题。

**例1：常数列。** 若$a_n=c$对每个$n$成立，则任给$\varepsilon>0$取$N=0$。任取$m,n\ge0$，有$|a_m-a_n|=|c-c|=0<\varepsilon$，故为柯西列。

**例2：两值交替。** 设$r_n$是$n$除以2的余数，令$a_n=\nu(r_n)$。任给$N$，取$m=2N$、$n=2N+1$。自然数加法保序给$2N\ge N$，进而$n\ge N$。商余唯一性给$r_{2N}=0,r_{2N+1}=1$，故距离为$|0-1|=1$。用固定$\varepsilon_0=1$满足否定，得到不是柯西列。该列仍满足$|a_n|\le1$，所以有界不能替代柯西条件。

### 2. 收敛给出柯西性，柯西性给出全列界 {#cauchy-necessary-bounded}

**命题 CY1。** 若$a_n\to L\in\mathbb R$，则$a$为柯西列。

**证明。** 任给$\varepsilon>0$。实数2为正，故$\varepsilon/2>0$。由收敛定义取得自然数$N$，使每个$t\ge N$满足$|a_t-L|<\varepsilon/2$。现在任取$m,n\ge N$。两者分别可代入同一个尾项结论。由加法群律，$a_m-a_n=(a_m-L)+(L-a_n)$；由三角不等式及绝对值取反不变，

$$
|a_m-a_n|\le |a_m-L|+|L-a_n|
=|a_m-L|+|a_n-L|<\varepsilon/2+\varepsilon/2=\varepsilon.
$$

最后严格不等式由实数加法保严格序得到。这个$N$与随后任取的$m,n$无关，恰好满足定义。证毕。

**命题 CY2。** 每个实数柯西列都有一个非负实数$M$，使所有$n\in\mathbb N$满足$|a_n|\le M$。

**证明。** 在柯西定义中取误差1，取得$N$。对于任意$n\ge N$，另一个指标可以合法地取$N$本身，因此$|a_n-a_N|<1$。由三角不等式，

$$
|a_n|=|(a_n-a_N)+a_N|\le |a_n-a_N|+|a_N|<1+|a_N|.
$$

这还没有控制早期项。由[有限前缀界的已证构造](#seqlaw-bounded)，存在非负实数$C_N$使$0\le n<N$时$|a_n|\le C_N$；该构造对$N=0$给$C_0=0$，不要求空集合有最大元。取

$$
M=C_N+1+|a_N|.
$$

各加数非负且1正，所以$M>0$。若$n<N$，则$|a_n|\le C_N\le M$。若$N\le n$，上式尾界及$C_N\ge0$给$|a_n|<1+|a_N|\le M$。自然全序保证两种情形穷尽。故同一个$M$控制全部项，包括$N=0$时没有早期项的情形。证毕。

**常见误解。** CY1的逆向尚未证明；CY2的逆向已被交替例否定。不能把两个单向箭头拼成“有界所以收敛”。

### 3. 由一个收敛子列确定整列 {#cauchy-criterion}

**命题 CY3。** 若实数列$a$为柯西列，并且存在严格递增函数$k:\mathbb N\to\mathbb N$使$a_{k_j}\to L\in\mathbb R$，则$a_n\to L$。

**证明。** 任给$\varepsilon>0$。柯西性给起点$N$，使$m,n\ge N$时$|a_m-a_n|<\varepsilon/2$。子列收敛给起点$J$，使$j\ge J$时$|a_{k_j}-L|<\varepsilon/2$。

令$j_0=\max(N,J)$，这是前文已定义的两个自然数最大值。由[严格指标增长](#subseq-indices)，$k_j\ge j$对每个$j$成立，所以

$$
k_{j_0}\ge j_0\ge N,\qquad j_0\ge J.
$$

固定这一个子列项$a_{k_{j_0}}$，再任取原列指标$n\ge N$。柯西条件可用于$n,k_{j_0}$这一对；子列条件可用于$j_0$。于是

$$
\begin{aligned}
|a_n-L|&=|(a_n-a_{k_{j_0}})+(a_{k_{j_0}}-L)|\\
&\le |a_n-a_{k_{j_0}}|+|a_{k_{j_0}}-L|\\
&<\varepsilon/2+\varepsilon/2=\varepsilon.
\end{aligned}
$$

因此每个$n\ge N$均满足误差要求。固定的$j_0$可以依赖$\varepsilon$；它不需要依赖随后任取的$n$。原列收敛到$L$。证毕。

**定理 CY4：实数柯西判据。** 对任意全函数$a:\mathbb N\to\mathbb R$，以下两条件等价：存在实数$L$使$a_n\to L$；$a$是柯西列。

**证明。** 第一条件推出第二条件已经由CY1证明。反向假设$a$为柯西列。CY2给全列界，由[实数数列BW定理](#subseq-bolzano-weierstrass)取得严格指标$k$和实数$L$，使$a_{k_j}\to L$。CY3随即推出$a_n\to L$。两方向都已建立。极限的唯一性来自前文SL2，而不是另一个未经证明的选择。证毕。

**完备性用在何处。** BW的证明通过单调子列和实数上确界性质取得实数极限；这正是反向箭头所需的存在性。我们没有把柯西收敛当作新的公理，再用它证明自身。一个只有有理项的列也可以看作实数列，但所得实数极限未必位于有理数像$i(\mathbb Q)$中；选读题8给出完整例子。这里不定义一般空间的完备性。

**有限改动。** 若$a,b$在某个$K$以后逐项相等，则$a$是柯西列当且仅当$b$是柯西列。证明一个方向：给定$a$的误差起点$N$，取$H=\max(N,K)$。任取$m,n\ge H$，有$b_m=a_m,b_n=a_n$，故$|b_m-b_n|<\varepsilon$。反方向交换$a,b$重复同一步。没有把可能很大的早期项删掉，也不声称整列界保持原值。

### 4. 相邻步长趋于零仍可能越走越远 {#cauchy-adjacent}

令$x_n=\sqrt{\nu(n)+1}$。由于$\nu(n)\ge0$，根号内至少为1，每项存在且$x_n\ge1$。平方根保序和$\nu(n+1)=\nu(n)+1$给$x_{n+1}>x_n$。平方的差展开为

$$
(x_{n+1}-x_n)(x_{n+1}+x_n)=x_{n+1}^2-x_n^2
=(\nu(n)+2)-(\nu(n)+1)=1.
$$

分母$x_{n+1}+x_n\ge2>0$，故可除，得到

$$
0<x_{n+1}-x_n=\frac1{x_{n+1}+x_n}\le\frac1{x_n}.
$$

**先证无界。** 任给非负实数$B$，由实数阿基米德性质选$N$使$\nu(N)>B^2$。则$x_N^2=\nu(N)+1>B^2$，因$x_N,B$均非负，平方保序反映大小，推出$x_N>B$。不存在控制所有项的非负界；CY2因此排除柯西性。

**再证邻差趋零。** 任给$\varepsilon>0$，令$t=1/\varepsilon>0$。取$N$使$\nu(N)>t^2$。对于任意$n\ge N$，嵌入保序给$\nu(n)\ge\nu(N)>t^2$，因而$x_n^2>t^2$、$x_n>t>0$。正数倒数反序给$1/x_n<1/t=\varepsilon$。结合已证邻差界，

$$
|x_{n+1}-x_n|=x_{n+1}-x_n\le1/x_n<\varepsilon.
$$

所以邻差数列趋于零，但原列不是柯西列。这里没有使用对数、积分或调和级数。关键区别是相邻差只检验$m=n+1$这一部分指标对，而柯西条件要求所有足够靠后的指标对。

### 5. 课后题 {#cauchy-exercises}

#### 题1：量词与坏指标对 {#cauchy-q01}

写出柯西条件的否定。有人说“任给$m,n$，取$N>m,n$，条件就成立，所以所有数列均柯西”，指出错误。对于$a_n=\nu(n)$，给一个固定正误差，并对每个$N$构造违反条件的指标对。

[查看完整解答](#cauchy-a01)

#### 题2：基本例的直接阈值 {#cauchy-q02}

不用CY1，直接证明$b_n=1/(\nu(n)+1)$是柯西列。要求起点对全部指标对有效，说明分母与严格不等式。

[查看完整解答](#cauchy-a02)

#### 题3：有界不能代替柯西 {#cauchy-q03}

令$r_n$是$n$除以2的余数，$a_n=3\nu(r_n)-1$。求其两个可能值、一个全列界，并用柯西条件的否定证明它不是柯西列。

[查看完整解答](#cauchy-a03)

#### 题4：早期项、空前缀与界 {#cauchy-q04}

假定$|a_m-a_n|<1$对$m,n\ge N$成立，且$C_N\ge0$控制前$N$项绝对值。证明$C_N+1+|a_N|$控制全列。分别解释$N=0$与只有尾界而遗漏前缀时的问题，并给一个反例说明尾界不自动控制早期项。

[查看完整解答](#cauchy-a04)

#### 题5：有限改动与任意固定尾移 {#cauchy-q05}

固定$K\in\mathbb N$，令$b_j=a_{j+K}$。证明$a$是柯西列当且仅当$b$是柯西列。反向须合法构造自然差，不得使用负指标。

[查看完整解答](#cauchy-a05)

#### 题6：一个子列还不够 {#cauchy-q06}

给出有收敛子列但整列不收敛的例子。随后证明：若另加整列柯西这一条件，任何一个收敛子列的极限就是整列极限。解释共同阈值中为什么要比较子列输入$j$与原列输入$k_j$。

[查看完整解答](#cauchy-a06)

#### 题7：柯西条件下的和与常数倍 {#cauchy-q07}

设$a,b$为实数柯西列，$c$为固定实数。直接从双指标定义证明$a+b$及$ca$均为柯西列，不先使用CY4转成收敛。常数倍证明须单独处理$c=0$。

[查看完整解答](#cauchy-a07)

#### 题8：选读——极限不一定留在有理数中 {#cauchy-q08}

令$\alpha=\sqrt2$。对每个$n$，记$d_n=\nu(n)+1$，在自然数集合

$$
E_n=\{k\in\mathbb N:\alpha d_n<\nu(k)\}
$$

中取最小元$k_n$。先证明它存在且非零，写$k_n=t_n+1$，并定义有理数

$$
q_n=\frac{\eta(t_n)}{\eta(n)+1}.
$$

证明$0\le\alpha-i(q_n)<1/d_n$；由此证明实数列$i(q_n)$收敛且为柯西列，但不存在$q\in\mathbb Q$使$i(q_n)\to i(q)$。最后解释为什么这不违背CY4。

[查看完整解答](#cauchy-a08)

**来源与边界。** 柯西定义、实数判据的标准条件与有限前缀要求对照Jiří Lebl《Basic Analysis I》6.3固定提交的Cauchy sequences节；本次实际读取及原缓存身份见`research/production/real_sequences_cauchy_sources_2026-11-05.json`。来源以正整数起始且用上、下极限证明反向，本书从零起始，独立通过已证BW及一个子列完成证明。题目与解答独立编写，不搬运源书练习。全部一般结论由证明承担，没有用有限数值测试替代。
