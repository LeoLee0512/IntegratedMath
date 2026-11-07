## 基础单元 B2.22 戴德金分割、次序与上确界 {#cut-unit}

**学习目标与位置。** 上一单元给出了非空、有上界却没有有理上确界的集合。本单元用有理数的某些下段作为新对象，证明这些对象可以比较大小，有理数可以保序地嵌入其中，而且每个非空有上界的新对象集合都有最小上界。主归属第526章97Fxx中的97F50“实数、复数（教育方面）”，本次只处理实数构造的集合与次序部分；06A05、03E20交叉。这里没有讨论复数，也未定义新对象的加法或乘法。

**精确先修。** 使用[集合成员、子集与外延相等](#fun-sets)、[函数的三项数据](#fun-definition)、[像的成员条件](#fun-image)、[有理数全序](#rord-laws)、[平移比较](#rord-translation)、[有理数中点](#qgap-density-archimedean)、[上界与上确界的定义](#qgap-supremum-definition)、[非负范围的平方比较](#sqrat-order)、[平方缺口的改进公式](#qgap-perturbation)及[没有有理上确界的结论](#qgap-no-rational-supremum)。本单元不把实数连续性或某个实数平方根作为先修。

**对象与记号。** 小写 $p,q,r,s$ 通常表示有理数，大写 $A,B,D,U$ 表示有理数的子集。集合 $A$ 本身与一个有理数 $q$ 是不同类型的对象。下文先定义分割，再用 $\mathbb R$ 记本构造中的全体分割。它的大小比较来自集合包含；本单元出现的 $q+1$、$q^2$ 等算式仍只对有理数进行。

### 1. 先说明允许形成哪些集合 {#cut-set-background}

此前已经采用按元素判等、已有数集、有限集合、有序对集合以及从已有集合按条件选取子集的背景，也收集过具体构造中的等价类。现在要收集有理数的所有下段，还须公开增加一项背景：

> 给定有理数集合 $\mathbb Q$，它的所有子集组成一个集合，记为 $\mathcal P(\mathbb Q)$，称为 $\mathbb Q$ 的幂集。允许从这个已有集合按明确条件选出子集。

于是 $A\in\mathcal P(\mathbb Q)$ 就是 $A\subseteq\mathbb Q$。这里采用幂集存在的集合背景，不宣称已经从一套集合论公理证明它，也不允许据此把没有限定范围的“所有对象”收成集合。

稍后给定一个由有理数子集构成的集合 $\mathcal F$，我们用

$$
\{q\in\mathbb Q:\text{存在 }A\in\mathcal F\text{ 使 }q\in A\}
$$

形成它的并集。这仍是从已有 $\mathbb Q$ 按条件选取子集，不需要先收集所有可能的集合族。证明中使用通常的反证和排中推理；从一个存在条件取一个见证，不等于为任意整个集合族同时选出见证。

### 2. 分割与有理数的下段 {#cut-definition}

戴德金在1872年的《连续性与无理数》中以有理数的分割讨论连续性与无理数；原著使用两侧分割，并讨论端点分配。本书采用现代常见的单侧下集表述，把“下段无最大元”明确放入定义，不把以下四条件逐字归作原著表述；版本对照见[来源审计](#rational-gaps-cuts-sources)。

**定义：戴德金分割的单侧形式。** 本书称 $A\subseteq\mathbb Q$ 为一个**分割**，当且仅当它满足四项条件：

1. **非空：** 存在 $a\in A$。
2. **不是整个 $\mathbb Q$：** 存在 $b\in\mathbb Q$ 使 $b\notin A$。
3. **向下封闭：** 若 $a\in A$ 且 $q\in\mathbb Q$ 满足 $q<a$，则 $q\in A$。
4. **没有最大元：** 对每个 $a\in A$，存在 $c\in A$ 使 $a<c$。

第四项要求较大见证仍在 $A$ 内。仅仅在 $\mathbb Q$ 中找一个较大数不够。第二项也不要求补集没有最小元。

按上一节采用的背景，定义集合

$$
\mathbb R
 =\{A\in\mathcal P(\mathbb Q):A\text{ 满足上述四项条件}\}.
$$

这就说明“全体分割”确在一个给定集合内按条件形成。我们用它作为实数构造中的对象集合；其运算尚待后续另行定义，现在只研究次序。

**命题 DC1：每个有理数给出一个分割。** 对 $r\in\mathbb Q$，令

$$
i(r)=\{q\in\mathbb Q:q<r\}.
$$

那么 $i(r)\in\mathbb R$。

**逐项证明。**

- $r-1<r$，所以 $r-1\in i(r)$，给出非空见证。【依据：$0<1$ 与有理平移比较。】
- $r\notin i(r)$，因为严格序不允许 $r<r$，故它不是整个 $\mathbb Q$。
- 若 $a\in i(r)$ 且 $q<a$，则 $a<r$，传递性给 $q<r$，所以 $q\in i(r)$。
- 若 $a\in i(r)$，则 $a<r$。[QG1](#qgap-density-archimedean)给中点 $m=(a+r)/2$ 满足 $a<m<r$。因而 $m\in i(r)$，且比 $a$ 大。

四项都成立，DC1证毕。特别地，$i(0)$ 已给出一个分割，所以 $\mathbb R$ 非空。

例如 $i(0)$ 收集严格小于零的有理数，$i(3/2)$ 收集严格小于 $3/2$ 的有理数。数 $r$ 不属于自己的下段 $i(r)$。它的补集恰为

$$
\mathbb Q\setminus i(r)=\{q\in\mathbb Q:q\ge r\},
$$

其中 $r$ 是最小元：它在补集中，且每个补集成员都不小于它。这不违反分割条件，因为无最大元的要求施加在下段上。

若改用 $\{q\in\mathbb Q:q\le r\}$，这个集合虽然非空、真小于 $\mathbb Q$ 且向下封闭，却含有最大元 $r$，不再是本书定义的分割。

### 3. 包含为什么在这些对象上成为全序 {#cut-order-embedding}

对 $A,B\in\mathbb R$ 定义

$$
A\le_{\mathbb R}B\quad\Longleftrightarrow\quad A\subseteq B,
$$

并定义

$$
A<_{\mathbb R}B
\quad\Longleftrightarrow\quad A\subseteq B\text{ 且 }A\ne B.
$$

**命题 DC2。** $\le_{\mathbb R}$ 是全序；映射 $i:\mathbb Q\to\mathbb R$ 保持并反映次序，并且单射。具体说，对有理数 $r,s$，

$$
\begin{aligned}
r\le s&\quad\Longleftrightarrow\quad i(r)\le_{\mathbb R}i(s),\\
r=s&\quad\Longleftrightarrow\quad i(r)=i(s),\\
r<s&\quad\Longleftrightarrow\quad i(r)<_{\mathbb R}i(s).
\end{aligned}
$$

**先证明序律。** 任取 $A$ 的一个成员，它当然仍属于 $A$，故 $A\subseteq A$，这是自反性。若 $A\subseteq B$ 且 $B\subseteq C$，则 $q\in A$ 依次推出 $q\in B$、$q\in C$，所以 $A\subseteq C$，这是传递性。若 $A\subseteq B$ 且 $B\subseteq A$，两集合具有完全相同的成员，外延相等给 $A=B$，这是反对称性。

还须证明任意两个分割可比。若 $A\subseteq B$，已经得到一个方向。否则，取

$$
a\in A,\qquad a\notin B.
$$

任取 $b\in B$。有理数三歧性给 $b<a$、$b=a$、$a<b$ 三种情形。若 $b=a$，则 $a\in B$，矛盾；若 $a<b$，$B$ 的向下封闭性同样给 $a\in B$，矛盾。所以 $b<a$。由 $a\in A$ 和 $A$ 向下封闭，得 $b\in A$。这对任意 $b\in B$ 成立，故 $B\subseteq A$，可比性证毕。

【依据：这里用到了两个集合的下闭性质。普通子集并不总可比，例如 $\{0\}$ 不包含于 $\{1\}$，$\{1\}$ 也不包含于 $\{0\}$。】

**再证明嵌入。** 每个输入 $r\in\mathbb Q$ 按成员条件唯一确定 $i(r)$，DC1保证输出在 $\mathbb R$ 中，所以定义域为 $\mathbb Q$、目标为 $\mathbb R$ 的函数 $i$ 已成立。

若 $r\le s$，任取 $q\in i(r)$，有 $q<r\le s$，混合传递给 $q<s$，于是 $q\in i(s)$。故 $i(r)\subseteq i(s)$。

反过来，若 $i(r)\subseteq i(s)$，却有 $r>s$，则

$$
s\in i(r),\qquad s\notin i(s),
$$

违反包含关系。因此三歧性排除 $r>s$，留下 $r\le s$。这证明了次序的两个方向。

若 $i(r)=i(s)$，两个方向的包含分别给 $r\le s$ 与 $s\le r$，有理序的反对称性给 $r=s$。反向 $r=s$ 时两个下段成员条件相同，当然相等。所以 $i$ 单射。

若 $r<s$，前面已给 $i(r)\subseteq i(s)$；而 $r\in i(s)$、$r\notin i(r)$，故包含严格。反过来，若 $i(r)<_{\mathbb R}i(s)$，反射给 $r\le s$，相等 $r=s$ 又会给下段相等，与严格包含矛盾，所以 $r<s$。DC2全部结论得证。

这是一份**次序嵌入**：有理数的大小信息得以完整保留。当前尚未定义目标集合中的加法与乘法，不能据此宣称这些运算也已保持。

**每个分割上下还有其他分割。** 任取 $A\in\mathbb R$。由非空性取 $a\in A$，则 $i(a)\subseteq A$，因为每个 $q<a$ 都由下闭性属于 $A$；又有 $a\in A$ 而 $a\notin i(a)$，所以

$$
i(a)<_{\mathbb R}A.
$$

由真子集条件取 $b\notin A$。对任何 $q\in A$，$q=b$ 会直接矛盾，$b<q$ 会由下闭性推出 $b\in A$；故只能 $q<b$。于是 $A\subseteq i(b)\subseteq i(b+1)$。又因为 $b\in i(b+1)$ 而 $b\notin A$，得到

$$
A<_{\mathbb R}i(b+1).
$$

所以 $\mathbb R$ 没有最小元素，也没有最大元素。这些见证的构造不需要在所有分割中同时选取成员。

### 4. 平方缺口给出一个不来自有理数的分割 {#cut-gap}

沿用上一单元的集合

$$
S=\{q\in\mathbb Q:0\le q\text{ 且 }q^2<2\}.
$$

它本身不是分割：$0\in S$，但 $-1<0$ 且 $-1\notin S$，不满足下闭性。我们另定义

$$
D=\{q\in\mathbb Q:q<0\text{，或 }(q\ge0\text{ 且 }q^2<2)\}.
$$

**命题 DC3。** $D$ 是一个分割，并且

$$
q\in D
\quad\Longleftrightarrow\quad
\text{存在 }s\in S\text{ 使 }q<s.
$$

不存在有理数 $r$ 使 $D=i(r)$。

**先核四项条件。**

非空：$0\ge0$ 且 $0^2=0<2$，所以 $0\in D$。

真子集：二不是负数，且 $2^2=4>2$，故 $2\notin D$。

下闭：设 $q\in D$，且 $p<q$。若 $p<0$，它直接满足 $D$ 的第一支。若 $p\ge0$，则 $q>p\ge0$，所以 $q$ 不可能属于负数支，只能满足 $q^2<2$。现在 $p,q$ 都非负，可以使用[SQ1](#sqrat-order)，得到

$$
p^2<q^2<2.
$$

因此 $p$ 满足第二支，仍在 $D$ 中。两种情况覆盖全部 $p$。

无最大元：若 $q\in D$ 且 $q<0$，取 $0\in D$，有 $q<0$。若 $q\ge0$，则 $q\in S$。[QG3](#qgap-perturbation)已经证明

$$
f(q)=\frac{2q+2}{q+2}\in S,\qquad q<f(q).
$$

因为 $S\subseteq D$，$f(q)$ 就是更大的 $D$ 成员。这里分母合法与 $f(q)$ 的平方条件都来自 QG3；零输入也包含在其证明中。四项条件齐备，故 $D\in\mathbb R$。

**再证严格下段的描述。** 若 $q\in D$ 且 $q<0$，取 $s=0\in S$，满足 $q<s$。若 $q\in D$ 且 $q\ge0$，则 $q\in S$，取 $s=f(q)\in S$，也有 $q<s$。这证明左到右。

反向，设存在 $s\in S$ 使 $q<s$。若 $q<0$，则 $q\in D$。若 $q\ge0$，因为 $s\ge0$，SQ1给 $q^2<s^2<2$，所以 $q\in D$。双向等价得证。

该描述可读作：$D$ 收集所有某个 $S$ 成员以下的有理数。特别地，每个 $s\in S$ 都给 $i(s)\subseteq D$；而每个 $q\in D$ 又属于某个这样的 $i(s)$。这是一条逐成员结论，尚未调用一般上确界定理。

**最后证明它不是有理数的下段。** 反设存在 $r\in\mathbb Q$ 使 $D=i(r)$。对任意 $s\in S$，有

$$
i(s)\subseteq D=i(r).
$$

DC2的次序反射给 $s\le r$。因此 $r$ 是 $S$ 的有理上界。

现在任取 $S$ 的一个有理上界 $u$。对每个 $s\in S$，$s\le u$，DC2给 $i(s)\subseteq i(u)$。任取 $q\in D$，由刚证的成员描述取 $s\in S$ 使 $q\in i(s)$，所以 $q\in i(u)$。于是

$$
D=i(r)\subseteq i(u),
$$

再次反射得到 $r\le u$。这说明 $r$ 不大于任何有理上界，因而就是 $S$ 的有理上确界，与[QG4](#qgap-no-rational-supremum)矛盾。故这样的 $r$ 不存在，DC3证毕。

可以把形如 $i(r)$ 的分割称为本书的**有理下段**，把不属于像 $i(\mathbb Q)$ 的分割称为**非主分割**；$D$ 是已证明的例子。这说明新集合中的对象确实比有理下段更多。此时只证明了次序上的扩充，没有对分割定义平方，因此还不能用平方根性质给 $D$ 命名。

### 5. 非空有上界的分割族：并集就是上确界 {#cut-supremum}

这里的**分割族** $\mathcal F\subseteq\mathbb R$ 是一个集合，它的元素 $A$ 自身又是有理数的子集。须分清

$$
A\in\mathcal F\qquad\text{和}\qquad q\in A.
$$

前者说哪个分割属于这族，后者说哪个有理数属于这个分割。

按包含次序，$U\in\mathbb R$ 是 $\mathcal F$ 的上界，指对每个 $A\in\mathcal F$ 都有 $A\subseteq U$。上确界是一个这样的上界 $V$，并满足：若 $W\in\mathbb R$ 也是上界，则 $V\subseteq W$。若两个分割均满足此条件，彼此包含，故外延相等；所以存在时唯一，记为 $\sup_{\mathbb R}\mathcal F$。

**命题 DC4。** 设 $\mathcal F\subseteq\mathbb R$ 非空，且存在一个分割上界 $U\in\mathbb R$。定义

$$
V=\{q\in\mathbb Q:\text{存在 }A\in\mathcal F\text{ 使 }q\in A\}.
$$

那么 $V\in\mathbb R$，并且 $\sup_{\mathbb R}\mathcal F=V$。这个集合通常记作并集 $\bigcup\mathcal F$。

**先证明 $V$ 是分割。**

非空：从 $\mathcal F\ne\varnothing$ 取 $A_0\in\mathcal F$。由于 $A_0$ 是分割，存在 $a_0\in A_0$。于是 $a_0\in V$。

真子集：任取 $q\in V$，有一个见证 $A\in\mathcal F$ 使 $q\in A$。上界条件给 $A\subseteq U$，所以 $q\in U$。这证明 $V\subseteq U$。因为 $U$ 是分割，可取 $b\in\mathbb Q$ 满足 $b\notin U$，于是 $b\notin V$，保证 $V\ne\mathbb Q$。

下闭：设 $q\in V$ 且 $p<q$。取 $A\in\mathcal F$ 使 $q\in A$，由 $A$ 下闭得到 $p\in A$，于是 $p\in V$。

无最大元：设 $q\in V$，仍取一个见证 $A\in\mathcal F$ 使 $q\in A$。由 $A$ 无最大元，存在 $r\in A$ 满足 $q<r$。同一个 $A$ 又见证 $r\in V$，所以每个 $V$ 成员都有更大成员。

至此四项条件成立，$V$ 确实是允许作为上确界的新对象。

**再证明共同上界与最小性。** 对任意 $A\in\mathcal F$，若 $q\in A$，那么 $A$ 本身就见证 $q\in V$。故 $A\subseteq V$，$V$ 是共同上界。

若 $W\in\mathbb R$ 是任意另一个共同上界，任取 $q\in V$，选择一个见证 $A\in\mathcal F$ 使 $q\in A$。因 $A\subseteq W$，得 $q\in W$，所以 $V\subseteq W$。这正是最小性。DC4证毕。

【见证范围：非空性只取一个 $A_0$ 和其中一点；其他证明对一个给定 $q$ 使用其存在见证。没有构造一个同时为每个 $A\in\mathcal F$ 选出成员的函数，因此没有使用选择公理。】

### 6. 同一个缺口，在较大有序集合中有了上确界 {#cut-gap-supremum}

从已有 $\mathbb R$ 按条件形成

$$
\mathcal F_S
 =\{A\in\mathbb R:\text{存在 }s\in S\text{ 使 }A=i(s)\}.
$$

因为 $0\in S$，有 $i(0)\in\mathcal F_S$，所以它非空。又因二是 $S$ 的有理上界，每个 $s\in S$ 都满足 $s\le2$，DC2给 $i(s)\subseteq i(2)$，所以 $i(2)$ 是该分割族的上界。

DC4因此适用。对任意 $q\in\mathbb Q$，逐项展开并集的成员条件：

$$
\begin{aligned}
q\in\bigcup\mathcal F_S
&\quad\Longleftrightarrow\quad
\text{存在 }s\in S\text{ 使 }q\in i(s)\\
&\quad\Longleftrightarrow\quad
\text{存在 }s\in S\text{ 使 }q<s\\
&\quad\Longleftrightarrow\quad q\in D.
\end{aligned}
$$

最后一步是DC3。外延相等给 $\bigcup\mathcal F_S=D$，于是

$$
\sup_{\mathbb R}\mathcal F_S=D.
$$

这与 $S$ 没有有理上确界相容：$S$ 是 $\mathbb Q$ 中的集合，$\mathcal F_S$ 是 $\mathbb R$ 中的集合，而 $D$ 已证不属于 $i(\mathbb Q)$。嵌入保持原有次序，较大的对象集合容纳了原来没有的最小上界。

### 7. 两个条件不可删除，算术也不能自动补上 {#cut-boundaries}

**空族。** 若 $\mathcal F=\varnothing$，没有 $A\in\mathcal F$ 能见证任何有理数属于并集，所以并集为空，不是分割。事实上空族没有 $\mathbb R$ 中的上确界：每个分割都是真空成立的共同上界；若某个 $V$ 是最小上界，DC2后证明的无端点性质却给一个 $L<_{\mathbb R}V$。最小性要求 $V\subseteq L$，与严格较小矛盾。

**无界族。** 令

$$
\mathcal G=i(\mathbb Q)
 =\{A\in\mathbb R:\text{存在 }r\in\mathbb Q\text{ 使 }A=i(r)\}.
$$

任取 $q\in\mathbb Q$，有 $q<q+1$，所以 $q\in i(q+1)$，而 $i(q+1)\in\mathcal G$。因此 $\bigcup\mathcal G=\mathbb Q$，不满足分割的真子集条件。

这个族也确实没有分割上界。若 $U$ 是共同上界，由 $U$ 的真子集条件取 $b\notin U$；可是 $b\in i(b+1)$ 且 $i(b+1)\subseteq U$，矛盾。不能把整个 $\mathbb Q$ 添加为一个已经符合定义的最大分割。

因此本单元准确得到的性质是：**每个非空且有上界的分割集合，在 $\mathbb R$ 中有唯一上确界。** 它也称最小上界性质。我们没有证明“任意分割族都有上确界”，也没有加入无穷大对象。

最后，$q\in A$、$A\in\mathbb R$、$A\le_{\mathbb R}B$ 各有不同含义。现有有理运算不能仅因新对象也叫“数”就直接施加到这些集合上。后续需要定义分割运算、证明结果仍是分割，并验证与有理嵌入相容；这些是新的证明任务。

### 8. 课后题 {#cut-exercises}

#### 题1：四个条件分别排除什么 {#cut-q01}

逐项检查 $i(0)$、$i(3/2)$ 是分割。说明 $\varnothing$、$\mathbb Q$、$\{q\in\mathbb Q:q\le0\}$ 各违反哪项条件；对最后一个集合说明另外三项为什么仍成立。[完整解答](#cut-a01)

#### 题2：下段与补集的端点 {#cut-q02}

对任意 $r\in\mathbb Q$ 完整证明 $i(r)$ 是分割，明确四项见证或推理。证明其补集恰为 $\{q\in\mathbb Q:q\ge r\}$ 且最小元是 $r$；解释补集有最小元为什么不矛盾。[完整解答](#cut-a02)

#### 题3：包含何时成为全序 {#cut-q03}

逐成员证明分割包含序的自反、传递、反对称与可比性。不包含时须给差集见证，并对另一集合任意成员展开三歧性。给两个不可比的普通有理子集，说明证明在哪里需要下闭条件。[完整解答](#cut-a03)

#### 题4：保序、反射与上下见证 {#cut-q04}

完整证明 $i$ 保持并反映 $\le$、$<$ 与相等，说明为何得到单射。解释 $r$ 与 $i(r)$ 的对象区别。再对任意分割 $A$ 构造 $L,H\in\mathbb R$，使 $L<_{\mathbb R}A<_{\mathbb R}H$，给出两处严格性的差集见证。[完整解答](#cut-a04)

#### 题5：把平方缺口变成下闭分割 {#cut-q05}

说明 $S$ 不是分割；对本单元的 $D$ 完整证明四项条件，并证明 $q\in D$ 当且仅当存在 $s\in S$ 使 $q<s$。负输入和非负输入须分开处理，零处不得遗漏较大见证。[完整解答](#cut-a05)

#### 题6：新分割不来自任何有理下段 {#cut-q06}

反设 $D=i(r)$，依次证明 $r$ 是 $S$ 的有理上界，且不大于每个有理上界，由此推出矛盾。指出哪里用次序反射，说明这个结论为何还不能写成分割的平方等式。[完整解答](#cut-a06)

#### 题7：并集不仅要包含每一项 {#cut-q07}

设 $\mathcal F\subseteq\mathbb R$ 非空，且有分割上界 $U$。按成员条件定义 $V$，逐项证明它是分割，明确非空和真子集见证。再分别证明 $V$ 是共同上界及不大于任何共同上界。[完整解答](#cut-a07)

#### 题8：改变上确界所在的有序集合 {#cut-q08}

完整证明 $\sup_{\mathbb R}\mathcal F_S=D$，并解释与 $S$ 无有理上确界的关系。证明空分割族没有上确界，全体有理下段族没有分割上界；核两族的并集各是什么。说明上述证明为什么不需选择公理，也不能添加未经定义的最大分割或无穷大。[完整解答](#cut-a08)

**来源与范围说明。** 定义版本与公开来源的对照见[本批来源审计](#rational-gaps-cuts-sources)。本书采用非空、非全体、下闭、无最大元的单侧分割约定，逐项证明其序结构。已证的是非空有上界子集的最小上界性质；分割算术及实数平方根的存在性不在本单元结论内。有限样本或程序不能枚举全部分割，也不能替代DC1—DC4的全称证明。
