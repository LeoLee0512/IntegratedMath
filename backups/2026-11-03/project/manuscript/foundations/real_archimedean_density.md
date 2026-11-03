## 基础单元 B2.31 实数的自然数界、阿基米德性质与有理稠密 {#realarch-unit}

**学习目标与位置。** 分割的运算已经提供有序域规则。现在分别回答三个问题：给定一个实数，是否有自然数的副本超过它？给定任意正实数作为单位，足够大的自然数倍率能否超过指定实数？给定两个不同实数，能否在它们之间放入一个有理数的副本？最后把第三个结论用于给定宽度的有理夹逼。主归属第526章97F50的实数基础教学部分；06A05全序、12J15有序域交叉。这些交叉只定位已经构造的有序域应用，不表示相应分类已经完整覆盖。实数平方根、数列极限与几何长度仍需各自的证明。

**精确先修。** 使用[函数定义](#fun-definition)、[复合函数](#fc-composition)、[自然数到有理数的复合嵌入](#pow-compatibility)、[有理自然数界及嵌入保序](#qgap-density-archimedean)、[正自然数的前驱](#ord-predecessor)与[自然数加法比较](#ord-addition-order)。分割使用[四项定义](#cut-definition)、[包含全序与有理嵌入](#cut-order-embedding)、[内外点分离](#cutadd-separation)、[加法和取反的有理相容](#cutadd-rational)、[加法群规则](#cutgroup-laws)、[双向序平移](#cutgroup-translation)、[取反及差的比较](#cutgroup-negation-subtraction)。运算使用[乘法单位与符号](#cutsigned-signs)、[有理乘法相容](#cutsigned-rational-zero)、[全分配律](#cutring-distributive)、[正因子比较](#cutring-multiplication-order)、[非零逆元及其符号](#cutinv-signed-unique)、[双倒数与有理相容](#cutinv-rational-identities)、[除法及乘回](#cutdiv-definition)、[商比较与正倒数反序](#cutdiv-order)。题2另用[有理正倒数反序](#rord-a08)。本单元只对这些已构造的对象应用规则，不由“有序域”这个名称直接推出阿基米德性。

**对象与记号。** $A,X,Y,E,\varepsilon$ 表示实数，也就是本书的分割；$p,q,r,s$ 表示有理数；$m,n,k$ 表示自然数。沿用实数加法 $\oplus$、相反数 $N$、差 $\ominus$、乘法 $\otimes$ 与非零分母商 $\oslash$；$\le_{\mathbb R}$ 仍是分割间的包含。零、一和二分别记作

$$
0_{\mathbb R}=i(0),\qquad
1_{\mathbb R}=i(1),\qquad
2_{\mathbb R}=i(2).
$$

$0_{\mathbb R}<_{\mathbb R}1_{\mathbb R}<_{\mathbb R}2_{\mathbb R}$ 来自有理嵌入保序。

### 1. 自然数怎样进入分割集合 {#realarch-embedding}

先保留各层对象的区别。已有映射为

$$
\iota:\mathbb N\to\mathbb Z,\qquad
j:\mathbb Z\to\mathbb Q,\qquad
\eta=j\circ\iota:\mathbb N\to\mathbb Q,\qquad
i:\mathbb Q\to\mathbb R.
$$

定义自然数到实数的映射

$$
\nu:\mathbb N\to\mathbb R,\qquad
\nu(n)=i(\eta(n)).
$$

每个 $\eta(n)$ 是有理数，因而可输入 $i$；输出是分割。已有嵌入相容给

$$
\nu(0)=i(0)=0_{\mathbb R},\qquad
\nu(1)=i(1)=1_{\mathbb R}.
$$

对自然数 $m,n$，先在有理层使用 $\eta$ 的相容，再进入实数层：

$$
\nu(m+n)=i(\eta(m)+\eta(n))
          =\nu(m)\oplus\nu(n).
$$

【依据：$\eta$ 保加法；[DA4](#cutadd-rational)给 $i(a+b)=i(a)\oplus i(b)$。左侧括号内是自然加法，中间括号内是有理加法，右侧是分割加法。】

两次次序嵌入也给

$$
m<n
\quad\Longleftrightarrow\quad
\eta(m)<\eta(n)
\quad\Longleftrightarrow\quad
\nu(m)<_{\mathbb R}\nu(n).
$$

不严格比较同样保持并反映。因此 $\nu$ 单射，且 $n>0$ 当且仅当 $\nu(n)>_{\mathbb R}0_{\mathbb R}$。下文的自然数界是形如 $\nu(n)$ 的实数，不是把自然数对象直接当成有理子集。

### 2. 用一个有理外点取得自然数界 {#realarch-natural-bound}

**命题 RA1。** 对每个 $A\in\mathbb R$，存在正自然数 $n$，使

$$
A<_{\mathbb R}\nu(n).
$$

因此自然数嵌入像 $\nu(\mathbb N)$ 在 $\mathbb R$ 内没有上界。并且对每个 $A$，存在正自然数 $k$，使

$$
N(\nu(k))<_{\mathbb R}A<_{\mathbb R}\nu(k).
$$

**先证明单侧界。** 分割 $A$ 不等于整个 $\mathbb Q$，所以可以取

$$
r\in\mathbb Q,\qquad r\notin A.
$$

[QG1](#qgap-density-archimedean)对这个有理数给出正自然数 $n$，使 $r<\eta(n)$。这里调用的是已经在有理数中证明的界性质。

任取 $a\in A$。若 $a=r$，则与 $r\notin A$ 矛盾；若 $r<a$，$A$ 下闭也会给 $r\in A$。有理数三歧性只留下 $a<r$。于是

$$
a<r<\eta(n),
$$

所以 $a\in i(\eta(n))=\nu(n)$。这证明 $A\subseteq\nu(n)$。

还须证明包含严格。所选外点恰好给出见证：

$$
r\in\nu(n),\qquad r\notin A.
$$

第一项因为 $r<\eta(n)$。因此 $A\ne\nu(n)$，合起来就是 $A<_{\mathbb R}\nu(n)$。正自然数 $n$ 的存在来自QG1，不是由“自然数无限”直接推断。

**自然数像无上界。** 若某个 $U\in\mathbb R$ 是 $\nu(\mathbb N)$ 的上界，就应对每个 $n\in\mathbb N$ 有 $\nu(n)\le_{\mathbb R}U$。把刚证结论应用于 $A=U$，却得到某个正自然数 $n$ 使 $U<_{\mathbb R}\nu(n)$，矛盾。所以没有这样的 $U$。

**双侧界。** 对 $A$ 与 $N(A)$ 分别使用单侧结论，取正自然数 $n,m$，使

$$
A<_{\mathbb R}\nu(n),\qquad
N(A)<_{\mathbb R}\nu(m).
$$

令 $k=n+m$。由 $m>0$ 和 $n>0$，自然数加法严格比较给 $n<k$、$m<k$，而且 $k>0$。嵌入保序得到

$$
A<_{\mathbb R}\nu(n)<_{\mathbb R}\nu(k),\qquad
N(A)<_{\mathbb R}\nu(m)<_{\mathbb R}\nu(k).
$$

对第二串比较取反，使用双重取反，得 $N(\nu(k))<_{\mathbb R}A$。与第一串合并即得双侧界。这里没有另外定义实数绝对值。RA1证毕。

### 3. 任意正单位的倍率，以及任意小的正倒数 {#realarch-scaled-reciprocal}

**命题 RA2。** 若 $X>_{\mathbb R}0_{\mathbb R}$，$Y\in\mathbb R$ 任意，则存在正自然数 $n$，使

$$
Y<_{\mathbb R}\nu(n)\otimes X.
$$

这称为本单元采用的实数**阿基米德性质**。此外，对每个正实数 $\varepsilon$，存在正自然数 $n$，使

$$
0_{\mathbb R}
<_{\mathbb R}\operatorname{Inv}(\nu(n))
<_{\mathbb R}\varepsilon,
\qquad
\operatorname{Inv}(\nu(n))=i\!\left(\frac1{\eta(n)}\right).
$$

**正单位的倍率。** $X>_{\mathbb R}0_{\mathbb R}$ 保证 $X\ne0_{\mathbb R}$，所以 $Y\oslash X$ 是已定义的实数。RA1给正自然数 $n$，使

$$
Y\oslash X<_{\mathbb R}\nu(n).
$$

两边乘同一个正实数 $X$，保持严格比较：

$$
(Y\oslash X)\otimes X
<_{\mathbb R}\nu(n)\otimes X.
$$

【依据：[SR3](#cutring-multiplication-order)，正因子是 $X$，分子 $Y$ 无需为正。】[DQ1](#cutdiv-definition)把左侧化为 $Y$，得到所求结论。

这里的 $\nu(n)\otimes X$ 是实数乘积，可称 $X$ 的自然数倍率。它确实符合从零开始每次增加 $X$ 的规则：

$$
\nu(0)\otimes X=0_{\mathbb R},
$$

$$
\begin{aligned}
\nu(n+1)\otimes X
&=(\nu(n)\oplus1_{\mathbb R})\otimes X\\
&=(\nu(n)\otimes X)\oplus X.
\end{aligned}
$$

【依据：$\nu$ 保加法与一、分配律及乘法单位。】这解释了“倍率”的含义；这里没有另行使用一个尚未定义的实数有限和函数。

**例。** 取 $X=i(2/5)$、$Y=i(7/3)$。有理嵌入保序给 $X>_{\mathbb R}0_{\mathbb R}$。正自然数 $n=6$ 是一个可用见证，因为

$$
\nu(6)\otimes X=i(6)\otimes i(2/5)=i(12/5),
$$

而有理差

$$
\frac{12}{5}-\frac73=\frac{36-35}{15}=\frac1{15}>0
$$

给出 $Y<_{\mathbb R}\nu(6)\otimes X$。这是一个输入的核验，一般存在性由前面的证明给出。

**任意小的正倒数。** 固定 $\varepsilon>_{\mathbb R}0_{\mathbb R}$。它非零，且[IR3](#cutinv-signed-unique)保证 $\operatorname{Inv}(\varepsilon)>_{\mathbb R}0_{\mathbb R}$。对这个实数使用RA1，取正自然数 $n$，使

$$
\operatorname{Inv}(\varepsilon)<_{\mathbb R}\nu(n).
$$

两端都正：[IR3](#cutinv-signed-unique)给左端正，$\nu$ 保序给右端正。因此可以应用[DQ3的严格正倒数反序](#cutdiv-order)：

$$
\operatorname{Inv}(\nu(n))
<_{\mathbb R}\operatorname{Inv}(\operatorname{Inv}(\varepsilon))
=\varepsilon.
$$

【依据：正倒数反序；[IR4](#cutinv-rational-identities)的双倒数公式。第二次取倒数合法，因为第一次输出非零。】同时 $\nu(n)>_{\mathbb R}0_{\mathbb R}$ 的逆元为正，所以两侧严格界都成立。

还要核对有理写法。由 $n>0$ 得 $\eta(n)>0$，故有理数 $1/\eta(n)$ 有定义；IR4给

$$
\operatorname{Inv}(\nu(n))
=\operatorname{Inv}(i(\eta(n)))
=i\!\left(\frac1{\eta(n)}\right).
$$

RA2证毕。

$n=0$ 不能代入倒数，因为 $\nu(0)=0_{\mathbb R}$。$\varepsilon=0_{\mathbb R}$ 也不能替代正性条件，因为不存在同时严格大于零又严格小于零的实数。命题说每次给定正 $\varepsilon$ 后存在相应的 $n$，没有把量词换成“一个 $n$ 适合所有正 $\varepsilon$”，也没有在这里定义或证明数列收敛。

### 4. 两个实数之间的有理下段 {#realarch-rational-density}

**命题 RA3。** 若 $A,B\in\mathbb R$ 且 $A<_{\mathbb R}B$，则存在 $s\in\mathbb Q$，使

$$
A<_{\mathbb R}i(s)<_{\mathbb R}B.
$$

这称为有理嵌入像 $i(\mathbb Q)$ 在 $\mathbb R$ 中**稠密**。这里比较的是三个分割；中间分割来自有理数。

**证明。** 严格包含 $A\subsetneq B$ 提供一个有理见证

$$
r\in B,\qquad r\notin A.
$$

因为 $B$ 无最大元，可再选有理数 $s$，使

$$
s\in B,\qquad r<s.
$$

先证明左边的严格比较。任意 $a\in A$ 与外点 $r\notin A$ 满足 $a<r$，所以 $a<r<s$，从而 $a\in i(s)$。因此 $A\subseteq i(s)$。又因为 $r<s$，

$$
r\in i(s),\qquad r\notin A,
$$

故包含严格，即 $A<_{\mathbb R}i(s)$。

再证明右边的严格比较。若 $q\in i(s)$，则 $q<s$；由于 $s\in B$ 且 $B$ 下闭，得到 $q\in B$。因此 $i(s)\subseteq B$。另一个见证是 $s$ 本身：

$$
s\in B,\qquad s\notin i(s).
$$

后者因为有理严格序不允许 $s<s$。故 $i(s)<_{\mathbb R}B$。两边合并，RA3证毕。

**为什么要再取一次较大内点？** 只取 $r\in B\setminus A$，并不能保证 $A<_{\mathbb R}i(r)$。例如

$$
A=i(0),\qquad B=i(1),\qquad r=0.
$$

由于 $0<1$，有 $r\in B$；由于 $0\not<0$，有 $r\notin A$。但是 $i(r)=i(0)=A$。第二次取 $s>r$，才使 $r$ 成为 $i(s)$ 中而不在 $A$ 中的严格见证。

这一证明只用了分割四条件与有理比较，没有借助实数序列、整数取整函数或RA2。稠密只回答两个不同实数之间能否找到有理像；它不宣称每个实数都等于某个 $i(q)$。此前的[非主分割](#cut-gap)已经说明后者不成立。

### 5. 在任意给定正宽度内夹住一个实数 {#realarch-rational-brackets}

**命题 RA4。** 给定 $A\in\mathbb R$ 和 $\varepsilon>_{\mathbb R}0_{\mathbb R}$，存在 $p,q\in\mathbb Q$，使

$$
i(p)<_{\mathbb R}A<_{\mathbb R}i(q),
\qquad
0_{\mathbb R}<_{\mathbb R}i(q-p)<_{\mathbb R}\varepsilon.
$$

此时 $p<q$，并且两侧误差都满足

$$
0_{\mathbb R}<_{\mathbb R}A\ominus i(p)<_{\mathbb R}\varepsilon,
\qquad
0_{\mathbb R}<_{\mathbb R}i(q)\ominus A<_{\mathbb R}\varepsilon.
$$

**先取得正半量。** $2_{\mathbb R}>_{\mathbb R}0_{\mathbb R}$，所以定义

$$
E=\varepsilon\oslash2_{\mathbb R}.
$$

对 $0_{\mathbb R}<_{\mathbb R}\varepsilon$ 同除以正 $2_{\mathbb R}$，DQ3与 $0_{\mathbb R}\oslash2_{\mathbb R}=0_{\mathbb R}$ 给 $E>_{\mathbb R}0_{\mathbb R}$。由DA4，

$$
2_{\mathbb R}=1_{\mathbb R}\oplus1_{\mathbb R}.
$$

于是分配与乘回给

$$
\begin{aligned}
E\oplus E
&=(E\otimes1_{\mathbb R})\oplus(E\otimes1_{\mathbb R})\\
&=E\otimes(1_{\mathbb R}\oplus1_{\mathbb R})\\
&=(\varepsilon\oslash2_{\mathbb R})\otimes2_{\mathbb R}
=\varepsilon.
\end{aligned}
$$

**分别取得两个有理见证。** 由 $E>_{\mathbb R}0_{\mathbb R}$，取反给 $N(E)<_{\mathbb R}0_{\mathbb R}$，平移给

$$
A\ominus E<_{\mathbb R}A<_{\mathbb R}A\oplus E.
$$

对左侧一对实数使用RA3，取 $p\in\mathbb Q$；再对右侧一对使用RA3，取 $q\in\mathbb Q$，得到

$$
A\ominus E<_{\mathbb R}i(p)<_{\mathbb R}A
<_{\mathbb R}i(q)<_{\mathbb R}A\oplus E.
$$

**证明总宽度的上界。** 为把左侧的界变成相减时可用的界，先取反：

$$
N(i(p))<_{\mathbb R}N(A\ominus E)=N(A)\oplus E.
$$

【依据：取反严格反序；$A\ominus E=A\oplus N(E)$，和的取反及双重取反给右侧等式。】

在 $i(q)<_{\mathbb R}A\oplus E$ 两边同加 $N(i(p))$，得到

$$
i(q)\ominus i(p)
<_{\mathbb R}(A\oplus E)\oplus N(i(p)).
$$

再在刚证的 $N(i(p))<_{\mathbb R}N(A)\oplus E$ 两边同加 $A\oplus E$，得到

$$
(A\oplus E)\oplus N(i(p))
<_{\mathbb R}(A\oplus E)\oplus(N(A)\oplus E).
$$

右端只用加法群规则整理：

$$
(A\oplus E)\oplus(N(A)\oplus E)
=(A\oplus N(A))\oplus(E\oplus E)
=0_{\mathbb R}\oplus\varepsilon=\varepsilon.
$$

【依据：交换、结合、相反数及已经证明的 $E\oplus E=\varepsilon$。】传递性给 $i(q)\ominus i(p)<_{\mathbb R}\varepsilon$。

另一方面，$i(p)<_{\mathbb R}A<_{\mathbb R}i(q)$ 给 $i(p)<_{\mathbb R}i(q)$。同加 $N(i(p))$，得

$$
0_{\mathbb R}<_{\mathbb R}i(q)\ominus i(p).
$$

差的有理相容给 $i(q)\ominus i(p)=i(q-p)$；嵌入的次序反映还从 $i(p)<_{\mathbb R}i(q)$ 给出 $p<q$。因此总宽度确是正实数，且严格小于指定的 $\varepsilon$。

**证明两侧误差。** 由 $i(p)<_{\mathbb R}A<_{\mathbb R}i(q)$，同加 $N(i(p))$ 得

$$
0_{\mathbb R}<_{\mathbb R}A\ominus i(p)
<_{\mathbb R}i(q)\ominus i(p)<_{\mathbb R}\varepsilon.
$$

对于另一侧，$A<_{\mathbb R}i(q)$ 给 $0_{\mathbb R}<_{\mathbb R}i(q)\ominus A$。再把 $i(p)<_{\mathbb R}A$ 取反，得 $N(A)<_{\mathbb R}N(i(p))$；同加 $i(q)$ 后，

$$
i(q)\ominus A<_{\mathbb R}i(q)\ominus i(p)
<_{\mathbb R}\varepsilon.
$$

这完成了两个误差界。RA4证毕。

每次结论只要求对给定的 $A,\varepsilon$ 找到两个有理数见证。任意分割并没有附带可执行的成员判定程序；这个存在证明也没有提供对所有输入都能运行的搜索算法，更没有据此建立无穷小数或极限。

### 6. 课后题 {#realarch-exercises}

#### 题1：分清自然数、有理数和实数副本 {#realarch-q01}

写出 $\iota,j,\eta,i,\nu$ 的定义域与目标。证明 $\nu(0)=0_{\mathbb R}$、$\nu(1)=1_{\mathbb R}$、$\nu(m+n)=\nu(m)\oplus\nu(n)$，并证明 $n>0$ 当且仅当 $\nu(n)>_{\mathbb R}0_{\mathbb R}$。每个公式标清所用运算所在的数系。[完整解答](#realarch-a01)

#### 题2：从外点证明严格自然数界 {#realarch-q02}

对任意分割 $A$，取有理外点 $r$，由QG1选正自然数 $n$，逐成员证明 $A<_{\mathbb R}\nu(n)$，明确严格性的见证。再考察集合
$$
\mathcal T=\left\{i\!\left(\frac1{\eta(n)}\right):n\in\mathbb N,\ n>0\right\}.
$$
证明它有上界 $1_{\mathbb R}$，不同正自然数给不同成员，因此可取任意多的不同成员。说明为什么不能用“成员无限多”直接断言一个集合无上界。[完整解答](#realarch-a02)

#### 题3：双侧自然数界与无上界的量词 {#realarch-q03}

对 $A$ 和 $N(A)$ 分别取正自然数上界，用 $k=n+m$ 证明 $N(\nu(k))<_{\mathbb R}A<_{\mathbb R}\nu(k)$。另证 $\nu(\mathbb N)$ 在 $\mathbb R$ 内无上界；说明所证量词次序为何不是“存在一个自然数超过所有实数”。[完整解答](#realarch-a03)

#### 题4：换一个正单位仍能越过目标 {#realarch-q04}

给定 $X>_{\mathbb R}0_{\mathbb R}$ 与任意 $Y\in\mathbb R$，从商的合法性开始，证明存在正自然数 $n$ 使 $Y<_{\mathbb R}\nu(n)\otimes X$。核该倍率的零项与每次增加 $X$ 的递推。对 $X=i(2/5)$、$Y=i(7/3)$，验证 $n=6$ 是见证。[完整解答](#realarch-a04)

#### 题5：倒数能小到什么程度 {#realarch-q05}

对每个 $\varepsilon>_{\mathbb R}0_{\mathbb R}$，完整证明存在正自然数 $n$ 使 $0_{\mathbb R}<_{\mathbb R}\operatorname{Inv}(\nu(n))<_{\mathbb R}\varepsilon$，并证明它等于 $i(1/\eta(n))$。核 $\varepsilon=i(3/10)$ 时 $n=4$ 可用。解释 $n=0$、$\varepsilon=0_{\mathbb R}$ 为何不能放入该断言，以及本题是否已经定义了数列收敛。[完整解答](#realarch-a05)

#### 题6：稠密性需要两份严格见证 {#realarch-q06}

给定 $A<_{\mathbb R}B$，从 $r\in B\setminus A$ 和 $s\in B,\ r<s$ 出发，分别证明 $A\subseteq i(s)$、$A\ne i(s)$、$i(s)\subseteq B$、$i(s)\ne B$。用 $A=i(0),B=i(1),r=0$ 说明为什么不能直接以 $i(r)$ 代替 $i(s)$。[完整解答](#realarch-a06)

#### 题7：总宽度与两侧误差都要证明 {#realarch-q07}

给定 $A\in\mathbb R$、$\varepsilon>_{\mathbb R}0_{\mathbb R}$，先证明 $E=\varepsilon\oslash2_{\mathbb R}$ 正且 $E\oplus E=\varepsilon$，再两次使用RA3取得 $p,q\in\mathbb Q$。完整推出RA4的夹逼、总宽度及两侧误差界，并核 $p<q$。不得省略取反、相加不等式及差的嵌入相容。[完整解答](#realarch-a07)

#### 题8：插入两个有理像与唯一识别 {#realarch-q08}

先证明 $A<_{\mathbb R}B$ 时存在有理数 $p<q$，使 $A<_{\mathbb R}i(p)<_{\mathbb R}i(q)<_{\mathbb R}B$。再设 $A,B\in\mathbb R$ 满足：对每个 $q\in\mathbb Q$，$i(q)<_{\mathbb R}A$ 当且仅当 $i(q)<_{\mathbb R}B$。证明 $A=B$。说明这个结论与“每个实数都是有理像”有什么区别。[完整解答](#realarch-a08)

**来源与范围说明。** 公开教材与形式库中阿基米德性质的条件对照见[本批来源审计](#real-arch-sqrt-sources)。本单元的自然数界与有理稠密直接使用分割见证；倒数结论依赖此前实际构造的非零逆元。证明没有借用待证的实数平方根、实数序列或完备有序域唯一同构，也没有把存在见证当成任意分割上的判定算法。
