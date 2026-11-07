## 基础单元 有限坐标向量的线性组合 {#flc-unit}

**位置与目标。** 本单元主归第84章15Axx基础线性代数的15A03有限坐标线性组合局部。我们把同样长度的有限个实坐标向量，按对应实数系数合成一个向量，并逐坐标证明系数相加、共同缩放、向量项相加、连续拼接和坐标重编号的规则。这里不定义张成、基、线性相关、秩、维数、矩阵或行列式；一个具体组合计算不能替代这些后续概念与定理。

**精确先修。** 使用[函数集合背景与$V_n$模型](#frc-model)、[逐坐标运算](#frc-operations)、[向量加法规律](#frc-additive-laws)、[标量规律与零](#frc-scalar-laws)、[坐标重编号](#frc-reindex)，以及[实数有限和定义](#rfs-definition)、[前缀与有限表](#rfs-prefix-table)、[逐项加法和缩放](#rfs-linearity)、[连续拼接](#rfs-concatenation)、[全零表和](#rfs-padding)。函数相等使用[FC1](#fc-equality)，索引使用[$I_n$](#sum-indices)、[后继分解](#ord-successor-comparison)，拼接还用[有条件自然差](#sub-definition)。坐标内部的实数计算用[乘法交换与单位](#cutsigned-signs)、[结合律](#cutsigned-associative)、[分配律](#cutring-distributive)和[零积/乘零](#cutsigned-rational-zero)。

**阅读顺序。** 先把“向量项”和“一个向量中的坐标”区分清楚，再学定义和两个空参数；随后逐项核五种公式。练习八题，独立完整解答另列。所有标量和坐标值都是实数；数值例里的有理数按既有嵌入理解，不把自然索引当成实数运算对象。

### 1. 两套索引对应两层函数 {#flc-data}

固定自然数$m,n$。$n$表示每个向量有几个坐标，$m$表示要组合几个向量。数据为

$$
a:I_m\to\mathbb R,\qquad v:I_m\to V_n.
$$

$a$称为**系数表**，$v$称为**向量表**。对$k\in I_m$，$a_k$是实数，$v_k=v(k)$是一个向量，即函数$I_n\to\mathbb R$。再给$j\in I_n$，才可读出实数$(v_k)_j$。

例如$m=2,n=3$，$v_0=(1,0,2),v_1=(-1,3,4)$。这里向量项的编号是$k=0,1$，每项的坐标编号是$j=0,1,2$；$(v_1)_2=4$。表达式$v_2$没有定义，但$(v_0)_2$有定义。两个下标的角色不能因都写自然数而交换。

沿用FRC公开采用的函数集合背景，记

$$
\mathcal T_{m,n}=\{v:v\text{是函数 }I_m\to V_n\}.
$$

系数表集合就是$V_m$，但系数表在这里承担参数角色，输出向量属于$V_n$。即使$m=n$，两个角色也不能因此混用。全部向量项必须属于同一个$V_n$；如果某项只有两个坐标、另一项有三个坐标，给出的数据就不满足这里的类型。

### 2. 逐坐标定义组合，并处理两个零参数 {#flc-definition}

**FLC1（有限线性组合）。** 对上述$a,v$，每固定$j\in I_n$，定义一个实数表

$$
b^{[j]}:I_m\to\mathbb R,\qquad
b^{[j]}_k=a_k(v_k)_j.
$$

$k\in I_m$保证系数与向量项有定义，$v_k\in V_n$保证其第$j$坐标有定义；实数乘法给唯一实数输出。因此$b^{[j]}$是合法的长度$m$实数表。已证RFS定义给唯一实数$\operatorname{Sum}_{\mathbb R}(b^{[j]})$。

以此规定输出向量$w$：

$$
w_j=\operatorname{Sum}_{\mathbb R}(b^{[j]})
=\sum_{0\le k<m}a_k(v_k)_j\quad(j\in I_n).
$$

每个合法$j$都有唯一实数输出，所以得到函数$I_n\to\mathbb R$，即$w\in V_n$；同域同目标的逐点相等保证输出唯一。我们定义

$$
C_{m,n}:V_m\times\mathcal T_{m,n}\to V_n,
\qquad C_{m,n}(a,v)=w,
$$

称$w$为以$a$为系数的$v$的**有限线性组合**。当输入类型已经写明，简记$C(a,v)$。组合的结果是一个向量，不是$m$个实数，也不是一张尚未定义的矩阵。

在此定义之后，允许把

$$
\sum_{0\le k<m}a_kv_k
$$

作为$C(a,v)$的另一种记法。此处求和符号的值是向量，由刚才的逐坐标实数和来定义；它不是提前借用某个尚未建立的一般向量和递归。带坐标的$\sum_{k<m}a_k(v_k)_j$则是RFS已经定义的实数。

**$m=0$：没有向量项。** $a:I_0\to\mathbb R$与$v:I_0\to V_n$均为空函数。对每个$j\in I_n$，$b^{[j]}$为空实数表，其和为0，故输出所有合法坐标为零，$C(a,v)=0_n$。若$n>0$，这个输出有$n$个零坐标，并不是空向量。

**$n=0$：没有坐标。** $V_0$只有$0_0$。无论$m$是多少，每个$v_k$都必须为$0_0$，而输出函数的域是$I_0$，没有$j$需要指定，故$C(a,v)=0_0$。这不要求$m=0$：可以有三个向量项，每一项恰是空向量。$m=n=0$时两个描述一致，输出唯一空向量。

**一项与两项的兼容。** 若$m=1$，RFS一项和给每个$j$处

$$
C(a,v)_j=0+a_0(v_0)_j=a_0(v_0)_j=(a_0v_0)_j,
$$

所以$C(a,v)=a_0v_0$。若$m=2$，递归前两项给

$$
\begin{aligned}
C(a,v)_j
&=(0+a_0(v_0)_j)+a_1(v_1)_j\\
&=a_0(v_0)_j+a_1(v_1)_j\\
&=(a_0v_0+a_1v_1)_j.
\end{aligned}
$$

故$C(a,v)=a_0v_0+a_1v_1$，与旧二元向量运算相容。两式也适用于$n=0$，因为都是同域同目标的空表等式。

例：$v_0=(1,0),v_1=(0,2)$，$a=(3,-1)$。第0坐标的实数表为$(3\cdot1,(-1)\cdot0)=(3,0)$，和为3；第1坐标的表为$(3\cdot0,(-1)\cdot2)=(0,-2)$，和为$-2$。因此输出$C(a,v)=(3,-2)$。先确定两个内层表，才得到一个外层向量。

### 3. 系数逐项相加 {#flc-coefficients}

**FLC2。** 给$a,b:I_m\to\mathbb R$及$v:I_m\to V_n$，则

$$
C(a+b,v)=C(a,v)+C(b,v).
$$

左侧$a+b$是长度$m$实数表的逐项相加，右侧是$V_n$中的向量加法；两者已有不同但明确的规则。三项组合都合法。

任取$j\in I_n$，定义$p_k=a_k(v_k)_j$、$q_k=b_k(v_k)_j$，得到$p,q:I_m\to\mathbb R$。实数分配律对每个$k\in I_m$给

$$
(a_k+b_k)(v_k)_j=p_k+q_k.
$$

所以左侧第$j$坐标的加权表就是$p+q$，不是仅仅碰巧同和值。RFS逐项加法给

$$
\begin{aligned}
C(a+b,v)_j
&=\operatorname{Sum}_{\mathbb R}(p+q)\\
&=\operatorname{Sum}_{\mathbb R}(p)+\operatorname{Sum}_{\mathbb R}(q)\\
&=C(a,v)_j+C(b,v)_j\\
&=(C(a,v)+C(b,v))_j.
\end{aligned}
$$

两边都在$V_n$，每个合法坐标相同，结论成立。$m=0$时内层表均为空，RFS公式仍成立；$n=0$时逐坐标条件空真，输出同为空向量。

### 4. 共同缩放与零数据 {#flc-scaling}

**FLC3。** 固定实数$c$，给$a:I_m\to\mathbb R$、$v:I_m\to V_n$。系数表$ca$规定$(ca)_k=ca_k$，向量表$cv$规定$(cv)_k=cv_k$；后一式的输出由FRC标量乘法仍在$V_n$。则

$$
C(ca,v)=cC(a,v),\qquad C(a,cv)=cC(a,v).
$$

先任取$j\in I_n$，令$p_k=a_k(v_k)_j$。实数结合律给

$$
(ca_k)(v_k)_j=c\bigl(a_k(v_k)_j\bigr)=cp_k.
$$

因此$C(ca,v)$在第$j$处的加权表为$cp$。RFS实数缩放给

$$
C(ca,v)_j=\operatorname{Sum}_{\mathbb R}(cp)
=c\operatorname{Sum}_{\mathbb R}(p)
=cC(a,v)_j=(cC(a,v))_j.
$$

逐点判等得第一式。

对于第二式，先由FRC知道$(cv_k)_j=c(v_k)_j$。每个$k$处的实数乘积逐步为

$$
a_k\bigl(c(v_k)_j\bigr)
=(a_kc)(v_k)_j
=(ca_k)(v_k)_j
=c\bigl(a_k(v_k)_j\bigr)=cp_k.
$$

依次用结合、交换两个实数$a_k,c$、再结合。没有把两个向量相乘。故第二式在第$j$处也等于$\operatorname{Sum}_{\mathbb R}(cp)=cC(a,v)_j$，逐点得到结论。证明没有除法，$c=0$或负$c$都可用。

**零系数表。** 若每个$a_k=0$，对任意$j$，加权表每项为$0(v_k)_j=0$。RFS全零表和为0，故$C(a,v)=0_n$。**零向量表。** 若每个$v_k=0_n$，则$(v_k)_j=0$，加权表每项$a_k0=0$，同样得到$C(a,v)=0_n$。这两条允许$m=0$和$n=0$，没有要求实际存在一个$k$或$j$。

### 5. 把每个向量项拆成两个同长向量 {#flc-vector-addition}

**FLC4。** 给$a:I_m\to\mathbb R$及$v,w:I_m\to V_n$。定义$(v+w)_k=v_k+w_k$，其输出由FRC加法属于$V_n$，所以$v+w$是合法向量表。则

$$
C(a,v+w)=C(a,v)+C(a,w).
$$

固定$j\in I_n$。令$p_k=a_k(v_k)_j$、$q_k=a_k(w_k)_j$，它们是长度$m$实数表。向量加法定义与实数分配给

$$
a_k(v_k+w_k)_j
=a_k\bigl((v_k)_j+(w_k)_j\bigr)
=p_k+q_k.
$$

所以该坐标的加权表为$p+q$。使用RFS逐项加法，

$$
\begin{aligned}
C(a,v+w)_j
&=\operatorname{Sum}_{\mathbb R}(p+q)\\
&=\operatorname{Sum}_{\mathbb R}(p)+\operatorname{Sum}_{\mathbb R}(q)\\
&=C(a,v)_j+C(a,w)_j\\
&=(C(a,v)+C(a,w))_j.
\end{aligned}
$$

逐点判等完成证明。若$v_k,w_k$坐标长度不同，$v_k+w_k$本来就不在本单元运算的输入域中，不能套这条公式。空项数和空坐标数则都合法。

### 6. 系数与向量项必须同步拼接 {#flc-concatenation}

**FLC5。** 设前段系数$a:I_m\to\mathbb R$、向量表$v:I_m\to V_n$，后段系数$b:I_p\to\mathbb R$、向量表$w:I_p\to V_n$。记同步拼接为$d=a\Vert b$、$z=v\Vert w$：

$$
d_k=a_k,\ z_k=v_k\quad(k<m),
\qquad d_{m+t}=b_t,\ z_{m+t}=w_t\quad(t<p).
$$

$d:I_{m+p}\to\mathbb R$，$z:I_{m+p}\to V_n$。索引检查正是RFS拼接中已证明的两段分解：后段输入$t$由$m+t$唯一确定；对整体索引$k\ge m$，才可取$t=k-m$，且$k<m+p$使$t<p$。前后不交并覆盖全部域，每项也在指定目标内，故两份拼接均合法。符号$\Vert$仅指这种连续拼接，不是向量加法。

结论为

$$
C(d,z)=C(a,v)+C(b,w).
$$

任取$j\in I_n$。前段加权实数表为$h_k=a_k(v_k)_j$，后段为$\ell_t=b_t(w_t)_j$。整体加权表$e_k=d_k(z_k)_j$在前段等于$h_k$，在后段满足$e_{m+t}=b_t(w_t)_j=\ell_t$，所以它就是这两个实数表的连续拼接。RFS4给

$$
\begin{aligned}
C(d,z)_j
&=\operatorname{Sum}_{\mathbb R}(e)\\
&=\operatorname{Sum}_{\mathbb R}(h)+\operatorname{Sum}_{\mathbb R}(\ell)\\
&=C(a,v)_j+C(b,w)_j.
\end{aligned}
$$

两边同属$V_n$，逐点判等即得结论。$m=0$或$p=0$时相应段为空，其组合为$0_n$；$n=0$时全部输出为空向量。若只拼接系数却忘记同步拼接向量项，就改变了配对关系或输入类型，不能照用公式。

### 7. 固定坐标重编号可以移到组合之外 {#flc-reindex}

**FLC6。** 给坐标置换$\sigma:I_n\to I_n$，FRC定义$T_\sigma(x)=x\circ\sigma$。对向量表$v:I_m\to V_n$，定义新表$v^\sigma$为

$$
(v^\sigma)_k=T_\sigma(v_k)\quad(k\in I_m).
$$

每个输出仍在$V_n$，故$v^\sigma:I_m\to V_n$合法。此操作换的是**每项向量的坐标$j$**，没有改变向量项编号$k$或其系数。则

$$
C(a,v^\sigma)=T_\sigma(C(a,v)).
$$

对任意$j\in I_n$，$\sigma(j)\in I_n$，并有

$$
((v^\sigma)_k)_j=(v_k)_{\sigma(j)}\quad(k\in I_m).
$$

因此计算$C(a,v^\sigma)_j$的实数表，逐项等于计算$C(a,v)_{\sigma(j)}$的实数表；两表域均为$I_m$、目标均为$\mathbb R$，所以是同一表，其和相等。于是

$$
C(a,v^\sigma)_j=C(a,v)_{\sigma(j)}
=(T_\sigma(C(a,v)))_j.
$$

逐点判等得结论。FRC5已经证明$T_{\sigma^{-1}}$为$T_\sigma$的逆，因此对新组合应用它，便恢复$C(a,v)$。这不是两层求和换序：只在同一个坐标求值处改名，内层$I_m$上的项顺序始终保持。

### 8. 八道练习 {#flc-exercises}

#### 题1：两个向量合成一个向量 {#flc-q01}

取$m=2,n=2$，$v_0=(1,-1),v_1=(2,3)$，$a=(3,-2)$。列出每个坐标的加权实数表，求$C(a,v)$；再用$a_0v_0+a_1v_1$核结果。说明输入中哪个对象是实数、哪个是向量、哪个是向量表。 [完整解答](#flc-a01)

#### 题2：两个零参数与错类型 {#flc-q02}

分别描述$m=0,n=3$与$m=3,n=0$时$a,v$的类型和组合输出。若系数表为空、向量表却有两项，能否直接应用定义？若两向量项一项在$V_2$、一项在$V_3$，能否按现定义组合？解释两个零参数不能混为同一原因。 [完整解答](#flc-a02)

#### 题3：系数相加的完整证明 {#flc-q03}

对任意$a,b:I_m\to\mathbb R$与$v:I_m\to V_n$，完整逐坐标证明$C(a+b,v)=C(a,v)+C(b,v)$。每次写明内层表的域目标、实数分配与RFS3分别用在哪里，检查$m=0$及$n=0$。 [完整解答](#flc-a03)

#### 题4：共同缩放放在哪一层 {#flc-q04}

完整证明$C(ca,v)=cC(a,v)=C(a,cv)$，第二个等式须展开实数交换与结合。用题1数据分别检查$c=0$、$c=-1$。再证明全零系数表或全零向量表都给$0_n$，不要求$m,n$正。 [完整解答](#flc-a04)

#### 题5：每项的向量加法 {#flc-q05}

给$a:I_m\to\mathbb R$与$v,w:I_m\to V_n$，定义$v+w$并完整证明$C(a,v+w)=C(a,v)+C(a,w)$。说明“向量表项数相同”和“每项坐标数相同”分别保证哪一步合法；给一个坐标数不同导致当前定义无法使用的数据例。 [完整解答](#flc-a05)

#### 题6：两段同步拼接 {#flc-q06}

取$n=2$，前段$v_0=(1,0),v_1=(0,1)$、$a=(2,-1)$，后段$w_0=(1,1)$、$b=(3)$。列出拼接数据并求组合，核FLC5。再对一般$m,p,n$逐坐标证明拼接公式，说明后段局部自然差何时有定义。 [完整解答](#flc-a06)

#### 题7：系数未必能从结果唯一恢复 {#flc-q07}

固定$v_0=(1,1),v_1=(2,2)$。证明两份不同系数$(2,0)$和$(0,1)$给同一组合。对任意系数$(s,t)$写出组合的两个坐标，并证明$(1,0)$不可能由这两项获得。仅按已定义运算说明，不预用基、张成或维数定理。 [完整解答](#flc-a07)

#### 题8：换坐标与换向量项不同 {#flc-q08}

取$m=2,n=3$，$v_0=(1,2,0),v_1=(0,-1,3)$，$a=(2,1)$，坐标置换$\sigma=(2,0,1)$。分别计算先组合再换坐标、先逐项换坐标再组合，求逆置换并恢复原组合。然后给FLC6的一般逐坐标证明，明确没有交换项索引$k$。 [完整解答](#flc-a08)

### 9. 来源与范围 {#flc-sources}

实际核读Robert A. Beezer《A First Course in Linear Algebra》所列固定版本[“Linear Combinations”原文](https://raw.githubusercontent.com/rbeezer/fcla/347f27fe909b54b26970bcc0fcbf69c7e853c766/src/section-LC.xml)第1—125行，采用的内容边界是第1—29行的定义与输入输出类型说明；后续例子已读但未采用其数值或题解。原文使用复数列向量、从1起的索引。本书以已建实数、零起函数表和RFS实数和逐坐标定义，独立补足两个零参数、全部公式证明与八题完整解答，不把这些细节说成已由源文提供。

[固定版本COPYING](https://raw.githubusercontent.com/rbeezer/fcla/347f27fe909b54b26970bcc0fcbf69c7e853c766/COPYING.txt)为GFDL 1.2或以后，无不变节及封面文字。实际网络取得与缓存身份见制作记录`research/production/finite_coordinate_combinations_sources.json`。本书未复制翻译来源的例题、图或练习答案。

本单元只定义这类有限实坐标加权组合；没有建立一般对象上的向量和递归，没有证明任意项重排或双重和换序。系数可以重复、为零，向量项也可以重复；既不自动保证系数唯一，也不自动保证能产生$V_n$的每个向量。后续需要的表示理论须另给定义和证明。
