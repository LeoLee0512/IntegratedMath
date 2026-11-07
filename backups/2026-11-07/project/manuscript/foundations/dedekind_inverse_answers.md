## B2.29 分割的非零倒数与唯一性：完整解答 {#cutinv-answers}

以下大写 $A,X,U$ 等表示分割，小写 $a_0,u,v,q,r$ 等表示有理数。候选 $I(A)$ 只对正分割定义；全倒数函数 $\operatorname{Inv}$ 只接受非零分割。有理数的 $1/r$ 已有定义，但必须先核 $r\ne0$，不能把它当作本组题目尚在构造的分割运算。

### 题1完整解答：由正外点定义倒数候选 {#cutinv-a01}

[返回题目](#cutinv-q01)

固定 $A>_{\mathbb R}0_{\mathbb R}$。由NP1的正分割判据，存在正有理成员 $a_0\in A$；NP1的外点结论又给正有理数 $r_0\notin A$。这两种见证作用不同，前者在分割内，后者在分割外。

候选的完整条件是
$$
I(A)=\{q\in\mathbb Q:\exists r\in\mathbb Q,\
r>0,\ r\notin A,\ q<1/r\}.
$$
要求 $r>0$ 同时保证有理倒数合法及其为正；$r\notin A$ 是外点资格；最后一个比较必须严格。

任取有理数 $q\le0$。因为 $r_0>0$，已有有理数规律给 $1/r_0>0$，所以
$$
q\le0<1/r_0.
$$
因此这个固定的正外点 $r_0$ 就见证 $q\in I(A)$。特别地，$0\in I(A)$，也有全部负有理数属于候选。

这只证明了一个包含及非空性。要称为分割，还须排除候选为整个 $\mathbb Q$，证明下闭和无最大元。这些不能从“含有全部非正有理数”直接取得。它也没有证明候选不含正数，因而不能据此断言 $I(A)=\{q\in\mathbb Q:q\le0\}$。事实上，若完成分割条件，$0$ 是内部成员又无最大元，会迫使候选还有某个大于零的内部成员。

### 题2完整解答：倒数候选的四个分割条件 {#cutinv-a02}

[返回题目](#cutinv-q02)

设 $A$ 正，取正内点 $a_0\in A$、正外点 $r_0\notin A$。

**非空。** $1/r_0>0$，所以正外点 $r_0$ 见证 $0\in I(A)$。

**真子集。** 对每个候选见证 $r>0$、$r\notin A$，内外分离给 $a_0<r$。因为 $a_0r>0$，同除该正有理数，得到
$$
\frac{a_0}{a_0r}<\frac r{a_0r}.
$$
由有理结合、逆元与消去，左侧为 $1/r$、右侧为 $1/a_0$，所以
$$
1/r<1/a_0.
$$
若 $1/a_0$ 属于 $I(A)$，其成员条件会给某个正外点 $r$ 使 $1/a_0<1/r$，与上述不等式矛盾。因此 $1/a_0$ 是候选的有理外点，候选不等于 $\mathbb Q$。

**下闭。** 若 $q\in I(A)$，有正外点 $r$ 满足 $q<1/r$。对任何有理数 $p<q$，传递性给 $p<1/r$，所以同一外点见证 $p\in I(A)$。

**无最大元。** 给定 $q\in I(A)$ 及其正外点见证 $r$，定义
$$
q'=(q+1/r)/2.
$$
二是非零有理数，中点结论给 $q<q'<1/r$。所以原来的 $r$ 仍见证 $q'\in I(A)$，并且 $q'$ 严格超过 $q$。

四条件全部成立，候选才取得分割资格。又已证 $0\in I(A)$，对这个分割应用NP1，得到 $I(A)>_{\mathbb R}0_{\mathbb R}$。这里不在闭合之前把NP1直接应用于尚未检查的子集。

因此规则 $I$ 的输入集合是 $\{A\in\mathbb R:A>_{\mathbb R}0_{\mathbb R}\}$，目标也是这个正分割集合。每个输入由明确成员条件唯一确定一个有理子集，四条件和正性确保输出属于目标，所以确实定义函数。每次证明只选给定分割的见证，不需要一个为全部分割同时选点的规则。

### 题3完整解答：先证明乘积不超过一分割 {#cutinv-a03}

[返回题目](#cutinv-q03)

题2已经证明 $I(A)$ 正，且原 $A$ 正，所以 $P(A,I(A))$ 的输入合法。任取有理成员 $q\in P(A,I(A))$。

若 $q<0$，则 $q<0<1$，故 $q\in i(1)$。

若 $q\ge0$，乘积定义的负支不成立，所以存在正有理数 $a,b$ 满足
$$
a\in A,\qquad b\in I(A),\qquad q<ab.
$$
由 $b\in I(A)$，取有理见证 $r>0$、$r\notin A$，且 $b<1/r$。内外分离给 $a<r$。除数 $r$ 正，所以 $a/r<1$；又 $a>0$，将 $b<1/r$ 同乘 $a$，得 $ab<a/r$。合并为
$$
q<ab<a/r<1.
$$
每次比较都使用已证明的有理正乘或正除法，没有在分割上作除法。因此 $q\in i(1)$。

两个符号分支覆盖全部乘积成员，得到
$$
P(A,I(A))\subseteq i(1).
$$
这还不是逆元等式：右侧可能有尚未被证明属于左侧的成员。还必须对任意有理数 $q<1$ 构造左侧成员见证，才能得到反向包含和集合相等。题4完成这一部分。

### 题4完整解答：反向包含的严格间距 {#cutinv-a04}

[返回题目](#cutinv-q04)

给定 $0\le q<1$，取正有理内点 $a_0\in A$。因为 $1-q>0$，定义
$$
\varepsilon=a_0(1-q)>0.
$$
DA1应用于分割 $A$ 和这个正有理数，给出
$$
u\in A,\qquad v\notin A,\qquad 0<v-u<\varepsilon.
$$
DA1的结论没有包含 $u\ge a_0$，本题也不需要它。

由 $a_0\in A$ 与 $v\notin A$，内外分离直接给 $v>a_0>0$。由于 $1-q>0$，同乘这个正有理数得
$$
a_0(1-q)<v(1-q).
$$
连同严格间距，得到
$$
v-u<a_0(1-q)<v(1-q)=v-qv.
$$
所以 $v-u<v-qv$。两边同减 $v$，得到 $-u<-qv$；取反反序给
$$
u>qv.
$$
因为 $q\ge0$、$v>0$，有 $qv\ge0$，从而 $u>0$。如果 $q=0$，这一结论仍为严格的 $u>0$；不能把原来的严格跨界间距降成不足以产生严格见证的形式。

现在 $u,v$ 均正，因此 $uv>0$。在 $u>qv$ 两边同除以 $uv$，化简得
$$
1/v>q/u.
$$
同时 $q/u\ge0$。令
$$
b=\frac{q/u+1/v}{2}.
$$
中点性质给
$$
0\le q/u<b<1/v.
$$
所以 $b>0$。因为 $v>0$ 且 $v\notin A$，这个外点以及 $b<1/v$ 正好见证 $b\in I(A)$。将 $q/u<b$ 同乘正数 $u$，得 $q<ub$。于是正成员 $u\in A$、$b\in I(A)$ 与该严格比较共同给
$$
q\in P(A,I(A)).
$$

如果最初给定的 $q<1$ 是负数，则直接属于乘积定义的负分支，不需要上面的中点构造。所以任意 $q<1$ 都属于乘积，得到
$$
i(1)\subseteq P(A,I(A)).
$$
取正内点的作用是给一个正尺度 $a_0$ 并通过内外分离控制 $v$；正性 $u>0$ 是后来从 $\varepsilon$ 的具体选择推得的。整个证明未假定网格返回的内点超过预先选定的 $a_0$。

### 题5完整解答：双侧逆元与零成员的具体检查 {#cutinv-a05}

[返回题目](#cutinv-q05)

题3给 $P(A,I(A))\subseteq i(1)$，题4给相反包含，因此由集合外延性，
$$
P(A,I(A))=i(1)=1_{\mathbb R}.
$$
非负乘法交换律使
$$
P(I(A),A)=P(A,I(A))=1_{\mathbb R}.
$$
题2保证 $A$ 与 $I(A)$ 都为正分割，因而全乘法定义的非负支适用：
$$
A\otimes I(A)=P(A,I(A)),\qquad
I(A)\otimes A=P(I(A),A).
$$
所以两侧全乘法逆元式也成立。不能对一个未经核非负的输入直接把 $P$ 与 $\otimes$ 混写。

具体取 $A=i(2)$、$q=0$、$a_0=1$。$1>0$ 且 $1<2$，所以 $a_0$ 是正内点。此时
$$
\varepsilon=a_0(1-q)=1.
$$
所给 $u=3/2$ 满足 $0<u<2$，所以 $u\in A$；$v=2$ 等于严格下段的端点，不属于 $A$。两者间距为
$$
v-u=2-\frac32=\frac12,
\qquad 0<\frac12<1=\varepsilon.
$$
并且 $v>a_0>0$，$u>0=qv$。中点公式给
$$
b=\frac{q/u+1/v}{2}
=\frac{0+1/2}{2}=\frac14.
$$
有 $b>0$、$b<1/v=1/2$，所以正外点 $v$ 见证 $b\in I(A)$。又有
$$
ub=\frac32\cdot\frac14=\frac38>0=q.
$$
故 $u,b$ 确为有理零进入乘积的正见证。

这组数值只检查了一个分割和一个有理成员。逆元等式要求每个正分割和每个 $q<1$ 的完整反向包含，并且还有题3的正向包含；这些全称证明不能由此有限算例替代。

### 题6完整解答：负分割的倒数必须先定义出来 {#cutinv-a06}

[返回题目](#cutinv-q06)

定义非零子集 $\mathbb R^\times=\{A\in\mathbb R:A\ne0_{\mathbb R}\}$，并规定
$$
\operatorname{Inv}(A)=
\begin{cases}
I(A),&A>_{\mathbb R}0_{\mathbb R},\\
N(I(N(A))),&A<_{\mathbb R}0_{\mathbb R}.
\end{cases}
$$
全序使每个非零输入恰属其中一支。

正输入的 $I(A)$ 由题2为正，所以它是非零输出，且与输入同号。负输入先由取反反序得到 $N(A)>_{\mathbb R}0_{\mathbb R}$，于是 $I(N(A))$ 有定义且为正；再取 $N$ 得负分割，所以输出仍非零并与输入同号。各支使用已有函数，因此逐输入唯一输出，定义了
$$
\operatorname{Inv}:\mathbb R^\times\to\mathbb R^\times.
$$

正输入的两侧逆元式由题5给出。对负输入，令 $U=N(A)$。则 $U$ 正，双重取反给 $A=N(U)$，定义又给 $\operatorname{Inv}(A)=N(I(U))$。所以
$$
\begin{aligned}
A\otimes\operatorname{Inv}(A)
&=N(U)\otimes N(I(U))\\
&=U\otimes I(U)\\
&=1_{\mathbb R}.
\end{aligned}
$$
第二行使用前一批已从符号定义证明的双取反乘积公式，第三行对正 $U$ 使用题5。交换律再给
$$
\operatorname{Inv}(A)\otimes A=1_{\mathbb R}.
$$
这份证明没有对负分割作除法。先定义其倒数为一个已经闭合的负分割，再验证两侧乘积为一，存在性才得到落实。

### 题7完整解答：唯一性不是存在性的替代 {#cutinv-a07}

[返回题目](#cutinv-q07)

设 $A\ne0_{\mathbb R}$。题6已经实际构造 $\operatorname{Inv}(A)$，并证明 $\operatorname{Inv}(A)\otimes A=1_{\mathbb R}$。若另有分割 $X$ 满足 $A\otimes X=1_{\mathbb R}$，则
$$
\begin{aligned}
X
&=1_{\mathbb R}\otimes X\\
&=(\operatorname{Inv}(A)\otimes A)\otimes X\\
&=\operatorname{Inv}(A)\otimes(A\otimes X)\\
&=\operatorname{Inv}(A)\otimes1_{\mathbb R}\\
&=\operatorname{Inv}(A).
\end{aligned}
$$
第一、五步使用单位；第二步使用已构造的倒数等式；第三步使用已证全乘法结合；第四步代入对 $X$ 的假设。因此逆元唯一。并未要求先知道 $X$ 非零；如果它是零，原等式就会与乘零及零一不同矛盾。

对零分割，任取 $X\in\mathbb R$，都有 $0_{\mathbb R}\otimes X=0_{\mathbb R}$。嵌入保序已给 $0_{\mathbb R}<_{\mathbb R}1_{\mathbb R}$，所以乘积不等于一。故零没有乘法逆元，$\operatorname{Inv}$ 不在零处定义。

唯一性计算的第二行已经用到了实际存在的 $\operatorname{Inv}(A)$。若此前没有构造这个对象，仅写“若有两个逆元则相等”，只能排除多个候选，不能保证至少一个。已有非零消去也只保证方程 $A\otimes X=1_{\mathbb R}$ 至多一个解；题1—6提供的正候选、严格反向包含及负支才解决存在性。

### 题8完整解答：有理相容、双倒数与取反 {#cutinv-a08}

[返回题目](#cutinv-q08)

设 $r\in\mathbb Q$ 且 $r\ne0$。如果 $i(r)=0_{\mathbb R}=i(0)$，嵌入相等反射会给 $r=0$，矛盾。因此 $\operatorname{Inv}(i(r))$ 有定义。有理倒数满足 $r(1/r)=1$；全有理乘法相容给
$$
i(r)\otimes i(1/r)=i(r(1/r))=i(1)=1_{\mathbb R}.
$$
所以 $i(1/r)$ 是 $i(r)$ 的一个逆元。题7的唯一性给
$$
\operatorname{Inv}(i(r))=i(1/r).
$$
无论 $r$ 正或负，这个证明都适用。右侧有理倒数也非零，否则有理乘回不可能等于一。

一分割非零，且单位律给 $1_{\mathbb R}\otimes1_{\mathbb R}=1_{\mathbb R}$，因此唯一性给
$$
\operatorname{Inv}(1_{\mathbb R})=1_{\mathbb R}.
$$

对任意 $A\in\mathbb R^\times$，题6保证 $\operatorname{Inv}(A)\in\mathbb R^\times$，所以第二次调用倒数合法。又有 $\operatorname{Inv}(A)\otimes A=1_{\mathbb R}$，说明 $A$ 是 $\operatorname{Inv}(A)$ 的一个逆元。唯一性遂给
$$
\operatorname{Inv}(\operatorname{Inv}(A))=A.
$$

如果 $N(A)=0_{\mathbb R}$，对等式取 $N$，用双重取反与 $N(0_{\mathbb R})=0_{\mathbb R}$ 会得 $A=0_{\mathbb R}$，与条件矛盾。所以 $N(A)$ 非零，$\operatorname{Inv}(N(A))$ 有定义。已有双取反乘积式给
$$
N(A)\otimes N(\operatorname{Inv}(A))
=A\otimes\operatorname{Inv}(A)=1_{\mathbb R}.
$$
由 $N(A)$ 的逆元唯一性，
$$
\operatorname{Inv}(N(A))=N(\operatorname{Inv}(A)).
$$
这里还由 $\operatorname{Inv}(A)$ 非零及双反知道其相反数非零，但验证候选的逆元等式时并不需要预先把它作为倒数函数输入。

具体计算，
$$
1/(-3/4)=-4/3,\qquad 1/(2/5)=5/2,
$$
因此
$$
\operatorname{Inv}(i(-3/4))=i(-4/3),\qquad
\operatorname{Inv}(i(2/5))=i(5/2).
$$
两边是分割对象；计算的分数属于已有有理数系。零输入没有公式，因为题7已证明零没有乘法逆元，而且函数的定义域已明确排除它。不得把在非零域上成立的公式当作给 $\operatorname{Inv}(0_{\mathbb R})$ 赋值的规则。
