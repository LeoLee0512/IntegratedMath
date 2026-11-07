## 基础单元 B2.28 课后题完整解答 {#cutring-answers}

以下解答对应[全分配律、乘法比较与消去](#cutring-unit)。大写字母均表示分割。$P$ 仅接受非负输入，$\otimes$ 是已经按符号定义的全乘法；对非负输入二者一致。取反乘积规律已经由符号定义证明；题1—4才完成全分配，题5以后才能使用所推出的乘法差式。

### 题1：非负乘数下的两种同号加法 {#cutring-a01}

[返回题目](#cutring-q01)

固定 $C\ge_{\mathbb R}0_{\mathbb R}$。

若 $A,B$ 都非负，非负加法闭合给 $A\oplus B$ 非负。因而每个全乘积均可改成 $P$，非负分配NL3给

$$
\begin{aligned}
(A\oplus B)\otimes C
&=P(A\oplus B,C)\\
&=P(A,C)\oplus P(B,C)\\
&=(A\otimes C)\oplus(B\otimes C).
\end{aligned}
$$

若 $A,B$ 都非正，令 $X=N(A)$、$Y=N(B)$。取反反序把 $A\le_{\mathbb R}0_{\mathbb R}$ 化为 $0_{\mathbb R}\le_{\mathbb R}X$，同样得 $Y$ 非负。双重取反给 $A=N(X)$、$B=N(Y)$。已证和的相反数公式给

$$
N(X\oplus Y)=N(X)\oplus N(Y)=A\oplus B.
$$

于是

$$
\begin{aligned}
(A\oplus B)\otimes C
&=N(X\oplus Y)\otimes C\\
&=N\bigl((X\oplus Y)\otimes C\bigr)\\
&=N\bigl(P(X\oplus Y,C)\bigr)\\
&=N\bigl(P(X,C)\oplus P(Y,C)\bigr)\\
&=N(P(X,C))\oplus N(P(Y,C))\\
&=(N(X)\otimes C)\oplus(N(Y)\otimes C)\\
&=(A\otimes C)\oplus(B\otimes C).
\end{aligned}
$$

第二行用前单元从符号定义证明的取反乘积；第三行用非负输入一致性；第四行用NL3；第五行用加法中和的相反数；第六行再反向使用取反乘积。

$X,Y,C$ 的条件只需非负，不要求正，所以 $A=0_{\mathbb R}$、$B=0_{\mathbb R}$ 或 $C=0_{\mathbb R}$ 均可代入。此时 $N(0_{\mathbb R})=0_{\mathbb R}$、零乘及加法单位保证同一串等式成立。没有遗漏同号情况的零边界，也没有在这些步骤中借用待证的全分配。

### 题2：异号加项，非负部分较大 {#cutring-a02}

[返回题目](#cutring-q02)

设 $X,Y,C$ 非负且 $Y\le_{\mathbb R}X$。定义 $D=X\ominus Y=X\oplus N(Y)$。加法差的次序判据给 $D\ge_{\mathbb R}0_{\mathbb R}$。按已证加法结合、逆元和单位，

$$
\begin{aligned}
D\oplus Y
&=(X\oplus N(Y))\oplus Y\\
&=X\oplus(N(Y)\oplus Y)\\
&=X\oplus0_{\mathbb R}=X.
\end{aligned}
$$

因此可把 $X$ 写成两个非负分割的和 $D\oplus Y$。NL3可作用于 $D,Y,C$，给

$$
P(X,C)=P(D\oplus Y,C)=P(D,C)\oplus P(Y,C).
$$

对这个等式的两边同加 $N(P(Y,C))$。右侧经加法群化简，

$$
\begin{aligned}
P(X,C)\oplus N(P(Y,C))
&=(P(D,C)\oplus P(Y,C))\oplus N(P(Y,C))\\
&=P(D,C)\oplus\bigl(P(Y,C)\oplus N(P(Y,C))\bigr)\\
&=P(D,C)\oplus0_{\mathbb R}\\
&=P(D,C).
\end{aligned}
$$

另一方面，$X\oplus N(Y)=D$ 且 $D,C$ 非负，所以

$$
(X\oplus N(Y))\otimes C=D\otimes C=P(D,C).
$$

两式合起来，正好给题目的等式。若再写回两个加项的全乘法，$X\otimes C=P(X,C)$，而取反乘积给 $N(Y)\otimes C=N(P(Y,C))$，所以这确是异号分配。

若 $X=Y$，有 $D=X\oplus N(X)=0_{\mathbb R}$。左侧为零乘积；右侧为 $P(X,C)\oplus N(P(X,C))=0_{\mathbb R}$。这里零的是差 $D$ 和所求两侧，并不能据此说 $X$、$Y$ 或它们各自与 $C$ 的乘积一定为零。

### 题3：异号加项，非正部分的幅度较大 {#cutring-a03}

[返回题目](#cutring-q03)

设 $0_{\mathbb R}\le_{\mathbb R}X<_{\mathbb R}Y$，且 $C$ 非负。令 $E=Y\ominus X=Y\oplus N(X)$。严格差判据给 $E>_{\mathbb R}0_{\mathbb R}$。先实际计算

$$
\begin{aligned}
X\oplus E
&=X\oplus(Y\oplus N(X))\\
&=X\oplus(N(X)\oplus Y)\\
&=(X\oplus N(X))\oplus Y\\
&=0_{\mathbb R}\oplus Y=Y.
\end{aligned}
$$

因此 $Y=X\oplus E$。再用和的相反数和加法群规律，

$$
\begin{aligned}
X\oplus N(Y)
&=X\oplus N(X\oplus E)\\
&=X\oplus(N(X)\oplus N(E))\\
&=(X\oplus N(X))\oplus N(E)\\
&=N(E).
\end{aligned}
$$

由于 $X,E,C$ 都非负，NL3给

$$
P(Y,C)=P(X\oplus E,C)=P(X,C)\oplus P(E,C).
$$

把这个等式代入要比较的右侧，仅用加法规律变形：

$$
\begin{aligned}
P(X,C)\oplus N(P(Y,C))
&=P(X,C)\oplus N\bigl(P(X,C)\oplus P(E,C)\bigr)\\
&=P(X,C)\oplus\bigl(N(P(X,C))\oplus N(P(E,C))\bigr)\\
&=\bigl(P(X,C)\oplus N(P(X,C))\bigr)\oplus N(P(E,C))\\
&=0_{\mathbb R}\oplus N(P(E,C))\\
&=N(P(E,C)).
\end{aligned}
$$

左侧待证乘积为

$$
(X\oplus N(Y))\otimes C
=N(E)\otimes C
=N(E\otimes C)
=N(P(E,C)).
$$

第二个等号用此前已证取反乘积，最后一个等号只对非负的 $E,C$ 使用 $P$。两边相同，故该异号分支成立。即使 $C=0_{\mathbb R}$，也有 $P(E,C)=0_{\mathbb R}$ 和 $N(0_{\mathbb R})=0_{\mathbb R}$，没有漏零因子。

若第一加项非正、第二加项非负，写作 $A=N(X)$、$B=Y$，其中 $X=N(A)\ge_{\mathbb R}0_{\mathbb R}$、$Y=B\ge_{\mathbb R}0_{\mathbb R}$。题2与本题已经覆盖“非负在前、非正在后”的全部比较情况，所以可对 $Y,N(X)$ 应用已得结论：

$$
\begin{aligned}
(A\oplus B)\otimes C
&=(Y\oplus N(X))\otimes C\\
&=(Y\otimes C)\oplus(N(X)\otimes C)\\
&=(B\otimes C)\oplus(A\otimes C)\\
&=(A\otimes C)\oplus(B\otimes C).
\end{aligned}
$$

首尾重排都只用加法交换。整个异号证明先把较大非负分割拆成“较小分割加差”，用非负分配后再作加法化简，没有假定全乘法已经对减法分配。

### 题4：把非负乘数推进到全部乘数 {#cutring-a04}

[返回题目](#cutring-q04)

对非负 $C$，题1覆盖两个加项同为非负或同为非正；题2、3覆盖两个加项符号相反，且按两非负部分的比较处理了相等及两个严格方向。全序保证任意两个加项属于这些情况之一，所以对任意 $A,B$ 和非负 $C$，第一种分配已经证明。

现在设 $C<_{\mathbb R}0_{\mathbb R}$，令 $K=N(C)$。取反反序给 $K>_{\mathbb R}0_{\mathbb R}$，双重取反给 $C=N(K)$。对每个分割 $Z$，取反乘积规律给

$$
Z\otimes C=Z\otimes N(K)=N(Z\otimes K).
$$

于是可以计算

$$
\begin{aligned}
(A\oplus B)\otimes C
&=N\bigl((A\oplus B)\otimes K\bigr)\\
&=N\bigl((A\otimes K)\oplus(B\otimes K)\bigr)\\
&=N(A\otimes K)\oplus N(B\otimes K)\\
&=(A\otimes C)\oplus(B\otimes C).
\end{aligned}
$$

第一、四步用已证符号规律；第二步的因子 $K$ 正，属于已完成的非负因子分配；第三步是加法中和的相反数。$C\ge_{\mathbb R}0_{\mathbb R}$ 与 $C<_{\mathbb R}0_{\mathbb R}$ 穷尽，所以第一种分配对全部输入成立。

另一侧分配通过全乘法交换逐项得到：

$$
\begin{aligned}
C\otimes(A\oplus B)
&=(A\oplus B)\otimes C\\
&=(A\otimes C)\oplus(B\otimes C)\\
&=(C\otimes A)\oplus(C\otimes B).
\end{aligned}
$$

此处没有证明循环。前一单元的取反乘积由全乘法四个符号分支、非负乘积和双重取反直接证明，并未以全分配为前提。本题在此既有结论上完成全分配；如果反过来先借分配证明符号规律，再用同一符号规律证明分配，才会形成循环。

### 题5：分配以后才能使用乘法差式 {#cutring-a05}

[返回题目](#cutring-q05)

现在题4的两侧全分配已经完成。对任意分割 $A,B,C$，按差定义和取反乘积，

$$
\begin{aligned}
(A\ominus B)\otimes C
&=(A\oplus N(B))\otimes C\\
&=(A\otimes C)\oplus(N(B)\otimes C)\\
&=(A\otimes C)\oplus N(B\otimes C)\\
&=(A\otimes C)\ominus(B\otimes C).
\end{aligned}
$$

另一侧依次使用第二种分配和第二输入取反规律：

$$
\begin{aligned}
C\otimes(A\ominus B)
&=C\otimes(A\oplus N(B))\\
&=(C\otimes A)\oplus(C\otimes N(B))\\
&=(C\otimes A)\oplus N(C\otimes B)\\
&=(C\otimes A)\ominus(C\otimes B).
\end{aligned}
$$

两条公式都在使用处有全分配作为依据，不能挪到题2、3中提前代替异号证明。

具体取 $A=i(-2/3)$、$B=i(1/6)$、$C=i(3/5)$。已证有理差相容给

$$
A\ominus B=i(-2/3-1/6)=i(-4/6-1/6)=i(-5/6).
$$

再用全符号有理乘法相容，

$$
(A\ominus B)\otimes C
=i\bigl((-5/6)(3/5)\bigr)=i(-1/2).
$$

分别计算右侧两个乘积，

$$
A\otimes C=i\bigl((-2/3)(3/5)\bigr)=i(-2/5),
$$

$$
B\otimes C=i\bigl((1/6)(3/5)\bigr)=i(1/10).
$$

因此

$$
(A\otimes C)\ominus(B\otimes C)
=i(-2/5-1/10)=i(-4/10-1/10)=i(-1/2).
$$

两侧一致。每个分数计算在已有有理数中完成，再通过 $i$ 进入分割；这个算例没有替代前面的全称证明。

交换环需要加法交换群、乘法闭合与结合、乘法单位、两侧分配，以及乘法交换。分割加法群已有完整证明；全乘法闭合、交换、单位和结合来自前一单元，本题之前已经补全两侧分配。所以现在可以给这一具体结构命名为交换环。只有符号表和结合律仍不足，因为尚未说明乘法与加法之间的分配关系。名称不能替代缺少的结构条件。

### 题6：正因子下，原加项不必非负 {#cutring-a06}

[返回题目](#cutring-q06)

固定正 $C$。先设 $A\le_{\mathbb R}B$，令 $D=B\ominus A$。第一次使用差的次序判据，得到

$$
D\ge_{\mathbb R}0_{\mathbb R}.
$$

因为 $D,C$ 都非负，$D\otimes C=P(D,C)$ 非负。题5的差乘公式给

$$
D\otimes C
=(B\ominus A)\otimes C
=(B\otimes C)\ominus(A\otimes C).
$$

所以 $(B\otimes C)\ominus(A\otimes C)\ge_{\mathbb R}0_{\mathbb R}$。第二次使用差的次序判据，得到 $A\otimes C\le_{\mathbb R}B\otimes C$，这证明弱保持。该部分实际上也允许 $C=0_{\mathbb R}$。

如果原比较严格，即 $A<_{\mathbb R}B$，第一次差判据给 $D>_{\mathbb R}0_{\mathbb R}$。由于 $C$ 正，正积结论给 $D\otimes C>_{\mathbb R}0_{\mathbb R}$。借同一个差乘等式，再用严格差判据，得到 $A\otimes C<_{\mathbb R}B\otimes C$。这里两次差判据都用严格版本。

反射不能只从弱保持得到。设乘积满足 $A\otimes C\le_{\mathbb R}B\otimes C$。若原比较 $A\le_{\mathbb R}B$ 为假，包含全序给 $B<_{\mathbb R}A$；对这对交换输入用刚证严格保持，得到 $B\otimes C<_{\mathbb R}A\otimes C$，与假设冲突。因此 $A\le_{\mathbb R}B$。

若乘积严格比较，先由上述不严格反射得 $A\le_{\mathbb R}B$。假如 $A=B$，同一输入的函数值相等，两乘积应相等，又与严格比较冲突。因此 $A<_{\mathbb R}B$。两种双向结论均得证。

本题允许 $A,B$ 是任意分割。没有直接写可能越域的 $P(A,C)$ 或 $P(B,C)$；进入 $P$ 的只有已由比较证明非负的差 $D$ 和正因子 $C$。原输入的乘积使用对全部分割定义的 $\otimes$。这正是全分配差式把非负乘积性质用于一般比较的作用。

### 题7：负因子和零因子的全部边界 {#cutring-a07}

[返回题目](#cutring-q07)

先设 $C<_{\mathbb R}0_{\mathbb R}$。令 $K=N(C)$，则 $K>_{\mathbb R}0_{\mathbb R}$，且 $C=N(K)$。由取反乘积，

$$
A\otimes C=N(A\otimes K),\qquad
B\otimes C=N(B\otimes K).
$$

题6对正 $K$ 的双向结论与DG4取反反序给

$$
\begin{aligned}
A\le_{\mathbb R}B
&\Longleftrightarrow A\otimes K\le_{\mathbb R}B\otimes K\\
&\Longleftrightarrow N(B\otimes K)\le_{\mathbb R}N(A\otimes K)\\
&\Longleftrightarrow B\otimes C\le_{\mathbb R}A\otimes C.
\end{aligned}
$$

每个连接均为双向：正因子既保持又反射，取反也已证明两向反序，所以最后确能反推原比较。

严格情形分别使用同两条结论的严格形式，

$$
\begin{aligned}
A<_{\mathbb R}B
&\Longleftrightarrow A\otimes K<_{\mathbb R}B\otimes K\\
&\Longleftrightarrow N(B\otimes K)<_{\mathbb R}N(A\otimes K)\\
&\Longleftrightarrow B\otimes C<_{\mathbb R}A\otimes C.
\end{aligned}
$$

所以负因子把比较方向颠倒，但保留完整的双向关系。

若 $C=0_{\mathbb R}$，任意输入的乘积都为零。取 $A=0_{\mathbb R}$、$B=1_{\mathbb R}$，原来 $A<_{\mathbb R}B$，乘后相等，严格保持失败。另取 $A=1_{\mathbb R}$、$B=0_{\mathbb R}$，乘后仍有 $A\otimes C\le_{\mathbb R}B\otimes C$，但原来的 $A\le_{\mathbb R}B$ 为假，所以反射失败。正、负因子的反射条件不能放宽到包括零。

共同因子在左侧时，乘法交换给 $C\otimes A=A\otimes C$、$C\otimes B=B\otimes C$。将这两个等式代入上面的正因子、负因子或零因子结论，就逐项得到左乘的版本；没有额外假定另一种乘法次序定理。

### 题8：两种消去证明与存在性缺口 {#cutring-a08}

[返回题目](#cutring-q08)

设 $C\ne0_{\mathbb R}$，假设 $A\otimes C=B\otimes C$。

**次序证明。** 全序把非零 $C$ 分为正、负两种。若 $C$ 正，相等给 $A\otimes C\le_{\mathbb R}B\otimes C$ 和 $B\otimes C\le_{\mathbb R}A\otimes C$。题6分别反射成 $A\le_{\mathbb R}B$ 和 $B\le_{\mathbb R}A$，反对称性给 $A=B$。

若 $C$ 负，由相等先取 $B\otimes C\le_{\mathbb R}A\otimes C$，题7的反序反射给 $A\le_{\mathbb R}B$；另取 $A\otimes C\le_{\mathbb R}B\otimes C$，反序反射给 $B\le_{\mathbb R}A$。同样得到 $A=B$。两种情形已穷尽，不能漏掉负因子的方向颠倒。

**代数证明。** 题5给

$$
\begin{aligned}
(A\ominus B)\otimes C
&=(A\otimes C)\ominus(B\otimes C)\\
&=(B\otimes C)\ominus(B\otimes C)\\
&=0_{\mathbb R}.
\end{aligned}
$$

最后一个等号来自加法逆元，因为 $Z\ominus Z=Z\oplus N(Z)=0_{\mathbb R}$。前一单元已证明全符号零积判据，所以 $A\ominus B=0_{\mathbb R}$ 或 $C=0_{\mathbb R}$。后者被假设排除，故 $A\ominus B=0_{\mathbb R}$。

为从零差恢复相等，把 $B$ 加回去并用加法群：

$$
\begin{aligned}
A
&=A\oplus0_{\mathbb R}\\
&=A\oplus(N(B)\oplus B)\\
&=(A\oplus N(B))\oplus B\\
&=(A\ominus B)\oplus B\\
&=0_{\mathbb R}\oplus B=B.
\end{aligned}
$$

这份证明完全没有除以 $C$。它用了全分配之后的差乘公式，而不只是形式上把同一因子划掉。

反过来，若 $A=B$，相等输入的乘积相等，所以相等的双向结论成立。乘法交换还给共同左因子的消去。若 $C=0_{\mathbb R}$，则 $0_{\mathbb R}\otimes C=1_{\mathbb R}\otimes C$，但 $0_{\mathbb R}\ne1_{\mathbb R}$，说明非零条件确实不可删除。

固定非零分割 $C$，定义函数

$$
M_C:\mathbb R\longrightarrow\mathbb R,\qquad
M_C(A)=A\otimes C.
$$

全乘法闭合给目标合法；两种消去证明中的任一种都给 $M_C(A)=M_C(B)\Rightarrow A=B$，故 $M_C$ 单射。满射要求对任意目标 $Y\in\mathbb R$ 至少找到一个输入；本题没有做这种构造。非零消去保证方程 $A\otimes C=Y$ 至多有一个解，并不说明至少有一个解。

当前已证明交换环全部规律，以及全序、加法序相容、正乘积正和相应乘法比较，所以可以称为有序交换环。没有为每个非零 $C$ 构造满足 $A\otimes C=1_{\mathbb R}$ 的 $A$，就尚未完成倒数、除法及有序域的证明。把存在性留给后续具体构造，不是宣称这种倒数不存在。
