## 基础单元 B2.26 非负乘积的结合、分配与严格比较 {#cutprod-laws-unit}

**学习目标与位置。** 前一单元已经定义非负分割的乘积，并证明闭合、乘零、正性、交换、单位及有理相容。本单元继续证明结合律和两侧分配律，再用已经建立的加法差证明正因子严格保持次序，最后说明比较能够反推，乘积相等能够消去正因子。主归属第526章97F50的实数基础教学部分；06A05交叉。本单元只处理非负分割，不提前定义负分割参与的乘法。

**精确先修。** 使用[正分割及正内外见证NP1](#cutprod-positive-witnesses)、[非负乘积定义、闭合与零积NP2](#cutprod-definition)、[交换、单位及弱单调NP3](#cutprod-basic-laws)、[非负有理相容NP4](#cutprod-rational)。加法部分使用[精确和成员定义](#cutadd-definition)、[分割加法交换结合及单位](#cutgroup-laws)、[加法逆元](#cutgroup-inverses)、[双向次序平移](#cutgroup-translation)、[减法及差的次序判据](#cutgroup-negation-subtraction)。有理见证使用[乘法结合](#rmul-laws)、[分配律](#rmul-distributive)、[非零除法](#rdiv-division)、[有理平移](#rord-translation)、[正因子比较](#rord-multiplication)、[正除数比较](#rord-division)及[中点](#qgap-density-archimedean)。函数结论使用[函数定义](#fun-definition)、[单射](#bij-injective)与[满射](#bij-surjective)。

**对象与记号。** 沿用非负分割集合 $\mathbb R_+=\{A\in\mathbb R:0_{\mathbb R}\le_{\mathbb R}A\}$，其中 $0_{\mathbb R}=i(0)$。对 $A,B\in\mathbb R_+$，

$$
P(A,B)=\{q\in\mathbb Q:q<0\text{，或存在 }a\in A,b\in B
\text{ 满足 }a>0,b>0,q<ab\}.
$$

$P$ 已是函数 $\mathbb R_+\times\mathbb R_+\to\mathbb R_+$。大写字母表示分割，小写字母表示有理数；$ab$ 是既有有理乘积，$P(A,B)$ 是新分割对象。本单元不把两者用同一个乘号混写。还要区分“分割非负”与“它的成员非负”：每个非负分割都包含全部负有理数。

### 1. 为两层见证准备正的上界 {#cutprod-cofinal-witnesses}

结合与分配要反复展开成员定义。和分割中的一个成员虽然可以写成 $b+c$，两个见证却可能为负；乘积中的负成员也可能直接来自定义的负支。先说明怎样在正输入内找到可用的正见证。

**命题 NL1。**

1. 若 $B,C\in\mathbb R_+$，则 $B\oplus C\in\mathbb R_+$。若其中至少一个严格大于 $0_{\mathbb R}$，则和也严格大于 $0_{\mathbb R}$。
2. 若 $B,C>_{\mathbb R}0_{\mathbb R}$ 且 $w\in B\oplus C$，则存在正有理数 $b\in B,c\in C$，使 $w<b+c$。
3. 若 $A,B>_{\mathbb R}0_{\mathbb R}$ 且 $q\in P(A,B)$，则存在正有理数 $a\in A,b\in B$，使 $q<ab$，包括 $q<0$ 的情形。

第二、三条只给指定成员的正见证上界，并非宣称在一个分割内找到了其全部成员的上界。

**非负和及正和。** 从 $0_{\mathbb R}\le_{\mathbb R}B$ 两边同加 $C$，由DG3得到

$$
C=0_{\mathbb R}\oplus C\le_{\mathbb R}B\oplus C.
$$

再用 $0_{\mathbb R}\le_{\mathbb R}C$ 及传递性，和非负。若 $C>_{\mathbb R}0_{\mathbb R}$，上述不严格比较已经使和严格为正。若 $B>_{\mathbb R}0_{\mathbb R}$，则从 $0_{\mathbb R}\le_{\mathbb R}C$ 同加 $B$ 得 $B\le_{\mathbb R}B\oplus C$，同样得到正和。加法闭合保证这些和本来都是分割。

**上调和的两个见证。** 按精确和定义，取 $b_0\in B,c_0\in C$，使 $w=b_0+c_0$。因为 $B,C$ 都正，NP1保证分别存在正内点 $b\in B,c\in C$，满足

$$
b_0<b,\qquad c_0<c.
$$

先对第一式同加 $c_0$，再对第二式同加 $b$，得到

$$
w=b_0+c_0<b+c_0<b+c.
$$

【依据：上调的结论只要求原点属于相应正分割，不要求 $b_0,c_0$ 自己为正；比较使用有理平移。】

**补出乘积成员的正见证。** 若 $q\ge0$，定义中的 $q<0$ 分支不成立，所以成员条件直接给正 $a\in A,b\in B$ 且 $q<ab$。若 $q<0$，由NP1分别取任意正内点 $a\in A,b\in B$。有理正乘积给 $ab>0$，于是 $q<0<ab$。两种情形覆盖所有有理成员，第三条成立。

这里需要输入严格为正。例如 $P(0_{\mathbb R},B)=0_{\mathbb R}$ 虽有负成员，第一因子却没有正内点，不能为它们补出这种正见证。

### 2. 结合律要展开两层成员 {#cutprod-associative}

**命题 NL2。** 对任意 $A,B,C\in\mathbb R_+$，

$$
P(P(A,B),C)=P(A,P(B,C)).
$$

两个内部乘积仍非负，故两种外层 $P$ 都有定义。以下先检查零边界，再对正输入逐层展开；不能在证明之前就把 $P$ 当作可任意改括号的普通乘法。

**有零输入。** 若 $A=0_{\mathbb R}$，左侧为 $P(0_{\mathbb R},C)=0_{\mathbb R}$，右侧也因第一因子为零而等于零。若 $B=0_{\mathbb R}$，左侧内积 $P(A,0_{\mathbb R})$ 为零，右侧内积 $P(0_{\mathbb R},C)$ 为零，所以两侧均零。若 $C=0_{\mathbb R}$，左侧直接乘零，右侧先有 $P(B,0_{\mathbb R})=0_{\mathbb R}$，再乘零，两侧仍零。这些判断只用NP2。

以下设三个输入均严格为正。NP2说明两个内部乘积也正。任意 $q<0$ 都在两种外层乘积的负支中。只须对 $q\ge0$ 比较成员条件。

我们将证明：两种括号的成员条件都等价于

$$
\text{存在正 }a\in A,b\in B,c\in C
\text{，使 }q<(ab)c.
$$

**左括号推出三个见证。** 若 $q\in P(P(A,B),C)$，因为 $q\ge0$，有正有理数 $u\in P(A,B),c\in C$，满足 $q<uc$。$u>0$ 又排除内层的负支，所以存在正 $a\in A,b\in B$，满足 $u<ab$。乘正数 $c$，得到

$$
q<uc<(ab)c.
$$

外层、内层的成员要求都已展开。

**三个见证补成左括号成员。** 反过来，假设正 $a,b,c$ 满足 $q<(ab)c$。因为 $c>0$，可以除以 $c$，得到 $q/c<ab$。取有理中点

$$
u=\frac{q/c+ab}{2}.
$$

$q\ge0$、$c>0$ 给 $q/c\ge0$，而 $ab>0$。中点关系于是给

$$
0\le q/c<u<ab.
$$

所以 $u>0$，正见证 $a,b$ 说明 $u\in P(A,B)$。再将 $q/c<u$ 乘正数 $c$，得到 $q<uc$。因此 $u,c$ 是外层要求的正见证，$q\in P(P(A,B),C)$。

【依据：$c$ 和二都已核正，所有除法合法；$u<ab$ 与 $q<uc$ 是两个不同层次的严格条件，不能只核其中一个。】

**右括号推出三个见证。** 若 $q\in P(A,P(B,C))$，则有正 $a\in A,v\in P(B,C)$，满足 $q<av$。再由 $v>0$ 展开内层，取正 $b\in B,c\in C$，使 $v<bc$。乘正数 $a$，并使用有理结合律，得到

$$
q<av<a(bc)=(ab)c.
$$

**三个见证补成右括号成员。** 仍从正 $a,b,c$ 及 $q<(ab)c=a(bc)$ 出发。因为 $a>0$，有 $q/a<bc$。令

$$
v=\frac{q/a+bc}{2}.
$$

中点给 $0\le q/a<v<bc$。所以 $v>0$，由正见证 $b,c$ 得 $v\in P(B,C)$；把 $q/a<v$ 乘正数 $a$，得 $q<av$。于是 $a,v$ 见证 $q\in P(A,P(B,C))$。

对 $q\ge0$，四个方向已经给出同一个三见证条件；对 $q<0$，两边都含该成员。因而两边具有相同的有理成员，外延相等给NL2。这里用来连接三因子式的始终是有理数结合律，新乘法的结合律是最后得到的结论。

### 3. 分配律必须处理可能为负的成员 {#cutprod-distributive}

**命题 NL3。** 对任意 $A,B,C\in\mathbb R_+$，

$$
P(A,B\oplus C)=P(A,B)\oplus P(A,C),
$$

以及

$$
P(A\oplus B,C)=P(A,C)\oplus P(B,C).
$$

NL1保证和输入非负；NP2保证各乘积非负，因此全部表达式有定义。先证第一式。

**全部零边界。** 若 $A=0_{\mathbb R}$，左侧为零，右侧为 $0_{\mathbb R}\oplus0_{\mathbb R}=0_{\mathbb R}$。若 $B=0_{\mathbb R}$，左侧为 $P(A,C)$，右侧为 $0_{\mathbb R}\oplus P(A,C)=P(A,C)$。若 $C=0_{\mathbb R}$，左侧为 $P(A,B)$，右侧为 $P(A,B)\oplus0_{\mathbb R}=P(A,B)$。这些等式也覆盖多项同时为零。以下只剩 $A,B,C$ 全正的情形。

**正向包含的负成员。** 任取 $q\in P(A,B\oplus C)$。若 $q<0$，则 $q/2<0$，所以它分别属于 $P(A,B)$ 与 $P(A,C)$ 的负支。又有

$$
q=\frac q2+\frac q2.
$$

因此这两个负成员是精确和见证，$q\in P(A,B)\oplus P(A,C)$。

**正向包含的非负成员。** 若 $q\ge0$，乘积定义给正 $a\in A,w\in B\oplus C$，满足 $q<aw$。NL1给正 $b\in B,c\in C$，满足 $w<b+c$。乘正数 $a$，再用有理分配律，得到

$$
q<aw<a(b+c)=ab+ac.
$$

要进入右侧的精确和定义，不能只停在“小于两个乘积的和”。我们具体分出两个成员。令

$$
h=\frac{ab+ac-q}{2}>0,\qquad x=ab-h,\qquad y=ac-h.
$$

分子严格为正，分母二正，所以 $h>0$。于是 $x<ab$，正内点 $a,b$ 见证 $x\in P(A,B)$；同理 $y<ac$，正内点 $a,c$ 见证 $y\in P(A,C)$。有理加法计算给

$$
\begin{aligned}
x+y&=(ab-h)+(ac-h)\\
&=ab+ac-2h\\
&=ab+ac-(ab+ac-q)=q.
\end{aligned}
$$

【依据：有理加法交换结合、相反数合并及合法乘回 $2h=ab+ac-q$。$x,y$ 不必非负；乘积定义允许任何严格低于正乘积见证的有理成员。】

所以 $x,y$ 给出所需精确和，正向包含完成。

**反向包含：先统一第一因子的见证。** 任取

$$
q\in P(A,B)\oplus P(A,C).
$$

精确和定义给 $x\in P(A,B),y\in P(A,C)$，满足 $q=x+y$。即使 $q\ge0$，也不能断言这两个成员都非负。对任意符号的 $x,y$，NL1分别给正有理见证

$$
a_1\in A,\quad b\in B,\quad x<a_1b,
$$

$$
a_2\in A,\quad c\in C,\quad y<a_2c.
$$

两个第一因子可能不同。按有理全序，在 $a_1,a_2$ 中取较大者，记作 $a=\max(a_1,a_2)$。它是两者之一，所以 $a\in A$ 且 $a>0$；并有 $a_1\le a$、$a_2\le a$。分别乘正数 $b,c$，得到

$$
a_1b\le ab,\qquad a_2c\le ac.
$$

因此 $x<ab$、$y<ac$。两次有理平移与分配律给

$$
q=x+y<ab+y<ab+ac=a(b+c).
$$

令 $w=b+c$。由 $b\in B,c\in C$ 和精确和定义，$w\in B\oplus C$；又因 $b,c>0$，有 $w>0$。于是正 $a\in A,w\in B\oplus C$ 见证 $q\in P(A,B\oplus C)$，反向包含完成。这里没有要求 $q$、$x$、$y$ 为正。

两个包含及外延性得到第一式。

**另一侧分配。** 用已证的NP3交换律，先交换整个乘积的两个输入，再用刚证明的第一式，最后分别交换两个结果项的输入：

$$
\begin{aligned}
P(A\oplus B,C)
&=P(C,A\oplus B)\\
&=P(C,A)\oplus P(C,B)\\
&=P(A,C)\oplus P(B,C).
\end{aligned}
$$

每次调用的输入均非负，故交换律与分配律都在各自定义域内。NL3证毕。

### 4. 先有分配，再证明正因子严格保持次序 {#cutprod-strict-order}

**命题 NL4。** 设 $A,B\in\mathbb R_+$、$C>_{\mathbb R}0_{\mathbb R}$，则

$$
A\le_{\mathbb R}B
\quad\Longleftrightarrow\quad
P(A,C)\le_{\mathbb R}P(B,C),
$$

$$
A<_{\mathbb R}B
\quad\Longleftrightarrow\quad
P(A,C)<_{\mathbb R}P(B,C),
$$

并且 $P(A,C)=P(B,C)$ 当且仅当 $A=B$。由交换律，固定正因子放在左侧也有相同结论。

**从正差取得严格保持。** 先设 $A<_{\mathbb R}B$，定义分割差

$$
D=B\ominus A=B\oplus N(A).
$$

DG4的差判据给 $D>_{\mathbb R}0_{\mathbb R}$。这里使用的是已经建立的分割加法及相反数，尚未对负分割做任何乘法。群律还给

$$
\begin{aligned}
A\oplus D
&=A\oplus(B\oplus N(A))\\
&=A\oplus(N(A)\oplus B)\\
&=(A\oplus N(A))\oplus B\\
&=0_{\mathbb R}\oplus B=B.
\end{aligned}
$$

【依据：先代入差的定义，再交换内部加项、改变括号，最后用已证加法逆元和单位。】

现在 $A,D,C$ 全部非负，且 $D,C$ 严格为正，可以使用**刚证明**的NL3和NP2：

$$
P(B,C)=P(A\oplus D,C)=P(A,C)\oplus P(D,C),
\qquad P(D,C)>_{\mathbb R}0_{\mathbb R}.
$$

对 $0_{\mathbb R}<_{\mathbb R}P(D,C)$ 两边同加 $P(A,C)$，由DG3严格平移及加法单位得到

$$
P(A,C)<_{\mathbb R}P(A,C)\oplus P(D,C)=P(B,C).
$$

这证明严格保持。关键并非把NP3的弱不等号直接换成严格号，而是用分配律把两个乘积之间的差写成一个已知严格为正的乘积。

**不严格比较的反射。** 正向 $A\le_{\mathbb R}B$ 推出两乘积不严格比较，已由NP3弱单调给出。反向，假设 $P(A,C)\le_{\mathbb R}P(B,C)$。若 $A\le_{\mathbb R}B$ 不成立，包含全序给 $B<_{\mathbb R}A$。把刚证的严格保持用于这对交换的输入，会得到

$$
P(B,C)<_{\mathbb R}P(A,C),
$$

与假设矛盾。因此 $A\le_{\mathbb R}B$，不严格比较确能反推。

**严格反射与相等消去。** 若 $P(A,C)<_{\mathbb R}P(B,C)$，先由不严格反射得 $A\le_{\mathbb R}B$；若 $A=B$，相等输入的函数值相等，与严格比较冲突。所以 $A<_{\mathbb R}B$，严格双向成立。

若 $P(A,C)=P(B,C)$，相等给两个方向的不严格比较，各自反射回 $A\le_{\mathbb R}B$ 和 $B\le_{\mathbb R}A$；反对称性给 $A=B$。反向由相等输入即得相等输出。NL4证毕。

**一个有理嵌入的例子。** 取 $A=i(1/3)$、$B=i(2/3)$、$C=i(3/5)$。有理保序嵌入给 $0_{\mathbb R}<_{\mathbb R}A<_{\mathbb R}B$，且 $C$ 正。NP4把两乘积化为 $i(1/5)$ 和 $i(2/5)$，它们严格比较，与NL4一致。这个例子核对相容性，一般结论仍来自上面的差与分配证明。

**为什么不能把正因子放宽为非负因子。** 取 $A=0_{\mathbb R}$、$B=1_{\mathbb R}$、$C=0_{\mathbb R}$。虽然 $A<_{\mathbb R}B$，两乘积均为零，所以严格保持和相等消去都失败。若取 $A=1_{\mathbb R}$、$B=0_{\mathbb R}$、$C=0_{\mathbb R}$，乘后满足不严格比较，原输入却不满足 $A\le_{\mathbb R}B$，所以不严格反射也失败。

固定正 $C$ 的规则 $A\mapsto P(A,C)$ 是 $\mathbb R_+\to\mathbb R_+$ 的单射，因为相等输出迫使相等输入。本单元没有为任意目标分割构造原输入，因而这里没有证明满射、乘法逆函数或分割倒数。

### 5. 已经建立的规律与下一步 {#cutprod-laws-boundary}

非负分割的乘法现已具备结合、交换、单位、零、两侧分配及正因子的双向次序比较。分配律的证明没有假设乘积成员都非负；严格单调的证明也没有借用尚未定义的全符号乘法。下一阶段还须对负分割定义乘法，并独立验证符号规则和异号加法中的分配律。当前不能仅把正负号写上去，就宣布全部实数已满足域的运算规则。

### 6. 课后题 {#cutprodlaw-exercises}

#### 题1：把成员上调为正见证 {#cutprodlaw-q01}

证明非负分割之和非负，且其中一项正时和正。若 $B,C$ 正且 $w\in B\oplus C$，构造正 $b\in B,c\in C$ 使 $w<b+c$。再对正 $A,B$ 证明：每个 $q\in P(A,B)$ 都有正内点见证使 $q<ab$，包括负 $q$；解释输入为零时为何不能照用最后的结论。[完整解答](#cutprodlaw-a01)

#### 题2：结合律的零边界与负成员 {#cutprodlaw-q02}

分别处理 $A=0_{\mathbb R}$、$B=0_{\mathbb R}$、$C=0_{\mathbb R}$，证明结合律两侧均为零。若三输入都正，说明两个嵌套乘积为什么有定义，以及每个负有理数为什么同时属于两侧。[完整解答](#cutprodlaw-a02)

#### 题3：两个括号的四个方向 {#cutprodlaw-q03}

对正 $A,B,C$ 及有理 $q\ge0$，完整证明两种括号成员都等价于存在正 $a\in A,b\in B,c\in C$ 使 $q<(ab)c$。必须分别检查 $u=(q/c+ab)/2$ 与 $v=(q/a+bc)/2$ 的正性、内部成员和外层严格比较。与题2合并得到一般非负结合律。[完整解答](#cutprodlaw-a03)

#### 题4：分配律正向如何得到精确和 {#cutprodlaw-q04}

设 $A,B,C$ 都正，证明 $P(A,B\oplus C)\subseteq P(A,B)\oplus P(A,C)$。分别处理 $q<0$ 与 $q\ge0$；非负情形须上调和的见证，再实际给出 $h,x,y$，核对它们的成员资格和 $x+y=q$，说明是否要求 $x,y\ge0$。[完整解答](#cutprodlaw-a04)

#### 题5：分配律反向的共同第一因子 {#cutprodlaw-q05}

设 $A,B,C$ 都正，从任意精确和成员 $q=x+y$ 出发证明反向包含。不得先假定 $x,y$ 非负；说明为何可补正见证，以及 $a=\max(a_1,a_2)$ 为何仍属于 $A$，逐步完成 $q<a(b+c)$。[完整解答](#cutprodlaw-a05)

#### 题6：补齐分配律的零边界与另一侧 {#cutprodlaw-q06}

逐项处理分配律中 $A=0_{\mathbb R}$、$B=0_{\mathbb R}$、$C=0_{\mathbb R}$，并结合题4、5得到全部非负输入的结论。再用交换律逐行证明 $P(A\oplus B,C)=P(A,C)\oplus P(B,C)$，核查出现的和输入都非负。[完整解答](#cutprodlaw-a06)

#### 题7：由正差证明严格单调 {#cutprodlaw-q07}

给定 $0_{\mathbb R}\le_{\mathbb R}A<_{\mathbb R}B$ 和 $C>_{\mathbb R}0_{\mathbb R}$，取 $D=B\ominus A$。证明 $D>_{\mathbb R}0_{\mathbb R}$、$A\oplus D=B$，再逐步推出 $P(A,C)<_{\mathbb R}P(B,C)$。标出分配、正积、严格加法平移的使用位置，解释为什么不能在证明分配之前借用这条路线。[完整解答](#cutprodlaw-a07)

#### 题8：比较反射、消去与尚未证明的满射 {#cutprodlaw-q08}

固定正分割 $C$，对非负 $A,B$ 证明不严格比较、严格比较及相等的三个双向结论。给出零因子下严格保持、反射和消去失败的反例。说明 $A\mapsto P(A,C)$ 的定义域、目标、单射依据，以及本单元是否已证明它满射或已构造 $C$ 的倒数。[完整解答](#cutprodlaw-a08)

**来源与范围说明。** 定义版本与证明义务的对照见[分割乘法来源审计](#dedekind-multiplication-sources)。本单元从有理成员见证及已证加法群规律独立推导非负乘法规律，不借未建立的实数域、连续性、实数倒数或一般分割成员算法。有限主下段实例不替代全称证明。
