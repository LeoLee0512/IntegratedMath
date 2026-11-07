## 基础单元 B4.2 收敛数列的界与四则运算 {#seqlaw-unit}

**学习目标与位置。** 数列收敛的误差定义与极限唯一性已经建立。现在证明收敛数列有界，再从定义逐步推出和、常数倍、积与合法商的极限。主归属第242章40A05“级数与数列的收敛与发散”，交叉26A03与97I30；本单元只处理实数数列，不写无穷级数。它属于B4单变量分析入口，可由实数和函数直接进入，不以前面的平面几何为先修，也不宣称B3或整个归纳计数模块已经完成。

**精确先修。** 使用[函数与唯一输出](#fun-definition)、[条件子集](#fun-sets)、[有序对与笛卡尔积](#fun-pairs)、[已采用的自然数归纳规则](#b1-induction)、[已采用的固定更新递归原则](#b1-recursion-principle)、[后继与加一](#b1-add-one)、[自然数全序](#ord-trichotomy)、[后继比较](#ord-successor-comparison)。实数部分使用[包含全序与有理嵌入](#cut-order-embedding)、[加法群](#cutgroup-laws)、[序平移](#cutgroup-translation)、[相反数与差](#cutgroup-negation-subtraction)、[乘法符号](#cutsigned-signs)、[乘法结合](#cutsigned-associative)、[零积与有理相容](#cutsigned-rational-zero)、[有理加法嵌入相容](#cutadd-rational)、[分配与差乘](#cutring-distributive)、[乘法比较](#cutring-multiplication-order)、[除法与乘回](#cutdiv-definition)、[非零系数方程](#cutdiv-equations)、[商比较与正倒数反序](#cutdiv-order)、[绝对值](#realabs-definition-bounds)、[绝对值乘商与三角、反三角](#realabs-products-triangle)、[自然数的实数嵌入](#realarch-embedding)、[实数的自然数界](#realarch-natural-bound)。数列先修为[收敛定义](#seq-definition)、[极限唯一性](#seq-uniqueness)、[常数与倒数基本例](#seq-basic-limits)、[最终相同与交替例](#seq-tails)。

**对象与记号。** $n,k,N$ 是含零的自然数，$a,b:\mathbb N\to\mathbb R$ 是数列，$a_n=a(n)$。$A,B,c,\varepsilon$ 等是实数；所有实数运算沿用已经构造的运算简写。自然指标出现在实数运算中时写其嵌入 $\nu(n)$，不把自然数对象与实数对象默认为同一个。实数平方仅表示两个相同因子相乘。记 $a\to A$ 为此前的收敛定义；使用极限记号时以已经证明的唯一性为依据。

### 1. 先构造有限前缀的界 {#seqlaw-bounded}

称数列 $a$ **有界**，如果存在实数 $M\ge0$，使每个 $n\in\mathbb N$ 都满足 $|a_n|\le M$。这里要求全部指标，不能只给某个尾部的界。

**命题 SA1。** 每个收敛的实数数列都有界；反向不成立。

**两实数的较大值。** 定义函数

$$
\max_{\mathbb R}(x,y)=
\begin{cases}
y,&x\le y,\\
x,&y<x.
\end{cases}
$$

实数全序使两条件互斥且穷尽，输出唯一。第一支输出 $y$，由条件有 $x\le y$ 且 $y\le y$；第二支输出 $x$，有 $y<x$ 且 $x\le x$。所以该值总是两个输入的共同上界；两输入非负时输出也非负。这只定义两个数的较大者，尚未引用一般有限集合最大值定理。

**把前缀过程放进固定递归规则。** 固定整条数列 $a$，取状态集合

$$
\mathcal X=\mathbb N\times\mathbb R_{\ge0},
\qquad x_0=(0,0).
$$

定义一个固定函数

$$
T:\mathcal X\to\mathcal X,
\qquad
T(k,U)=\bigl(k+1,\max_{\mathbb R}(U,|a_k|)\bigr).
$$

给定状态，$k+1$ 是自然数；$U$ 与 $|a_k|$ 非负，较大者非负。因此 $T$ 的输出仍在 $\mathcal X$，且两分量唯一。数列 $a$ 已固定，所以这是一份固定更新规则；不是在每一步偷偷换一个只能用于该步的函数。

已采用的递归原则给唯一 $F:\mathbb N\to\mathcal X$，满足 $F(0)=(0,0)$、$F(k+1)=T(F(k))$。归纳证明 $F(k)$ 的第一分量就是 $k$：起点为零；若第 $k$ 步第一分量为 $k$，更新的第一分量就是 $k+1$。将第二分量记为实数 $U_k\ge0$，于是

$$
F(k)=(k,U_k),\qquad
U_0=0,\qquad U_{k+1}=\max_{\mathbb R}(U_k,|a_k|).
$$

再对 $k$ 归纳，证明每个 $n<k$ 都有 $|a_n|\le U_k$。$k=0$ 时没有自然数 $n<0$，故条件成立。设第 $k$ 步成立，任取 $n<k+1$；后继比较给 $n\le k$。若 $n<k$，则

$$
|a_n|\le U_k\le U_{k+1};
$$

若 $n=k$，由较大值定义直接得 $|a_n|=|a_k|\le U_{k+1}$。全序穷尽两支，归纳完成。因此任意前 $N$ 项都有这个明确构造的非负界，包括 $N=0$ 的空前缀。

**覆盖整个收敛数列。** 设 $a\to A$。以正误差 $1$ 使用定义，取 $N\in\mathbb N$，使 $n\ge N$ 时 $|a_n-A|<1$。对这些指标，实数三角给

$$
|a_n|=|(a_n-A)+A|
\le|a_n-A|+|A|<1+|A|.
$$

取 $M=\max_{\mathbb R}(U_N,1+|A|)\ge0$。若 $n<N$，前缀证明给 $|a_n|\le U_N\le M$；若 $n\ge N$，尾部证明给 $|a_n|<1+|A|\le M$。两支覆盖所有自然指标，SA1正向得证。$N=0$ 时只有尾部支，并无需要另外处理的第一项。

反向由SL4的零一交替数列否定：它每项为零或一，所以绝对值不超过一，确实有界；SL4已经从每个尾部都同时含零和一证明它不收敛。有界与收敛不能互换。

### 2. 和、常数倍、差与绝对值 {#seqlaw-linear-absolute}

**命题 SA2。** 若 $a\to A$、$b\to B$，且 $c\in\mathbb R$ 固定，则

$$
(a_n+b_n)\to A+B,\qquad
(ca_n)\to cA,\qquad
(a_n-b_n)\to A-B,
$$

$$
(|a_n|)\to|A|.
$$

这些表达式都先按逐项规则定义函数 $\mathbb N\to\mathbb R$：每个输入 $n$ 给已知实数 $a_n,b_n$，已有实数加、乘、差、绝对值各给唯一实数输出。绝对值输出还非负，但这里可将它作为实数数列考察。

**和。** 任给实数 $\varepsilon>0$。$\varepsilon/2>0$，分别由两列收敛取得 $N_a,N_b$，使

$$
n\ge N_a\Longrightarrow |a_n-A|<\varepsilon/2,
\qquad
n\ge N_b\Longrightarrow |b_n-B|<\varepsilon/2.
$$

按自然数全序取 $N=\max_{\mathbb N}(N_a,N_b)$，这里较大者是自然数，不是上节的实数较大值函数。任意 $n\ge N$ 同时满足两界。加法群重排及三角给

$$
\begin{aligned}
|(a_n+b_n)-(A+B)|
&=|(a_n-A)+(b_n-B)|\\
&\le|a_n-A|+|b_n-B|\\
&<\varepsilon/2+\varepsilon/2=\varepsilon.
\end{aligned}
$$

严格比较由两次平移保持得到；最后等式来自 $2(\varepsilon/2)=\varepsilon$ 与二倍的分配。这给一个依赖 $\varepsilon$ 的共同起点，其后每个指标都满足误差条件。

**常数倍。** 若 $c=0$，新列每项为零，目标 $cA=0$，误差恒零；取 $N=0$ 就小于任意正 $\varepsilon$。若 $c\ne0$，令 $h=|c|>0$。对正误差 $\varepsilon/h$，取 $N$ 使 $n\ge N$ 时 $|a_n-A|<\varepsilon/h$。由差乘和绝对值乘积，

$$
|ca_n-cA|=|c(a_n-A)|
=h|a_n-A|<h(\varepsilon/h)=\varepsilon.
$$

严格性使用正因子 $h$，乘回也因 $h\ne0$ 合法。零因子支不能靠严格乘法保序混过去。

**差。** 对 $b$ 使用已证常数倍规律，$(-b_n)\to -B$。再对 $a_n$ 与 $-b_n$ 使用已证和规律，得到 $(a_n-b_n)\to A-B$。每个步骤已有全称误差证明，未把待证差规律作为前提。

**绝对值。** 任给 $\varepsilon>0$，取收敛定义给出的 $N$。对每个 $n\ge N$，已证实数反三角界给

$$
\bigl||a_n|-|A|\bigr|\le|a_n-A|<\varepsilon.
$$

所以绝对值列收敛到 $|A|$。极限唯一性允许把以上结论写为相应的 $\lim$ 等式。SA2证毕。

### 3. 乘积先需要一个全列的界 {#seqlaw-product}

**命题 SA3。** 若 $a\to A$、$b\to B$，则逐项乘积数列 $(a_nb_n)$ 收敛到 $AB$。

实数乘法闭合且唯一，所以 $n\mapsto a_nb_n$ 确是实数数列。先对 $a$ 用SA1，取 $M\ge0$ 使所有 $n$ 有 $|a_n|\le M$。固定

$$
K=M+|B|+1>0.
$$

因 $M,|B|\ge0$，有 $M\le K$、$|B|\le K$。这些数不依赖随后选取的指标。

任给 $\varepsilon>0$，令 $\eta=\varepsilon/(2K)>0$。两收敛定义各给阈值，再取自然数较大者 $N$，使任意 $n\ge N$ 同时满足

$$
|a_n-A|<\eta,\qquad |b_n-B|<\eta.
$$

误差分解必须在实数中核对：

$$
\begin{aligned}
a_n(b_n-B)+B(a_n-A)
&=a_nb_n-a_nB+Ba_n-BA\\
&=a_nb_n-AB.
\end{aligned}
$$

末步用交换律消去 $-a_nB+Ba_n$，并将 $BA$ 写为 $AB$。三角与绝对值乘积给

$$
|a_nb_n-AB|
\le |a_n|\,|b_n-B|+|B|\,|a_n-A|.
$$

分别估计两项：

$$
|a_n|\,|b_n-B|\le K|b_n-B|<K\eta,
$$

$$
|B|\,|a_n-A|\le K|a_n-A|<K\eta.
$$

前一步乘非负误差只需弱比较；后一步用 $K>0$ 才保持严格比较。因此即使 $M=0$ 或 $B=0$，仍然有效，未用零因子制造错误的严格不等式。

由商乘回 $(2K)\eta=\varepsilon$，且 $2(K\eta)=(2K)\eta$，系数二非零的方程唯一性给 $K\eta=\varepsilon/2$。于是

$$
|a_nb_n-AB|<K\eta+K\eta=\varepsilon.
$$

SA3得证。证明先取得界再控制两个误差，不是从两个因子各自“接近”就省略乘积估计。

### 4. 最终非零与合法的倒数、商 {#seqlaw-reciprocal-quotient}

**命题 SA4。** 设 $b\to B$ 且 $B\ne0$。则存在 $N_0\in\mathbb N$，使所有 $n\ge N_0$ 的项 $b_n$ 非零。

若另外知道每个 $b_n$ 都非零，则全列 $c_n=1/b_n$ 合法，并且 $c\to1/B$；若还有 $a\to A$，全列 $(a_n/b_n)$ 收敛到 $A/B$。

若只知道尾部非零，需先明确填入早期实值，才能定义全体自然指标上的倒数或商数列。下面构造这样的全列，并证明极限不依赖早期所填的值。

**尾部的统一正下界。** 令 $h=|B|>0$，取 $\delta=h/2>0$。乘回给 $2\delta=h$，所以 $h-\delta=\delta$。由收敛取 $N_0$，使 $n\ge N_0$ 时

$$
|b_n-B|<\delta.
$$

反三角和绝对值基本界给

$$
h-|b_n|\le\bigl|h-|b_n|\bigr|
\le|B-b_n|=|b_n-B|<\delta.
$$

移项得 $|b_n|>h-\delta=\delta>0$，因而 $b_n\ne0$。这一结论只覆盖 $n\ge N_0$，不包括未经检查的早期指标。

**倒数误差的合法恒等式。** 对 $n\ge N_0$，两个分母 $b_n,B$ 都非零，乘积也非零。逐乘回计算

$$
\begin{aligned}
\left(\frac1{b_n}-\frac1B\right)(b_nB)
&=\left(\frac1{b_n}\right)b_nB
 -\left(\frac1B\right)Bb_n\\
&=B-b_n.
\end{aligned}
$$

乘法方程的唯一解因此给

$$
\frac1{b_n}-\frac1B=\frac{B-b_n}{b_nB}.
$$

再用绝对商、绝对乘积和取反不变，得到

$$
\left|\frac1{b_n}-\frac1B\right|
=\frac{|b_n-B|}{|b_n|h}.
$$

右分母严格正，分子允许为零。

**统一误差估计。** 固定正实数 $d=\delta h>0$。因为 $2\delta=h$，还有 $2d=h^2$，故它也等于合法商 $h^2/2$。在上述尾部，

$$
Q_n=|b_n|h>\delta h=d>0.
$$

任给 $\varepsilon>0$，正容差 $\varepsilon d$ 可输入收敛定义，取 $N_1$ 使 $n\ge N_1$ 时 $e_n=|b_n-B|<\varepsilon d$。令 $N=\max_{\mathbb N}(N_0,N_1)$。任意 $n\ge N$，正倒数反序给 $1/Q_n<1/d$；乘以非负 $e_n$ 后只使用弱比较：

$$
\frac{e_n}{Q_n}\le\frac{e_n}{d}
<\frac{\varepsilon d}{d}=\varepsilon.
$$

第二步因 $d>0$ 才能对 $e_n<\varepsilon d$ 作严格商比较；最后一步是乘回。特别当 $e_n=0$，第一步两边都为零，不能写成严格小于；整条链仍凭第二步得小于 $\varepsilon$。

**把尾部公式变成全列。** 对这份 $N_0$，定义

$$
c_n=
\begin{cases}
0,&n<N_0,\\
1/b_n,&n\ge N_0.
\end{cases}
$$

自然数全序使两支互斥且穷尽。第一支给合法实数零；第二支已有 $b_n\ne0$，给唯一合法商。因此 $c:\mathbb N\to\mathbb R$ 是函数。若 $N_0=0$，第一支为空，仍合法。上述阈值 $N\ge N_0$ 保证每个相关项都使用倒数支，所以证明直接给 $c\to1/B$。这里并没有为 $1/0$ 指定值。

还可任取函数

$$
g:\{n\in\mathbb N:n<N_0\}\to\mathbb R,
$$

把第一支零改为 $g(n)$。域条件保证每个早期输入有唯一实值；尾部仍采用合法倒数，所以新规则也是全列。它从 $N_0$ 起与 $c$ 相同，SL4的最终相同定理给同一极限 $1/B$。$N_0=0$ 时这个早期域为空，空函数与空分支不会要求选出不存在的输入。

如果原来所有 $b_n\ne0$，未修改的 $n\mapsto1/b_n$ 也是全列，并从 $N_0$ 起与 $c$ 相同，所以同样趋于 $1/B$。

**商。** 若 $a\to A$，先用SA3得 $(a_nc_n)\to A(1/B)=A/B$。这个全列在早期为零，尾部等于 $a_n/b_n$，因为除法的定义就是乘非零分母的倒数。任意另填早期实值而保留尾部商的全列与它最终相同，故也有同一极限。若所有 $b_n\ne0$，原本未修改的逐项商全列当然在其中。分母极限 $B\ne0$ 保证结论中的 $A/B$ 合法，分子极限 $A$ 可以为零。

**两个边界不能混同。** 令 $b_0=0$，对 $n\ge1$ 令 $b_n=1$。它与常数一列最终相同，所以趋于一；但 $1/b_0$ 没有定义。填零所得倒数全列为零、一、一、……，确实趋于一，却不意味着原始倒数式在第零项也有意义。

再取SL3的 $b_n=1/(\nu(n)+1)>0$，它趋于零。其逐项倒数为 $\nu(n)+1$：这个值与 $b_n$ 相乘为一，由非零系数方程唯一性得到。该倒数列无界：任给 $M\ge0$，自然数界给某个 $n$ 使 $\nu(n)>M$，故 $\nu(n)+1>M$，且该项正，绝对值就是自身。SA1说明它不收敛。不过取 $a_n=b_n$ 时，每项商 $a_n/b_n=1$，反而收敛到一。所以 $B=0$ 时不能套用SA4，也不能概括成“所有商都发散”。

### 5. 课后题 {#seqlaw-exercises}

#### 题1：固定递归规则与空前缀 {#seqlaw-q01}

给任意实数数列 $a$，定义两个实数的较大值并逐支核其共同上界性质。以状态集合 $\mathbb N\times\mathbb R_{\ge0}$ 和固定更新 $T$ 构造 $U_k$，先归纳证明状态第一分量为 $k$，再证明 $n<k$ 时 $|a_n|\le U_k$。说明 $k=0$ 为什么不要求挑选前缀元素。[完整解答](#seqlaw-a01)

#### 题2：收敛有界与错误的逆命题 {#seqlaw-q02}

假设 $a\to A$。用误差一取得尾部界，再用题1构造前缀界，完整覆盖 $n<N$ 与 $n\ge N$，包括 $N=0$。用已有零一交替数列说明“有界必收敛”错误，并说明只给尾部界还缺哪一步。[完整解答](#seqlaw-a02)

#### 题3：和、差、常数倍及零常数 {#seqlaw-q03}

设 $a\to A$、$b\to B$，$c$ 是固定实数。先核逐项和、差、常数倍的函数合法性，再从误差定义证明和与常数倍的极限，常数零单列，最后由已证结果得到差规律。每处写共同起点与其适用的全部后续指标。[完整解答](#seqlaw-a03)

#### 题4：绝对值列的极限 {#seqlaw-q04}

设 $a\to A$。定义绝对值数列，使用实数反三角证明它趋于 $|A|$，覆盖 $A=0$。解释外层绝对值的输入是什么，不能把 $|a_n-A|$ 与 $|a_n|-|A|$ 直接写成相等。[完整解答](#seqlaw-a04)

#### 题5：乘积的界与两项误差 {#seqlaw-q05}

设 $a\to A$、$b\to B$。先取 $|a_n|\le M$ 的全列界，令 $K=M+|B|+1$，逐分配核误差分解，再以容差 $\varepsilon/(2K)$ 完成乘积证明。明确 $M=0$ 或 $B=0$ 时，哪些比较只能先写弱式，为什么后续仍得严格误差界。[完整解答](#seqlaw-a05)

#### 题6：非零极限的尾部下界 {#seqlaw-q06}

设 $b\to B\ne0$。令 $h=|B|$、$\delta=h/2$，先核正性与 $h-\delta=\delta$，用反三角证明最终 $|b_n|>\delta$。给一条趋于非零数却早期有零项的完整数列，核其收敛并说明它反驳了什么错误推论。[完整解答](#seqlaw-a06)

#### 题7：倒数、商与早期填值的合法性 {#seqlaw-q07}

设 $b\to B\ne0$，另有 $a\to A$。从题6的阈值起，以乘回证明倒数误差恒等式，并用正数 $d=(|B|/2)|B|$ 完成误差估计。完整定义早期填零的倒数列与商列，并证明任意早期实值替换不改极限；说明何时可以使用从第零项起未经修改的倒数式。诊断两句话：“最终非零，所以所有倒数项都已有定义”；“$Q>d>0$ 总使 $e/Q<e/d$，即使 $e=0$”。[完整解答](#seqlaw-a07)

#### 题8：精确分解与零极限分母的两种行为 {#seqlaw-q08}

证明全列 $z_n=(2\nu(n)+3)/(\nu(n)+1)$ 合法，逐项用乘回证 $z_n=2+1/(\nu(n)+1)$，再用已证规律求极限。令 $b_n=1/(\nu(n)+1)$，证明其倒数列不收敛，而 $b_n/b_n$ 为常数一列；说明为何不能以“最高次项”或“分母趋零必发散”代替证明。[完整解答](#seqlaw-a08)

**来源与范围说明。** 收敛定义与运算定理的公开材料条件对照见[本批来源审计](#real-sequences-sources)。本单元自行给出固定状态递归、全部误差估计及习题解答，不借用未证的一般有限最大值、实数多项式极限、无穷级数或连续性定理。
