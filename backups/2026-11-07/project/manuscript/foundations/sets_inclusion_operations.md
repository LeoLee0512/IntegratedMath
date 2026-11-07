## 基础单元 B3.2 集合包含、相等与有限次集合运算 {#sio-unit}

**位置与目标。** 本单元主归第8章03Exx集合论的03E20（包括函数、关系与集合代数），交叉第525章97E60集合与集合论教育。目标是从成员条件逐步证明包含和相等，定义交、并、差及相对补，证明两条分配律和两条德摩根规律，并辨认空集与全集改变时的边界。“有限次运算”指二元运算及有限个嵌套，参与的集合自身不必有限。不引入任意集合族的并交、幂集或基数理论，不构造公理集合论、选择原则或数系的集合模型；本单元不表示分类叶或整章完成。

**精确先修。** 沿用[成员、子集、空集与条件子集](#fun-sets)的集合背景，有限数值例只用[自然数命名及不同性](#b1-peano-rules)。证明语言来自B3.1已写的[经典语义约定](#lcq-conventions)、[且与包容或](#lcq-connectives)、[否定与等价LQ1](#lcq-equivalence)、[前提保真推断](#lcq-inference)、[带域量词及空域](#lcq-quantifiers)、[量词否定LQ3](#lcq-scope-negation)。这些是具体的文本先修接口；是否已经完成某一版PDF构建是另外的产物状态。

**阅读安排。** 预计正文约14—22页，八题答案另列。先读成员与包含、运算定义、两向包含方法；再读分配与补集。图形可以帮助猜测，但本单元的结论由逐成员论证承担，不以几个有限集合的计算替代一般证明。

### 1. 固定工作集合，不制造“所有对象” {#sio-background}

沿用前文公开采用的集合背景：允许使用已给的有限集合、已建立的数集，并从一个已给集合中按明确条件取子集；集合按其元素判等。成员关系$x\in A$表示$x$属于$A$，$x\notin A$表示该成员条件的否定。这些背景不是本单元新证明的公理结论。

本单元固定一个已给集合$U$，称为当前的**工作全集**；所讨论的$A,B,C$都满足$A,B,C\subseteq U$。$U$可以是有限集，也可以是已有数集，还可以为空。“全集”只指当前工作范围，不表示存在包含所有对象的一个集合。我们只在$U$中筛选，不采用“任意条件都能形成一个不受限制的集合”。

这里$U$是工作范围，可以理解为B3.1某个非空背景对象域中的限制集合；允许它为空不改变B3.1的经典语义约定。比如背景中已有自然数，而本次只研究其空子集，也是合法安排。

三个不同类型的写法要分清：$x\in A$是成员陈述；$A\subseteq B$是关于两个集合的陈述；稍后定义的$A\cap B$本身是一个集合。前两者可以讨论真假，后者要先取元素或与别的集合比较，不能把一个集合直接说成真或假。

### 2. 包含检查所有成员，相等检查两个方向 {#sio-inclusion}

**定义回访。** $A\subseteq B$表示$A$的每个元素都属于$B$，即

$$
\forall x\in A\ (x\in B).
$$

它允许$A=B$。在已知$A,B\subseteq U$时，也可以写作$\forall x\in U\ (x\in A\to x\in B)$。一个不在$A$的对象，不是这项包含的反例；反例必须确实在左边却不在右边。

由LQ3，包含的否定准确为

$$
A\not\subseteq B
\quad\Longleftrightarrow\quad
\exists x\in A\ (x\notin B).
$$

例如$A=\{0,2\}$、$B=\{0,1,2\}$时，$A\subseteq B$，因为左边仅有的两个成员都在右边。反向$B\subseteq A$失败，成员1就是见证。这里两个集合在部分成员上一致，不等于彼此相等。

**外延相等的采用原则。** 两集合相等，当且仅当有完全相同的元素。因此证明$A=B$的一种准确任务分解是

$$
A\subseteq B\quad\text{且}\quad B\subseteq A.
$$

从相等当然得到两个包含；反过来，两个包含说明左边每个成员都在右边、右边每个成员都在左边，由采用的外延原则得到相等。这不是说必须枚举所有成员，而是要求论证覆盖任意成员。

**命题 SI1。** 对给定集合，包含具有反身性和传递性，且$\varnothing\subseteq A$。

反身性：任取$x\in A$，它已经属于$A$，所以$A\subseteq A$。传递性：若$A\subseteq B$且$B\subseteq C$，任取$x\in A$，第一前提给$x\in B$，第二前提给$x\in C$，所以$A\subseteq C$。空集情形：否定$\varnothing\subseteq A$须有属于空集而不属于$A$的成员，但空集无成员，故不存在这样的反例；也可直接按空域全称语义取得包含。

“任取$x\in A$”是在该成员条件下论证每个可能输入，不是宣称$A$一定非空。若$A$为空，没有成员需要处理，该全称论证仍成立；若某一步必须实际拿到一个成员，就另需非空条件。

### 3. 交、并、差都是有范围的条件子集 {#sio-operations}

对$A,B\subseteq U$，定义

$$
\begin{aligned}
A\cap B&=\{x\in U:x\in A\wedge x\in B\},\\
A\cup B&=\{x\in U:x\in A\vee x\in B\},\\
A\setminus B&=\{x\in U:x\in A\wedge x\notin B\}.
\end{aligned}
$$

分别读作交集、并集和差集。三者都是从已给$U$按明确条件取出的子集，因此其存在属于本单元已声明采用的集合背景，不是靠写下一个没有范围的条件创造新集合。定义中“或”是包容或：同时在$A,B$中的对象也在并中，只记录其成员身份，不重复增加元素。

因为$A,B\subseteq U$，一个对象只要已满足$x\in A$或$x\in B$，就已属于$U$。因此判断这些运算的成员时，可以简写为

$$
\begin{aligned}
x\in A\cap B&\Longleftrightarrow(x\in A\wedge x\in B),\\
x\in A\cup B&\Longleftrightarrow(x\in A\vee x\in B),\\
x\in A\setminus B&\Longleftrightarrow(x\in A\wedge x\notin B).
\end{aligned}
$$

它们的条件都会自动给出所需的$U$成员身份；对$U$外的对象，两侧都不可能成立。这里的双向箭头表示固定对象后的成员条件等价，不是把集合对象和逻辑公式混成同一种东西。

**相对补。** 对$A\subseteq U$，记

$$
C_U(A)=U\setminus A=\{x\in U:x\notin A\}.
$$

这是$A$相对于$U$的补集，下标提醒背景。其成员条件是“在$U$中并且不在$A$中”，不能只说“不在$A$中”而忘记$U$。差$A\setminus B$从$A$中删去属于$B$的成员；相对补则从指定的$U$中删去$A$。

**例题。** 取$U=\{0,1,2,3,4\}$，$A=\{0,2,4\}$、$B=\{1,2\}$。同时属于两集合的只有2，故$A\cap B=\{2\}$；属于至少一边的是0、1、2、4，故$A\cup B=\{0,1,2,4\}$。从$A$删去$B$中的成员，删去2，得到$A\setminus B=\{0,4\}$；从$B$删去$A$中的成员，同样删去2，却得到$B\setminus A=\{1\}$。所以差一般不交换。最后$U$中不在$A$的成员是1、3，故$C_U(A)=\{1,3\}$。每个答案都按整个有限范围核过，未把漏列元素当作自动排除。

### 4. 从成员条件走到集合等式 {#sio-element-method}

**命题 SI2（基本关系）。** 对$A,B\subseteq U$，有

$$
A\cap B\subseteq A,\qquad A\subseteq A\cup B,
$$

以及

$$
A\cup\varnothing=A,\qquad A\cap U=A,
\qquad C_U(C_U(A))=A.
$$

**两个包含。** 若$x\in A\cap B$，交的定义给$x\in A$，因此第一个包含成立。若$x\in A$，则“$x\in A$或$x\in B$”已真，并的定义给$x\in A\cup B$，因此第二个包含成立。两个论证都从任意左侧成员出发，不反推尚未证明的方向。

**并空集的两个方向。** 任取$x\in A\cup\varnothing$，则$x\in A$或$x\in\varnothing$；第二种不可能，所以$x\in A$。这给$A\cup\varnothing\subseteq A$。反向任取$x\in A$，它满足并的第一支，故$x\in A\cup\varnothing$。两包含得到相等。

**交全集的两个方向。** 任取$x\in A\cap U$，直接得$x\in A$。反向任取$x\in A$，由先决条件$A\subseteq U$还有$x\in U$，所以$x\in A\cap U$。由外延原则相等；反向明确用了$A$在该工作全集内。

**双补的两个方向。** 若$x\in C_U(C_U(A))$，则$x\in U$且$x\notin C_U(A)$。若$x\notin A$，与$x\in U$合起来便给$x\in C_U(A)$，矛盾；经典二值因此给$x\in A$。反向，若$x\in A$，先由$A\subseteq U$得$x\in U$；它不可能在$C_U(A)$，因为补集成员同时要求$x\notin A$。于是$x\in U$且$x\notin C_U(A)$，故$x\in C_U(C_U(A))$。两个方向合成双补等式。SI2证毕。

两向包含的用法不是“先猜左右一样，再在中间写几个符号”。每个方向都有一个明确的任意输入、可用的成员条件，以及要到达的目标条件。若用一串双向等价代替两段证明，每一步都必须确实可逆，且所有域条件保持。

### 5. 两条分配律分别怎样证明 {#sio-distribution}

**命题 SI3。** 对同一$U$的子集$A,B,C$，

$$
A\cap(B\cup C)=(A\cap B)\cup(A\cap C),
$$

$$
A\cup(B\cap C)=(A\cup B)\cap(A\cup C).
$$

所有中间运算仍是$U$的子集，所以可以继续按同一成员定义解释。

**第一式从左到右。** 任取$x\in A\cap(B\cup C)$。则$x\in A$，并且$x\in B\cup C$。后者分为$x\in B$或$x\in C$。第一支与$x\in A$合起来给$x\in A\cap B$，第二支给$x\in A\cap C$；两支都使$x$进入右侧并集。因此左侧包含于右侧。

**第一式从右到左。** 任取$x\in(A\cap B)\cup(A\cap C)$。若$x\in A\cap B$，便有$x\in A$和$x\in B$，后者给$x\in B\cup C$，所以$x\in A\cap(B\cup C)$。若$x\in A\cap C$，以$x\in C$进入同一个并集，再与$x\in A$合起来，也得到目标。或的两支穷尽，右侧包含于左侧，第一式成立。

**第二式从左到右。** 任取$x\in A\cup(B\cap C)$。若$x\in A$，则同时属于$A\cup B$与$A\cup C$，故在右侧交中。若$x\in B\cap C$，则$x\in B$和$x\in C$分别让它进入这两个并，仍在右侧交中。因此得到一个包含。

**第二式从右到左。** 任取$x\in(A\cup B)\cap(A\cup C)$，得到$x\in A\cup B$和$x\in A\cup C$。按经典二值分情况：若$x\in A$，直接进入左侧并集。若$x\notin A$，第一个并的$A$支已排除，只能有$x\in B$；第二个并同理给$x\in C$。因此$x\in B\cap C$，进入左侧并集。两种情况覆盖全部可能，反向包含成立，第二式证毕。

证明没有把两个“或”同时成立误读成“两个都选了同一支”。当$x$不在$A$时，才由排除法迫使它分别进入$B,C$。这也说明为什么每个括号和每个重复的$A$都不能随意删除。

### 6. 德摩根规律必须使用同一个工作全集 {#sio-demorgan}

**命题 SI4。** 对$A,B\subseteq U$，

$$
C_U(A\cup B)=C_U(A)\cap C_U(B),
$$

$$
C_U(A\cap B)=C_U(A)\cup C_U(B).
$$

**第一式从左到右。** 若$x\in C_U(A\cup B)$，则$x\in U$且$x\notin A\cup B$。若$x\in A$或$x\in B$任一成立，就会使$x\in A\cup B$，所以二者都不成立。连同$x\in U$，得到$x\in C_U(A)$且$x\in C_U(B)$，因此在右侧交中。

**第一式从右到左。** 若$x\in C_U(A)\cap C_U(B)$，则补的定义给$x\in U$、$x\notin A$、$x\notin B$。并的成员条件是两个成员命题的或；二者均假，或为假，故$x\notin A\cup B$。与$x\in U$合起来得到左侧成员，两个包含证明第一式。

**第二式从左到右。** 若$x\in C_U(A\cap B)$，则$x\in U$且$x\notin A\cap B$。交的定义把后者解释为否定“$x\in A$且$x\in B$”。由LQ1的德摩根规律，$x\notin A$或$x\notin B$。在第一支，连同$x\in U$得$x\in C_U(A)$；第二支得$x\in C_U(B)$。所以两支都使$x$进入右侧并。

**第二式从右到左。** 若$x\in C_U(A)\cup C_U(B)$，就至少在一个补集中。若在$C_U(A)$，有$x\in U$且$x\notin A$，它不可能同时在$A$和$B$，所以不在交中。若在$C_U(B)$，同理利用$x\notin B$。两支都给$x\in U$且$x\notin A\cap B$，因此进入左侧补。第二式成立。

若$U=\varnothing$，由$A,B\subseteq U$可知二者也为空；所有交、并、补都为空，等式仍成立。上面的任意成员证明没有假定一个空集真的有成员，也没有从“非成员”单独推出“在补中”；每次都保留了$x\in U$。

### 7. 改全集时，补集为什么随之改变 {#sio-universe}

取$U=\{0,1\}$、$V=\{0,1,2\}$，$A=\{0\}$同时是它们的子集。则

$$
C_U(A)=\{1\},\qquad C_V(A)=\{1,2\}.
$$

二者不同，差异来自2是否属于工作范围。对只依赖$x\in A$、$x\in B$的交、并、差，只要工作范围都已包含$A,B$，它们的成员判据不变；补集额外使用全集本身，因而一般会改变。

还可精确比较嵌套工作范围。若$U\subseteq V$且$A\subseteq U$，则

$$
U\setminus A=U\cap(V\setminus A).
$$

从左到右：若$x\in U\setminus A$，有$x\in U$且$x\notin A$；由$U\subseteq V$得$x\in V$，所以$x\in V\setminus A$，于是属于右侧交。从右到左：若$x\in U\cap(V\setminus A)$，有$x\in U$且$x\notin A$，正好给$x\in U\setminus A$。两个包含证得等式。右侧的运算可以全在较大的工作范围$V$中解释；没有把不同全集的补集直接视为相同。

德摩根公式中每个补都必须相对于同一个$U$。若将其中一个偷偷改用$V$，可能把$U$外的元素带到一侧，公式失效；题8会给完整反例。因此书写简略符号以前，要先固定并记住补集的范围。

### 8. 来源与采用边界 {#sio-sources}

定义和标准操作核对Oscar Levin，*Discrete Mathematics: An Open Introduction*，第四版活动原生[Sets章节](https://raw.githubusercontent.com/oscarlevin/discrete-book/master/source/sec_structures-sets.ptx)。实际读集合、外延相等、包含和交并补差的指定段；当前内容SHA-256及阅读行段在来源记录中。主文件明确第四版；许可按实际LICENSE与frontmatter为CC BY-NC-SA 4.0，不移用早期版许可。

该来源用于核定义与范围。本单元分配及德摩根证明依本书LQ语义逐元素独立写出，不声称外部章节已经给出相同证明。没有迁入源书幂集、基数或图示内容，也没有把某个数必须是或不是集合当作新的数系公理。本文所采用的集合外延与限定子集背景仍是开头那份约定，不由这些等式倒推出任意概括原则。

### 9. 课后练习 {#sio-exercises}

#### 题1：成员与包含检查的对象不同 {#sio-q01}

取$A=\{0,2\}$、$B=\{0,1,2\}$。判断$0\in A$、$\{0\}\subseteq A$、$A\subseteq B$、$B\subseteq A$，每项给完整理由或反例。再证明$\varnothing\subseteq A$，判断$\varnothing\in\{\varnothing\}$，并说明$\{\varnothing\}\ne\varnothing$。[参考答案](#sio-a01)

#### 题2：按定义核有限运算 {#sio-q02}

取$U=\{0,1,2,3,4,5\}$，$A=\{0,2,5\}$、$B=\{1,2,4\}$、$C=\{0,4,5\}$。求$A\cap B$、$A\cup B$、$A\setminus B$、$B\setminus A$、$C_U(A\cap B)$、$A\setminus(B\cup C)$及$(A\setminus B)\cap C$。说明每个答案如何同时检查收进来的成员和被排除的成员。[参考答案](#sio-a02)

#### 题3：包含有两个等式刻画 {#sio-q03}

对$A,B\subseteq U$证明：$A\subseteq B$当且仅当$A\cap B=A$，也当且仅当$A\cup B=B$。分别给出两个“当且仅当”的正反方向，并说明是否要求$A$或$B$非空。[参考答案](#sio-a03)

#### 题4：分配时不能漏掉一个条件 {#sio-q04}

独立用两向包含证明$A\cup(B\cap C)=(A\cup B)\cap(A\cup C)$。再取$U=\{0\}$、$A=B=\varnothing$、$C=\{0\}$，核验错误猜想$A\cap(B\cup C)=(A\cap B)\cup C$在哪里失败。[参考答案](#sio-a04)

#### 题5：两条德摩根逐元素重建 {#sio-q05}

对同一$U$的子集$A,B$，用两向包含证明$C_U(A\cup B)=C_U(A)\cap C_U(B)$及$C_U(A\cap B)=C_U(A)\cup C_U(B)$。标出每次从“非成员”转成补集成员时还用了什么条件；最后单独核$U=\varnothing$。[参考答案](#sio-a05)

#### 题6：差集中的保留条件不能丢 {#sio-q06}

对$A,B,C\subseteq U$，证明$A\setminus(B\cup C)=(A\setminus B)\cap(A\setminus C)$和$A\setminus(B\cap C)=(A\setminus B)\cup(A\setminus C)$。可用逐成员等价链，但须说明每一步双向成立，并保留“属于$A$”的条件。[参考答案](#sio-a06)

#### 题7：包含怎样传递给运算 {#sio-q07}

设$A\subseteq B\subseteq U$且$C\subseteq U$。证明$A\cap C\subseteq B\cap C$、$A\cup C\subseteq B\cup C$及$C_U(B)\subseteq C_U(A)$。从第一个运算后包含是否总能反推$A\subseteq B$？用$U=\{0\}$、$A=\{0\}$、$B=C=\varnothing$检验反向。[参考答案](#sio-a07)

#### 题8：同名补集背后的全集 {#sio-q08}

取$U=\{0,1\}$、$V=\{0,1,2\}$、$A=B=\{0\}$，计算$C_U(A)$、$C_V(B)$，比较$C_U(A\cap B)$与$C_U(A)\cup C_V(B)$，指出为何不是同一全集下的德摩根公式。再对一般$U\subseteq V$、$A\subseteq U$证明$U\setminus A=U\cap(V\setminus A)$；解释这与两个补集通常不相等为何相容。[参考答案](#sio-a08)
