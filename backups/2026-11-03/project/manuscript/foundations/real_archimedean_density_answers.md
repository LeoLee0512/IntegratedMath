## 基础单元 B2.31 课后题完整解答 {#realarch-answers}

以下解答对应[实数的自然数界、阿基米德性质与有理稠密](#realarch-unit)。$i:\mathbb Q\to\mathbb R$ 把有理数送到严格下段，$\eta:\mathbb N\to\mathbb Q$ 是已有复合嵌入，$\nu=i\circ\eta$。实数运算用 $\oplus,\ominus,N,\otimes,\oslash$；有理数运算保留通常符号。每次使用 $\operatorname{Inv}$ 或 $\oslash$ 都先核非零条件。

### 题1完整解答：分清自然数、有理数和实数副本 {#realarch-a01}

[返回题目](#realarch-q01)

各映射的域与目标为

$$
\iota:\mathbb N\to\mathbb Z,\qquad
j:\mathbb Z\to\mathbb Q,\qquad
\eta:\mathbb N\to\mathbb Q,\quad \eta(n)=j(\iota(n)),
$$

$$
i:\mathbb Q\to\mathbb R,\quad
i(r)=\{q\in\mathbb Q:q<r\},\qquad
\nu:\mathbb N\to\mathbb R,\quad \nu(n)=i(\eta(n)).
$$

两次复合的中间域都匹配：$\iota(n)$ 是整数，可输入 $j$；$\eta(n)$ 是有理数，可输入 $i$。已有嵌入保零、一，因此

$$
\nu(0)=i(\eta(0))=i(0)=0_{\mathbb R},\qquad
\nu(1)=i(\eta(1))=i(1)=1_{\mathbb R}.
$$

【依据：[复合嵌入的相容性](#pow-compatibility)及实数零、一的定义；$i$ 内的零、一是有理数。】

对 $m,n\in\mathbb N$，$\eta$ 保加法先给

$$
\eta(m+n)=\eta(m)+\eta(n).
$$

左边的 $m+n$ 是自然加法，右边是有理加法。把两边送入 $i$，再用[DA4](#cutadd-rational)，得到

$$
\begin{aligned}
\nu(m+n)
&=i(\eta(m+n))\\
&=i(\eta(m)+\eta(n))\\
&=i(\eta(m))\oplus i(\eta(n))\\
&=\nu(m)\oplus\nu(n).
\end{aligned}
$$

最后两行是分割之间的运算。每次换写均来自已证相容，而不是把三个数系的加号先视为同一操作。

最后，$\eta$ 与 $i$ 分别保持并反映严格序，所以

$$
n>0
\quad\Longleftrightarrow\quad
\eta(n)>\eta(0)=0
\quad\Longleftrightarrow\quad
i(\eta(n))>_{\mathbb R}i(0).
$$

最右边就是 $\nu(n)>_{\mathbb R}0_{\mathbb R}$。两个方向都成立；反向使用的是次序反映，不能仅由“单射”二字推出。

### 题2完整解答：从外点证明严格自然数界 {#realarch-a02}

[返回题目](#realarch-q02)

给定 $A\in\mathbb R$。因为分割是真子集，取 $r\in\mathbb Q$ 且 $r\notin A$。[QG1](#qgap-density-archimedean)对有理输入 $r$ 给正自然数 $n$，使

$$
r<\eta(n).
$$

任取 $a\in A$。有理三歧性列出 $a<r$、$a=r$、$r<a$。第二种直接违反 $r\notin A$；第三种由 $A$ 下闭同样得到 $r\in A$。因此只有 $a<r$，继而 $a<\eta(n)$。所以每个 $a\in A$ 都属于 $i(\eta(n))=\nu(n)$，即 $A\subseteq\nu(n)$。

包含严格需要额外见证。因为 $r<\eta(n)$ 而 $r\notin A$，

$$
r\in\nu(n)\setminus A.
$$

所以 $A\ne\nu(n)$，得到 $A<_{\mathbb R}\nu(n)$。所取 $n>0$ 也是QG1结论的一部分。

再看 $\mathcal T$。若 $n>0$，自然数前驱结论给 $n=1+k$，其中 $k\in\mathbb N$，所以 $n\ge1$。$\eta$ 保序给 $\eta(n)\ge1>0$；倒数有定义，并且有理正倒数反序给

$$
0<\frac1{\eta(n)}\le1.
$$

送入 $i$ 得

$$
0_{\mathbb R}<_{\mathbb R}i\!\left(\frac1{\eta(n)}\right)
\le_{\mathbb R}i(1)=1_{\mathbb R}.
$$

这对 $\mathcal T$ 的每个成员成立，所以 $1_{\mathbb R}$ 是上界。

若 $0<n<m$，有理嵌入给 $0<\eta(n)<\eta(m)$。两数均正，可以使用严格倒数反序：

$$
\frac1{\eta(m)}<\frac1{\eta(n)}.
$$

再经 $i$ 得

$$
i\!\left(\frac1{\eta(m)}\right)
<_{\mathbb R}
i\!\left(\frac1{\eta(n)}\right).
$$

因此不同正自然数给不同成员。对任意给定的正自然数 $M$，输入 $1,2,\ldots,M$ 就给 $M$ 个互不相同的成员；继续取后继还会得到新的成员。它们始终不超过 $1_{\mathbb R}$。成员数量没有统一有限限制与有上界可以同时成立，所以“成员无限多”不是无上界的证明；RA1必须实际构造超过给定实数的自然数像。

### 题3完整解答：双侧自然数界与无上界的量词 {#realarch-a03}

[返回题目](#realarch-q03)

$A$ 和 $N(A)$ 都属于 $\mathbb R$。由RA1单侧结论分别取正自然数 $n,m$，满足

$$
A<_{\mathbb R}\nu(n),\qquad
N(A)<_{\mathbb R}\nu(m).
$$

令 $k=n+m$。由 $0<m$，自然数平移比较给 $n<n+m=k$。由 $0<n$，给 $m<m+n=k$，最后用自然加法交换律。因此 $k>0$，且 $\nu$ 保序给

$$
\nu(n)<_{\mathbb R}\nu(k),\qquad
\nu(m)<_{\mathbb R}\nu(k).
$$

与原比较分别连接，得到

$$
A<_{\mathbb R}\nu(k),\qquad
N(A)<_{\mathbb R}\nu(k).
$$

把第二式取反，取反反序及双重取反给

$$
N(\nu(k))<_{\mathbb R}N(N(A))=A.
$$

所以同一个 $k$ 满足双侧界。这个论证没有使用尚未在本题定义的实数绝对值。

要证明 $\nu(\mathbb N)$ 无上界，假设有 $U\in\mathbb R$，满足每个自然数 $n$ 都有 $\nu(n)\le_{\mathbb R}U$。对实数 $A=U$ 使用RA1，得到一个正自然数 $n$，却有 $U<_{\mathbb R}\nu(n)$。两式矛盾，所以该上界不存在。

RA1的量词次序是

$$
\text{对每个 }A\in\mathbb R,\quad
\text{存在正自然数 }n,\quad A<_{\mathbb R}\nu(n).
$$

$n$ 可以依赖 $A$。若错误地改成“存在一个 $n$，对所有 $A$ 都成立”，令 $A=\nu(n)$，就会要求 $\nu(n)<_{\mathbb R}\nu(n)$，违反严格序的非自反性。

### 题4完整解答：换一个正单位仍能越过目标 {#realarch-a04}

[返回题目](#realarch-q04)

条件为 $X>_{\mathbb R}0_{\mathbb R}$、$Y\in\mathbb R$。先由 $X\ne0_{\mathbb R}$ 确认

$$
Y\oslash X=Y\otimes\operatorname{Inv}(X)
$$

是已定义的实数。对它用RA1，选正自然数 $n$，使

$$
Y\oslash X<_{\mathbb R}\nu(n).
$$

共同因子 $X$ 严格为正，故[SR3](#cutring-multiplication-order)给

$$
(Y\oslash X)\otimes X
<_{\mathbb R}\nu(n)\otimes X.
$$

由于分母 $X$ 非零，[DQ1](#cutdiv-definition)允许将左侧乘回成 $Y$。因此 $Y<_{\mathbb R}\nu(n)\otimes X$。这里不需要 $Y$ 非负；目标可以是任意实数。

倍率的起点为

$$
\nu(0)\otimes X=0_{\mathbb R}\otimes X=0_{\mathbb R}.
$$

下一步使用 $\nu$ 保加法与一，得到

$$
\nu(n+1)=\nu(n)\oplus1_{\mathbb R}.
$$

两边乘 $X$，由全分配和单位，

$$
\begin{aligned}
\nu(n+1)\otimes X
&=(\nu(n)\oplus1_{\mathbb R})\otimes X\\
&=(\nu(n)\otimes X)\oplus(1_{\mathbb R}\otimes X)\\
&=(\nu(n)\otimes X)\oplus X.
\end{aligned}
$$

所以每当自然指标加一，倍率的值就增加一个 $X$。这用具体递推说明了“自然数倍率”，没有预设一般实数有限求和规则。

最后核给定算例。$2/5>0$，故 $X=i(2/5)>_{\mathbb R}0_{\mathbb R}$；$n=6>0$。有理乘法相容给

$$
\nu(6)\otimes X=i(6)\otimes i(2/5)=i(12/5).
$$

有理数的正分母计算给

$$
\frac{12}{5}-\frac73=\frac{36}{15}-\frac{35}{15}=\frac1{15}>0.
$$

因此 $7/3<12/5$，嵌入保序给 $Y<_{\mathbb R}\nu(6)\otimes X$，代入核验完成。这个具体见证并不取代对所有 $X>0,Y$ 的一般存在证明。

### 题5完整解答：倒数能小到什么程度 {#realarch-a05}

[返回题目](#realarch-q05)

给定 $\varepsilon>_{\mathbb R}0_{\mathbb R}$，先核 $\varepsilon\ne0_{\mathbb R}$。[IR3](#cutinv-signed-unique)给它的逆元有定义且为正：

$$
\operatorname{Inv}(\varepsilon)>_{\mathbb R}0_{\mathbb R}.
$$

对该实数使用RA1，取正自然数 $n$，满足

$$
\operatorname{Inv}(\varepsilon)<_{\mathbb R}\nu(n).
$$

$n>0$ 经嵌入给 $\nu(n)>_{\mathbb R}0_{\mathbb R}$，所以比较两端都正。对这两个输入使用[DQ3](#cutdiv-order)的严格正倒数反序，得

$$
\operatorname{Inv}(\nu(n))
<_{\mathbb R}
\operatorname{Inv}(\operatorname{Inv}(\varepsilon)).
$$

IR3保证 $\operatorname{Inv}(\varepsilon)$ 非零，因而右侧第二次取倒数合法。[IR4](#cutinv-rational-identities)把它化为 $\varepsilon$。另外，正输入 $\nu(n)$ 的逆元也正，合起来是

$$
0_{\mathbb R}<_{\mathbb R}\operatorname{Inv}(\nu(n))
<_{\mathbb R}\varepsilon.
$$

由 $n>0$ 得有理数 $\eta(n)>0$，所以 $1/\eta(n)$ 合法。IR4的有理相容给

$$
\operatorname{Inv}(\nu(n))
=\operatorname{Inv}(i(\eta(n)))
=i\!\left(\frac1{\eta(n)}\right).
$$

例中 $\varepsilon=i(3/10)>_{\mathbb R}0_{\mathbb R}$，$n=4>0$。有理差为

$$
\frac3{10}-\frac14=\frac6{20}-\frac5{20}=\frac1{20}>0,
$$

且 $1/4>0$，所以

$$
0_{\mathbb R}<_{\mathbb R}i(1/4)
<_{\mathbb R}i(3/10)=\varepsilon.
$$

由逆元相容，$i(1/4)=\operatorname{Inv}(\nu(4))$，验证完成。

若 $n=0$，$\nu(n)=0_{\mathbb R}$，本书的 $\operatorname{Inv}$ 在该处没有定义。若 $\varepsilon=0_{\mathbb R}$，所要求的严格链会成为 $0_{\mathbb R}<_{\mathbb R}Z<_{\mathbb R}0_{\mathbb R}$，由传递性得到零严格小于自身，矛盾。两项条件都不可省。

本题只证明对每个正宽度存在一个正自然指标。没有给“数列”“收敛”的定义，也没有把本题陈述改写成一个已经证明的极限定理。

### 题6完整解答：稠密性需要两份严格见证 {#realarch-a06}

[返回题目](#realarch-q06)

由 $A<_{\mathbb R}B$ 得 $A\subseteq B$ 且 $A\ne B$。所以存在有理数 $r\in B\setminus A$；再由分割 $B$ 无最大元，取有理数 $s\in B$ 且 $r<s$。

**第一个包含。** 任取 $a\in A$。因 $r\notin A$，若 $a=r$ 就直接矛盾，若 $r<a$ 就由 $A$ 下闭推出 $r\in A$。故 $a<r<s$，于是 $a\in i(s)$。这对所有 $a\in A$ 成立，所以 $A\subseteq i(s)$。

**第一个不等。** 因 $r<s$，$r\in i(s)$；而选取时有 $r\notin A$。因此两集合有不同成员，$A\ne i(s)$。结合前一包含得到 $A<_{\mathbb R}i(s)$。

**第二个包含。** 任取 $q\in i(s)$，有 $q<s$。$s\in B$ 且 $B$ 下闭，故 $q\in B$。所以 $i(s)\subseteq B$。

**第二个不等。** $s\in B$，但是 $s\notin i(s)$，因为 $s<s$ 不成立。故 $i(s)\ne B$，从而 $i(s)<_{\mathbb R}B$。

两边严格比较的见证分别是 $r$ 与 $s$；二者承担不同任务。

对反例取 $A=i(0)$、$B=i(1)$。有理 $0<1$ 经嵌入给 $A<_{\mathbb R}B$。$r=0$ 满足 $r\in B$，因为 $0<1$；也满足 $r\notin A$，因为 $0<0$ 为假。但

$$
i(r)=i(0)=A.
$$

所以只凭 $r\in B\setminus A$，无法得到 $A<_{\mathbb R}i(r)$。需要利用 $B$ 的无最大元条件再取 $s>r$，才能得到两个严格比较。

### 题7完整解答：总宽度与两侧误差都要证明 {#realarch-a07}

[返回题目](#realarch-q07)

给定 $A\in\mathbb R$、$\varepsilon>_{\mathbb R}0_{\mathbb R}$。由有理嵌入保序，$2_{\mathbb R}=i(2)>_{\mathbb R}0_{\mathbb R}$。因此

$$
E=\varepsilon\oslash2_{\mathbb R}
$$

合法。将 $0_{\mathbb R}<_{\mathbb R}\varepsilon$ 同除以正 $2_{\mathbb R}$，商比较与零分子公式给

$$
0_{\mathbb R}=0_{\mathbb R}\oslash2_{\mathbb R}
<_{\mathbb R}E.
$$

DA4给 $1_{\mathbb R}\oplus1_{\mathbb R}=i(1+1)=i(2)=2_{\mathbb R}$。利用分配及乘回，

$$
\begin{aligned}
E\oplus E
&=(E\otimes1_{\mathbb R})\oplus(E\otimes1_{\mathbb R})\\
&=E\otimes(1_{\mathbb R}\oplus1_{\mathbb R})\\
&=E\otimes2_{\mathbb R}\\
&=(\varepsilon\oslash2_{\mathbb R})\otimes2_{\mathbb R}
=\varepsilon.
\end{aligned}
$$

【依据：乘法单位、分配、二的表达式及DQ1；所有除法的分母均是已证正的 $2_{\mathbb R}$。】

由 $E>_{\mathbb R}0_{\mathbb R}$，取反与平移给

$$
A\ominus E<_{\mathbb R}A,\qquad
A<_{\mathbb R}A\oplus E.
$$

这两个比较分别满足RA3的严格条件。先在第一对之间选有理数 $p$，再在第二对之间选有理数 $q$，得到

$$
A\ominus E<_{\mathbb R}i(p)<_{\mathbb R}A
<_{\mathbb R}i(q)<_{\mathbb R}A\oplus E.
$$

特别地 $i(p)<_{\mathbb R}i(q)$；由 $i$ 反映次序，得 $p<q$。

下面证明宽度上界，不能只凭图形判断。对左端比较 $A\ominus E<_{\mathbb R}i(p)$ 取反，得

$$
N(i(p))<_{\mathbb R}N(A\ominus E).
$$

把右侧按群规律展开：

$$
N(A\ominus E)
=N(A\oplus N(E))
=N(A)\oplus N(N(E))
=N(A)\oplus E.
$$

【依据：差的定义、和的取反与双重取反。】因此

$$
N(i(p))<_{\mathbb R}N(A)\oplus E.
$$

先对 $i(q)<_{\mathbb R}A\oplus E$ 同加 $N(i(p))$：

$$
i(q)\ominus i(p)
<_{\mathbb R}(A\oplus E)\oplus N(i(p)).
$$

再对 $N(i(p))<_{\mathbb R}N(A)\oplus E$ 同加 $A\oplus E$，用交换律调整共同加项的位置：

$$
(A\oplus E)\oplus N(i(p))
<_{\mathbb R}(A\oplus E)\oplus(N(A)\oplus E).
$$

最后用加法交换、结合与逆元整理右端：

$$
\begin{aligned}
(A\oplus E)\oplus(N(A)\oplus E)
&=(A\oplus N(A))\oplus(E\oplus E)\\
&=0_{\mathbb R}\oplus\varepsilon=\varepsilon.
\end{aligned}
$$

连续使用两次严格传递，得到 $i(q)\ominus i(p)<_{\mathbb R}\varepsilon$。

宽度还应为正。由 $i(p)<_{\mathbb R}i(q)$ 同加 $N(i(p))$，得到

$$
0_{\mathbb R}<_{\mathbb R}i(q)\ominus i(p).
$$

差的有理相容逐步写为

$$
\begin{aligned}
i(q)\ominus i(p)
&=i(q)\oplus N(i(p))\\
&=i(q)\oplus i(-p)\\
&=i(q-p).
\end{aligned}
$$

【依据：差的定义，DA4的取反相容和加法相容。】所以

$$
0_{\mathbb R}<_{\mathbb R}i(q-p)<_{\mathbb R}\varepsilon.
$$

左侧误差由 $i(p)<_{\mathbb R}A<_{\mathbb R}i(q)$ 同加 $N(i(p))$ 得到：

$$
0_{\mathbb R}<_{\mathbb R}A\ominus i(p)
<_{\mathbb R}i(q)\ominus i(p)
<_{\mathbb R}\varepsilon.
$$

右侧误差的正性由 $A<_{\mathbb R}i(q)$ 同加 $N(A)$ 得到。再从 $i(p)<_{\mathbb R}A$ 取反，得到 $N(A)<_{\mathbb R}N(i(p))$；同加 $i(q)$，有

$$
0_{\mathbb R}<_{\mathbb R}i(q)\ominus A
<_{\mathbb R}i(q)\ominus i(p)
<_{\mathbb R}\varepsilon.
$$

至此夹逼、正总宽度及两侧严格误差界都已经证明。本题是给定 $A,\varepsilon$ 的存在结论，不要求为任意分割实现成员搜索。

### 题8完整解答：插入两个有理像与唯一识别 {#realarch-a08}

[返回题目](#realarch-q08)

先设 $A<_{\mathbb R}B$。RA3给一个 $p\in\mathbb Q$，使

$$
A<_{\mathbb R}i(p)<_{\mathbb R}B.
$$

$i(p)$ 与 $B$ 都是实数，且中间比较严格，故可以再对这一对应用RA3，取 $q\in\mathbb Q$，使

$$
i(p)<_{\mathbb R}i(q)<_{\mathbb R}B.
$$

合并即得 $A<_{\mathbb R}i(p)<_{\mathbb R}i(q)<_{\mathbb R}B$。嵌入反映严格序给 $p<q$，所以确是两个不同的有理数。

再设 $A,B$ 满足题给的全称条件：

$$
\text{对每个 }q\in\mathbb Q,\qquad
i(q)<_{\mathbb R}A
\quad\Longleftrightarrow\quad
i(q)<_{\mathbb R}B.
$$

分割全序给 $A<B$、$A=B$、$B<A$ 三种可能，其中这里的比较均为 $\mathbb R$ 的比较。

若 $A<_{\mathbb R}B$，由RA3选 $q\in\mathbb Q$ 使 $A<_{\mathbb R}i(q)<_{\mathbb R}B$。因为 $i(q)<_{\mathbb R}B$，题给等价的反向迫使 $i(q)<_{\mathbb R}A$。它与 $A<_{\mathbb R}i(q)$ 合并会给 $A<_{\mathbb R}A$，矛盾。因此 $A<_{\mathbb R}B$ 不可能。

若 $B<_{\mathbb R}A$，RA3选 $q\in\mathbb Q$ 使 $B<_{\mathbb R}i(q)<_{\mathbb R}A$。这次 $i(q)<_{\mathbb R}A$ 经题给等价的正向推出 $i(q)<_{\mathbb R}B$，与 $B<_{\mathbb R}i(q)$ 矛盾。因此第二种严格次序也不可能。

三歧性只留下 $A=B$。证明使用的是“所有严格有理像下界相同”这一信息；没有从这些下界中选出一个恰好等于 $A$ 的有理像。因此它不意味着 $i$ 满射，也不与[非主分割的存在](#cut-gap)冲突，更没有证明不同构造的完备有序域之间存在唯一同构。
