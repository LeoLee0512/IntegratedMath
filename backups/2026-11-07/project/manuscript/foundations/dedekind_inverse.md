## 基础单元 B2.29 分割的非零倒数与唯一性 {#cutinv-unit}

**学习目标与位置。** 已有的全乘法满足环规律，非零因子可以消去，但这只保证乘法方程的解至多一个。现在要实际构造每个非零分割的乘法逆元。我们先用正分割的有理外点定义候选，再逐成员证明乘积为一；随后处理负输入、唯一性、零无逆及有理倒数相容。主归属第526章97F50的实数基础教学部分；06A05、06F25交叉。除法的定义及有序域结构的汇总留到下一单元。

**精确先修。** 使用[分割四条件](#cut-definition)、[包含序与有理嵌入](#cut-order-embedding)、[内外严格分离](#cutadd-separation)、[有理跨界间隔DA1](#cutadd-grid)、[正内点与正外点NP1](#cutprod-positive-witnesses)、[非负乘积定义与闭合](#cutprod-definition)、[非负交换](#cutprod-basic-laws)。全乘法使用[四支定义](#cutsigned-definition)、[符号、零、单位及交换](#cutsigned-signs)、[结合律](#cutsigned-associative)、[全有理相容](#cutsigned-rational-zero)。相反数使用[双重取反](#cutgroup-inverses)、[取反反序](#cutgroup-negation-subtraction)及[有理相反数相容](#cutadd-rational)。有理见证使用[有理除法](#rdiv-division)、[有理乘法规律](#rmul-laws)、[正乘比较](#rord-multiplication)、[正倒数的符号](#rord-reciprocal)、[正除法比较](#rord-division)及[有理中点](#qgap-density-archimedean)。另使用[条件子集](#fun-sets)、[函数定义](#fun-definition)、[有理平移比较](#rord-translation)及[有理取反反序](#rord-negation)。

**对象与记号。** $A,B,X$ 等表示分割，小写 $a_0,u,v,q,r$ 等表示有理数。零、一分割仍为 $0_{\mathbb R}=i(0)$、$1_{\mathbb R}=i(1)$。从已有集合中取非零子集
$$
\mathbb R^\times=\{A\in\mathbb R:A\ne0_{\mathbb R}\}.
$$
上标 $\times$ 在这里仅是非零子集的记号，不是已经证明了新的群结构。正输入的候选记为 $I(A)$；后面定义全部非零输入的倒数函数 $\operatorname{Inv}$。式子 $1/r$ 始终是已定义的有理除法，不能与尚待构造的分割倒数混同。

### 1. 正分割的外点给出倒数候选 {#cutinv-positive-definition}

设 $A>_{\mathbb R}0_{\mathbb R}$。从 $\mathbb Q$ 按条件形成
$$
I(A)=\{q\in\mathbb Q:\exists r\in\mathbb Q,\
r>0,\ r\notin A,\ q<1/r\}.
$$
见证 $r$ 是严格正的有理外点，所以每次 $1/r$ 都是合法的有理数。先给这个子集命名，不预先假定它是分割，更不预先假定它与 $A$ 相乘为一。

**命题 IR1。** 对每个正分割 $A$，候选 $I(A)$ 是正分割。因此这条规则定义了正分割集合到自身的函数。

**先取得两种有理见证。** 因 $A$ 正，NP1给正内点 $a_0\in A$；同一命题还给正外点 $r_0\notin A$。这两个数都在 $\mathbb Q$ 中，且严格为正。

**非空。** 正有理数的倒数为正，所以 $0<1/r_0$。外点 $r_0$ 因而见证
$$
0\in I(A).
$$
这已给非空，但要使用分割的正性判据，仍须先检查另外三个分割条件。

**真子集。** 我们证明有理数 $1/a_0$ 不在候选中。任给正外点 $r\notin A$，内外分离给
$$
0<a_0<r.
$$
有理积 $a_0r$ 正，故可在 $a_0<r$ 两边同除以它，得到
$$
\frac{a_0}{a_0r}<\frac r{a_0r},
\qquad\text{即}\qquad
\frac1r<\frac1{a_0}.
$$
【依据：正除法保持严格比较；两次化简只约去已核非零的有理因子。】

若 $1/a_0\in I(A)$，定义又会给某个这样的正外点 $r$ 满足 $1/a_0<1/r$，与刚得的反向严格比较矛盾。因此 $1/a_0\notin I(A)$，候选不是整个 $\mathbb Q$。

**向下封闭。** 若 $q\in I(A)$，取正外点 $r\notin A$ 使 $q<1/r$。对任意有理数 $p<q$，有 $p<q<1/r$，同一外点 $r$ 见证 $p\in I(A)$。

**无最大元。** 对同一个 $q$ 和见证 $r$，取有理中点
$$
q'=\frac{q+1/r}{2}.
$$
因为 $q<1/r$，有 $q<q'<1/r$。原正外点 $r$ 仍见证 $q'\in I(A)$，所以每个候选成员都有更大的内部成员。

四项条件成立，$I(A)\in\mathbb R$。又已有 $0\in I(A)$，NP1的正性判据遂给
$$
I(A)>_{\mathbb R}0_{\mathbb R}.
$$
每个正输入按同一个明确成员条件唯一确定子集，闭合和正性保证目标正确，故函数结论成立。IR1证毕。

还可明确说：任意有理数 $q\le0$ 都属于 $I(A)$，因为选定的正外点 $r_0$ 给 $q\le0<1/r_0$。这不表示 $I(A)$ 等于非正有理数的集合；它已经是正分割，且按无最大元性质还有正成员。这里也没有为所有分割同时选择外点的要求，每个存在论证只处理给定输入。

### 2. 乘积为一需要两个包含方向 {#cutinv-positive-inverse}

**命题 IR2。** 对每个 $A>_{\mathbb R}0_{\mathbb R}$，
$$
P(A,I(A))=1_{\mathbb R}=P(I(A),A).
$$
因此在全乘法中也有
$$
A\otimes I(A)=1_{\mathbb R}=I(A)\otimes A.
$$

IR1已经保证两个输入正，所有非负乘积都有定义。以下证明第一个等式，其余等式再由交换和非负输入一致性取得。

**第一个包含：乘积中的成员都小于有理一。** 任取 $q\in P(A,I(A))$。若 $q<0$，立即有 $q<1$。若 $q\ge0$，乘积定义给正有理成员
$$
a\in A,\qquad b\in I(A),\qquad q<ab.
$$
展开第二个成员，可取正有理外点 $r\notin A$ 满足 $b<1/r$。内外分离给 $a<r$，而 $r>0$，故 $a/r<1$。将 $b<1/r$ 同乘正数 $a$，得到
$$
q<ab<a/r<1.
$$
所以两种分支都给 $q\in i(1)=1_{\mathbb R}$，证明
$$
P(A,I(A))\subseteq1_{\mathbb R}.
$$

**反向先处理负成员。** 给定任意有理数 $q<1$。若 $q<0$，它直接属于 $P(A,I(A))$ 的负分支，不需要另造正见证。以下只须处理
$$
0\le q<1.
$$

**选出适合这一成员的严格间距。** 取正内点 $a_0\in A$，定义正有理数
$$
\varepsilon=a_0(1-q).
$$
由于 $a_0>0$ 且 $1-q>0$，确有 $\varepsilon>0$。对分割 $A$ 应用DA1，取得有理数 $u,v$ 满足
$$
u\in A,\qquad v\notin A,\qquad 0<v-u<\varepsilon.
$$
此时不能直接假定 $u$ 正，也不能要求DA1额外给出 $u\ge a_0$；我们将由当前不等式推出真正需要的正性。

**外点位置使内点足够大。** 因 $a_0\in A$ 而 $v\notin A$，内外分离给
$$
v>a_0>0.
$$
乘以正有理数 $1-q$，得 $a_0(1-q)<v(1-q)$。因此
$$
v-u<a_0(1-q)<v(1-q)=v-qv.
$$
对最左与最右的比较同减 $v$，得到 $-u<-qv$；再用有理取反反序，得到
$$
u>qv.
$$
又因 $q\ge0$、$v>0$，有 $qv\ge0$。所以
$$
u>qv\ge0.
$$
特别地，$u>0$。当 $q=0$ 时，这条链仍给严格的 $u>0$；零这个成员没有被略去。

**再把倒数成员放在两个有理数之间。** 现在 $u,v$ 都已正，可以在 $u>qv$ 两边同除以正数 $uv$，化简得
$$
q/u<1/v.
$$
同时 $q/u\ge0$。取中点
$$
b=\frac{q/u+1/v}{2}.
$$
则
$$
0\le q/u<b<1/v.
$$
所以 $b>0$；正外点 $v\notin A$ 和 $b<1/v$ 见证 $b\in I(A)$。再把 $q/u<b$ 同乘正数 $u$，得到 $q<ub$。因此正有理内点
$$
u\in A,\qquad b\in I(A),\qquad q<ub
$$
共同见证 $q\in P(A,I(A))$。

负 $q$ 和非负 $q<1$ 都已处理，故
$$
1_{\mathbb R}\subseteq P(A,I(A)).
$$
与第一个包含合并，得到 $P(A,I(A))=1_{\mathbb R}$。非负乘法交换给 $P(I(A),A)=1_{\mathbb R}$；因两个输入都正，全乘法定义第一支把它们分别改写为 $A\otimes I(A)$、$I(A)\otimes A$。IR2证毕。

证明中没有对分割除法，也没有取极限或调用上确界。DA1只提供有理跨界间隔；关键正性来自正内点与外点的分离，以及特定的 $\varepsilon$ 选择。

**检查有理零这一边界。** 取 $A=i(2)$、$q=0$、$a_0=1$，则 $\varepsilon=1$。可以取
$$
u=\frac32\in i(2),\qquad v=2\notin i(2),\qquad
0<v-u=\frac12<1.
$$
这里 $v>a_0>0$，且 $u>0=qv$。按公式，
$$
b=\frac{0/u+1/v}{2}=\frac14.
$$
外点 $v=2$ 见证 $b<1/v$，而 $ub=3/8>0=q$，所以有理零确在乘积中。这个例子检查一般构造的一次代入，不能替代任意分割和任意 $q<1$ 的两个包含证明。

### 3. 全部非零分割的倒数及其唯一性 {#cutinv-signed-unique}

定义
$$
\operatorname{Inv}(A)=
\begin{cases}
I(A),&A>_{\mathbb R}0_{\mathbb R},\\
N(I(N(A))),&A<_{\mathbb R}0_{\mathbb R},
\end{cases}
\qquad A\in\mathbb R^\times.
$$

**命题 IR3。** 该规则定义函数
$$
\operatorname{Inv}:\mathbb R^\times\longrightarrow\mathbb R^\times,
$$
且 $\operatorname{Inv}(A)$ 与 $A$ 同号。对每个非零分割 $A$，
$$
A\otimes\operatorname{Inv}(A)
=1_{\mathbb R}
=\operatorname{Inv}(A)\otimes A.
$$
若分割 $X$ 满足 $A\otimes X=1_{\mathbb R}$，则 $X=\operatorname{Inv}(A)$。零分割没有乘法逆元。

**定义域和输出。** 非零分割按全序恰为正或负，定义的两支互斥且穷尽。如果 $A$ 正，IR1使 $I(A)$ 正，所以输出非零且同号。如果 $A$ 负，取反反序给 $N(A)$ 正，故 $I(N(A))$ 合法且为正；再取 $N$ 得负分割，仍非零且与 $A$ 同号。每支由已定义函数给唯一输出，所以确有上述函数。

**逆元等式。** 正输入的两侧等式正是IR2。负输入令 $U=N(A)$，则 $U$ 正且 $A=N(U)$。由定义 $\operatorname{Inv}(A)=N(I(U))$，已经证明的双取反乘积规则给
$$
\begin{aligned}
A\otimes\operatorname{Inv}(A)
&=N(U)\otimes N(I(U))\\
&=U\otimes I(U)\\
&=1_{\mathbb R}.
\end{aligned}
$$
最后一步对正 $U$ 用IR2。全乘法交换再给另一侧为一。这里没有通过“除以负数”来证明负分割逆元，只有已定义的取反和乘法。

**唯一性。** 固定非零 $A$，设 $A\otimes X=1_{\mathbb R}$，其中 $X$ 是任意分割。由单位、刚证逆元、结合律，
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
所以任何候选都等于已经构造的倒数。没有先假定 $X$ 非零；事实上它若为零，原乘积为零就不可能等于一。存在性来自IR1、IR2及负支构造，不能由这一唯一性计算单独取得。

**零无逆。** 对任意分割 $X$，已有
$$
0_{\mathbb R}\otimes X=0_{\mathbb R}\ne1_{\mathbb R}.
$$
不等号来自 $i(0)<_{\mathbb R}i(1)$。因此不存在满足零分割逆元等式的 $X$。函数 $\operatorname{Inv}$ 不在零处定义；本书不会为了填满一个函数表而把零的倒数设为某个分割。IR3证毕。

现在可将 $\operatorname{Inv}(A)$ 简记为 $A^{-1}$，但只在 $A\ne0_{\mathbb R}$ 时使用。本单元后续保留 $\operatorname{Inv}$，提醒其定义域条件。

### 4. 与有理倒数相容及两次取倒数 {#cutinv-rational-identities}

**命题 IR4。** 对任意非零有理数 $r$，
$$
\operatorname{Inv}(i(r))=i(1/r).
$$
并有
$$
\operatorname{Inv}(1_{\mathbb R})=1_{\mathbb R},
$$
对任意 $A\in\mathbb R^\times$，
$$
\operatorname{Inv}(\operatorname{Inv}(A))=A,\qquad
\operatorname{Inv}(N(A))=N(\operatorname{Inv}(A)).
$$

**有理嵌入相容。** 若 $r\ne0$，嵌入的相等反射给 $i(r)\ne i(0)=0_{\mathbb R}$，所以左侧倒数有定义。有理倒数已给 $r(1/r)=1$；其倒数本身也非零，否则这个乘积为零而非一。由全有理乘法相容，
$$
i(r)\otimes i(1/r)=i(r(1/r))=i(1)=1_{\mathbb R}.
$$
所以 $i(1/r)$ 是 $i(r)$ 的一个乘法逆元。IR3的唯一性迫使它等于 $\operatorname{Inv}(i(r))$。正、负有理数都被这一论证覆盖；有理零不满足条件。

**一的倒数。** 因 $1_{\mathbb R}\ne0_{\mathbb R}$，它的倒数有定义；单位律给 $1_{\mathbb R}\otimes1_{\mathbb R}=1_{\mathbb R}$。唯一性给 $\operatorname{Inv}(1_{\mathbb R})=1_{\mathbb R}$。

**两次取倒数。** IR3不仅给 $\operatorname{Inv}(A)$ 一个输出，还保证它非零。因此第二次调用合法。已有
$$
\operatorname{Inv}(A)\otimes A=1_{\mathbb R},
$$
说明 $A$ 是分割 $\operatorname{Inv}(A)$ 的一个逆元。对这个非零分割使用唯一性，得 $\operatorname{Inv}(\operatorname{Inv}(A))=A$。

**取反与倒数。** 若 $N(A)=0_{\mathbb R}$，对等式取 $N$ 并用双重取反会得 $A=0_{\mathbb R}$，矛盾。因此 $N(A)$ 非零，其倒数有定义。全乘法的双取反规律及IR3给
$$
N(A)\otimes N(\operatorname{Inv}(A))
=A\otimes\operatorname{Inv}(A)=1_{\mathbb R}.
$$
这把 $N(\operatorname{Inv}(A))$ 验为 $N(A)$ 的一个逆元，再由唯一性得到所求等式。IR4证毕。

例如，
$$
\operatorname{Inv}(i(-3/4))=i(-4/3),\qquad
\operatorname{Inv}(i(2/5))=i(5/2).
$$
等号两边都是分割；右侧括号里的分数是先在 $\mathbb Q$ 中计算的倒数，再经嵌入形成下段。一般相容证明依赖逆元唯一性，不能只由这两个数值例子判断。

### 5. 课后题 {#cutinv-exercises}

#### 题1：由正外点定义倒数候选 {#cutinv-q01}

固定正分割 $A$，取得正有理内点 $a_0$ 和正有理外点 $r_0$，写出 $I(A)$ 的完整成员条件。证明任意有理数 $q\le0$ 都属于 $I(A)$；说明这一步为什么还不足以证明 $I(A)$ 是分割，也不说明它等于非正有理数集合。[完整解答](#cutinv-a01)

#### 题2：倒数候选的四个分割条件 {#cutinv-q02}

逐项证明 $I(A)$ 非空、为真子集、下闭、无最大元。真子集部分须从 $a_0<r$ 实际推出 $1/r<1/a_0$，再排除 $1/a_0$；最后在闭合证明之后，由 $0\in I(A)$ 得到 $I(A)$ 正，并说明函数的输入和目标范围。[完整解答](#cutinv-a02)

#### 题3：先证明乘积不超过一分割 {#cutinv-q03}

证明 $P(A,I(A))\subseteq i(1)$。分别处理负成员与非负成员，展开第二因子的外点见证，写出 $q<ab<a/r<1$ 并标明每次乘除的正性条件。是否已经由这一包含证明逆元等式？[完整解答](#cutinv-a03)

#### 题4：反向包含的严格间距 {#cutinv-q04}

给定有理数 $0\le q<1$，取正内点 $a_0\in A$，令 $\varepsilon=a_0(1-q)$。使用DA1构造 $u,v$，由内外分离推出 $v>a_0$，再逐步推出 $u>qv\ge0$，最后构造正 $b\in I(A)$ 使 $q<ub$。解释 $q=0$ 为何有效、为何不需要 $u\ge a_0$，并补上负 $q$ 得到整个反向包含。[完整解答](#cutinv-a04)

#### 题5：双侧逆元与零成员的具体检查 {#cutinv-q05}

结合题3、4得到正 $A$ 的两侧逆元等式，并说明从 $P$ 转为 $\otimes$ 的条件。再取 $A=i(2)$、$q=0$、$a_0=1$、$u=3/2$、$v=2$，计算 $\varepsilon$ 和 $b$，核验全部成员、正性和严格间距。说明这组具体数值能否代替一般逆元证明。[完整解答](#cutinv-a05)

#### 题6：负分割的倒数必须先定义出来 {#cutinv-q06}

写出 $\operatorname{Inv}$ 在全部非零分割上的两支定义，逐支核输出与输入同号且非零。对负输入令 $U=N(A)$，完整证明两侧逆元等式，明确使用双取反乘积而非尚未定义的分割除法。写出该函数的定义域与目标。[完整解答](#cutinv-a06)

#### 题7：唯一性不是存在性的替代 {#cutinv-q07}

对非零 $A$，从 $A\otimes X=1_{\mathbb R}$ 出发，用完整结合等式证明 $X=\operatorname{Inv}(A)$。再证明零分割没有乘法逆元。说明这份唯一性证明依赖哪一处已经构造的存在见证，以及为什么已有非零消去也不能单独提供一个倒数。[完整解答](#cutinv-a07)

#### 题8：有理相容、双倒数与取反 {#cutinv-q08}

用逆元唯一性证明全部非零有理数的倒数相容，再证明一的倒数、两次取倒数及取反与倒数的公式。每次调用 $\operatorname{Inv}$ 都要核输入非零。计算 $\operatorname{Inv}(i(-3/4))$ 与 $\operatorname{Inv}(i(2/5))$，说明为什么没有对零输入给公式。[完整解答](#cutinv-a08)

**来源与范围说明。** 公开来源的定义条件、零倒数约定差异及本书独立推导边界见[分割倒数与除法来源核验](#dedekind-inverse-sources)。本文实际构造非零分割的逆元，未借尚未建立的分割除法、实数连续性或极限。外部形式化库的全域逆符号约定不改变本书的非零定义域；除法、方程全参数分类及完备有序域接口将在下一单元完成。
