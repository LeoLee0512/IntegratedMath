## 基础单元 B4.5 实数数列的柯西判据 {#seqcauchy-unit}

**位置与目标。** 本单元继续第242章40A05“级数与数列的收敛与发散”的数列部分，交叉26A03与97I30，属于 `single-analysis` 的B4学习路线。前面的收敛定义需要一个候选极限；这里考察只比较数列自身尾项的条件，最后证明它恰好刻画实数数列的收敛。只完成这一有限任务，不涉及级数、一般度量空间或整个分析模块的完备课程。

**精确先修。** 使用[函数及求值](#fun-definition)、[条件子集](#fun-sets)、[有序对与积集](#fun-pairs)、[复合](#fc-composition)、[自然数归纳](#b1-induction)、[固定更新递归原则](#b1-recursion-principle)、[自然序的见证](#ord-definition)、[自然全序](#ord-trichotomy)、[后继比较](#ord-successor-comparison)、[自然加法保序](#ord-addition-order)、[自然乘法与单位](#b1-multiplication-units)、[自然乘法交换与分配](#b1-multiplication-commutative)、[商余定理](#div-theorem)及[余数的唯一求值](#div-quotient-remainder)。实数方面使用[加法群与差](#cutgroup-negation-subtraction)、[序平移](#cutgroup-translation)、[分配律](#cutring-distributive)、[非零除法与乘回](#cutdiv-definition)、[正倒数反序](#cutdiv-order)、[双倒数](#cutinv-rational-identities)、[绝对值基本界](#realabs-definition-bounds)、[三角不等式](#realabs-products-triangle)、[自然嵌入及保序](#realarch-embedding)、[严格自然数界](#realarch-natural-bound)。数列方面使用[收敛定义](#seq-definition)、[极限唯一性及自然数较大者](#seq-uniqueness)、[常数与倒数基本例](#seq-basic-limits)、[零一交替列](#seq-tails)、[任意数列的有限前缀界](#seqlaw-bounded)、[子列指标及其下界](#subseq-indices)和[有界实数列的BW定理](#subseq-bolzano-weierstrass)。

**对象与记号。** $a:\mathbb N\to\mathbb R$ 是全函数，$a_n=a(n)$；$\mathbb N$ 含零。$m,n,N,j,J$ 表示自然指标，$L,M,\varepsilon$ 等表示实数。自然指标进入实数运算时使用既有嵌入 $\nu$；实数常数0、1、2沿用有理像。实数加、减、乘、除仍是已建立运算的简写。自然数二元较大者记 $\max_{\mathbb N}$，SA1定义的实数二元较大者记 $\max_{\mathbb R}$，不混淆两种输入域。

### 1. 同时比较任意两个尾项 {#seqcauchy-definition}

**定义与命题 CA1。** 称实数数列 $a$ 为**柯西列**，如果

$$
\begin{gathered}
\forall\varepsilon\in\mathbb R,\ \varepsilon>0,
\quad\exists N\in\mathbb N\quad\forall m,n\in\mathbb N,\\
m\ge N\ \text{且}\ n\ge N
\quad\Longrightarrow\quad |a_m-a_n|<\varepsilon.
\end{gathered}
$$

它不是柯西列，当且仅当

$$
\begin{gathered}
\exists\varepsilon_0\in\mathbb R,\ \varepsilon_0>0,
\quad\forall N\in\mathbb N\quad\exists m,n\in\mathbb N,\\
m\ge N,\qquad n\ge N,\qquad |a_m-a_n|\ge\varepsilon_0.
\end{gathered}
$$

**量词与否定。** 固定整条数列后，先任取正误差，再选自然阈值，最后任取两个尾指标；所选阈值不能随后来任取的 $m,n$ 改变。不满足定义，意味着某个正误差下每个阈值都有一对违规尾项。否定最后的蕴含，同时保留 $m,n\ge N$ 而把严格小于改为不严格大于，便得到所列完整否定。这里仅使用经典逻辑和实数全序。

这个条件没有候选实数 $L$。它要求全部尾项彼此接近；只检验 $m=n$ 时，任何数列都有 $|a_n-a_n|=0$，因此对角线检验不能代替双指标条件。

**常数与倒数例。** 若 $a_n=C$，每个差恒零；对任意 $\varepsilon>0$，$N=0$ 就满足定义。再令

$$
b_n=\frac1{\nu(n)+1}.
$$

每个分母至少为正实数1，所以 $b$ 是合法全列且 $b_n>0$。任给 $\varepsilon>0$，令 $d=\varepsilon/2>0$。严格自然数界给自然数 $N$，使 $1/d<\nu(N)$。若 $r\ge N$，保序及加1给

$$
0<1/d<\nu(N)\le\nu(r)<\nu(r)+1.
$$

正倒数反序及双倒数给 $0<b_r<d$。因此对任意 $m,n\ge N$，

$$
|b_m-b_n|\le |b_m|+|-b_n|=b_m+b_n<d+d=\varepsilon.
$$

最后等式由 $2(\varepsilon/2)=\varepsilon$ 和分配律得到。这个证明直接控制两个尾指标，并未先调用本单元尚未证明的柯西判据。

**每尾都失败的例。** 令 $r_n\in\{0,1\}$ 是 $n$ 除以2的唯一余数，令 $c_n=\nu(r_n)$。这是已有的零一交替列。任给 $N\in\mathbb N$，取

$$
m=2N,\qquad n=2N+1.
$$

自然数运算中 $2N=N+N$，所以 $m\ge N$，继而 $n\ge N$。商余候选分别为 $(N,0)$、$(N,1)$，余数均小于2，唯一性给 $c_m=0,c_n=1$。于是

$$
|c_m-c_n|=|0-1|=1.
$$

取固定实数 $\varepsilon_0=1$，便符合CA1的完整否定。等于误差边界已足以破坏严格小于，故不必把误差再缩小。该列不是柯西列。

### 2. 从收敛到柯西，从柯西到有界 {#seqcauchy-bounded}

**命题 CA2。** 每个收敛实数列都是柯西列；每个柯西实数列都有界。第二结论的证明不假定柯西列已经收敛。

**收敛给双指标控制。** 假设 $a_n\to L$。任给实数 $\varepsilon>0$，由收敛定义对正误差 $\varepsilon/2$ 取 $N$。任意 $m,n\ge N$ 同时满足

$$
|a_m-L|<\varepsilon/2,\qquad |a_n-L|<\varepsilon/2.
$$

加法群给 $a_m-a_n=(a_m-L)+(L-a_n)$。三角和取反不改绝对值得

$$
\begin{aligned}
|a_m-a_n|
&\le |a_m-L|+|L-a_n|\\
&=|a_m-L|+|a_n-L|\\
&<\varepsilon/2+\varepsilon/2=\varepsilon.
\end{aligned}
$$

两项都由同一阈值控制，故符合柯西定义。未要求极限 $L$ 非零，也未要求两个指标不同。

**柯西给整个尾部的界。** 现在只假设 $a$ 柯西。以正误差1取自然阈值 $N$，使任意 $m,n\ge N$ 有 $|a_m-a_n|<1$。指标 $N$ 本身属于尾部，可固定其中一个输入为 $N$；于是任意 $n\ge N$ 有

$$
|a_n-a_N|<1,
\qquad
|a_n|=|(a_n-a_N)+a_N|
\le |a_n-a_N|+|a_N|<1+|a_N|.
$$

这只控制了尾部，尚不能省略早期输入。

**用已建前缀界补齐。** SA1在任意全列 $a$ 上构造了非负实数 $U_k$，满足

$$
U_0=0,\qquad U_{k+1}=\max_{\mathbb R}(U_k,|a_k|),
\qquad n<k\Longrightarrow |a_n|\le U_k.
$$

该构造先在固定状态集 $\mathbb N\times\mathbb R_{\ge0}$ 上定义更新，再递归；其存在与归纳证明不需要数列收敛。因此可在这里用于当前仅知柯西的 $a$。令

$$
M=\max_{\mathbb R}(U_N,1+|a_N|).
$$

两输入非负，故 $M\ge0$。若 $n<N$，则 $|a_n|\le U_N\le M$；若 $n\ge N$，则 $|a_n|<1+|a_N|\le M$。自然全序穷尽两支，所以每个自然输入都满足 $|a_n|\le M$，这正是有界。若 $N=0$，$U_0=0$ 仍有定义，前缀支为空，尾部支覆盖全列。CA2得证。

有界不蕴含柯西：CA1的交替列每项为0或1，故 $|c_n|\le1$，但已经证明它不是柯西列。

### 3. 一个收敛子列怎样控制全列 {#seqcauchy-subsequence}

**命题 CA3。** 设 $a$ 是柯西列，$k:\mathbb N\to\mathbb N$ 为严格递增指标函数。如果给定实数 $L$，使子列 $a_{k_j}\to L$，则全列 $a_n\to L$。

**证明。** 任给实数 $\varepsilon>0$。由柯西条件取 $N$，使

$$
m,n\ge N\Longrightarrow |a_m-a_n|<\varepsilon/2.
$$

由所给子列的收敛取 $J$，使

$$
j\ge J\Longrightarrow |a_{k_j}-L|<\varepsilon/2.
$$

现在固定一次自然数 $j_*=\max_{\mathbb N}(N,J)$。SS1给每个严格递增自然指标的下界 $k_j\ge j$，因此

$$
k_{j_*}\ge j_*\ge N,\qquad j_*\ge J.
$$

任取 $n\ge N$。比较的两个原列指标 $n$ 与 $k_{j_*}$ 都在柯西尾部；子列指标 $j_*$ 也在自己的收敛尾部。由差式和三角，

$$
\begin{aligned}
|a_n-L|
&=|(a_n-a_{k_{j_*}})+(a_{k_{j_*}}-L)|\\
&\le |a_n-a_{k_{j_*}}|+|a_{k_{j_*}}-L|\\
&<\varepsilon/2+\varepsilon/2=\varepsilon.
\end{aligned}
$$

所选 $j_*$ 可以依赖 $\varepsilon$，但固定后不随后来任取的 $n$ 改变；同一子列项与整个尾部比较。于是阈值 $N$ 使全部 $n\ge N$ 都满足收敛定义，故 $a_n\to L$。两误差允许等于零，严格界仍来自它们分别小于正数 $\varepsilon/2$。证毕。

此处并未证明每条数列都有收敛子列。命题把“已经给出一个收敛子列”和“原列柯西”作为两项独立假设。

### 4. 实数柯西判据与有限改动 {#seqcauchy-criterion}

**命题 CA4（实数数列的柯西判据）。** 对任意 $a:\mathbb N\to\mathbb R$，

$$
a\text{ 是柯西列}
\quad\Longleftrightarrow\quad
\exists L\in\mathbb R,\ a_n\to L.
$$

若收敛，该 $L$ 由SL2唯一。

**充分性。** 假设 $a$ 柯西。CA2给实数 $M\ge0$，使每项 $|a_n|\le M$。已有SS3的实数数列版BW定理应用于这个全列，给某个严格递增自然指标函数 $k$ 以及实数 $L$，使 $a_{k_j}\to L$。于是CA3的两项假设都满足，得到 $a_n\to L$。这里从有界列取得一个收敛子列，使用的是已由单调子列和实数上确界证明的BW；不是借待证的柯西充分性。

**必要性。** 若存在实数 $L$ 使 $a_n\to L$，CA2的第一段已经对任意正误差和两个尾指标证明柯西条件。故反向成立，判据得证。

**完备性的这一含义。** 我们最初为所构造实数证明的是非空有上界集合的上确界性质。它随后支持单调收敛与BW，再经本单元的估计，得到“每条实数柯西列都收敛到一个实数”。现在可称实数具有**数列意义下的柯西完备性**。这是上述证明链的结论，不是只凭“完备”这个词跳过证明，也没有在实数集合外增添一个极限值。

**最终相同保持柯西性的两个方向。** 设 $a,b:\mathbb N\to\mathbb R$，且有 $N_0\in\mathbb N$ 使全部 $n\ge N_0$ 满足 $a_n=b_n$。若 $a$ 柯西，任给 $\varepsilon>0$，取它的柯西阈值 $N_a$，令 $N=\max_{\mathbb N}(N_0,N_a)$。任意 $m,n\ge N$ 都满足两份项值相等，也在原柯西尾部，故

$$
|b_m-b_n|=|a_m-a_n|<\varepsilon.
$$

所以 $b$ 柯西。反过来，若 $b$ 柯西，对其误差阈值 $N_b$ 取 $\max_{\mathbb N}(N_0,N_b)$；每对尾指标满足

$$
|a_m-a_n|=|b_m-b_n|<\varepsilon,
$$

故 $a$ 柯西。$N_0=0$ 时同样成立。此结论要求双方先是全函数，允许早期项任意改成合法实数；它不替未定义的早期项补定义。

### 5. 课后题 {#seqcauchy-exercises}

#### 题1：双指标量词不能缩成对角线 {#seqcauchy-q01}

给定 $a:\mathbb N\to\mathbb R$，写出柯西条件的完整否定，说明阈值能依赖什么。证明只检查 $m=n$ 会让任何数列通过，并用零一交替列说明该检查不足。[完整解答](#seqcauchy-a01)

#### 题2：不先使用判据的两个正例 {#seqcauchy-q02}

任给实数 $C$，从双指标定义证明常数列 $a_n=C$ 柯西。再证明 $b_n=1/(\nu(n)+1)$ 是全函数，并用自然数界和正倒数反序直接证明它柯西；说明两个尾指标怎样共享一个阈值。[完整解答](#seqcauchy-a02)

#### 题3：由候选极限消去候选极限 {#seqcauchy-q03}

设 $a_n\to L$，其中 $L\in\mathbb R$。从收敛定义证明 $a$ 柯西，写明加减 $L$ 的差式及两个指标条件；解释 $L=0$、$m=n$ 是否需要排除。[完整解答](#seqcauchy-a03)

#### 题4：前缀与尾部都要有界 {#seqcauchy-q04}

设 $a$ 柯西。以误差1取得阈值 $N$，构造覆盖全列的非负界。重述SA1固定状态递归为何适用于当前全列，给出前缀界的归纳证明，并单独说明 $N=0$。不可在此使用“柯西列必收敛”。[完整解答](#seqcauchy-a04)

#### 题5：只固定一个子列项 {#seqcauchy-q05}

设 $a$ 柯西，$k$ 是严格递增自然指标，且 $a_{k_j}\to L$。对给定 $\varepsilon>0$，分别取得阈值 $N,J$ 后，说明怎样固定一个合法子列项，并用它证明全列趋于 $L$。解释为什么只取 $j=J$ 可能不足。[完整解答](#seqcauchy-a05)

#### 题6：充分性实际使用了什么 {#seqcauchy-q06}

从CA2、CA3与已有BW定理证明实数柯西判据的两个方向，指出极限存在性、极限唯一性各来自哪里，并列出从实数上确界到这一判据的依赖顺序。说明是否需要上极限、下极限或把新极限加入实数集。[完整解答](#seqcauchy-a06)

#### 题7：任意合法有限改动 {#seqcauchy-q07}

设 $a,b:\mathbb N\to\mathbb R$ 在全部 $n\ge N_0$ 上相同。从双指标定义证明它们的柯西性等价，两个方向都写。进一步，给定任意函数 $g:\{n\in\mathbb N:n<N_0\}\to\mathbb R$，以早期取 $g(n)$、其后取 $a_n$ 定义 $b$；证明它是全函数并适用结论，包括 $N_0=0$。[完整解答](#seqcauchy-a07)

#### 题8：有一个收敛子列仍不够 {#seqcauchy-q08}

令 $c_n=\nu(r_n)$，其中 $r_n$ 是 $n$ 除以2的余数。证明它有界，证明 $k_j=2j$ 给严格递增指标且 $c_{k_j}\to0$，再给完整双指标见证证明它不是柯西列。由此说明CA3不能删去哪个假设，并证明原列不收敛。[完整解答](#seqcauchy-a08)

### 6. 来源与本单元的边界 {#seqcauchy-source-boundary}

公开教材的定义与条件对照见[柯西与函数点极限来源记录](#real-cauchy-function-limits-sources)。本单元的证明以已有实数、前缀界和BW接口逐步重建，所有练习另给完整解答。本单元没有使用limsup、liminf、无穷级数或任意无限选取实点的原则；有限改动与一个给定子列的比较都已明确写出量词。
