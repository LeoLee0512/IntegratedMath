## 基础单元 B4.6 实函数的点极限 {#funlimit-unit}

**位置与目标。** 本单元进入第18部分“实函数”的第146章“一元函数”（26Axx），主归26A03“基础：极限及其推广、直线上的初等拓扑”，函数域与类型的教学接口交叉97I20。我们用实数误差和输入半径直接定义点极限，证明唯一性、局部性质及基本运算。这里只是 `single-analysis` 路线的一段，不表示微积分、拓扑或整章完成；数列柯西判据不是本单元的逻辑先修。

**精确先修。** 使用[集合、子集与条件成员](#fun-sets)、[函数及唯一输出](#fun-definition)、[实数全序](#cut-order-embedding)、[加法群](#cutgroup-laws)、[相反数与差](#cutgroup-negation-subtraction)、[序平移](#cutgroup-translation)、[实数乘法符号](#cutsigned-signs)、[乘法结合](#cutsigned-associative)、[零积与有理乘法相容](#cutsigned-rational-zero)、[有理加法相容](#cutadd-rational)、[分配与差乘](#cutring-distributive)、[乘法比较](#cutring-multiplication-order)、[合法除法与乘回](#cutdiv-definition)、[非零系数方程唯一解](#cutdiv-equations)、[正除法比较与倒数反序](#cutdiv-order)、[绝对值基本界及零判据](#realabs-definition-bounds)、[绝对值乘商、三角与反三角](#realabs-products-triangle)、[实数平方与平方差](#realsqrt-square-order)。本单元不借数列运算定理代替函数的误差证明。

**对象。** $D$ 是实数集合的子集，$p,L,A,B,c,d,x,\varepsilon,\delta,r$ 都是实数。函数的域会逐次声明。正半径的单位与输入实数使用同一实数模型；$1,2,3$ 等常数是有理数嵌入像，运算是已构造实数运算的简写。平方 $x^2$ 只表示 $xx$。

### 1. 必须先有能靠近的输入 {#funlimit-domain-definition}

**聚点定义。** 给 $D\subseteq\mathbb R$ 与 $p\in\mathbb R$。若

$$
\begin{gathered}
\forall r>0\ \exists x\in D,\\
0<|x-p|<r,
\end{gathered}
$$

则称 $p$ 是 $D$ 的**聚点**。这里 $r$ 为实数。每个正半径内都要有不同于 $p$ 的域内输入；$p$ 可以属于 $D$，也可以不属于 $D$。

对正实数 $\delta$，记穿孔输入域为

$$
D^*(p,\delta)=\{x\in D:0<|x-p|<\delta\}.
$$

“穿孔”只表示去掉中心 $p$。聚点条件就是每个这样的穿孔输入域非空，而不是仅说 $D$ 非空。

**命题 FL1：定义、否定与域的实例。** 设 $f:D\to\mathbb R$，并且 $p$ 是 $D$ 的聚点。对固定实数 $L$，定义 $f(x)$ 沿 $D$ 趋近 $p$ 时收敛到 $L$，为

$$
\begin{gathered}
\forall\varepsilon>0\ \exists\delta>0\ \forall x\in D,\\
0<|x-p|<\delta\Longrightarrow |f(x)-L|<\varepsilon.
\end{gathered}
$$

$\varepsilon,\delta$ 都为实数。先给正的输出误差，再选一个正输入半径，最后检查该穿孔域的所有输入。所选半径可以依赖 $f,D,p,L,\varepsilon$，不能依赖之后任取的 $x$。

固定 $L$ 时，收敛条件的否定是

$$
\begin{gathered}
\exists\varepsilon_0>0\ \forall\delta>0\ \exists x\in D,\\
0<|x-p|<\delta\quad\text{且}\quad |f(x)-L|\ge\varepsilon_0.
\end{gathered}
$$

**否定的依据。** 否定“每个正误差都有半径”，得到某个正误差没有可用半径；任给半径都失败，意味着存在一个满足穿孔输入条件却不满足误差严格界的输入。实数全序把最后的“不小于”写成 $\ge$。这里没有构造一串输入，只是逐个给定半径时使用存在量词。要证明不存在任何实数极限，还需对每个 $L\in\mathbb R$ 排除收敛，不能只排除某个指定 $L$。

**三个聚点实例。** 对任给 $p\in\mathbb R$，$p$ 是 $\mathbb R$ 的聚点，也是 $\mathbb R\setminus\{p\}$ 的聚点。证明：给定 $r>0$，实数2正，所以 $t=r/2>0$，乘回给 $t+t=r$；同加正数 $t$ 得 $t<r$。取 $x=p+t$，则 $x-p=t$，因此

$$
0<|x-p|=t=r/2<r.
$$

$x$ 是实数，且 $x\ne p$，所以同时属于这两个域。类似地，$0$ 是 $D=[0,\infty)=\{x\in\mathbb R:x\ge0\}$ 的聚点：给 $r>0$，取 $x=r/2>0$，它属于 $D$ 且满足所需距离。这里 $[0,\infty)$ 只是非负实数集的区间记号，$\infty$ 不是一个新实数。

**孤立输入的反例。** 若 $D=\{p\}$，任何 $x\in D$ 都有 $|x-p|=0$，不可能满足穿孔条件。因此 $p$ 不是 $D$ 的聚点。对任意函数 $f:\{p\}\to\mathbb R$、任意实数 $L$，裸的误差条件却都会成立：给 $\varepsilon>0$ 可取 $\delta=1$，因为没有穿孔输入能反驳其蕴含式。故我们只在已经核对聚点条件时使用“点极限”术语，避免把这种真空成立误当成唯一极限。FL1的实例和否定均已核。

### 2. 聚点提供唯一性所需的见证 {#funlimit-unique-examples}

**合并两个正半径。** 对实数 $u,v>0$ 定义

$$
\min(u,v)=\begin{cases}u,&u\le v,\\v,&v<u.\end{cases}
$$

全序保证两支互斥且穷尽。第一支输出正数 $u$，且不大于 $u,v$；第二支输出正数 $v$，也不大于二者。因此 $0<\min(u,v)\le u,v$。以后合并三个半径时用 $\min(u,\min(v,w))$，两次应用此结论就得到正性与三个上界，不调用任何无限取最小值的原则。

**命题 FL2：唯一性与直接例。** 固定 $f:D\to\mathbb R$ 及 $D$ 的聚点 $p$，点极限若存在则唯一。同一域上常数函数 $f(x)=C$ 的极限为 $C$；恒等规则 $f(x)=x$ 的极限为 $p$；对任意固定实数 $c,d$，仿射规则 $f(x)=cx+d$ 的极限为 $cp+d$。

**唯一性。** 假设同时趋于 $L$ 与 $M$，反设 $L\ne M$。绝对值零判据给 $s=|L-M|>0$；令 $h=s/3>0$。两份收敛条件分别给正半径 $\delta_L,\delta_M$，使其穿孔输入的误差各小于 $h$。令 $r=\min(\delta_L,\delta_M)>0$。

因为 $p$ 是 $D$ 的聚点，存在实际输入 $x\in D$ 满足 $0<|x-p|<r$。它同时在两份穿孔域中，因而 $|f(x)-L|<h$、$|f(x)-M|<h$。加法群及三角给

$$
\begin{aligned}
s&=|(L-f(x))+(f(x)-M)|\\
&\le |L-f(x)|+|f(x)-M|\\
&=|f(x)-L|+|f(x)-M|<2h.
\end{aligned}
$$

$h>0$，所以 $2h<3h=s$，最后等式由商乘回。得到 $s<s$ 的矛盾，故 $L=M$。聚点提供了这一个共同输入；没有它，仅有两份蕴含式不能取得矛盾。

**唯一性之后的记号。** 对满足聚点条件的域，若上述定义成立，写

$$
\lim_{\substack{x\to p\\x\in D}}f(x)=L.
$$

以下说“沿 $D$ 在 $p$ 有 $f\to L$”就是这个定义。它不要求 $p\in D$，不要求 $f(p)$ 有定义，也不要求函数某个值等于 $L$。

**常数与恒等。** 两规则都给域内每个输入唯一实数。常数规则对任给 $\varepsilon>0$ 取 $\delta=1$，所有穿孔输入都有 $|C-C|=0<\varepsilon$。恒等规则取 $\delta=\varepsilon>0$，所有 $0<|x-p|<\delta$ 的域内输入都有 $|f(x)-p|=|x-p|<\varepsilon$。

**仿射规则。** 实数运算保证它为 $D\to\mathbb R$ 的函数。若 $c=0$，规则恒等于 $d$，目标 $cp+d=d$，取 $\delta=1$ 即可。若 $c\ne0$，则 $|c|>0$。任给 $\varepsilon>0$，取 $\delta=\varepsilon/|c|>0$。对每个穿孔输入，分配与加法消去给

$$
\begin{aligned}
|(cx+d)-(cp+d)|
&=|c(x-p)|=|c|\,|x-p|\\
&<|c|\delta=\varepsilon.
\end{aligned}
$$

严格比较使用正数 $|c|$，乘回使用它非零。零系数分支没有借乘零保存严格号。FL2证毕。

### 3. 局部相同、局部有界与非零下界 {#funlimit-locality}

**命题 FL3。** 设 $p$ 为 $D$ 的聚点。

1. 若同域函数 $f,g:D\to\mathbb R$ 在某个正半径 $r$ 的穿孔输入域上相等，则对每个实数 $L$，沿 $D$ 在 $p$ 有 $f\to L$ 当且仅当 $g\to L$。
2. 若 $f\to A$，则存在 $r>0$，使所有 $x\in D^*(p,r)$ 都满足 $|f(x)|<1+|A|$。
3. 若 $g\to B$ 且 $B\ne0$，则存在 $r_0>0$，使所有 $x\in D^*(p,r_0)$ 都满足 $|g(x)|>|B|/2>0$。

**局部相同的两个方向。** 先设 $f\to L$。给 $\varepsilon>0$，取 $f$ 的正半径 $\delta_f$，令 $\delta=\min(r,\delta_f)>0$。任意 $x\in D^*(p,\delta)$ 同时满足局部相等与误差条件，故 $|g(x)-L|=|f(x)-L|<\varepsilon$。于是 $g\to L$。

反过来，若 $g\to L$，对给定正误差取其半径 $\delta_g$，令 $\delta=\min(r,\delta_g)>0$。每个此穿孔域输入都满足 $f(x)=g(x)$，因此 $|f(x)-L|=|g(x)-L|<\varepsilon$，即 $f\to L$。

**局部上界。** 对 $f\to A$ 用正误差1，取其正半径 $r$。任意 $x\in D^*(p,r)$ 满足

$$
|f(x)|=|(f(x)-A)+A|
\le|f(x)-A|+|A|<1+|A|.
$$

这是指定穿孔近域的界，不是对整个 $D$ 或被排除的中心值的界。

**非零下界。** 令 $h=|B|>0$、$t=h/2>0$。商乘回给 $2t=h$，所以 $h-t=t$。对误差 $t$ 取 $g$ 的正半径 $r_0$。每个 $x\in D^*(p,r_0)$ 都有 $|g(x)-B|<t$。反三角及绝对值基本界给

$$
h-|g(x)|\le\bigl|h-|g(x)|\bigr|
\le|B-g(x)|=|g(x)-B|<t.
$$

同加 $|g(x)|-t$ 得 $h-t<|g(x)|$，故 $|g(x)|>t=h/2>0$。绝对值零判据给这些输入处 $g(x)\ne0$。FL3证毕。

**只改中心值。** 若 $p\in D$，两个函数只在 $p$ 处的值可能不同，则它们在每个穿孔域中相等，故共享极限。具体在 $D=\mathbb R$ 上定义 $f(p)=1$、$x\ne p$ 时 $f(x)=0$，与零函数在每个穿孔域相同，所以沿 $\mathbb R$ 在 $p$ 的极限为零，而点值为一。若 $p\notin D$，就没有 $f(p)$ 可修改；点极限仍可有定义。本单元尚未用这些例子定义连续性。

### 4. 同域运算与商的实际定义域 {#funlimit-algebra}

**命题 FL4。** 设 $f,g:D\to\mathbb R$，$p$ 为 $D$ 聚点，且沿 $D$ 在 $p$ 有 $f\to A$、$g\to B$。则同域的和、常数倍、差、绝对值与积满足

$$
\begin{gathered}
f+g\to A+B,\qquad cf\to cA\quad(c\in\mathbb R),\\
f-g\to A-B,\qquad |f|\to|A|,\qquad fg\to AB.
\end{gathered}
$$

若 $B\ne0$，则实际商域

$$
D_g=\{x\in D:g(x)\ne0\}
$$

也以 $p$ 为聚点，并且 $q:D_g\to\mathbb R$、$q(x)=f(x)/g(x)$ 满足沿 $D_g$ 在 $p$ 的极限为 $A/B$。不要求 $g$ 在整个 $D$ 都非零。

**同域规则先合法。** 对每个 $x\in D$，$f(x),g(x)$ 都是唯一实数，已有加、乘、差、绝对值运算给唯一实数，故上述五种同域规则均为函数 $D\to\mathbb R$。商的域另行处理。

**和。** 给 $\varepsilon>0$，用正误差 $\varepsilon/2$ 分别取半径 $\delta_f,\delta_g>0$。令 $\delta=\min(\delta_f,\delta_g)>0$。每个 $x\in D^*(p,\delta)$ 同时满足两份误差，因而

$$
\begin{aligned}
|(f(x)+g(x))-(A+B)|
&=|(f(x)-A)+(g(x)-B)|\\
&\le|f(x)-A|+|g(x)-B|\\
&<\varepsilon/2+\varepsilon/2=\varepsilon.
\end{aligned}
$$

最后相等由 $2(\varepsilon/2)=\varepsilon$；严格相加用两次平移保序。

**常数倍与差。** 若 $c=0$，误差恒零，对任意正误差可取 $\delta=1$。若 $c\ne0$，$|c|>0$；以正误差 $\varepsilon/|c|$ 为 $f$ 取半径 $\delta>0$。所有相应穿孔输入满足

$$
|cf(x)-cA|=|c|\,|f(x)-A|
<|c|(\varepsilon/|c|)=\varepsilon.
$$

对于差，也可直接给误差半径：以 $\varepsilon/2$ 为 $f,g$ 取正半径并取其较小者。对每个相应穿孔输入，由差重排、三角及取反不变得

$$
\begin{aligned}
|(f(x)-g(x))-(A-B)|
&=|(f(x)-A)-(g(x)-B)|\\
&\le|f(x)-A|+|g(x)-B|<\varepsilon.
\end{aligned}
$$

**绝对值。** 给 $\varepsilon>0$，取 $f$ 对该误差的正半径 $\delta$。相应每个穿孔输入满足

$$
\bigl||f(x)|-|A|\bigr|\le|f(x)-A|<\varepsilon,
$$

故绝对值规则趋于 $|A|$。这些是函数的全称输入证明，没有把数列法则直接更名使用。

**积。** 先由FL3取正半径 $r$，使 $x\in D^*(p,r)$ 时 $|f(x)|<M=|A|+1$。这里 $M>0$。固定

$$
K=M+|B|+1>0,
$$

并有 $M\le K$、$|B|\le K$。给定 $\varepsilon>0$，正数 $2K$ 允许容差 $\eta=\varepsilon/(2K)>0$。为 $f,g$ 各取误差 $\eta$ 对应的半径 $\delta_f,\delta_g>0$，令

$$
\delta=\min(r,\min(\delta_f,\delta_g))>0.
$$

每个 $x\in D^*(p,\delta)$ 同时具备局部界及两份误差。分配并抵消给

$$
\begin{aligned}
f(x)(g(x)-B)+B(f(x)-A)
&=f(x)g(x)-f(x)B+Bf(x)-BA\\
&=f(x)g(x)-AB.
\end{aligned}
$$

因此三角及绝对乘积给

$$
|f(x)g(x)-AB|
\le |f(x)|\,|g(x)-B|+|B|\,|f(x)-A|.
$$

两个误差因子都非负，故第一项 $\le K|g(x)-B|<K\eta$，第二项 $\le K|f(x)-A|<K\eta$。每项的严格一步使用 $K>0$，所以 $A=0$、$B=0$ 或误差为零都不产生问题。由 $(2K)\eta=\varepsilon$ 和结合律，$2(K\eta)=\varepsilon$，非零系数2的方程唯一解给 $K\eta=\varepsilon/2$。两项相加得到 $|f(x)g(x)-AB|<\varepsilon$，证明乘积结论。

**商域的聚点。** 现在假设 $B\ne0$。FL3给 $r_0>0$，使 $D^*(p,r_0)$ 内全部 $g(x)\ne0$。故这些输入均属于 $D_g$，在 $D_g$ 上除法确有唯一实数输出。

任给 $r>0$，$s=\min(r,r_0)>0$。因为 $p$ 是 $D$ 聚点，存在 $x\in D$ 满足 $0<|x-p|<s$。它同时满足 $|x-p|<r_0$，故 $g(x)\ne0$、$x\in D_g$，还满足 $0<|x-p|<r$。这正是 $p$ 为 $D_g$ 聚点的全部量词。此步先于在商域谈极限。

**倒数误差。** 在 $D_g$ 上定义 $v(x)=1/g(x)$。令 $h=|B|>0$，FL3的同一 $r_0$ 可取为保证 $|g(x)|>h/2$ 的半径。对 $x\in D_g^*(p,r_0)$，$g(x)B\ne0$，逐乘回有

$$
\begin{aligned}
\left(\frac1{g(x)}-\frac1B\right)g(x)B
&=\left(\frac1{g(x)}\right)g(x)B
  -\left(\frac1B\right)Bg(x)\\
&=B-g(x).
\end{aligned}
$$

方程唯一性给倒数差等于 $(B-g(x))/(g(x)B)$，取绝对值并用绝对乘商得

$$
\left|v(x)-\frac1B\right|
=\frac{|g(x)-B|}{|g(x)|h}.
$$

固定 $d=(h/2)h>0$。上述近域内 $Q=|g(x)|h>d>0$。任给 $\varepsilon>0$，为 $g\to B$ 的正误差 $\varepsilon d$ 取半径 $r_1>0$，令 $\delta=\min(r_0,r_1)>0$。任意 $x\in D_g^*(p,\delta)$ 属于 $D$，并满足 $e=|g(x)-B|<\varepsilon d$ 和 $Q>d$。正倒数反序后乘非负 $e$，再除正数 $d$，得到

$$
\left|v(x)-\frac1B\right|=\frac eQ
\le\frac ed<\frac{\varepsilon d}{d}=\varepsilon.
$$

$e=0$ 时第一个比较为相等，后一个严格比较仍成立。因此沿 $D_g$ 在 $p$ 有 $v\to1/B$。

**限制域后应用同域乘积。** 定义 $u:D_g\to\mathbb R$ 为 $u(x)=f(x)$。对任意 $\varepsilon>0$，原来 $f\to A$ 的半径同样可用：$D_g$ 是 $D$ 子集，故所有 $D_g$ 中的穿孔输入满足原误差界。这样沿 $D_g$ 在 $p$ 有 $u\to A$。

$u,v$ 的域均为 $D_g$，且已证 $p$ 是该域聚点，故可用刚证明的乘积法则，得 $uv\to A(1/B)=A/B$。逐点 $u(x)v(x)=f(x)/g(x)=q(x)$，所以商结论成立。$B\ne0$ 保证目标 $A/B$ 也合法。FL4证毕。

**不要扩大非零结论。** 即使 $p\in D$，也可能 $g(p)=0$，于是 $p\notin D_g$，这不影响穿孔极限。若分母极限为零，也不能一概说商不收敛。例如 $D=\mathbb R$、$p=0$、$f(x)=g(x)=x$，两者都趋零；但实际商域为 $\mathbb R\setminus\{0\}$，其上商恒为一，所以沿该域的极限为一。这是定理条件不满足的例子，不是对定理的反例。

### 5. 课后题 {#funlimit-exercises}

#### 题1：域中有没有靠近的不同输入 {#funlimit-q01}

给 $p\in\mathbb R$，完整核 $\mathbb R$ 与 $\mathbb R\setminus\{p\}$ 都以 $p$ 为聚点；再核非负实数集以0为聚点。对 $D=\{p\}$，证明 $p$ 不是聚点，而任意 $f:D\to\mathbb R$ 与任意候选 $L\in\mathbb R$ 都满足不附聚点条件的裸误差蕴含。解释非空域为何不够。[完整解答](#funlimit-a01)

#### 题2：完整否定与唯一性的共同输入 {#funlimit-q02}

给 $f:D\to\mathbb R$、$D$ 的聚点 $p$ 及固定实数 $L$，写出点极限定义及完整否定，区分固定 $L$ 失败与无任何实数极限。另假设同一函数沿 $D$ 在 $p$ 同时趋于 $L$ 与实数 $M$，用两个正半径的较小者及聚点见证证明 $L=M$，不可只说“选足够近的输入”。[完整解答](#funlimit-a02)

#### 题3：不借连续性证明基本例 {#funlimit-q03}

设 $D\subseteq\mathbb R$，$p$ 为其聚点，$C,c,d\in\mathbb R$。直接从定义证明同域常数规则 $C$、恒等规则 $x$、仿射规则 $cx+d$ 的极限分别为 $C,p,cp+d$。先核函数合法性，仿射规则单列 $c=0$，其余情况先核分母正。[完整解答](#funlimit-a03)

#### 题4：只改中心值和局部相等 {#funlimit-q04}

给同域 $f,g:D\to\mathbb R$ 与 $D$ 聚点 $p$，假设某个 $r>0$ 的穿孔域内二者相等。对任给实数 $L$，证明共享该极限的两个方向。另在 $\mathbb R$ 上写出 $f(p)=1$、其他值为零的完整规则，证明点极限为零。若 $p\notin D$，解释为什么不能讨论修改 $f(p)$。[完整解答](#funlimit-a04)

#### 题5：局部上界与非零下界 {#funlimit-q05}

设沿域 $D$ 在其聚点 $p$ 有 $f\to A$、$g\to B\ne0$。从误差定义证明某个穿孔近域内 $|f(x)|<1+|A|$，以及另一穿孔近域内 $|g(x)|>|B|/2>0$。逐步写出反三角后的移项，并解释为何这不证明全域有界或全域分母非零。[完整解答](#funlimit-a05)

#### 题6：和与积的共同半径 {#funlimit-q06}

设 $f,g:D\to\mathbb R$、$p$ 为 $D$ 聚点，且 $f\to A$、$g\to B$。完整证明和与积的极限。乘积须先取得 $f$ 的局部界，再合并局部界半径与两份误差半径；逐分配核误差式，说明 $B=0$ 或某误差为零时为何仍得到严格结论。[完整解答](#funlimit-a06)

#### 题7：实际商域先要有聚点 {#funlimit-q07}

设同域 $f,g:D\to\mathbb R$ 沿 $D$ 在其聚点 $p$ 分别趋 $A,B$，且 $B\ne0$。定义 $D_g=\{x\in D:g(x)\ne0\}$，证明 $p$ 也是 $D_g$ 聚点。然后从乘回开始完整证明其上倒数趋 $1/B$，再核 $f$ 限制到 $D_g$ 的极限并推出商趋 $A/B$。覆盖零误差，说明是否需要 $p\in D_g$。[完整解答](#funlimit-a07)

#### 题8：平方差商与零分母极限 {#funlimit-q08}

固定实数 $p$，在 $D=\mathbb R\setminus\{p\}$ 上定义 $q(x)=(x^2-p^2)/(x-p)$。核域及聚点，逐分配与乘回证明 $q(x)=x+p$，直接用误差定义证明沿 $D$ 在 $p$ 的极限为 $2p$。再对 $f(x)=g(x)=x$、$D=\mathbb R$、$p=0$，核两极限及实际商域上的商极限，说明“分母趋零必发散”错在哪里。[完整解答](#funlimit-a08)

### 6. 来源与接续边界 {#funlimit-source-boundary}

标准聚点与点极限条件、公开固定版本的实际读取范围及许可记录见[本批来源核查](#real-cauchy-function-limits-sources)。所有估计、穿孔见证、题目与解答在本书中独立展开。仅用有限个正半径的较小者合并条件；没有用每个半径任选一个实数输入构造无限序列，也没有把自然数最小元用于任意实数候选集。

后续可在域与聚点条件明确后定义连续性。本单元尚未证明函数极限的序列刻画、复合极限、左右极限或任何微分积分结论，不能把这些内容作为这里的隐含先修。
