## 基础单元 B4.3 数列比较、夹逼与单调收敛 {#seqorder-unit}

**学习目标与位置。** 已经知道怎样检验一个指定的极限，以及收敛列的四则规律。现在先证明极限怎样保留比较，再证明一种不必预先猜出极限的存在定理：非减且有上界的实数列必收敛。关键依据是已经构造的实数上确界性质。主归属第242章40A05“级数与数列的收敛与发散”，交叉26A03与97I30；本单元不引入无穷级数、连续函数或柯西判据。

**精确先修。** 使用[函数及唯一输出](#fun-definition)、[条件子集](#fun-sets)、[已采用的归纳](#b1-induction)、[固定更新递归原则](#b1-recursion-principle)、[自然数序](#ord-definition)、[自然全序](#ord-trichotomy)、[自然加法保序](#ord-addition-order)、[合法自然差](#sub-definition)、[自然嵌入](#realarch-embedding)及[自然数的实数界](#realarch-natural-bound)。实数部分使用[上确界构造](#cut-supremum)、[该性质在同一有序域中的保留](#cutdiv-complete-field)、[序平移](#cutgroup-translation)、[取反与差](#cutgroup-negation-subtraction)、[实数乘法比较](#cutring-multiplication-order)、[商及乘回](#cutdiv-definition)、[非零系数方程](#cutdiv-equations)、[正倒数反序](#cutdiv-order)、[绝对值及双侧界](#realabs-definition-bounds)、[绝对值乘积与三角](#realabs-products-triangle)。数列接口为[定义与准确否定](#seq-definition)、[唯一性](#seq-uniqueness)、[常数与倒数例](#seq-basic-limits)、[有限改动与交替例](#seq-tails)、[收敛列有界](#seqlaw-bounded)、[线性及绝对值规律](#seqlaw-linear-absolute)。

**对象与记号。** 指标属于 $\mathbb N=\{0,1,\ldots\}$；实数数列是函数 $\mathbb N\to\mathbb R$。$a_n,b_n,x_n,L,\varepsilon$ 为实数；$\nu(n)$ 才是自然指标的实数嵌入。自然指标的较大者写 $\max_{\mathbb N}$，多于两个指标时重复取两个数的较大者。数字常量表示有理数的实数像。沿用
$$
b_n=\frac1{\nu(n)+1}>0,\qquad b_n\longrightarrow0.
$$
实数区间 $[\alpha,\beta]$ 表示条件子集 $\{x\in\mathbb R:\alpha\le x\le\beta\}$，使用时说明端点次序。

### 1. 最终比较怎样传给极限 {#seqorder-comparison}

称“最终 $a_n\le x_n$”，是指存在自然数 $N_0$，使每个 $n\ge N_0$ 都有该比较。早期的项可以不满足。

先记录严格误差的写法。对实数 $z,L$ 和 $\varepsilon>0$，
$$
|z-L|<\varepsilon
\quad\Longleftrightarrow\quad
L-\varepsilon<z<L+\varepsilon.
$$
正向由 $-|z-L|\le z-L\le|z-L|$ 得两侧严格界。反向若 $z-L\ge0$，绝对值为 $z-L<\varepsilon$；若 $z-L<0$，左侧严格界给 $-(z-L)<\varepsilon$，也就是所需绝对值界。两支穷尽，不能把弱不等式未经核对换成严格不等式。

**命题 SO1。** 若 $a_n\to A$、$x_n\to B$，且最终 $a_n\le x_n$，则 $A\le B$。特别地，最终非负的收敛列极限非负；最终属于闭区间 $[\alpha,\beta]$ 的收敛列，极限仍属于该区间。

**证明。** 反设 $A>B$。令
$$
\delta=\frac{A-B}{3}>0.
$$
分母三正，乘回给 $A-B=3\delta$，所以
$$
(A-\delta)-(B+\delta)=\delta>0.
$$
分别按误差 $\delta$ 取两列的阈值 $N_a,N_x$。再取最终比较的起点 $N_0$，令
$$
N=\max_{\mathbb N}\bigl(N_0,\max_{\mathbb N}(N_a,N_x)\bigr).
$$
在指标 $n=N$，三个尾部条件同时成立，于是
$$
a_N>A-\delta>B+\delta>x_N,
$$
与 $a_N\le x_N$ 矛盾。故 $A\le B$。

对最终非负列，把零常数列放在比较左侧即可。若 $\alpha\le a_n\le\beta$ 最终成立，且 $\alpha\le\beta$，分别与两常数列比较，得到 $\alpha\le A\le\beta$。SO1证毕。

**严格比较未必保留。** 对每个 $n$，有 $0<b_n$，但两列都趋零。因此从逐项严格比较只能一般性地推出极限的弱比较。

**极限与固定边界有间隔时。** 若 $a_n\to A$ 且 $A<c$，取 $\varepsilon=(c-A)/2>0$。误差尾部满足
$$
a_n<A+\varepsilon<c;
$$
第二步因为 $c-(A+\varepsilon)=\varepsilon>0$。同理，若 $A>c$，取 $\varepsilon=(A-c)/2$ 得最终 $a_n>c$。极限等于边界时不能使用这个正间隔。

### 2. 夹逼与可检验的误差界 {#seqorder-squeeze}

**命题 SO2。** 给三个实数数列，若最终
$$
a_n\le x_n\le c_n,
$$
且 $a_n\to L$、$c_n\to L$，则 $x_n\to L$。

**证明。** 任给 $\varepsilon>0$，分别取两端误差阈值，再与比较起点取共同最大值 $N$。对任意 $n\ge N$，
$$
L-\varepsilon<a_n\le x_n\le c_n<L+\varepsilon.
$$
上一节的严格误差等价给 $|x_n-L|<\varepsilon$。这正是收敛定义，证明中未先假定中间列收敛。

**误差控制的形式。** 若 $e_n\to0$ 且最终 $|x_n-L|\le e_n$，则 $x_n\to L$。因为该比较同时保证尾部 $e_n\ge0$；对任意 $\varepsilon>0$，在两个条件的共同尾部，
$$
|x_n-L|\le e_n=|e_n|<\varepsilon.
$$
这证明推广，不要求早期误差界成立。

例如固定 $C\ge0$，若最终
$$
|x_n-L|\le\frac{C}{\nu(n)+1}=Cb_n,
$$
则由常数倍规律，右端趋零，故 $x_n\to L$。其中乘回可核商与 $Cb_n$ 相同。$C=0$ 时尾部误差为零，说明最终等于 $L$，不需要除以 $C$。

**有界列乘趋零列。** 假设 $|u_n|\le M$ 对所有 $n$ 成立，$M\ge0$，且 $v_n\to0$。不要求 $u_n$ 收敛。绝对值乘积及非负乘法保序给
$$
0\le |u_nv_n|=|u_n||v_n|\le M|v_n|.
$$
绝对值规律给 $|v_n|\to0$，常数倍规律给 $M|v_n|\to0$。误差控制应用于乘积列与目标零，得到 $u_nv_n\to0$。$M=0$ 包含在内；此时积恒为零。这里没有把只针对两个收敛因子的乘积定理错误用于可能不收敛的 $u$。

### 3. 单调、全指标比较与下确界 {#seqorder-monotone-bounds}

称数列**非减**，如果对每个自然数 $n$ 有 $a_n\le a_{n+1}$；称其**非增**，如果对每个 $n$ 有 $a_{n+1}\le a_n$。满足其中之一称为**单调**。常数列同时满足两种条件；单调一词在这里不要求严格比较。

**命题 SO3。** 非减列对任意 $m\le n$ 都满足 $a_m\le a_n$；非增列满足反向比较。因此非减列有下界 $a_0$，非增列有上界 $a_0$。此外，每个非空且有下界的实数子集 $S$ 都有唯一最大下界，可记为
$$
\inf S=-\sup(-S),\qquad -S=\{-x:x\in S\}.
$$

**从相邻到任意指标。** 固定 $m$，对自然数 $r$ 归纳证明 $a_m\le a_{m+r}$。零步是自反性。若比较到 $m+r$ 成立，再由非减性
$$
a_m\le a_{m+r}\le a_{m+r+1},
$$
得到后继步。若 $m\le n$，合法自然差给 $r$ 满足 $m+r=n$，故所需比较成立。这里不引入负指标。

若原列非增，则 $-a_n$ 非减；刚证结论给 $-a_m\le-a_n$，取反反序得到 $a_n\le a_m$。取 $m=0$ 就给所述单边界。

**从上确界构造下确界。** 一个实数 $\ell$ 是 $S$ 的下界，意思是每个 $x\in S$ 都满足 $\ell\le x$。取反反序使 $-\ell$ 为 $-S$ 的上界。$S$ 非空给 $-S$ 非空，所以已证上确界性质允许定义
$$
U=\sup(-S),\qquad I=-U.
$$
任意 $x\in S$ 都有 $-x\in -S$，故 $-x\le U$，取反得 $I\le x$。所以 $I$ 是下界。若 $d$ 是任一下界，则 $-d$ 为 $-S$ 的上界；上确界最小性给 $U\le-d$，取反得 $d\le I$。因此 $I$ 是最大下界。若有两个最大下界，分别不大于对方，反对称使它们相等。SO3证毕。

**单边界与绝对值界。** 非减列若还有上界 $U$，则 $a_0\le a_n\le U$。取 $M=|a_0|+|U|\ge0$，有
$$
-M\le-|a_0|\le a_0\le a_n\le U\le|U|\le M,
$$
所以 $|a_n|\le M$。非增列若有下界 $\ell$，同理可取 $M=|\ell|+|a_0|$。上界本身可以为负；不能未经核验就把它当作非负绝对值界。

### 4. 上确界为什么给出单调列的极限 {#seqorder-monotone-convergence}

**命题 SO4（单调收敛）。** 非减且有实数上界的数列收敛，其极限为项的集合的上确界。非增且有实数下界的数列收敛，其极限为项的集合的下确界。因此，单调实数列收敛当且仅当有界。

**非减情形。** 形成条件子集
$$
S=\{x\in\mathbb R:\text{存在 }n\in\mathbb N\text{ 使 }x=a_n\}.
$$
$a_0\in S$，故非空；数列给定的上界也是 $S$ 的上界。因此实数上确界性质给 $L=\sup S$。特别地，全部 $a_n\le L$。

任给 $\varepsilon>0$。因为 $L-\varepsilon<L$，它不能仍是 $S$ 的上界：否则最小上界性给 $L\le L-\varepsilon$，矛盾。于是存在某个 $x\in S$ 满足 $x>L-\varepsilon$；成员条件再给自然数 $N$ 使 $x=a_N$。这里从一个存在的集合成员取得一个指标，不构造一系列任意选择。

对每个 $n\ge N$，SO3给
$$
L-\varepsilon<a_N\le a_n\le L.
$$
所以
$$
|a_n-L|=L-a_n<\varepsilon.
$$
阈值 $N$ 依赖给定误差，但此后每个指标同时满足界。非减情形完成，上确界不必是任何一项。

**非增情形。** 若 $\ell$ 是下界，则相反列 $c_n=-a_n$ 非减且有上界 $-\ell$。刚证结论给
$$
c_n\longrightarrow U=\sup(-S).
$$
常数倍规律给 $-c_n\to-U$，而 $-c_n=a_n$。SO3已证明 $-U=\inf S$，所以原列收敛到下确界。这里没有把递减情形当作未经证明的“同理”。

若单调列有界，则两方向分别具有所需单边界，因而收敛。反过来，收敛列有界已由SA1证明，故等价成立。SO4证毕。

**两个条件的用途。** $0/1$ 交替列有界却不收敛，说明不能删单调条件。自然嵌入列 $\nu(n)$ 非减而无实数上界；若它收敛，SA1会给绝对值界，进而给上界，与自然数界定理矛盾。因此不能删对应的单边界。本单元不把这种不收敛写成尚未定义的无穷极限。

单调收敛首次允许我们在不知道具体极限值时证明它存在。随后若能由递归关系辨认这个值，辨认步骤仍须使用已经证明的数列规则；仅解一个候选方程不等于证明数列收敛。

### 5. 课后题 {#seqorder-exercises}

#### 题1：最终比较与严格性的边界 {#seqorder-q01}

设 $a_n\to A$、$x_n\to B$，且存在 $N_0$ 使全部 $n\ge N_0$ 有 $a_n\le x_n$。完整证明 $A\le B$。再证明闭区间 $[\alpha,\beta]$（$\alpha\le\beta$）的最终成员条件传给极限，并给逐项严格比较却极限相等的例子。[完整解答](#seqorder-a01)

#### 题2：极限与固定边界之间的间隔 {#seqorder-q02}

设 $a_n\to L$、$L<c$，证明最终 $a_n<c$；再证明 $L>c$ 的相应结论。用 $b_n=1/(\nu(n)+1)$ 及 $-b_n$ 说明把前提分别改成 $L\le c$ 或 $L\ge c$ 后，严格结论可能失败。[完整解答](#seqorder-a02)

#### 题3：夹逼需要同一个极限 {#seqorder-q03}

设最终 $a_n\le x_n\le c_n$，且两端都趋 $L$，完整证明 $x_n\to L$。若只知道两端有界，是否足够？用已定义的交替列给出反例，并证明其有界与不收敛。[完整解答](#seqorder-a03)

#### 题4：误差控制与不收敛因子的乘积 {#seqorder-q04}

设 $C\ge0$，且最终 $|x_n-L|\le C/(\nu(n)+1)$，证明 $x_n\to L$，单列 $C=0$。令 $r_n\in\{0,1\}$ 为除以二余数的实数像，计算 $3+r_n/(\nu(n)+1)$ 的极限。另证有界实数列 $u$ 与趋零实数列 $v$ 的乘积趋零，不假定 $u$ 收敛。[完整解答](#seqorder-a04)

#### 题5：相邻比较怎样覆盖任意两个指标 {#seqorder-q05}

从非减的相邻定义出发，证明任意自然数 $m\le n$ 都有 $a_m\le a_n$；写明归纳对象及自然差的条件。证明非增情形并指出各自的初项单边界。举例说明不能把结论统一改成严格比较。[完整解答](#seqorder-a05)

#### 题6：下确界由取反构造 {#seqorder-q06}

对非空有下界的实数集 $S$，完整证明 $\inf S=-\sup(-S)$，包括唯一性。对
$$
S=\left\{2+\frac1{\nu(n)+1}:n\in\mathbb N\right\}
$$
证明下确界为二且未被任何成员取得；每个大于二的候选都须给出不是下界的理由。[完整解答](#seqorder-a06)

#### 题7：上确界收敛与不被取得的极限 {#seqorder-q07}

证明非减有上界列收敛到上确界，并通过相反列完整处理非增有下界的情形。对 $a_n=1-1/(\nu(n)+1)$，证明非减、有上界、极限为一，且任何一项都不等于该上确界。[完整解答](#seqorder-a07)

#### 题8：先证明递归列收敛，再求它的极限 {#seqorder-q08}

设 $X=[0,1]$，给规则 $T(x)=(x+2)/3$。先证明它是函数 $X\to X$，然后从 $a_0=0$ 按固定更新递归定义 $a_{n+1}=T(a_n)$。证明该列非减且有界，故存在极限 $A$。再用尾移、线性规律与唯一性求出 $A$。不得只解不动点方程就断言收敛，也不使用等比级数或连续函数定理。[完整解答](#seqorder-a08)

**来源与范围。** 标准命题的公开来源条件、实际缓存读取位置及许可见[本批来源记录](#real-sequences-order-subsequences-sources)。本单元在既有上确界构造上独立证明数列结果；源书留下的递减情形在这里补全。没有把单调收敛提前当成柯西判据或一般紧致性的同义名称。
