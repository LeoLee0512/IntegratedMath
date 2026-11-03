## B2.27 全部分割的乘法、符号与结合：完整解答 {#cutsigned-answers}

以下 $A,B,C,U,V,W$ 等表示分割，$e,f,g$ 为集合 $\{0,1\}$ 中的符号标签；有理数的类型在各处说明。$P$ 只接受非负分割，$\otimes$ 按四个符号区域定义，$N$ 是已证的加法相反数。所有分配律的全符号结论仍留到下一单元，不用它证明本组答案。

### 题1完整解答：四支是否穷尽，输出是否已有定义 {#cutsigned-a01}

[返回题目](#cutsigned-q01)

对任意 $A,B\in\mathbb R$，规则是
$$
A\otimes B=
\begin{cases}
P(A,B),&A\ge_{\mathbb R}0_{\mathbb R},\ B\ge_{\mathbb R}0_{\mathbb R},\\
N(P(N(A),B)),&A<_{\mathbb R}0_{\mathbb R},\ B\ge_{\mathbb R}0_{\mathbb R},\\
N(P(A,N(B))),&A\ge_{\mathbb R}0_{\mathbb R},\ B<_{\mathbb R}0_{\mathbb R},\\
P(N(A),N(B)),&A<_{\mathbb R}0_{\mathbb R},\ B<_{\mathbb R}0_{\mathbb R}.
\end{cases}
$$

全序给每个输入恰好满足“非负”与“负”之一：若它小于零就不能同时不小于零；若它不小于零就排除小于零；两者又穷尽全序的可能。分别对 $A$、$B$ 作这一划分，其组合恰是上列四域。任意两域至少在一个输入的符号要求上相反，所以不相交；任何输入对都落入其中一域。

第一支里 $A,B$ 已非负，NP2保证 $P(A,B)$ 有定义并输出分割。

第二支里 $A<_{\mathbb R}0_{\mathbb R}$，已证取反反序给
$$
0_{\mathbb R}=N(0_{\mathbb R})<_{\mathbb R}N(A).
$$
故 $N(A)$ 正，$B$ 非负，$P(N(A),B)$ 的两个输入均合法，输出也是分割。$N$ 定义于全部分割，所以对这个输出再取 $N$ 有定义。

第三支同样由 $B<_{\mathbb R}0_{\mathbb R}$ 得 $N(B)>_{\mathbb R}0_{\mathbb R}$。$A$ 非负，故 $P(A,N(B))$ 合法，取 $N$ 仍合法。

第四支中两输入都负，反序使 $N(A),N(B)$ 都正，所以它们的 $P$ 有定义并输出分割。

零满足非负条件而不满足负条件。因此没有某个零输入同时触发两个公式的冲突。四域唯一选择一支，各支由已有函数指定唯一分割输出，于是这条规则定义函数 $\mathbb R\times\mathbb R\to\mathbb R$。此结论只检查定义与闭合，不等于已经证明分配律。

### 题2完整解答：把含负输入的乘积展开成有理子集 {#cutsigned-a02}

[返回题目](#cutsigned-q02)

设 $A<_{\mathbb R}0_{\mathbb R}$、$B\ge_{\mathbb R}0_{\mathbb R}$。令 $U=N(A),V=B$，则 $U$ 正、$V$ 非负，$P(U,V)$ 已是非负分割。由负分割的既有定义，
$$
A\otimes B
=\{q\in\mathbb Q:\exists t\in\mathbb Q,\
t\notin P(U,V)\text{ 且 }q<-t\}.
$$
外部见证 $t$ 属于 $\mathbb Q\setminus P(U,V)$，并非要求它属于 $\mathbb Q\setminus U$ 或 $\mathbb Q\setminus V$。成员比较是严格的 $q<-t$，不是 $q\le -t$。其中
$$
P(U,V)=\{x\in\mathbb Q:x<0\text{，或存在正 }u\in U,v\in V
\text{ 使 }x<uv\}.
$$
这确实把输出解释为已有有理集合上的条件子集。由于已证 $P(U,V)$ 为分割，随后取 $N$ 的闭合条件得到满足。

分别证明两个位置的零因子。固定任意 $B$：若 $B\ge_{\mathbb R}0_{\mathbb R}$，第一支给
$$
0_{\mathbb R}\otimes B=P(0_{\mathbb R},B)=0_{\mathbb R}.
$$
若 $B<_{\mathbb R}0_{\mathbb R}$，第三支给
$$
0_{\mathbb R}\otimes B
=N(P(0_{\mathbb R},N(B)))
=N(0_{\mathbb R})=0_{\mathbb R}.
$$
这里 $N(B)$ 正，所以对非负乘积调用零律合法。

固定任意 $A$：若 $A\ge_{\mathbb R}0_{\mathbb R}$，第一支给
$$
A\otimes0_{\mathbb R}=P(A,0_{\mathbb R})=0_{\mathbb R}.
$$
若 $A<_{\mathbb R}0_{\mathbb R}$，第二支给
$$
A\otimes0_{\mathbb R}
=N(P(N(A),0_{\mathbb R}))
=N(0_{\mathbb R})=0_{\mathbb R}.
$$
四个计算只用定义、NP2乘零及 $N(0_{\mathbb R})=0_{\mathbb R}$。没有在证明第二个位置时预用交换律。两个输入同时为零包含在非负的相应分支中。

### 题3完整解答：交换与单位从哪一支得到 {#cutsigned-a03}

[返回题目](#cutsigned-q03)

**两个输入非负。** 若 $A,B\ge_{\mathbb R}0_{\mathbb R}$，定义第一支及NP3给
$$
A\otimes B=P(A,B)=P(B,A)=B\otimes A.
$$
这支已经包括两个输入中至少一个为零、另一个非负的情况。

**第一负、第二非负。** 若 $A<_{\mathbb R}0_{\mathbb R}\le_{\mathbb R}B$，则 $N(A)$ 正。交换前用第二支，交换后用第三支，NP3只作用于非负输入：
$$
A\otimes B=N(P(N(A),B))
=N(P(B,N(A)))=B\otimes A.
$$
如果 $B=0_{\mathbb R}$，这些公式仍合法，双方都由题2等于零。

**第一非负、第二负。** 若 $B<_{\mathbb R}0_{\mathbb R}\le_{\mathbb R}A$，第三支和第二支分别给
$$
A\otimes B=N(P(A,N(B)))
=N(P(N(B),A))=B\otimes A.
$$
中间仍只用NP3的合法非负交换。$A=0_{\mathbb R}$ 也在这支内。

**两个输入负。** 取反后两者都正，第四支给
$$
A\otimes B=P(N(A),N(B))
=P(N(B),N(A))=B\otimes A.
$$
四域已经穷尽所有输入，故交换律成立，零边界也已覆盖。

一分割 $1_{\mathbb R}=i(1)$ 严格为正，因为 $0<1$ 经过嵌入保序给 $0_{\mathbb R}<_{\mathbb R}1_{\mathbb R}$。若 $A\ge_{\mathbb R}0_{\mathbb R}$，第一支和NP3单位给
$$
A\otimes1_{\mathbb R}=P(A,1_{\mathbb R})=A.
$$
若 $A<_{\mathbb R}0_{\mathbb R}$，第二支及正输入 $N(A)$ 的非负单位律给
$$
A\otimes1_{\mathbb R}
=N(P(N(A),1_{\mathbb R}))
=N(N(A))=A.
$$
最后一步是已经证明的加法双重取反，未用分配律。非负支包含零，所以右单位对全部分割成立。再用刚证的交换律，
$$
1_{\mathbb R}\otimes A=A\otimes1_{\mathbb R}=A.
$$
左右单位都得证。

### 题4完整解答：唯一正幅度与取反乘积 {#cutsigned-a04}

[返回题目](#cutsigned-q04)

定义函数
$$
E_0:\mathbb R\to\mathbb R,\ E_0(X)=X,\qquad
E_1:\mathbb R\to\mathbb R,\ E_1(X)=N(X).
$$
恒等规则及已定义的 $N$ 保证这两个函数合法。下标是标签，没有预设幂运算。

设 $A\ne0_{\mathbb R}$。若 $A>_{\mathbb R}0_{\mathbb R}$，取 $e=0,U=A$。若 $A<_{\mathbb R}0_{\mathbb R}$，取 $e=1,U=N(A)$；反序使 $U$ 正，双重取反使 $E_1(U)=A$。全序保证这两种情况覆盖所有非零输入，故表示存在。

对正 $U$，$E_0(U)>_{\mathbb R}0_{\mathbb R}$，而 $E_1(U)=N(U)<_{\mathbb R}0_{\mathbb R}$。所以若 $A$ 正，标签必为零，再由 $A=E_0(U)=U$ 唯一确定幅度；若 $A$ 负，标签必为一，再由 $A=N(U)$ 两边取 $N$，得到 $U=N(A)$。因此标签与正幅度均唯一。无论标签是哪一个，正幅度给出的输出都非零，所以零没有这种表示。

在 $\{0,1\}$ 上定义
$$
0\diamond0=0,\quad 0\diamond1=1,\quad
1\diamond0=1,\quad 1\diamond1=0.
$$
对正 $U,V$，令 $T=P(U,V)$。NP2保证 $T$ 正。四支定义分别给：
$$
E_0(U)\otimes E_0(V)=P(U,V)=T=E_0(T),
$$
$$
E_0(U)\otimes E_1(V)
=N(P(U,N(N(V))))=N(T)=E_1(T),
$$
$$
E_1(U)\otimes E_0(V)
=N(P(N(N(U)),V))=N(T)=E_1(T),
$$
$$
E_1(U)\otimes E_1(V)
=P(N(N(U)),N(N(V)))=T=E_0(T).
$$
因此统一为
$$
E_e(U)\otimes E_f(V)=E_{e\diamond f}(P(U,V)).
$$
正的 $T$ 与负的 $N(T)$ 分别给同号正、异号负的实际结论。

定义标签翻转 $\bar0=1,\bar1=0$。当 $e=0$ 时，$N(E_e(X))=N(X)=E_1(X)$；当 $e=1$ 时，$N(E_e(X))=N(N(X))=X=E_0(X)$。所以对任意分割 $X$，
$$
N(E_e(X))=E_{\bar e}(X).
$$
标签比较的四行是：

| $(e,f)$ | $\bar e\diamond f$ | $\overline{e\diamond f}$ |
| --- | --- | --- |
| $(0,0)$ | $1$ | $1$ |
| $(0,1)$ | $0$ | $0$ |
| $(1,0)$ | $0$ | $0$ |
| $(1,1)$ | $1$ | $1$ |

故两个标签表达式在全部输入上相等。对非零 $A=E_e(U)$、$B=E_f(V)$，逐步有
$$
\begin{aligned}
N(A)\otimes B
&=E_{\bar e}(U)\otimes E_f(V)\\
&=E_{\bar e\diamond f}(P(U,V))\\
&=E_{\overline{e\diamond f}}(P(U,V))\\
&=N(E_{e\diamond f}(P(U,V)))\\
&=N(A\otimes B).
\end{aligned}
$$
这里取反后的输入仍有正幅度 $U$，故可合法使用符号公式。

若 $A=0_{\mathbb R}$，$N(A)=0_{\mathbb R}$，题2使两边均零；若 $B=0_{\mathbb R}$，左边乘零为零，右边为 $N(0_{\mathbb R})=0_{\mathbb R}$。所以该公式对全部输入成立。另由双重取反可知，$N(A)$ 为零当且仅当 $A$ 为零，不存在遗漏的额外零分支。

题3交换律给
$$
A\otimes N(B)=N(B)\otimes A
=N(B\otimes A)=N(A\otimes B).
$$
最后将第一因子取反式应用于 $A,N(B)$，再用第二因子取反式及双重取反：
$$
N(A)\otimes N(B)
=N(A\otimes N(B))
=N(N(A\otimes B))=A\otimes B.
$$
因此全部取反公式成立。证明只依赖四支定义、已证非负正性与加法相反数，没有使用任意符号下的分配律。

### 题5完整解答：零出现在三因子的哪个位置 {#cutsigned-a05}

[返回题目](#cutsigned-q05)

如果 $A=0_{\mathbb R}$，由题2分别算两边：
$$
(A\otimes B)\otimes C
=(0_{\mathbb R}\otimes B)\otimes C
=0_{\mathbb R}\otimes C=0_{\mathbb R},
$$
$$
A\otimes(B\otimes C)
=0_{\mathbb R}\otimes(B\otimes C)=0_{\mathbb R}.
$$

如果 $B=0_{\mathbb R}$，则
$$
(A\otimes B)\otimes C
=(A\otimes0_{\mathbb R})\otimes C
=0_{\mathbb R}\otimes C=0_{\mathbb R},
$$
$$
A\otimes(B\otimes C)
=A\otimes(0_{\mathbb R}\otimes C)
=A\otimes0_{\mathbb R}=0_{\mathbb R}.
$$

如果 $C=0_{\mathbb R}$，则
$$
(A\otimes B)\otimes C
=(A\otimes B)\otimes0_{\mathbb R}=0_{\mathbb R},
$$
$$
A\otimes(B\otimes C)
=A\otimes(B\otimes0_{\mathbb R})
=A\otimes0_{\mathbb R}=0_{\mathbb R}.
$$
这些计算不假定输入的其它项正负，也允许两项、三项同时为零。它们只反复应用零乘公式，未在计算中把三个乘法因子任意改括号。

零在中间的一个例子是 $A=i(-1),B=i(0),C=i(2)$；左边先算 $i(-1)\otimes i(0)=0_{\mathbb R}$，右边先算 $i(0)\otimes i(2)=0_{\mathbb R}$，故两边均零。零在末尾的一个例子是 $A=i(1),B=i(-2),C=i(0)$；左边直接由外层乘零为零，右边的内积先为零，外层也为零。

本题尚未处理三个输入均非零的情形。完整结合律还需要题6的正幅度及标签比较，不能仅从零例子推断一般结论。

### 题6完整解答：八行标签表与一般结合律 {#cutsigned-a06}

[返回题目](#cutsigned-q06)

设 $A,B,C$ 都非零。题4给唯一表示
$$
A=E_e(U),\qquad B=E_f(V),\qquad C=E_g(W),
$$
其中三个幅度 $U,V,W$ 均正，三个标签均属于 $\{0,1\}$。

由NP2，$P(U,V)>_{\mathbb R}0_{\mathbb R}$、$P(V,W)>_{\mathbb R}0_{\mathbb R}$。题4符号公式给
$$
A\otimes B=E_{e\diamond f}(P(U,V)),\qquad
B\otimes C=E_{f\diamond g}(P(V,W)).
$$
这两个中间输出非零，而且所显示的幅度为正。因此能够再次把它们作为正幅度表示送入符号公式，得到
$$
(A\otimes B)\otimes C
=E_{(e\diamond f)\diamond g}(P(P(U,V),W)),
$$
$$
A\otimes(B\otimes C)
=E_{e\diamond(f\diamond g)}(P(U,P(V,W))).
$$

逐行使用题4的四个标签定义，结果如下：

| $e$ | $f$ | $g$ | $e\diamond f$ | $f\diamond g$ | $(e\diamond f)\diamond g$ | $e\diamond(f\diamond g)$ |
| --- | --- | --- | --- | --- | --- | --- |
| $0$ | $0$ | $0$ | $0$ | $0$ | $0$ | $0$ |
| $0$ | $0$ | $1$ | $0$ | $1$ | $1$ | $1$ |
| $0$ | $1$ | $0$ | $1$ | $1$ | $1$ | $1$ |
| $0$ | $1$ | $1$ | $1$ | $0$ | $0$ | $0$ |
| $1$ | $0$ | $0$ | $1$ | $0$ | $1$ | $1$ |
| $1$ | $0$ | $1$ | $1$ | $1$ | $0$ | $0$ |
| $1$ | $1$ | $0$ | $0$ | $1$ | $0$ | $0$ |
| $1$ | $1$ | $1$ | $0$ | $0$ | $1$ | $1$ |

例如第六行先算 $1\diamond0=1$，再算 $1\diamond1=0$；另一括号先算 $0\diamond1=1$，再算 $1\diamond1=0$。其它行的中间两列与最后两列也直接由四个定义值给出。最后两列全部一致，所以
$$
(e\diamond f)\diamond g=e\diamond(f\diamond g)
$$
对全部标签成立。

另一方面，$U,V,W$ 都非负，已经证明的NL2给
$$
P(P(U,V),W)=P(U,P(V,W)).
$$
两个括号结果的标签相同、幅度相同；$E_0,E_1$ 是函数，故相同标签的函数作用于相等幅度给相等结果。因此
$$
(A\otimes B)\otimes C=A\otimes(B\otimes C)
$$
对非零输入成立。再结合题5的全部零位置，就得到任意分割上的结合律。

有限表列举的是三个二值标签的所有八种可能，并没有只选八组三个分割。任意非零分割的幅度仍是任意正分割，它们的结合性由NL2的全称证明承担。因此这里没有用有限数值样本替代一般分割的证明。

### 题7完整解答：全有理相容需要哪些符号区域 {#cutsigned-a07}

[返回题目](#cutsigned-q07)

固定任意有理数 $r,s$。若 $r=0$，题2给
$$
i(r)\otimes i(s)=0_{\mathbb R}=i(0)=i(rs).
$$
若 $s=0$，第二位置零公式也给相同结论。以下两个有理输入均非零。

若 $r,s>0$，嵌入保序使两分割正，定义第一支及NP4给
$$
i(r)\otimes i(s)=P(i(r),i(s))=i(rs).
$$

若 $r<0,s>0$，则 $i(r)$ 负、$i(s)$ 正，且 $-r>0$。已有相反数相容给 $N(i(r))=i(-r)$，所以
$$
\begin{aligned}
i(r)\otimes i(s)
&=N(P(N(i(r)),i(s)))\\
&=N(P(i(-r),i(s)))\\
&=N(i((-r)s))\\
&=i(-((-r)s))\\
&=i(rs).
\end{aligned}
$$
NP4在第三行的输入 $-r,s$ 都正；第四行是相反数相容。末行由有理符号律 $(-r)s=-(rs)$ 和有理双重取反得到。

若 $r>0,s<0$，则 $r,-s$ 都正，第三支给
$$
\begin{aligned}
i(r)\otimes i(s)
&=N(P(i(r),N(i(s))))\\
&=N(P(i(r),i(-s)))\\
&=N(i(r(-s)))\\
&=i(-(r(-s)))\\
&=i(rs).
\end{aligned}
$$
第三行仍只对正有理输入应用NP4；最后使用 $r(-s)=-(rs)$。

若 $r,s<0$，则 $-r,-s$ 正，第四支给
$$
\begin{aligned}
i(r)\otimes i(s)
&=P(N(i(r)),N(i(s)))\\
&=P(i(-r),i(-s))\\
&=i((-r)(-s))\\
&=i(rs).
\end{aligned}
$$
最后一行用有理双取反乘积规律。四个非零区域与此前零区域共同穷尽全部输入，所以相容性成立。

代入具体有理数，
$$
i(-2/3)\otimes i(3/5)
=i((-2/3)(3/5))=i(-2/5),
$$
$$
i(-2/3)\otimes i(-3/5)
=i((-2/3)(-3/5))=i(2/5).
$$
前一个乘积负、后一个乘积正，与一般符号规律一致。两个算例是已证全称结论的应用；一般结论依赖前面的零支与四区域证明，不能由两次代入取得。

### 题8完整解答：零积判据没有构造倒数 {#cutsigned-a08}

[返回题目](#cutsigned-q08)

若 $A=0_{\mathbb R}$ 或 $B=0_{\mathbb R}$，题2的两个位置零公式直接给 $A\otimes B=0_{\mathbb R}$。

反过来，假设 $A\otimes B=0_{\mathbb R}$，却有两个输入都非零。题4允许写
$$
A=E_e(U),\qquad B=E_f(V),\qquad U,V>_{\mathbb R}0_{\mathbb R}.
$$
非负正积结论给 $T=P(U,V)>_{\mathbb R}0_{\mathbb R}$。符号公式把乘积写成 $E_{e\diamond f}(T)$。若 $e\diamond f=0$，乘积等于正分割 $T$，不等于零；若 $e\diamond f=1$，乘积等于 $N(T)$，由严格反序为负，也不等于零。标签只有这两种取值，所以两种都与假设矛盾。故至少一个输入必须为零，得到
$$
A\otimes B=0_{\mathbb R}
\Longleftrightarrow A=0_{\mathbb R}\text{ 或 }B=0_{\mathbb R}.
$$

倒数存在要求另外一个全称存在命题：
$$
\text{对每个 }A\ne0_{\mathbb R},\
\text{存在 }X\in\mathbb R\text{ 使 }A\otimes X=1_{\mathbb R}.
$$
本题零积判据只说明两个非零输入相乘不会等于零，并未对给定的非零 $A$ 构造任何使输出为 $1_{\mathbb R}$ 的输入 $X$。所以不能据此宣称倒数存在；后续必须给候选集合，核其是分割，并验证乘积等于一。

全符号分配要求对任意 $A,B,C\in\mathbb R$ 证明
$$
A\otimes(B\oplus C)
=(A\otimes B)\oplus(A\otimes C),
$$
以及另一侧的对应公式。当前非负分配只允许相关输入非负；如果 $B,C$ 异号，其和又可能正、零或负，必须核这些新的符号情形。零积判据没有提供这样的等式。所以下一单元仍需独立完成全分配，不能因乘法符号与结合已证，就自动把它也算作已证。
