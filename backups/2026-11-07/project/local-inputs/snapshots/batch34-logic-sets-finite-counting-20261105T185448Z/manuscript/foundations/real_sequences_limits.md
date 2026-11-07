## 基础单元 B4.1 实数数列、收敛定义与基本例 {#seq-unit}

**位置与目标。** 本单元进入 B4 大学共同基础，主归第242章“无穷极限过程的收敛与发散”的40A05“级数与数列的收敛与发散”，交叉26A03与97I30。学习任务是把“项越来越接近某数”写成能检验的量词，并从定义证明基本收敛例。这里只写实数数列的一段入口，不表示级数、微积分、学习模块 `single-analysis` 或整章已经完成。平面几何不是本单元先修。

**精确先修。** 使用[函数与求值](#fun-definition)、[有序对](#fun-pairs)、[集合相等](#fun-sets)及[复合](#fc-composition)；自然数方面使用[已采用的归纳规则](#b1-induction)、[加法及零](#b1-addition-definition)、[加法交换](#b1-addition-commutative)、[加法结合](#b1-addition-associative)、[乘法与单位](#b1-multiplication-units)、[乘法交换及分配](#b1-multiplication-commutative)、[自然序](#ord-definition)、[三歧性](#ord-trichotomy)、[后继比较](#ord-successor-comparison)、[加法保序并反映序](#ord-addition-order)、[自然差的存在唯一](#sub-definition)、[商余定理](#div-theorem)及[余数定义](#div-quotient-remainder)。实数方面使用[自然数嵌入与保序](#realarch-embedding)、[严格自然数界](#realarch-natural-bound)、[加法群与差](#cutgroup-negation-subtraction)、[平移保序](#cutgroup-translation)、[乘法比较](#cutring-multiplication-order)、[非零除法](#cutdiv-definition)、[方程唯一解](#cutdiv-equations)、[正倒数反序](#cutdiv-order)、[双倒数](#cutinv-rational-identities)、[绝对值基本界](#realabs-definition-bounds)及[三角与反三角](#realabs-products-triangle)。有理数常数在实数中计算的依据是[加法相容](#cutadd-rational)、[乘法相容](#cutsigned-rational-zero)及[除法相容](#cutdiv-definition)。这些接口不等于完整 B3 公理课程已经写成；自然数规则、经典逻辑和集合背景仍按前文公开采用。

**对象与记号。** 本书的 $\mathbb N$ 包含零。$n,N,k,K,m$ 表示自然数，$A,L,M,\varepsilon$ 等表示实数。保持已建嵌入链

$$
\iota:\mathbb N\to\mathbb Z,\qquad j:\mathbb Z\to\mathbb Q,
\qquad\eta=j\circ\iota:\mathbb N\to\mathbb Q,
\qquad i:\mathbb Q\to\mathbb R,
$$

$$
\nu=i\circ\eta:\mathbb N\to\mathbb R.
$$

每一步输出都在下一步定义域内。RA的嵌入接口已证明 $\nu(0)=0$、$\nu(1)=1$、$\nu(m+n)=\nu(m)+\nu(n)$，以及 $m\le n$ 当且仅当 $\nu(m)\le\nu(n)$。因此自然指标的运算与实数值的运算不可混淆。本单元在涉及指标的实数公式中保留 $\nu$；作为实数常数的 $1,2,3,1/10$ 等是相应有理数的像。实数运算沿用 $+,-,\cdot,/$，是此前已经建立的分割运算。

### 1. 从全函数到收敛的量词 {#seq-definition}

**定义。** 一个实数数列是函数 $a:\mathbb N\to\mathbb R$。写 $a_n=a(n)$，用 $(a_n)_{n\in\mathbb N}$ 表示整个函数。下标是输入，不是乘法。数列的值域像集合 $\{a_n:n\in\mathbb N\}$ 只记录出现过的实数；函数还记录各输入对应哪个输出。

**命题 SL1：有限前缀与收敛的准确含义。** 任给自然数 $K$，前 $K$ 项不能唯一决定整个数列。对已给数列 $a$ 和固定实数 $L$，定义“$a$ 收敛到 $L$”，记 $a_n\to L$，为

$$
\begin{gathered}
\forall\varepsilon>0\ \exists N\in\mathbb N\ \forall n\in\mathbb N,\\
n\ge N\Longrightarrow |a_n-L|<\varepsilon.
\end{gathered}
$$

其中 $\varepsilon$ 取实数。固定 $L$ 时，这个断言不成立当且仅当

$$
\begin{gathered}
\exists\varepsilon_0\in\mathbb R,\ \varepsilon_0>0,
\quad\forall N\in\mathbb N\ \exists n\in\mathbb N,\\
n\ge N\ \text{且}\ |a_n-L|\ge\varepsilon_0.
\end{gathered}
$$

**有限前缀的证明。** “前 $K$ 项”指 $0\le n<K$。定义两个全函数

$$
a_n=0\quad(n\in\mathbb N),\qquad
b_n=\begin{cases}0,&n<K,\\1,&K\le n.\end{cases}
$$

自然全序保证两支互斥且穷尽，每支给唯一实数，所以 $b$ 确是函数。前 $K$ 项相同；输入 $n=K$ 时，$a_K=0\ne1=b_K$，故两函数不同。$K=0$ 时前缀为空，结论仍成立。

**量词的读取与否定。** 收敛定义依次要求：任取正误差 $\varepsilon$，选一个自然起点 $N$，然后检查每个 $n\ge N$。选 $N$ 时可以使用 $a,L,\varepsilon$，却不能依赖尚未任取的 $n$。否定“对每个正误差都有这样的起点”，得到“某个正误差没有这样的起点”；再否定“起点以后每项都符合”，得到“每个起点以后至少有一项不符合”。实数全序使“不是 $|a_n-L|<\varepsilon_0$”等价于 $|a_n-L|\ge\varepsilon_0$，从而得到所列否定。证毕。

**固定目标失败与无极限。** 若存在某个 $L$ 使 $a_n\to L$，称数列收敛；若不存在任何这样的实数 $L$，称它不收敛。否定某个指定 $L$ 并不足以证明不收敛。例如常数列零不趋于一，但稍后会证明它趋于零。这里暂不用把极限当作唯一输出的 $\lim$ 记号。

**次序不能被像集合代替。** 由商余定理，每个 $n$ 除以正自然数2有唯一余数 $r_n\in\{0,1\}$。令 $c_n=\nu(r_n)$，另令 $d_n=1-c_n$。在输入0和1处，商余候选分别为 $(0,0)$、$(0,1)$，所以 $c_0=0,c_1=1,d_0=1,d_1=0$。两列的像集合都是 $\{0,1\}$，但在输入0处值不同。数列不是它的像集合。

### 2. 一个数列不能收敛到两个不同实数 {#seq-uniqueness}

先定义自然数的二元最大值：若 $p\le q$，令 $\max(p,q)=q$；若 $q<p$，令 $\max(p,q)=p$。自然全序保证恰一支适用。第一支中结果同时不小于 $p,q$；第二支也如此。故 $n\ge\max(p,q)$ 总能推出 $n\ge p$ 且 $n\ge q$。这里是两个自然数的比较，没有使用有限实数集合的最大值定理。

**命题 SL2：极限唯一。** 若 $a_n\to L$ 且 $a_n\to M$，则 $L=M$。

**证明。** 假设 $L\ne M$。差的零判据及绝对值零判据给

$$
\delta=|L-M|>0.
$$

实数常数3正，因此 $\delta/3>0$。对两份收敛定义分别用这一误差，得到 $N_1,N_2\in\mathbb N$，满足

$$
n\ge N_1\Longrightarrow |a_n-L|<\delta/3,
\qquad
n\ge N_2\Longrightarrow |a_n-M|<\delta/3.
$$

令 $N=\max(N_1,N_2)$，并选自然指标 $n=N$。两份严格界同时成立。加法群给 $L-M=(L-a_N)+(a_N-M)$；绝对值取反不变给 $|L-a_N|=|a_N-L|$。因此

$$
\begin{aligned}
\delta
&=|(L-a_N)+(a_N-M)|\\
&\le |L-a_N|+|a_N-M|\\
&<\delta/3+\delta/3=2\delta/3.
\end{aligned}
$$

【依据：三角不等式；两份严格界先后平移相加。最后等式可将两边乘正数3，分别得到 $\delta+\delta=2\delta$，再用非零消去。】

同时 $2<3$，乘正数 $\delta/3$ 得 $2\delta/3<\delta$；右端相等由除法乘回。于是 $\delta<\delta$，与严格序矛盾。故 $L=M$。证毕。

**定理后的记号。** 若 $a$ 收敛，才将唯一实数 $L$ 写成

$$
\lim_{n\to\infty}a_n=L.
$$

此处 $n\to\infty$ 是所定义量词的记号，并没有把 $\infty$ 加入实数集，也不要求数列某一项等于 $L$。

### 3. 常数与从零索引开始的倒数列 {#seq-basic-limits}

**命题 SL3。** 对每个实数 $C$，常数列 $a_n=C$ 收敛到 $C$。函数

$$
b:\mathbb N\to\mathbb R,\qquad b_n=\frac1{\nu(n)+1}
$$

也有定义，并收敛到零。

**常数列。** 任给 $\varepsilon>0$，取 $N=0$。对每个 $n\ge0$，

$$
|a_n-C|=|C-C|=0<\varepsilon.
$$

这正是定义的全部量词，所以结论成立。

**倒数列的定义域。** 自然数 $0\le n$，保序给 $0\le\nu(n)$，同加正数1得 $\nu(n)+1\ge1>0$。故每个分母非零，每个输入都给唯一实数。正数的倒数正，所以 $b_n>0$，并且 $b_0=1$。没有出现 $1/\nu(0)$。

**倒数列的收敛。** 任给 $\varepsilon>0$。其倒数 $1/\varepsilon$ 有定义且正。由 RA1 取正自然数 $N$，使

$$
1/\varepsilon<\nu(N).
$$

任取 $n\ge N$。保序给 $\nu(N)\le\nu(n)$；平移和传递给

$$
0<1/\varepsilon<\nu(N)\le\nu(n)<\nu(n)+1.
$$

对两个正实数 $1/\varepsilon$ 和 $\nu(n)+1$ 用严格正倒数反序，再用双倒数公式：

$$
0<\frac1{\nu(n)+1}<\frac1{1/\varepsilon}=\varepsilon.
$$

因此 $|b_n-0|=b_n<\varepsilon$。所选 $N$ 依赖 $\varepsilon$，且这一论证覆盖全部 $n\ge N$。故 $b_n\to0$。证毕。

**具体阈值与最早阈值。** 对误差 $\varepsilon=1/10$，$N=10$ 可用：若 $n\ge10$，则 $\nu(n)+1\ge11>10$，正倒数反序得 $b_n<1/10$。若 $N<10$，自然后继比较给 $N\le9$，所以输入 $n=9$ 在该尾部，而 $b_9=1/10$，不满足严格小于。因此10是最早阈值。同理，$\varepsilon=1/100$ 时，$N=100$ 足够；任何更早 $N$ 满足 $N\le99$，尾项 $b_{99}=1/100$ 使严格界失败。自然指标9、10、99、100进入实数公式时使用 $\nu$ 及其嵌入相容。

**只看一个误差时怎样读图。** 下图取 $\varepsilon=1/4$。任意自然数 $n\ge4$ 都满足 $\nu(n)+1\ge5>0$，正倒数反序给 $0<b_n\le1/5<1/4$；所以4是阈值。若自然数 $N<4$，则 $N\le3$，尾部含输入3而 $b_3=1/4$，故任何更早阈值都失败。这个证明用任意 $n\ge4$，不依赖只画到14的取点。

![倒数列在误差四分之一内的严格阈值](figures/b2_real_sequence_epsilon.png)

图中下标 $n,N$ 是自然数；纵向实数公式 $1/(n+1)$ 简写正文的 $1/(\nu(n)+1)$，分数与纵轴常数指有理嵌入像。空心点强调等于误差边界不符合严格要求。有限散点图不证明全部尾项；图下的全称推导才说明这个误差下的整个尾部，而任意正误差的收敛证明已经在 SL3 给出。完整绘图与精确有理输入检查见[误差阈值图代码](#real-sequence-epsilon-figure-code)。

### 4. 有限改动、尾移与每个尾部的反例 {#seq-tails}

**命题 SL4。** 以下各列均为 $\mathbb N\to\mathbb R$ 的全函数。

1. 若存在 $N_0\in\mathbb N$ 使每个 $n\ge N_0$ 都有 $a_n=b_n$，则对每个实数 $L$，$a_n\to L$ 当且仅当 $b_n\to L$。
2. 固定 $k\in\mathbb N$，定义 $b_n=a_{n+k}$。则对每个实数 $L$，$a_n\to L$ 当且仅当 $b_n\to L$。
3. 令 $r_n$ 为 $n$ 除以2的余数，定义 $c_n=\nu(r_n)$。每项都满足 $|c_n|\le1$，但此列不收敛到任何实数。

**第1条：最终相同。** 假设 $a_n\to L$。任给 $\varepsilon>0$，取其阈值 $N_1$，再令 $N=\max(N_0,N_1)$。任取 $n\ge N$，同时有 $a_n=b_n$ 和 $|a_n-L|<\varepsilon$，所以

$$
|b_n-L|=|a_n-L|<\varepsilon.
$$

这证明 $b_n\to L$。反过来，若 $b_n\to L$，对其误差阈值 $N_2$ 取 $\max(N_0,N_2)$；每个此后输入都满足 $a_n=b_n$，同一等式反向给 $|a_n-L|<\varepsilon$。故 $a_n\to L$。$N_0=0$ 也包括在内。

**第2条：固定尾移。** 对每个自然数 $n$，$n+k$ 仍为自然数，故 $a_{n+k}$ 唯一，定义得到全函数。

先假设 $a_n\to L$。对任给 $\varepsilon>0$ 取原列阈值 $N$。若 $n\ge N$，则 $n\le n+k$，见证是 $k$；传递给 $n+k\ge N$。所以

$$
|b_n-L|=|a_{n+k}-L|<\varepsilon.
$$

再假设 $b_n\to L$。给定 $\varepsilon>0$，取其阈值 $N$。我们为 $a$ 选阈值 $N+k$。任取 $m\ge N+k$，则 $k\le N+k\le m$，故自然差 $n=m-k$ 存在，满足 $k+n=m$，交换得 $n+k=m$。由

$$
N+k\le m=n+k
$$

用自然加法反映比较，得到 $N\le n$。因而

$$
|a_m-L|=|a_{n+k}-L|=|b_n-L|<\varepsilon.
$$

这证明原列收敛。反向没有引入负指标；$k=0$ 时同样成立。

**第3条：交替例。** 商余存在唯一给每个 $r_n$，且 $0\le r_n<2$，后继比较给 $r_n=0$ 或 $r_n=1$。嵌入后 $c_n$ 只取0或1，所以 $|c_n|\le1$。

任给自然阈值 $N$。自然数 $2N=N+N\ge N$，见证是 $N$；$2N+1\ge2N\ge N$。商余候选

$$
2N=2\cdot N+0,\qquad 2N+1=2\cdot N+1
$$

的余数分别满足 $0\le0<2$ 和 $0\le1<2$，唯一性给

$$
c_{2N}=0,\qquad c_{2N+1}=1.
$$

若存在实数 $L$ 使 $c_n\to L$，取正误差 $1/3$ 及其阈值 $N$。上述两个指标都在尾部，故 $|0-L|<1/3$、$|1-L|<1/3$。加法群给 $1=(1-L)+(L-0)$，从而

$$
1=|1|\le |1-L|+|L-0|
       =|1-L|+|0-L|<1/3+1/3=2/3<1,
$$

矛盾。因此不存在任何实数极限。证毕。

若一列所有项都被某个统一非负实数 $H$ 控制为 $|a_n|\le H$，称它**有界**。交替例取 $H=1$，说明有界本身不能保证收敛。下一单元再证明收敛一定给出这样的统一界，不能把未证的反方向用于本单元。

### 5. 课后题 {#seq-exercises}

#### 题1：有限前缀与像集合 {#seq-q01}

任给 $K\in\mathbb N$，写出两个 $\mathbb N\to\mathbb R$ 的完整规则，使前 $K$ 项相同而全函数不同，说明 $K=0$ 的意义。再用除2余数构造两个像集合都为 $\{0,1\}$ 而不同的数列，核查函数合法性和不同的输入见证。[完整解答](#seq-a01)

#### 题2：否定的是哪个量词 {#seq-q02}

对固定实数 $L$ 写出收敛定义和完整否定；再写“不存在实数极限”的量词。证明常数列零不趋于一却有极限。另证：把定义中的误差条件换成 $|a_n-L|\le\varepsilon$，所得定义与原严格定义等价，不能只说“小于和小于等于一样”。[完整解答](#seq-a02)

#### 题3：两份阈值必须同时有效 {#seq-q03}

设 $a_n\to L$ 且 $a_n\to M$。从 $L\ne M$ 时的正数 $\delta=|L-M|$ 出发，用 $\delta/3$、自然二元最大值和三角不等式证明 $L=M$。解释为何可选一个确实存在的共同尾部指标，以及为何证明之后才能把极限写成唯一值。[完整解答](#seq-a03)

#### 题4：常数列改掉前若干项 {#seq-q04}

设 $C\in\mathbb R$、$K\in\mathbb N$，$a:\mathbb N\to\mathbb R$ 满足所有 $n\ge K$ 都有 $a_n=C$，较早各项可为任意实数。直接按定义证明 $a_n\to C$，包括 $K=0$。再对一般最终相同的两全数列，证明共享同一个指定极限的两个方向。[完整解答](#seq-a04)

#### 题5：每个分母都要先合法 {#seq-q05}

完整证明 $b_n=1/(\nu(n)+1)$ 是从含零的自然数集到实数集的函数，并由 RA1 证明 $b_n\to0$。必须给任意正 $\varepsilon$ 的阈值构造、全部 $n\ge N$ 的界及正倒数反序的条件。解释 $1/\nu(n)$ 为什么不能照此定义同一域上的全函数。[完整解答](#seq-a05)

#### 题6：最早阈值与尾移的反方向 {#seq-q06}

对题5的列，求误差 $1/10$ 与 $1/100$ 下最早的自然阈值，分别证明充分与更早必失败。另设 $a:\mathbb N\to\mathbb R$、$k\in\mathbb N$，任给实数 $L$，证明 $a_{n+k}\to L$ 当且仅当 $a_n\to L$；反向先证所用自然差存在，再证新指标不小于阈值。[完整解答](#seq-a06)

#### 题7：每个尾部都有两种值 {#seq-q07}

以除2余数定义 $c_n\in\{0,1\}$，证明它有界却不收敛。对每个自然阈值 $N$，必须给出尾部中取0、取1的明确指标，并用同一个误差阈值反驳任意候选实数 $L$；不能引用子列定理或实数整数幂。[完整解答](#seq-a07)

#### 题8：两种“看起来接近”的错误 {#seq-q08}

有人说：“每个尾部总能找到一项等于零，所以数列趋零。”用题7的列给完整反驳。又有人说：“正项逐项严格变小，所以趋零。”对 $p_n=1+1/(\nu(n)+1)$，先证明它为正且严格递减，再直接按定义证明它趋于1，并证明不趋于0。尚未证明数列四则运算法则，不得调用它们。[完整解答](#seq-a08)

### 6. 来源与边界 {#seq-source-boundary}

本单元的标准定义与条件对照 Lebl《Basic Analysis I》固定公开版本的序列章；实际读取范围、URL、时间与双许可条件见[本批来源记录](#real-sequences-sources)。原文从1索引，本书从0索引，所有倒数与尾移已按本书类型重新核验。正文、练习和解答独立编写，没有复制外部题解或用外部省略替代证明。本单元未建立一般级数、单调收敛、子列、柯西列或连续性；这些目标留在后续依赖链中。
