## 基础单元 B2.27 全部分割的乘法、符号与结合 {#cutsigned-unit}

**学习目标与位置。** 非负分割的乘法已经成立。现在按输入的符号，把它扩展为全部分割上的二元运算；随后从定义证明交换、乘零、乘一、取反乘积和结合律，最后核对全部有理数的乘法相容及零乘积判据。主归属第526章97F50的实数基础教学部分；06A05交叉。本单元不预用任意符号下的分配律，也不定义分割倒数。

**精确先修。** 使用[包含全序与有理嵌入](#cut-order-embedding)、[负分割定义及闭合](#cutadd-negation)、[有理加法与相反数相容](#cutadd-rational)、[双重取反与零的相反数](#cutgroup-inverses)、[取反的双向反序](#cutgroup-negation-subtraction)。非负乘法使用[正分割见证NP1](#cutprod-positive-witnesses)、[闭合、零及正积NP2](#cutprod-definition)、[交换与单位NP3](#cutprod-basic-laws)、[非负有理相容NP4](#cutprod-rational)、[非负结合律NL2](#cutprod-associative)。有理成员计算使用[有理乘法规律](#rmul-laws)及[有理乘法符号律](#rmul-signs)。函数记号沿用[函数定义](#fun-definition)。

**对象与记号。** $A,B,C$ 等表示分割；小写 $r,s,q$ 等表示有理数。沿用
$$
0_{\mathbb R}=i(0),\qquad 1_{\mathbb R}=i(1),\qquad
\mathbb R_+=\{A\in\mathbb R:0_{\mathbb R}\le_{\mathbb R}A\}.
$$
非负乘积 $P$ 的定义域仍是 $\mathbb R_+\times\mathbb R_+$。对任意分割的乘法另用 $A\otimes B$，从而能检查每次 $P$ 调用是否真正处于非负域。负分割 $N(A)$ 已是加法相反数，且
$$
N(N(A))=A,\qquad N(0_{\mathbb R})=0_{\mathbb R}.
$$
以下 $A<_{\mathbb R}0_{\mathbb R}$ 称为负分割；取反反序说明负分割的相反数为正，正分割的相反数为负。

### 1. 四个互斥的符号区域 {#cutsigned-definition}

全序使每个分割恰好属于“非负”或“负”中的一类。两个输入因此有四个互不重叠且穷尽全部输入的符号区域。

**定义与命题 SP1。** 对任意 $A,B\in\mathbb R$，定义
$$
A\otimes B=
\begin{cases}
P(A,B),&A\ge_{\mathbb R}0_{\mathbb R},\ B\ge_{\mathbb R}0_{\mathbb R},\\
N(P(N(A),B)),&A<_{\mathbb R}0_{\mathbb R},\ B\ge_{\mathbb R}0_{\mathbb R},\\
N(P(A,N(B))),&A\ge_{\mathbb R}0_{\mathbb R},\ B<_{\mathbb R}0_{\mathbb R},\\
P(N(A),N(B)),&A<_{\mathbb R}0_{\mathbb R},\ B<_{\mathbb R}0_{\mathbb R}.
\end{cases}
$$
每个输出都是分割，因此这个规则定义函数
$$
\otimes:\mathbb R\times\mathbb R\longrightarrow\mathbb R.
$$

这先是一个具体规则。“两个负号相乘应当怎样”不是用来证明它的先修；我们还要证明该规则与已经建立的运算规律相容。

**逐支检查定义域与输出。**

第一支的 $A,B$ 本来非负，所以 $P(A,B)$ 已有定义，且输出非负分割。

第二支中 $A<_{\mathbb R}0_{\mathbb R}$。由取反反序，
$$
0_{\mathbb R}=N(0_{\mathbb R})<_{\mathbb R}N(A).
$$
因此 $N(A)$ 为正，而 $B$ 非负；$P(N(A),B)$ 是合法的非负乘积。再对它应用已定义于全部 $\mathbb R$ 的 $N$，仍得分割。

第三支中 $B<_{\mathbb R}0_{\mathbb R}$ 同样给 $N(B)>_{\mathbb R}0_{\mathbb R}$；$A$ 非负，故 $P(A,N(B))$ 合法，再取 $N$ 仍为分割。

第四支的两个负输入取反后都正，所以 $P(N(A),N(B))$ 也合法，且输出为非负分割。

每个输入恰落在一支中，各支内部函数输出唯一。因此全域上存在且唯一的输出得到证明，SP1成立。零输入只进入“非负”条件，不同时进入“负”条件。

**输出仍是实际有理子集。** 例如第二支令
$$
U=N(A),\qquad V=B,
$$
两者均非负。其输出按已有负分割定义，实际是
$$
N(P(U,V))
=\{q\in\mathbb Q:\exists t\in\mathbb Q,\ t\notin P(U,V)\text{ 且 }q<-t\}.
$$
其中 $P(U,V)$ 又是上一单元已构造的有理子集：
$$
P(U,V)=\{x\in\mathbb Q:x<0\text{，或存在正 }u\in U,v\in V
\text{ 使 }x<uv\}.
$$
若需要展开 $U=N(A)$，其成员也按已证的严格外点定义判断。这里每一层都有确定集合，既没有把“负的乘积”当作未定义对象，也没有选择一个分割的有理代表。一般分割本来就未必有这种代表。

### 2. 先从定义证明符号规则 {#cutsigned-signs}

**命题 SP2。** 对任意 $A,B\in\mathbb R$，
$$
A\otimes B=B\otimes A,\qquad
A\otimes0_{\mathbb R}=0_{\mathbb R}=0_{\mathbb R}\otimes A,
$$
$$
A\otimes1_{\mathbb R}=A=1_{\mathbb R}\otimes A,
$$
$$
N(A)\otimes B=N(A\otimes B)=A\otimes N(B),
\qquad
N(A)\otimes N(B)=A\otimes B.
$$
非零输入的乘积符号由两个输入的符号唯一决定：同号为正，异号为负。下面的证明同时解释这句话的全部条件。

**先独立处理零因子。** 若 $B\ge_{\mathbb R}0_{\mathbb R}$，第一支及NP2给
$$
0_{\mathbb R}\otimes B=P(0_{\mathbb R},B)=0_{\mathbb R}.
$$
若 $B<_{\mathbb R}0_{\mathbb R}$，第三支给
$$
0_{\mathbb R}\otimes B
=N(P(0_{\mathbb R},N(B)))=N(0_{\mathbb R})=0_{\mathbb R}.
$$
若 $A\ge_{\mathbb R}0_{\mathbb R}$，第一支给 $A\otimes0_{\mathbb R}=P(A,0_{\mathbb R})=0_{\mathbb R}$；若 $A<_{\mathbb R}0_{\mathbb R}$，第二支给
$$
A\otimes0_{\mathbb R}
=N(P(N(A),0_{\mathbb R}))=0_{\mathbb R}.
$$
所以两个位置的零因子公式已从定义分别证明，不靠交换律倒推。

**非零分割的唯一正幅度与符号。** 定义两个已有函数的简记
$$
E_0:\mathbb R\to\mathbb R,\quad E_0(X)=X,\qquad
E_1:\mathbb R\to\mathbb R,\quad E_1(X)=N(X).
$$
下标 $0,1$ 是区分这两个函数的两个自然数标签，不是分割乘法的指数。因 $N$ 已定义于全部分割，这两函数都有意义。

每个 $A\ne0_{\mathbb R}$ 都可唯一写成
$$
A=E_e(U),\qquad e\in\{0,1\},\qquad U>_{\mathbb R}0_{\mathbb R}.
$$
这里把 $U$ 称为该表示的**正幅度**，把 $e$ 称为符号标签；此处只是定义一种表示，不预先调用实数绝对值。

如果 $A>_{\mathbb R}0_{\mathbb R}$，取 $e=0,U=A$。如果 $A<_{\mathbb R}0_{\mathbb R}$，取 $e=1,U=N(A)$；反序给 $U>_{\mathbb R}0_{\mathbb R}$，双重取反给 $E_1(U)=A$，证明存在。

唯一性也要分清。对正的 $U$，$E_0(U)=U$ 为正，$E_1(U)=N(U)$ 为负。所以正的 $A$ 只能用 $e=0$，随后必有 $U=A$；负的 $A$ 只能用 $e=1$，从 $A=N(U)$ 两边取 $N$ 得 $U=N(A)$。全序排除了其它标签及幅度。零分割没有这种正幅度表示，因为两个 $E_e(U)$ 都非零。

**有限符号表。** 对标签 $e,f\in\{0,1\}$，按四个输入定义标签函数 $e\diamond f$，如下表第三列。这是一个有限规则，不假定已经建立模运算或新的代数结构。

| $e$ | $f$ | $e\diamond f$ |
| --- | --- | --- |
| $0$ | $0$ | $0$ |
| $0$ | $1$ | $1$ |
| $1$ | $0$ | $1$ |
| $1$ | $1$ | $0$ |

对任意正分割 $U,V$，四支定义直接给
$$
E_e(U)\otimes E_f(V)=E_{e\diamond f}(P(U,V)).
$$
逐项说明如下：两个标签为零时是 $P(U,V)$；标签为 $0,1$ 时，$N(V)$ 为负，第三支给 $N(P(U,N(N(V))))=N(P(U,V))$；标签为 $1,0$ 时，第二支及 $N(N(U))=U$ 给同样形式；标签为 $1,1$ 时，第四支与两次双重取反给 $P(U,V)$。所以四行等式都有实际定义依据。

NP2给 $P(U,V)>_{\mathbb R}0_{\mathbb R}$；取反反序使 $N(P(U,V))<_{\mathbb R}0_{\mathbb R}$。因此第三列为零恰对应正积，为一恰对应负积。这证明非零输入的同号、异号规律，没有调用分配律。

**交换。** 零因子情形已由两个位置的零公式保证交换。若两输入非零，写成 $A=E_e(U)$、$B=E_f(V)$。上表逐行给 $e\diamond f=f\diamond e$，NP3给 $P(U,V)=P(V,U)$。因此
$$
\begin{aligned}
A\otimes B
&=E_{e\diamond f}(P(U,V))\\
&=E_{f\diamond e}(P(V,U))
=B\otimes A.
\end{aligned}
$$
其中第二步只是同一个已定义函数在相等输入上的输出相等。

**一个因子取反。** 对标签定义翻转 $\bar0=1,\bar1=0$。对任意分割 $X$，
$$
N(E_e(X))=E_{\bar e}(X).
$$
当 $e=0$，两边都是 $N(X)$；当 $e=1$，左边是 $N(N(X))=X$，右边也是 $X$。

再按四行直接核对：

| $e$ | $f$ | $\bar e\diamond f$ | $\overline{e\diamond f}$ |
| --- | --- | --- | --- |
| $0$ | $0$ | $1$ | $1$ |
| $0$ | $1$ | $0$ | $0$ |
| $1$ | $0$ | $0$ | $0$ |
| $1$ | $1$ | $1$ | $1$ |

若 $A,B$ 都非零，把它们写成上述唯一表示，得到
$$
\begin{aligned}
N(A)\otimes B
&=E_{\bar e}(U)\otimes E_f(V)\\
&=E_{\bar e\diamond f}(P(U,V))\\
&=E_{\overline{e\diamond f}}(P(U,V))\\
&=N(E_{e\diamond f}(P(U,V)))\\
&=N(A\otimes B).
\end{aligned}
$$
若某个输入为零，$N(0_{\mathbb R})=0_{\mathbb R}$ 与两位置零律使等式两边也都为零。这里 $N(A)=0_{\mathbb R}$ 当且仅当 $A=0_{\mathbb R}$：反向已知，正向对等式取 $N$ 并用双重取反即可。因此上述非零分支确实也可用于取反后的输入。

使用刚证的交换律和第一因子取反式，
$$
A\otimes N(B)=N(B)\otimes A
=N(B\otimes A)=N(A\otimes B).
$$
再对两个因子都取反，
$$
\begin{aligned}
N(A)\otimes N(B)
&=N(A\otimes N(B))\\
&=N(N(A\otimes B))=A\otimes B.
\end{aligned}
$$
全部取反规律只由符号定义、有限表与加法双重取反建立。

**单位。** 一分割严格为正，所以 $1_{\mathbb R}=E_0(1_{\mathbb R})$。对非零 $A=E_e(U)$，标签表给 $e\diamond0=e$，非负单位律给
$$
A\otimes1_{\mathbb R}
=E_{e\diamond0}(P(U,1_{\mathbb R}))
=E_e(U)=A.
$$
如果 $A=0_{\mathbb R}$，零乘公式也给该等式。交换律再给左单位。SP2全部结论得证。

到这里，符号规律可以使用，但任意符号下的分配律仍未证明。本单元特意从定义建立取反乘积；不能反过来先用待证的分配律证明这些符号式。

### 3. 用八行检查把结合律扩到所有符号 {#cutsigned-associative}

**命题 SP3。** 对任意分割 $A,B,C$，
$$
(A\otimes B)\otimes C=A\otimes(B\otimes C).
$$

**先核零输入。** 如果 $A=0_{\mathbb R}$，左边先算 $0_{\mathbb R}\otimes B=0_{\mathbb R}$，再乘 $C$ 为零；右边因第一因子为零也为零。如果 $B=0_{\mathbb R}$，左边内部乘积和右边内部乘积都为零，外层两边也为零。如果 $C=0_{\mathbb R}$，左边直接乘零；右边内部 $B\otimes0_{\mathbb R}=0_{\mathbb R}$，外层也乘零。三种位置及多项为零均覆盖。

**非零输入时还要检查中间乘积。** 写出唯一表示
$$
A=E_e(U),\qquad B=E_f(V),\qquad C=E_g(W),
$$
其中 $U,V,W$ 正，标签 $e,f,g$ 均在 $\{0,1\}$ 中。NP2保证 $P(U,V)$ 与 $P(V,W)$ 都正。所以SP2给出的中间乘积
$$
A\otimes B=E_{e\diamond f}(P(U,V)),\qquad
B\otimes C=E_{f\diamond g}(P(V,W))
$$
也都非零，并且右侧幅度仍为正，可以继续使用SP2公式。于是
$$
(A\otimes B)\otimes C
=E_{(e\diamond f)\diamond g}(P(P(U,V),W)),
$$
$$
A\otimes(B\otimes C)
=E_{e\diamond(f\diamond g)}(P(U,P(V,W))).
$$

有两件事分别需要核对。幅度的相等由已证非负结合律NL2给出：
$$
P(P(U,V),W)=P(U,P(V,W)).
$$
标签是否相同则由有限表检查，不能预用尚未证明的 $\diamond$ 结合律。

| $e$ | $f$ | $g$ | $e\diamond f$ | $f\diamond g$ | $(e\diamond f)\diamond g$ | $e\diamond(f\diamond g)$ |
| --- | --- | --- | --- | --- | --- | --- |
| $0$ | $0$ | $0$ | $0$ | $0$ | $0$ | $0$ |
| $0$ | $0$ | $1$ | $0$ | $1$ | $1$ | $1$ |
| $0$ | $1$ | $0$ | $1$ | $1$ | $1$ | $1$ |
| $0$ | $1$ | $1$ | $1$ | $0$ | $0$ | $0$ |
| $1$ | $0$ | $0$ | $1$ | $0$ | $1$ | $1$ |
| $1$ | $0$ | $1$ | $1$ | $1$ | $0$ | $0$ |
| $1$ | $1$ | $0$ | $0$ | $1$ | $0$ | $0$ |
| $1$ | $1$ | $1$ | $0$ | $0$ | $1$ | $1$ |

最后两列在全部八种输入上相等。它们穷尽三个二值标签的所有可能；这只是有限函数的全域检查，不是对无限分割作有限抽样。结合幅度相等，同一个 $E_0$ 或 $E_1$ 对相等输入给相等输出，所以两个括号结果相等。SP3得证。

### 4. 全部有理数的相容与零乘积 {#cutsigned-rational-zero}

**命题 SP4。** 对任意有理数 $r,s$，
$$
i(r)\otimes i(s)=i(rs).
$$
对任意分割 $A,B$，
$$
A\otimes B=0_{\mathbb R}
\quad\Longleftrightarrow\quad
A=0_{\mathbb R}\text{ 或 }B=0_{\mathbb R}.
$$

**先核有理零。** 如果 $r=0$，SP2给 $i(r)\otimes i(s)=0_{\mathbb R}$，有理零乘给 $i(rs)=i(0)=0_{\mathbb R}$。如果 $s=0$，第二位置零律给同样相等。以下 $r,s$ 均非零，分成四个符号区域。

若 $r>0,s>0$，嵌入保序使两个分割都正，定义第一支及NP4直接给
$$
i(r)\otimes i(s)=P(i(r),i(s))=i(rs).
$$

若 $r<0,s>0$，嵌入保序使第一输入负、第二输入正。有理相反数相容给 $N(i(r))=i(-r)$，其中 $-r>0$。于是
$$
\begin{aligned}
i(r)\otimes i(s)
&=N(P(N(i(r)),i(s)))\\
&=N(P(i(-r),i(s)))\\
&=N(i((-r)s))\\
&=i(-((-r)s))=i(rs).
\end{aligned}
$$
第三行只对正有理数 $-r,s$ 用NP4；第四行先用相反数相容，最后用已有有理符号律及双重取反。

若 $r>0,s<0$，同样逐行核第三支：
$$
\begin{aligned}
i(r)\otimes i(s)
&=N(P(i(r),N(i(s))))\\
&=N(P(i(r),i(-s)))\\
&=N(i(r(-s)))\\
&=i(-(r(-s)))=i(rs).
\end{aligned}
$$
这里NP4的两个有理输入是正的 $r,-s$，没有让它越域处理负数。

若 $r<0,s<0$，两个相反数都正，定义第四支给
$$
\begin{aligned}
i(r)\otimes i(s)
&=P(N(i(r)),N(i(s)))\\
&=P(i(-r),i(-s))\\
&=i((-r)(-s))=i(rs).
\end{aligned}
$$
最后一式是有理数的双取反乘积规律。零与四个非零符号区域共同覆盖全部有理输入，相容性得证。

例如，
$$
i(-2/3)\otimes i(3/5)=i(-2/5),\qquad
i(-2/3)\otimes i(-3/5)=i(2/5).
$$
这些算例使用刚证明的全有理相容，不能用两个算例反过来代替前面的全称证明。

**零乘积。** 若某个输入为零，SP2已经给零乘积。反过来，若两个输入均非零，用正幅度表示
$$
A=E_e(U),\qquad B=E_f(V),\qquad U,V>_{\mathbb R}0_{\mathbb R}.
$$
令 $T=P(U,V)$，NP2给 $T>_{\mathbb R}0_{\mathbb R}$。SP2使乘积为 $E_{e\diamond f}(T)$：标签为零时它是正的 $T$，标签为一时它是负的 $N(T)$。两种都非零。所以零乘积不能来自两个非零输入，反向成立，SP4证毕。

这个判据是排除某种零乘积的结论，尚未给定非零 $A$ 就构造满足 $A\otimes X=1_{\mathbb R}$ 的 $X$。非零倒数的存在不能从零乘积判据直接宣称。

### 5. 当前证明链的边界 {#cutsigned-boundaries}

运算现在定义于全部分割，交换、结合、零、单位、符号和有理乘法相容都已逐项证明。非零乘积也已排除为零。但要与已有加法组成环，还需要证明任意符号下的两侧分配律；尤其一个正输入与一个负输入相加时，和可能为正、零或负，不能只引用非负域的分配式。下一单元将按这些情形完成证明。

本单元没有创建一套新的商类：正幅度表示的唯一性只是从已证全序和取反得到的表示事实。也没有提供任意分割成员的算法，或把实数域、连续性、实数根式作为定义的依据。

### 6. 课后题 {#cutsigned-exercises}

#### 题1：四支是否穷尽，输出是否已有定义 {#cutsigned-q01}

写出全部分割乘法的四支定义。证明符号区域互斥并穷尽全部输入，逐支检查每次 $P$ 的输入非负、每次 $N$ 的输入已经是分割。说明零归入哪一侧，以及为什么定义确实给出函数 $\mathbb R\times\mathbb R\to\mathbb R$。[完整解答](#cutsigned-a01)

#### 题2：把含负输入的乘积展开成有理子集 {#cutsigned-q02}

设 $A<_{\mathbb R}0_{\mathbb R}$、$B\ge_{\mathbb R}0_{\mathbb R}$，令 $U=N(A),V=B$。把 $A\otimes B=N(P(U,V))$ 展开成有理成员条件，明确外部见证属于哪个补集及严格号的方向。再按另一输入的正负，分别证明两个位置的零因子公式，不使用交换律。[完整解答](#cutsigned-a02)

#### 题3：交换与单位从哪一支得到 {#cutsigned-q03}

对任意分割 $A,B$，按四个输入区域证明交换律，零输入也要覆盖。再按 $A$ 非负与负两类直接证明 $A\otimes1_{\mathbb R}=A$，明确 $1_{\mathbb R}$ 为正及负输入中双重取反的用途，最后推出左单位。[完整解答](#cutsigned-a03)

#### 题4：唯一正幅度与取反乘积 {#cutsigned-q04}

定义 $E_0,E_1$ 后，完整证明每个非零分割具有唯一表示 $E_e(U)$，其中 $e\in\{0,1\}$、$U>_{\mathbb R}0_{\mathbb R}$，而零没有此表示。由四支定义证明符号表公式，核标签翻转表，再证明一个及两个因子取反的全部公式，包括零边界。不得用尚未证明的全分配律。[完整解答](#cutsigned-a04)

#### 题5：零出现在三因子的哪个位置 {#cutsigned-q05}

分别令 $A$、$B$、$C$ 为零分割，逐项证明 $(A\otimes B)\otimes C$ 与 $A\otimes(B\otimes C)$ 都为零。给两个有理下段的具体例子，使零分别出现在中间与末尾；解释该证明是否已覆盖没有零输入的情况。[完整解答](#cutsigned-a05)

#### 题6：八行标签表与一般结合律 {#cutsigned-q06}

对三个非零输入写出正幅度表示，先证明两个中间乘积的幅度正，才能继续调用符号公式。列出全部八行，核 $(e\diamond f)\diamond g=e\diamond(f\diamond g)$，再结合NL2得到全结合律。说明有限表为何是标签全域检查，而非对任意分割作有限抽样。[完整解答](#cutsigned-a06)

#### 题7：全有理相容需要哪些符号区域 {#cutsigned-q07}

对全部有理数 $r,s$ 证明 $i(r)\otimes i(s)=i(rs)$。先处理零，再逐个非零符号区域核相反数相容、NP4正输入条件及有理符号律。计算 $i(-2/3)\otimes i(3/5)$ 和 $i(-2/3)\otimes i(-3/5)$，并说明这些算例与一般证明的关系。[完整解答](#cutsigned-a07)

#### 题8：零积判据没有构造倒数 {#cutsigned-q08}

证明对任意分割 $A,B$，乘积为零当且仅当至少一个输入为零。反向必须从正幅度及其乘积的严格符号排除两个非零输入。再解释：这个结论是否已经证明每个非零 $A$ 存在 $X$ 使 $A\otimes X=1_{\mathbb R}$，或者已经证明全符号分配律？分别指出还缺哪一种证明义务。[完整解答](#cutsigned-a08)

**来源与范围说明。** 定义、符号依赖及抽象结构义务的对照见[分割乘法来源核验](#dedekind-signed-sources)。本文从四支定义及已证加法相反数建立符号律，再用非负结合和完整标签表建立全结合。外部已假定环结构后从分配推符号的路线不作为此处先修；当前仍未声明有序域或非零倒数已经构造。
