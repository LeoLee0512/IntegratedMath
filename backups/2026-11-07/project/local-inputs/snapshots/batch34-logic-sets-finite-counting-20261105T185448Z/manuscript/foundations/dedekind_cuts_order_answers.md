## 基础单元 B2.22 课后题完整解答 {#cut-answers}

以下解答对应[戴德金分割、次序与上确界](#cut-unit)。$\mathbb R$ 是本书由 $\mathbb Q$ 子集构成的分割集合，$A\le_{\mathbb R}B$ 的含义是 $A\subseteq B$。对有理输入进行的加减乘除仍在 $\mathbb Q$ 中；这里不使用尚未定义的分割运算。每个“分割”结论都须检查非空、非全体、下闭、无最大元四项。

### 题1：四个条件分别排除什么 {#cut-a01}

[返回题目](#cut-q01)

先看 $i(0)=\{q\in\mathbb Q:q<0\}$。

1. $-1<0$，所以 $-1\in i(0)$，集合非空。
2. $0\notin i(0)$，因为 $0<0$ 不成立，所以它不是整个 $\mathbb Q$。
3. 若 $q\in i(0)$ 且 $p<q$，则 $p<q<0$，由传递性得 $p<0$，于是 $p\in i(0)$。
4. 若 $q\in i(0)$，则 $q<0$。由[有理中点结论](#qgap-density-archimedean)，$q<(q+0)/2<0$。故 $q/2$ 是集合内比 $q$ 更大的成员，集合没有最大元。

再看 $i(3/2)=\{q\in\mathbb Q:q<3/2\}$。

1. $1<3/2$，所以 $1\in i(3/2)$，集合非空。严格比较可由 $3/2-1=1/2>0$ 得到。
2. $3/2\notin i(3/2)$，所以它不是整个 $\mathbb Q$。
3. 若 $q<3/2$ 且 $p<q$，则 $p<3/2$，故 $p\in i(3/2)$。
4. 若 $q<3/2$，则中点 $m=(q+3/2)/2$ 是有理数，并满足 $q<m<3/2$。于是 $m$ 是更大的集合成员。

所以这两个集合都满足四项，是分割。两次中点的除数二均为严格正的有理数，输入任意有理 $q$ 都合法。

空集 $\varnothing$ 违反第一项非空条件。它的下闭和无最大元条件按“对每个成员”表述时都真空成立，但这不能弥补没有任何成员。

整个 $\mathbb Q$ 违反第二项：不存在有理数位于它之外。它非空、下闭，每个 $q$ 又有更大的 $q+1\in\mathbb Q$；仍因第二项失败而不是分割。

令 $E=\{q\in\mathbb Q:q\le0\}$。它非空，因为 $0\in E$；它是真子集，因为 $1\notin E$；它下闭，因为 $p<q\le0$ 推出 $p<0$，从而 $p\le0$、$p\in E$。但 $0\in E$ 且每个成员都不大于零，所以零是最大元。特别地，对成员零无法找到 $c\in E$ 使 $0<c$，故第四项失败。

这说明四项需要同时满足，不能用三项代替完整定义。

### 题2：下段与补集的端点 {#cut-a02}

[返回题目](#cut-q02)

任取 $r\in\mathbb Q$，定义 $i(r)=\{q\in\mathbb Q:q<r\}$。四项核查如下。

非空：由 $-1<0$ 和平移比较得 $r-1<r$，所以 $r-1\in i(r)$。

真子集：严格序的非自反性给 $r\notin i(r)$，因此有一个有理数不在该集合内。

下闭：设 $a\in i(r)$ 且 $q<a$。成员定义给 $a<r$，与 $q<a$ 合成 $q<r$，所以 $q\in i(r)$。

无最大元：设 $a\in i(r)$，则 $a<r$。中点 $m=(a+r)/2$ 属于 $\mathbb Q$，并满足 $a<m<r$。故 $m\in i(r)$ 且比 $a$ 大。

于是 $i(r)$ 是分割。这里的最后一步是对每一个给定成员构造一个更大成员，并没有把端点 $r$ 加入下段。

对任意 $q\in\mathbb Q$，

$$
q\in\mathbb Q\setminus i(r)
\quad\Longleftrightarrow\quad q\not<r
\quad\Longleftrightarrow\quad q\ge r.
$$

第二个等价来自有理数三歧性：不是小于时，只可能相等或大于。因此补集恰为 $\{q\in\mathbb Q:q\ge r\}$。数 $r$ 自己满足 $r\ge r$，所以属于补集；每个补集成员又按定义不小于 $r$，故 $r$ 是其最小元。

分割第四项限制的是下段没有最大元，没有要求补集没有最小元。本题补集的最小元与下段的无最大元可以同时成立。若把下段改成 $q\le r$，则 $r$ 被包含且成为最大元，才会违反本书约定。

### 题3：包含何时成为全序 {#cut-a03}

[返回题目](#cut-q03)

对分割 $A,B$，定义 $A\le_{\mathbb R}B$ 当且仅当 $A\subseteq B$。

**自反性。** 任取 $q\in A$，结论 $q\in A$ 本来就成立，所以 $A\subseteq A$。

**传递性。** 设 $A\subseteq B$ 且 $B\subseteq C$。任取 $q\in A$，第一个包含给 $q\in B$，第二个给 $q\in C$。因此 $A\subseteq C$。

**反对称性。** 设 $A\subseteq B$ 且 $B\subseteq A$。前者说明 $A$ 的每个成员都是 $B$ 成员，后者说明反向也成立，所以两集合成员相同。由[外延相等](#fun-sets)，$A=B$。

**任意两项可比。** 若 $A\subseteq B$，已经有需要的一个方向。否则按不包含的含义取 $a\in A$ 且 $a\notin B$。任取 $b\in B$，在有理数全序中分三种情形：

- 若 $b=a$，由 $b\in B$ 得 $a\in B$，矛盾。
- 若 $a<b$，由 $b\in B$ 和 $B$ 下闭得 $a\in B$，矛盾。
- 所以只剩 $b<a$。因为 $a\in A$ 且 $A$ 下闭，得到 $b\in A$。

每个 $b\in B$ 都属于 $A$，所以 $B\subseteq A$。于是任意两分割至少有一个包含方向。结合前面三条，包含在分割集合上是全序。

普通有理子集 $E=\{0\}$、$F=\{1\}$ 不可比：零在 $E$ 但不在 $F$，故 $E\nsubseteq F$；一在 $F$ 但不在 $E$，故 $F\nsubseteq E$。这不违反刚证结论，因为它们不是下闭集合。例如 $-1<0\in E$，却 $-1\notin E$；$0<1\in F$，却 $0\notin F$。

可比性证明中的两次下闭推理是关键：一次排除 $a<b$，另一次从 $b<a$ 把 $b$ 送入 $A$。只使用普通集合包含的三条序律，不能自动得到可比性。

### 题4：保序、反射与上下见证 {#cut-a04}

[返回题目](#cut-q04)

对每个有理输入 $r$，成员条件 $q<r$ 唯一规定一个子集 $i(r)$；上一题组已证明该子集是分割。因此 $i$ 有明确的定义域 $\mathbb Q$、目标 $\mathbb R$ 和唯一输出，是一个函数。

**非严格次序。** 若 $r\le s$，对任意 $q\in i(r)$，有 $q<r\le s$，混合传递给 $q<s$，所以 $q\in i(s)$。于是 $i(r)\subseteq i(s)$。

反向设 $i(r)\subseteq i(s)$。如果 $s<r$，则 $s\in i(r)$，但 $s\notin i(s)$，违反包含。故不可能 $s<r$，三歧性给 $r\le s$。由此

$$
r\le s\quad\Longleftrightarrow\quad i(r)\le_{\mathbb R}i(s).
$$

**相等与单射。** 若 $r=s$，两个成员条件相同，所以 $i(r)=i(s)$。反向，若两下段相等，它们彼此包含，刚证的反射分别给 $r\le s$、$s\le r$，故 $r=s$。所以输出相等必输入相等，$i$ 单射。

**严格次序。** 若 $r<s$，先由非严格结论得 $i(r)\subseteq i(s)$。同时 $r\in i(s)$ 而 $r\notin i(r)$，有明确差集见证，所以 $i(r)\ne i(s)$，即 $i(r)<_{\mathbb R}i(s)$。

反向，若 $i(r)<_{\mathbb R}i(s)$，包含反射给 $r\le s$；若 $r=s$，函数值应相等，又与严格包含矛盾。因此 $r<s$。

有理数 $r$ 是前文由整数记录构造的对象，$i(r)$ 则是所有小于它的有理数组成的集合。嵌入将前者对应到后者；它们不是同一次构造中的同一写法。当前的保序结果也没有定义目标中的算术。

**严格较小的分割。** 任取 $A\in\mathbb R$，由非空性取 $a\in A$。令 $L=i(a)$，DC1给 $L\in\mathbb R$。若 $q\in L$，则 $q<a$，由 $A$ 下闭得到 $q\in A$，所以 $L\subseteq A$。又有 $a\in A$、$a\notin L$，差集非空，故 $L<_{\mathbb R}A$。

**严格较大的分割。** 由 $A\ne\mathbb Q$ 取 $b\in\mathbb Q$ 且 $b\notin A$。令 $H=i(b+1)$，它也是分割。任取 $q\in A$：若 $q=b$，直接矛盾；若 $b<q$，由 $A$ 下闭也得到 $b\in A$，矛盾。因此 $q<b<b+1$，从而 $q\in H$。所以 $A\subseteq H$。而 $b<b+1$ 给 $b\in H$，同时 $b\notin A$，所以 $A<_{\mathbb R}H$。

最终得到 $L<_{\mathbb R}A<_{\mathbb R}H$，两处严格性的见证分别为 $a$、$b$。这证明任意分割都不是整个序的最小或最大元素；仅为这个给定的 $A$ 各取一个见证即可。

### 题5：把平方缺口变成下闭分割 {#cut-a05}

[返回题目](#cut-q05)

集合 $S$ 要求成员非负，所以 $-1\notin S$；但 $0\in S$ 且 $-1<0$。这说明 $S$ 不下闭，因而不是分割。非空、有上界、无最大元都不能弥补下闭条件的失败。

考虑

$$
D=\{q\in\mathbb Q:q<0\text{，或 }(q\ge0\text{ 且 }q^2<2)\}.
$$

**非空。** 零非负且 $0^2=0<2$，所以 $0\in D$。

**真子集。** 二不是负数，且平方四不小于二，所以两个成员分支都不适用于二，$2\notin D$。

**向下封闭。** 设 $q\in D$ 且 $p<q$。若 $p<0$，由定义第一支 $p\in D$。若 $p\ge0$，则 $q>p\ge0$；$q$ 不能是负数，故其成员条件必为 $q^2<2$。现在 $0\le p<q$，由SQ1的非负严格平方比较得 $p^2<q^2<2$。因此 $p$ 也满足第二支，$p\in D$。没有对负数套用非负范围的平方单调性。

**无最大元。** 任取 $q\in D$。如果 $q<0$，零是 $D$ 中严格较大的成员。如果 $q\ge0$，则 $q\in S$，QG3给

$$
f(q)=\frac{2q+2}{q+2}\in S\subseteq D,
\qquad q<f(q).
$$

这里 $q+2>0$，所以公式合法；QG3已经分别证明 $f(q)>0$、$f(q)^2<2$ 与较大关系。特别当 $q=0$ 时，$f(0)=1$，零也确有严格较大见证。于是 D 四项全满足，是分割。

再证等价描述。若 $q\in D$ 且 $q<0$，取 $s=0$，则 $s\in S$ 且 $q<s$。若 $q\in D$ 且 $q\ge0$，则 $q\in S$，取 $s=f(q)$，QG3保证 $s\in S$ 且 $q<s$。所以每个 D 成员严格小于某个 S 成员。

反过来，设 $s\in S$ 且 $q<s$。如果 $q<0$，立刻有 $q\in D$。如果 $q\ge0$，则 $q,s$ 都非负，SQ1给 $q^2<s^2<2$，所以 $q\in D$。两种方向合起来得到

$$
q\in D\quad\Longleftrightarrow\quad
\exists s\in S,\ q<s.
$$

因此 D 是由 S 的所有严格下段收集而成的集合。这个等式中特别需要 S 没有最大元，才能把每个非负 D 成员本身放入某个严格下段；不能只把自己当作满足严格不等式的见证。

### 题6：新分割不来自任何有理下段 {#cut-a06}

[返回题目](#cut-q06)

反设有 $r\in\mathbb Q$ 使 $D=i(r)$。上题的成员等价式说明：对每个 $s\in S$，任何 $q\in i(s)$ 都满足 $q<s$，因此 $q\in D$。所以

$$
i(s)\subseteq D=i(r).
$$

由 $i$ 的次序反射，$s\le r$。这是对每个 $s\in S$ 的结论，所以 $r$ 是 $S$ 的有理上界。仅证明这一步还不够导出矛盾，因为 S 本来就有有理上界。

接着任取 $S$ 的任何有理上界 $u$。对每个 $s\in S$ 都有 $s\le u$，保序性给 $i(s)\subseteq i(u)$。现任取 $q\in D$，由上题等价描述取 $s\in S$ 满足 $q<s$，即 $q\in i(s)$。所以 $q\in i(u)$，证明

$$
D=i(r)\subseteq i(u).
$$

第二次使用次序反射，得到 $r\le u$。因 $u$ 是任意上界，$r$ 不大于所有上界；结合前面的“r本身是上界”，$r$ 满足有理上确界的两项定义。这与QG4证明的 S 无有理上确界矛盾。

因此没有这样的有理 $r$，$D\notin i(\mathbb Q)$。本书称这类分割为非主分割，结论是新对象集合确实超出了有理下段的像。

两个反射步骤分别把包含关系送回“r是上界”和“r最小”这两个数值结论。它们只涉及序。当前尚未定义两个分割怎样相乘，也未给分割的平方运算，所以不能把这个结果直接写成 $D$ 的平方等式。原先定义 D 时出现的 $q^2$ 是有理数的平方，不是 D 这个集合的平方。

### 题7：并集不仅要包含每一项 {#cut-a07}

[返回题目](#cut-q07)

设 $\mathcal F\subseteq\mathbb R$ 非空，且 $U\in\mathbb R$ 满足对每个 $A\in\mathcal F$ 都有 $A\subseteq U$。从已有 $\mathbb Q$ 按条件定义

$$
V=\{q\in\mathbb Q:\exists A\in\mathcal F,\ q\in A\}.
$$

这是一个有理数子集，尚须检查它是分割。

**非空。** 因 $\mathcal F$ 非空，存在 $A_0\in\mathcal F$。因 $A_0$ 是分割，存在 $a_0\in A_0$。这两个成员关系正好满足 V 的存在条件，故 $a_0\in V$。第一层非空给一个集合，第二层非空才给一个有理数。

**真子集。** 任取 $q\in V$，有见证 $A\in\mathcal F$ 使 $q\in A$；上界假设给 $A\subseteq U$，所以 $q\in U$。因此 $V\subseteq U$。又因 $U$ 是分割，存在有理数 $b\notin U$；若 $b\in V$，包含会给 $b\in U$，矛盾。因此 $b\notin V$，V 不是整个 Q。这里必须用到一个允许的分割上界，不能只说每个 A 都是真子集便认定并集也是真子集。

**下闭。** 若 $q\in V$ 且 $p<q$，取 $A\in\mathcal F$ 使 $q\in A$。$A$ 下闭，所以 $p\in A$；同一个 A 见证 $p\in V$。

**无最大元。** 若 $q\in V$，取 $A\in\mathcal F$ 使 $q\in A$。$A$ 无最大元，所以存在 $r\in A$ 满足 $q<r$。因此 $r\in V$ 且严格大于 q。此论证适用于每个 q，故 V 无最大元。

四项成立，$V\in\mathbb R$。然后验证上确界的两个要求。

**共同上界。** 任取 $A\in\mathcal F$。对任何 $q\in A$，这个 A 就是 V 成员条件的见证，所以 $q\in V$。故 $A\subseteq V$。这对每一项成立，V 是共同上界。

**最小性。** 任取另一个共同上界 $W\in\mathbb R$。若 $q\in V$，就有某个 $A\in\mathcal F$ 使 $q\in A$。共同上界条件给 $A\subseteq W$，从而 $q\in W$。所以 $V\subseteq W$，即 $V\le_{\mathbb R}W$。因 W 任意，V 是最小上界。

若还有另一个最小上界 $V'$，两个最小性分别给 $V\subseteq V'$ 和 $V'\subseteq V$，外延相等给 $V=V'$。因此可以唯一地记

$$
\sup_{\mathbb R}\mathcal F=V=\bigcup\mathcal F.
$$

“并集包含每一项”只完成共同上界一项；分割合法性与不大于任意上界的证明都不能省略。

### 题8：改变上确界所在的有序集合 {#cut-a08}

[返回题目](#cut-q08)

先从 R 按条件定义

$$
\mathcal F_S
 =\{A\in\mathbb R:\exists s\in S,\ A=i(s)\}.
$$

因为 $0\in S$，$i(0)\in\mathcal F_S$，所以族非空。二是 S 的有理上界；若 $A\in\mathcal F_S$，取 $s\in S$ 使 $A=i(s)$，则 $s\le2$，保序性给 $A=i(s)\subseteq i(2)$。因此 $i(2)\in\mathbb R$ 是共同上界。上题的定理适用。

任取 $q\in\mathbb Q$。如果 $q\in\bigcup\mathcal F_S$，存在 $A\in\mathcal F_S$ 使 $q\in A$，再按族的定义取 $s\in S$ 使 $A=i(s)$，得到 $q<s$。反过来，如果有 $s\in S$ 满足 $q<s$，则 $i(s)\in\mathcal F_S$ 且 $q\in i(s)$，故 $q\in\bigcup\mathcal F_S$。结合题5，

$$
q\in\bigcup\mathcal F_S
\quad\Longleftrightarrow\quad\exists s\in S,\ q<s
\quad\Longleftrightarrow\quad q\in D.
$$

所以外延相等给 $\bigcup\mathcal F_S=D$，上题的最小上界定理给

$$
\sup_{\mathbb R}\mathcal F_S=D.
$$

S 的有理上确界不存在，谈的是在 Q 内寻找一个有理上界中的最小者。现在 $\mathcal F_S$ 的元素是分割，而 D 是分割序中的上确界；题6已经证明 D 不等于任何 $i(r)$。两个结论处于不同有序集合，彼此相容。当前结论仍不涉及分割乘法。

**空族的边界。** 对 $\mathcal F=\varnothing$，任意有理 q 都找不到 $A\in\mathcal F$ 的见证，故并集是 $\varnothing$，不是分割。另一方面，任意 $U\in\mathbb R$ 都是空族上界，因为没有任何成员能违反上界条件。反设空族有上确界 V。由题4，可构造 $L<_{\mathbb R}V$；L 同样是空族上界，V 的最小性要求 $V\subseteq L$，而 $L\subseteq V$ 且二者不等。两个包含将强迫相等，矛盾。因此空族没有 R 中的上确界。

**全体有理下段的边界。** 令

$$
\mathcal G=\{A\in\mathbb R:\exists r\in\mathbb Q,\ A=i(r)\}.
$$

任意 $q\in\mathbb Q$ 满足 $q<q+1$，所以 $q\in i(q+1)$，且 $i(q+1)\in\mathcal G$，从而 $q\in\bigcup\mathcal G$。反向每个分割都是 Q 的子集，所以并集也包含于 Q。两方向合起来得 $\bigcup\mathcal G=\mathbb Q$，不是分割。

若 U 是这个族的分割上界，由 U 的真子集条件取 $b\notin U$。但 $i(b+1)\in\mathcal G$ 且 $b\in i(b+1)$，上界条件又给 $i(b+1)\subseteq U$，推出 $b\in U$，矛盾。因此该族没有分割上界，更无分割上确界。

**集合背景与见证。** 全体分割由公开采用的 $\mathcal P(\mathbb Q)$ 按条件取子集形成；两族 $\mathcal F_S,\mathcal G$ 又从已知 R 按条件形成；并集从 Q 按存在条件形成。非空证明只取一个族成员及其中一点，其他步骤对一个给定 q 取其成员关系提供的见证。没有同时给每个分割选择一个元素的函数，因此不需选择公理。

本书得到的是非空、有上界分割族的最小上界性质。空族和无界族的反例说明不能把范围扩大成所有分割族。整个 Q 已被定义的真子集条件排除，不能把它称为一个现成的最大分割；也未定义额外的无穷大对象来给这些失败情形赋值。
