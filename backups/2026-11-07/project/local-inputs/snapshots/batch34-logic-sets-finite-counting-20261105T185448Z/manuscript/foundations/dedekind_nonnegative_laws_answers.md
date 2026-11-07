## 基础单元 B2.26 课后题完整解答 {#cutprodlaw-answers}

以下解答对应[非负乘积的结合、分配与严格比较](#cutprod-laws-unit)。$A,B,C$ 表示分割，$0_{\mathbb R}=i(0)$，$P$ 的输入必须非负。其成员条件为：有理 $q<0$，或者存在正有理内点 $a,b$ 使 $q<ab$。$\oplus,N,\ominus$ 均为已证加法群中的运算。下面的小写乘除仍是有理数运算。

### 题1：把成员上调为正见证 {#cutprodlaw-a01}

[返回题目](#cutprodlaw-q01)

设 $0_{\mathbb R}\le_{\mathbb R}B$ 且 $0_{\mathbb R}\le_{\mathbb R}C$。由第一个比较同加 $C$，得

$$
0_{\mathbb R}\oplus C\le_{\mathbb R}B\oplus C.
$$

左侧等于 $C$，所以 $0_{\mathbb R}\le_{\mathbb R}C\le_{\mathbb R}B\oplus C$，和非负。若 $C$ 正，则 $0_{\mathbb R}<_{\mathbb R}C\le_{\mathbb R}B\oplus C$，和正。若 $B$ 正，改从 $0_{\mathbb R}\le_{\mathbb R}C$ 同加 $B$，得到 $B\le_{\mathbb R}B\oplus C$；再用 $0_{\mathbb R}<_{\mathbb R}B$，也得正和。这里每个平移都用已证DG3。

现在假设 $B,C$ 都正，并取 $w\in B\oplus C$。精确和定义给 $b_0\in B,c_0\in C$，使 $w=b_0+c_0$。不假定 $b_0,c_0$ 的符号。由NP1取正内点 $s\in B$。在 $b_0,s$ 中选择较大者 $m$；$m$ 是二者之一，所以 $m\in B$。无最大元给 $b\in B$ 且 $m<b$，故 $b>b_0$ 并且 $b>s>0$。

对 $C$ 另取正内点 $t$，在 $c_0,t$ 中取较大者 $n\in C$，再由无最大元取 $c\in C$ 且 $n<c$。因此 $c>c_0$ 且 $c>t>0$。有理平移比较给

$$
w=b_0+c_0<b+c_0<b+c.
$$

于是所需正见证 $b,c$ 已构造。这里所取“较大者”仅从两个已给数中选一个，不是寻找分割的最大元。

最后设 $A,B$ 正，$q\in P(A,B)$。若 $q\ge0$，定义中的负支被排除，必有正 $a\in A,b\in B$ 使 $q<ab$。若 $q<0$，NP1保证各自至少有一个正内点；任取这样的 $a,b$，有理正乘积给 $ab>0$，故 $q<0<ab$。这证明包括负成员在内的全称结论。

若 $A=0_{\mathbb R}$，乘积虽仍含全部负有理数，$A$ 却没有正内点。例如 $-1\in P(0_{\mathbb R},1_{\mathbb R})$，但不存在正 $a\in0_{\mathbb R}$。所以最后一条的正输入条件不可删去。

### 题2：结合律的零边界与负成员 {#cutprodlaw-a02}

[返回题目](#cutprodlaw-q02)

所有输入先假定非负，NP2保证内部乘积也非负，外层运算始终有定义。

若 $A=0_{\mathbb R}$，

$$
P(P(A,B),C)=P(0_{\mathbb R},C)=0_{\mathbb R},
$$

$$
P(A,P(B,C))=P(0_{\mathbb R},P(B,C))=0_{\mathbb R}.
$$

若 $B=0_{\mathbb R}$，

$$
P(P(A,B),C)=P(P(A,0_{\mathbb R}),C)
=P(0_{\mathbb R},C)=0_{\mathbb R},
$$

$$
P(A,P(B,C))=P(A,P(0_{\mathbb R},C))
=P(A,0_{\mathbb R})=0_{\mathbb R}.
$$

若 $C=0_{\mathbb R}$，

$$
P(P(A,B),C)=P(P(A,B),0_{\mathbb R})=0_{\mathbb R},
$$

$$
P(A,P(B,C))=P(A,P(B,0_{\mathbb R}))
=P(A,0_{\mathbb R})=0_{\mathbb R}.
$$

这些等式全部使用已有乘零律，没有使用待证结合律；两项或三项为零也被覆盖。

若 $A,B,C$ 均正，NP2进一步给 $P(A,B)$ 与 $P(B,C)$ 正。对任何有理 $q<0$，无论外层是否另有正乘积见证，定义的负支已经直接给

$$
q\in P(P(A,B),C),\qquad q\in P(A,P(B,C)).
$$

因此负成员的比较已经完成，剩下的工作只有 $q\ge0$ 时两侧是否具有相同成员。这部分在题3完成。

### 题3：两个括号的四个方向 {#cutprodlaw-a03}

[返回题目](#cutprodlaw-q03)

设 $A,B,C$ 严格为正，固定有理数 $q\ge0$。记条件 $H(q)$ 为：存在正有理数 $a\in A,b\in B,c\in C$ 使 $q<(ab)c$。以下分别证明两个成员条件与 $H(q)$ 的双向等价。

**左括号的正向。** 若 $q\in P(P(A,B),C)$，因 $q\ge0$，有正 $u\in P(A,B),c\in C$ 满足 $q<uc$。又因 $u>0$，内层成员也必须来自正见证支，故有正 $a\in A,b\in B$ 使 $u<ab$。两边乘正 $c$，得 $uc<(ab)c$。与 $q<uc$ 合并，得到 $q<(ab)c$，即 $H(q)$。

**左括号的反向。** 设 $H(q)$ 成立，固定它给出的正 $a,b,c$。$c>0$，所以 $q/c$ 有定义，且

$$
0\le q/c<ab.
$$

取 $u=(q/c+ab)/2$。有理中点结论给

$$
q/c<u<ab.
$$

左端非负，所以 $u>0$。由于正 $a\in A,b\in B$ 且 $u<ab$，乘积成员定义给 $u\in P(A,B)$。再把 $q/c<u$ 乘正 $c$，合法乘回得 $q<uc$。因此正 $u\in P(A,B),c\in C$ 是外层见证，$q\in P(P(A,B),C)$。

**右括号的正向。** 若 $q\in P(A,P(B,C))$，展开外层可取正 $a\in A,v\in P(B,C)$，使 $q<av$。展开正的 $v$，可取正 $b\in B,c\in C$，使 $v<bc$。乘正 $a$，并用已有有理结合律，

$$
q<av<a(bc)=(ab)c.
$$

于是又得到 $H(q)$。此处没有把两个 $P$ 改括号，只改了三个有理数的括号。

**右括号的反向。** 若 $H(q)$ 成立，有理结合律给 $q<a(bc)$。$a>0$ 保证商有定义，除以正数后得到

$$
0\le q/a<bc.
$$

令 $v=(q/a+bc)/2$。由中点结论，$q/a<v<bc$，所以 $v>0$。正内点 $b,c$ 与 $v<bc$ 说明 $v\in P(B,C)$；把 $q/a<v$ 乘正 $a$ 得 $q<av$。因此 $a,v$ 见证 $q\in P(A,P(B,C))$。

四个方向证明两个成员条件都等价于 $H(q)$。两个中点构造分别检查了除数正、输出正、内部成员和外层严格比较，不能用“有个中间数”省掉这些检查。

题2已处理零输入和负 $q$。本题处理其余正输入和非负 $q$，所以对任何非负 $A,B,C$，两种括号具有完全相同的有理成员。由集合外延性，

$$
P(P(A,B),C)=P(A,P(B,C)).
$$

### 题4：分配律正向如何得到精确和 {#cutprodlaw-a04}

[返回题目](#cutprodlaw-q04)

设 $A,B,C$ 都正。由题1，$B\oplus C$ 正，特别非负，所以 $P(A,B\oplus C)$ 有定义。任取其成员 $q$。

若 $q<0$，二正使 $q/2<0$。于是

$$
x=q/2\in P(A,B),\qquad y=q/2\in P(A,C).
$$

两项都来自各自乘积的负支。有理运算给 $x+y=q$，这正是精确和的成员见证，所以 $q\in P(A,B)\oplus P(A,C)$。

若 $q\ge0$，负支不成立，故有正 $a\in A,w\in B\oplus C$ 满足 $q<aw$。题1给正 $b\in B,c\in C$ 且 $w<b+c$。因为 $a>0$，

$$
q<aw<a(b+c)=ab+ac.
$$

最后一个等号使用有理分配律。令

$$
h=\frac{ab+ac-q}{2},\qquad x=ab-h,\qquad y=ac-h.
$$

$ab+ac-q>0$ 且二正，所以 $h>0$，全部表达式有定义。于是 $x<ab$，正内点 $a,b$ 使 $x\in P(A,B)$；$y<ac$，正内点 $a,c$ 使 $y\in P(A,C)$。同时

$$
\begin{aligned}
x+y
&=(ab-h)+(ac-h)\\
&=ab+ac-(h+h)\\
&=ab+ac-2h\\
&=ab+ac-(ab+ac-q)=q.
\end{aligned}
$$

【依据：有理加法重组、$h+h=2h$ 以及定义中合法的乘回。】

因此 $x,y$ 构成精确和成员，仍得 $q\in P(A,B)\oplus P(A,C)$。两个符号分支覆盖任意 $q$，正向包含成立。

没有要求 $x,y\ge0$。乘积定义要求的是见证 $a,b,c$ 严格为正，而不是要求被见证的成员 $x,y$ 非负。若某个分出的成员为负，它既可由负支进入，也确实满足已经写出的正乘积上界。把成员与见证的符号条件混同，会凭空删掉合法分解。

### 题5：分配律反向的共同第一因子 {#cutprodlaw-a05}

[返回题目](#cutprodlaw-q05)

设 $A,B,C$ 正，任取 $q\in P(A,B)\oplus P(A,C)$。按精确和定义，有

$$
x\in P(A,B),\qquad y\in P(A,C),\qquad q=x+y.
$$

$x,y$ 可以有任意符号。题1对正输入的乘积成员给出正见证 $a_1\in A,b\in B$，使 $x<a_1b$；另给正见证 $a_2\in A,c\in C$，使 $y<a_2c$。若 $x$ 或 $y$ 为负，该题的补见证分支仍然适用，所以没有遗漏这种情形。

由有理全序，要么 $a_1\le a_2$，此时取 $a=a_2$；要么 $a_2<a_1$，此时取 $a=a_1$。两种情形都给

$$
a\in A,\qquad a>0,\qquad a_1\le a,\qquad a_2\le a.
$$

这就是 $a=\max(a_1,a_2)$ 的含义。它是两个既有内部成员之一，故不需要假设分割含上端点。

因为 $b,c>0$，分别乘以相应正数得到 $a_1b\le ab$、$a_2c\le ac$。混合传递给 $x<ab$、$y<ac$。先把第一比较同加 $y$，再把第二比较同加 $ab$，得到

$$
q=x+y<ab+y<ab+ac=a(b+c).
$$

令 $w=b+c$。正有理数之和为正，故 $w>0$；$b\in B,c\in C$ 及精确等式 $w=b+c$ 给 $w\in B\oplus C$。所以正 $a\in A,w\in B\oplus C$ 和 $q<aw$ 正好满足左侧乘积成员条件，得到

$$
q\in P(A,B\oplus C).
$$

这证明反向包含。关键是统一两个第一因子，再形成同一个 $a(b+c)$；若直接把不同的 $a_1b+a_2c$ 写成 $a_1(b+c)$，就会使用一个没有根据的等式。

### 题6：补齐分配律的零边界与另一侧 {#cutprodlaw-a06}

[返回题目](#cutprodlaw-q06)

给定非负 $A,B,C$，题1使 $B\oplus C$ 非负，所以 $P(A,B\oplus C)$ 合法。NP2保证两个右侧乘积均非负，加法也已闭合。

若 $A=0_{\mathbb R}$，乘零律和加法单位给

$$
P(A,B\oplus C)=0_{\mathbb R},
$$

$$
P(A,B)\oplus P(A,C)
=0_{\mathbb R}\oplus0_{\mathbb R}=0_{\mathbb R}.
$$

若 $B=0_{\mathbb R}$，

$$
P(A,B\oplus C)=P(A,0_{\mathbb R}\oplus C)=P(A,C),
$$

$$
P(A,B)\oplus P(A,C)
=0_{\mathbb R}\oplus P(A,C)=P(A,C).
$$

若 $C=0_{\mathbb R}$，

$$
P(A,B\oplus C)=P(A,B\oplus0_{\mathbb R})=P(A,B),
$$

$$
P(A,B)\oplus P(A,C)
=P(A,B)\oplus0_{\mathbb R}=P(A,B).
$$

这些支允许多个输入同时为零，并且都成立。若没有零输入，非负性与全序使三个输入都正，题4和题5提供两个包含方向。因此对全部非负输入，

$$
P(A,B\oplus C)=P(A,B)\oplus P(A,C).
$$

为证明另一侧分配，先由题1核 $A\oplus B\in\mathbb R_+$。于是可以逐行写

$$
\begin{aligned}
P(A\oplus B,C)
&=P(C,A\oplus B)\\
&=P(C,A)\oplus P(C,B)\\
&=P(A,C)\oplus P(B,C).
\end{aligned}
$$

第一行调用NP3交换律；第二行用刚完成的分配，代入第一因子 $C$、和的两项 $A,B$；第三行分别用两次NP3交换。所有因子及和输入非负，因此没有把只在非负域证明的规律越域使用。

### 题7：由正差证明严格单调 {#cutprodlaw-a07}

[返回题目](#cutprodlaw-q07)

设 $0_{\mathbb R}\le_{\mathbb R}A<_{\mathbb R}B$，且 $C>_{\mathbb R}0_{\mathbb R}$。定义

$$
D=B\ominus A=B\oplus N(A).
$$

由DG4的严格差判据，$A<_{\mathbb R}B$ 当且仅当 $0_{\mathbb R}<_{\mathbb R}B\ominus A$。所以 $D$ 正，特别是 $P(D,C)$ 的输入合法。加法群规律给

$$
\begin{aligned}
A\oplus D
&=A\oplus(B\oplus N(A))\\
&=A\oplus(N(A)\oplus B)\\
&=(A\oplus N(A))\oplus B\\
&=0_{\mathbb R}\oplus B\\
&=B.
\end{aligned}
$$

第一步代入差定义；第二步交换内部 $B,N(A)$；第三步结合；第四步逆元；第五步左单位。尽管 $N(A)$ 可能为负，这些都是已经在全部分割上成立的加法运算，没有对它调用 $P$。

将 $B=A\oplus D$ 代入乘积，再用题6得到的另一侧分配，

$$
P(B,C)=P(A\oplus D,C)=P(A,C)\oplus P(D,C).
$$

$D,C$ 严格为正，所以NP2的正积结论给 $0_{\mathbb R}<_{\mathbb R}P(D,C)$。两边同加 $P(A,C)$，DG3严格平移给

$$
P(A,C)\oplus0_{\mathbb R}
<_{\mathbb R}P(A,C)\oplus P(D,C).
$$

用加法单位及前一个乘积等式化简，便得

$$
P(A,C)<_{\mathbb R}P(B,C).
$$

所用顺序是：加法差为正→非负分配展开→正积→严格加法平移。若在分配律尚未证明时就把 $P(A\oplus D,C)$ 展成两项，上述关键等式没有依据。因此不能先用本题的严格单调去证明它所依赖的分配律。

### 题8：比较反射、消去与尚未证明的满射 {#cutprodlaw-a08}

[返回题目](#cutprodlaw-q08)

固定 $C>_{\mathbb R}0_{\mathbb R}$，设 $A,B\in\mathbb R_+$。

**不严格比较。** 若 $A\le_{\mathbb R}B$，NP3对共同第二因子 $C$ 给 $P(A,C)\le_{\mathbb R}P(B,C)$。反过来，假设这两个乘积满足不严格比较。若原输入不满足 $A\le_{\mathbb R}B$，全序给 $B<_{\mathbb R}A$。题7对 $B,A,C$ 应用严格保持，得到

$$
P(B,C)<_{\mathbb R}P(A,C).
$$

这与已假定的相反方向不严格比较冲突。因此必须有 $A\le_{\mathbb R}B$。两个方向合起来，

$$
A\le_{\mathbb R}B
\quad\Longleftrightarrow\quad
P(A,C)\le_{\mathbb R}P(B,C).
$$

**严格比较。** 正向已经由题7证明。若反过来有 $P(A,C)<_{\mathbb R}P(B,C)$，它首先给不严格比较，刚证的反射使 $A\le_{\mathbb R}B$。若 $A=B$，由于 $P$ 是函数，同一输入产生相同输出，两个乘积应相等，矛盾。所以 $A\ne B$，结合不严格比较，得 $A<_{\mathbb R}B$。因而

$$
A<_{\mathbb R}B
\quad\Longleftrightarrow\quad
P(A,C)<_{\mathbb R}P(B,C).
$$

**相等。** 若两乘积相等，就分别满足两个方向的不严格比较。各自反射得到 $A\le_{\mathbb R}B$ 与 $B\le_{\mathbb R}A$，反对称性给 $A=B$。若 $A=B$，函数性质直接给两乘积相等。因此

$$
P(A,C)=P(B,C)\quad\Longleftrightarrow\quad A=B.
$$

**零因子的反例。** 嵌入保序给 $0_{\mathbb R}<_{\mathbb R}1_{\mathbb R}$。取 $C=0_{\mathbb R}$ 时，

$$
P(0_{\mathbb R},C)=0_{\mathbb R}=P(1_{\mathbb R},C).
$$

所以原来的严格比较不保持；相等输出也不能消去共同因子得出 $0_{\mathbb R}=1_{\mathbb R}$。若改取原输入顺序 $A=1_{\mathbb R},B=0_{\mathbb R}$，乘积仍相等，因而满足 $P(A,C)\le_{\mathbb R}P(B,C)$，但 $A\le_{\mathbb R}B$ 为假。这另证不严格反射也失败。

**函数结论的边界。** 对固定正 $C$ 定义

$$
F_C:\mathbb R_+\longrightarrow\mathbb R_+,
\qquad F_C(A)=P(A,C).
$$

NP2给非负闭合，故域与目标合法。刚证相等消去说明 $F_C(A)=F_C(B)$ 必有 $A=B$，这就是单射。满射还要求对每个目标 $Y\in\mathbb R_+$ 找到输入 $A$ 使 $P(A,C)=Y$；本单元没有给出这种全称存在构造。尤其没有为目标 $1_{\mathbb R}$ 构造所需输入，不能据单射宣布已经得到 $C$ 的乘法逆元或逆函数。相等反射是唯一性信息，不能替代存在性证明。
