## 基础单元 B2.32 非负实数平方根的存在唯一 {#realsqrt-unit}

**学习目标与位置。** 有理数二没有有理平方根，并不自动说明另一个数系中已经有了这个根。本单元从现有分割有序域出发，先证明实数平方的代数与次序规律，再用上确界构造每个非负实数的非负平方根。存在与唯一都建立后，才定义根函数，并给出平方方程的全部解和一个无理实数。主归属第526章97F50的实数教学桥接，06A05与已有12J15有序域结构交叉；这里不建立极限理论或一般实数幂。

**精确先修。** 使用[条件子集与外延性](#fun-sets)、[函数定义](#fun-definition)、[分割包含全序与有理嵌入](#cut-order-embedding)、[非空有上界族的上确界](#cut-supremum)。实数运算使用[加法闭合](#cutadd-definition)、[有理加法相容](#cutadd-rational)、[加法群律](#cutgroup-laws)、[相反数](#cutgroup-inverses)、[平移比较](#cutgroup-translation)、[取反、差及差的判据](#cutgroup-negation-subtraction)、[全乘法的单位与负号](#cutsigned-signs)、[全结合律](#cutsigned-associative)、[有理乘法相容与零积](#cutsigned-rational-zero)、[全分配及差乘](#cutring-distributive)、[正负因子比较](#cutring-multiplication-order)、[非零消去](#cutring-cancellation)。除法使用[商定义与乘回](#cutdiv-definition)、[实数乘法方程唯一解](#cutdiv-equations)、[正除数比较](#cutdiv-order)及[有序域与上确界性质](#cutdiv-complete-field)。有理部分只引用[部分根函数的定义](#sqrat-root-uniqueness)及[二不是有理平方](#sqrat-two-not-square)；下面的实数平方规律须另外从实数运算证明。本单元不依赖前一单元的实数稠密性或阿基米德性质。

**记号转换与类型。** 本单元中的 $A,X,U,s,h,t,u,v,\delta$ 表示实数，即已构造的分割；$q,r$ 表示有理数。族用 $\mathcal S_A$ 表示，它的成员是实数。为缩短展开式，以下对实数使用

$$
X+Y:=X\oplus Y,\quad -X:=N(X),\quad
X-Y:=X\ominus Y,\quad XY:=X\otimes Y,
$$

以及仅在 $Y\ne0_{\mathbb R}$ 时使用 $X/Y:=X\oslash Y$。这只是已有运算的简记。实数比较中的 $\le,<$ 简写原来的 $\le_{\mathbb R},<_{\mathbb R}$。在实数公式内，$0,1,2$ 分别简写

$$
0_{\mathbb R}=i(0),\qquad1_{\mathbb R}=i(1),\qquad2_{\mathbb R}=i(2).
$$

嵌入保加法与次序给 $2_{\mathbb R}=1_{\mathbb R}+1_{\mathbb R}>0_{\mathbb R}$，故实数除以二合法。$i$ 的括号内仍是有理数；明确写“有理数”的段落使用其原有运算。对实数仅定义平方

$$
X^2:=XX.
$$

不在这里预定义其他指数。乘法相容给 $i(q)^2=i(q^2)$，右侧的 $q^2$ 是有理平方。

### 1. 先在实数中证明平方规律 {#realsqrt-square-order}

**命题 RS1。** 每个实数 $X$ 满足 $X^2\ge0$，且 $X^2=0$ 当且仅当 $X=0$。对非负实数 $u,v$，平方保持并反映不严格比较、严格比较及相等。

**全符号的平方。** 若 $X=0$，乘零给 $X^2=0$。若 $X>0$，正乘积正给 $X^2>0$。若 $X<0$，则 $-X>0$；已证的双取反乘积规律给

$$
(-X)^2=(-X)(-X)=XX=X^2,
$$

而左侧是两个正数的积，故仍有 $X^2>0$。三歧性穷尽这些情形，所以平方非负，且只有零的平方为零。负号平方等式对任意 $X$ 都成立。

**展开必须来自实数分配律。** 对任意实数 $s,h$，两侧分配分别给

$$
\begin{aligned}
(s+h)^2
&=(s+h)(s+h)\\
&=s(s+h)+h(s+h)\\
&=(ss+sh)+(hs+hh)\\
&=s^2+(sh+sh)+h^2.
\end{aligned}
$$

末步使用乘法交换 $hs=sh$，并按加法结合重新分组。又由单位和分配，

$$
sh+sh=(1+1)(sh)=2(sh)=(2s)h.
$$

因此通常简写 $2sh=(2s)h$，并得到

$$
(s+h)^2=s^2+2sh+h^2.
$$

在已经对任意实数成立的展开式中把 $h$ 换为 $-h$，用取反乘积和 $(-h)^2=h^2$，得到

$$
\begin{aligned}
(s-h)^2
&=s^2+2s(-h)+(-h)^2\\
&=s^2-2sh+h^2.
\end{aligned}
$$

差平方也从实数分配推得：

$$
\begin{aligned}
(v-u)(v+u)
&=v(v+u)-u(v+u)\\
&=(vv+vu)-(uv+uu)\\
&=v^2+(vu-uv)-u^2\\
&=v^2-u^2.
\end{aligned}
$$

第三步用和的相反数与加法群重排，最后用 $vu=uv$ 消去相反的交叉项。以上三个恒等式没有符号限制；它们是在实数环中证明的，不是直接引用有理数范围的同形公式。

**非负范围的比较。** 设 $0\le u<v$。平移比较给 $v-u>0$；又 $v>0$ 且 $u\ge0$，故 $v+u\ge v>0$。两个因子均正，所以

$$
v^2-u^2=(v-u)(v+u)>0,
$$

再用差的判据得到 $u^2<v^2$。当 $u=0$ 时，两个因子都等于正数 $v$，证明仍成立。若 $u=v$，平方相等；于是弱比较的正向也成立。

反过来，假设 $u^2\le v^2$。若 $v<u$，刚证的严格保持给 $v^2<u^2$，矛盾。全序故给 $u\le v$。若假设更强为 $u^2<v^2$，相等输入又不可能，故 $u<v$。若平方相等，两个方向的弱反射给 $u\le v$ 及 $v\le u$，故 $u=v$。这样对非负输入有

$$
\begin{aligned}
u\le v&\Longleftrightarrow u^2\le v^2,\\
u<v&\Longleftrightarrow u^2<v^2,\\
u=v&\Longleftrightarrow u^2=v^2.
\end{aligned}
$$

非负限制不可删除：嵌入给 $i(-2)<i(-1)$，但乘法相容给 $i(-2)^2=i(4)>i(1)=i(-1)^2$。

### 2. 用上确界构造非负平方根 {#realsqrt-existence}

**命题 RS2。** 对每个 $A\in\mathbb R$、$A\ge0$，存在实数 $s\ge0$ 使 $s^2=A$。这里还没有定义根号；先构造所需对象。

**候选族非空且有上界。** 从既有实数集合按条件形成

$$
\mathcal S_A=\{X\in\mathbb R:0\le X\text{ 且 }X^2\le A\}.
$$

这是一个分割族：成员 $X$ 是实数，不是有理成员。$0^2=0\le A$，所以 $0\in\mathcal S_A$。取实数 $U=A+1$，由 $A\ge0$ 得 $U\ge1>0$。RS1的展开和加法群给

$$
\begin{aligned}
U^2-A
&=(A+1)^2-A\\
&=A^2+2A+1-A\\
&=A^2+A+1>0.
\end{aligned}
$$

最后因为 $A^2\ge0$、$A\ge0$ 且 $1>0$。故 $U^2>A$。任取 $X\in\mathcal S_A$；若 $U<X$，两个数均非负，RS1给 $U^2<X^2$，于是 $A<U^2<X^2$，与 $X^2\le A$ 矛盾。故每个 $X\in\mathcal S_A$ 均满足 $X\le U$，$U$ 确为共同上界。

现在[DC4](#cut-supremum)的非空与有分割上界条件均满足，故有实数

$$
s=\sup_{\mathbb R}\mathcal S_A.
$$

它是上界，并小于等于任何其他上界。因为 $0\in\mathcal S_A$，有 $s\ge0$。此时还没有证明 $s\in\mathcal S_A$，尤其不能先写 $s^2\le A$；下面分别排除两种严格比较。

**两个数的较小者。** 本证明只需要局部函数

$$
\min(u,v)=
\begin{cases}
u,&u\le v,\\
v,&v<u,
\end{cases}
\qquad u,v\in\mathbb R.
$$

全序保证两支互斥穷尽。第一支输出等于 $u$ 且不大于 $v$，第二支输出等于 $v$ 且小于 $u$，所以总有 $\min(u,v)\le u,v$。若两个输入都正，各支返回的都是正数，故 $\min(u,v)>0$。这只定义两个给定实数的较小者，不需要一般有限族的最小值理论。

**若平方太小，上调一个候选。** 假设 $s^2<A$，令

$$
\delta=A-s^2>0,\qquad
h=\min\left(1,\frac{\delta}{2s+2}\right).
$$

$s\ge0$ 给 $2s+2>0$；正分子除以正分母仍正，可由DQ3对 $0<\delta$ 同除正分母，并用零商得出。因此两个较小者输入都正，且

$$
h>0,\qquad h\le1,\qquad h\le\frac{\delta}{2s+2}.
$$

第一项弱界同乘正 $h$，给 $h^2\le h$。第二项弱界同乘正 $2s+2$，利用商的乘回给 $(2s+2)h\le\delta$。又因 $2s+1<2s+2$，同乘正 $h$ 得严格比较。合在一起，

$$
\begin{aligned}
2sh+h^2
&\le2sh+h\\
&=(2s+1)h\\
&<(2s+2)h\\
&\le\delta.
\end{aligned}
$$

【依据：第一步为加法保序；等式用分配与单位；严格步的共同因子为正 $h$；末步用已核合法的乘回。】因此RS1给

$$
(s+h)^2=s^2+(2sh+h^2)<s^2+\delta=A.
$$

又有 $s+h>0$，故 $s+h\in\mathcal S_A$。但 $h>0$ 同时给 $s+h>s$，与 $s$ 是该族上界矛盾。这一构造允许 $s=0$；所有正性已由常量二和正 $\delta$ 保证。

**若平方太大，下调一个上界。** 假设 $s^2>A$。因为 $A\ge0$，有 $s^2>0$，RS1零判据给 $s\ne0$；连同 $s\ge0$ 得 $s>0$。令

$$
\delta=s^2-A,\qquad h=\frac{\delta}{2s}.
$$

由假设及 $A\ge0$，

$$
0<\delta\le s^2.
$$

分母 $2s$ 正，所以 $h>0$，并且正除法给

$$
h\le\frac{s^2}{2s}.
$$

为化简右侧，先核实数 $s/2$ 合法且正。DQ1的乘回给 $2(s/2)=s$；结合交换遂给

$$
(2s)(s/2)=s\bigl(2(s/2)\bigr)=s^2.
$$

而 $s^2/(2s)$ 也乘以非零 $2s$ 得 $s^2$，所以由非零消去，

$$
\frac{s^2}{2s}=\frac s2,
\qquad 0<h\le s/2.
$$

这里没有预用一般分式约分公式。再由分配和 $2(s/2)=s$ 得 $(s/2)+(s/2)=s$，所以 $s-s/2=s/2$。定义

$$
t=s-h.
$$

由 $h\le s/2$、取反反序和平移，

$$
t=s-h\ge s-s/2=s/2>0.
$$

又由 $h>0$ 得 $t<s$。商的乘回给 $2sh=\delta$；RS1的减量展开给

$$
\begin{aligned}
t^2
&=(s-h)^2\\
&=s^2-2sh+h^2\\
&=s^2-\delta+h^2\\
&=A+h^2>A.
\end{aligned}
$$

最后的严格号来自 $h>0$，故 $h^2>0$。

现在必须证明 $t$ 是整个候选族的上界。任取 $X\in\mathcal S_A$，已有 $X\ge0$ 且 $X^2\le A$。若 $X\ge t$，因为 $t>0$，RS1的非负平方弱保持给

$$
X^2\ge t^2>A,
$$

矛盾。因此每个 $X\in\mathcal S_A$ 都满足 $X<t$，尤其满足 $X\le t$。这才说明 $t$ 为共同上界；仅知道 $t^2>A$ 或 $t\notin\mathcal S_A$ 本身并不足够。$s$ 的最小上界性质于是给 $s\le t$，与 $t<s$ 矛盾。

两种严格比较都不成立，全序只剩 $s^2=A$。再结合 $s\ge0$，存在性得到证明。即使 $A=0$，上侧假设也先给 $s>0$，所有除法合法，同一矛盾仍可使用；并未在证明中除以可能为零的 $A$。RS2证毕。

这个证明两次使用上确界的不同部分：上调时违反“是上界”，下调时违反“最小”。它没有用有理稠密性、实数阿基米德性、数列极限或连续性来寻找 $h$。

### 3. 唯一非负根给出一个函数 {#realsqrt-function}

**命题 RS3。** 每个非负实数有唯一的非负平方根。若 $s,t\ge0$ 且 $s^2=t^2=A$，RS1的非负平方判等给 $s=t$。存在来自RS2，唯一来自RS1，因此可以定义函数

$$
\operatorname{sqrt}_{\mathbb R}:\mathbb R_{\ge0}\longrightarrow\mathbb R_{\ge0},
\qquad
\mathbb R_{\ge0}=\{A\in\mathbb R:A\ge0\}.
$$

它在输入 $A$ 的输出是唯一满足 $s\ge0,s^2=A$ 的实数 $s$。函数的图由这些输入输出对组成；每个域内输入已有且只有一个目标内输出。以后简记

$$
\sqrt A:=\operatorname{sqrt}_{\mathbb R}(A),\qquad A\ge0.
$$

这个根号代表一个非负值。因为 $0^2=0$、$1^2=1$ 且两者非负，唯一性给 $\sqrt0=0$、$\sqrt1=1$。若 $A>0$，其根不能等于零，否则 $A=(\sqrt A)^2=0$；故 $\sqrt A>0$。若 $A<0$，RS1说明没有任何实数平方等于它，且根函数不在这个输入处定义。

例如 $3/4$ 是正有理数，$i(3/4)>0$，平方相容给 $i(3/4)^2=i(9/16)$。由唯一性，

$$
\sqrt{i(9/16)}=i(3/4).
$$

**与已有有理根函数相容。** 旧定义的域为

$$
S_{\mathbb Q}=\{q\in\mathbb Q:\text{存在 }r\in\mathbb Q, r\ge0\text{ 且 }r^2=q\}.
$$

设 $q\in S_{\mathbb Q}$，令有理数 $r=\operatorname{sqrt}_{\mathbb Q}(q)$。已有 $r\ge0$、$r^2=q$，从而 $q\ge0$，$i(q)$ 在实数根函数域内。嵌入保序和乘法相容给

$$
i(r)\ge0,\qquad i(r)^2=i(r^2)=i(q).
$$

由实数非负根唯一性，

$$
\operatorname{sqrt}_{\mathbb R}(i(q))
=i\bigl(\operatorname{sqrt}_{\mathbb Q}(q)\bigr).
$$

反过来，设有理数 $q\ge0$，且 $\sqrt{i(q)}=i(r)$，其中 $r\in\mathbb Q$。根非负和嵌入反映次序给 $r\ge0$；平方关系给 $i(r^2)=i(q)$，单射性给 $r^2=q$，所以 $q\in S_{\mathbb Q}$。若 $q\notin S_{\mathbb Q}$，不能写不存在的 $\operatorname{sqrt}_{\mathbb Q}(q)$；新的实数根可能正好补上旧有理数范围的缺口。

### 4. 平方方程的全部实数解与二的无理根 {#realsqrt-equations-irrational}

**命题 RS4。** 固定 $A\in\mathbb R$，候选域是 $\mathbb R$。左、右两边分别是函数 $X\mapsto X^2$ 和常值函数 $X\mapsto A$，解集为 $\{X\in\mathbb R:X^2=A\}$。

若 $A<0$，平方非负给解集为空。若 $A=0$，平方零判据给解集恰为 $\{0\}$。若 $A>0$，令 $s=\sqrt A>0$，则 $s^2=A$，并且 $(-s)^2=s^2=A$，所以 $s$、$-s$ 都是解。

为排除其他解，任取 $X^2=A=s^2$。由已在实数中证明的差平方和全乘法零积判据，

$$
(X-s)(X+s)=X^2-s^2=0
\quad\Longrightarrow\quad X-s=0\text{ 或 }X+s=0.
$$

第一支两边同加 $s$ 得 $X=s$；第二支同加 $-s$ 得 $X=-s$。因此上述候选穷尽全部解。又有 $-s<0<s$，两者不同。完整分类为

$$
\{X\in\mathbb R:X^2=A\}
=
\begin{cases}
\varnothing,&A<0,\\
\{0\},&A=0,\\
\{\sqrt A,-\sqrt A\},&A>0.
\end{cases}
$$

“$\pm\sqrt A$”只是在正目标的解集中列两项的简写，不是给根函数两个输出。

**二的根确实存在，而且不在有理像中。** 嵌入给 $i(2)>0$，所以RS2、RS3已经构造了实数 $s=\sqrt{i(2)}>0$。若存在有理数 $q$ 使 $s=i(q)$，平方相容给

$$
i(q^2)=i(q)^2=s^2=i(2).
$$

嵌入单射性会给有理等式 $q^2=2$，与[二不是有理平方](#sqrat-two-not-square)矛盾。因此 $s\notin i(\mathbb Q)$，其中

$$
i(\mathbb Q)=\{X\in\mathbb R:\text{存在 }q\in\mathbb Q\text{ 使 }X=i(q)\}.
$$

本处称 $\mathbb R\setminus i(\mathbb Q)$ 的元素为**无理实数**。这区别于声称有理数底层对象字面就是实数底层对象。

还可不用小数近似确定根的位置。常量一、二与 $s$ 均非负，且

$$
1^2=i(1)<i(2)=s^2<i(4)=2^2.
$$

RS1反映严格比较，给 $1<s<2$。这个结论来自平方与次序，不依赖几何长度。此前构造的非主分割与这个根是否为同一个具体有理下集，本单元不作未经逐成员证明的认定。

### 5. 课后题 {#realsqrt-exercises}

#### 题1：平方的定义与全符号 {#realsqrt-q01}

说明实数平方的定义和本单元普通运算符的含义。按零、正、负三种输入证明 $X^2\ge0$、$X^2=0\Longleftrightarrow X=0$ 及 $(-X)^2=X^2$。以 $i(-2),i(-1)$ 检查平方在全实数域不保持严格次序。[完整解答](#realsqrt-a01)

#### 题2：展开与非负平方比较 {#realsqrt-q02}

从实数两侧分配逐步推导 $(s+h)^2$、$(s-h)^2$ 及差平方公式，写出四项展开和交叉项合并的依据。继而在非负范围证明平方的严格保持、弱保持、反射及判等；标明差平方的两个因子为什么正。[完整解答](#realsqrt-a02)

#### 题3：形成候选族并合法使用上确界 {#realsqrt-q03}

对 $A\ge0$ 定义 $\mathcal S_A$，证明非空。取 $U=A+1$，完整展开 $U^2-A$ 并证明它正，再逐任意候选说明 $U$ 是上界。由DC4取得 $s$ 并证明 $s\ge0$，说明此时为什么尚不能断言 $s\in\mathcal S_A$。[完整解答](#realsqrt-a03)

#### 题4：平方太小时上调候选 {#realsqrt-q04}

先定义两个实数的 $\min$，逐支证明它不大于两输入，且正输入给正输出。假设题3中的 $s^2<A$，构造 $\delta,h$ 并核所有分母及正性，逐步证明 $2sh+h^2<\delta$，推出 $s+h$ 是大于上界的族成员。说明 $s=0$ 边界仍有效。[完整解答](#realsqrt-a04)

#### 题5：平方太大时下调上界 {#realsqrt-q05}

假设 $s^2>A\ge0$，证明 $s>0$、$0<\delta=s^2-A\le s^2$。取 $h=\delta/(2s)$，以乘回和非零消去证明 $h\le s/2$，再令 $t=s-h$，核 $0<t<s$ 及 $t^2=A+h^2>A$。逐任意 $X\in\mathcal S_A$ 证明 $X<t$，从而 $t$ 为上界并与最小性矛盾。不得省略任意候选这一段；检查 $A=0$。[完整解答](#realsqrt-a05)

#### 题6：根函数的存在、唯一与定义域 {#realsqrt-q06}

合并题3—5的结论取得非负根存在，再证唯一，写出根函数的域、目标和求值规则。证明零、一及正输入的根性质，说明负输入的情形。通过检验候选与唯一性求 $\sqrt{i(9/16)}$。[完整解答](#realsqrt-a06)

#### 题7：有理相容与无理根 {#realsqrt-q07}

对 $q\in S_{\mathbb Q}$ 证明两种根函数经嵌入相容；反过来，非负有理数的实数根若属于有理像，证明该有理数属于 $S_{\mathbb Q}$。据此或直接用嵌入单射性证明 $\sqrt{i(2)}\notin i(\mathbb Q)$，并证明 $1<\sqrt{i(2)}<2$。[完整解答](#realsqrt-a07)

#### 题8：平方方程全解与一次平移 {#realsqrt-q08}

在候选域 $\mathbb R$ 中完整分类 $X^2=A$ 的三个参数分支；正目标须先代回两个候选，再用差平方和零积证明穷尽。应用到 $(X-1)^2=i(2)$，证明 $Y=X-1$ 与 $X=Y+1$ 是双向代换，列出全部解、代回、证明两解不同且都不在有理像中。[完整解答](#realsqrt-a08)

**来源与范围说明。** 上确界扰动路线及条件差异见[实数界、稠密与平方根来源核验](#real-arch-sqrt-sources)。本单元在已构造的实数运算中重新展开，使用两个明确扰动证明一般非负目标的存在，再定义根函数；没有借连续性、极限、一般实数幂或几何公理。有理算例不替代一般存在证明。
