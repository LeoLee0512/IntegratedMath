## 基础单元 B4.8 连续复合与局部定义域 {#ccomp-unit}

**位置与目标。** 本单元主归第146章26A15连续性基础，交叉97I20函数教学。目标是先检查两条规则能在哪里先后求值，再用连续定义控制两层误差。我们还要区分全域映入、自然可求值域和确有整个局部邻域映入三种条件。本单元不建立一般点极限复合定理，不引入序列判据、介值、极值、紧致性、一致连续性、导数或积分；完成本单元不表示整个26A15完成。

**精确先修。** 使用[条件子集](#fun-sets)、[函数三项数据与求值](#fun-definition)、[实际像](#fun-image)、[函数相等FC1](#fc-equality)、[限制FC2](#fc-restriction)、[严格类型复合FC3](#fc-composition)。分析先修为[实数连续定义及量词](#cont-definition)、[孤立点CT1](#cont-isolated-limit)、[常数、包含规则及限制CT2](#cont-basic-restriction)、[有限运算CT3](#cont-algebra)、[倒数和商域CT4](#cont-quotient)。误差估计使用[实数加法与序](#cutgroup-translation)、[乘法比较](#cutring-multiplication-order)、[乘法符号及平方非负所用取反规则](#cutsigned-signs)、[零积判据](#cutsigned-rational-zero)、[非零除法](#cutdiv-definition)、[绝对值基本界](#realabs-definition-bounds)与[实数线距](#realabs-distance)。最后的反例只调用[积点](#flim-domain-cluster)和[去心点极限定义](#flim-definition)，不用尚未写成的复合极限定理。

**阅读安排。** 预计教学正文约10—14页，八题答案另列。先读类型与连续复合证明，再读自然域和局部一致；后半段只复用前半段与CT2的限制结论。

**记号。** $D,E\subseteq\mathbb R$；$g:D\to\mathbb R$是内层实值函数，$f:E\to\mathbb R$是外层实值函数。$g(D)=\{g(x):x\in D\}$是实际像，未必等于声明的目标$\mathbb R$。$c$是域内中心，$x,y$是输入，$\varepsilon,\eta,\delta,r_0$是正实数容差或半径。$[a,b]=\{x\in\mathbb R:a\le x\le b\}$，本单元使用的有限闭区间均满足$a\le b$。另记$[0,\infty)=\{x\in\mathbb R:x\ge0\}$、$(0,\infty)=\{x\in\mathbb R:x>0\}$；这里$\infty$只是无上端点的记号，不是实数输入。所有常量都是实数域中的相应有理像。

### 1. 先确认内层输出能送入外层 {#ccomp-types}

如果只写两条计算公式，可能遗漏外层根本没有定义的输入。例如$g:\mathbb R\to\mathbb R$、$g(x)=x$，而$f:[0,\infty)\to\mathbb R$、$f(y)=y^2$。虽然$(-1)^2$在实数代数中有意义，但作为这个已指定的函数，$f$并没有输入$-1$的记录。因此$f(g(-1))$不是该函数的合法求值。另定义一个全实域平方函数是可以的，却不能声称原来的$f$已经具有这个定义域。

**构造 CC0（像包含下的新函数）。** 设$g:D\to\mathbb R$、$f:E\to\mathbb R$且

$$
g(D)\subseteq E.
$$

对每个$x\in D$，逐点规定

$$
h(x)=f(g(x)).
$$

这给出唯一函数$h:D\to\mathbb R$。具体地，$g$对$x$有唯一输出$g(x)$；像包含保证$g(x)\in E$，于是$f$对这个输入有唯一实输出$f(g(x))$。所有这样的有序对$(x,f(g(x)))$组成$D\times\mathbb R$中的图，每个$x$恰有一个输出，故三项数据确实构成函数。若另一个函数具有相同定义域、目标及逐点规则，由FC1它等于$h$。

**与前文严格复合怎样相容。** FC3要求内层的声明目标恰等于外层的定义域。这里原$g$的目标是$\mathbb R$；若$E\ne\mathbb R$，不能直接把原$g$与$f$当作满足该类型条件的两个记录。

像包含允许另造函数$g_E:D\to E$，保留$g$的图。每个输出属于$E$且唯一，故新记录合法。此时$f\circ g_E:D\to\mathbb R$符合FC3；对每个$x\in D$，

$$
(f\circ g_E)(x)=f(g_E(x))=f(g(x))=h(x).
$$

两端集合也与$h$相同，因此$h=f\circ g_E$。若$E\ne\mathbb R$，$g_E$与$g$的目标不同，它们不是同一个三项记录。我们没有暗改$g$，也没有要求$g_E$满射。以下“连续复合”研究的是CC0定义的实值$h$；连续条件仍只用于实值$g:D\to\mathbb R$与$f:E\to\mathbb R$。

若$D=\varnothing$，构造给出目标为$\mathbb R$的空域函数，输出条件为空真。若$D\ne\varnothing$而$E=\varnothing$，任取$x\in D$会有$g(x)\in g(D)$，不可能满足$g(D)\subseteq E$。因而定理条件本身排除了这种安排。

### 2. 两层误差按相反方向选取 {#ccomp-theorem}

**定理 CC1（连续复合）。** 设$g:D\to\mathbb R$、$f:E\to\mathbb R$、$g(D)\subseteq E$，并按CC0定义$h:D\to\mathbb R$、$h(x)=f(g(x))$。若$c\in D$，$g$在$c$连续，$f$在$g(c)$相对$E$连续，那么$h$在$c$连续。

这里$g(c)\in E$由像包含保证，外层的中心值$f(g(c))$确实存在。证明不是同时随意挑两个半径，而是从最终误差倒着安排控制。

**第一步：先向外层提出误差要求。** 任给$\varepsilon>0$。由$f$在$g(c)$连续，存在$\eta>0$，使任意$y\in E$满足

$$
|y-g(c)|<\eta
\quad\Longrightarrow\quad
|f(y)-f(g(c))|<\varepsilon.
$$

$\eta$是外层允许的输入误差。

**第二步：让内层输出落入这个误差范围。** 把已经选定的正数$\eta$作为$g$的输出容差。由$g$在$c$连续，存在$\delta>0$，使任意$x\in D$满足

$$
|x-c|<\delta
\quad\Longrightarrow\quad
|g(x)-g(c)|<\eta.
$$

$\delta$在随后任取$x$之前已选好。

**第三步：把两段控制接起来。** 任取$x\in D$且$|x-c|<\delta$。第二步给出$|g(x)-g(c)|<\eta$，像包含同时给出$g(x)\in E$，所以能将第一步的$y$取为$g(x)$。于是

$$
|h(x)-h(c)|
=|f(g(x))-f(g(c))|
<\varepsilon.
$$

这恰好是$h$在$c$连续的定义。CC1证毕。

选取顺序是$\varepsilon\to\eta\to\delta$，实际求值顺序则是$x\to g(x)\to f(g(x))$。证明允许$g(x)=g(c)$：此时外层输出差为零，照样小于$\varepsilon$。不能额外加上“内层输出不得等于中心”的去心限制。$c$或$g(c)$若为相应域的孤立点，其连续条件仍是同一不去心定义，证明也完全适用。

若$g$在$D$上连续，$f$在$E$上连续，且$g(D)\subseteq E$，对每个$c\in D$使用CC1，便知$h$在$D$上连续。$D$为空时这个全称结论仍成立，但不能据此指定一个域外点并说$h$在那里连续。

**例题：处处合法的两层规则。** 令$g:\mathbb R\to\mathbb R$、$g(x)=1+x^2$，$E=(0,\infty)=\{y\in\mathbb R:y>0\}$，$f:E\to\mathbb R$、$f(y)=1/y$。由实数平方非负，$g(x)\ge1>0$，所以实际像包含于$E$；每次外层除法的分母非零。包含规则、常数及CT3给$g$处处连续；CT4应用于$E$上的实值包含规则$y\mapsto y$，因每个中心$y>0$，给$f$在$E$连续。CC0与CC1于是给出

$$
h:\mathbb R\to\mathbb R,\qquad h(x)=\frac1{1+x^2}
$$

在全实域连续。这里确认的是所有输入的正分母，几个代入值不能替代这个检查。

### 3. 只有部分输入可以交给外层时 {#ccomp-local-domain}

给定$g:D\to\mathbb R$、$f:E\to\mathbb R$，不假定$g(D)\subseteq E$。先定义**自然可求值域**

$$
H=\{x\in D:g(x)\in E\}.
$$

对$x\in H$，外层求值合法，所以CC0应用于$g|_H:H\to\mathbb R$，定义

$$
h_H:H\to\mathbb R,\qquad h_H(x)=f(g(x)).
$$

下标$H$提醒当前输入域。$H$可能为空，也可能是$D$的真子集；不能默默把$h_H$的域写成$D$。

**命题 CC2（自然域及局部延拓）。** 设$c\in D$且$g(c)\in E$，$g$在$c$连续，$f$在$g(c)$相对$E$连续。则$h_H$在$c$相对$H$连续。

进一步，若已知存在$r_0>0$使

$$
U=\{x\in D:|x-c|<r_0\},\qquad g(U)\subseteq E,
$$

则逐点规则给出$h_U:U\to\mathbb R$、$h_U(x)=f(g(x))$，且它在$c$相对$U$连续。若另有已合法定义的$F:D\to\mathbb R$满足$F|_U=h_U$，则$F$在$c$相对$D$连续。

**自然域的证明。** $g(c)\in E$给$c\in H$，所以讨论$h_H(c)$合法。$H\subseteq D$，由CT2，$g|_H$在$c$相对$H$连续；它的实际像包含于$E$，且$(g|_H)(c)=g(c)$。将CC1应用于这条限制函数和$f$，得到$h_H$在$c$连续。这没有证明$H$包含$c$的整个相对$D$邻域，也不需要这样证明。

**局部规则的证明。** 因$r_0>0$，$|c-c|=0<r_0$，故$c\in U$。由$g(U)\subseteq E$及CT2，CC1同样给$h_U$在$c$连续。任给$\varepsilon>0$，取它的连续半径$\delta_U>0$，然后令

$$
\delta=\min(r_0,\delta_U)>0.
$$

若$x\in D$且$|x-c|<\delta$，则$|x-c|<r_0$，故$x\in U$；又$|x-c|<\delta_U$。局部一致包括$c$，所以$F(x)=h_U(x)$且$F(c)=h_U(c)$，因此

$$
|F(x)-F(c)|=|h_U(x)-h_U(c)|<\varepsilon.
$$

这证明$F$在$c$连续。CC2证毕。定义于$U$的规则本身不会自动为远处的输入补值；上面的$F$是另一个已经合法定义的函数。

**中心能求值，不保证整个局部邻域都能求值。** 取$D=\mathbb R$、$g(x)=x$、$E=[0,\infty)$、$c=0$。虽然$g(c)=0\in E$，但任给$r>0$，取$x=-r/2$，有$|x|=r/2<r$而$g(x)<0$，不属于$E$。自然域$H=[0,\infty)$没有包含0的任何整个相对$D$邻域。若$f(y)=y^2$，$h_H(x)=x^2$相对$H$连续；另造全实域平方函数也可以，但它是域不同的新函数。

**只在去心处一致还不够。** 令$Z:\mathbb R\to\mathbb R$恒为0，而$P(0)=1$、$P(x)=0$当$x\ne0$。它们在每个非零输入相同，却不在中心一致。$Z$连续；对$P$固定$\varepsilon_0=1/2$，任给$\delta>0$取$x=\delta/2$，则$0<|x|<\delta$而$|P(x)-P(0)|=1\ge\varepsilon_0$，所以$P$在0不连续。CC2的中心一致条件不可删去。

### 4. 条件、结论与来源边界 {#ccomp-boundary}

CC1给出足以保证连续的一组条件，没有声称这些条件必要。外层若为常函数，内层的跳变可能完全不影响最终输出；内层若为常函数，则只访问外层的一个点，无法借最终输出检测外层在附近其他点的行为。题6将分别完整核验这两种反向失败。

连续定义对中心本身也给控制，去心点极限只约束非中心输入。如果内层经常或始终取中心值，就不能把外层去心极限直接当作外层连续性来用。题8给出精确反例；这里不建立一般点极限复合判据。

**来源说明。** 核验的标准条件见Jiří Lebl，*Basic Analysis I*，6.3，固定提交`e21ec524ca7d54f800c693b948020c188d21d01f`的[连续函数原生章节](https://raw.githubusercontent.com/jirilebl/ra/e21ec524ca7d54f800c693b948020c188d21d01f/ch-contfunc.tex)，第999—1038行。原文的内外层类型是$g:A\to B$与$f:B\to\mathbb R$，其证明使用连续的序列判据。本单元没有采用那条尚未建立的证明链；在本书函数三项记录约定下，另核CC0合法性，并独立给出直接$\varepsilon\to\eta\to\delta$证明、局部域说明及八题。来源核验不表示已读完该外部章节，也不把其中三角函数、极值等内容算作本单元先修。外部正文不收入本书分发材料。

### 5. 课后练习 {#ccomp-exercises}

每题写清输入域、目标、实际像条件和所讨论的中心。完整解答另列；不能只把两个公式接起来便省略合法性。

#### 题1：实际像足够求值，但没有改写原目标 {#ccomp-q01}

设$g:\mathbb R\to\mathbb R$、$g(x)=x^2$，$E=[0,\infty)$，$f:E\to\mathbb R$、$f(y)=y+1$。核验像包含，按CC0构造$h$并求输出；另构造$g_E:\mathbb R\to E$，证明$h=f\circ g_E$。说明为何原$g$与$g_E$不同，以及是否需要先证明$g_E$满射。[参考答案](#ccomp-a01)

#### 题2：把两段连续量词真正接起来 {#ccomp-q02}

在CC1全部条件下，独立写出$h$在$c$连续的证明。标出各次选半径的先后与任取输入的位置，说明哪里使用了像包含；另说明$g(x)=g(c)$、$c$孤立或$g(c)$孤立是否造成缺口。[参考答案](#ccomp-a02)

#### 题3：正分母带来的全域连续 {#ccomp-q03}

通过内层$g(x)=1+x^2$与外层$f(y)=1/y$，证明$h(x)=1/(1+x^2)$是全实域连续函数。写出两条原函数的域和实目标，核实际像与外层每个中心的非零条件，并说明严格FC3应使用哪个新函数记录。[参考答案](#ccomp-a03)

#### 题4：只在指定中心附近映入 {#ccomp-q04}

令$D=\mathbb R$、$g(x)=x^2$，$E=(0,\infty)$，$f(y)=1/y$，中心$c=1$。用$r_0=1/2$核局部映入。另定义$F:\mathbb R\to\mathbb R$，$F(0)=7$，$x\ne0$时$F(x)=1/x^2$。通过CC2证明$F$在1连续；本题不要求它在其他点的连续性结论。[参考答案](#ccomp-a04)

#### 题5：自然域不必包含整个邻域 {#ccomp-q05}

令$g:\mathbb R\to\mathbb R$为$g(x)=x$，$E=[0,\infty)$，$f:E\to\mathbb R$、$f(y)=y^2$。求自然域$H$并证明$h_H$在0相对$H$连续；证明不存在$r_0>0$使所有$|x|<r_0$的实输入都映入$E$。另设$Q:\mathbb R\to\mathbb R$、$Q(x)=x^2$，说明$Q$与$h_H$的准确关系及为何不是同一个函数。[参考答案](#ccomp-a05)

#### 题6：复合连续不能反推两个因子的连续 {#ccomp-q06}

两组函数均以$\mathbb R$为定义域与目标。第一组：$g(x)=0$当$x\le0$、$g(x)=1$当$x>0$，$f(y)=0$恒成立。第二组：$g(x)=0$恒成立，$f(0)=1$、$f(y)=0$当$y\ne0$。分别证明新函数$h(x)=f(g(x))$在0连续，但第一组$g$在0不连续，第二组$f$在$g(0)$不连续。解释这些反例是否否定CC1。[参考答案](#ccomp-a06)

#### 题7：孤立输出也能参与连续复合 {#ccomp-q07}

设$D=\{0\}\cup[1,2]$、$E=\{0,1\}$。定义$g:D\to\mathbb R$，$g(0)=0$、$g(x)=1$当$x\in[1,2]$；定义$f:E\to\mathbb R$，$f(0)=7$、$f(1)=-3$。证明$g$在$D$连续、$f$在$E$连续；核像包含并求新$h:D\to\mathbb R$的两支输出，证明它在$D$连续。不要为$E$的孤立点虚构去心点极限。[参考答案](#ccomp-a07)

#### 题8：局部一致和去心一致的分界 {#ccomp-q08}

设$c\in D$、$r_0>0$，$U=\{x\in D:|x-c|<r_0\}$。设$k:U\to\mathbb R$在$c$连续，$F:D\to\mathbb R$且$F|_U=k$。独立证明$F$在$c$连续。再用仅在0改变恒零函数点值的例子说明不能只要求去心一致。最后令$f:\mathbb R\to\mathbb R$满足$f(0)=1$、$f(y)=0$当$y\ne0$，令$g:\mathbb R\to\mathbb R$恒为0：核$f$在$y\to0$时的去心极限为0，但$h(x)=f(g(x))$在$x\to0$时的去心极限为1且不是0。说明CC1的哪一项没有满足。[参考答案](#ccomp-a08)
