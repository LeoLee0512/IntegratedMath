## B4.6 实函数的点极限：完整解答 {#funlimit-answers}

以下各输入、中心、候选极限、误差与半径均为实数。函数的域逐题声明；所有半径和误差先要求严格正。沿域在某中心谈点极限时，该中心须为该域聚点。使用两个正数的较小者时，按全序分两支，它等于其中一个正数且不大于二者；嵌套两次即可合并三个正半径。

### 题1：域中有没有靠近的不同输入 {#funlimit-a01}

[返回题目](#funlimit-q01)。固定实数 $p$。为核聚点，任给实数 $r>0$。实数2正，所以 $t=r/2>0$，商乘回给 $2t=r$，分配给 $2t=t+t$。将 $0<t$ 同加 $t$ 得 $t<t+t=r$。

取 $x=p+t$。实数加法闭合使 $x\in\mathbb R$；加法群给 $x-p=t$，故

$$
0<|x-p|=|t|=t<r.
$$

这个输入见证说明 $p$ 是 $\mathbb R$ 聚点。又 $x-p=t>0$，所以 $x\ne p$，同一见证也属于 $\mathbb R\setminus\{p\}$，证明 $p$ 是这个删点域的聚点。可见聚点无需属于域。

对非负实数集 $D=\{x\in\mathbb R:x\ge0\}$ 和中心0，给定 $r>0$ 仍取 $x=r/2$。它正，故属于 $D$，且 $0<|x-0|=r/2<r$。因此0是该域聚点，即使没有负输入也可以在此定义沿域的点极限。

若域改为 $D=\{p\}$，任取 $x\in D$ 必有 $x=p$，所以 $|x-p|=0$。对正半径1，找不到 $x\in D$ 满足 $0<|x-p|<1$，聚点条件失败。

然而对任意函数 $f:D\to\mathbb R$、任意候选实数 $L$，任给 $\varepsilon>0$ 都可取 $\delta=1$。此时所有 $x\in D$ 的蕴含式

$$
0<|x-p|<\delta\Longrightarrow |f(x)-L|<\varepsilon
$$

都成立，因为其前提没有满足的输入。无论 $f(p)$ 是什么、$L$ 是什么，都不会改变这个事实。若不要求聚点，会把不同的 $L$ 同时当成极限。域非空仅提供某个输入；聚点要求每个正半径都有一个不同于中心的输入，二者不能混同。

### 题2：完整否定与唯一性的共同输入 {#funlimit-a02}

[返回题目](#funlimit-q02)。给 $f:D\to\mathbb R$、$D$ 的聚点 $p$ 和固定 $L\in\mathbb R$。收敛定义为

$$
\begin{gathered}
\forall\varepsilon>0\ \exists\delta>0\ \forall x\in D,\\
0<|x-p|<\delta\Longrightarrow |f(x)-L|<\varepsilon.
\end{gathered}
$$

$\delta$ 在任取 $x$ 以前选，可以依赖给定函数、域、中心、目标及误差，不能依赖后来检查的输入。固定 $L$ 的否定为

$$
\begin{gathered}
\exists\varepsilon_0>0\ \forall\delta>0\ \exists x\in D,\\
0<|x-p|<\delta\quad\text{且}\quad |f(x)-L|\ge\varepsilon_0.
\end{gathered}
$$

这是依次否定全称、存在、全称量词，并以全序把“不是小于”改写成“不小于”。若要表达无任何实数极限，还须在此否定外层加 $\forall L\in\mathbb R$；每个候选可有自己的失败误差。某个固定 $L$ 失败不能排除另一个候选。

现在假设函数沿同一域在 $p$ 同时趋 $L,M\in\mathbb R$。反设 $L\ne M$，则 $s=|L-M|>0$。取 $h=s/3>0$，分别由两极限定义得到 $\delta_L>0$、$\delta_M>0$，保证相应穿孔输入上的两误差各小于 $h$。

若 $\delta_L\le\delta_M$，取 $r=\delta_L$；否则取 $r=\delta_M$。两支中 $r$ 都正且不大于两半径。聚点性质在半径 $r$ 下给一个 $x\in D$，使 $0<|x-p|<r$。因此同一个输入满足两份误差，而不是分别选两个可能不同的输入。

由 $L-M=(L-f(x))+(f(x)-M)$ 及三角，

$$
\begin{aligned}
s&\le |L-f(x)|+|f(x)-M|\\
&=|f(x)-L|+|f(x)-M|\\
&<h+h=2h<3h=s.
\end{aligned}
$$

取反不改变绝对值；严格相加由平移保序；$2h<3h$ 因 $h>0$，$3h=s$ 因商乘回。矛盾，故 $L=M$。这份证明说明聚点假设的用途就是提供共同穿孔见证。

### 题3：不借连续性证明基本例 {#funlimit-a03}

[返回题目](#funlimit-q03)。设 $D\subseteq\mathbb R$，$p$ 是其聚点，$C,c,d$ 为固定实数。常数规则 $f(x)=C$ 对每个 $x\in D$ 给同一唯一实数；恒等规则 $u(x)=x$ 因 $D\subseteq\mathbb R$ 给唯一实数；仿射规则 $v(x)=cx+d$ 由实数乘加闭合与唯一性给实数。因此三者均为域 $D$ 上的全函数。

任给实数 $\varepsilon>0$。常数函数取 $\delta=1>0$；任意 $x\in D$ 且 $0<|x-p|<\delta$ 都满足 $|f(x)-C|=|C-C|=0<\varepsilon$，故极限为 $C$。

恒等函数取 $\delta=\varepsilon>0$。任意相应穿孔输入满足 $|u(x)-p|=|x-p|<\delta=\varepsilon$，故沿 $D$ 在 $p$ 的极限为 $p$。这不要求 $p\in D$。

仿射函数分两支。若 $c=0$，每个 $v(x)=d$，目标 $cp+d=d$，误差恒零，对任意正误差取 $\delta=1$。

若 $c\ne0$，绝对值零判据给 $|c|>0$，因此 $\delta=\varepsilon/|c|$ 合法且正。任取 $x\in D$ 满足 $0<|x-p|<\delta$，逐次消去与分配给

$$
(cx+d)-(cp+d)=cx-cp=c(x-p).
$$

于是绝对值乘积与正因子比较给

$$
|v(x)-(cp+d)|=|c|\,|x-p|
<|c|\delta=\varepsilon.
$$

最后等式因非零分母乘回成立。故仿射极限为 $cp+d$，包含负的 $c$；严格比较使用的是正数 $|c|$。没有援引多项式连续性。

### 题4：只改中心值和局部相等 {#funlimit-a04}

[返回题目](#funlimit-q04)。给同域函数 $f,g:D\to\mathbb R$、$D$ 聚点 $p$，且存在 $r>0$，使 $x\in D$、$0<|x-p|<r$ 时 $f(x)=g(x)$。固定任意实数 $L$。

先假设沿 $D$ 在 $p$ 有 $f\to L$。给任意 $\varepsilon>0$，取 $f$ 的正半径 $\delta_f$，令 $\delta=\min(r,\delta_f)>0$。若 $x\in D$ 且 $0<|x-p|<\delta$，则输入同时在相等区域和 $f$ 的误差区域内，故

$$
|g(x)-L|=|f(x)-L|<\varepsilon.
$$

所以沿该域在 $p$ 有 $g\to L$。

反向若 $g\to L$，对同一任意正误差取 $g$ 的半径 $\delta_g>0$，再取 $\delta'=\min(r,\delta_g)>0$。每个相应穿孔输入都有

$$
|f(x)-L|=|g(x)-L|<\varepsilon,
$$

所以 $f\to L$。两次取较小者的正性都来自两个输入半径正，未将半径取成零。

在 $\mathbb R$ 上固定 $p$，定义

$$
f(x)=\begin{cases}1,&x=p,\\0,&x\ne p.\end{cases}
$$

相等或不相等两支互斥穷尽，每支给唯一实数，故为全函数。中心 $p$ 是 $\mathbb R$ 聚点。任给 $\varepsilon>0$，取 $\delta=1$。若 $0<|x-p|<\delta$，绝对值零判据给 $x\ne p$，所以 $f(x)=0$，从而 $|f(x)-0|=0<\varepsilon$。故点极限为零，而定义给 $f(p)=1$。也可由它与零函数在穿孔域相等推出同样结论。

若原函数的域 $D$ 不含 $p$，函数求值只对域内输入定义，因此不存在这个函数的 $f(p)$ 可修改。若另向域中添加 $p$ 并赋值，就定义了一个不同域的新函数；不能把它与原函数的已有求值混为一谈。

### 题5：局部上界与非零下界 {#funlimit-a05}

[返回题目](#funlimit-q05)。设 $f,g:D\to\mathbb R$，$p$ 是 $D$ 聚点，沿 $D$ 在 $p$ 有 $f\to A$、$g\to B\ne0$。

给 $f$ 使用正误差1，取得半径 $r>0$。任意 $x\in D$ 满足 $0<|x-p|<r$ 时，$|f(x)-A|<1$。加法群与三角给

$$
|f(x)|=|(f(x)-A)+A|
\le |f(x)-A|+|A|<1+|A|.
$$

这只控制上述穿孔近域，定义并没有对更远输入提出条件，也没有控制中心值。

对 $g$，令 $h=|B|>0$。因为实数2正，$t=h/2>0$。乘回 $2t=h$ 与分配 $2t=t+t$ 给 $h-t=t$。对正误差 $t$ 使用 $g\to B$，取 $r_0>0$，使 $x\in D^*(p,r_0)$ 时 $|g(x)-B|<t$。

基本绝对值界及反三角依次给

$$
\begin{aligned}
h-|g(x)|
&\le\bigl|h-|g(x)|\bigr|\\
&=\bigl||B|-|g(x)|\bigr|\\
&\le|B-g(x)|=|g(x)-B|<t.
\end{aligned}
$$

将最后得到的 $h-|g(x)|<t$ 两边同加 $|g(x)|-t$，得 $h-t<|g(x)|$。因此

$$
|g(x)|>h-t=t=|B|/2>0.
$$

这些输入处 $g(x)\ne0$，但条件仍只在穿孔近域内。

例如在 $D=\mathbb R$、中心 $p=0$，定义 $g(0)=0$，其余输入 $g(x)=1$。域含每个实数，规则全定义；对任意误差取半径1，所有穿孔输入误差为零，所以它趋于非零数1。然而 $g(0)=0$，故不能推出全域非零。

为具体说明局部上界不意味着全域有界，可取 $D=\mathbb R$、$p=0$、$f(x)=x$。它按恒等函数证明趋于零。但对任意拟议非负全域界 $H$，输入 $x=H+1\in\mathbb R$ 正，满足 $|f(x)|=H+1>H$，故全域无界。这个反例不需要序列或无穷极限。

### 题6：和与积的共同半径 {#funlimit-a06}

[返回题目](#funlimit-q06)。设题给同域函数沿 $D$ 在其聚点 $p$ 分别趋 $A,B$。每个 $x\in D$ 给唯一实数 $f(x),g(x)$；已建实数加法和乘法给唯一实数输出，所以和与积都是域 $D$ 上的全函数。

先证和。任给 $\varepsilon>0$，正数2保证 $\varepsilon/2>0$。为两函数各取此误差的正半径 $\delta_f,\delta_g$，取 $\delta=\min(\delta_f,\delta_g)>0$。任给 $x\in D^*(p,\delta)$，它同时满足两份误差。于是

$$
\begin{aligned}
|(f(x)+g(x))-(A+B)|
&=|(f(x)-A)+(g(x)-B)|\\
&\le |f(x)-A|+|g(x)-B|\\
&<\varepsilon/2+|g(x)-B|\\
&<\varepsilon/2+\varepsilon/2=\varepsilon.
\end{aligned}
$$

两个严格步均同加相同实数；末式由正分母2的乘回。故和的极限为 $A+B$。

乘积先取 $f\to A$ 对误差1的正半径 $r$。在 $D^*(p,r)$ 上三角给 $|f(x)|<M=|A|+1$，且 $M>0$。固定 $K=M+|B|+1>0$，其中 $M\le K$、$|B|\le K$。

现在任给 $\varepsilon>0$，令 $\eta=\varepsilon/(2K)>0$；这里 $2K>0$，所以商合法。为 $f,g$ 各取误差 $\eta$ 的半径 $r_f,r_g>0$，并令

$$
\delta=\min(r,\min(r_f,r_g)).
$$

内层较小者是正数且不大于 $r_f,r_g$；外层也是正数且不大于 $r$ 及内层。因此 $\delta>0$ 并同时不大于三个半径。任取 $x\in D^*(p,\delta)$，局部界与两误差同时成立。

逐分配并抵消：

$$
\begin{aligned}
f(x)(g(x)-B)+B(f(x)-A)
&=f(x)g(x)-f(x)B+Bf(x)-BA\\
&=f(x)g(x)-AB.
\end{aligned}
$$

第二步用乘法交换使 $-f(x)B+Bf(x)=0$，并将 $BA$ 写成 $AB$。三角和绝对乘积给

$$
|f(x)g(x)-AB|
\le |f(x)|\,|g(x)-B|+|B|\,|f(x)-A|.
$$

两项分别估计为

$$
|f(x)|\,|g(x)-B|\le K|g(x)-B|<K\eta,
$$

$$
|B|\,|f(x)-A|\le K|f(x)-A|<K\eta.
$$

第一个比较各自只乘非负误差，故使用弱式；严格步乘的是 $K>0$，不是可能为零的 $|B|$ 或误差。商乘回给 $(2K)\eta=\varepsilon$，结合律给 $2(K\eta)=\varepsilon$；系数2非零，唯一解为 $K\eta=\varepsilon/2$。将两项严格界相加得到 $|f(x)g(x)-AB|<\varepsilon$，即积趋于 $AB$。

若 $B=0$，第二项实际为零，但它仍小于正数 $K\eta$；若某个误差为零，相关弱式可能相等，最后仍由 $0<K\eta$ 或正 $K$ 乘严格误差得到严格上界。整份证明不依赖那些因子非零。

### 题7：实际商域先要有聚点 {#funlimit-a07}

[返回题目](#funlimit-q07)。设题给函数同域、$p$ 为域聚点，且分别趋 $A,B$，其中 $B\ne0$。定义

$$
D_g=\{x\in D:g(x)\ne0\}.
$$

对每个 $x\in D_g$，$g(x)$ 非零，所以 $v(x)=1/g(x)$ 与 $q(x)=f(x)/g(x)$ 都有唯一实数输出，确为该域上的全函数。

由题5，存在 $r_0>0$，使 $x\in D^*(p,r_0)$ 时 $|g(x)|>|B|/2>0$，故这些输入属于 $D_g$。任给正实数 $r$，$s=\min(r,r_0)>0$。用 $D$ 的聚点性质取得 $x\in D$，满足 $0<|x-p|<s$。它因距离小于 $r_0$ 而有 $g(x)\ne0$，故 $x\in D_g$；同时距离小于 $r$。所以对每个 $r>0$，都有 $D_g$ 内的穿孔见证，$p$ 确为商域的聚点。

令 $h=|B|>0$。在上述近域，每个 $g(x)\ne0$ 且 $B\ne0$，零积判据给 $g(x)B\ne0$。倒数差逐乘回为

$$
\begin{aligned}
\left(\frac1{g(x)}-\frac1B\right)g(x)B
&=\left[\left(\frac1{g(x)}\right)g(x)\right]B
 -\left[\left(\frac1B\right)B\right]g(x)\\
&=B-g(x).
\end{aligned}
$$

首行用分配、交换与结合，次行用非零分母乘回。系数 $g(x)B$ 非零，方程唯一性给

$$
\frac1{g(x)}-\frac1B=\frac{B-g(x)}{g(x)B}.
$$

绝对商、绝对乘积与差的取反不变得到

$$
\left|v(x)-\frac1B\right|
=\frac{|g(x)-B|}{|g(x)|h}.
$$

固定 $d=(h/2)h>0$。近域下界乘正数 $h$，给 $Q=|g(x)|h>d$。给任意 $\varepsilon>0$，$\varepsilon d>0$，所以可为 $g\to B$ 取半径 $r_1>0$，控制 $|g(x)-B|<\varepsilon d$。令 $\delta=\min(r_0,r_1)>0$。任意 $x\in D_g^*(p,\delta)$ 属于原域 $D$，同时满足这份误差和分母下界。记 $e=|g(x)-B|\ge0$，正倒数反序给 $1/Q<1/d$，乘非负 $e$ 后只断言弱式，继而

$$
\left|v(x)-\frac1B\right|
=\frac eQ\le\frac ed
<\frac{\varepsilon d}{d}=\varepsilon.
$$

第二个严格号因正除数 $d$ 保持 $e<\varepsilon d$，最后乘回合法。若 $e=0$，第一比较两边同为零，不能写成严格小于，但整条链仍成立。因此沿 $D_g$ 在 $p$ 有 $v\to1/B$。

定义限制函数 $u:D_g\to\mathbb R$ 为 $u(x)=f(x)$。每个 $D_g$ 输入属于 $D$，所以输出合法。给 $\varepsilon>0$，选原 $f\to A$ 的半径 $r_f$。若 $x\in D_g$ 且 $0<|x-p|<r_f$，它也是原定义所要求的输入，故 $|u(x)-A|=|f(x)-A|<\varepsilon$。于是沿 $D_g$ 在 $p$ 有 $u\to A$。

现在 $u,v$ 同域 $D_g$，该域以 $p$ 为聚点，两极限均已证明，可以应用同域乘积定理：$uv\to A(1/B)=A/B$。在每个 $x\in D_g$，$u(x)v(x)=f(x)(1/g(x))=q(x)$，所以商极限为 $A/B$。目标分母 $B$ 已非零；分子 $A$ 可以为零。

不需要 $p\in D_g$。例如 $D=\mathbb R$、$p=0$，取 $g(0)=0$、其余 $g(x)=1$；直接误差定义给 $g\to1$，而 $D_g=\mathbb R\setminus\{0\}$，中心不在商域中却仍是聚点。不能把近域非零扩大成原域全部非零。

### 题8：平方差商与零分母极限 {#funlimit-a08}

[返回题目](#funlimit-q08)。固定 $p\in\mathbb R$，定义 $D=\mathbb R\setminus\{p\}$。若 $x\in D$，则 $x\ne p$，实数差的零判据给 $x-p\ne0$。分子 $x^2-p^2$ 由已定义的实数平方与差得到，所以

$$
q(x)=\frac{x^2-p^2}{x-p}
$$

为每个 $D$ 输入给唯一实数，确为 $D\to\mathbb R$ 的全函数。

对任意正半径 $r$，取 $t=r/2>0$、$x=p+t$。正数2的乘回与平移给 $0<t<r$，故 $0<|x-p|=t<r$；同时 $x\ne p$，所以 $x\in D$。因此 $p$ 是实际域 $D$ 的聚点。

逐分配计算候选 $x+p$ 乘分母：

$$
\begin{aligned}
(x+p)(x-p)
&=x(x-p)+p(x-p)\\
&=x^2-xp+px-p^2\\
&=x^2-p^2.
\end{aligned}
$$

最后用实数乘法交换 $xp=px$ 及加法逆元抵消。系数 $x-p$ 非零，乘法方程唯一性给 $q(x)=x+p$。此等式只对 $x\in D$ 声明，未在 $x=p$ 处取消零分母。

任给实数 $\varepsilon>0$，取 $\delta=\varepsilon>0$。若 $x\in D$ 且 $0<|x-p|<\delta$，分配给 $2p=p+p$，加法群消去给

$$
|q(x)-2p|=|(x+p)-(p+p)|=|x-p|<\varepsilon.
$$

所以沿删点域在 $p$ 的极限为 $2p$。没有引用多项式连续性或一般有理函数极限定理。

再取 $D=\mathbb R$、$p=0$、$f(x)=g(x)=x$。域以0为聚点；对任意 $\varepsilon>0$ 取 $\delta=\varepsilon$，穿孔输入满足 $|f(x)-0|=|g(x)-0|=|x|<\varepsilon$，故两个极限都是零。

实际商域为 $D_g=\mathbb R\setminus\{0\}$，因为 $g(x)\ne0$ 当且仅当 $x\ne0$。它仍以0为聚点，见证取 $x=r/2$。对每个此域输入 $x$，候选1乘回分母得 $1\cdot x=x$；非零系数方程唯一性给 $x/x=1$。商函数因而恒为一。对任意 $\varepsilon>0$ 取 $\delta=1$，每个商域穿孔输入的输出误差为 $|1-1|=0<\varepsilon$，所以商极限为一。

这里分母极限为零，因此不能代入要求 $B\ne0$ 的商法则；但商仍有极限。定理不适用与结论必失败是不同断言，“分母趋零必发散”正是混淆了二者。
