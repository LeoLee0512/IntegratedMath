## 基础单元 B3.2 课后题完整解答 {#sio-answers}

对应[集合包含、相等与有限次集合运算](#sio-unit)。所有补集均带工作全集下标；相等按两向包含或逐成员双向等价核实。集合存在与外延背景沿正文采用，不由某个有限计算推出任意集合的结论。

### 题1：成员与包含检查的对象不同 {#sio-a01}

[返回题目](#sio-q01)

$A=\{0,2\}$的列举明确把0收入，故$0\in A$为真。$\{0\}\subseteq A$也为真，但理由要检查左边集合的成员：任取$x\in\{0\}$，有$x=0$，而$0\in A$，所以$x\in A$。成员命题与子集命题的对象角色不同，这两个真值不能靠混写记号取得。

对于$A\subseteq B$，任取$x\in A$，列举给$x=0$或$x=2$；两种数都在$B=\{0,1,2\}$中，所以包含成立。反向$B\subseteq A$为假：$1\in B$，而1与0、2都不同，所以$1\notin A$。这是一个确实属于左边、却不属于右边的反例。

$\varnothing\subseteq A$为真，因为其否定要求存在$x\in\varnothing$且$x\notin A$，而空集没有元素。这个论证没有从空集中取出对象。

$\varnothing\in\{\varnothing\}$为真：右边是明确列出一个元素的集合，该元素恰为空集。空集作为对象可以被另一个集合收进来，与空集自身没有元素不矛盾。也正因$\varnothing$属于$\{\varnothing\}$却不属于$\varnothing$，两集合的成员不同，外延原则给$\{\varnothing\}\ne\varnothing$。此处不需要假定自然数在某种集合模型里是什么对象。

### 题2：按定义核有限运算 {#sio-a02}

[返回题目](#sio-q02)

工作范围为$U=\{0,1,2,3,4,5\}$。用成员表把全部六个对象列出，T表示属于，F表示不属于：

| 对象 | $A$ | $B$ | $C$ |
|---|---|---|---|
| 0 | T | F | T |
| 1 | F | T | F |
| 2 | T | T | F |
| 3 | F | F | F |
| 4 | F | T | T |
| 5 | T | F | T |

交要求$A,B$两列都真，只有2满足，所以$A\cap B=\{2\}$。并要求至少一列真，0、1、2、4、5满足，3不满足，所以$A\cup B=\{0,1,2,4,5\}$。

$A\setminus B$要求$A$列真而$B$列假，恰是0、5，故为$\{0,5\}$。$B\setminus A$要求相反，恰是1、4，故为$\{1,4\}$。两个差不同；差的方向不能交换。

$C_U(A\cap B)$从完整的$U$删去交集唯一成员2，所以

$$
C_U(A\cap B)=\{0,1,3,4,5\}.
$$

没有把$U$外的对象加到补中；也没有因为3不属于$A$或$B$就把它从补中排除，恰恰它属于$U$且不在交中，应被保留。

先求$B\cup C$：$B$贡献1、2、4，$C$贡献0、4、5，合起来是$\{0,1,2,4,5\}$。$A$的三个成员0、2、5都在这个并中，所以从$A$删去它们后没有剩余，得到

$$
A\setminus(B\cup C)=\varnothing.
$$

最后$A\setminus B=\{0,5\}$，这两个对象也都在$C$中，故

$$
(A\setminus B)\cap C=\{0,5\}.
$$

每一步的条件都只在$U$的六个候选上判断，表中已经穷尽它们，且定义排除所有$U$外对象。因此既核实列出的每个成员满足条件，也核实其他对象不应收入；这只证明本题具体集合计算，不替代一般集合恒等式的证明。

### 题3：包含有两个等式刻画 {#sio-a03}

[返回题目](#sio-q03)

先证明$A\subseteq B$推出$A\cap B=A$。任取$x\in A\cap B$，交的成员条件给$x\in A$，所以$A\cap B\subseteq A$。反向任取$x\in A$，由假设得$x\in B$，故同时在两集合中，$x\in A\cap B$。于是$A\subseteq A\cap B$。两个包含给出所需相等。

反过来，假设$A\cap B=A$。任取$x\in A$，由集合相等，$x\in A\cap B$，交的定义再给$x\in B$。这对任意$x\in A$成立，故$A\subseteq B$，第一个当且仅当完成。

再证明$A\subseteq B$推出$A\cup B=B$。任取$x\in A\cup B$，则$x\in A$或$x\in B$；第一支用假设得到$x\in B$，第二支本来就在$B$中，所以$A\cup B\subseteq B$。反向任取$x\in B$，它满足并的第二支，故$x\in A\cup B$，得到$B\subseteq A\cup B$，两包含给相等。

反过来，若$A\cup B=B$，任取$x\in A$，它属于$A\cup B$，再由相等属于$B$。因此$A\subseteq B$，第二个当且仅当完成。

四个方向都是条件性的任意成员论证，没有一步必须先取得某个成员，所以不要求$A$或$B$非空。例如$A=\varnothing$时，第一个等式为$\varnothing\cap B=\varnothing$，第二个为$\varnothing\cup B=B$；与$\varnothing\subseteq B$完全相容。若$B=\varnothing$，包含成立只可能$A=\varnothing$，两个等式也会要求同样结果。

### 题4：分配时不能漏掉一个条件 {#sio-a04}

[返回题目](#sio-q04)

从左向右，任取$x\in A\cup(B\cap C)$。若$x\in A$，则它同时满足两个并的$A$支，故$x\in A\cup B$且$x\in A\cup C$，于是属于右侧交。若$x\in B\cap C$，则$x\in B$使它进入$A\cup B$，$x\in C$使它进入$A\cup C$，仍属于右侧交。并的两支覆盖原成员条件，得到左侧包含于右侧。

从右向左，任取$x\in(A\cup B)\cap(A\cup C)$。于是它在两个并中。按$x\in A$或$x\notin A$分情况：若在$A$中，直接进入$A\cup(B\cap C)$。若不在$A$中，第一个并的成员条件迫使$x\in B$，第二个迫使$x\in C$。因此$x\in B\cap C$，再进入左侧并。两种情况穷尽，反向包含也成立，外延原则给等式。

再检验题给错误猜想。$A=B=\varnothing$、$C=\{0\}$，所以$B\cup C=\{0\}$。左侧

$$
A\cap(B\cup C)=\varnothing\cap\{0\}=\varnothing,
$$

因为没有任何对象属于空集$A$。右侧$A\cap B=\varnothing$，于是

$$
(A\cap B)\cup C=\varnothing\cup\{0\}=\{0\}.
$$

0属于右侧却不属于左侧，故错误式不成立。正确交对并分配的第二支是$A\cap C$，仍要求属于$A$；删掉这个条件便把本来不许进入的0收入右侧。

### 题5：两条德摩根逐元素重建 {#sio-a05}

[返回题目](#sio-q05)

先证第一式。任取$x\in C_U(A\cup B)$，得到$x\in U$且$x\notin A\cup B$。若$x\in A$，就会在并中，矛盾；若$x\in B$也一样。因此$x\notin A$且$x\notin B$。连同$x\in U$，分别得到$x\in C_U(A)$与$x\in C_U(B)$，所以$x$在右侧交中。

反向，任取$x\in C_U(A)\cap C_U(B)$，有$x\in U$、$x\notin A$且$x\notin B$。两个成员条件都假，包容或也假，故$x\notin A\cup B$。再利用$x\in U$，得到$x\in C_U(A\cup B)$。两个包含证明第一式。

再证第二式。任取$x\in C_U(A\cap B)$，有$x\in U$且$x\notin A\cap B$。交的成员条件为“在$A$且在$B$”；它的否定按LQ1等价于“非$A$成员或非$B$成员”。若$x\notin A$，结合$x\in U$得$x\in C_U(A)$；若$x\notin B$，同理得$x\in C_U(B)$。至少一支成立，所以$x$在右侧并中。

反向，任取$x\in C_U(A)\cup C_U(B)$。第一支若成立，补的定义给$x\in U$且$x\notin A$，所以$x$不可能在$A\cap B$。第二支若成立，同样得到$x\in U$且$x\notin B$，也不可能在交中。两支都给$x\in U$且$x\notin A\cap B$，因而$x\in C_U(A\cap B)$。第二式的两个方向完成。

每次由$x\notin A$等条件组成补集成员，都同时使用了$x\in U$；单独一个非成员条件不能排除工作范围外的对象。所有补都取同一$U$，所以这项条件在各方向持续保留。

若$U=\varnothing$，任何$A\subseteq U$都没有成员，否则它的成员也会属于空集；所以$A=B=\varnothing$。交、并都为空，从空$U$删去任何成员仍为空，两式的左右均为空。这个检查没有假装能从空域挑一个$x$。

### 题6：差集中的保留条件不能丢 {#sio-a06}

[返回题目](#sio-q06)

各集合都是$U$的子集，比较时可固定任意$x\in U$；对$U$外对象，各个待比较集合均无成员。第一式的成员条件逐步为

$$
\begin{aligned}
x\in A\setminus(B\cup C)
&\Longleftrightarrow x\in A\ \wedge\ x\notin B\cup C\\
&\Longleftrightarrow x\in A\ \wedge\ x\notin B\ \wedge\ x\notin C\\
&\Longleftrightarrow x\in(A\setminus B)\cap(A\setminus C).
\end{aligned}
$$

第一步是差的定义，第二步是并成员条件的否定及LQ1德摩根规律。最后一步双向检查如下：若$x$在$A$中且同时不在$B,C$中，它便同时在$A\setminus B$与$A\setminus C$中；反过来，若它在这两个差的交中，两项都给$x\in A$，并分别给$x\notin B,x\notin C$。重复一次同样的$A$成员条件没有改变真假。因此每一步都双向，两个集合对所有成员的判断相同，由外延原则得到相等。

第二式先保留$A$条件，再对交取否定：

$$
\begin{aligned}
x\in A\setminus(B\cap C)
&\Longleftrightarrow x\in A\ \wedge\ x\notin B\cap C\\
&\Longleftrightarrow x\in A\ \wedge\ (x\notin B\ \vee\ x\notin C)\\
&\Longleftrightarrow x\in(A\setminus B)\cup(A\setminus C).
\end{aligned}
$$

前两步由差定义及交成员条件的德摩根否定。最后一步也要核两个方向：若$x\in A$且不在$B$或不在$C$，第一种使它在$A\setminus B$，第二种使它在$A\setminus C$，故进入两差的并。反过来，若进入两差之一，每支都给$x\in A$，并分别给$x\notin B$或$x\notin C$，得到上一行。所有允许成员判断等价，证明第二式。

若丢掉$x\in A$，就会把只满足外侧否定、却根本不在$A$中的对象收入结果。差的被减集合决定保留范围，不能在应用逻辑德摩根时一并删去。

### 题7：包含怎样传递给运算 {#sio-a07}

[返回题目](#sio-q07)

假设$A\subseteq B\subseteq U$且$C\subseteq U$。任取$x\in A\cap C$，则$x\in A$且$x\in C$。由包含得$x\in B$，与$x\in C$合起来给$x\in B\cap C$。因此$A\cap C\subseteq B\cap C$。

任取$x\in A\cup C$。若$x\in A$，由假设得到$x\in B$，所以$x\in B\cup C$；若$x\in C$，直接属于$B\cup C$。两支都达到目标，故$A\cup C\subseteq B\cup C$。

对于补，任取$x\in C_U(B)$，有$x\in U$且$x\notin B$。若$x\in A$，假设$A\subseteq B$会推出$x\in B$，矛盾；所以$x\notin A$。保留$x\in U$，得到$x\in C_U(A)$。于是$C_U(B)\subseteq C_U(A)$，包含方向反过来了。

反向猜想“从$A\cap C\subseteq B\cap C$推出$A\subseteq B$”并不总成立。取题给$U=\{0\}$、$A=\{0\}$、$B=C=\varnothing$，两边与$C$的交都是空集，所以运算后包含$\varnothing\subseteq\varnothing$成立。但$0\in A$且$0\notin B$，所以原包含失败。这不反驳已经证明的正向结论，因为反例没有满足其前提$A\subseteq B$；它只说明交上一个集合可能隐藏原来的差别。

### 题8：同名补集背后的全集 {#sio-a08}

[返回题目](#sio-q08)

题给$U=\{0,1\}$、$V=\{0,1,2\}$、$A=B=\{0\}$。从$U$删去0剩1，故$C_U(A)=\{1\}$；从$V$删去0剩1、2，故$C_V(B)=\{1,2\}$。又$A\cap B=\{0\}$，所以

$$
C_U(A\cap B)=\{1\},
\qquad C_U(A)\cup C_V(B)=\{1,2\}.
$$

2在右侧而不在左侧，二者不相等。SI4的正确右侧是$C_U(A)\cup C_U(B)$，两个补都相对于$U$；题中的第二个补改用了$V$，把$U$外的2带入右侧，因此不满足同一全集的公式条件。右侧的并本身可以在$V$中合法定义，这并不能修复它与左侧的差异。

对一般$U\subseteq V$且$A\subseteq U$，先证

$$
U\setminus A\subseteq U\cap(V\setminus A).
$$

任取左侧成员$x$，有$x\in U$且$x\notin A$；由$U\subseteq V$得$x\in V$，所以$x\in V\setminus A$。再与$x\in U$合起来，得到右侧交成员。这里所有右侧运算都可以在较大的已给工作范围$V$内解释。

反向，任取$x\in U\cap(V\setminus A)$。交的定义给$x\in U$，差的定义给$x\notin A$，合起来恰为$x\in U\setminus A$。两个包含证明

$$
U\setminus A=U\cap(V\setminus A).
$$

这不声称$U\setminus A=V\setminus A$。它说先在较大范围取补，再交回$U$，才得到较小范围的补。本题具体例子中，较大补$\{1,2\}$交回$\{0,1\}$后删去2，只剩$\{1\}$，与已算结果一致。
