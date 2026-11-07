## 基础单元 B4.7 实函数在定义域内的连续性 {#cont-unit}

**位置与目标。** 本单元主归第146章26A15连续性基础，交叉97I20函数教学。先把点极限与点值接起来，再证明连续性在限制域和有限运算下怎样保留。所论对象都是实数子集上的实值函数；不引入复合的连续性定理、序列判据、介值或极值定理、紧致性、一致连续性、导数和积分。本单元完成不表示26A15整节或第146章已完成。

**精确先修。** 使用[条件子集](#fun-sets)、[函数及求值的定义域](#fun-definition)、[函数相等的三项记录](#fc-equality)、[限制函数及输出](#fc-restriction)、[恒等函数定义](#fc-identity)。实数部分使用[加法群](#cutgroup-laws)、[平移保序](#cutgroup-translation)、[取反与差](#cutgroup-negation-subtraction)、[乘法符号及单位](#cutsigned-signs)、[乘法结合](#cutsigned-associative)、[零积](#cutsigned-rational-zero)、[实数分配与差乘](#cutring-distributive)、[乘法比较](#cutring-multiplication-order)、[合法商及乘回](#cutdiv-definition)、[非零系数方程唯一解](#cutdiv-equations)、[正倒数反序](#cutdiv-order)、[绝对值基本界](#realabs-definition-bounds)、[乘商、三角与反三角](#realabs-products-triangle)及[实数线距](#realabs-distance)。点极限接口是[积点](#flim-domain-cluster)、[去心极限定义](#flim-definition)、[唯一性FL1](#flim-uniqueness)与[局部相同FL3](#flim-basic-local)。下面的连续有限运算直接从定义证明，不把积点处的极限运算未经检查套到孤立点。

**阅读安排。** 本单元预计教学正文约10—16页，答案另计。可分两次阅读：先读定义、孤立点和限制，再读有限运算及商域；第二段复用第一段的连续定义及限制结论。

**对象与记号。** $D,E$为实数子集，$f,g:D\to\mathbb R$为全定义在$D$上的函数；“全定义”不表示$D$必须等于全体实数。$x,c,b,a,\varepsilon,\delta$均为实数，误差$\varepsilon$与半径$\delta$要求为正。数字常量均为实数中的有理像。$f$在一点连续时，该点必须属于$D$，否则$f(c)$没有定义。

### 1. 连续控制到实际点值的误差 {#cont-definition}

**入口。** 点极限只观察靠近$c$却不等于$c$的输入；连续性还要求这些输出接近已经指定的$f(c)$。因此，点值是否存在、指定了什么值、输入从哪个域中靠近，都是问题的一部分。

**定义。** 设$f:D\to\mathbb R$且$c\in D$。称$f$在$c$处连续，是指

$$
\begin{gathered}
\forall\varepsilon>0\ \exists\delta>0\ \forall x\in D,\\
|x-c|<\delta\Longrightarrow |f(x)-f(c)|<\varepsilon.
\end{gathered}
$$

这个条件不去心：允许$x=c$，此时输出误差为零。它也不要求$c$是积点。$\delta$可以依赖固定的$f,D,c,\varepsilon$，不能依赖后来任取的$x$。它只约束属于$D$的输入，不为域外的$x$补定义。

在已知$c\in D$时，**不连续**是上述条件的否定：

$$
\begin{gathered}
\exists\varepsilon_0>0\ \forall\delta>0\ \exists x\in D,\\
|x-c|<\delta\quad\text{且}\quad |f(x)-f(c)|\ge\varepsilon_0.
\end{gathered}
$$

逐层否定量词给该式。输出误差$\varepsilon_0$固定，坏输入可以随$\delta$变化；由于$\varepsilon_0>0$，任何坏输入必有$x\ne c$，但这是从坏误差推出的结论，不是连续定义预先排除了$c$。

若对每个$c\in D$都连续，就称$f$**在$D$上连续**。空定义域函数没有域内点，故这项全称条件成立；不能由此说它在任意实数$c$处连续，因为那些$f(c)$没有定义。若$c\notin D$，本单元不把“在$c$处不连续”用来代替“这里未定义”。

**合并两个半径。** 沿用FL1的实数二元较小者：$r\le s$时取$\min(r,s)=r$，否则取$s$。若$r,s>0$，两支都给$\min(r,s)>0$且不大于两个输入。多个正半径可以反复取二元较小者；这不是数列阈值中的自然数最大值。

### 2. 孤立点与积点分别怎样判断 {#cont-isolated-limit}

**定义。** 若$c\in D$，且存在$r_0>0$使

$$
x\in D,\quad |x-c|<r_0\quad\Longrightarrow\quad x=c,
$$

就称$c$是$D$的**孤立点**。在域内点的前提下，孤立与不是积点等价：不是积点给某个正半径内没有去心输入；在这个半径内任取输入，若不等于$c$，绝对值零判据便给正距离，造成矛盾。反向，孤立半径内只有$c$，去心后没有输入，故不满足积点条件。这里用的是经典量词否定。

**命题 CT1。** 任意函数$f:D\to\mathbb R$在每个孤立点连续。若$c\in D$同时是$D$的积点，则

$$
f\text{在}c\text{处连续}
\quad\Longleftrightarrow\quad
f(x)\longrightarrow f(c)\quad(x\to c,\ x\in D).
$$

**孤立点的证明。** 固定一个隔离半径$r_0>0$。任给$\varepsilon>0$，取$\delta=r_0$。若$x\in D$且$|x-c|<\delta$，孤立条件给$x=c$，所以$|f(x)-f(c)|=0<\varepsilon$。这对任意点值都成立，因而得到连续性。

**积点处的正向。** 若连续，对每个$\varepsilon$取其半径；满足$0<|x-c|<\delta$的输入也满足$|x-c|<\delta$，故输出误差小于$\varepsilon$。积点条件已经保证点极限定义可以使用，所以极限为$f(c)$。

**积点处的反向。** 若点极限为$f(c)$，给$\varepsilon>0$取去心极限的半径$\delta$。任取$x\in D$且$|x-c|<\delta$。若$x=c$，输出误差为零；若$x\ne c$，零判据给$0<|x-c|<\delta$，使用极限条件得误差小于$\varepsilon$。两支穷尽，故连续。CT1证毕。

**三个不同场景。** $D=\{0\}$上的任意函数都在0连续，但0不是积点，本书不在这里赋予去心点极限。$D=\{x\in\mathbb R:x>0\}$上的$f(x)=x$在0有极限0，但$f(0)$没有定义，不能讨论它在0的连续性。最后，若$D=\mathbb R$，规定$p(0)=1$、$p(x)=0$当$x\ne0$，则0是积点，去心极限为0，而点值为1；它在0不连续。后一结论也可直接检验：固定$\varepsilon_0=1/2$，对任意$\delta>0$取$x=\delta/2$，便有$0<|x|<\delta$且$|p(x)-p(0)|=1\ge\varepsilon_0$。

### 3. 基本函数与限制定义域 {#cont-basic-restriction}

**命题 CT2。** 对任意$D\subseteq\mathbb R$，常数函数$C_b(x)=b$、实值包含函数$u_D(x)=x$及$A_D(x)=|x|$均在$D$上连续。若$f:D\to\mathbb R$在$c\in D$连续，$E\subseteq D$且$c\in E$，则$f|_E:E\to\mathbb R$在$c$连续。

这些规则每个合法输入都有唯一实数输出，故确为所列函数。$u_D$准确地说是$\operatorname{id}_{\mathbb R}|_D:D\to\mathbb R$；当$D\ne\mathbb R$时，它与目标为$D$的$\operatorname{id}_D$不是同一三项函数记录。这里保持实数目标，不默改函数的第二项数据。

**三个基本证明。** 固定$c\in D$。常数情形，任给$\varepsilon>0$取$\delta=1$，输出误差恒为零。包含函数情形取$\delta=\varepsilon$，则$|u_D(x)-u_D(c)|=|x-c|<\varepsilon$。绝对值情形也取$\delta=\varepsilon$，反三角不等式给

$$
|A_D(x)-A_D(c)|=\bigl||x|-|c|\bigr|\le|x-c|<\varepsilon.
$$

以上都是对任意$x\in D$且$|x-c|<\delta$的证明，允许$x=c$及孤立的$c$。

**限制的证明。** 给$\varepsilon>0$，用$f$在$c$的连续性取$\delta$。若$x\in E$且$|x-c|<\delta$，由$E\subseteq D$有$x\in D$；又$c\in E$保证限制在$c$有值。FC2给

$$
|(f|_E)(x)-(f|_E)(c)|=|f(x)-f(c)|<\varepsilon.
$$

同一半径适用，证明完成。未要求$c$是$E$或$D$的积点。若$E$为空，就没有可以讨论的$c\in E$；全域连续的陈述按空域规则处理。

**限制的逆向一般不成立。** 定义$s:\mathbb R\to\mathbb R$，当$x\le0$时$s(x)=0$，当$x>0$时$s(x)=1$。实数全序保证两支互斥且穷尽，故函数合法。在$E=\{x\in\mathbb R:x\le0\}$上，限制为常数零，因而在0连续。原函数在0却不连续：固定$\varepsilon_0=1/2$，对任意$\delta>0$取$x=\delta/2>0$，有$|x|<\delta$而$|s(x)-s(0)|=1$。被限制删去的正输入正是这些坏输入。

### 4. 同一点的有限运算 {#cont-algebra}

假设$f,g:D\to\mathbb R$在同一个$c\in D$连续。逐点定义$f+g$、$af$、$f-g$、$|f|$和$fg$，其输出依次为$f(x)+g(x)$、$af(x)$、$f(x)-g(x)$、$|f(x)|$及$f(x)g(x)$。所有运算在实数域内处处合法，故得到共同定义域$D$、目标$\mathbb R$的函数。

**命题 CT3。** 上述五种函数均在$c$连续，其中$a$为任意固定实数，包括零。

**和。** 任给$\varepsilon>0$，分别对$f,g$取输出误差$\varepsilon/2$的正半径，再取共同较小者$\delta>0$。任取$x\in D$且$|x-c|<\delta$，由群律和三角不等式，

$$
\begin{aligned}
|(f+g)(x)-(f+g)(c)|
&=|(f(x)-f(c))+(g(x)-g(c))|\\
&\le |f(x)-f(c)|+|g(x)-g(c)|<\varepsilon.
\end{aligned}
$$

**常数倍。** 若$a=0$，函数恒零，由CT2连续。若$a\ne0$，绝对值零判据给$|a|>0$。对$f$取正误差$\varepsilon/|a|$的半径$\delta$；在其中，

$$
|af(x)-af(c)|=|a|\,|f(x)-f(c)|
<|a|\frac{\varepsilon}{|a|}=\varepsilon.
$$

乘严格不等式的是正数$|a|$，所以$a<0$时也成立。零因子已另证，没有除以零。

**差与绝对值。** 对$g$用系数$-1$的常数倍结论，得到$-g$在$c$连续；再将$f$与$-g$代入已证和的结论，得到$f-g$连续，值为$f(c)-g(c)$。对$|f|$，给$\varepsilon>0$直接沿用$f$的半径，使用

$$
\bigl||f(x)|-|f(c)|\bigr|\le|f(x)-f(c)|<\varepsilon.
$$

这证明绝对值函数在$c$的误差条件。

**乘积先取局部界。** 对$f$取误差1的正半径$r_0$。若$x\in D$且$|x-c|<r_0$，则

$$
|f(x)|\le |f(x)-f(c)|+|f(c)|<1+|f(c)|.
$$

记$B=1+|f(c)|>0$，再取$K=B+|g(c)|+1>0$。在这个邻域内有$|f(x)|\le K$，且$|g(c)|\le K$。此界包括$x=c$，却不声称控制整个定义域。

给$\varepsilon>0$，令$\eta=\varepsilon/(2K)>0$。分别取$f,g$对误差$\eta$的半径$r_f,r_g$，令

$$
\delta=\min(r_0,\min(r_f,r_g))>0.
$$

对任意$x\in D$且$|x-c|<\delta$，分配律与交换律给

$$
f(x)g(x)-f(c)g(c)
=f(x)(g(x)-g(c))+g(c)(f(x)-f(c)).
$$

确实，右侧展开后中间两项$-f(x)g(c)+g(c)f(x)$相消。三角及绝对值乘积给

$$
|f(x)g(x)-f(c)g(c)|
\le |f(x)|\,|g(x)-g(c)|+|g(c)|\,|f(x)-f(c)|.
$$

第一项不超过$K|g(x)-g(c)|<K\eta=\varepsilon/2$；第二项不超过$K|f(x)-f(c)|<K\eta=\varepsilon/2$。弱放大使用非负误差，严格步使用$K>0$，所以某个函数值为零也不影响推理。两项合计小于$\varepsilon$，乘积连续。CT3证毕。

例如$p(x)=x^2-3x+2$在$\mathbb R$上连续：同域实值恒等函数与自身相乘给$x^2$连续，常数倍给$-3x$连续，两次和再加入常数二。对任意$c$，这些结论都以该点的实际值$p(c)$为比较中心；不需要借用尚未建立的多项式总定理。

### 5. 分母在该点非零，还要写对商域 {#cont-quotient}

**命题 CT4。** 设$f,g:D\to\mathbb R$在$c\in D$连续，且$g(c)\ne0$。定义

$$
H=\{x\in D:g(x)\ne0\}.
$$

则$c\in H$。在$H$上定义$r(x)=1/g(x)$及$q(x)=f(x)/g(x)$，二者都在$c$连续。结论不要求$g$在远处也非零，不把商定义到$D\setminus H$上。

**先保证附近输入有合法分母。** 令$h=|g(c)|>0$，由$g$连续，取误差$h/2>0$的半径$r_0$。当$x\in D$且$|x-c|<r_0$时，反三角与绝对值基本界给

$$
h-|g(x)|\le\bigl|h-|g(x)|\bigr|
\le|g(c)-g(x)|<h/2.
$$

移项得$|g(x)|>h/2>0$，故$g(x)\ne0$。所有这些域内邻近输入都属于$H$，包括$c$；这是一份局部保证。

**倒数的误差。** 给$\varepsilon>0$，对$g$再取正误差$\varepsilon h^2/2$的半径$r_1$，令$\delta=\min(r_0,r_1)>0$。任取$x\in H$且$|x-c|<\delta$。两个分母$g(x),g(c)$均非零，乘积也非零。分配、交换与乘回给

$$
\left(\frac1{g(x)}-\frac1{g(c)}\right)g(x)g(c)=g(c)-g(x).
$$

由非零系数方程唯一解，再取绝对值，得到

$$
|r(x)-r(c)|
=\frac{|g(c)-g(x)|}{|g(x)|h}.
$$

因$|g(x)|h>h^2/2>0$，正倒数反序与非负分子给

$$
|r(x)-r(c)|
\le\frac2{h^2}|g(c)-g(x)|
<\frac2{h^2}\frac{\varepsilon h^2}{2}=\varepsilon.
$$

第一步保留弱不等式，因为分子可能为零；第二步的系数正。倒数因此在$c$连续，孤立点也包含在证明内。

**商。** CT2给$f|_H$在$c$连续；刚证$r:H\to\mathbb R$也在$c$连续。对这两个同域函数用CT3的乘积结论，得到$(f|_H)r$连续。合法商的定义逐点给$(f|_H)(x)r(x)=f(x)/g(x)=q(x)$；两者同域同目标，故是同一函数。因此$q$连续。CT4证毕。

若$g(c)=0$，则$c\notin H$，该商在$c$根本没有值，不能把CT4代入零分母。若希望补一个点值，必须另外定义扩大的函数，并检查它是否连续；不能以“可以约分”把原函数的域无声扩大。题8给出一个完整例子。

### 6. 课后题 {#cont-exercises}

#### 题1：量词与域内点 {#cont-q01}

写出在已知$c\in D$时不连续的准确否定。有人先任取$x\ne c$，再选$\delta=|x-c|/2$，据此前件不成立断言“所有函数连续”，指出错误。解释空域函数在域上连续，为什么不表示它在0处有一个连续点值。

[查看完整解答](#cont-a01)

#### 题2：孤立点与端点处的域限制 {#cont-q02}

先证明任意单点域$\{c\}$上的函数在$c$连续，并说明本书为何不在此定义去心点极限。再令$D=\{0\}\cup[1,2]$，其中$[1,2]=\{x\in\mathbb R:1\le x\le2\}$。规定$f(0)=7$，$x\in[1,2]$时$f(x)=x$。证明这是函数$D\to\mathbb R$，0是孤立点，且$f$在$D$上连续。对$c\in[1,2]$给明确正半径，包含$c=1,2$。

[查看完整解答](#cont-a02)

#### 题3：零斜率与绝对值 {#cont-q03}

固定实数$a,b$与$D\subseteq\mathbb R$，定义$u(x)=ax+b$、$v(x)=|ax+b|$。不用CT3，直接证明它们在每个$c\in D$连续；分别核$a=0$、$a\ne0$以及负$a$；再明确常数、实值包含函数与$|x|$对应哪些参数；说明何时该包含函数也是恒等函数。

[查看完整解答](#cont-a03)

#### 题4：限制保留连续，但逆向可能失败 {#cont-q04}

证明CT2中的限制结论，明确$c\in E\subseteq D$的作用。对正文的阶跃规则$s(x)=0$（$x\le0$）、$s(x)=1$（$x>0$），证明$s|_{\{x:x\le0\}}$在0连续而$s$在0不连续。用一个固定误差和每个半径内的实际坏输入完成反例。

[查看完整解答](#cont-a04)

#### 题5：去心极限、点值与未定义位置 {#cont-q05}

先对一般$f:D\to\mathbb R$及属于$D$的积点$c$，完整证明连续当且仅当点极限为$f(c)$。再定义$p:\mathbb R\to\mathbb R$，$p(0)=1$而$x\ne0$时$p(x)=0$，证明其在0的点极限为0却不连续。再令$E=\mathbb R\setminus\{0\}$，核0是$E$积点，并说明$p|_E$在0的极限及“在0连续”是否可按本单元定义讨论。最后把$p(0)$改成0，检查新函数的连续性。

[查看完整解答](#cont-a05)

#### 题6：乘积的局部界与一个具体函数 {#cont-q06}

设$f,g:D\to\mathbb R$在$c\in D$连续。直接证明$fg$在$c$连续，要求先给一份包括中心的局部界，且证明允许$f(c)=0$或$g(c)=0$。随后逐步用已证规则说明$x^2-3x+2$在每个实数$c$连续，不调用未写的“所有多项式连续”定理。

[查看完整解答](#cont-a06)

#### 题7：倒数与商的实际定义域 {#cont-q07}

设$g:D\to\mathbb R$在$c\in D$连续且$g(c)\ne0$。证明存在正半径使邻近域内输入满足$|g(x)|>|g(c)|/2$；在$H=\{x\in D:g(x)\ne0\}$上证明$1/g$在$c$连续。再写出$q(x)=(x^2+1)/(x-2)$的实际实数定义域，并逐条件证明它在那里连续。能否称这份$q$在2连续？

[查看完整解答](#cont-a07)

#### 题8：约分与补点是两件事 {#cont-q08}

对固定$b\in\mathbb R$，定义$F_b:\mathbb R\to\mathbb R$：当$x\ne1$时$F_b(x)=(x^2-1)/(x-1)$，当$x=1$时$F_b(1)=b$。证明函数合法，在每个$c\ne1$处连续，在1处的点极限为2，并证明它在1连续当且仅当$b=2$。原来的商函数与$F_2$是否为同一函数记录？写明定义域的区别。

[查看完整解答](#cont-a08)

**来源与范围。** 标准定义、孤立点和积点处关系对照Jiří Lebl《Basic Analysis I》6.3固定提交`e21ec524ca7d54f800c693b948020c188d21d01f`的[连续函数章](https://github.com/jirilebl/ra/blob/e21ec524ca7d54f800c693b948020c188d21d01f/ch-contfunc.tex)。本单元作者实际读取该固定源码第739—905行及许可全文；公开源为CC BY-SA 4.0或CC BY-NC-SA 4.0双许可，实际缓存、哈希与阅读范围见本批来源记录。源书同段的序列判据和一般多项式论证不列本轮成果；本书直接给误差证明。正文、例子和八道题答独立编写，不分发外部源码或复制题解。有限运算证明从不去心的连续定义出发，覆盖孤立点；积点处才用点极限与点值的关系。这里没有以“图像不断开”替代定义，也没有提前使用后续全局定理。
