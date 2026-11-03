## 基础单元 B2.28 全分配律、乘法比较与消去 {#cutring-unit}

**学习目标与位置。** 全部分割的乘法已经按输入符号定义，并有交换、结合、单位、乘零和取反规律。尚须证明它与全部分割的加法相容，特别是两个加项符号相反时的分配律。本单元先完成这项证明，再推出乘法对差的作用、正负因子的双向次序比较及非零消去。主归属第526章97F50的实数基础教学部分；06A05与06F25交叉。全部结论建立后得到有序交换环，分割倒数和除法仍待后续构造。

**精确先修。** 使用[全符号乘法定义与闭合](#cutsigned-definition)、[交换、零、单位及取反乘积](#cutsigned-signs)、[全结合律](#cutsigned-associative)、[有理相容与零积判据](#cutsigned-rational-zero)。非负输入使用[乘积定义与正性](#cutprod-definition)、[非负和及见证](#cutprod-cofinal-witnesses)、[两侧非负分配](#cutprod-distributive)。加法使用[交换结合与单位](#cutgroup-laws)、[逆元与双重取反](#cutgroup-inverses)、[双向序平移](#cutgroup-translation)、[取反反序、和的相反数及差的判据](#cutgroup-negation-subtraction)，次序使用[包含全序](#cut-order-embedding)。函数部分使用[函数定义](#fun-definition)、[单射](#bij-injective)及[满射](#bij-surjective)。

**对象与记号。** $A,B,C,X,Y,D,E,K$ 均表示分割。沿用加法 $\oplus$、相反数函数 $N$ 和差 $A\ominus B=A\oplus N(B)$。全乘法记为 $A\otimes B$，它对全部 $\mathbb R\times\mathbb R$ 有定义；只有两个输入都非负时，才可把它改写为前两单元的 $P(A,B)$。零与一分别是 $0_{\mathbb R}=i(0)$、$1_{\mathbb R}=i(1)$。

以下会使用已经从符号定义证明的规则

$$
N(A)\otimes B=N(A\otimes B)=A\otimes N(B).
$$

它在本单元不是从分配律推出的；前一单元已逐符号证明它，包括零输入。现在可以用它连接不同符号的乘积，但仍不能提前使用待证的乘法差公式。

### 1. 先固定一个非负乘数 {#cutring-distributive-nonnegative-factor}

**命题 SR1。** 固定 $C\ge_{\mathbb R}0_{\mathbb R}$。对任意分割 $A,B$，

$$
(A\oplus B)\otimes C
=(A\otimes C)\oplus(B\otimes C).
$$

证明按两个加项的符号展开。非负分配只处理两个加项都非负的情形；异号时，我们将比较两个非负分割，再用已经建立的加法群规律移项。

**两个加项都非负。** 若 $A,B\ge_{\mathbb R}0_{\mathbb R}$，它们的和也非负。全部乘积均可改写成 $P$，NL3直接给

$$
(A\oplus B)\otimes C
=P(A\oplus B,C)
=P(A,C)\oplus P(B,C)
=(A\otimes C)\oplus(B\otimes C).
$$

**两个加项都非正。** 若 $A,B\le_{\mathbb R}0_{\mathbb R}$，令 $X=N(A)$、$Y=N(B)$。取反反序保证 $X,Y$ 非负，双重取反给 $A=N(X)$、$B=N(Y)$。由和的相反数规律，

$$
A\oplus B=N(X)\oplus N(Y)=N(X\oplus Y).
$$

$X\oplus Y$ 非负，所以可按以下顺序计算：

$$
\begin{aligned}
(A\oplus B)\otimes C
&=N(X\oplus Y)\otimes C\\
&=N\bigl(P(X\oplus Y,C)\bigr)\\
&=N\bigl(P(X,C)\oplus P(Y,C)\bigr)\\
&=N(P(X,C))\oplus N(P(Y,C))\\
&=(A\otimes C)\oplus(B\otimes C).
\end{aligned}
$$

【依据：第二行用已证取反乘积及非负输入的一致性；第三行用NL3；第四行只用加法中和的相反数；最后再用取反乘积。没有把全分配律作为任何一步的理由。】

这些式子允许 $X$、$Y$ 或 $C$ 为零，因为所调用的规律均包括零。

**第一加项非负，第二加项非正。** 写成

$$
A=X\ge_{\mathbb R}0_{\mathbb R},\qquad
B=N(Y),\qquad Y\ge_{\mathbb R}0_{\mathbb R}.
$$

此时待比较的两个表达式是

$$
(X\oplus N(Y))\otimes C
\quad\text{与}\quad
P(X,C)\oplus N(P(Y,C)).
$$

不能先说“乘法对减法分配”，因为那正是尚待建立的结论。按包含全序，分成 $Y\le_{\mathbb R}X$ 和 $X<_{\mathbb R}Y$ 两种情形。

**情形一：$Y\le_{\mathbb R}X$。** 令

$$
D=X\ominus Y=X\oplus N(Y).
$$

差的次序判据给 $D\ge_{\mathbb R}0_{\mathbb R}$。加法结合、逆元与单位给

$$
D\oplus Y=(X\oplus N(Y))\oplus Y
=X\oplus(N(Y)\oplus Y)=X.
$$

因此 $X=D\oplus Y$，而 $D,Y,C$ 都非负，可以用NL3得到

$$
P(X,C)=P(D\oplus Y,C)=P(D,C)\oplus P(Y,C).
$$

现在对这个已证等式作**加法**移项：

$$
\begin{aligned}
P(X,C)\oplus N(P(Y,C))
&=(P(D,C)\oplus P(Y,C))\oplus N(P(Y,C))\\
&=P(D,C)\oplus\bigl(P(Y,C)\oplus N(P(Y,C))\bigr)\\
&=P(D,C)\oplus0_{\mathbb R}\\
&=P(D,C).
\end{aligned}
$$

另一方面，$A\oplus B=D$，故左侧待证乘积是 $D\otimes C=P(D,C)$。两边于是相等。$X=Y$ 包含在这一情形中：此时 $D=X\oplus N(X)=0_{\mathbb R}$，上述所有公式仍然合法。

**情形二：$X<_{\mathbb R}Y$。** 令

$$
E=Y\ominus X=Y\oplus N(X)>_{\mathbb R}0_{\mathbb R}.
$$

先用加法群规律核 $X\oplus E=Y$：在 $X\oplus(Y\oplus N(X))$ 内交换 $Y,N(X)$，再结合，使 $X\oplus N(X)$ 消成零。因而 $Y=X\oplus E$。和的相反数与单位进一步给

$$
\begin{aligned}
X\oplus N(Y)
&=X\oplus N(X\oplus E)\\
&=X\oplus(N(X)\oplus N(E))\\
&=(X\oplus N(X))\oplus N(E)\\
&=N(E).
\end{aligned}
$$

对非负的 $X,E,C$ 使用NL3，

$$
P(Y,C)=P(X\oplus E,C)=P(X,C)\oplus P(E,C).
$$

所以右侧待证两项和可以按已证加法规律化简为

$$
\begin{aligned}
P(X,C)\oplus N(P(Y,C))
&=P(X,C)\oplus N\bigl(P(X,C)\oplus P(E,C)\bigr)\\
&=P(X,C)\oplus\bigl(N(P(X,C))\oplus N(P(E,C))\bigr)\\
&=\bigl(P(X,C)\oplus N(P(X,C))\bigr)\oplus N(P(E,C))\\
&=N(P(E,C)).
\end{aligned}
$$

左侧待证乘积则为

$$
(A\oplus B)\otimes C
=N(E)\otimes C
=N(E\otimes C)=N(P(E,C)).
$$

这里最后三步使用已经证明的取反乘积及非负输入一致性。两侧再次相等，第二情形完成。

**第一加项非正，第二加项非负。** 设 $A\le_{\mathbb R}0_{\mathbb R}$、$B\ge_{\mathbb R}0_{\mathbb R}$。把刚完成的异号结论应用于第一加项 $B$ 与第二加项 $A$，再用加法交换：

$$
\begin{aligned}
(A\oplus B)\otimes C
&=(B\oplus A)\otimes C\\
&=(B\otimes C)\oplus(A\otimes C)\\
&=(A\otimes C)\oplus(B\otimes C).
\end{aligned}
$$

包含全序保证任意 $A,B$ 至少属于上述一种符号情况；零可能使情况重合，但各条推导均含零且给同一等式。因此SR1覆盖全部加项。共同因子 $C=0_{\mathbb R}$ 也始终包含在这些非负因子的证明中。

### 2. 任意乘数、两侧分配与差式 {#cutring-distributive}

**命题 SR2。** 对任意 $A,B,C\in\mathbb R$，

$$
(A\oplus B)\otimes C
=(A\otimes C)\oplus(B\otimes C),
$$

$$
C\otimes(A\oplus B)
=(C\otimes A)\oplus(C\otimes B).
$$

此外，

$$
(A\ominus B)\otimes C
=(A\otimes C)\ominus(B\otimes C),
$$

$$
C\otimes(A\ominus B)
=(C\otimes A)\ominus(C\otimes B).
$$

**补上负乘数。** 若 $C\ge_{\mathbb R}0_{\mathbb R}$，第一式已经由SR1证明。若 $C<_{\mathbb R}0_{\mathbb R}$，令 $K=N(C)>_{\mathbb R}0_{\mathbb R}$，双重取反给 $C=N(K)$。对任意分割 $Z$，已有取反乘积给

$$
Z\otimes C=Z\otimes N(K)=N(Z\otimes K).
$$

因此

$$
\begin{aligned}
(A\oplus B)\otimes C
&=N\bigl((A\oplus B)\otimes K\bigr)\\
&=N\bigl((A\otimes K)\oplus(B\otimes K)\bigr)\\
&=N(A\otimes K)\oplus N(B\otimes K)\\
&=(A\otimes C)\oplus(B\otimes C).
\end{aligned}
$$

第二行对非负因子 $K$ 使用已经完成的SR1；第三行使用加法中和的相反数。这样负乘数也被覆盖，没有把取反乘积与待证分配互相作为证明依据。

**另一侧分配。** 利用全乘法已经证明的交换律，

$$
\begin{aligned}
C\otimes(A\oplus B)
&=(A\oplus B)\otimes C\\
&=(A\otimes C)\oplus(B\otimes C)\\
&=(C\otimes A)\oplus(C\otimes B).
\end{aligned}
$$

全部分割都在全乘法的定义域内，不再限于非负输入。

**此时才能推出乘法差式。** 按差的定义、刚证分配与已证取反乘积，

$$
\begin{aligned}
(A\ominus B)\otimes C
&=(A\oplus N(B))\otimes C\\
&=(A\otimes C)\oplus(N(B)\otimes C)\\
&=(A\otimes C)\oplus N(B\otimes C)\\
&=(A\otimes C)\ominus(B\otimes C).
\end{aligned}
$$

另一侧使用第二种分配，

$$
\begin{aligned}
C\otimes(A\ominus B)
&=C\otimes(A\oplus N(B))\\
&=(C\otimes A)\oplus(C\otimes N(B))\\
&=(C\otimes A)\oplus N(C\otimes B)\\
&=(C\otimes A)\ominus(C\otimes B).
\end{aligned}
$$

SR2证毕。SR1的异号证明中，我们只对加法等式作移项，没有提前使用这里刚得到的差式。

**现在可以命名已证结构。** 一个集合配有加法与乘法，若加法构成交换群，乘法封闭、结合且有单位，并满足两侧分配律，本书称这套结构为带单位的**环**；乘法还交换时称为**交换环**。前文已证明分割加法交换群，上一单元已证明全乘法封闭、交换、结合及单位，本节补全两侧分配，所以这些分割运算构成交换环。本书这一具体结构还有 $0_{\mathbb R}\ne1_{\mathbb R}$，因为嵌入保序给 $0_{\mathbb R}<_{\mathbb R}1_{\mathbb R}$。名称汇总已经证明的规则，不是反过来为前面的推理提供新公理。

### 3. 正、负、零因子的比较要分别处理 {#cutring-multiplication-order}

**命题 SR3。** 对任意分割 $A,B,C$：

若 $C>_{\mathbb R}0_{\mathbb R}$，则

$$
A\le_{\mathbb R}B\Longleftrightarrow A\otimes C\le_{\mathbb R}B\otimes C,
$$

$$
A<_{\mathbb R}B\Longleftrightarrow A\otimes C<_{\mathbb R}B\otimes C.
$$

若 $C<_{\mathbb R}0_{\mathbb R}$，则

$$
A\le_{\mathbb R}B\Longleftrightarrow B\otimes C\le_{\mathbb R}A\otimes C,
$$

$$
A<_{\mathbb R}B\Longleftrightarrow B\otimes C<_{\mathbb R}A\otimes C.
$$

若 $C=0_{\mathbb R}$，两个乘积都为零，不能由乘后比较反推原比较。

此外，若只要求由 $A\le_{\mathbb R}B$ 推出 $A\otimes C\le_{\mathbb R}B\otimes C$，共同因子可放宽为 $C\ge_{\mathbb R}0_{\mathbb R}$。

**先证明非负因子的弱保持。** 设 $A\le_{\mathbb R}B$、$C\ge_{\mathbb R}0_{\mathbb R}$，令 $D=B\ominus A$。差的次序判据给 $D\ge_{\mathbb R}0_{\mathbb R}$，故非负乘积闭合给

$$
D\otimes C=P(D,C)\ge_{\mathbb R}0_{\mathbb R}.
$$

SR2的差式使这一个乘积等于

$$
D\otimes C=(B\ominus A)\otimes C
=(B\otimes C)\ominus(A\otimes C).
$$

再用DG4的差判据，得到 $A\otimes C\le_{\mathbb R}B\otimes C$。这里原来的 $A,B$ 可以为负；被用于 $P$ 的是已经证明非负的差 $D$ 与因子 $C$。

**正因子的严格保持。** 若进一步 $A<_{\mathbb R}B$ 且 $C>_{\mathbb R}0_{\mathbb R}$，则 $D>_{\mathbb R}0_{\mathbb R}$。两个正分割的乘积正，故

$$
0_{\mathbb R}<_{\mathbb R}D\otimes C
=(B\otimes C)\ominus(A\otimes C).
$$

DG4的严格差判据立即给 $A\otimes C<_{\mathbb R}B\otimes C$。

**正因子的反射。** 设 $C>_{\mathbb R}0_{\mathbb R}$ 且 $A\otimes C\le_{\mathbb R}B\otimes C$。如果 $A\le_{\mathbb R}B$ 不成立，全序给 $B<_{\mathbb R}A$；刚证严格保持将给 $B\otimes C<_{\mathbb R}A\otimes C$，与假设矛盾。因此 $A\le_{\mathbb R}B$。

若已知乘积严格比较，先用上述不严格反射得 $A\le_{\mathbb R}B$；相等 $A=B$ 会使乘积相等，与严格比较冲突，所以 $A<_{\mathbb R}B$。正因子的两种双向结论至此都成立。

**负因子把方向反过来。** 若 $C<_{\mathbb R}0_{\mathbb R}$，令 $K=N(C)>_{\mathbb R}0_{\mathbb R}$。已有

$$
A\otimes C=N(A\otimes K),\qquad
B\otimes C=N(B\otimes K).
$$

把正因子的双向比较与取反反序的双向结论连接起来：

$$
\begin{aligned}
A\le_{\mathbb R}B
&\Longleftrightarrow A\otimes K\le_{\mathbb R}B\otimes K\\
&\Longleftrightarrow N(B\otimes K)\le_{\mathbb R}N(A\otimes K)\\
&\Longleftrightarrow B\otimes C\le_{\mathbb R}A\otimes C.
\end{aligned}
$$

第一步因 $K>_{\mathbb R}0_{\mathbb R}$ 合法，第二步用DG4，第三步代入符号公式。对严格比较，分别调用这两个已证严格双向版本，得到

$$
\begin{aligned}
A<_{\mathbb R}B
&\Longleftrightarrow A\otimes K<_{\mathbb R}B\otimes K\\
&\Longleftrightarrow N(B\otimes K)<_{\mathbb R}N(A\otimes K)\\
&\Longleftrightarrow B\otimes C<_{\mathbb R}A\otimes C.
\end{aligned}
$$

没有在未经证明时直接“划掉一个负因子”；反向来自整条双向等价。

**零因子。** 乘零规律给 $A\otimes0_{\mathbb R}=0_{\mathbb R}=B\otimes0_{\mathbb R}$。例如 $1_{\mathbb R}\not\le_{\mathbb R}0_{\mathbb R}$，但乘零后两个结果相等，满足不严格比较，因此反射失败。原来的严格比较 $0_{\mathbb R}<_{\mathbb R}1_{\mathbb R}$ 也在乘零后变为相等。

全乘法交换律把以上结论逐项转为共同因子在左侧的版本。已有全序、加法序平移、$0_{\mathbb R}<_{\mathbb R}1_{\mathbb R}$ 以及正乘积正，这一具体交换环称为**有序交换环**。这里依然没有得到所有非零分割的乘法逆元。

### 4. 非零因子可以消去，但尚未给出除法 {#cutring-cancellation}

**命题 SR4。** 设 $C\ne0_{\mathbb R}$。对任意分割 $A,B$，

$$
A\otimes C=B\otimes C\quad\Longleftrightarrow\quad A=B.
$$

共同因子在左侧时也成立。下面给出两种证明，以说明不同先修各承担什么作用。

**用次序反射。** 假设两乘积相等。若 $C>_{\mathbb R}0_{\mathbb R}$，相等给两个方向的非严格比较，SR3分别反射为 $A\le_{\mathbb R}B$ 与 $B\le_{\mathbb R}A$。反对称性给 $A=B$。

若 $C<_{\mathbb R}0_{\mathbb R}$，先取相等中的方向 $B\otimes C\le_{\mathbb R}A\otimes C$，负因子的反序反射给 $A\le_{\mathbb R}B$；另一个方向 $A\otimes C\le_{\mathbb R}B\otimes C$ 给 $B\le_{\mathbb R}A$。仍由反对称性得 $A=B$。因为 $C\ne0_{\mathbb R}$，全序保证这两个符号情况穷尽。

**用差式与零积。** 从相等的假设出发，SR2给

$$
(A\ominus B)\otimes C
=(A\otimes C)\ominus(B\otimes C)
=0_{\mathbb R}.
$$

最后一步使用相等的加法对象与其逆元相加为零。前一单元的全符号零积判据给

$$
A\ominus B=0_{\mathbb R}\quad\text{或}\quad C=0_{\mathbb R}.
$$

假设排除后一项，因此 $A\ominus B=0_{\mathbb R}$。再按加法规律恢复原等式：

$$
\begin{aligned}
A
&=A\oplus(N(B)\oplus B)\\
&=(A\oplus N(B))\oplus B\\
&=(A\ominus B)\oplus B\\
&=0_{\mathbb R}\oplus B=B.
\end{aligned}
$$

这里没有除以 $C$。使用的是已经证明的全分配差式、零积判据与加法群。

反向，若 $A=B$，相等输入的乘积当然相等。交换律给左侧共同因子的消去。SR4证毕。

零因子不可保留：$0_{\mathbb R}\otimes0_{\mathbb R}=1_{\mathbb R}\otimes0_{\mathbb R}$，而 $0_{\mathbb R}\ne1_{\mathbb R}$。

固定非零 $C$ 的乘法规则

$$
M_C:\mathbb R\to\mathbb R,\qquad M_C(A)=A\otimes C
$$

已有闭合且为单射。要证明它满射，仍须对每个目标 $B$ 构造输入 $A$ 使 $A\otimes C=B$；尤其需要为目标 $1_{\mathbb R}$ 构造原输入。非零消去只说这样的输入若存在则唯一，没有提供存在见证。倒数、除法及有序域将在后续完成相应构造与证明之后命名。

### 5. 课后题 {#cutring-exercises}

#### 题1：非负乘数下的两种同号加法 {#cutring-q01}

固定 $C\ge_{\mathbb R}0_{\mathbb R}$。分别对 $A,B\ge_{\mathbb R}0_{\mathbb R}$ 和 $A,B\le_{\mathbb R}0_{\mathbb R}$，证明 $(A\oplus B)\otimes C=(A\otimes C)\oplus(B\otimes C)$。非正情形写出 $X=N(A),Y=N(B)$，逐项标明非负分配、取反乘积与和的相反数的使用位置，并检查零边界。[完整解答](#cutring-a01)

#### 题2：异号加项，非负部分较大 {#cutring-q02}

设 $X,Y,C\ge_{\mathbb R}0_{\mathbb R}$ 且 $Y\le_{\mathbb R}X$。取 $D=X\ominus Y$，从 $D\ge_{\mathbb R}0_{\mathbb R}$、$X=D\oplus Y$ 出发，用非负分配与加法移项证明 $(X\oplus N(Y))\otimes C=P(X,C)\oplus N(P(Y,C))$。单独说明 $X=Y$ 时哪些量为零。[完整解答](#cutring-a02)

#### 题3：异号加项，非正部分的幅度较大 {#cutring-q03}

设 $0_{\mathbb R}\le_{\mathbb R}X<_{\mathbb R}Y$、$C\ge_{\mathbb R}0_{\mathbb R}$。取 $E=Y\ominus X$，证明 $Y=X\oplus E$ 及 $X\oplus N(Y)=N(E)$，继而完成异号分配。再说明第一加项非正、第二加项非负时如何逐式归约。不得预用尚未由这些证明建立的乘法差式。[完整解答](#cutring-a03)

#### 题4：把非负乘数推进到全部乘数 {#cutring-q04}

结合题1—3，先说明任意两个加项、非负因子的分配已被覆盖。对 $C<_{\mathbb R}0_{\mathbb R}$ 令 $K=N(C)$，完整证明相同分配。再由交换得到另一侧分配，解释这里使用的取反乘积为何不与全分配形成循环。[完整解答](#cutring-a04)

#### 题5：分配以后才能使用乘法差式 {#cutring-q05}

从差的定义逐行推出两侧乘法差式。取 $A=i(-2/3)$、$B=i(1/6)$、$C=i(3/5)$，分别计算 $(A\ominus B)\otimes C$ 与 $(A\otimes C)\ominus(B\otimes C)$，核对相同结果。说明交换环名称需要哪些已证规律，为什么只有符号表和结合律还不够。[完整解答](#cutring-a05)

#### 题6：正因子下，原加项不必非负 {#cutring-q06}

对任意分割 $A,B$ 及 $C>_{\mathbb R}0_{\mathbb R}$，利用 $D=B\ominus A$ 完整证明弱保持、严格保持及它们的反射。写出差乘公式和两次差的序判据；说明为什么没有把可能为负的 $A,B$ 直接放进 $P$。[完整解答](#cutring-a06)

#### 题7：负因子和零因子的全部边界 {#cutring-q07}

对 $C<_{\mathbb R}0_{\mathbb R}$，用 $K=N(C)$、题6与取反反序，分别写出不严格、严格比较的双向等价。对 $C=0_{\mathbb R}$ 给严格保持和反射失败的反例。再说明共同因子放在左侧时如何得到结论。[完整解答](#cutring-a07)

#### 题8：两种消去证明与存在性缺口 {#cutring-q08}

设 $C\ne0_{\mathbb R}$，分别用次序反射和“差乘为零”证明 $A\otimes C=B\otimes C$ 当且仅当 $A=B$。说明零因子为何失败，并写出固定非零因子乘法函数的定义域、目标与单射依据。当前是否已证明这个函数满射、所有非零分割都有倒数，或已完成有序域？[完整解答](#cutring-a08)

**来源与范围说明。** 结构义务与外部定理前提的对照见[分割乘法来源审计](#dedekind-signed-sources)。本文的异号分配由非负分配和已证加法群直接推导，全符号差式随后才使用。没有借尚未构造的分割倒数、实数域、连续性或通用分割计算算法；有理实例仅核对已证相容规律。
