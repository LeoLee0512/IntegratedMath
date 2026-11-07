## 基础单元 B2.30 课后题完整解答 {#cutdiv-answers}

以下解答对应[分割除法、乘法方程与有序域](#cutdiv-unit)。$A,B,C,D,E,F,X$ 等表示分割；函数、族、有理参数与成员的类型在各处说明。$\operatorname{Inv}$ 的域是 $\mathbb R^\times=\{A\in\mathbb R:A\ne0_{\mathbb R}\}$，输出也在这个子集中；没有零的逆元或零分母商。各题使用前单元已证明的逆元存在与唯一性，不把消去律当作存在性证明。

### 题1：商的域与两种乘回 {#cutdiv-a01}

[返回题目](#cutdiv-q01)

定义

$$
\oslash:\mathbb R\times\mathbb R^\times\to\mathbb R,
\qquad A\oslash B=A\otimes\operatorname{Inv}(B).
$$

每个合法输入 $(A,B)$ 都满足 $B\ne0_{\mathbb R}$，所以 $\operatorname{Inv}(B)$ 是唯一且非零的分割。全乘法对 $A$ 与它闭合，且有唯一输出，故商规则确实定义上述函数；这里不要求 $A$ 非零。

对这样的 $A,B$，按定义、结合律、逆元及单位分别计算：

$$
\begin{aligned}
(A\oslash B)\otimes B
&=(A\otimes\operatorname{Inv}(B))\otimes B\\
&=A\otimes(\operatorname{Inv}(B)\otimes B)\\
&=A\otimes1_{\mathbb R}=A,\\
(A\otimes B)\oslash B
&=(A\otimes B)\otimes\operatorname{Inv}(B)\\
&=A\otimes(B\otimes\operatorname{Inv}(B))\\
&=A\otimes1_{\mathbb R}=A.
\end{aligned}
$$

两次除法的第二输入都是 $B$，即使 $A\otimes B=0_{\mathbb R}$，第二种商也合法。因为 $1_{\mathbb R}\ne0_{\mathbb R}$ 且 $\operatorname{Inv}(1_{\mathbb R})=1_{\mathbb R}$，有

$$
A\oslash1_{\mathbb R}=A\otimes1_{\mathbb R}=A.
$$

零乘法又给

$$
0_{\mathbb R}\oslash B
=0_{\mathbb R}\otimes\operatorname{Inv}(B)=0_{\mathbb R}.
$$

因此分子为零不会阻碍除法，分母为零则使输入不在定义域内。$A\oslash0_{\mathbb R}$ 对任何 $A$ 都没有定义，包括 $A=0_{\mathbb R}$。方程 $0_{\mathbb R}\otimes X=0_{\mathbb R}$ 虽有许多解，却没有唯一解可据此指定一个除法函数值。

### 题2：有理商与分割商相容 {#cutdiv-a02}

[返回题目](#cutdiv-q02)

设 $r,s\in\mathbb Q$ 且 $s\ne0$。若 $i(s)=0_{\mathbb R}=i(0)$，嵌入的单射性会给 $s=0$，矛盾。因此 $i(s)$ 为合法分母。由有理逆元相容与全乘法相容，

$$
\begin{aligned}
i(r)\oslash i(s)
&=i(r)\otimes\operatorname{Inv}(i(s))\\
&=i(r)\otimes i(1/s)\\
&=i(r(1/s))=i(r/s).
\end{aligned}
$$

正分母的例子中，$2/5\ne0$ 且它的有理倒数为 $5/2$，所以

$$
i(-3/4)\oslash i(2/5)
=i\bigl((-3/4)(5/2)\bigr)=i(-15/8).
$$

负分母的例子中，$-2/5\ne0$ 且它的倒数为 $-5/2$，所以

$$
i(3/4)\oslash i(-2/5)
=i\bigl((3/4)(-5/2)\bigr)=i(-15/8).
$$

这两个计算都先核分母非零，再使用一般相容式，没有重新假设“分割就是一个已知实数值”。若 $r=0$ 且 $s\ne0$，同一式子给 $i(0)\oslash i(s)=i(0/s)=i(0)$。若 $s=0$，有理数 $1/s$ 与分割 $\operatorname{Inv}(i(s))$ 都不在各自的定义域内，因而不能把 $s=0$ 代入上述证明或结论。

### 题3：乘法方程的全部参数分支 {#cutdiv-a03}

[返回题目](#cutdiv-q03)

固定 $C,D\in\mathbb R$。候选域是 $\mathbb R$，左、右两边分别给函数 $X\mapsto C\otimes X$ 和 $X\mapsto D$，均为 $\mathbb R\to\mathbb R$。解集是

$$
\mathcal S(C,D)=\{X\in\mathbb R:C\otimes X=D\}.
$$

若 $C\ne0_{\mathbb R}$，逆元存在。取 $X_0=\operatorname{Inv}(C)\otimes D$，闭合保证 $X_0\in\mathbb R$。代入得

$$
\begin{aligned}
C\otimes X_0
&=C\otimes(\operatorname{Inv}(C)\otimes D)\\
&=(C\otimes\operatorname{Inv}(C))\otimes D\\
&=1_{\mathbb R}\otimes D=D.
\end{aligned}
$$

所以至少有一个解。若任意候选 $X$ 满足方程，则

$$
\begin{aligned}
X
&=1_{\mathbb R}\otimes X\\
&=(\operatorname{Inv}(C)\otimes C)\otimes X\\
&=\operatorname{Inv}(C)\otimes(C\otimes X)\\
&=\operatorname{Inv}(C)\otimes D=X_0.
\end{aligned}
$$

这依次使用单位、逆元、结合律及方程假设，证明每个解必等于所构造的候选。由交换律和商的定义，$X_0=D\otimes\operatorname{Inv}(C)=D\oslash C$。所以解集恰为单元素集 $\{D\oslash C\}$。

若 $C=0_{\mathbb R}$，则对每个 $X\in\mathbb R$，$C\otimes X=0_{\mathbb R}$。若同时 $D=0_{\mathbb R}$，所有 $X$ 都是解，解集为 $\mathbb R$，其中 $0_{\mathbb R}$ 与 $1_{\mathbb R}$ 已经是两个不同的解。若 $D\ne0_{\mathbb R}$，没有任何 $X$ 能使零乘积等于 $D$，解集为 $\varnothing$。

这三个分支穷尽全部参数，没有使用除零。旧有理方程单元以有理数为候选，不能直接证明当前包含非主分割候选的结论；这里明确重新声明域，并用已建立的分割运算逐步证明了必要性和充分性。

### 题4：乘法函数的两次往返 {#cutdiv-a04}

[返回题目](#cutdiv-q04)

固定 $C\ne0_{\mathbb R}$，IR3保证 $\operatorname{Inv}(C)\ne0_{\mathbb R}$。定义两个函数

$$
\begin{aligned}
&M_C:\mathbb R\to\mathbb R,&&M_C(X)=C\otimes X,\\
&M_{\operatorname{Inv}(C)}:\mathbb R\to\mathbb R,
&&M_{\operatorname{Inv}(C)}(X)=\operatorname{Inv}(C)\otimes X.
\end{aligned}
$$

全乘法闭合保证两者合法，且两个方向的复合均合法，因为中间目标与所接的定义域都是 $\mathbb R$。对任意 $X\in\mathbb R$，

$$
\begin{aligned}
(M_{\operatorname{Inv}(C)}\circ M_C)(X)
&=\operatorname{Inv}(C)\otimes(C\otimes X)\\
&=(\operatorname{Inv}(C)\otimes C)\otimes X\\
&=1_{\mathbb R}\otimes X=X,\\
(M_C\circ M_{\operatorname{Inv}(C)})(X)
&=C\otimes(\operatorname{Inv}(C)\otimes X)\\
&=(C\otimes\operatorname{Inv}(C))\otimes X\\
&=1_{\mathbb R}\otimes X=X.
\end{aligned}
$$

两次逐点等式给

$$
M_{\operatorname{Inv}(C)}\circ M_C=\operatorname{id}_{\mathbb R},
\qquad
M_C\circ M_{\operatorname{Inv}(C)}=\operatorname{id}_{\mathbb R}.
$$

双侧逆定理于是给 $M_C$ 为双射，且逆函数为 $M_{\operatorname{Inv}(C)}$。也可直接读出两个性质：若 $M_C(X)=M_C(Y)$，两边应用 $M_{\operatorname{Inv}(C)}$ 即得 $X=Y$，所以单射；若目标是任意 $D\in\mathbb R$，取

$$
X=M_{\operatorname{Inv}(C)}(D)
=\operatorname{Inv}(C)\otimes D=D\oslash C,
$$

第二次复合恒等就给 $M_C(X)=D$，所以满射。

元素 $\operatorname{Inv}(C)$ 是属于 $\mathbb R^\times$ 的一个分割；逆函数 $M_{\operatorname{Inv}(C)}$ 则以全部 $\mathbb R$ 为域和目标。前者存在以后，才可用它形成后者。此前非零消去只说明相同输出不可能来自不同输入；当前构造额外为每个目标给出实际原输入，补全了满射所需的存在性。

### 题5：一次仿射方程与负系数 {#cutdiv-a05}

[返回题目](#cutdiv-q05)

固定 $C,E,F\in\mathbb R$。候选范围为 $\mathbb R$，两边分别是同域的函数 $X\mapsto(C\otimes X)\oplus E$、$X\mapsto F$。若 $(C\otimes X)\oplus E=F$，两边同加 $N(E)$，得到

$$
\begin{aligned}
C\otimes X
&=(C\otimes X)\oplus(E\oplus N(E))\\
&=((C\otimes X)\oplus E)\oplus N(E)\\
&=F\oplus N(E)=F\ominus E.
\end{aligned}
$$

反过来，若 $C\otimes X=F\ominus E$，则

$$
\begin{aligned}
(C\otimes X)\oplus E
&=(F\ominus E)\oplus E\\
&=(F\oplus N(E))\oplus E\\
&=F\oplus(N(E)\oplus E)=F.
\end{aligned}
$$

这证明双向等价，而不仅是从旧式得到一个必要条件。

若 $C\ne0_{\mathbb R}$，乘法方程的存在性与唯一性给唯一解 $X=(F\ominus E)\oslash C$。若 $C=0_{\mathbb R}$，原式对每个 $X$ 都化为 $E=F$：当 $E=F$ 时解集为 $\mathbb R$，当 $E\ne F$ 时解集为空。它与移项后的目标分类一致，因为 $F\ominus E=0_{\mathbb R}$ 当且仅当 $F=E$：一向是相反数相加；另一向在 $F\oplus N(E)=0_{\mathbb R}$ 两边同加 $E$ 即得 $F=E$。

因此三个分支的解集分别为

$$
\begin{cases}
\{(F\ominus E)\oslash C\},&C\ne0_{\mathbb R},\\
\mathbb R,&C=0_{\mathbb R},\ E=F,\\
\varnothing,&C=0_{\mathbb R},\ E\ne F.
\end{cases}
$$

给定例中 $C=i(-2)\ne0_{\mathbb R}$，由有理差相容，

$$
F\ominus E=i(5/6)\ominus i(1/3)=i(5/6-1/3)=i(1/2).
$$

商相容于是给

$$
X=i(1/2)\oslash i(-2)=i\bigl((1/2)/(-2)\bigr)=i(-1/4).
$$

代回原方程的左侧，

$$
\begin{aligned}
(i(-2)\otimes i(-1/4))\oplus i(1/3)
&=i((-2)(-1/4))\oplus i(1/3)\\
&=i(1/2)\oplus i(1/3)\\
&=i(1/2+1/3)=i(5/6).
\end{aligned}
$$

所以该候选确实是解。因为系数非零，必要性证明又保证任意实数候选若为解，必等于它，故解集为 $\{i(-1/4)\}$。

### 题6：固定除数的弱比较与严格比较 {#cutdiv-a06}

[返回题目](#cutdiv-q06)

设 $A,B\in\mathbb R$。若 $C>_{\mathbb R}0_{\mathbb R}$，则 $C$ 非零，逆元合法且 $\operatorname{Inv}(C)>_{\mathbb R}0_{\mathbb R}$。用正因子双向比较，再展开商的定义，得到

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

若 $C<_{\mathbb R}0_{\mathbb R}$，同号性给 $\operatorname{Inv}(C)<_{\mathbb R}0_{\mathbb R}$。用负因子的双向比较，得到

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

每一行第一步来自已证SR3，包含保持与反射两个方向；第二步只是替换已定义且相等的表达式。SR3允许任意分割 $A,B$，所以分子可以为零，也可以为负。若分子为零而 $C\ne0_{\mathbb R}$，零乘法给 $0_{\mathbb R}\oslash C=0_{\mathbb R}$。

若 $C=0_{\mathbb R}$，$\operatorname{Inv}(C)$ 根本没有定义，两个商表达式都不合法。乘零得到零是一个已经定义的乘法规律，不能用来给零分母商赋值。

### 题7：正倒数反序的共同因子证明 {#cutdiv-a07}

[返回题目](#cutdiv-q07)

设 $A,B>_{\mathbb R}0_{\mathbb R}$。它们均非零，逆元存在且同为正。由正乘积正，

$$
T=\operatorname{Inv}(A)\otimes\operatorname{Inv}(B)>_{\mathbb R}0_{\mathbb R}.
$$

第一端用结合律和 $A$ 的逆元式：

$$
\begin{aligned}
A\otimes T
&=A\otimes(\operatorname{Inv}(A)\otimes\operatorname{Inv}(B))\\
&=(A\otimes\operatorname{Inv}(A))\otimes\operatorname{Inv}(B)\\
&=1_{\mathbb R}\otimes\operatorname{Inv}(B)
=\operatorname{Inv}(B).
\end{aligned}
$$

第二端先交换括号内的两个逆元，再结合并使用 $B$ 的逆元式：

$$
\begin{aligned}
B\otimes T
&=B\otimes(\operatorname{Inv}(A)\otimes\operatorname{Inv}(B))\\
&=B\otimes(\operatorname{Inv}(B)\otimes\operatorname{Inv}(A))\\
&=(B\otimes\operatorname{Inv}(B))\otimes\operatorname{Inv}(A)\\
&=1_{\mathbb R}\otimes\operatorname{Inv}(A)
=\operatorname{Inv}(A).
\end{aligned}
$$

因为 $T$ 是共同正因子，SR3同时给弱比较和严格比较的双向等价。代入两端的化简结果，得到

$$
\begin{aligned}
A\le_{\mathbb R}B
&\Longleftrightarrow A\otimes T\le_{\mathbb R}B\otimes T\\
&\Longleftrightarrow\operatorname{Inv}(B)\le_{\mathbb R}\operatorname{Inv}(A),\\
A<_{\mathbb R}B
&\Longleftrightarrow A\otimes T<_{\mathbb R}B\otimes T\\
&\Longleftrightarrow\operatorname{Inv}(B)<_{\mathbb R}\operatorname{Inv}(A).
\end{aligned}
$$

本证明各次逆元求值都合法，正性保证比较方向，结合与交换保证两端化简；未假设逆乘积公式。

若只保留非零条件，取 $A=i(-1)$、$B=i(1)$。嵌入保持次序给 $A<_{\mathbb R}B$，而有理逆相容给

$$
\operatorname{Inv}(A)=i(-1),\qquad \operatorname{Inv}(B)=i(1).
$$

于是 $\operatorname{Inv}(B)\le_{\mathbb R}\operatorname{Inv}(A)$ 不成立，严格反向比较也不成立。这说明跨零时不能把正输入上的倒数反序直接推广到全部非零输入。

### 题8：逐项核对有序域与完备性的含义 {#cutdiv-a08}

[返回题目](#cutdiv-q08)

域要求：一个零与一不同的交换环，其中每个非零元素都有乘法逆元。在分割系统中，加法闭合来自DA2，交换、结合、单位和相反数来自DG1—DG2；全乘法闭合、交换、结合与单位来自SP1—SP3；两侧全分配来自SR1—SR2。因此这些运算组成交换环。嵌入保持 $0<1$，给 $0_{\mathbb R}<_{\mathbb R}1_{\mathbb R}$，特别地零与一不同。IR1—IR3从正候选和负输入扩展实际证明了每个非零分割的逆元存在，故现在满足域的定义。

有序域还要求全序、加法保序及正乘积正。DC2已证明分割包含序是全序；DG3已证明共同加法平移保序，且能反射比较；正乘积正来自非负乘积的见证证明及全乘法在非负输入上的一致性。因此这些要求也都已经落实。名称本身不额外给零逆元赋值。

本处完备性是 Dedekind 上确界性质：对每个非空且有上界的 $\mathcal G\subseteq\mathbb R$，存在最小上界。DC4已经在同一个分割集合与同一个包含序上证明

$$
\sup_{\mathbb R}\mathcal G
=\{x\in\mathbb Q:\text{存在 }A\in\mathcal G\text{ 使 }x\in A\}
=\bigcup\mathcal G.
$$

其分割闭合依赖非空性提供内点、共同分割上界提供外点，而下闭与无最大元从见证成员继承。每个族成员包含于并集，任何共同上界又包含并集，所以它既为上界又最小。后来添加加法、乘法和逆元没有改变这些集合或次序，故这一既有定理正适用于现在构造的有序域。

对指定族，可完整写为

$$
\mathcal F=\{A\in\mathbb R:\text{存在 }r\in\mathbb Q, r<1\text{ 且 }A=i(r)\}.
$$

由 $0<1$，$i(0)\in\mathcal F$，所以族非空。若 $A\in\mathcal F$，取其有理见证 $r<1$；嵌入保序给 $A=i(r)\le_{\mathbb R}i(1)$。因此 $i(1)$ 是共同分割上界，DC4的两个假设均已核。

现逐成员核对并集。若 $x\in\bigcup\mathcal F$，则 $x$ 是有理数，并且存在 $A\in\mathcal F$ 使 $x\in A$。再展开 $A$ 的条件，得某个有理数 $r<1$ 且 $A=i(r)$。所以 $x<r<1$，从而 $x\in i(1)$。

反过来，设 $x\in i(1)$，即 $x\in\mathbb Q$ 且 $x<1$。令 $r=(x+1)/2\in\mathbb Q$。因为

$$
r-x=\frac{1-x}{2}>0,\qquad 1-r=\frac{1-x}{2}>0,
$$

有 $x<r<1$。于是 $i(r)\in\mathcal F$，且 $x\in i(r)$，故 $x\in\bigcup\mathcal F$。两包含得 $\bigcup\mathcal F=i(1)$，再由DC4得

$$
\sup_{\mathbb R}\mathcal F=i(1).
$$

这里 $A=i(r)$ 是族的分割成员，$x$ 才是该分割或并集的有理成员，不能混用这两种类型。这一具体族只是一般上确界定理的一次应用。

空族没有满足非空假设，无上界族没有满足有上界假设，所以本结论没有对它们许诺实数最小上界，也没有加入无穷大分割。“完备”在本处并未同时证明柯西完备与上确界性质的等价、完备有序域的唯一同构、每个正元素的平方根存在、实数阿基米德性这四项后续结论；实数稠密性及一般极限理论也仍需专门建立。
