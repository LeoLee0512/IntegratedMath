# 一元一次方程与二元一次方程组来源审计（2026-10-29）

范围为B2.5、B2.6，正文来源锚为 `linear-equations-sources`。这是公开来源审计，不是正文或整章完成证明。

通过继承代理及正常TLS实际发出24次公开请求：23次200；最初误猜的 `openstax/osbooks-prealgebra` 为404，随后定位真实bundle仓库。失败请求如实保留，不计成功来源。环境独立检查为current/enforced/running，未读写凭据。每个响应的UTC时间、精确URL、字节数及SHA-256见同名JSON；第三方全文仅在 `/tmp`。

## 两个独立来源系列

### LIN-OPENSTAX：Elementary Algebra 2e

作者：Lynn Marecek、MaryAnne Anthony-Smith、Andrea Honeycutt Mathis。公开CNXML源码快照；commit ad40c7e3c9a909cde81a24c526f52fe26a51fb14（访问2026-10-29）。

CC-BY-NC-SA-4.0。当前快照为署名—非商业性使用—相同方式共享4.0，不能误写成CC BY4.0；艺术图像另有署名或许可边界。定位：LICENSE首行；collection行5；modules/m82630/index.cnxml行21、27。

- [Solution of an equation / fs-id1168345262736](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m82463/index.cnxml#L63)（modules/m82463/index.cnxml，行63–74）：解是代入后使等式为真的值；本书额外明确允许范围D⊆Q及两边在D处的定义条件。
- [Subtraction Property of Equality](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m82463/index.cnxml#L178)（modules/m82463/index.cnxml，行178–184）：同减一数保持等式；本书需明确反向同加回来，才证明解集相同。
- [Addition Property of Equality](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m82463/index.cnxml#L250)（modules/m82463/index.cnxml，行250–258）：同加一数保持等式；单向保持与解集等价分开。
- [Division Property of Equality](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m82464/index.cnxml#L74)（modules/m82464/index.cnxml，行74–80）：除数明确非零；本书每次除以参数或含未知数表达式时逐项验证。
- [Multiplication Property of Equality](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m82464/index.cnxml#L153)（modules/m82464/index.cnxml，行153–159）：原文乘法性质仅为a=b推出ac=bc，允许c=0；不能据此把乘零也当等价变形。
- [identity / contradiction](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m82467/index.cnxml#L803)（modules/m82467/index.cnxml，行803–855）：区分恒等与矛盾；原教材例子谈全体实数，本书按原声明D⊆Q给D或空集，不引入尚未构造的实数。
- [rational equation / extraneous solution](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m82538/index.cnxml#L101)（modules/m82538/index.cnxml，行101–108）：解方程前排除原分母为零的输入；化简后表达式看似有定义不能自动把禁值加回。只借用定义域警示，不沿用其后更高次方程题目。
- [How to solve equations with rational expressions](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m82538/index.cnxml#L154)（modules/m82538/index.cnxml，行154–168）：先记录分母禁值，再找公分母、去分母与原式检查。本书只在D中各分母非零处证明双向等价，不把增根当合法原解。
- [Elimination Method](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m82495/index.cnxml#L40)（modules/m82495/index.cnxml，行40–73）：通过等式相加与倍乘消元；本书另以可逆行操作证明保留另一方程的必要性，不能只剩一个消元后方程。
- [degenerate systems discussion](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m82495/index.cnxml#L481)（modules/m82495/index.cnxml，行481–566）：来源以图像和实例说明无解/无穷解；本书不据几幅图证明全体2×2情况，而对所有零主元和全零系数逐支证明。

### LIN-BEEZER：A First Course in Linear Algebra

作者：Robert A. Beezer。src/bookinfo.xml版本3.50，版权2004–2015；commit 347f27fe909b54b26970bcc0fcbf69c7e853c766。

GFDL-1.2-or-later。无不变章节、无封面文本要求；若分发改编仍须遵守GFDL义务。定位：COPYING.txt；src/bookinfo.xml行19。

- [SLE / SSLE / SSSLE](https://github.com/rbeezer/fcla/blob/347f27fe909b54b26970bcc0fcbf69c7e853c766/src/section-SSLE.xml#L43)（src/section-SSLE.xml，行43–74）：声明系数、常数和未知数所在数域，解为同时满足全部方程的有序表，解集须包含所有且仅所有解。源域为复数，正文暂限Q。
- [ESYS / EO](https://github.com/rbeezer/fcla/blob/347f27fe909b54b26970bcc0fcbf69c7e853c766/src/section-SSLE.xml#L149)（src/section-SSLE.xml，行149–167）：等价系统定义为解集相等；三类操作为交换方程、非零倍乘、另一方程任意倍相加且保留原式。
- [EOPSS：交换与非零倍乘证明](https://github.com/rbeezer/fcla/blob/347f27fe909b54b26970bcc0fcbf69c7e853c766/src/section-SSLE.xml#L178)（src/section-SSLE.xml，行178–226）：分别证明两向包含；非零倍乘的反向明确使用1/α，说明α=0时证明断裂。交换不依赖方程次序。
- [EOPSS：倍加另一式证明](https://github.com/rbeezer/fcla/blob/347f27fe909b54b26970bcc0fcbf69c7e853c766/src/section-SSLE.xml#L230)（src/section-SSLE.xml，行230–263）：通过仍保留的第i式从第j式新等式减回α倍；该操作的α可以为零，不能把它与整式非零倍乘条件混淆。
- [CSRN](https://github.com/rbeezer/fcla/blob/347f27fe909b54b26970bcc0fcbf69c7e853c766/src/section-TSS.xml#L356)（src/section-TSS.xml，行356–375）：一般系统以行最简形与主元数区分唯一解和自由变量。本书没有这些先修，不引用此段作为省略2×2证明的理由。
- [PSSLS](https://github.com/rbeezer/fcla/blob/347f27fe909b54b26970bcc0fcbf69c7e853c766/src/section-TSS.xml#L410)（src/section-TSS.xml，行410–423）：一般线性系统无解/唯一/无穷多三分法依赖前面的CSRN。本批以有理数上的2×2可逆消元独立推导，不扩大到未经教学的一般矩阵秩理论。

## 本书范围内的独立推理核验

1. 解集先固定D⊆Q，并要求U,V在D上均有定义：S={x∈D:U(x)=V(x)}。两式等价是同一D上S相同；只证明原解仍满足新式只给一个包含方向。
2. 在同一D内，同加或同减H(x)可用反操作还原；乘M(x)总给正向等式，反向要求每个相关x都有M(x)≠0。若M(x)=0未排除，必须另分支，不能消去。
3. 对于ax+b=cx+d，设A=a−c、B=d−b，则等价于Ax=B。A≠0时唯一候选B/A，还要检查属于D；A=0且B≠0时无解；A=B=0时解集为原D，而不是默认全部Q。
4. 涉及分母时D先排除每个原分母的零点；在D内去分母所乘积非零，才能证明可逆。即使约分后表达式扩大了可定义范围，也须保留原D，不把消去的禁值当解。
5. 系统解为有序对(x,y)∈Q²，必须同时满足两式。交换两式的逆是再交换；非零倍乘的逆是乘倒数；R2←R2+tR1并保留R1的逆是R2←R2−tR1，t可为零。两式相加后删除所有原式通常丢失约束。
6. 对ax+by=e、cx+dy=f，若a≠0，保留第一式，用第二式减(c/a)倍第一式得到hy=k，其中h=d−cb/a，k=f−ce/a；全部除法因a≠0合法。h≠0时y=k/h且x=(e−by)/a唯一；h=0,k≠0无解；h=k=0时令任意t∈Q，y=t,x=(e−bt)/a得到全部解。
7. 若a=0但c≠0先交换两式得到非零x主元；若x系数均为零则检查y系数，非零者可交换变量角色处理且最后换回有序对。所有变量系数均为零时，两常数均零给Q²，任一常数非零给空集。不在零主元上除法。
8. 参数解须证两方向：每个参数值代回确实满足全部原式；每个原解以它的自由坐标作为参数被公式收录。自由坐标直接等于参数，故不同参数给不同解；Q含无限多个不同整数，才得到无穷多。全零情况需要两个自由参数。
9. 本批数值采用精确有理数；有限测试核实现但不替代任意有理系数的证明。既不使用坐标图像作证据，也不把一般矩阵秩、行最简形或实数构造当成已写先修。

## 使用及完成边界

公开可读、许可条件与数学可信度分别核查。OpenStax当前许可含非商业及相同方式共享要求，不能沿用旧印象标成CC BY；Beezer版权与GFDL条件也不省略。本批只用来交叉核对事实、条件与证明链，不复制外部题干、例题、图、原文段落或源码。原创编写不是把第三方原文换几个变量。

OpenStax的实数/图像叙述、Beezer的复数域与行最简形证明并非本书已具备先修。本书仅在已建有理数上独立证明2×2全部分支；一般线性代数另行教学。有限精确验证支持代码，不替代一般证明。

归属保持第63部分97-XX、第528章97Hxx及97H30；97H20只交叉，B2.6另以实核15A06交叉，不增其完成范围。两个新增单元为第26、27单元；若全部题答实际存在，累计216基础题加绪论14题，共230题，正式计数以构建验收为准。整章、整部分均未据此完成；push仍未到期。
