## 基础单元 B2.24 课后题完整解答 {#cutgroup-answers}

以下解答对应[分割加法的群律与次序平移](#cutgroup-unit)。$A,B,C,X$ 表示分割，$\oplus$ 和 $N$ 是已经证明闭合的分割运算；小写见证仍属于 $\mathbb Q$。零分割 $0_{\mathbb R}=i(0)$ 的成员恰为负有理数。前几题建立一般加法规则，后几题才使用它们消去、反射次序或解方程。

### 题1：先展开见证，再改有理括号 {#cutgroup-a01}

[返回题目](#cutgroup-q01)

若 $q\in A\oplus B$，由定义取 $a\in A,b\in B$ 使 $q=a+b$。有理加法交换律给 $q=b+a$，所以 $b,a$ 见证 $q\in B\oplus A$。反过来，若 $q\in B\oplus A$，取 $b\in B,a\in A$ 使 $q=b+a$；交换有理加项得到 $q=a+b$，故 $q\in A\oplus B$。两个包含方向给 $A\oplus B=B\oplus A$。

结合律必须多展开一层。先设 $q\in(A\oplus B)\oplus C$，外层定义给 $u\in A\oplus B,c\in C$，满足 $q=u+c$。内层定义又给 $a\in A,b\in B$，满足 $u=a+b$。于是

$$
q=(a+b)+c=a+(b+c).
$$

三个小写量都是有理数，所以这一步使用既有有理结合律。令 $v=b+c$，由于 $b\in B,c\in C$，有 $v\in B\oplus C$；又因为 $a\in A$ 且 $q=a+v$，得到 $q\in A\oplus(B\oplus C)$。

反向设 $q\in A\oplus(B\oplus C)$。先取 $a\in A,v\in B\oplus C$ 使 $q=a+v$，再取 $b\in B,c\in C$ 使 $v=b+c$。有理结合律给

$$
q=a+(b+c)=(a+b)+c.
$$

令 $u=a+b$，则 $u\in A\oplus B$。由 $c\in C$ 和 $q=u+c$，得到 $q\in(A\oplus B)\oplus C$。两个方向通过外延相等合成

$$
(A\oplus B)\oplus C=A\oplus(B\oplus C).
$$

本题重组的是有理见证 a、b、c，并逐项核新的中间和属于哪一个和分割；并未在证明之前假设分割加法可以任意重括号。

### 题2：零单位为什么需要无最大元 {#cutgroup-a02}

[返回题目](#cutgroup-q02)

先设 $q\in A\oplus0_{\mathbb R}$。取 $a\in A,z\in0_{\mathbb R}$ 使 $q=a+z$。由零分割定义 $z<0$；同加有理数 a 得 $q=a+z<a$。A 向下封闭，故 $q\in A$。这给出

$$
A\oplus0_{\mathbb R}\subseteq A.
$$

反向，任取 $q\in A$。A 无最大元，所以存在 $a\in A$ 满足 $q<a$。令 $z=q-a$。有理平移比较给 $z<0$，于是 $z\in0_{\mathbb R}$；有理加减规则给

$$
a+z=a+(q-a)=q.
$$

因此 a、z 是所需的两个成员见证，$q\in A\oplus0_{\mathbb R}$。得到反向包含，故 $A\oplus0_{\mathbb R}=A$。再用题1交换律，

$$
0_{\mathbb R}\oplus A=A\oplus0_{\mathbb R}=A.
$$

不能取 $z=0$ 来证明反向：虽然有理等式 $q=q+0$ 成立，但有理零不满足 $0<0$，所以 $0\notin0_{\mathbb R}$。和分割的定义不仅要求一个等式，还要求两个见证分别属于输入分割。本题通过无最大元找到 a，再用严格负差弥补了这个成员要求。

### 题3：逆元等式的第一个包含 {#cutgroup-a03}

[返回题目](#cutgroup-q03)

给定 $q\in A\oplus N(A)$，先展开和的成员条件，取

$$
a\in A,\qquad c\in N(A),\qquad q=a+c.
$$

再展开负分割成员条件，取有理数 r，满足

$$
r\notin A,\qquad c<-r.
$$

内点 a 与外点 r 满足 $a<r$：若相等，r 直接属于 A；若 $r<a$，A 下闭也给 $r\in A$；两者都矛盾，所以有理三歧性只剩 $a<r$。

由 $c<-r$ 同加 a，得 $a+c<a-r$。由 $a<r$ 同加 $-r$，得 $a-r<0$。合起来

$$
q=a+c<a-r<0.
$$

因此 $q\in0_{\mathbb R}$。对任意 q 都成立，故 $A\oplus N(A)\subseteq0_{\mathbb R}$。此时只有一个包含，还不能宣称逆元等式完成。

例如取 $A=i(2)$，则有理一属于 A，因为 $1<2$；但一不是负数。还可取外点 r=2 与负分割成员 c=−3，因为 $-3<-2$，故 $c\in N(A)$。其和 $1+(-3)=-2<0$。一般证明中需要的是 $a<r$ 与 $c<-r$，并没有要求两个和见证各自都负。

### 题4：严格跨界间距补出另一个包含 {#cutgroup-a04}

[返回题目](#cutgroup-q04)

任取 $x\in0_{\mathbb R}$，即有理数 $x<0$。令 $\varepsilon=-x$，由有理取反反序有 $\varepsilon>0$，所以可以对 A 使用DA1。取得有理数 u、v，满足

$$
u\in A,\qquad v\notin A,\qquad 0<v-u<\varepsilon=-x.
$$

从 $v-u<-x$ 的两边同加 x，得

$$
x+(v-u)<x+(-x)=0.
$$

再在两边同加 $-v$，得到

$$
x+(v-u)-v<-v.
$$

左侧用有理结合交换写为 $x-u+(v-v)=x-u$，因此

$$
x-u<-v.
$$

令 $c=x-u$。外点 $v\notin A$ 和严格比较 $c<-v$ 就是负分割定义要求的见证，所以 $c\in N(A)$。又有 $u+c=u+(x-u)=x$，所以 $u\in A,c\in N(A)$ 共同给出 $x\in A\oplus N(A)$。

这对每个 $x\in0_{\mathbb R}$ 成立，得到 $0_{\mathbb R}\subseteq A\oplus N(A)$。与题3合并，

$$
A\oplus N(A)=0_{\mathbb R}.
$$

题1交换律再给 $N(A)\oplus A=0_{\mathbb R}$，两侧逆元均证明。

若只知道 $v-u\le-x$，同样移项只能得到 $c\le-v$。取到等号时，外点 v 不再满足负分割见证所需的 $c<-v$。这不是仅凭非严格间距就能忽略的边界。例如 $A=i(0)$、$x=-1$，取 $u=-1\in A,v=0\notin A$，确有 $v-u=1=-x$，但 $c=x-u=0$。对这个 A，前单元已证 $N(i(0))=i(0)$，而有理零不属于它。因此这组不带严格余量的见证实际不能完成证明。DA1的严格间距正好排除了该失败情形。

### 题5：逆元唯一以后才能双重取反 {#cutgroup-a05}

[返回题目](#cutgroup-q05)

设分割 B 满足 $A\oplus B=0_{\mathbb R}$。题4已经给出 $N(A)\oplus A=0_{\mathbb R}$，题1、2给出结合与单位。因此

$$
\begin{aligned}
B
 &=0_{\mathbb R}\oplus B\\
 &=(N(A)\oplus A)\oplus B\\
 &=N(A)\oplus(A\oplus B)\\
 &=N(A)\oplus0_{\mathbb R}\\
 &=N(A).
\end{aligned}
$$

第一行用左单位；第二行用已证的左逆元等式；第三行用结合律；第四行代入关于 B 的假设；最后用右单位。于是所有逆元候选都等于 $N(A)$，逆元唯一。这里没有先从两个和相等中消去 A，而是把已证逆元实际加进去再用结合律。

现在把分割 $N(A)$ 作为新的输入。题4保证它的指定逆元 $N(N(A))$ 存在；又因为 $N(A)\oplus A=0_{\mathbb R}$，A 也是它的一个逆元。刚证唯一性迫使

$$
N(N(A))=A.
$$

这并非从集合补集两次还原直接推得，因为 N 的定义还含严格下段；我们使用的是已经证明的加法逆元身份。

对于零分割，单位律给 $0_{\mathbb R}\oplus0_{\mathbb R}=0_{\mathbb R}$，所以零分割自身是一个逆元候选。唯一性得到 $N(0_{\mathbb R})=0_{\mathbb R}$。同一结论也与有理相容 $N(i(0))=i(-0)=i(0)$ 一致。

到这里，所用闭合、结合、交换、单位和逆元都是前面实际证明的性质。将其称为“交换加法群”只是给这一组结论命名，不以名称作为任何一步的理由。

### 题6：平移的保序、反射和逆函数 {#cutgroup-a06}

[返回题目](#cutgroup-q06)

先设 $A\le_{\mathbb R}B$，即 $A\subseteq B$。若 $q\in A\oplus C$，则有 $a\in A,c\in C$ 满足 $q=a+c$。由于 $a\in B$，同一对见证给 $q\in B\oplus C$，所以

$$
A\oplus C\subseteq B\oplus C.
$$

这只是非严格保序，完全来自成员定义。

反向设 $A\oplus C\subseteq B\oplus C$。把刚证方向应用于两个和分割，再同加 $N(C)$，得

$$
(A\oplus C)\oplus N(C)
\subseteq(B\oplus C)\oplus N(C).
$$

左侧用结合、逆元和单位化为

$$
A\oplus(C\oplus N(C))=A\oplus0_{\mathbb R}=A;
$$

右侧同样化为 B。故 $A\subseteq B$，非严格比较的反射已证。

如果 $A\oplus C=B\oplus C$，两方向包含分别反射回 $A\subseteq B$ 和 $B\subseteq A$，由外延相等得 $A=B$。如果 $A=B$，输入相等当然给两和相等。因此相等可以消去同一加项，且两个方向均成立。

若 $A<_{\mathbb R}B$，非严格保序给两和包含；若两和相等，刚证消去给 $A=B$，矛盾。故两和严格比较。反过来，若两和严格比较，非严格反射给 $A\subseteq B$；若 $A=B$，两和又会相等，矛盾。于是 $A<_{\mathbb R}B$。这说明严格保序不是仅由“单调”二字取得，而用了消去和不相等。

固定 C，函数 $T_C:\mathbb R\to\mathbb R$ 定义为 $T_C(A)=A\oplus C$；闭合保证每个输出属于目标。定义 $T_{N(C)}$ 同样合法，且对每个 A，

$$
T_{N(C)}(T_C(A))
=(A\oplus C)\oplus N(C)
=A\oplus0_{\mathbb R}=A,
$$

$$
T_C(T_{N(C)}(A))
=(A\oplus N(C))\oplus C
=A\oplus(N(C)\oplus C)=A.
$$

两函数都是从 R 到 R，复合的定义域和目标匹配。这两个逐点等式说明它们互为双侧逆；由既有双侧逆判据，$T_C$ 双射。也可直接说明：消去给单射，而任意目标 B 的前像可取 $B\oplus N(C)$，代入第二个等式给满射。

### 题7：取反反序与和的相反数 {#cutgroup-a07}

[返回题目](#cutgroup-q07)

设 $A\subseteq B$。任取 $q\in N(B)$，展开成员见证得到有理 r，满足 $r\notin B$ 且 $q<-r$。如果 $r\in A$，包含会给 $r\in B$，矛盾；故 $r\notin A$。于是同一个 r 见证 $q\in N(A)$，证明 $N(B)\subseteq N(A)$。

反向若 $N(B)\subseteq N(A)$，对这两个分割再次应用刚证的取反反序方向，得到

$$
N(N(A))\subseteq N(N(B)).
$$

题5双重取反把它化为 $A\subseteq B$。因此

$$
A\le_{\mathbb R}B
\quad\Longleftrightarrow\quad
N(B)\le_{\mathbb R}N(A).
$$

若 $A<_{\mathbb R}B$，已有 $N(B)\subseteq N(A)$。若两负分割相等，对等式两边施加 N 并用双重取反，得到 $B=A$，矛盾；故包含严格。反过来，若 $N(B)<_{\mathbb R}N(A)$，反射先得 $A\subseteq B$；若 $A=B$，函数值相等会与前面的严格比较冲突。因此 $A<_{\mathbb R}B$。严格取反也是双向反序。

对于和的相反数，先证明候选 $N(A)\oplus N(B)$ 的逆元性质。完整重括号为

$$
\begin{aligned}
&(A\oplus B)\oplus(N(A)\oplus N(B))\\
&=((A\oplus B)\oplus N(A))\oplus N(B)\\
&=(A\oplus(B\oplus N(A)))\oplus N(B)\\
&=(A\oplus(N(A)\oplus B))\oplus N(B)\\
&=((A\oplus N(A))\oplus B)\oplus N(B)\\
&=(0_{\mathbb R}\oplus B)\oplus N(B)\\
&=B\oplus N(B)\\
&=0_{\mathbb R}.
\end{aligned}
$$

第一处变形把最后的括号展开为左结合；第二处只将前三项按结合律重组；第三处交换内部 $B,N(A)$；第四处再重组，使 $A,N(A)$ 相邻成一组；接着依次用 A 的逆元、左单位、B 的逆元。每一步都已在前题证明，没有把四项当成可以无理由任意重排的列表。

因此 $N(A)\oplus N(B)$ 是分割 $A\oplus B$ 的一个加法逆元。题5唯一性才给

$$
N(A\oplus B)=N(A)\oplus N(B).
$$

这证明了常被省记为“和的负号分配”的规则；它的依据是具体重括号和逆元唯一性。

### 题8：减法、方程及差的符号 {#cutgroup-a08}

[返回题目](#cutgroup-q08)

定义 $A\ominus B=A\oplus N(B)$。N 与和都已闭合，因此任意 A、B 都有一个分割输出。减法到这里才在新对象集合上定义，不是把有理成员的减法未经说明搬过来。

先解 $A\oplus X=B$。若 X 是解，则

$$
\begin{aligned}
X
 &=0_{\mathbb R}\oplus X\\
 &=(N(A)\oplus A)\oplus X\\
 &=N(A)\oplus(A\oplus X)\\
 &=N(A)\oplus B.
\end{aligned}
$$

这给出必要的唯一候选。反过来，取 $X=N(A)\oplus B$，闭合保证 X 是分割；代入有

$$
A\oplus X
=A\oplus(N(A)\oplus B)
=(A\oplus N(A))\oplus B
=0_{\mathbb R}\oplus B=B.
$$

候选确为解。必要性强制每个解相等，所以唯一；也可从两个解的等式 $A\oplus X=A\oplus Y$，先交换再用消去得到 X=Y。没有要求 A 非零，整个过程也没有除法。

由前一单元的相容性，

$$
\begin{aligned}
i(r)\ominus i(s)
 &=i(r)\oplus N(i(s))\\
 &=i(r)\oplus i(-s)\\
 &=i(r+(-s))=i(r-s).
\end{aligned}
$$

这里等式右边的 $r-s$ 是有理差，再取其下段；左边是刚定义的分割差。两者相容已经通过等式证明。

具体取 $A=i(2/3)$、$B=i(-5/6)$，一般解公式给

$$
\begin{aligned}
X
 &=N(i(2/3))\oplus i(-5/6)\\
 &=i(-2/3)\oplus i(-5/6)\\
 &=i(-4/6-5/6)\\
 &=i(-9/6)=i(-3/2).
\end{aligned}
$$

代回核验：

$$
i(2/3)\oplus i(-3/2)
=i(4/6-9/6)=i(-5/6)=B.
$$

因此实例的唯一解正是 $i(-3/2)$；一个算例没有被用来代替任意分割的解法。

最后，用题6的平移双向等价，同加 $N(A)$，得

$$
\begin{aligned}
A\le_{\mathbb R}B
&\quad\Longleftrightarrow\quad
A\oplus N(A)\le_{\mathbb R}B\oplus N(A)\\
&\quad\Longleftrightarrow\quad
0_{\mathbb R}\le_{\mathbb R}B\ominus A.
\end{aligned}
$$

第一步的反向不是未经证明的“消去不等式”，而是题6已经建立的反射。用其严格等价同样得到

$$
A<_{\mathbb R}B
\quad\Longleftrightarrow\quad
0_{\mathbb R}<_{\mathbb R}B\ominus A.
$$

对 $A=0_{\mathbb R}$，所有等式及比较仍合法，因为 $N(0_{\mathbb R})=0_{\mathbb R}$，没有出现零作除数。此处只用了加法、逆元与次序，尚未定义分割乘法，也没有因此得到有序域。
