# 下一有界单元计划：有限表线性无关、表示唯一性与冗余项

2026-11-05，规划者/root/part1_pedagogy，按root后续线性支线建议。本文件仅计划；FSP已完成独立数学和教学通过；本轮先交计划，待root核范围后再开正文。全部/tmp，不注册34或后续冻结输入。

建议一个有界单元，正文拟`finite_coordinate_independence.md`，8解另稿，锚fli。主归第84章15Axx/15A03的有限实坐标线性无关与冗余局部，partial。不引基、维数、交换引理、任意项重排、消元算法或m>n必相关定理；后者不能用有限索引计数界直接替代线性论证。

## 1. 固定对象及精确先修

v:I_m→V_n为有限**表**，允许重复项；m项、n坐标，允许任一为0。沿FLC用C(a,v)表示实数系数表a:I_m→R的组合。线性无关是当前表的性质，不先压成值集而丢掉重复项。系数表示的唯一性只讨论x∈span(v)，不假称它能表示所有V_n。

- 函数/逻辑：fun-definition、fc-equality、fc-restriction、lcq-scope-negation、frc-model。
- 坐标规律：frc-operations、frc-additive-laws、frc-scalar-laws、frc-cancellation。
- 组合：flc-definition、flc-coefficients、flc-scaling、flc-concatenation。
- 生成集合：fsp-generated-set、fsp-contains-entries、fsp-minimality；单位系数取项已依赖fsp-single-term-sum，不能另用未证δ求和。
- 有限和/索引：rfs-concatenation、sum-indices、ord-successor-comparison、ord-trichotomy、ord-addition-order、ord-cancellation、sub-definition、b1-addition-associative。只用连续拼接与三组向量的二元交换结合，不用任意重排。
- 实数逆与差：cutdiv-definition（非零分母及乘回，本次已读24–86）、cutgroup-negation-subtraction、cutsigned-associative、cutsigned-signs。只有选中系数a_r≠0后才写1/a_r，绝不由‘关系非平凡’推每个系数非零。

## 2. 六项目标和证明义务

### FLI1：零关系、无关与非平凡见证（fli-definition）

定义表v无关为对所有a∈V_m，C(a,v)=0_n⇒a=0_m；相关为存在a，C(a,v)=0_n且存在r<m满足a_r≠0。由逐点判等和经典量词否定证明这两个概念互为否定。零系数总给零组合，但它不是相关见证。

m0只有一份空系数表，所以空向量表无关，span={0_n}；n0/m>0的每项为空向量，单位系数e^(0)非零且组合0_0，因此相关。含零项用e^(r)见证；重复项r≠s用e^(r)−e^(s)与下一项差公式见证（若按叙述顺序尚未得差公式，放在FLI2后再证）。不称重复值集无关性与表无关性相同。

### FLI2：系数差与表示唯一性（fli-uniqueness）

先由FLC2/3及FRC负号推出C(a−b,v)=C(a,v)−C(b,v)，逐式写出a−b=a+(-1)b，不能仅凭符号猜。然后证明无关⇔映射a↦C(a,v)单射⇔每个x∈span(v)恰有一份系数表。

正向C(a)=C(b)给差组合0，再无关得a−b=0_m，逐坐标实数群律给a=b。反向把零关系与零系数两份表示比较；‘每个x∈span’的存在性来自定义，唯一性来自刚证单射。没有要求span(v)=V_n。

### FLI3：删除指定位置的显式索引（fli-deletion）

给r<m。后继比较给r+1≤m，故自然差s=m−(r+1)存在且m=(r+1)+s。定义前缀p:I_r→V_n，p_k=v_k；后缀q:I_s→V_n，q_t=v_(r+1+t)。由自然加法保持严格序核r+1+t<m，输出合法。删除表u=p∥q:I_(r+s)→V_n，规定u_k=v_k(k<r)，u_(r+t)=v_(r+1+t)(t<s)。明确前后索引不交、后段局部差k−r仅r≤k时使用且唯一；沿RFS/FLC拼接。无需统一写m−1。

同法删除系数a中位置r，得b=a^−∥a^+。原表和原系数是‘前缀—一项—后缀’两次连续拼接。FLC5与单项式给
C(a,v)=(C(a^−,p)+a_r v_r)+C(a^+,q)，
C(b,u)=C(a^−,p)+C(a^+,q)。

这两式证明后才能求解单项。r0允许前缀空，r为末项允许后缀空，m1删除后空表；m0没有r可删除。这里不先用不明的‘删去一个项自然不变’。

### FLI4：有非零指定系数恰对应指定项冗余（fli-redundancy）

对上面的指定r与删除表u，证明以下等价：
- 存在零关系a且a_r≠0；
- v_r∈span(u)。

正向写A=C(a^−,p)、B=a_r v_r、D=C(a^+,q)，由(A+B)+D=0，通过明确两次二元结合/一次交换把它写成(A+D)+B=0，故B=−(A+D)=−C(b,u)。只有此时用a_r≠0，FRC标量结合与实数逆乘回给v_r=C((-1/a_r)b,u)。应写出实际新系数表，零长度亦允许。

反向若v_r=C(b,u)，先将b按删除表的前r/后s位置拆成γ/δ。构造原长a，前缀−γ、r处1、后缀−δ。两次FLC5给C(a,v)=(-A+v_r)+(-D)，而v_r=A+D，由向量二元结合/逆元得0_n；a_r=1≠0，是非平凡关系。这里可选择中系数−1但全文固定一种，不混正负。

### FLI5：删除冗余项恰不改变生成集合（fli-span-deletion）

删除表u的每项都是v的某项，所以fsp-contains-entries与最小性给span(u)⊆span(v)。若v_r∈span(u)，原表其余项也由前/后索引映射属于span(u)，最小性给span(v)⊆span(u)。反向若两个span相等，v_r∈span(v)给v_r∈span(u)。因此指定项冗余⇔删后span相同。

由相关见证至少一个非零坐标可选r，得到‘相关表至少有一个可删冗余项’。不能推成每个项都可删；选中a_r=0时不能做上述除法。无关表若有项，删除任一项均改变span，否则反向FLI4给非平凡关系。

### FLI6：删除不会破坏原来的无关性（fli-deletion-independent）

若v无关，任给删除表u的零关系b，在原位置r插入系数0，其余按删除的前后对应回填为a。两次拼接及0倍/零向量给C(a,v)=C(b,u)=0_n。无关给a全零，前后对应给b全零，故u无关。仅处理明确删除一次，不延伸到未定义的一般子族/基抽取算法。

## 3. 八题与独立答案义务

1. 定义和量词否定：m0/n0，两类零记录；辨认零系数为何不是相关见证。
2. 用坐标证明v0=(1,0),v1=(1,1)无关；含零项及重复项各给确切非平凡系数，并明确表与值集区别。
3. 系数差公式及表示唯一性三向等价完整证明，特别解释只要求x∈span。
4. m4/r1删除的显式前后索引表，再完整核一般r0/末项/m1；不取空前驱。
5. v0=(1,0),v1=(3,2),v2=(0,1)，关系(-6,2,-4)指定r1；除以已知非零2得删后系数(3,2)，逐坐标核。反向按前缀/中1/后缀构造新关系(-3,1,-2)。
6. FLI4与FLI5的一般反向及最小性两包含证明；强调原长关系的r系数确实非零。
7. FLI6零插入全证明和单项非零表删除后的空表边界；不将空表的无关性误说成能生成整个V_n。
8. 相关不等于任意项冗余：v=((1,0),(0,1),(2,0))的关系(-2,0,1)；可删第三项，但删中项后所有组合第二坐标0，不能生成(0,1)。不得对关系的零中系数除法。说明与计数/维数定理的界限。

## 4. 已实际读取的来源与限制

本次从先前实际读取的固定Beezer原生src目录取得LI/LISS/LDS精确路径；三个固定raw文件均HTTP200，记录在`/tmp/finite-coordinate-independence-source-cache/requests.json`。实际读：

- section-LI.xml 1–40：零关系、非平凡、无关/相关定义。源以集合叙述，本书用允许重复的有限表，需要另明确重复项边界。
- section-LISS.xml 578–622：唯一表示定理与系数相减证明；源在“basis”及抽象向量空间/全体V被生成的框架，本书仅用其系数差论证思路，将存在性范围限定span(v)，不导入基名称或全域覆盖。
- section-LDS.xml 1–99：非平凡关系隔离非零系数得到一项是其余项组合，及逆向关系。该思路确来自所读源；本书补明确I_m函数表删除/拼接、两空段、非零分母及逐点记录，不声称这些索引细节已在源中给出。源后续矩阵化例、基抽取与维数结论未实读采用。

源主体复数、1起索引，本书仅实数、0起索引；全部例题/练习/答案须原创，不能复用源数值题解。版本3.50/作者/许可GFDL1.2或以后、无不变节/封面文字，在本会话此前已实际核COPYING全文和bookinfo1–22；这次不冒报新许可HTTP。后续若正文启动再出正式作者sourceJSON，保留本次实际取得路径/时间/hash。若将新缓存保全到ignored local-inputs，按root新要求另写cache-preservation.json映射，不回改已签历史sourceJSON。

## 5. 启动条件

FSP正文最终d61775e91c706c45cf03b216ed16e0b03de8799926f51302815c51ffdf09fd97及答案93847c7812c470fb727c277edd5853ea64f0071b63ec4776c65ec9d8330f29dc现已完成独立数学审（报告SHA e3b73d9a00a4ec19ef2fb1866960a6069949d901373458eb1a3280d8ab2ac11d）。当前只交此计划，不预报正文、章节或构建完成。
