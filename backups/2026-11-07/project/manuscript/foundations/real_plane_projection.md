## 基础单元 B2.38 正交、投影与最近点 {#planeproj-unit}

**学习目标与位置。** 平面距离已经从坐标平方和得到；直线也已同时具有参数与一次方程的描述。现在用两分量乘积和为零定义正交，构造任意点到一条真正直线的唯一垂足，并证明它也是唯一最近点。最后推导点到一般一次方程直线的距离。主归属第527章97G70“解析几何与向量代数（教育方面）”，交叉51N20欧氏解析几何；这里仍是实数坐标模型，不预设角度测量、一般内积空间或优化定理。

**精确先修。** 使用[函数定义](#fun-definition)、[有序对逐分量相等](#fun-pairs)、[实数坐标模型](#realplane-model)、[位移与点平移](#realplane-operations)、[参数直线及参数单射](#realplane-lines)、[非零方向的比例判据](#planeline-determinant)、[直线的一次方程](#planeline-equation)。实数代数和比较使用[加法群](#cutgroup-laws)、[序平移](#cutgroup-translation)、[取反与差](#cutgroup-negation-subtraction)、[乘法符号](#cutsigned-signs)、[乘法结合](#cutsigned-associative)、[有理相容及零积](#cutsigned-rational-zero)、[分配及差乘](#cutring-distributive)、[乘法序](#cutring-multiplication-order)、[消去](#cutring-cancellation)、[除法及乘回](#cutdiv-definition)、[非零系数方程](#cutdiv-equations)。还使用[实数平方比较](#realsqrt-square-order)、[唯一非负根](#realsqrt-function)、[绝对值](#realabs-definition-bounds)、[绝对值乘积](#realabs-products-triangle)、[二维点积与范数](#planedist-cauchy)、[范数规律](#planedist-norm-laws)、[平面距离](#planedist-metric)。不以本单元结论回证这些先修。

**类型与记号。** $P,X,H,Y$ 是点；$u,v,w,r,s$ 是位移记录，其底层数据同为实数有序对。点加位移得到点，两点之差得到位移。零位移为 $\mathbf0$，原点为 $O$。实数的普通运算沿用分割运算简写，数字为有理嵌入像。位移差已定义，点减位移尚未定义，所以需要从点移去一个位移时明确写点加相反位移。$u^\perp$ 将是一个新位移记号，不是前面有理坐标嵌入 $J$。

### 1. 两分量内积律与正交方向 {#planeproj-inner-orthogonal}

沿用函数

$$
u\cdot v=u_1v_1+u_2v_2,
\qquad
\|u\|^2=u\cdot u.
$$

此处也称这个两项乘积和为**内积**；所需规律仍须在两个实数分量中证明。定义关系

$$
u\perp v\quad\Longleftrightarrow\quad u\cdot v=0,
$$

称 $u$ 与 $v$ 正交。这是位移之间的代数关系，暂不表示一份未经定义的角度测量。

**命题 PP1。** 内积交换，对两输入的加法都分配，并与任意实数标量相容。零位移与每个位移正交。定义函数

$$
u\longmapsto u^\perp:=(-u_2,u_1)
\quad(\mathbb R^2\to\mathbb R^2).
$$

则 $u\perp u^\perp$。若固定 $u\ne\mathbf0$，则 $u^\perp\ne\mathbf0$，且任给位移 $v$，

$$
v\perp u
\quad\Longleftrightarrow\quad
\text{存在唯一实数 }\lambda\text{ 使 }v=\lambda u^\perp.
$$

这里允许 $v=\mathbf0$；该时唯一系数为零。

**内积律逐项证明。** 任取位移 $u,v,w$ 和实数 $t$。交换律给

$$
u\cdot v=u_1v_1+u_2v_2
=v_1u_1+v_2u_2=v\cdot u.
$$

对第一输入的和，分配并重排四个加项：

$$
\begin{aligned}
(u+v)\cdot w
&=(u_1+v_1)w_1+(u_2+v_2)w_2\\
&=u_1w_1+v_1w_1+u_2w_2+v_2w_2\\
&=(u_1w_1+u_2w_2)+(v_1w_1+v_2w_2)\\
&=u\cdot w+v\cdot w.
\end{aligned}
$$

第二输入也直接计算：

$$
\begin{aligned}
u\cdot(v+w)
&=u_1(v_1+w_1)+u_2(v_2+w_2)\\
&=u_1v_1+u_1w_1+u_2v_2+u_2w_2\\
&=(u_1v_1+u_2v_2)+(u_1w_1+u_2w_2)\\
&=u\cdot v+u\cdot w.
\end{aligned}
$$

标量相容在两侧分别为

$$
\begin{aligned}
(tu)\cdot v
&=(tu_1)v_1+(tu_2)v_2
=t(u_1v_1)+t(u_2v_2)=t(u\cdot v),\\
u\cdot(tv)
&=u_1(tv_1)+u_2(tv_2)
=t(u_1v_1)+t(u_2v_2)=t(u\cdot v).
\end{aligned}
$$

这里只用实数乘法交换结合与分配。取 $t=-1$，再用位移负号的分量定义，便得两侧取反内积也取反。结合两份加法分配，差式例如

$$
(u-v)\cdot w=u\cdot w-v\cdot w,
\qquad u\cdot(v-w)=u\cdot v-u\cdot w.
$$

零输入的两个分量相乘都为零，所以 $\mathbf0\cdot v=v\cdot\mathbf0=0$。交换律也证明正交关系对称。

**全部正交方向。** 直接代入得

$$
u\cdot u^\perp=u_1(-u_2)+u_2u_1
=-u_1u_2+u_1u_2=0.
$$

若 $u^\perp=\mathbf0$，则 $-u_2=0$、$u_1=0$，从而 $u=\mathbf0$。所以非零 $u$ 给非零 $u^\perp$。前一单元对任意位移对定义了 $D$；逐分量有

$$
D(u^\perp,v)=(-u_2)v_2-u_1v_1
=-(u_1v_1+u_2v_2)=-u\cdot v.
$$

固定 $u\ne\mathbf0$ 后，$u^\perp$ 是可用PL1的非零第一方向。因此 $v\perp u$ 当且仅当 $D(u^\perp,v)=0$，再当且仅当 $v$ 是 $u^\perp$ 的唯一实数倍。反向也可由标量相容直接核正交。$v=\mathbf0$ 时系数零给存在，唯一性排除其他系数。若 $u=\mathbf0$，所有 $v$ 都与它正交，而 $u^\perp=\mathbf0$ 的倍数只有零；所以这个非零条件不能删。PP1证毕。

### 2. 一条直线上的唯一垂足 {#planeproj-foot}

固定点 $P$ 和非零位移 $u$，令

$$
L=L(P,u)=\{P+tu:t\in\mathbb R\}.
$$

给任意点 $X$，记 $w=X-P$。先核

$$
N=u\cdot u=\|u\|^2>0.
$$

因为 $u\ne\mathbf0$，范数零判据和非负性给 $\|u\|>0$，正数平方严格正。所以以下商合法：

$$
t_0=\frac{w\cdot u}{N},\qquad H=P+t_0u.
$$

**命题 PP2。** $H$ 是直线 $L$ 上唯一满足 $(X-H)\perp u$ 的点，称为 $X$ 在 $L$ 上的**正交投影点**或**垂足**。固定 $P,u$ 后，这给函数

$$
\Pi_{P,u}:\mathbb R^2\longrightarrow L(P,u),
\qquad \Pi_{P,u}(X)=H.
$$

**存在。** 商给唯一实数 $t_0$，故 $H$ 确属 $L$。逐坐标有

$$
x_j-(p_j+t_0u_j)=(x_j-p_j)-t_0u_j=w_j-t_0u_j
\qquad(j=1,2).
$$

所以 $X-H=w-t_0u$。PP1与商的乘回给

$$
(X-H)\cdot u
=(w-t_0u)\cdot u
=w\cdot u-t_0(u\cdot u)
=w\cdot u-w\cdot u=0.
$$

存在性已证。

**唯一。** 任取 $K\in L$ 且 $(X-K)\cdot u=0$。成员定义给某个实数 $t$ 使 $K=P+tu$。同样的两个坐标差计算及内积差式给

$$
0=(X-K)\cdot u=w\cdot u-tN,
\qquad Nt=w\cdot u.
$$

系数 $N>0$，该乘法方程唯一解为 $t=t_0$，因此 $K=P+t_0u=H$。这还与非零方向的参数单射相符，未将参数存在误当成唯一。

**线上输入的退化。** 若 $X\in L$，则点 $X$ 自身满足 $X-X=\mathbf0\perp u$；刚证唯一性给 $H=X$。反过来，若 $H=X$，因 $H\in L$，也有 $X\in L$。此时残差为零。零残差与 $u$ 正交完全合法，但不能称其为一条非零垂线方向。PP2证毕。

### 3. 勾股恒等式与最近点唯一性 {#planeproj-nearest}

**命题 PP3。** 任意位移 $r,s$ 满足

$$
r\perp s
\quad\Longleftrightarrow\quad
\|r+s\|^2=\|r\|^2+\|s\|^2.
$$

这称为本坐标模型内的**勾股恒等式及其逆命题**，允许任一位移为零。对PP2的 $X,H,t_0$，任意 $Y=P+tu\in L$ 满足

$$
d_2(X,Y)^2=d_2(X,H)^2+(t-t_0)^2\|u\|^2.
$$

从而 $d_2(X,H)\le d_2(X,Y)$，且相等当且仅当 $Y=H$。所以垂足是直线上的唯一最近点。

**恒等式的双向。** 两个坐标分别用实数平方展开：

$$
\begin{aligned}
\|r+s\|^2
&=(r_1+s_1)^2+(r_2+s_2)^2\\
&=r_1^2+2r_1s_1+s_1^2+r_2^2+2r_2s_2+s_2^2\\
&=(r_1^2+r_2^2)+(s_1^2+s_2^2)+2(r_1s_1+r_2s_2)\\
&=\|r\|^2+\|s\|^2+2(r\cdot s).
\end{aligned}
$$

若 $r\cdot s=0$，即得所述平方等式。反过来，若该平方等式成立，同减两个平方和得 $2(r\cdot s)=0$。实数 $2>0$，由非零消去给 $r\cdot s=0$。证明没有除以任何范数；零位移时两方向仍成立。

**任意线上点的平方差。** 记 $e=X-H$，PP2给 $e\cdot u=0$。因为

$$
H-Y=((p_1+t_0u_1)-(p_1+tu_1),
      (p_2+t_0u_2)-(p_2+tu_2))
=((t_0-t)u_1,(t_0-t)u_2),
$$

故 $H-Y=(t_0-t)u$。PP1给 $e\cdot(H-Y)=(t_0-t)(e\cdot u)=0$。两个坐标还分别有

$$
(x_j-h_j)+(h_j-y_j)=x_j-y_j\qquad(j=1,2),
$$

所以 $X-Y=(X-H)+(H-Y)$。刚证勾股恒等式给

$$
\|X-Y\|^2=\|X-H\|^2+\|H-Y\|^2.
$$

距离定义写的是点差的另一个方向，但范数取反不变给 $\|X-Y\|=d_2(X,Y)$，同理 $\|X-H\|=d_2(X,H)$。由范数倍率和绝对值平方，

$$
\|H-Y\|^2
=\bigl(|t_0-t|\,\|u\|\bigr)^2
=(t_0-t)^2\|u\|^2
=(t-t_0)^2\|u\|^2.
$$

中间一步重排四个实数因子并用 $|z|^2=z^2$，末步用取反不改变平方。所求平方差公式得证。

该额外项非负，因此两个距离平方满足弱比较；距离本身都非负，平方反映给最近点不等式。距离相等当且仅当平方相等，也当且仅当

$$
(t-t_0)^2\|u\|^2=0.
$$

因 $\|u\|^2=N>0$，非零消去及平方零判据给 $t=t_0$。非零方向的参数单射给 $t=t_0$ 当且仅当 $Y=H$。因此最近点唯一，既包括不在线上的 $X$，也包括 $X=H$、最小距离为零的情形。PP3证毕。

### 4. 点到一次方程直线的距离 {#planeproj-line-distance}

对一条真正直线 $L$，定义函数

$$
\operatorname{dist}_L:\mathbb R^2\to\mathbb R_{\ge0},
\qquad \operatorname{dist}_L(X)=d_2(X,H),
$$

其中 $H$ 是刚证明的唯一最近点。这是已经达到的最小值，不使用尚未定义的下确界。若用不同基点和方向表示同一集合 $L$，PP3所刻画的“属于 $L$ 且对所有 $Y\in L$ 距离最小”是同一条件，其唯一性使所得点与数值相同；所以记号依赖直线集合，而不依赖参数表示。

**命题 PP4。** 给实数 $a,b,c$，其中 $a,b$ 不全为零，令

$$
L=\{(y_1,y_2)\in\mathbb R^2:ay_1+by_2=c\}.
$$

对任意点 $X=(x_1,x_2)$，

$$
\operatorname{dist}_L(X)
=\frac{|ax_1+bx_2-c|}{\sqrt{a^2+b^2}}.
$$

分母严格为正。若把三个系数同时乘任意非零实数 $\lambda$，直线集合与此距离值均不变。

**构造并核垂足。** PL2已给直线的基点存在：$a\ne0$ 时可取 $P=(c/a,0)$；$a=0$ 时有 $b\ne0$，可取 $P=(0,c/b)$。令

$$
n=(a,b),\qquad u=(-b,a),\qquad
N=n\cdot n=a^2+b^2,\qquad s=\|n\|=\sqrt N.
$$

$n\ne\mathbf0$，故 $N>0$、$s>0$ 且 $s^2=N$。$u\ne\mathbf0$，PL2给 $L=L(P,u)$；直接计算 $n\cdot u=-ab+ba=0$，故称 $n$ 为这个方程的一条**法向位移**。

记实数

$$
E=ax_1+bx_2-c=n\cdot(X-P),\qquad
\rho=E/N.
$$

这里第二等号用 $ap_1+bp_2=c$ 及两次分配差式。定义点

$$
K=X+(-\rho n)=(x_1-\rho a,x_2-\rho b).
$$

这是点加位移的已有运算。逐项代回方程：

$$
\begin{aligned}
a(x_1-\rho a)+b(x_2-\rho b)
&=ax_1+bx_2-\rho(a^2+b^2)\\
&=ax_1+bx_2-\rho N\\
&=ax_1+bx_2-E=c.
\end{aligned}
$$

其中 $\rho N=E$ 由合法商乘回。因此 $K\in L$。两个坐标分别相减给 $X-K=(\rho a,\rho b)=\rho n$；PP1又给 $(X-K)\cdot u=\rho(n\cdot u)=0$。PP2的唯一性迫 $K=H$。

**把倍率值化为商。** 距离对称及范数倍率给

$$
\operatorname{dist}_L(X)=\|X-K\|=\|\rho n\|=|\rho|s.
$$

从 $\rho N=E$ 取实数绝对值，乘积相容及 $N>0$ 给 $|\rho|N=|E|$。因此

$$
s(|\rho|s)=|\rho|s^2=|\rho|N=|E|.
$$

系数 $s>0$，乘法方程 $sZ=|E|$ 的唯一解为 $Z=|E|/s$。所以 $|\rho|s=|E|/s$，得所述公式。这里没有使用一般的开根乘积或商公式；$E=0$ 时 $\rho=0$、$K=X$、两边距离零，也完全包含。

**系数同时缩放。** 设 $\lambda\ne0$。由分配和非零消去，

$$
(\lambda a)y_1+(\lambda b)y_2=\lambda c
\quad\Longleftrightarrow\quad ay_1+by_2=c.
$$

新法向为 $\lambda n\ne\mathbf0$，其范数为 $|\lambda|s>0$；新分子为 $|\lambda E|=|\lambda||E|$。令 $D=|E|/s$，乘回 $sD=|E|$，于是

$$
(|\lambda|s)D=|\lambda|(sD)=|\lambda||E|.
$$

新正分母对应的方程唯一性说明新商也为 $D$。若 $\lambda=0$，方程变成 $0=0$，解集为全平面，已不是真正直线，且距离公式分母变零，不可使用。原直线确非全平面：对其基点 $P$，点 $P+n$ 代入左侧为 $c+N\ne c$。

**精确算例。** 原点到 $x_1+x_2=2$：$n=(1,1)$、$N=2$、$E=-2$、$\rho=-1$，故 $H=O+(-\rho n)=(1,1)$，距离 $\sqrt2$。商式给 $2/\sqrt2$，乘回 $\sqrt2\sqrt2=2$ 说明它等于 $\sqrt2$，不是凭根式形式约去。原点到 $x_1=3$：$n=(1,0)$、$N=1$、$E=-3$、$\rho=-3$，故 $H=(3,0)$，距离 $3$。所有数字简写有理数的实数像。PP4证毕。

![一次方程直线上的正交投影与平方距离分解](figures/b2_real_plane_projection.png)

图取 $L:x_1+x_2=2$、$P=(0,2)$、$u=(1,-1)$、$X=(0,0)$。此时 $w=(0,-2)$、$u\cdot u=2$、$w\cdot u=2$，所以投影参数 $t_0=1$，垂足 $H=(1,1)$。另取线上点 $Y=(2,0)=P+2u$，平方距离满足 $4=2+2$，与PP3的全称公式一致。数字简写有理数的实数像；最短与唯一性来自正文证明，线条外观不定义角度或正交。精确有理算例及完整程序见[正交投影图代码](#real-projection-figure-code)。

### 5. 课后题 {#planeproj-exercises}

#### 题1：内积律与零正交 {#planeproj-q01}

对任意位移 $u,v,w$ 和实数 $t$，逐两分量证明内积交换、两侧加法分配、两侧标量相容及差式。定义正交，证明关系对称与零位移同每个位移正交，说明这不预设角度测量。[完整解答](#planeproj-a01)

#### 题2：固定非零方向的全部正交位移 {#planeproj-q02}

固定 $u\ne\mathbf0$，定义 $u^\perp=(-u_2,u_1)$。证明它非零且与 $u$ 正交；逐算 $D(u^\perp,v)=-u\cdot v$，利用PL1证明 $v\perp u$ 当且仅当存在唯一 $\lambda$ 使 $v=\lambda u^\perp$。处理 $v=\mathbf0$，并给出删去 $u\ne\mathbf0$ 后失败的实例。[完整解答](#planeproj-a02)

#### 题3：垂足的分母、存在与唯一 {#planeproj-q03}

给 $L=L(P,u)$、$u\ne\mathbf0$ 与任意点 $X$。证明 $N=u\cdot u>0$，使 $t_0=((X-P)\cdot u)/N$ 合法。逐坐标与内积律证明 $H=P+t_0u$ 在直线上且残差正交，再从任意另一候选推出相同参数。写出固定 $P,u$ 时投影函数的域、目标及规则。[完整解答](#planeproj-a03)

#### 题4：线上输入与零残差 {#planeproj-q04}

在题3条件下，证明 $X\in L$ 当且仅当 $H=X$，也当且仅当 $X-H=\mathbf0$。若 $X=P+qu$，直接计算投影参数为 $q$；说明为什么此时仍有正交关系，却没有从零残差得到非零垂线方向。[完整解答](#planeproj-a04)

#### 题5：勾股恒等式的双向与零边界 {#planeproj-q05}

对任意位移 $r,s$，完整展开两坐标平方，证明 $r\perp s$ 当且仅当 $\|r+s\|^2=\|r\|^2+\|s\|^2$。逆向写清非零系数，分别核 $r=\mathbf0$ 或 $s=\mathbf0$，不除以范数。[完整解答](#planeproj-a05)

#### 题6：最近点的完整平方差 {#planeproj-q06}

在题3条件下，任取 $Y=P+tu$，逐坐标证明 $X-Y=(X-H)+(H-Y)$ 与 $H-Y=(t_0-t)u$。用正交及题5得到PP3平方差式，再证明距离最小与等号恰在 $Y=H$；覆盖 $X\in L$ 的情形。[完整解答](#planeproj-a06)

#### 题7：一般一次方程的距离公式 {#planeproj-q07}

给实数 $a,b,c$，$a,b$ 不全为零。任给点 $X=(x_1,x_2)$。先构造直线 $ax_1+bx_2=c$ 的基点及方向，再以 $n=(a,b)$、$\rho=(ax_1+bx_2-c)/(n\cdot n)$ 构造点 $K=X+(-\rho n)$。逐项证它是唯一垂足，并用正分母乘回推距离公式。写出距离函数的域、目标与达到最小值的含义，单列分子零，不用未证开根商式。[完整解答](#planeproj-a07)

#### 题8：精确实例、系数缩放与零反例 {#planeproj-q08}

计算原点到 $x_1+x_2=2$ 和 $x_1=3$ 的垂足与距离，核商式和直接范数值一致。对任意非零实数 $\lambda$，证明同时缩放一次方程三个系数不改变直线集合与距离公式值；再说明 $\lambda=0$ 时哪个条件失败，并证原直线并非全平面。[完整解答](#planeproj-a08)

**来源与范围说明。** 定义与证明义务的公开材料条件对照见[本批来源审计](#real-lines-projection-sources)。本单元的分量推导、练习和完整答案独立编写。正交与最近点在坐标模型内由已证实数规则推出，不以图形或外部几何定理代替证明。
