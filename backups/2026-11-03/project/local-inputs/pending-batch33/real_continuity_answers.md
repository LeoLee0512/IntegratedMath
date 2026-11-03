## B4.7 实函数的连续性：完整解答 {#continuity-answers}

以下所有集合都是实数子集，误差、半径、中心与函数值均为实数。连续性在域内点定义，输入条件是 $|x-c|<\delta$，包括中心；不额外假设中心为聚点。合并有限个正半径时用已按全序证明为正的二元较小值。

### 题1：中心、完整否定与孤立点 {#continuity-a01}

[返回题目](#continuity-q01)。给 $f:D\to\mathbb R$、$c\in D$，连续性为

$$
\begin{gathered}
\forall\varepsilon>0\ \exists\delta>0\ \forall x\in D,\\
|x-c|<\delta\Longrightarrow |f(x)-f(c)|<\varepsilon.
\end{gathered}
$$

先给正误差，选正半径，再检查全部域内近输入；半径不能依赖后来才任取的 $x$。否定这一量词次序，得到

$$
\begin{gathered}
\exists\varepsilon_0>0\ \forall\delta>0\ \exists x\in D,\\
|x-c|<\delta\quad\text{且}\quad |f(x)-f(c)|\ge\varepsilon_0.
\end{gathered}
$$

最后的弱不等式来自实数全序中“不小于”的刻画。若坏输入恰为 $c$，输出误差为 $|f(c)-f(c)|=0$，不可能大于或等于正数 $\varepsilon_0$，所以它自动不同于中心。但正常的连续定义仍检查中心输入，只是这个输入总符合要求。

若 $c$ 不是 $D$ 聚点，聚点定义的否定给某个 $r>0$，使不存在 $x\in D$ 满足 $0<|x-c|<r$。给任意 $\varepsilon>0$，选择同一个半径 $\delta=r$。任取 $x\in D$ 且 $|x-c|<r$。绝对值非负；如果它正，就成为被排除的穿孔输入。因此 $|x-c|=0$，零判据与差的零判据给 $x=c$。于是

$$
|f(x)-f(c)|=0<\varepsilon.
$$

所以任意域内孤立点处，函数都连续。证明不依赖 $f(c)$ 的具体值。

若 $c\notin D$，原函数的求值规则不接受输入 $c$，表达式 $f(c)$ 没有定义，因而不能直接用这个连续性条件。可以在域外聚点讨论已有定义的穿孔极限，但那是另一项条件，不自动产生中心函数值。

### 题2：聚点极限何时等于连续性 {#continuity-a02}

[返回题目](#continuity-q02)。设 $c\in D$ 又是 $D$ 的聚点。

若 $f$ 在 $c$ 连续，任给 $\varepsilon>0$，存在 $\delta>0$ 使每个 $x\in D$、$|x-c|<\delta$ 的输出误差小于 $\varepsilon$。特别地，满足更强输入条件 $0<|x-c|<\delta$ 的点也符合，所以沿 $D$ 在 $c$ 的点极限为 $f(c)$。聚点假设使这个点极限术语合法，唯一性已由FL2证明。

反过来，若沿 $D$ 在 $c$ 的点极限为 $f(c)$，给 $\varepsilon>0$ 取其正半径 $\delta$。任取 $x\in D$ 且 $|x-c|<\delta$：若 $x=c$，误差 $|f(x)-f(c)|=0<\varepsilon$；若 $x\ne c$，绝对值零判据给 $0<|x-c|<\delta$，点极限条件给误差小于 $\varepsilon$。两支穷尽，所以 $f$ 在 $c$ 连续。

再定义 $F:\mathbb R\to\mathbb R$ 为

$$
F(x)=\begin{cases}1,&x=0,\\0,&x\ne0.\end{cases}
$$

两条件互斥且穷尽，每个输入给唯一实数，所以函数全定义。取失败误差 $\varepsilon_0=1/2>0$。任给 $\delta>0$，令 $x=\delta/2$；实数2正，商乘回给 $0<x<\delta$。因此 $x\ne0$、$|x|<\delta$，但

$$
|F(x)-F(0)|=|0-1|=1\ge1/2.
$$

这满足不连续的完整否定，故 $F$ 在0不连续。

另一方面，0是实数域的聚点。任给 $\varepsilon>0$，对点极限可取 $\delta=1$；任意 $0<|x|<1$ 都满足 $x\ne0$，所以 $|F(x)-0|=0<\varepsilon$。故点极限为0，而中心值为1。相容定理要求两者相等，这个例子恰好不满足。

### 题3：限制的方向不能倒转 {#continuity-a03}

[返回题目](#continuity-q03)。设 $E\subseteq D\subseteq\mathbb R$、$c\in E$，且 $f:D\to\mathbb R$ 在 $c$ 连续。定义 $u:E\to\mathbb R$，$u(x)=f(x)$。每个 $E$ 输入都属于 $D$，原函数给唯一实数，所以限制规则全定义。特别 $u(c)=f(c)$。

任给 $\varepsilon>0$，由 $f$ 连续取 $\delta>0$，保证全部 $x\in D$、$|x-c|<\delta$ 的输出误差小于 $\varepsilon$。任取 $x\in E$ 满足同一距离条件，它也属于 $D$，因此

$$
|u(x)-u(c)|=|f(x)-f(c)|<\varepsilon.
$$

所以限制函数在 $c$ 连续。这只使用集合包含，没有用 $c$ 为 $E$ 聚点；即使 $E=\{c\}$ 也有效。

为反驳逆命题，仍在实数域上定义 $F(0)=1$、其余值为零。对 $\varepsilon_0=1/2$ 和任意 $\delta>0$，取 $x=\delta/2$，则 $0<|x|<\delta$，而 $|F(x)-F(0)|=1\ge1/2$，故原函数在0不连续。

限制到 $E=\{0\}$ 得 $u(0)=1$。任给 $\varepsilon>0$，取 $\delta=1$，任意 $x\in E$ 必有 $x=0$，所以 $|u(x)-u(0)|=0<\varepsilon$。因此限制函数在0连续。两个结论使用不同的输入域；不能凭较小域的检验推断较大域全部近输入也符合。

### 题4：局部相等与函数值间隔 {#continuity-a04}

[返回题目](#continuity-q04)。设存在 $r>0$，使 $x\in D$ 且 $|x-c|<r$ 时 $f(x)=g(x)$。因为 $c\in D$、$|c-c|=0<r$，首先得到 $f(c)=g(c)$。

若 $f$ 在 $c$ 连续，给任意 $\varepsilon>0$，取其半径 $\delta_f>0$，令 $\delta=\min(r,\delta_f)>0$。任意 $x\in D$、$|x-c|<\delta$ 同时属于局部相等范围和 $f$ 的误差范围，所以

$$
|g(x)-g(c)|=|f(x)-f(c)|<\varepsilon.
$$

故 $g$ 连续。反向若 $g$ 连续，给正误差取半径 $\delta_g>0$，令 $\delta'=\min(r,\delta_g)>0$；对全部相关域内输入有 $|f(x)-f(c)|=|g(x)-g(c)|<\varepsilon$，故 $f$ 连续。两次较小值等于一个正输入，因此不为零且同时不大于两个半径。

只要求穿孔相等时，中心值相等没有依据。取 $D=\mathbb R,c=0$，$F(0)=1$、其余0，另取 $G$ 恒零。两者在所有非零输入处相等。$G$ 对任意正误差可取半径1，误差恒零，故连续。$F$ 则对 $\varepsilon_0=1/2$、任意 $\delta>0$ 取 $x=\delta/2$，其近输入输出差为1，故不连续。这给穿孔相等无法保持连续性的完整反例。

现在设 $f$ 在 $c$ 连续、$y\in\mathbb R$。若 $f(c)<y$，差 $y-f(c)>0$，令 $t=(y-f(c))/2>0$。商乘回给 $y=f(c)+2t$。对误差 $t$ 取正半径 $r$。所有 $x\in D$ 且 $|x-c|<r$ 满足

$$
f(x)-f(c)\le|f(x)-f(c)|<t,
$$

同加 $f(c)$ 得 $f(x)<f(c)+t$，再由 $t>0$ 得 $f(c)+t<f(c)+2t=y$，所以 $f(x)<y$。

若 $f(c)>y$，取 $t=(f(c)-y)/2>0$，有 $f(c)=y+2t$。对误差 $t$ 取正半径。近域输入满足

$$
f(c)-f(x)\le|f(c)-f(x)|=|f(x)-f(c)|<t.
$$

平移得到 $f(x)>f(c)-t=y+t>y$。两支都只检查 $D$ 内输入，所以在闭区间端点处也可以使用同样论证。

### 题5：同域运算的全部误差条件 {#continuity-a05}

[返回题目](#continuity-q05)。设 $f,g:D\to\mathbb R$ 在 $c\in D$ 连续，$\lambda\in\mathbb R$ 固定。实数加、差、乘各给唯一实数，因此和、差、积、倍数规则都为 $D\to\mathbb R$ 全函数。它们在中心的值也由同一规则给出。

给任意 $\varepsilon>0$，实数2正，所以 $\varepsilon/2>0$。分别为 $f,g$ 取得该误差的正半径 $r_f,r_g$，取 $\delta=\min(r_f,r_g)>0$。任意 $x\in D$ 且 $|x-c|<\delta$ 同时满足两误差。把和的误差重排成两个差的和，三角给

$$
\begin{aligned}
|(f(x)+g(x))-(f(c)+g(c))|
&\le|f(x)-f(c)|+|g(x)-g(c)|\\
&<\varepsilon/2+\varepsilon/2=\varepsilon.
\end{aligned}
$$

差的误差为 $(f(x)-f(c))-(g(x)-g(c))$，三角及取反不变同样给

$$
|(f(x)-g(x))-(f(c)-g(c))|
\le|f(x)-f(c)|+|g(x)-g(c)|<\varepsilon.
$$

两份严格界相加使用平移保序，最后等式用正分母2的乘回。因此和与差在 $c$ 连续。

若 $\lambda=0$，倍数函数和它的中心值都为零，对任意正误差取 $\delta=1$，输出误差为零。若 $\lambda\ne0$，则 $h=|\lambda|>0$。为 $f$ 取得正误差 $\varepsilon/h$ 的半径 $\delta$。相关输入通过差乘和绝对乘积得到

$$
|\lambda f(x)-\lambda f(c)|=h|f(x)-f(c)|
<h(\varepsilon/h)=\varepsilon.
$$

严格性与乘回都已核 $h>0$，所以倍数规则连续。

为证积，先对 $f$ 连续性输入误差1，取半径 $r>0$。对全部 $x\in D$、$|x-c|<r$，三角给

$$
|f(x)|\le|f(x)-f(c)|+|f(c)|<1+|f(c)|=M,
$$

其中 $M>0$。令 $K=M+|g(c)|+1>0$，于是 $M\le K$、$|g(c)|\le K$。

现在给 $\varepsilon>0$，令 $\eta=\varepsilon/(2K)>0$。两连续条件分别给误差 $\eta$ 的正半径 $s_f,s_g$。取

$$
\delta=\min(r,\min(s_f,s_g))>0.
$$

内层较小值正且不大于 $s_f,s_g$，外层也正且不大于 $r$ 与内层，所以三条件同时有效。任取 $x\in D$、$|x-c|<\delta$，逐分配、交换与抵消核

$$
\begin{aligned}
&f(x)(g(x)-g(c))+g(c)(f(x)-f(c))\\
&\quad=f(x)g(x)-f(x)g(c)+g(c)f(x)-g(c)f(c)\\
&\quad=f(x)g(x)-f(c)g(c).
\end{aligned}
$$

三角与绝对乘积给总误差不大于

$$
|f(x)|\,|g(x)-g(c)|+|g(c)|\,|f(x)-f(c)|.
$$

第一项 $\le K|g(x)-g(c)|<K\eta$，第二项 $\le K|f(x)-f(c)|<K\eta$。弱步只乘非负误差，严格步使用正因子 $K$；不能把可能为零的 $g(c)$ 或误差当作严格保序因子。

由 $(2K)\eta=\varepsilon$ 及结合律，$2(K\eta)=\varepsilon$。系数2非零，方程唯一性给 $K\eta=\varepsilon/2$，所以总误差小于 $\varepsilon$，积在 $c$ 连续。若 $g(c)=0$，第二项是零；若任一误差为零，对应弱比较可能为等号，但仍因 $K\eta>0$ 得所需严格上界。全部中心与零误差情况都包括。

### 题6：实际商域中的连续性 {#continuity-a06}

[返回题目](#continuity-q06)。给题设同域连续函数，且 $g(c)\ne0$。定义 $D_g=\{x\in D:g(x)\ne0\}$。因为 $c\in D$ 且 $g(c)\ne0$，有 $c\in D_g$。每个 $D_g$ 输入的分母非零，所以 $v(x)=1/g(x)$、$q(x)=f(x)/g(x)$ 给唯一实数输出，均为该域上的全函数，中心值也存在。

令 $h=|g(c)|>0$，$t=h/2>0$，则 $h-t=t$。对 $g$ 连续性使用误差 $t$，取正半径 $r_0$。任意 $x\in D$ 且 $|x-c|<r_0$ 满足 $|g(x)-g(c)|<t$，反三角与基本绝对值界给

$$
h-|g(x)|\le\bigl|h-|g(x)|\bigr|
\le|g(c)-g(x)|<t.
$$

同加 $|g(x)|-t$，得到 $|g(x)|>h-t=t>0$。

在这样的 $D_g$ 输入处，$g(x),g(c)$ 及其乘积均非零。乘回计算

$$
\begin{aligned}
&\left(\frac1{g(x)}-\frac1{g(c)}\right)g(x)g(c)\\
&\quad=\left[\left(\frac1{g(x)}\right)g(x)\right]g(c)
-\left[\left(\frac1{g(c)}\right)g(c)\right]g(x)\\
&\quad=g(c)-g(x).
\end{aligned}
$$

分配与乘法交换结合给首个等号，两个合法倒数的乘回给最后等号。非零系数方程唯一性说明倒数差等于 $(g(c)-g(x))/(g(x)g(c))$。取绝对值并用绝对乘商及差取反，得

$$
|v(x)-v(c)|=\frac{|g(x)-g(c)|}{|g(x)|h}.
$$

固定 $d=th=(h/2)h>0$。局部下界乘正数 $h$，给 $Q=|g(x)|h>d$。任给正误差 $\varepsilon$，$\varepsilon d>0$，所以可对 $g$ 取其误差半径 $r_1>0$。令 $\delta=\min(r_0,r_1)>0$。任意 $x\in D_g$ 且 $|x-c|<\delta$ 同时满足 $e=|g(x)-g(c)|<\varepsilon d$ 和 $Q>d>0$。

由正倒数反序、乘非负数及正除法比较，

$$
|v(x)-v(c)|=\frac eQ\le\frac ed
<\frac{\varepsilon d}{d}=\varepsilon.
$$

当 $e=0$，第一步两边同为零，不能写严格小于；第二步仍来自 $e<\varepsilon d$ 与 $d>0$。因此 $v$ 在 $c$ 连续，包括 $x=c$ 的零误差。

再定义 $u:D_g\to\mathbb R$ 为 $u(x)=f(x)$。为任意正误差取原 $f$ 的半径；由于 $D_g\subseteq D$ 且 $u(c)=f(c)$，这个半径对全部 $D_g$ 近输入给

$$
|u(x)-u(c)|=|f(x)-f(c)|<\varepsilon.
$$

故限制函数连续。题5已证同域乘积连续，所以 $uv$ 在 $c$ 连续。对每个 $x\in D_g$，$u(x)v(x)=f(x)/g(x)=q(x)$，中心也按同一公式求值，因而商连续。

不要求原域处处非零。例如 $D=\mathbb R$、$g(x)=x$、$c=1$。恒等规则连续，$g(1)=1\ne0$，但 $g(0)=0$。实际倒数域为 $\mathbb R\setminus\{0\}$，包含中心1，所证倒数函数在1连续。域外排除的零点并没有被重新赋予倒数值。

### 题7：复合允许内层等于中心值 {#continuity-a07}

[返回题目](#continuity-q07)。设 $D,E\subseteq\mathbb R$，$g:D\to E$、$f:E\to\mathbb R$，$c\in D$，内外函数分别在 $c$ 与 $g(c)$ 连续。内函数的连续性按实数输出的误差衡量，目标集合 $E$ 仍保留用于复合。

每个 $x\in D$ 都有 $g(x)\in E$，外函数因此给唯一实数 $f(g(x))$，所以复合为 $D\to\mathbb R$ 的全函数。特别 $g(c)\in E$，中心值为 $f(g(c))$。

任给实数 $\varepsilon>0$，先用外层在 $g(c)$ 连续，取实数 $\eta>0$，使对全部 $y\in E$ 有

$$
|y-g(c)|<\eta\Longrightarrow |f(y)-f(g(c))|<\varepsilon.
$$

再用内层在 $c$ 连续，针对正误差 $\eta$ 取得 $\delta>0$，使全部 $x\in D$ 有

$$
|x-c|<\delta\Longrightarrow |g(x)-g(c)|<\eta.
$$

现在才任取 $x\in D$ 且 $|x-c|<\delta$。内层给误差小于 $\eta$，且 $g(x)$ 属于外层的域，所以代入 $y=g(x)$ 得

$$
|(f\circ g)(x)-(f\circ g)(c)|
=|f(g(x))-f(g(c))|<\varepsilon.
$$

这对整个近域成立；所选 $\delta$ 可依赖 $\varepsilon$，不依赖后来任取的输入，故复合连续。

若固定 $e\in E$，定义 $g(x)=e$，则每个域内输入输出相同。对任意正误差可取半径1，内层输出差为零，所以 $g$ 在每个域内点连续。在题设外层于 $e=g(c)$ 连续的条件下，两级证明照常适用：每次外层输入都恰为其中心，距离 $|e-e|=0<\eta$，输出误差也为零。连续性没有禁止这种相等输入；若把外层条件误换成穿孔极限条件，就不能直接作此代入。

### 题8：只用有限个已证操作构造函数 {#continuity-a08}

[返回题目](#continuity-q08)。对每个 $x\in\mathbb R$，绝对值非负，所以 $|x|+1\ge1>0$。平方 $x^2=xx$、加1和绝对值都由实数运算得到，分母非零，因此

$$
H(x)=\frac{x^2+1}{|x|+1}
$$

对每个实数输入给唯一实数输出，域确为全部 $\mathbb R$。

任取中心 $c\in\mathbb R$。恒等函数 $I(x)=x$ 在 $c$ 连续：任给正误差取同值半径即可。常数函数 $J(x)=1$ 也在 $c$ 连续：误差恒零，半径可取1。

将已证同域乘积规律用于 $I$ 与自身，得到 $S(x)=I(x)I(x)=x^2$ 在 $c$ 连续。再用同域和规律，$F(x)=S(x)+J(x)=x^2+1$ 在 $c$ 连续。这里只作一次两个实数函数的乘积，没有使用一般实幂或多项式总定理。

绝对值规则也在 $c$ 连续。直接地，给任意 $\varepsilon>0$，取 $\delta=\varepsilon$；$|x-c|<\delta$ 时反三角给

$$
\bigl||x|-|c|\bigr|\le|x-c|<\varepsilon.
$$

因此 $A(x)=|x|$ 连续，同域和规律给 $G(x)=A(x)+J(x)=|x|+1$ 在 $c$ 连续。它不仅在中心满足 $G(c)>0$，还对所有实数输入都非零，所以实际商域

$$
D_G=\{x\in\mathbb R:G(x)\ne0\}=\mathbb R.
$$

将已证实际商域规律用于 $F,G$，得到 $H=F/G$ 在 $c$ 连续，中心值就是 $(c^2+1)/(|c|+1)$。由于 $c$ 是任取实数，$H$ 在整个实数域连续。每次使用的都是已经给出完整误差证明的有限操作法则，而非未建立的一般有理函数连续性结论。
