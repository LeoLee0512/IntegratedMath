## 基础单元 有限实数和：递归、逐项规则与拼接 {#rfs-unit}

**位置与目标。** 本单元主归第528章97H20初等代数教育的有限实数求和局部，作为第84章15A03有限坐标线性组合的必要先修。我们重新建立实数值的有限和，证明空和、表外延拓独立、逐项相加、实数缩放、连续拼接与有理嵌入相容。前文有理值求和提供构造思路，却不能代替实数值对象的存在性和证明。当前不定义无限级数、任意重排、双重求和或向量线性组合，也不表示任何分类叶已完成。

**精确先修。** 使用[普通归纳](#b1-induction)、[固定更新递归原则](#b1-recursion-principle)、[自然数加法递推](#b1-addition-definition)、[加一与后继](#b1-add-one)、[加法结合](#b1-addition-associative)、[后继比较与索引分解](#ord-successor-comparison)、[自然数三分律](#ord-trichotomy)、[非严格序](#ord-partial-order)、[严格序与混合传递](#ord-strict-equivalence)、[同加保持与反映比较](#ord-addition-order)、[自然加法消去](#ord-cancellation)、[有条件自然减法](#sub-definition)，以及[有序对与积](#fun-pairs)、[函数规则](#fun-definition)、[逐点相等](#fc-equality)和[索引$I_n$](#sum-indices)。实数方面使用[加法闭合](#cutadd-definition)、[加法群律](#cutgroup-laws)、[相反数](#cutgroup-inverses)、[差](#cutgroup-negation-subtraction)、[乘法闭合](#cutsigned-definition)、[单位与取反乘积](#cutsigned-signs)、[乘零](#cutsigned-rational-zero)及[全分配律](#cutring-distributive)。有理相容部分另使用[实数零的定义$0_{\mathbb R}=i(0_{\mathbb Q})$](#cutadd-unit)、[有理嵌入保加](#cutadd-rational)、旧[有理和递归](#sum-definition)与[有理有限表和](#sum-extensionality)。

**记号与阅读顺序。** $m,n,k,j$是自然数；$a,c,r,s$等在数值运算中为实数。自然索引的加法与实数累计值的加法不可混淆。先建立实数序列的有限前缀和，再用零延拓给有限表定义和，随后证明各项规则。涉及有理数时明确写嵌入$i:\mathbb Q\to\mathbb R$；一般实数公式不假定输入有理。

### 1. 一个固定状态更新，而不是随步数换规则 {#rfs-definition}

给定$u:\mathbb N\to\mathbb R$，写$u_k=u(k)$。这是每个自然位置都有实数值的一条序列，但本单元每次只相加前面有限项，不讨论它的极限。

若只把累计值$s$作为状态，写“下一次加$u_k$”，$k$却不在状态中，这还不是旧递归原则所需的固定自映射。把步数与累计值一起记录，取

$$
X=\mathbb N\times\mathbb R,\qquad x_*=(0_{\mathbb N},0_{\mathbb R}),
\qquad T(k,s)=(k+1,s+u_k).
$$

给任何$(k,s)\in X$，$u$在输入$k$处恰有一个实数输出；$s+u_k$由已建立的实数加法恰得一个实数，而$k+1$是自然数。所以$T$给唯一输出并仍在$X$中，确实是一个固定函数$X\to X$。$X$的存在来自既有集合积背景；这里没有把有理状态范围原封不动地拿来用。

**RFS1（实数部分和的存在与唯一）。** 应用固定更新递归原则，得到唯一$F:\mathbb N\to X$，满足

$$
F(0)=x_*,\qquad F(n+1)=T(F(n)).
$$

先对$n$归纳，证明$F(n)$的第一分量等于$n$。在0处由$x_*$成立；若$F(n)=(n,s)$，更新给$F(n+1)=(n+1,s+u_n)$，其第一分量就是$n+1$。归纳完成。因此可以把唯一第二分量记为$S_n(u)$，有

$$
F(n)=(n,S_n(u)),\qquad
S_0(u)=0,\qquad S_{n+1}(u)=S_n(u)+u_n.
$$

这里$S_n(u)\in\mathbb R$；末式中的新增项索引为$n$，因为前$n$项尚未读它。

若另有实数值函数$H:\mathbb N\to\mathbb R$满足$H(0)=0$、$H(n+1)=H(n)+u_n$，另对$n$归纳：起点$H(0)=S_0(u)$；若$H(n)=S_n(u)$，则

$$
H(n+1)=H(n)+u_n=S_n(u)+u_n=S_{n+1}(u).
$$

故所有$n$处都相等，且域目标相同，所以$H$等于$n\mapsto S_n(u)$。存在性由核验过条件的状态递归给出，唯一性也直接核实；不能仅写递推式就假定它有唯一解。

定义求和记号

$$
\sum_{0\le j<n}u_j:=S_n(u).
$$

这叫前$n$项的实数和，$n=0$时为空和，值是实数零。另对$k\in\mathbb N$定义$\sum_{j=0}^{k}u_j:=S_{k+1}(u)$，因此$\sum_{j=0}^{0}u_j=S_1(u)=0+u_0=u_0$，是一项而非空和。不用$n-1$统一描述末索引，免得在$n=0$制造未定义的自然差。

### 2. 只读前缀，表外怎样延拓都无关 {#rfs-prefix-table}

**RFS2。** 若$u,v:\mathbb N\to\mathbb R$在每个$j<n$处同值，则$S_n(u)=S_n(v)$。

对$n$归纳，性质包含**所有**满足相应前缀条件的$u,v$。$n=0$时不需任何坐标条件，两边由定义均为零。假设结论对$n$成立，任取前$n+1$项一致的两序列。由$I_{n+1}=I_n\cup\{n\}$，它们前$n$项一致且$u_n=v_n$。先应用归纳假设，再加新增项：

$$
S_{n+1}(u)=S_n(u)+u_n=S_n(v)+v_n=S_{n+1}(v).
$$

所以结论对所有$n$成立。没有要求两序列在$n$及以后也相同。

现在给有限实数表$a:I_n\to\mathbb R$。定义其零延拓$\widetilde a:\mathbb N\to\mathbb R$：

$$
\widetilde a_j=
\begin{cases}
a_j,&j<n,\\
0,&n\le j.
\end{cases}
$$

自然全序保证恰有一支适用。第一支在表的域内才求$a_j$，第二支直接输出实数零，因而每个自然输入有唯一实数输出。定义

$$
\operatorname{Sum}_{\mathbb R}(a)=S_n(\widetilde a),
\qquad
\sum_{0\le j<n}a_j:=\operatorname{Sum}_{\mathbb R}(a).
$$

若$w:\mathbb N\to\mathbb R$是另一延拓，即对$j<n$有$w_j=a_j$，RFS2给$S_n(w)=S_n(\widetilde a)$。所以这个定义既提供一个确定候选，又证明和值不依赖表外的补值。有限表不能直接在表外求值；延拓是新域为$\mathbb N$的函数记录。

$n=0$时有限表为空表，零延拓虽在每个自然位置都为零，但表和只取前零项，值为0，没有读取不存在的$a_0$。一项表$(r)$的和是$r$，因为零延拓在0处为$r$，$S_1=0+r=r$。

例：取任意实数$r$，表$(r,-r,2)$的零延拓依次给状态

$$
(0,0),\quad(1,r),\quad(2,r+(-r))=(2,0),\quad(3,2).
$$

所以表和为2。这里$r$可以是任意已给实数；实数相反数律足以说明第二步，并不要求$r$有有理表示。

### 3. 两种逐项规则分别归纳 {#rfs-linearity}

给$u,v:\mathbb N\to\mathbb R$及固定$c\in\mathbb R$，定义序列$(u+v)_j=u_j+v_j$和$(cu)_j=cu_j$。实数加乘闭合且输出唯一，故这些规则确实给出相同域、目标的序列。这里是新定义的逐项操作，不是把函数当实数。

**RFS3。** 对每个$n\in\mathbb N$，

$$
S_n(u+v)=S_n(u)+S_n(v),\qquad
S_n(cu)=cS_n(u).
$$

**逐项加法。** 固定$u,v$，对$n$归纳。起点左边为0，右边为$0+0=0$。若$n$处成立，递归给

$$
S_{n+1}(u+v)
=S_n(u+v)+(u_n+v_n)
=(S_n(u)+S_n(v))+(u_n+v_n).
$$

为了明确此处只用二元实数加法，暂写$A=S_n(u),B=S_n(v),p=u_n,q=v_n$。四个实数按下列步骤重新结合：

$$
\begin{aligned}
(A+B)+(p+q)
&=A+(B+(p+q)) &&\text{结合律}\\
&=A+((B+p)+q) &&\text{内层结合律}\\
&=A+((p+B)+q) &&\text{只交换 }B,p\\
&=A+(p+(B+q)) &&\text{内层结合律}\\
&=(A+p)+(B+q) &&\text{结合律}.
\end{aligned}
$$

因此后继项等于

$$
(S_n(u)+u_n)+(S_n(v)+v_n)=S_{n+1}(u)+S_{n+1}(v).
$$

归纳完成。这里没有调用任意有限排列不变性。

**实数缩放。** 固定$c,u$，再对$n$归纳。起点左边为空和0，右边$c0=0$。若$S_n(cu)=cS_n(u)$，则

$$
\begin{aligned}
S_{n+1}(cu)
&=S_n(cu)+cu_n\\
&=cS_n(u)+cu_n\\
&=c(S_n(u)+u_n)\\
&=cS_{n+1}(u).
\end{aligned}
$$

中间合并使用已证实数分配律。没有除以$c$，所以$c=0$、负$c$都允许。归纳完成第二式。

**回到有限表。** 对同长$a,b:I_n\to\mathbb R$，逐点定义$(a+b)_j=a_j+b_j$与$(ca)_j=ca_j$。它们是合法实数表。比较零延拓：在$j<n$时按表规则相等，在$j\ge n$时$0+0=0,c0=0$，所以

$$
\widetilde{a+b}=\widetilde a+\widetilde b,
\qquad \widetilde{ca}=c\widetilde a.
$$

这些是同域同目标的函数等式。应用刚证的序列公式，得到

$$
\operatorname{Sum}_{\mathbb R}(a+b)
=\operatorname{Sum}_{\mathbb R}(a)+\operatorname{Sum}_{\mathbb R}(b),
\quad
\operatorname{Sum}_{\mathbb R}(ca)=c\operatorname{Sum}_{\mathbb R}(a).
$$

不同长度的表不能直接逐项相加。相反表定义为$(-a)_j=-a_j=(-1)a_j$，所以其和是$-\operatorname{Sum}_{\mathbb R}(a)$；差表定义为$a-b=a+(-b)$，再用两条公式得其和等于两和值之差。这些推论也包含空表。

### 4. 连续拼接保持原顺序 {#rfs-concatenation}

给$u:\mathbb N\to\mathbb R$及$m\in\mathbb N$，定义移位序列$u^{[m]}_j=u_{m+j}$。自然数加法闭合，故右侧处处合法；其第零项是$u_m$，不是$u_0$。方括号上标是移位标签，不是幂。

**RFS4。** 对所有$m,n\in\mathbb N$，

$$
S_{m+n}(u)=S_m(u)+S_n(u^{[m]}).
$$

固定$u,m$，对后一段长度$n$归纳。$n=0$时$m+0=m$，右边为$S_m(u)+0$，等式成立。若$n$处成立，利用自然加法递推$m+(n+1)=(m+n)+1$，有

$$
\begin{aligned}
S_{m+(n+1)}(u)
&=S_{(m+n)+1}(u)\\
&=S_{m+n}(u)+u_{m+n}\\
&=(S_m(u)+S_n(u^{[m]}))+u^{[m]}_n\\
&=S_m(u)+(S_n(u^{[m]})+u^{[m]}_n)\\
&=S_m(u)+S_{n+1}(u^{[m]}).
\end{aligned}
$$

依次使用自然索引关系、实数和递归、归纳假设与移位定义、实数结合律、移位序列的递归。归纳完成；$m$任意，所以也允许$m=0$。可记$\sum_{m\le j<m+n}u_j:=S_n(u^{[m]})$；它从$m$开始读$n$项，不用可能未定义的末索引差。

**有限表拼接的全部索引检查。** 给$a:I_m\to\mathbb R,b:I_n\to\mathbb R$，要定义$c:I_{m+n}\to\mathbb R$，规定

$$
c_j=a_j\quad(j<m),\qquad c_{m+k}=b_k\quad(k<n).
$$

先核这确实无重无漏。前段$j<m$，因为$m\le m+n$，混合传递给$j<m+n$。后段$k<n$，同加$m$给$m+k<m+n$，且$m\le m+k$；所以后段合法且不会落入前段。若$m+k=m+k'$，自然加法消去给$k=k'$，因此后段的输入不会产生两个不同读法。

任取$j<m+n$。若$j<m$，它由前段覆盖；若不成立，三分律给$m\le j$，此时才可用自然减法，取唯一$k=j-m$使$m+k=j$。由$m+k<m+n$及同加反映严格比较得$k<n$，因此后段也覆盖这个$j$。两支互斥、覆盖全部输入且输出都是唯一实数，所以$c$合法。

取$c$的零延拓$w$。RFS4给

$$
\operatorname{Sum}_{\mathbb R}(c)
=S_{m+n}(w)=S_m(w)+S_n(w^{[m]}).
$$

对$j<m$，$w_j=a_j$，所以RFS2给$S_m(w)=\operatorname{Sum}_{\mathbb R}(a)$；对$k<n$，$w^{[m]}_k=w_{m+k}=b_k$，同理得后段和。因此

$$
\operatorname{Sum}_{\mathbb R}(c)
=\operatorname{Sum}_{\mathbb R}(a)+\operatorname{Sum}_{\mathbb R}(b).
$$

$m=0$时前段为空，$n=0$时后段为空；索引论证和空和公式都保留成立。这是连续两段的拆接，没有重新排列任意项。

### 5. 补零不改和值，不能据此抹去长度 {#rfs-padding}

**RFS5。** 全零实数表的和为0；在有限表后拼接任意长度的零表，不改变和值。

先令零序列$z:\mathbb N\to\mathbb R$满足$z_j=0$。对$n$归纳：$S_0(z)=0$；若$S_n(z)=0$，则$S_{n+1}(z)=S_n(z)+z_n=0+0=0$。所以任意长度的全零表，其零延拓为$z$，表和为0。再用RFS4，表$a$与任意零表拼接得到$c$时，

$$
\operatorname{Sum}_{\mathbb R}(c)
=\operatorname{Sum}_{\mathbb R}(a)+0
=\operatorname{Sum}_{\mathbb R}(a).
$$

如果补入了非零长度，两个表的域不同，不是相同函数记录。和值只能反映部分信息：空表、一项表$(0)$、两项表$(r,-r)$均有和0。取$r=1$时最后一表还有非零项，故“和为零”既不推出“没有项”，也不推出“每项为零”。

### 6. 与原有理和比较，需要嵌入证明 {#rfs-rational-compatibility}

**RFS6。** 给有理序列$q:\mathbb N\to\mathbb Q$，将旧有理部分和记作$S_n^{\mathbb Q}(q)$。令$u=i\circ q:\mathbb N\to\mathbb R$，则

$$
S_n(u)=i\bigl(S_n^{\mathbb Q}(q)\bigr)
\quad(n\in\mathbb N).
$$

这是两个不同数域的对象之间的相容式，不是直接写“两个和值是同一个对象”。复合合法，因为$q$的目标正是$i$的域。

固定$q$，对$n$归纳。$n=0$时左边是实数零，右边为$i(0_{\mathbb Q})=0_{\mathbb R}$。若当前相容，则

$$
\begin{aligned}
S_{n+1}(i\circ q)
&=S_n(i\circ q)+i(q_n)\\
&=i(S_n^{\mathbb Q}(q))+i(q_n)\\
&=i(S_n^{\mathbb Q}(q)+q_n)\\
&=i(S_{n+1}^{\mathbb Q}(q)).
\end{aligned}
$$

第一式是新实数递归，第二式用归纳假设，第三式是已证嵌入保加，最后一式是旧有理递归。归纳完成；没有用有理线性公式代替实数线性证明。

对有理有限表$b:I_n\to\mathbb Q$，实数表$a=i\circ b:I_n\to\mathbb R$合法。把两个数域的零延拓分别记为$\widetilde b,\widetilde a$。当$j<n$时$\widetilde a_j=i(b_j)=i(\widetilde b_j)$；当$j\ge n$时$\widetilde a_j=0_{\mathbb R}=i(0_{\mathbb Q})=i(\widetilde b_j)$。因此$\widetilde a=i\circ\widetilde b$，将序列相容式应用于前$n$项，得

$$
\operatorname{Sum}_{\mathbb R}(i\circ b)
=i\bigl(\operatorname{Sum}_{\mathbb Q}(b)\bigr).
$$

同样包含空表。故精确有理数例可以先算有理和再嵌入；对任意实数表仍须使用本单元已建立的实数定义与规则。

### 7. 八道练习 {#rfs-exercises}

#### 题1：状态中的两种数 {#rfs-q01}

取任意实数$r$，令$a:I_3\to\mathbb R$输出为$(r+1,-r,2)$，$u$为其零延拓。写$F(0),F(1),F(2),F(3)$及$S_0(u),S_1(u),S_3(u)$，逐步解释消去。区分空和与$\sum_{j=0}^{0}u_j$，并说明状态第一分量和第二分量的类型。 [完整解答](#rfs-a01)

#### 题2：固定更新与合法延拓 {#rfs-q02}

为何只写$T(s)=s+u_k$尚未定义递归原则所需的固定自映射？补出状态、起点和更新，并核唯一输出与闭合。给$a:I_2\to\mathbb R$，$a=(3,-1)$，写零延拓各支；说明$a_2$、$\widetilde a_2$是否有定义。对空表再核一次。 [完整解答](#rfs-a02)

#### 题3：有限前缀的量词 {#rfs-q03}

完整归纳证明RFS2，写清每个$n$处量化哪些序列。给两条前两项相同但第三项不同的实数序列，核前两项和相等，而前三项和不同。解释RFS2并未断言两序列处处相等。 [完整解答](#rfs-a03)

#### 题4：两条逐项规律各自证明 {#rfs-q04}

对实数序列$u,v$与固定实数$c$，完整归纳证明逐项加法和缩放公式，四加数重组须写结合/交换步骤。解释$c=0$或$c<0$时是否需要另加限制，并核公式如何传给同长有限表。 [完整解答](#rfs-a04)

#### 题5：把后段从正确位置接上 {#rfs-q05}

给实数$r,s$及表$a=(r,-r,5):I_3\to\mathbb R$、$b=(-2,s,1):I_3\to\mathbb R$，列出拼接$c:I_6\to\mathbb R$，求三个表和，核拼接式。一般长度$m,n$时，证明后段的局部索引$k=j-m$在哪个条件下存在、为何唯一且满足$k<n$。说明$m=0$或$n=0$如何处理。 [完整解答](#rfs-a05)

#### 题6：零和的反向推断 {#rfs-q06}

从递归归纳证明任意长度全零表的和为0，再由拼接证明尾补零保和。给非空表而和零、且至少一个非零项的例子。说明补零后和值相同是否使两表成为同一函数，另说明空表与一项零表的区别。 [完整解答](#rfs-a06)

#### 题7：嵌入前后怎样比较 {#rfs-q07}

完整归纳证明$S_n(i\circ q)=i(S_n^{\mathbb Q}(q))$，并检查有限表的两个零延拓满足$\widetilde{i\circ b}=i\circ\widetilde b$。对有理表$b=(2/3,-1/6,1/2)$算其和，再给对应实数表的和；空表时相容式是什么？ [完整解答](#rfs-a07)

#### 题8：逐项乘积不是和值的乘积 {#rfs-q08}

给实数表$a=(2,3)$、$b=(4,-1)$，定义同长表$d$为$d_j=a_jb_j$。计算$\operatorname{Sum}_{\mathbb R}(d)$和$\operatorname{Sum}_{\mathbb R}(a)\operatorname{Sum}_{\mathbb R}(b)$，判断它们是否总应相等。用二元实数分配写出$(a_0+a_1)(b_0+b_1)$的正确带括号展开；指出为什么RFS3的“固定常数缩放”不能把随$j$变化的$b_j$抽到和外。 [完整解答](#rfs-a08)

### 8. 来源与继续接口 {#rfs-sources}

本单元实际核读Jiří Lebl《Basic Analysis I》所列固定版本[数列与级数章原文](https://raw.githubusercontent.com/jirilebl/ra/e21ec524ca7d54f800c693b948020c188d21d01f/ch-seq-ser.tex)第3000—3060、3302—3387行。该处在级数背景内定义有限部分和，并在证明中使用有限缩放与逐项加法等式，也提示逐项乘积的和不等于两和值之积。题8以自拟数值和完整解释检查这个通用事实，不是翻译来源练习。这里只用它核对有限公式与术语，不导入其中任何无限级数或取极限结论。来源未给本书需要的固定状态构造、零延拓和全套归纳证明；这些证明以及全部练习、解答独立编写。

[许可文件](https://raw.githubusercontent.com/jirilebl/ra/e21ec524ca7d54f800c693b948020c188d21d01f/LICENSE.md)为CC BY-SA 4.0与CC BY-NC-SA 4.0双许可。本次直接读取既有缓存，没有新网络请求；实际读取范围、版本与文件哈希见制作记录`research/production/finite_real_sums_sources.json`。未复制来源例题、图或题解。

后续有限坐标线性组合可对每个坐标构造一个有限实数表，再使用本单元的和。当前仍未证明任意置换重排不变、双重和换序或一般向量和递归；需要时须另给定义与证明。
