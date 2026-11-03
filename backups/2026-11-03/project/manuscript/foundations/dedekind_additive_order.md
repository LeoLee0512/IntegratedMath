## 基础单元 B2.24 分割加法的群律与次序平移 {#cutgroup-unit}

**学习目标与位置。** 上一单元已经定义和分割与负分割，并证明结果仍是分割。现在要证明这些运算确实满足熟悉的加法规则：交换、结合、零单位、加法逆元，以及同加一个分割时大小关系的双向保持。主归属第526章97F50的实数教学部分，06F20有序交换群、06A05全序交叉；本单元不定义分割乘法或除法。

**精确先修。** 使用[分割四条件](#cut-definition)、[包含全序与有理嵌入](#cut-order-embedding)、[内外分离](#cutadd-separation)、[任意小的有理跨界间隔](#cutadd-grid)、[和分割定义与闭合](#cutadd-definition)、[负分割定义与闭合](#cutadd-negation)、[有理运算相容](#cutadd-rational)。展开成员见证时使用既有[有理加法](#radd-laws)、[相反数](#radd-opposite)、[减法与加法方程](#radd-subtraction)、[有理平移比较](#rord-translation)、[取反反序](#rord-negation)。函数部分使用[函数定义](#fun-definition)与[双侧逆](#inv-two-sided)。

**固定记号。** 对分割 $A,B\in\mathbb R$，沿用

$$
A\oplus B=\{q\in\mathbb Q:\exists a\in A,\exists b\in B,\ q=a+b\},
$$

$$
N(A)=\{q\in\mathbb Q:\exists r\in\mathbb Q,\ r\notin A\text{ 且 }q<-r\},
\qquad 0_{\mathbb R}=i(0)=\{q\in\mathbb Q:q<0\}.
$$

这些集合已经属于 $\mathbb R$，所以 $\oplus:\mathbb R\times\mathbb R\to\mathbb R$、$N:\mathbb R\to\mathbb R$ 已有定义。本单元的大写字母均表示分割；成员等式中的小写加减是有理运算。$0_{\mathbb R}$ 非空，但不包含有理数零；在证明单位元性质前，不能仅凭名字就使用该性质。次序仍为 $A\le_{\mathbb R}B\Longleftrightarrow A\subseteq B$。

### 1. 从成员见证证明交换、结合与单位 {#cutgroup-laws}

对有理下段，上一单元已证 $i(r)\oplus i(s)=i(r+s)$。但不是每个分割都形如 $i(r)$；[非主分割的例子](#cut-gap)已经说明这一点。一般规律必须对任意分割另证。

**命题 DG1。** 对任意 $A,B,C\in\mathbb R$，

$$
A\oplus B=B\oplus A,
\qquad (A\oplus B)\oplus C=A\oplus(B\oplus C),
$$

$$
A\oplus0_{\mathbb R}=A=0_{\mathbb R}\oplus A.
$$

**交换律。** 若 $q\in A\oplus B$，取 $a\in A,b\in B$ 使 $q=a+b$。有理加法交换律给 $q=b+a$，所以同一对见证倒序放置便得 $q\in B\oplus A$。这证明一个包含方向。反过来，若 $q=b+a$ 的见证为 $b\in B,a\in A$，有理交换律又给 $q=a+b$，所以 $q\in A\oplus B$。外延相等给新运算的交换律。

**结合律。** 先取 $q\in(A\oplus B)\oplus C$。外层成员定义给出

$$
u\in A\oplus B,\quad c\in C,\quad q=u+c.
$$

再展开 $u\in A\oplus B$：存在 $a\in A,b\in B$ 使 $u=a+b$。于是

$$
q=(a+b)+c=a+(b+c).
$$

此处等号使用的是**有理数**结合律。令 $v=b+c$，见证 $b,c$ 保证 $v\in B\oplus C$；再由 $a\in A,q=a+v$ 得 $q\in A\oplus(B\oplus C)$。

反向，取 $q\in A\oplus(B\oplus C)$。先展开为 $q=a+v$，其中 $a\in A,v\in B\oplus C$；再取 $b\in B,c\in C$ 使 $v=b+c$。有理结合律给 $q=(a+b)+c$。令 $u=a+b\in A\oplus B$，于是 $q=u+c\in(A\oplus B)\oplus C$。两个包含合成所求等式，没有提前对分割运算任意改括号。

**右单位。** 若 $q\in A\oplus0_{\mathbb R}$，则存在 $a\in A,z\in0_{\mathbb R}$ 使 $q=a+z$。成员条件给 $z<0$，同加 $a$ 得 $q<a$。由 $A$ 向下封闭，$q\in A$。因此 $A\oplus0_{\mathbb R}\subseteq A$。

反过来，给定 $q\in A$。因为 $A$ 没有最大元，可取 $a\in A$ 满足 $q<a$。令有理数 $z=q-a$，则 $z<0$，所以 $z\in0_{\mathbb R}$；又有 $q=a+z$。这两个见证给出 $q\in A\oplus0_{\mathbb R}$。两个方向得 $A\oplus0_{\mathbb R}=A$。

最后，由刚证的交换律，$0_{\mathbb R}\oplus A=A\oplus0_{\mathbb R}=A$。DG1证毕。单位元证明中不能用 $z=0$：有理零不是零分割的成员，反向包含需要的是较大内点 $a$ 与严格负的差 $q-a$。

### 2. 负分割确为加法逆元 {#cutgroup-inverses}

**命题 DG2。** 对任意 $A\in\mathbb R$，

$$
A\oplus N(A)=0_{\mathbb R}=N(A)\oplus A.
$$

满足 $A\oplus B=0_{\mathbb R}$ 的分割 $B$ 唯一，并且

$$
N(N(A))=A,\qquad N(0_{\mathbb R})=0_{\mathbb R}.
$$

**先证和中的每个成员都严格小于零。** 若 $q\in A\oplus N(A)$，取 $a\in A,c\in N(A)$ 使 $q=a+c$。负分割的成员定义又给有理见证 $r\notin A$，满足 $c<-r$。

分割的[内外分离事实](#cutadd-separation)给 $a<r$。分别使用有理平移比较，得到

$$
a+c<a-r,\qquad a-r<0.
$$

所以 $q<0$，即 $q\in0_{\mathbb R}$。这证明 $A\oplus N(A)\subseteq0_{\mathbb R}$。这里没有假定 $a$ 自身为负；它与外点 $r$ 的相对位置才是依据。

**反向必须覆盖每一个负有理数。** 任取 $x\in0_{\mathbb R}$，即 $x<0$。令

$$
\varepsilon=-x>0.
$$

对分割 $A$ 应用[DA1的跨界间隔](#cutadd-grid)，得到有理数 $u,v$ 满足

$$
u\in A,\quad v\notin A,\quad 0<v-u<-x.
$$

从最后的严格比较逐步移项：

$$
\begin{aligned}
v-u&<-x,\\
x+v-u&<0,\\
x-u&<-v.
\end{aligned}
$$

【依据：第二行对两边同加 $x$，并用 $x+(-x)=0$；第三行对两边同加 $-v$，在有理加法结合交换下消去 $v+(-v)$。两个平移均保持严格比较。】

令 $c=x-u$。外点 $v\notin A$ 和 $c<-v$ 共同见证 $c\in N(A)$。又有 $u+c=u+(x-u)=x$，所以 $u,c$ 见证 $x\in A\oplus N(A)$。每个负有理数都被包含，故 $0_{\mathbb R}\subseteq A\oplus N(A)$。

两向合得 $A\oplus N(A)=0_{\mathbb R}$，再由DG1交换律得 $N(A)\oplus A=0_{\mathbb R}$。现在才证明 $N(A)$ 是 $A$ 的**加法逆元**。网格引理在此提供的严格间距不可降为不带余量的 $v-u\le -x$，否则只能得到 $c\le-v$，不能保证负分割定义要求的严格号。

**逆元唯一性。** 假设 $B\in\mathbb R$ 满足 $A\oplus B=0_{\mathbb R}$。依次用已经证明的单位、逆元、结合律，

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

因此任何候选都只能等于 $N(A)$。这里没有先使用尚未证明的加法消去律。

**双重取反。** 已有 $N(A)\oplus A=0_{\mathbb R}$，所以 $A$ 是分割 $N(A)$ 的一个逆元。把刚证的唯一性应用于这个分割，便得到 $A=N(N(A))$。

又由单位律，$0_{\mathbb R}\oplus0_{\mathbb R}=0_{\mathbb R}$，所以 $0_{\mathbb R}$ 是自身的一个逆元。唯一性给 $N(0_{\mathbb R})=0_{\mathbb R}$，与上一单元的有理嵌入相容结论一致。DG2证毕。

到这里可以给已证规则一个名称：一个集合配有封闭且满足结合律的加法、双侧单位及每个元素的加法逆元，称为加法群；若加法还交换，称为交换加法群。$\mathbb R$ 与 $\oplus,0_{\mathbb R},N$ 满足这些逐项证明的规则。名称概括证明结果，不是用来代替证明的先修公理。

### 3. 同加一个分割，次序能够保持也能够反射 {#cutgroup-translation}

**命题 DG3。** 对任意 $A,B,C\in\mathbb R$，

$$
A\le_{\mathbb R}B
\quad\Longleftrightarrow\quad
A\oplus C\le_{\mathbb R}B\oplus C,
$$

$$
A<_{\mathbb R}B
\quad\Longleftrightarrow\quad
A\oplus C<_{\mathbb R}B\oplus C.
$$

此外，$A\oplus C=B\oplus C$ 当且仅当 $A=B$。固定 $C$ 的平移是一个双射。

**弱保序。** 设 $A\subseteq B$。若 $q\in A\oplus C$，取 $a\in A,c\in C$ 使 $q=a+c$。由包含关系 $a\in B$，同一对见证给 $q\in B\oplus C$。因此 $A\oplus C\subseteq B\oplus C$。

这一步从成员定义直接得到，只证明了非严格方向。下面才说明如何反推。

**反射。** 设 $A\oplus C\subseteq B\oplus C$。将刚证的弱保序应用于这两个分割，并同加 $N(C)$，得到

$$
(A\oplus C)\oplus N(C)
\subseteq
(B\oplus C)\oplus N(C).
$$

DG1、DG2给

$$
(A\oplus C)\oplus N(C)
=A\oplus(C\oplus N(C))
=A\oplus0_{\mathbb R}=A,
$$

右侧同理化为 $B$。于是 $A\subseteq B$，证明非严格比较的双向等价。

**相等消去。** 若 $A\oplus C=B\oplus C$，两方向包含分别通过反射给 $A\subseteq B$、$B\subseteq A$，故 $A=B$。反向若 $A=B$，相等输入的函数值相等，所以两和相等。交换律也允许在左侧消去同一加项。

**严格比较。** 若 $A<_{\mathbb R}B$，弱保序先给 $A\oplus C\subseteq B\oplus C$；若两和相等，消去给 $A=B$，与严格比较矛盾。因此包含严格。反过来，若两和严格比较，弱反射给 $A\subseteq B$；若 $A=B$，两和会相等，矛盾。所以 $A<_{\mathbb R}B$。这证明严格等价，不是从一般单调性直接宣称严格保序。

**平移的双侧逆。** 固定 $C$，定义函数

$$
T_C:\mathbb R\to\mathbb R,\qquad T_C(A)=A\oplus C.
$$

加法闭合保证目标正确。对任意 $A\in\mathbb R$，

$$
T_{N(C)}(T_C(A))
=(A\oplus C)\oplus N(C)=A,
$$

$$
T_C(T_{N(C)}(A))
=(A\oplus N(C))\oplus C
=A\oplus(N(C)\oplus C)=A.
$$

因此 $T_{N(C)}$ 是 $T_C$ 的双侧逆；两函数的定义域与目标都为 $\mathbb R$，复合匹配。由[已证双侧逆判据](#inv-two-sided)，$T_C$ 是双射。DG3证毕。结合已有全序，这种加法与次序的相容结构称为**有序交换加法群**；乘法仍未包括在其中。

### 4. 取反、减法与加法方程 {#cutgroup-negation-subtraction}

**命题 DG4。** 对任意 $A,B\in\mathbb R$，

$$
A\le_{\mathbb R}B
\quad\Longleftrightarrow\quad
N(B)\le_{\mathbb R}N(A),
$$

严格比较同样反向，并且

$$
N(A\oplus B)=N(A)\oplus N(B).
$$

定义分割减法

$$
A\ominus B:=A\oplus N(B).
$$

则加法方程 $A\oplus X=B$ 对所有 $A,B$ 都有唯一解 $X=N(A)\oplus B$。另有

$$
i(r)\ominus i(s)=i(r-s)\qquad(r,s\in\mathbb Q),
$$

$$
A\le_{\mathbb R}B
\quad\Longleftrightarrow\quad
0_{\mathbb R}\le_{\mathbb R}B\ominus A,
$$

最后一个等价的严格版本也成立。

**先从成员证明取反的一向反序。** 设 $A\subseteq B$。若 $q\in N(B)$，取 $r\notin B$ 且 $q<-r$。这个 $r$ 也不属于 $A$，否则 $A\subseteq B$ 会推出 $r\in B$。所以同一个 $r$ 见证 $q\in N(A)$，即 $N(B)\subseteq N(A)$。

反向，设 $N(B)\subseteq N(A)$。对这对输入再次应用刚证的反序方向，得

$$
N(N(A))\subseteq N(N(B)).
$$

DG2的双重取反化为 $A\subseteq B$。因此非严格反序的两个方向均成立。

若 $A<_{\mathbb R}B$，已经有 $N(B)\subseteq N(A)$；若两者相等，应用函数 $N$ 并用双重取反会得 $B=A$，矛盾，所以 $N(B)<_{\mathbb R}N(A)$。反过来，若 $N(B)<_{\mathbb R}N(A)$，非严格反射给 $A\subseteq B$，相等 $A=B$ 又会迫使两负分割相等，矛盾。故 $A<_{\mathbb R}B$。

**和的相反数。** 先验证 $N(A)\oplus N(B)$ 是 $A\oplus B$ 的一个逆元。以下每次改变括号使用的是此时已经证明的DG1：

$$
\begin{aligned}
&(A\oplus B)\oplus(N(A)\oplus N(B))\\
&=((A\oplus B)\oplus N(A))\oplus N(B)\\
&=(A\oplus(B\oplus N(A)))\oplus N(B)\\
&=(A\oplus(N(A)\oplus B))\oplus N(B)\\
&=((A\oplus N(A))\oplus B)\oplus N(B)\\
&=(0_{\mathbb R}\oplus B)\oplus N(B)\\
&=B\oplus N(B)=0_{\mathbb R}.
\end{aligned}
$$

【依据：第二、三行依次改变外层与内层括号；第四行只交换内部的 $B$ 与 $N(A)$；第五行再结合；后三步用逆元和单位。】

DG2的逆元唯一性因此给 $N(A\oplus B)=N(A)\oplus N(B)$。不能把“负号分配”当作一个尚无证明的起点。

**减法及其有理相容。** 因 $N(B)\in\mathbb R$ 且和闭合，$A\ominus B$ 总是分割，所以这是定义在全部 $\mathbb R\times\mathbb R$ 上的二元运算。由[DA4](#cutadd-rational)，

$$
\begin{aligned}
i(r)\ominus i(s)
 &=i(r)\oplus N(i(s))\\
 &=i(r)\oplus i(-s)\\
 &=i(r+(-s))=i(r-s).
\end{aligned}
$$

**加法方程的必要性。** 若 $A\oplus X=B$，两边同加 $N(A)$，用交换、结合、逆元和单位，得到

$$
X=(N(A)\oplus A)\oplus X
=N(A)\oplus(A\oplus X)
=N(A)\oplus B.
$$

**充分性。** 取 $X=N(A)\oplus B$，则

$$
A\oplus X=A\oplus(N(A)\oplus B)
=(A\oplus N(A))\oplus B=B.
$$

候选确实存在且满足方程；必要性已强制所有解等于它，所以解唯一。这对 $A=0_{\mathbb R}$ 也成立，不需要把任何分割用作除数。

例：若 $A=i(2/3)$、$B=i(-5/6)$，有理相容给

$$
X=i(-2/3)\oplus i(-5/6)
=i(-4/6-5/6)=i(-3/2).
$$

代回 $i(2/3)\oplus i(-3/2)=i(4/6-9/6)=i(-5/6)$，与一般必要性合起来保证这是全部解。

**用差表示比较。** 对 $A\le_{\mathbb R}B$ 使用DG3，同加 $N(A)$，等价地得到

$$
A\oplus N(A)\le_{\mathbb R}B\oplus N(A).
$$

左侧化为 $0_{\mathbb R}$，右侧是定义的 $B\ominus A$，所以得到命题中的等价。DG3严格比较的双向形式以同样代入给

$$
A<_{\mathbb R}B
\quad\Longleftrightarrow\quad
0_{\mathbb R}<_{\mathbb R}B\ominus A.
$$

DG4证毕。这里才把比较写成一个分割差的正负；先修中网格点的差始终是有理差，两种层次不混用。

### 5. 容易越过的证明步骤 {#cutgroup-mistakes}

**有理实例不能覆盖非主分割。** $i(r)\oplus i(s)=i(r+s)$ 说明相容，却没有证明每个分割都是有理下段。一般结合、单位和逆元需要本单元的成员论证。

**只有一个包含还不是逆元等式。** 从 $a<r$ 很快得到 $A\oplus N(A)\subseteq0_{\mathbb R}$；要包含每个负有理数，必须构造足够近的内外点。正是这个反向使用了前一单元的网格引理。

**同加保持包含还不够反推。** 弱保序先由见证得到；反射要等逆元已证，再同加 $N(C)$ 并化简。严格保序又需排除两和相等，不能只把弱不等号换成严格号。

**零分割没有零这个成员。** 单位元是一个集合对象；它包含负有理数，而非仅含有理零。单位证明用 $q<a$ 来构造严格负的差，不能用不在零分割中的零充当见证。

**加法群不是有序域。** 本单元已经有加法、相反数、减法、全序及平移相容。分割乘法、倒数、分配律和平方根存在还需后续定义与证明；这些不能从“实数”这一名称自动取得。

### 6. 课后题 {#cutgroup-exercises}

#### 题1：先展开见证，再改有理括号 {#cutgroup-q01}

完整证明分割加法交换律与结合律。结合律的两个方向都要展开两层成员见证，并说明重新组合的中间和属于哪个分割；不得预用尚在证明的新结合律。[完整解答](#cutgroup-a01)

#### 题2：零单位为什么需要无最大元 {#cutgroup-q02}

完整证明 $A\oplus0_{\mathbb R}=A=0_{\mathbb R}\oplus A$。反向包含明确构造两个有理成员，并解释为什么直接选 $z=0$ 不是合法见证。[完整解答](#cutgroup-a02)

#### 题3：逆元等式的第一个包含 {#cutgroup-q03}

展开 $q\in A\oplus N(A)$ 的全部成员见证，证明 $q<0$，逐个说明严格比较来自何处。给一个有理下段例子说明 $a\in A$ 并不意味着 $a<0$。[完整解答](#cutgroup-a03)

#### 题4：严格跨界间距补出另一个包含 {#cutgroup-q04}

对任意 $x<0$，令 $\varepsilon=-x$ 并调用DA1，逐行构造 $u\in A,v\notin A,c=x-u$，证明 $c\in N(A)$ 及 $x=u+c$。与题3合并证明双边逆元；解释只有 $v-u\le-x$ 时为什么不能直接完成这一见证。[完整解答](#cutgroup-a04)

#### 题5：逆元唯一以后才能双重取反 {#cutgroup-q05}

完整证明逆元唯一、$N(N(A))=A$ 及 $N(0_{\mathbb R})=0_{\mathbb R}$，标出结合、单位与已证逆元的使用位置。说明没有提前使用消去律。[完整解答](#cutgroup-a05)

#### 题6：平移的保序、反射和逆函数 {#cutgroup-q06}

从成员定义证明弱平移保序，再用 $N(C)$ 证明反射。证明相等消去及严格比较的双向等价，最后给 $T_C(A)=A\oplus C$ 的双侧逆，核定义域与目标。[完整解答](#cutgroup-a06)

#### 题7：取反反序与和的相反数 {#cutgroup-q07}

由补集见证证明取反的非严格反序，再用双重取反得到反向及严格形式。通过完整的四项重括号步骤证明 $N(A\oplus B)=N(A)\oplus N(B)$，说明最后为何使用逆元唯一性。[完整解答](#cutgroup-a07)

#### 题8：减法、方程及差的符号 {#cutgroup-q08}

定义分割减法后，完整求解任意 $A\oplus X=B$ 并证明唯一，核 $i(r)\ominus i(s)=i(r-s)$。取 $A=i(2/3),B=i(-5/6)$ 给具体解并代回。再证明 $A\le_{\mathbb R}B$ 当且仅当 $0_{\mathbb R}\le_{\mathbb R}B\ominus A$，以及严格版本，说明是否需要 $A\ne0_{\mathbb R}$。[完整解答](#cutgroup-a08)

**来源与范围说明。** 与公开定义版本、群律和次序条件的对照见[本批来源审计](#dedekind-addition-sources)。本文把一般法则从成员定义及已证有理网格引理逐项推出，不借尚未建立的实数域、实数稠密性或极限；函数与运算也没有被宣称为任意分割的可执行成员算法。已证的是有序交换加法群结构。
