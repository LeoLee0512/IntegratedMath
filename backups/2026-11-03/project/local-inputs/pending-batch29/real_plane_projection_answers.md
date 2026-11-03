## 基础单元 B2.38 课后题完整解答 {#planeproj-answers}

以下解答对应[正交、投影与最近点](#planeproj-unit)。点与位移的角色沿用正文；坐标和标量为实数，普通运算是已建立的实数运算简写，数字指有理数的实数像。点减点为位移；需从点移去位移时写点加相反位移。

### 题1完整解答：内积律与零正交 {#planeproj-a01}

[返回题目](#planeproj-q01)

给位移 $u=(u_1,u_2)$、$v=(v_1,v_2)$、$w=(w_1,w_2)$ 和实数 $t$。交换两个输入：

$$
u\cdot v=u_1v_1+u_2v_2=v_1u_1+v_2u_2=v\cdot u,
$$

这里只用了每个实数乘积的交换律。

第一输入的加法分配为

$$
\begin{aligned}
(u+v)\cdot w
&=(u_1+v_1)w_1+(u_2+v_2)w_2\\
&=u_1w_1+v_1w_1+u_2w_2+v_2w_2\\
&=(u_1w_1+u_2w_2)+(v_1w_1+v_2w_2)\\
&=u\cdot w+v\cdot w.
\end{aligned}
$$

第二输入的加法分配也逐项核：

$$
\begin{aligned}
u\cdot(v+w)
&=u_1(v_1+w_1)+u_2(v_2+w_2)\\
&=u_1v_1+u_1w_1+u_2v_2+u_2w_2\\
&=(u_1v_1+u_2v_2)+(u_1w_1+u_2w_2)\\
&=u\cdot v+u\cdot w.
\end{aligned}
$$

两份计算中，四项展开用实数分配，重新分组用加法交换结合。

标量在第一侧时，

$$
\begin{aligned}
(tu)\cdot v
&=(tu_1)v_1+(tu_2)v_2\\
&=t(u_1v_1)+t(u_2v_2)
=t(u_1v_1+u_2v_2)=t(u\cdot v).
\end{aligned}
$$

标量在第二侧时，

$$
\begin{aligned}
u\cdot(tv)
&=u_1(tv_1)+u_2(tv_2)\\
&=t(u_1v_1)+t(u_2v_2)
=t(u_1v_1+u_2v_2)=t(u\cdot v).
\end{aligned}
$$

第二份计算还使用实数乘法交换把 $t$ 移至前面。令 $t=-1$，已证位移等式 $(-1)v=-v$ 给

$$
(-u)\cdot w=-(u\cdot w),\qquad u\cdot(-v)=-(u\cdot v).
$$

所以两侧差式分别为

$$
\begin{aligned}
(u-v)\cdot w
&=(u+(-v))\cdot w
=u\cdot w+(-v)\cdot w
=u\cdot w-v\cdot w,\\
u\cdot(v-w)
&=u\cdot(v+(-w))
=u\cdot v+u\cdot(-w)
=u\cdot v-u\cdot w.
\end{aligned}
$$

定义 $u\perp v$ 为实数等式 $u\cdot v=0$。内积交换使 $u\perp v$ 当且仅当 $v\perp u$。又

$$
\mathbf0\cdot v=0v_1+0v_2=0,
\qquad v\cdot\mathbf0=v_10+v_20=0,
$$

所以零位移与每个位移正交。这个关系仅使用实数乘加与零，没有先定义角度，更没有从纸上夹角测量取得结论。

### 题2完整解答：固定非零方向的全部正交位移 {#planeproj-a02}

[返回题目](#planeproj-q02)

固定 $u=(u_1,u_2)\ne\mathbf0$。定义 $u^\perp=(-u_2,u_1)$，其两个坐标都是实数，所以是合法位移。若 $u^\perp=\mathbf0$，逐分量相等给 $-u_2=0$、$u_1=0$，第一式再取反得 $u_2=0$，与 $u\ne\mathbf0$ 矛盾。因此 $u^\perp\ne\mathbf0$。

直接计算

$$
u\cdot u^\perp=u_1(-u_2)+u_2u_1
=-u_1u_2+u_1u_2=0,
$$

所以它与 $u$ 正交。

给任意位移 $v=(v_1,v_2)$。前一单元定义 $D(z,v)=z_1v_2-z_2v_1$，故

$$
\begin{aligned}
D(u^\perp,v)
&=(-u_2)v_2-u_1v_1\\
&=-u_2v_2-u_1v_1\\
&=-(u_1v_1+u_2v_2)=-u\cdot v.
\end{aligned}
$$

最后一步用和的相反数及加法交换。内积交换给 $v\perp u$ 等价于 $u\cdot v=0$，又等价于 $D(u^\perp,v)=0$。由于第一方向 $u^\perp$ 非零，PL1的比例判据适用，得到唯一实数 $\lambda$ 满足 $v=\lambda u^\perp$。

反向，若 $v=\lambda u^\perp$，题1标量相容给

$$
v\cdot u=(\lambda u^\perp)\cdot u
=\lambda(u^\perp\cdot u)=\lambda0=0.
$$

所以 $v\perp u$。系数唯一性不是来自正交等式本身，而来自非零方向 $u^\perp$ 的参数单射或PL1。

当 $v=\mathbf0$ 时，$\lambda=0$ 确实给 $v=0u^\perp$；因 $u^\perp$ 至少一分量非零，任何另一满足 $\lambda u^\perp=\mathbf0$ 的系数，在该分量由非零消去必须为零。

若删去 $u\ne\mathbf0$，取 $u=\mathbf0$、$v=(1,0)$。题1给 $v\perp u$，但 $u^\perp=\mathbf0$，所有 $\lambda u^\perp$ 均为零，不等于 $v$，连存在都失败。取 $v=\mathbf0$ 时所有系数均给零，唯一性也失败。因此题干的固定非零条件同时保护存在与唯一两个方向。

### 题3完整解答：垂足的分母、存在与唯一 {#planeproj-a03}

[返回题目](#planeproj-q03)

设 $P=(p_1,p_2)$、$u=(u_1,u_2)\ne\mathbf0$，$L=\{P+tu:t\in\mathbb R\}$，给点 $X=(x_1,x_2)$。记 $w=X-P$，其分量为 $w_j=x_j-p_j$。

范数非负且只有零位移的范数为零，所以 $u\ne\mathbf0$ 给 $\|u\|>0$。于是

$$
N=u\cdot u=u_1^2+u_2^2=\|u\|^2>0.
$$

实数分母 $N$ 非零，商 $t_0=(w\cdot u)/N$ 有定义且唯一，乘回满足 $t_0N=w\cdot u$。定义点 $H=P+t_0u$。因为 $t_0\in\mathbb R$，成员定义给 $H\in L$。

两个残差坐标为

$$
\begin{aligned}
x_1-(p_1+t_0u_1)&=(x_1-p_1)-t_0u_1=w_1-t_0u_1,\\
x_2-(p_2+t_0u_2)&=(x_2-p_2)-t_0u_2=w_2-t_0u_2.
\end{aligned}
$$

所以 $X-H=w-t_0u$。按已证内积差式和标量相容，

$$
\begin{aligned}
(X-H)\cdot u
&=(w-t_0u)\cdot u\\
&=w\cdot u-t_0(u\cdot u)\\
&=w\cdot u-t_0N=0.
\end{aligned}
$$

这证明线上正交残差点存在。

为证唯一，任取点 $K\in L$ 且 $(X-K)\cdot u=0$。由 $K\in L$，存在 $t\in\mathbb R$ 使 $K=P+tu$。逐坐标同上得 $X-K=w-tu$，于是

$$
0=(w-tu)\cdot u=w\cdot u-tN.
$$

同加 $tN$ 得 $Nt=w\cdot u$。系数 $N>0$，乘法方程唯一解为 $t=(w\cdot u)/N=t_0$。因此 $K=P+t_0u=H$，完成唯一性。

固定 $P,u$ 时，函数写为

$$
\Pi_{P,u}:\mathbb R^2\to L(P,u),
\qquad
\Pi_{P,u}(X)=P+\left(\frac{(X-P)\cdot u}{u\cdot u}\right)u.
$$

域是所有点，目标是该直线的点集；已经证明每个输入得到该目标内唯一输出。域无需先限制在线外。

### 题4完整解答：线上输入与零残差 {#planeproj-a04}

[返回题目](#planeproj-q04)

仍固定 $u\ne\mathbf0$，并令 $H=\Pi_{P,u}(X)$。若 $X\in L$，则 $X$ 本身是线上点且 $X-X=\mathbf0$。题1证明零位移与 $u$ 正交，所以 $X$ 也是题3所刻画的候选点。唯一性给 $H=X$。

反向，若 $H=X$，由投影点总属于 $L$，立即得 $X\in L$。两点差的零判据再给

$$
X-H=\mathbf0\quad\Longleftrightarrow\quad X=H.
$$

因此三个条件两两等价。

还可直接核参数。若 $X=P+qu$，逐坐标减去 $P$ 得

$$
X-P=((p_1+qu_1)-p_1,(p_2+qu_2)-p_2)
=(qu_1,qu_2)=qu.
$$

题1给 $(X-P)\cdot u=(qu)\cdot u=q(u\cdot u)=qN$。投影参数是方程 $Nt=(X-P)\cdot u=qN$ 的唯一解。$t=q$ 显然乘回成立，所以 $t_0=q$，从而 $H=P+qu=X$。

残差为零仍满足正交定义 $\mathbf0\cdot u=0$。但参数直线的方向须非零；把零残差拿来当方向只会得到单点集合。因此这里只得到合法的退化残差，而没有产生一条以该残差为非零方向的垂线。

### 题5完整解答：勾股恒等式的双向与零边界 {#planeproj-a05}

[返回题目](#planeproj-q05)

给任意位移 $r=(r_1,r_2)$、$s=(s_1,s_2)$。由范数平方公式和实数二项平方展开，

$$
\begin{aligned}
\|r+s\|^2
&=(r_1+s_1)^2+(r_2+s_2)^2\\
&=(r_1^2+2r_1s_1+s_1^2)
 +(r_2^2+2r_2s_2+s_2^2)\\
&=(r_1^2+r_2^2)+(s_1^2+s_2^2)
 +2(r_1s_1+r_2s_2)\\
&=\|r\|^2+\|s\|^2+2(r\cdot s).
\end{aligned}
$$

第三步先用加法交换结合分组，再用实数分配合并两个带系数二的项。

若 $r\perp s$，则 $r\cdot s=0$，代入得 $\|r+s\|^2=\|r\|^2+\|s\|^2$。

若反过来给定该平方等式，与上面全称展开比较，再同减 $\|r\|^2+\|s\|^2$，得到

$$
2(r\cdot s)=0.
$$

实数 $2>0$，特别地非零；非零乘法消去给 $r\cdot s=0$，即 $r\perp s$。用到的唯一非零系数是二，没有要求 $r,s$ 非零。

若 $r=\mathbf0$，左侧为 $\|s\|^2$，右侧为 $0+\|s\|^2$，同时 $r\cdot s=0$。若 $s=\mathbf0$，同样左侧为 $\|r\|^2$，右侧为 $\|r\|^2+0$，同时 $r\cdot s=0$。两者都零也包含。这是坐标模型中的双向代数恒等式，不通过未定义的直角测量作证明。

### 题6完整解答：最近点的完整平方差 {#planeproj-a06}

[返回题目](#planeproj-q06)

设 $H=P+t_0u$ 是题3的投影点，任取 $Y=P+tu\in L$。按两坐标计算，

$$
\begin{aligned}
h_1-y_1&=(p_1+t_0u_1)-(p_1+tu_1)=(t_0-t)u_1,\\
h_2-y_2&=(p_2+t_0u_2)-(p_2+tu_2)=(t_0-t)u_2.
\end{aligned}
$$

所以 $H-Y=(t_0-t)u$。又

$$
(x_1-h_1)+(h_1-y_1)=x_1-y_1,\qquad
(x_2-h_2)+(h_2-y_2)=x_2-y_2,
$$

故 $X-Y=(X-H)+(H-Y)$。

记 $e=X-H$。题3已给 $e\cdot u=0$，由题1第二输入标量相容，

$$
e\cdot(H-Y)=e\cdot((t_0-t)u)
=(t_0-t)(e\cdot u)=0.
$$

因此这两个位移正交，题5给

$$
\|X-Y\|^2=\|X-H\|^2+\|H-Y\|^2.
$$

范数取反不变和距离定义给 $\|X-Y\|=\|Y-X\|=d_2(X,Y)$，同理 $\|X-H\|=d_2(X,H)$。另由范数倍率，

$$
\begin{aligned}
\|H-Y\|^2
&=\|(t_0-t)u\|^2\\
&=\bigl(|t_0-t|\,\|u\|\bigr)^2\\
&=|t_0-t|^2\|u\|^2\\
&=(t_0-t)^2\|u\|^2
=(t-t_0)^2\|u\|^2.
\end{aligned}
$$

第三步重排四因子，第四步用绝对值平方与原平方相等，末步用 $t_0-t=-(t-t_0)$。所以

$$
d_2(X,Y)^2=d_2(X,H)^2+(t-t_0)^2\|u\|^2.
$$

额外项是两个非负实数的积。因此 $d_2(X,H)^2\le d_2(X,Y)^2$；两个距离都非负，平方反映给 $d_2(X,H)\le d_2(X,Y)$。

等号的全部条件为

$$
\begin{aligned}
d_2(X,H)=d_2(X,Y)
&\Longleftrightarrow d_2(X,H)^2=d_2(X,Y)^2\\
&\Longleftrightarrow(t-t_0)^2\|u\|^2=0\\
&\Longleftrightarrow(t-t_0)^2=0\\
&\Longleftrightarrow t=t_0\\
&\Longleftrightarrow Y=H.
\end{aligned}
$$

第一步用相同输入平方和非负平方判等；第二步用平方差式和加法消去；第三步因 $\|u\|^2=N>0$ 而可消去；第四步用实数平方零判据；末步正向直接代入，反向用非零方向参数单射。故 $H$ 是唯一最近点。

若 $X\in L$，题4给 $H=X$，首项距离平方为零，上式仍成立。任何 $Y\ne H$ 必有 $t\ne t_0$，额外项严格正，故不可能也有零最小距离。证明未因零残差失效。

### 题7完整解答：一般一次方程的距离公式 {#planeproj-a07}

[返回题目](#planeproj-q07)

设 $a,b,c\in\mathbb R$，且 $a,b$ 不全为零。若 $a\ne0$，取 $P=(c/a,0)$，乘回给 $a(c/a)+b0=c$。若 $a=0$，则 $b\ne0$，取 $P=(0,c/b)$，同理 $a0+b(c/b)=c$。所以基点存在。

设 $n=(a,b)$、$u=(-b,a)$。二者都非零，PL2已证明方程点集恰是 $L(P,u)$。逐分量计算

$$
n\cdot u=a(-b)+ba=-ab+ab=0.
$$

又有

$$
N=n\cdot n=a^2+b^2=\|n\|^2>0,
\qquad s=\|n\|=\sqrt N>0,\qquad s^2=N,
$$

因为非零位移范数正。两个可能作分母的数 $N,s$ 都已先证明严格正。

给任意点 $X=(x_1,x_2)$，令

$$
E=ax_1+bx_2-c.
$$

由于 $ap_1+bp_2=c$，

$$
\begin{aligned}
n\cdot(X-P)
&=a(x_1-p_1)+b(x_2-p_2)\\
&=ax_1+bx_2-(ap_1+bp_2)=E.
\end{aligned}
$$

合法商 $\rho=E/N$ 满足 $\rho N=E$。定义点

$$
K=X+(-\rho n)=(x_1-\rho a,x_2-\rho b).
$$

点加位移规则保证输出确是点，并没有借用尚未定义的点减位移。代入一次方程：

$$
\begin{aligned}
aK_1+bK_2
&=a(x_1-\rho a)+b(x_2-\rho b)\\
&=ax_1+bx_2-\rho a^2-\rho b^2\\
&=ax_1+bx_2-\rho(a^2+b^2)\\
&=ax_1+bx_2-E=c.
\end{aligned}
$$

所以 $K\in L$。两残差坐标分别为

$$
x_1-(x_1-\rho a)=\rho a,\qquad
x_2-(x_2-\rho b)=\rho b,
$$

故 $X-K=\rho n$。于是

$$
(X-K)\cdot u=(\rho n)\cdot u
=\rho(n\cdot u)=0.
$$

题3的存在唯一性说明该 $K$ 就是投影点 $H$；题6说明它还是唯一最近点。

对固定直线集合 $L$，因此定义

$$
\operatorname{dist}_L:\mathbb R^2\to\mathbb R_{\ge0},
\qquad \operatorname{dist}_L(X)=d_2(X,H).
$$

输入是点，目标是非负实数；每个输入都有唯一垂足，故规则合法。其输出是集合 $\{d_2(X,Y):Y\in L\}$ 中实际达到的最小元素，因为 $H\in L$ 且对所有 $Y\in L$ 有 $d_2(X,H)\le d_2(X,Y)$。不同参数表示若给同一 $L$，这个最近点条件也相同，题6唯一性使点和数值都相同。这里没有定义下确界，也没有把直线集合塞入旧的点对函数 $d_2$。

由范数取反不变与倍率，

$$
\operatorname{dist}_L(X)=\|X-K\|=\|\rho n\|=|\rho|s.
$$

从 $\rho N=E$ 取绝对值得

$$
|E|=|\rho N|=|\rho||N|=|\rho|N,
$$

末步用 $N>0$。于是

$$
s(|\rho|s)=|\rho|(ss)=|\rho|N=|E|.
$$

系数 $s$ 非零，方程 $sZ=|E|$ 有唯一解 $|E|/s$，而 $|\rho|s$ 已代回满足，因此

$$
\operatorname{dist}_L(X)
=\frac{|E|}{s}
=\frac{|ax_1+bx_2-c|}{\sqrt{a^2+b^2}}.
$$

这一化简只用乘回和唯一性，没有引用开根商式。若分子对应的 $E=0$，则 $\rho=0/N=0$，点 $K=X$；该点 $X$ 已在直线上，距离为零，右边 $0/s=0$，同样成立。

### 题8完整解答：精确实例、系数缩放与零反例 {#planeproj-a08}

[返回题目](#planeproj-q08)

第一条直线为 $x_1+x_2=2$，点 $X=O$。法向 $n=(1,1)$，故 $N=2$、$s=\sqrt2>0$，而 $E=0+0-2=-2$。方程 $2\rho=-2$ 的唯一解是 $\rho=-1$，所以

$$
H=X+(-\rho n)=(0,0)+(1,1)=(1,1).
$$

该点两坐标和为二，在直线上；残差 $X-H=(-1,-1)$ 与方向 $(-1,1)$ 的点积为 $1-1=0$。直接范数值为

$$
d_2(O,H)=\sqrt{1^2+1^2}=\sqrt2.
$$

一般公式给 $2/\sqrt2$。因为 $(\sqrt2)^2=2$ 且 $\sqrt2>0$，候选 $\sqrt2$ 满足方程 $(\sqrt2)Z=2$，唯一性说明 $2/\sqrt2=\sqrt2$，与直接值一致。

第二条直线为 $x_1=3$，法向 $n=(1,0)$，故 $N=1$、$s=1$、$E=-3$、$\rho=-3$。于是 $H=(3,0)$，直接距离是 $\sqrt{3^2}=3$，因为三正且平方为九。商式给 $|-3|/1=3$；候选三乘回一得到三，故两个值一致。

再给一般 $a,b,c$，其中 $a,b$ 不全零，以及非零实数 $\lambda$。对任意点 $Y=(y_1,y_2)$，

$$
\begin{aligned}
(\lambda a)y_1+(\lambda b)y_2=\lambda c
&\Longleftrightarrow \lambda(ay_1+by_2)=\lambda c\\
&\Longleftrightarrow ay_1+by_2=c.
\end{aligned}
$$

前一步用结合和分配，后一步用 $\lambda\ne0$ 的双向消去。因此两个方程描述同一集合。

设原法向 $n=(a,b)$，其范数 $s>0$，原分子内部值 $E=ax_1+bx_2-c$。新法向为 $n'=\lambda n$；若它为零，取 $n$ 的一个非零分量，非零消去会推出 $\lambda=0$，矛盾，所以它仍非零。范数倍率给新分母

$$
s'=\|n'\|=|\lambda|s>0.
$$

新分子内部值由分配为 $E'=\lambda E$，其绝对值为 $|E'|=|\lambda||E|$。令 $D=|E|/s$，合法商乘回给 $sD=|E|$。于是

$$
s'D=(|\lambda|s)D
=|\lambda|(sD)=|\lambda||E|=|E'|.
$$

因为 $s'>0$，方程 $s'Z=|E'|$ 的唯一解为新公式值 $|E'|/s'$，上式说明它等于 $D$。系数 $\lambda$ 可负，绝对值正倍率覆盖此支；$E=0$ 时两个商都为零，也不例外。

若 $\lambda=0$，三个新系数全为零，方程 $0y_1+0y_2=0$ 对每个点成立；新法向为零，新根分母为零，既不满足真直线条件，也不能使用距离商式。

原直线确实不是全平面。取题7构造的基点 $P=(p_1,p_2)$，令 $N=a^2+b^2>0$，则点 $P+n=(p_1+a,p_2+b)$ 满足

$$
a(p_1+a)+b(p_2+b)
=(ap_1+bp_2)+(a^2+b^2)=c+N>c.
$$

所以该点不在原直线上，却属于零缩放后的全平面。集合已改变，不能只说零缩放“公式不好算”而保留原几何对象。
