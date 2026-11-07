## 基础单元 B2.30 分割除法、乘法方程与有序域 {#cutdiv-unit}

**学习目标与位置。** 前一单元已经为每个非零分割构造唯一的乘法逆元。本单元据此定义除法，证明乘法方程和一次仿射方程的完整解集，再处理正负除数下的次序比较。最后逐项核对有序域的定义，并把原来分割包含序的上确界性质接到同一结构上。主归属第526章97F50的实数基础教学部分；06A05、06F25交叉。本单元全部证明建立后，12J15的有序域构造接口才具备相应实例，不意味着该分类的其余内容已经完成。

**精确先修。** 使用[非零逆元的存在、唯一性与同号性](#cutinv-signed-unique)、[有理逆相容及逆元恒等式](#cutinv-rational-identities)；乘法使用[交换、单位与乘零](#cutsigned-signs)、[全结合律](#cutsigned-associative)、[有理相容与零积](#cutsigned-rational-zero)、[非负乘积闭合与正性](#cutprod-definition)、[全分配](#cutring-distributive)、[正负因子的双向比较](#cutring-multiplication-order)及[非零消去](#cutring-cancellation)。加法使用[闭合与定义](#cutadd-definition)、[群规律](#cutgroup-laws)、[加法逆元](#cutgroup-inverses)、[序平移](#cutgroup-translation)、[差与有理差相容](#cutgroup-negation-subtraction)。对象与次序使用[分割四条件](#cut-definition)、[包含全序与有理嵌入](#cut-order-embedding)、[非空有上界族的上确界](#cut-supremum)。函数使用[函数定义](#fun-definition)、[逐点相等](#fc-equality)、[复合](#fc-composition)、[恒等函数](#fc-identity)、[单射](#bij-injective)、[满射](#bij-surjective)与[双侧逆](#inv-two-sided)。[有理解集](#lin-solutions)和[同域等价](#lin-equivalence)只提供表述方法；下面重新在实数候选域内定义解集并证明结论。有理算例使用[有理除法](#rdiv-division)，并集算例使用[有理中点](#qgap-density-archimedean)。

**对象与记号。** $A,B,C,D,E,F,X$ 表示分割，$r,s,q,x$ 等小写字母表示有理数，族用 $\mathcal F$ 表示。沿用 $\oplus,\otimes,N$ 和 $A\ominus B=A\oplus N(B)$。零与一为 $0_{\mathbb R}=i(0)$、$1_{\mathbb R}=i(1)$；次序 $\le_{\mathbb R}$ 仍是分割间的包含。非零子集与已构造的逆元函数是

$$
\mathbb R^\times=\{A\in\mathbb R:A\ne0_{\mathbb R}\},\qquad
\operatorname{Inv}:\mathbb R^\times\to\mathbb R^\times.
$$

对每个非零 $A$，已经证明

$$
A\otimes\operatorname{Inv}(A)
=1_{\mathbb R}
=\operatorname{Inv}(A)\otimes A.
$$

$\operatorname{Inv}(A)$ 与 $A$ 同号；$\operatorname{Inv}(0_{\mathbb R})$ 没有定义。

### 1. 除法只接受非零的第二输入 {#cutdiv-definition}

**命题 DQ1。** 定义分割除法函数

$$
\oslash:\mathbb R\times\mathbb R^\times\to\mathbb R,
\qquad A\oslash B=A\otimes\operatorname{Inv}(B).
$$

给定定义域中的一对 $(A,B)$，非零 $B$ 有唯一的逆元，该逆元属于 $\mathbb R$；全乘法对 $A$ 与它有唯一的分割输出。因此这确实给出上述域与目标之间的函数。分子 $A$ 可以为零，分母 $B$ 必须非零。

对任意 $A\in\mathbb R$、$B\ne0_{\mathbb R}$，有两种乘回规律：

$$
(A\oslash B)\otimes B=A,
\qquad (A\otimes B)\oslash B=A.
$$

直接展开定义，逐项使用乘法结合、逆元及单位，得到

$$
\begin{aligned}
(A\oslash B)\otimes B
&=(A\otimes\operatorname{Inv}(B))\otimes B\\
&=A\otimes(\operatorname{Inv}(B)\otimes B)\\
&=A\otimes1_{\mathbb R}=A,
\end{aligned}
$$

以及

$$
\begin{aligned}
(A\otimes B)\oslash B
&=(A\otimes B)\otimes\operatorname{Inv}(B)\\
&=A\otimes(B\otimes\operatorname{Inv}(B))\\
&=A\otimes1_{\mathbb R}=A.
\end{aligned}
$$

两处除法的第二输入都是原来的非零 $B$，没有要求 $A$ 或 $A\otimes B$ 非零。又因 $\operatorname{Inv}(1_{\mathbb R})=1_{\mathbb R}$，

$$
A\oslash1_{\mathbb R}=A\otimes1_{\mathbb R}=A,
\qquad
0_{\mathbb R}\oslash B
=0_{\mathbb R}\otimes\operatorname{Inv}(B)=0_{\mathbb R}.
$$

**有理嵌入相容。** 设 $r,s\in\mathbb Q$，且 $s\ne0$。嵌入的单射性保证 $i(s)\ne i(0)$，所以左侧商合法。逆元相容与乘法相容给

$$
\begin{aligned}
i(r)\oslash i(s)
&=i(r)\otimes\operatorname{Inv}(i(s))\\
&=i(r)\otimes i(1/s)\\
&=i(r(1/s))=i(r/s).
\end{aligned}
$$

这里 $1/s$、$r/s$ 是先前已有的有理数运算；左侧 $\oslash$ 才是新定义的分割运算。$r=0$ 允许，$s=0$ 不允许。特别地，$0_{\mathbb R}\oslash0_{\mathbb R}$ 没有定义；一个乘法方程具有许多解，并不能替它指定唯一商值。

### 2. 在实数候选域中求解方程 {#cutdiv-equations}

**命题 DQ2。** 固定 $C,D\in\mathbb R$。本节的候选范围是 $\mathbb R$，两边是函数 $X\mapsto C\otimes X$ 与常值函数 $X\mapsto D$，均从 $\mathbb R$ 到 $\mathbb R$。定义解集

$$
\mathcal S(C,D)=\{X\in\mathbb R:C\otimes X=D\}.
$$

这是在新候选域内按条件形成的子集。旧有理方程的结论不能直接替代以下实数运算证明。

**非零系数。** 若 $C\ne0_{\mathbb R}$，令

$$
X_0=\operatorname{Inv}(C)\otimes D=D\oslash C.
$$

末项等号使用全乘法交换律。这个分割确实满足方程，因为

$$
C\otimes X_0
=C\otimes(\operatorname{Inv}(C)\otimes D)
=(C\otimes\operatorname{Inv}(C))\otimes D
=1_{\mathbb R}\otimes D=D.
$$

这给出存在性。反过来，若候选 $X$ 满足 $C\otimes X=D$，则

$$
\begin{aligned}
X
&=1_{\mathbb R}\otimes X\\
&=(\operatorname{Inv}(C)\otimes C)\otimes X\\
&=\operatorname{Inv}(C)\otimes(C\otimes X)\\
&=\operatorname{Inv}(C)\otimes D=X_0.
\end{aligned}
$$

【依据：单位、已经构造出的逆元、全结合律、所给方程。】这给出必要性，也给出唯一性。因此 $\mathcal S(C,D)=\{D\oslash C\}$。

**零系数。** 若 $C=0_{\mathbb R}$，每个候选都给 $C\otimes X=0_{\mathbb R}$。当 $D=0_{\mathbb R}$ 时，每个分割都是解，所以解集是 $\mathbb R$；它至少包含互异的 $0_{\mathbb R}$ 与 $1_{\mathbb R}$，不是唯一解。当 $D\ne0_{\mathbb R}$ 时，没有候选满足方程，解集是 $\varnothing$。这两个分支都不引入除零。

**固定非零因子的乘法函数现在是双射。** 对 $C\ne0_{\mathbb R}$，设

$$
M_C:\mathbb R\to\mathbb R,\qquad M_C(X)=C\otimes X.
$$

此前用 $M_C(X)=X\otimes C$ 写同一函数；交换律使两种写法逐点相同。因为 $\operatorname{Inv}(C)\in\mathbb R^\times$，函数 $M_{\operatorname{Inv}(C)}:\mathbb R\to\mathbb R$ 也合法。对每个 $X\in\mathbb R$，

$$
\begin{aligned}
M_{\operatorname{Inv}(C)}(M_C(X))
&=\operatorname{Inv}(C)\otimes(C\otimes X)\\
&=(\operatorname{Inv}(C)\otimes C)\otimes X=X,\\
M_C(M_{\operatorname{Inv}(C)}(X))
&=C\otimes(\operatorname{Inv}(C)\otimes X)\\
&=(C\otimes\operatorname{Inv}(C))\otimes X=X.
\end{aligned}
$$

两个复合的域与目标都为 $\mathbb R$，所以分别等于 $\operatorname{id}_{\mathbb R}$。双侧逆定理给 $M_C$ 为双射，且它的逆函数是 $M_{\operatorname{Inv}(C)}$。此前的消去只保证单射；现在对每个目标 $D$ 真正给出了原输入 $D\oslash C$，所以满射也有了存在见证。分割 $\operatorname{Inv}(C)$ 是一个乘法逆元，函数 $M_{\operatorname{Inv}(C)}$ 是一个逆函数，二者类型不同。

**一次仿射方程。** 对任意 $C,E,F\in\mathbb R$，仍以 $\mathbb R$ 为候选范围，考虑

$$
(C\otimes X)\oplus E=F.
$$

左侧由乘法与加法给 $\mathbb R\to\mathbb R$ 函数，右侧是同域常值函数。若上式成立，两边同加 $N(E)$，加法结合、逆元与单位给

$$
C\otimes X=F\oplus N(E)=F\ominus E.
$$

反过来，若 $C\otimes X=F\ominus E$，则

$$
(C\otimes X)\oplus E
=(F\oplus N(E))\oplus E
=F\oplus(N(E)\oplus E)=F.
$$

因此移项是同一候选域内的双向等价。还要注意

$$
F\ominus E=0_{\mathbb R}\quad\Longleftrightarrow\quad F=E.
$$

右向只须在 $F\oplus N(E)=0_{\mathbb R}$ 两边同加 $E$；左向由加法逆元成立。应用刚刚证明的乘法方程分类，得到完整解集

$$
\{X\in\mathbb R:(C\otimes X)\oplus E=F\}
=
\begin{cases}
\{(F\ominus E)\oslash C\},& C\ne0_{\mathbb R},\\
\mathbb R,& C=0_{\mathbb R},\ E=F,\\
\varnothing,& C=0_{\mathbb R},\ E\ne F.
\end{cases}
$$

**例。** 求解

$$
(i(-2)\otimes X)\oplus i(1/3)=i(5/6).
$$

系数 $i(-2)$ 非零。由差的有理相容，$i(5/6)\ominus i(1/3)=i(1/2)$；由DQ1，唯一候选为

$$
X=i(1/2)\oslash i(-2)=i(-1/4).
$$

代回原式，乘法与加法的有理相容给

$$
(i(-2)\otimes i(-1/4))\oplus i(1/3)
=i(1/2)\oplus i(1/3)=i(5/6).
$$

代回确认存在性，前面的必要性证明保证没有别的实数候选。

### 3. 固定正负除数的双向比较 {#cutdiv-order}

**命题 DQ3。** 固定 $C\ne0_{\mathbb R}$，$A,B$ 为任意分割。若 $C>_{\mathbb R}0_{\mathbb R}$，IR3先给 $\operatorname{Inv}(C)>_{\mathbb R}0_{\mathbb R}$。把它作为SR3中的共同正因子，得到

$$
\begin{aligned}
A\le_{\mathbb R}B
&\Longleftrightarrow
A\otimes\operatorname{Inv}(C)\le_{\mathbb R}B\otimes\operatorname{Inv}(C)\\
&\Longleftrightarrow A\oslash C\le_{\mathbb R}B\oslash C,\\
A<_{\mathbb R}B
&\Longleftrightarrow
A\otimes\operatorname{Inv}(C)<_{\mathbb R}B\otimes\operatorname{Inv}(C)\\
&\Longleftrightarrow A\oslash C<_{\mathbb R}B\oslash C.
\end{aligned}
$$

若 $C<_{\mathbb R}0_{\mathbb R}$，IR3给 $\operatorname{Inv}(C)<_{\mathbb R}0_{\mathbb R}$。使用SR3的共同负因子版本，得到

$$
\begin{aligned}
A\le_{\mathbb R}B
&\Longleftrightarrow
B\otimes\operatorname{Inv}(C)\le_{\mathbb R}A\otimes\operatorname{Inv}(C)\\
&\Longleftrightarrow B\oslash C\le_{\mathbb R}A\oslash C,\\
A<_{\mathbb R}B
&\Longleftrightarrow
B\otimes\operatorname{Inv}(C)<_{\mathbb R}A\otimes\operatorname{Inv}(C)\\
&\Longleftrightarrow B\oslash C<_{\mathbb R}A\oslash C.
\end{aligned}
$$

这些都是双向等价，既能从原比较推出商的比较，也能从商的比较返回原比较；分子不必为正。若 $C=0_{\mathbb R}$，相关商没有定义，不能把乘零后相等的规律移用到除零。若仅分子为零而分母非零，则商确实为零。

**正倒数反序。** 设 $A,B>_{\mathbb R}0_{\mathbb R}$。两个逆元都正，因而

$$
T=\operatorname{Inv}(A)\otimes\operatorname{Inv}(B)>_{\mathbb R}0_{\mathbb R}.
$$

结合律与逆元式给

$$
\begin{aligned}
A\otimes T
&=A\otimes(\operatorname{Inv}(A)\otimes\operatorname{Inv}(B))\\
&=(A\otimes\operatorname{Inv}(A))\otimes\operatorname{Inv}(B)\\
&=\operatorname{Inv}(B),\\
B\otimes T
&=B\otimes(\operatorname{Inv}(B)\otimes\operatorname{Inv}(A))\\
&=(B\otimes\operatorname{Inv}(B))\otimes\operatorname{Inv}(A)\\
&=\operatorname{Inv}(A).
\end{aligned}
$$

第二段第一步还使用了内部两个逆元的交换。对共同正因子 $T$ 用SR3，得

$$
\begin{aligned}
A\le_{\mathbb R}B
&\Longleftrightarrow A\otimes T\le_{\mathbb R}B\otimes T
\Longleftrightarrow \operatorname{Inv}(B)\le_{\mathbb R}\operatorname{Inv}(A),\\
A<_{\mathbb R}B
&\Longleftrightarrow A\otimes T<_{\mathbb R}B\otimes T
\Longleftrightarrow \operatorname{Inv}(B)<_{\mathbb R}\operatorname{Inv}(A).
\end{aligned}
$$

两个输入为正的条件不可直接删去。例如 $i(-1)<_{\mathbb R}i(1)$，但有理逆相容给它们的逆元仍分别为 $i(-1)$、$i(1)$，因此不存在所有非零输入上的统一反序结论。本证明没有使用一般分式通分或逆乘积公式。

### 4. 有序域名称与上确界性质 {#cutdiv-complete-field}

**命题 DQ4。** 本书称一个具有不同的零和一的交换环为**域**，如果其中每个非零元素都有乘法逆元。若这个域还带有全序，加法保持次序，且两个正元素的积为正，就称为**有序域**。这里的加法保序指共同平移保持不严格次序；严格版本与反射在本构造中也已经证明。

已经构造的分割系统逐项满足这些要求：

| 需要的性质 | 本书已完成的依据 |
| --- | --- |
| 加法闭合、交换、结合、零与每个元素的相反数 | DA2的闭合及DG1、DG2的加法群证明 |
| 全乘法闭合、交换、结合、单位 | SP1—SP3的符号定义及证明 |
| 乘法对两侧加法分配 | SR1、SR2的全部符号证明 |
| $0_{\mathbb R}\ne1_{\mathbb R}$ | 有理嵌入保持并反射次序，且 $0<1$ |
| 每个非零元素具有乘法逆元 | IR1—IR3的正候选构造与符号扩展 |
| 次序为全序且加法保序 | DC2与DG3 |
| 两个正元素的积为正 | 非负乘积正性及全乘法的一致性 |

因此，带有 $\oplus,\otimes$ 和包含序的 $\mathbb R$ 是一个具体有序域。域这一名称汇总已经证明的规律；它没有替代逆元构造，也没有给 $\operatorname{Inv}(0_{\mathbb R})$ 或零分母商添加定义。

**这里的“完备”指什么。** 本书在本处称有序域**完备**，是指它具有以下 Dedekind 上确界性质：每个非空且有上界的子集都有最小上界。具体说，设

$$
\varnothing\ne\mathcal F\subseteq\mathbb R,
\qquad
\text{存在 }U\in\mathbb R\text{ 使每个 }A\in\mathcal F\text{ 都满足 }A\le_{\mathbb R}U.
$$

形成有理数条件子集

$$
V=\{q\in\mathbb Q:\text{存在 }A\in\mathcal F\text{ 使 }q\in A\}
=\bigcup\mathcal F.
$$

[DC4](#cut-supremum)已经证明，$V$ 是分割且是 $\mathcal F$ 的最小上界。为看清每个条件的作用，可把证明核对如下：非空族中取一个 $A_0$，其内点属于 $V$，所以 $V$ 非空；由 $V\subseteq U$，$U$ 的外点也在 $V$ 外，所以 $V\ne\mathbb Q$。若 $q\in V$，选择一个见证 $A\in\mathcal F$ 且 $q\in A$；比 $q$ 小的有理数仍属于这个 $A$，故属于 $V$，并且这个 $A$ 内存在大于 $q$ 的成员，它也属于 $V$。这样下闭与无最大元也成立。

每个 $A\in\mathcal F$ 都包含于 $V$，所以 $V$ 是上界。若 $W\in\mathbb R$ 是另一个上界，任意 $q\in V$ 都有某个 $A\in\mathcal F$ 见证，而 $A\subseteq W$，于是 $q\in W$。故 $V\subseteq W$，即 $V\le_{\mathbb R}W$，它是最小上界。因此

$$
\sup_{\mathbb R}\mathcal F=\bigcup\mathcal F.
$$

从建立DC4到现在，底层集合一直是这些分割，次序一直是包含；新增运算没有改变二者。因此原来已经证明的上确界性质适用于现在这个有序域，而不是另行假定的一条实数公理。

**一个并集的具体核对。** 令

$$
\mathcal F=\{A\in\mathbb R:\text{存在 }r\in\mathbb Q, r<1\text{ 且 }A=i(r)\}.
$$

这正是通常简写的 $\{i(r):r\in\mathbb Q,r<1\}$。因为 $0<1$，$i(0)\in\mathcal F$，所以非空。每个 $r<1$ 都给 $i(r)\le_{\mathbb R}i(1)$，所以 $i(1)$ 是分割上界。

若有理数 $x\in\bigcup\mathcal F$，存在 $r<1$ 使 $x\in i(r)$，于是 $x<r<1$，所以 $x\in i(1)$。反过来，若 $x\in i(1)$，则 $x<1$。取有理中点

$$
r=\frac{x+1}{2},\qquad x<r<1.
$$

此时 $i(r)\in\mathcal F$ 且 $x\in i(r)$，所以 $x\in\bigcup\mathcal F$。两包含给 $\bigcup\mathcal F=i(1)$，DC4遂给 $\sup_{\mathbb R}\mathcal F=i(1)$。族的成员是分割 $i(r)$，并集的成员才是有理数 $x$；这一次具体核对不取代对任意合条件族的DC4证明。

空族和无上界族不满足上述假设，本构造没有加入无穷大分割。现在可以说：已经构造了一个具有上确界性质的完备有序域。本单元尚未证明柯西完备与该性质的等价、完备有序域的唯一同构、正元素的平方根存在，也未建立实数的阿基米德性、稠密性或一般极限理论；这些需要后续各自的定义与证明。

### 5. 课后题 {#cutdiv-exercises}

#### 题1：商的域与两种乘回 {#cutdiv-q01}

写出 $\oslash$ 的定义域、目标与规则，证明每对合法输入有唯一分割输出。对 $B\ne0_{\mathbb R}$ 逐式证明 $(A\oslash B)\otimes B=A$、$(A\otimes B)\oslash B=A$、$A\oslash1_{\mathbb R}=A$ 与 $0_{\mathbb R}\oslash B=0_{\mathbb R}$。解释分子为零与分母为零的区别。[完整解答](#cutdiv-a01)

#### 题2：有理商与分割商相容 {#cutdiv-q02}

对 $r,s\in\mathbb Q$、$s\ne0$，核分母合法并证明 $i(r)\oslash i(s)=i(r/s)$。计算 $i(-3/4)\oslash i(2/5)$ 与 $i(3/4)\oslash i(-2/5)$。说明 $r=0$ 和 $s=0$ 分别能否代入。[完整解答](#cutdiv-a02)

#### 题3：乘法方程的全部参数分支 {#cutdiv-q03}

在候选范围 $\mathbb R$ 内，定义 $C\otimes X=D$ 的解集。对 $C\ne0_{\mathbb R}$ 分别证明解的存在性与必要性，得唯一解；再完整处理 $C=0_{\mathbb R}$ 下的两种目标。说明为何不能直接引用旧有理候选域的方程结论。[完整解答](#cutdiv-a03)

#### 题4：乘法函数的两次往返 {#cutdiv-q04}

固定 $C\ne0_{\mathbb R}$，给出 $M_C$ 与 $M_{\operatorname{Inv}(C)}$ 的定义域、目标与规则，逐式证明两个复合均为恒等函数。由此证明双射，并为任意目标 $D$ 写出原输入。区分逆元和逆函数，说明新构造为何补上了此前满射的缺口。[完整解答](#cutdiv-a04)

#### 题5：一次仿射方程与负系数 {#cutdiv-q05}

在 $\mathbb R$ 中证明 $(C\otimes X)\oplus E=F$ 与 $C\otimes X=F\ominus E$ 双向等价，给出全部三种参数分支的解集。解方程 $(i(-2)\otimes X)\oplus i(1/3)=i(5/6)$，代回并说明唯一性。[完整解答](#cutdiv-a05)

#### 题6：固定除数的弱比较与严格比较 {#cutdiv-q06}

分别对 $C>_{\mathbb R}0_{\mathbb R}$ 与 $C<_{\mathbb R}0_{\mathbb R}$，先核逆元符号，再写出商的弱、严格比较的完整双向链。说明分子允许零，且 $C=0_{\mathbb R}$ 时为什么不能写“两个商都为零”。[完整解答](#cutdiv-a06)

#### 题7：正倒数反序的共同因子证明 {#cutdiv-q07}

对 $A,B>_{\mathbb R}0_{\mathbb R}$，取 $T=\operatorname{Inv}(A)\otimes\operatorname{Inv}(B)$，证明 $T$ 正并完整化简 $A\otimes T$、$B\otimes T$。推出弱、严格倒数反序的双向等价，再用 $i(-1)$ 与 $i(1)$ 检查跨零时不能统一反序。[完整解答](#cutdiv-a07)

#### 题8：逐项核对有序域与完备性的含义 {#cutdiv-q08}

列出分割系统满足域、有序域和本处完备性定义的依据。对族 $\mathcal F=\{i(r):r\in\mathbb Q,r<1\}$，核非空和有上界，逐成员证明 $\bigcup\mathcal F=i(1)$，据DC4确定上确界。区分分割成员与有理成员，说明空族和无上界族不在假设内，并举出至少四项本单元尚未证明的后续结论。[完整解答](#cutdiv-a08)

**来源与范围说明。** 结构定义、外部倒数定理的非零条件及完备性用语的对照见[倒数与除法来源审计](#dedekind-inverse-sources)。本单元只在非零分母域定义商；实数方程、次序比较及结构命名均建立在已构造的分割运算上。有理实例不承担一般分割证明，也没有给出任意分割的成员判定算法。
