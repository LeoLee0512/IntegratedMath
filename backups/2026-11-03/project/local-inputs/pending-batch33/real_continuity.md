## 基础单元 B4.7 实函数的连续性 {#continuity-unit}

本单元主归第18部分“实函数”中第146章“一元函数”的26A15，函数域与复合接口交叉97I20。我们在实数域内直接证明逐点连续性、限制、运算与复合；不把这些结论计为整章或整个分析模块完成。

**精确先修。** 使用[集合与条件子集](#fun-sets)、[函数定义](#fun-definition)、[复合及其域条件](#fc-composition)、[实数全序](#cut-order-embedding)、[加法群](#cutgroup-laws)、[差与相反数](#cutgroup-negation-subtraction)、[平移比较](#cutgroup-translation)、[乘法符号](#cutsigned-signs)、[乘法结合](#cutsigned-associative)、[零积与有理乘法相容](#cutsigned-rational-zero)、[有理加法相容](#cutadd-rational)、[分配及差乘](#cutring-distributive)、[乘法比较](#cutring-multiplication-order)、[合法除法与乘回](#cutdiv-definition)、[非零系数方程](#cutdiv-equations)、[正除法与倒数比较](#cutdiv-order)、[绝对值基本界](#realabs-definition-bounds)、[绝对乘商、三角与反三角](#realabs-products-triangle)、[聚点和穿孔极限](#funlimit-domain-definition)、[极限唯一与正半径较小值](#funlimit-unique-examples)。以下 $D,E$ 是实数子集，中心、误差、半径及函数值均为实数；实数运算沿用已经构造的运算。

### 1. 连续性要求中心属于定义域 {#continuity-definition}

**定义。** 给函数 $f:D\to\mathbb R$，并给 $c\in D$。若

$$
\begin{gathered}
\forall\varepsilon>0\ \exists\delta>0\ \forall x\in D,\\
|x-c|<\delta\Longrightarrow |f(x)-f(c)|<\varepsilon,
\end{gathered}
$$

则称 $f$ 在 $c$ **连续**。若它在每个 $c\in D$ 都连续，称 $f$ 在 $D$ 上连续。$\varepsilon,\delta$ 为实数；半径先于随后任取的 $x$ 选定，可以依赖 $f,D,c,\varepsilon$，不要求同一半径对所有中心都适用。

这里没有条件 $0<|x-c|$。中心输入 $x=c$ 也在检查范围内，只是其输出误差为 $|f(c)-f(c)|=0$。中心必须在域内，否则 $f(c)$ 未定义，不能把此式当成连续性定义。

**命题 C1。** 在上述域与中心条件下：

1. $f$ 在 $c$ 不连续的准确否定是

$$
\begin{gathered}
\exists\varepsilon_0>0\ \forall\delta>0\ \exists x\in D,\\
|x-c|<\delta\quad\text{且}\quad |f(x)-f(c)|\ge\varepsilon_0.
\end{gathered}
$$

2. 如果 $c$ 不是 $D$ 的聚点，则任意 $f:D\to\mathbb R$ 都在 $c$ 连续。
3. 如果 $c$ 是 $D$ 的聚点，则 $f$ 在 $c$ 连续，当且仅当沿 $D$ 在 $c$ 的点极限等于 $f(c)$。
4. 域 $D$ 上的常数、恒等和仿射规则都在每个域内点连续。

**完整否定。** 否定“每个正误差都有可用正半径”，得到某个正误差对所有正半径都失败；否定半径内每个域内输入都满足误差条件，得到一个域内坏输入。实数全序把失败的严格界写成 $\ge\varepsilon_0$。这个坏输入必有 $x\ne c$：如果 $x=c$，输出误差为零，与 $\varepsilon_0>0$ 矛盾。但这只是坏输入的结论，不是在连续定义中删去中心。

**孤立点。** $c$ 不是聚点，表示存在 $r>0$，找不到 $x\in D$ 满足 $0<|x-c|<r$。给任意 $\varepsilon>0$，取 $\delta=r$。若 $x\in D$ 且 $|x-c|<\delta$，它不可能同时有 $|x-c|>0$；绝对值非负，所以 $|x-c|=0$，零判据给 $x=c$。于是 $|f(x)-f(c)|=0<\varepsilon$，证明连续。称这样的域内点为**孤立点**。这里没有给孤立点定义唯一的穿孔极限；连续性直接使用已有中心值。

**聚点处的相容。** 先设 $f$ 在 $c$ 连续。对每个正误差，连续性的半径对所有近域输入有效，当然对其中 $0<|x-c|<\delta$ 的输入有效。因此沿 $D$ 在 $c$ 的点极限为 $f(c)$。

反过来，假设 $c$ 是聚点且此点极限为 $f(c)$。给 $\varepsilon>0$，取点极限的半径 $\delta>0$。任取 $x\in D$ 且 $|x-c|<\delta$：若 $x=c$，误差为零；若 $x\ne c$，绝对值零判据给 $0<|x-c|<\delta$，点极限条件给误差小于 $\varepsilon$。两支覆盖全部输入，故连续。此命题同时要求 $c\in D$，不能把域外聚点的极限写成未定义的 $f(c)$。

**基本例的直接证明。** 常数规则 $f(x)=C$ 对每个输入给唯一实数。任给中心 $c\in D$ 和误差 $\varepsilon>0$，取 $\delta=1$，所有相关误差均为 $|C-C|=0<\varepsilon$。

恒等规则 $f(x)=x$ 合法，因为 $D\subseteq\mathbb R$。取 $\delta=\varepsilon>0$，则 $|x-c|<\delta$ 时 $|f(x)-f(c)|=|x-c|<\varepsilon$。

固定实数 $\alpha,\beta$，仿射规则 $f(x)=\alpha x+\beta$ 由实数运算闭合给全函数。若 $\alpha=0$，规则为常数 $\beta$，可取 $\delta=1$。若 $\alpha\ne0$，$|\alpha|>0$，取 $\delta=\varepsilon/|\alpha|>0$。任意 $x\in D$ 且 $|x-c|<\delta$ 满足

$$
\begin{aligned}
|f(x)-f(c)|
&=|\alpha x+\beta-(\alpha c+\beta)|\\
&=|\alpha(x-c)|=|\alpha|\,|x-c|\\
&<|\alpha|\delta=\varepsilon.
\end{aligned}
$$

分配与加法群给第二行，绝对乘积和正因子比较给严格界，最后由合法商乘回。所有证明都包括 $x=c$。C1证毕。

### 2. 局部、限制和函数值的符号 {#continuity-local-restriction}

**命题 C2。** 给 $f:D\to\mathbb R$ 与 $c\in D$。

1. 若 $g:D\to\mathbb R$，并存在 $r>0$ 使 $x\in D$、$|x-c|<r$ 时 $f(x)=g(x)$，则二者在 $c$ 的连续性等价。
2. 若 $E\subseteq D$ 且 $c\in E$，$f$ 在 $c$ 连续，则限制函数 $f|_E:E\to\mathbb R$、$f|_E(x)=f(x)$ 在 $c$ 连续。
3. 若 $f$ 在 $c$ 连续，则某个正半径内的全部域内输入满足 $|f(x)|<1+|f(c)|$。给定实数 $y$，若 $f(c)<y$，则某个正半径内全部域内输入有 $f(x)<y$；若 $f(c)>y$，则相应近域有 $f(x)>y$。
4. 若 $f$ 在 $c$ 连续且 $f(c)\ne0$，则某个正半径内全部域内输入有 $|f(x)|>|f(c)|/2>0$。

**含中心的局部相等。** 将 $x=c$ 代入相等条件，因为 $0=|c-c|<r$，先得到 $f(c)=g(c)$。若 $f$ 连续，给 $\varepsilon>0$ 取其半径 $\delta_f>0$，令 $\delta=\min(r,\delta_f)>0$。对任意 $x\in D$ 且 $|x-c|<\delta$，

$$
|g(x)-g(c)|=|f(x)-f(c)|<\varepsilon.
$$

所以 $g$ 连续。反过来，若 $g$ 连续，对给定正误差取其半径 $\delta_g$，用 $\min(r,\delta_g)>0$；同一局部相等条件与中心相等给 $|f(x)-f(c)|=|g(x)-g(c)|<\varepsilon$，所以 $f$ 连续。较小值的正性及不大于各输入的性质已在FL2按全序两支证明。

**限制。** 每个 $x\in E$ 属于 $D$，所以规则 $f|_E(x)=f(x)$ 给唯一实数，确为所声明的函数；$c\in E$ 保证其中心值存在且等于 $f(c)$。给 $\varepsilon>0$，取原连续性的半径 $\delta$。任何 $x\in E$ 且 $|x-c|<\delta$ 都是原定义允许的输入，因此

$$
\bigl|(f|_E)(x)-(f|_E)(c)\bigr|=|f(x)-f(c)|<\varepsilon.
$$

这里 $f|_E(x)$ 表示限制函数在 $x$ 的值。新域不必在 $c$ 聚集，证明仍然成立。

**局部上界。** 对正误差1取 $r>0$。所有 $x\in D$ 且 $|x-c|<r$ 都满足

$$
|f(x)|=|(f(x)-f(c))+f(c)|
\le|f(x)-f(c)|+|f(c)|<1+|f(c)|.
$$

这次近域包含中心，但不声称远处输入也满足此界。

**局部目标间隔。** 若 $f(c)<y$，令 $t=(y-f(c))/2>0$；乘回给 $y=f(c)+2t$。用误差 $t$ 取得半径 $r>0$。每个此近域输入满足

$$
f(x)-f(c)\le|f(x)-f(c)|<t,
$$

故 $f(x)<f(c)+t<f(c)+2t=y$。中间严格比较因 $t>0$。

若 $f(c)>y$，令 $t=(f(c)-y)/2>0$，所以 $f(c)=y+2t$。对误差 $t$ 取半径，近域输入满足 $f(c)-f(x)\le|f(x)-f(c)|<t$，平移得

$$
f(x)>f(c)-t=y+t>y.
$$

两种比较都只对实际域内输入声明，端点处的相对域也适用。

**非零的局部下界。** 设 $h=|f(c)|>0$，$t=h/2>0$，则 $h-t=t$。对误差 $t$ 取正半径 $r$。近域输入由反三角得

$$
h-|f(x)|\le\bigl|h-|f(x)|\bigr|
\le |f(c)-f(x)|<t.
$$

同加 $|f(x)|-t$，得到 $h-t<|f(x)|$，即 $|f(x)|>t=h/2>0$。C2证毕。

**两个不能倒用的结论。** 在 $D=\mathbb R$ 上定义 $F(0)=1$、$x\ne0$ 时 $F(x)=0$，并令 $G$ 恒为零。二者在中心0的每个穿孔域相等，但 $G$ 连续而 $F$ 在0不连续：取 $\varepsilon_0=1/2$，任给 $\delta>0$，输入 $x=\delta/2>0$ 满足 $|x|<\delta$，却有 $|F(x)-F(0)|=1\ge1/2$。所以含中心的局部相等不能改成只在穿孔域相等。

另一方面，将 $F$ 限制到 $E=\{0\}$，唯一输入就是中心，输出误差恒零，故限制函数连续。限制连续不能反推原域连续。

### 3. 同域四则与商的实际定义域 {#continuity-algebra}

**命题 C3。** 设 $f,g:D\to\mathbb R$ 都在 $c\in D$ 连续，$\lambda\in\mathbb R$ 固定。逐点和、差、积、常数倍和绝对值规则

$$
f+g,\quad f-g,\quad fg,\quad\lambda f,\quad |f|
$$

都是 $D\to\mathbb R$ 的函数，且都在 $c$ 连续。若 $g(c)\ne0$，则令

$$
D_g=\{x\in D:g(x)\ne0\},\qquad
q:D_g\to\mathbb R,\quad q(x)=\frac{f(x)}{g(x)},
$$

有 $c\in D_g$，并且 $q$ 在 $c$ 连续。不要求分母在原域 $D$ 上处处非零。

**同域函数的合法性。** 每个域内输入给唯一的实数 $f(x),g(x)$，实数加、减、乘及绝对值给唯一实数，因此五种规则确为同域全函数。它们在中心的值分别按同一规则计算，不能另指定一个不同目标。

**和与差。** 任给 $\varepsilon>0$，为两个函数各取误差 $\varepsilon/2>0$ 的正半径 $r_f,r_g$，令 $\delta=\min(r_f,r_g)>0$。任何 $x\in D$ 且 $|x-c|<\delta$ 都满足两份误差。加法群与三角分别给

$$
\begin{aligned}
|(f(x)+g(x))-(f(c)+g(c))|
&\le |f(x)-f(c)|+|g(x)-g(c)|<\varepsilon,\\
|(f(x)-g(x))-(f(c)-g(c))|
&\le |f(x)-f(c)|+|g(x)-g(c)|<\varepsilon.
\end{aligned}
$$

第一行把误差重排为两个差的和；第二行重排为两个差的差，再用绝对值取反不变。两份严格界相加为 $\varepsilon/2+\varepsilon/2=\varepsilon$，等式来自系数2的乘回。因此两种规则在 $c$ 连续。

**常数倍。** 若 $\lambda=0$，所有误差为零，任给正误差取 $\delta=1$。若 $\lambda\ne0$，则 $|\lambda|>0$；为 $f$ 的正误差 $\varepsilon/|\lambda|$ 取半径 $\delta>0$。相关输入满足

$$
|\lambda f(x)-\lambda f(c)|
=|\lambda|\,|f(x)-f(c)|
<|\lambda|(\varepsilon/|\lambda|)=\varepsilon.
$$

严格步使用正因子，乘回使用非零分母。此论证同时包括负常数。

**绝对值。** 给 $\varepsilon>0$，取 $f$ 对同一误差的半径。反三角给所有相关输入

$$
\bigl||f(x)|-|f(c)|\bigr|\le|f(x)-f(c)|<\varepsilon.
$$

输出 $|f(c)|$ 正是绝对值函数在中心的值，所以证明连续。

**积。** C2给正半径 $r$，使 $|x-c|<r$ 的域内输入满足 $|f(x)|<M=|f(c)|+1$。这里 $M>0$。固定

$$
K=M+|g(c)|+1>0,
$$

且 $M\le K$、$|g(c)|\le K$。给定 $\varepsilon>0$，令 $\eta=\varepsilon/(2K)>0$，分别用两个函数在 $c$ 连续取得误差 $\eta$ 的正半径 $r_f,r_g$。令 $\delta=\min(r,\min(r_f,r_g))$。内外两次较小值均为正，且最终半径不大于三个半径。

任取 $x\in D$ 且 $|x-c|<\delta$，局部界和两误差同时成立。逐分配、交换与抵消给

$$
\begin{aligned}
&f(x)(g(x)-g(c))+g(c)(f(x)-f(c))\\
&\quad=f(x)g(x)-f(x)g(c)+g(c)f(x)-g(c)f(c)\\
&\quad=f(x)g(x)-f(c)g(c).
\end{aligned}
$$

因此

$$
|f(x)g(x)-f(c)g(c)|
\le|f(x)|\,|g(x)-g(c)|+|g(c)|\,|f(x)-f(c)|.
$$

两项先分别弱估至 $K|g(x)-g(c)|$、$K|f(x)-f(c)|$，再由 $K>0$ 各严格小于 $K\eta$。由 $(2K)\eta=\varepsilon$ 得 $2(K\eta)=\varepsilon$，系数2非零的方程唯一性给 $K\eta=\varepsilon/2$。故总误差小于 $\varepsilon$。中心值或误差为零都不影响证明，因为弱比较之后的严格步乘的是正数 $K$。

**商的中心与域。** 现在假设 $g(c)\ne0$。由 $c\in D$ 得 $c\in D_g$，因此商在中心有值 $q(c)=f(c)/g(c)$。每个 $D_g$ 输入也都有合法的非零分母，定义给全函数。我们不需要 $c$ 为聚点，孤立点同样在连续性定义范围内。

先证明 $v:D_g\to\mathbb R$、$v(x)=1/g(x)$ 在 $c$ 连续。令 $h=|g(c)|>0$。C2给正半径 $r_0$，保证原域近输入有 $|g(x)|>h/2>0$。对其中的 $D_g$ 输入，$g(x)g(c)\ne0$，并有

$$
\begin{aligned}
&\left(\frac1{g(x)}-\frac1{g(c)}\right)g(x)g(c)\\
&\quad=\left[\left(\frac1{g(x)}\right)g(x)\right]g(c)
 -\left[\left(\frac1{g(c)}\right)g(c)\right]g(x)\\
&\quad=g(c)-g(x).
\end{aligned}
$$

首行使用分配、交换与结合。非零系数方程唯一性给倒数差等于 $(g(c)-g(x))/(g(x)g(c))$，绝对乘商于是给

$$
|v(x)-v(c)|=\frac{|g(x)-g(c)|}{|g(x)|h}.
$$

固定 $d=(h/2)h>0$，近域内 $Q=|g(x)|h>d>0$。给 $\varepsilon>0$，用 $g$ 连续性对正误差 $\varepsilon d$ 取半径 $r_1>0$，令 $\delta=\min(r_0,r_1)>0$。任意 $x\in D_g$ 且 $|x-c|<\delta$ 满足 $e=|g(x)-g(c)|<\varepsilon d$ 及分母下界。正倒数反序后乘非负 $e$，再除正数 $d$，得

$$
|v(x)-v(c)|=\frac eQ\le\frac ed
<\frac{\varepsilon d}{d}=\varepsilon.
$$

$e=0$ 时第一比较为相等，后一步仍严格；特别 $x=c$ 已被覆盖。故 $v$ 连续。

C2限制结论给 $u=f|_{D_g}$ 在 $c$ 连续，因为 $D_g\subseteq D$ 且 $c\in D_g$。刚证乘积规律可用于同域 $u,v$，得 $uv$ 在 $c$ 连续；逐点 $u(x)v(x)=f(x)/g(x)=q(x)$，故商连续。C3证毕。

例如 $g(x)=x$ 在实数域上连续，中心 $c=1$ 满足 $g(c)\ne0$。实际倒数域是 $\mathbb R\setminus\{0\}$，倒数在1连续；原域远处存在零点0并不妨碍结论。与穿孔点极限不同，连续性结论必以商的中心值存在为前提。

### 4. 复合的两级误差选择 {#continuity-composition}

**命题 C4。** 设 $D,E\subseteq\mathbb R$，$g:D\to E$、$f:E\to\mathbb R$，并给 $c\in D$。若 $g$ 在 $c$ 连续，且 $f$ 在 $g(c)$ 连续，则复合 $f\circ g:D\to\mathbb R$ 在 $c$ 连续。

这里说 $g:D\to E$ 连续，是指把其输出视为实数后，函数 $D\to\mathbb R$ 满足连续性的误差条件；原目标 $E$ 的成员要求仍用于保证复合合法。对每个 $x\in D$，$g(x)\in E$，所以 $f(g(x))$ 有唯一实数值，且 $g(c)\in E$ 使外层中心值存在。

**证明。** 任给实数 $\varepsilon>0$。先用外层函数在 $g(c)$ 连续，取 $\eta>0$，使每个 $y\in E$ 满足

$$
|y-g(c)|<\eta
\Longrightarrow |f(y)-f(g(c))|<\varepsilon.
$$

再用内层函数在 $c$ 连续，针对这个正误差 $\eta$ 取 $\delta>0$，使所有 $x\in D$ 有

$$
|x-c|<\delta\Longrightarrow |g(x)-g(c)|<\eta.
$$

任取这样的 $x$，先核 $y=g(x)\in E$，再代入外层误差条件，得到

$$
|(f\circ g)(x)-(f\circ g)(c)|
=|f(g(x))-f(g(c))|<\varepsilon.
$$

半径 $\delta$ 在任取 $x$ 之前已经确定，因此正是复合连续性的全部量词。证毕。

若 $g(x)=g(c)$，外层输入恰等于外层中心，仍满足 $|g(x)-g(c)|=0<\eta$，其输出误差为零。常数内函数完全允许。这里使用包含中心的连续条件，不是未经条件核对的穿孔极限复合法则，也没有构造无限选点序列。

### 5. 课后题 {#continuity-exercises}

#### 题1：中心、完整否定与孤立点 {#continuity-q01}

给 $f:D\to\mathbb R$ 和 $c\in D$，写出连续定义及其完整否定，说明坏输入为什么自动不同于中心。若 $c$ 不是 $D$ 的聚点，证明任意这样的 $f$ 都在 $c$ 连续，给出适用于每个正误差的半径；解释域外点为何不能直接放入此定义。[完整解答](#continuity-a01)

#### 题2：聚点极限何时等于连续性 {#continuity-q02}

设 $c\in D$ 又是 $D$ 的聚点。对 $f:D\to\mathbb R$，证明它在 $c$ 连续当且仅当沿 $D$ 的点极限为 $f(c)$，反向分清中心与非中心输入。再对实数域上的 $F(0)=1$、其他输入值为0的函数，直接证明在0不连续，并说明它的点极限与中心值。[完整解答](#continuity-a02)

#### 题3：限制的方向不能倒转 {#continuity-q03}

设 $E\subseteq D\subseteq\mathbb R$、$c\in E$，函数 $f:D\to\mathbb R$ 在 $c$ 连续。完整定义限制函数并证明它在 $c$ 连续，不假设 $c$ 是 $E$ 聚点。用题2的函数和 $E=\{0\}$ 说明反向错误，分别核两种连续性结论。[完整解答](#continuity-a03)

#### 题4：局部相等与函数值间隔 {#continuity-q04}

给同域 $f,g:D\to\mathbb R$ 与 $c\in D$。若某个含中心近域内两函数相等，证明其在 $c$ 连续的两个方向，并说明只要求穿孔相等为何不够。另设 $f$ 在 $c$ 连续、$y\in\mathbb R$，分别从 $f(c)<y$ 和 $f(c)>y$ 证明存在保持相应严格比较的正半径。[完整解答](#continuity-a04)

#### 题5：同域运算的全部误差条件 {#continuity-q05}

设 $f,g:D\to\mathbb R$ 在 $c\in D$ 连续，固定 $\lambda\in\mathbb R$。证明和、差、常数倍及积的规则合法并在 $c$ 连续；常数零单列，积先取局部界，再合并三个正半径。明确零中心值或零误差时哪些步骤只用弱比较。[完整解答](#continuity-a05)

#### 题6：实际商域中的连续性 {#continuity-q06}

设 $f,g:D\to\mathbb R$ 在 $c\in D$ 连续，且 $g(c)\ne0$。定义 $D_g$ 并核 $c\in D_g$，从反三角近域下界与乘回恒等式开始，完整证明 $1/g$ 在此域于 $c$ 连续，再证明 $f/g$ 连续。覆盖误差零，说明为何无需原域处处非零，并核 $g(x)=x,c=1$ 的例子。[完整解答](#continuity-a06)

#### 题7：复合允许内层等于中心值 {#continuity-q07}

设 $D,E\subseteq\mathbb R$，$g:D\to E$、$f:E\to\mathbb R$，$c\in D$，且两函数分别在 $c$ 与 $g(c)$ 连续。完整证明复合连续，按外层误差、内层误差、任意输入的顺序选量。另取某个 $e\in E$ 令 $g(x)=e$，解释它不违反证明中的任何条件。[完整解答](#continuity-a07)

#### 题8：只用有限个已证操作构造函数 {#continuity-q08}

在 $\mathbb R$ 上定义

$$
H(x)=\frac{x^2+1}{|x|+1},\qquad x^2=xx.
$$

先核每个分母非零，再用已证连续性规则证明 $H$ 在每个实数中心连续。须说明恒等、常数、平方、绝对值、和与实际商域各自的作用，不引用一般多项式或有理函数连续性定理。[完整解答](#continuity-a08)

### 6. 来源与接续 {#continuity-source-boundary}

标准定义、条件及公开教材的实际读取范围见[本批来源记录](#real-continuity-intermediate-sources)。本单元逐条给出直接误差证明；未采用来源中的逆序列刻画或以它证明复合。连续性允许中心输入，下一单元将用其局部符号性质与已经构造的实数上确界证明介值定理，不以连笔图像替代证明。
