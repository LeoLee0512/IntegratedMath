# V_n线性子空间与有限表生成集合：有界计划

2026-11-05，作者/root/part1_pedagogy。FLC现已独立数学/教学通过，root准许开始；本单元全部/tmp，不注册34冻结输入。综合范围可在一个单元中完整承载：六目标、8题独立全解；不加入子空间交/和、商空间、基、维数、独立性或消元算法。如独审认为超长，沿单项和引理之前拆分，不删证明。

主归第84章15Axx/15A03（Vector spaces, linear dependence, rank, lineability）有限实坐标子空间与有限生成局部，partial。仅V_n中的具体结构，不预先定义抽象向量空间。

## 精确先修

集合/函数：fun-sets、fun-image、fun-definition、fc-equality、fc-restriction；自然数：b1-induction、sum-indices、ord-successor-comparison、ord-trichotomy。实坐标：frc-model、frc-operations、frc-additive-laws、frc-scalar-laws。实数和：rfs-definition、rfs-prefix-table、rfs-concatenation、rfs-padding。组合：flc-data、flc-definition、flc-coefficients、flc-scaling、flc-concatenation。实数分配/次序例：cutring-distributive、cutsigned-signs、cutgroup-translation、cut-order-embedding（非负半线仅加法闭合的反例）。不以尚未证明的任意重排或克罗内克δ求和作先修。

## 固定目标与证明义务

1. **FSP1，fsp-subspace**：定义W⊆V_n、0_n∈W、对向量加法与全部实标量封闭，运算继承FRC。证明“非空+两闭合”等价，反向取任意w∈W再用0w=0_n，不暗中从空集取元；得负向量/差闭合。n0只有子空间V0={0_0}。给{0_n}、V_n和同齐次关系x1=2x0的例；非原点仿射线x1=2x0+3、非负半线V1中仅加法封闭反例。
2. **FSP2，fsp-single-term-sum**：单项可能非零的有限实数表和引理。归纳长度m，性质量化所有b:I_m→R、r<m、实数t：b_r=t且j≠r均0则Sum_R(b)=t。m0无r，结论空真；m+1用I_(m+1)=I_m∪{m}分r=m/r<m。前者前缀全零+一项t，后者前缀IH t+末项0；通过RFS拼接识别，不假设一般重排。
3. **FSP3，fsp-generated-set**：给v:I_m→V_n，定义span(v)={x∈V_n:存在a:I_m→R使x=C(a,v)}，即固定v系数映射的像。先按表定义，允许重复项/空表，未声称编号无关。FLC零系数给含0，FLC2/FLC3给加法/实标量闭合，因此子空间。m0时span={0_n}，n0任意v时span={0_0}，双向成员论证。
4. **FSP4，fsp-contains-entries**：对r∈I_m，显式系数e^(r):I_m→R，r处1、其余0；唯一输出合法。固定坐标j，加权表在r处为(v_r)_j、其余0，FSP2给和值为(v_r)_j，故C(e^(r),v)=v_r。单项可能值0也适用；m0不制造r。
5. **FSP5，fsp-minimality**：W子空间且每v_k∈W，则任意系数组合在W。对m归纳，P(m)包含所有n/W/v/a。基例m0输出0_n∈W；后继限制前m项、构造域I1的末项表，IH给前缀组合在W，实标量闭合给a_mv_m∈W，FLC5加FLC1单项式给全组合为二者之和，再加法闭合。故span(v)⊆任意含全部项的W。结合span本身子空间/含项，说明是包含关系下最小者（不是按集合基数比较）。
6. **FSP6，fsp-same-range**：在最小性之后证明同值集两有限表v:I_m→V_n、w:I_p→V_n生成相同。每w项因同值集等于某v项，属于span(v)，用最小性给span(w)⊆span(v)，反向同理。此时才可说重编号/重复列入不改变生成集合；不宣称线性组合任意重排定理已证。

## 八题固定要求

1. 三条件、非空版等价及n0唯一子空间，空集两闭合可空真却不是子空间。
2. W={(s,t):t=2s}逐条件证明，L={(s,t):t=2s+3}给不含零/0倍反例。
3. H={x∈V1:x0≥0}含0与加法闭合，实标量−1反例；说明只查正标量不够。按root教学预读意见增加迁移K={x∈V2:x1=0或x1=x0}，证明全部实标量封闭但(1,0)+(1,1)=(2,1)不属于K，形成两封闭条件的对照；仍计题3，不增加题数。
4. FSP2完整长度归纳、m0空前提与r末/非末分支，表(0,0,5,0)精确核，t0也覆盖。
5. 一般单位系数表取出指定项全证明；v0=(1,0),v1=(0,2),v2=(3,−1)用e^(1)=(0,1,0)核结果。
6. span定义的存在见证、含零及两闭合、m0/n0双向界限；区分有限表和生成集合。
7. 最小性完整项数归纳；再对(1,2)/(2,4)证明span恰为t=2s的集合，两向均给依据。
8. 同值集表生成相同的最小性证明，交换并重复列项的具体例，解释不能由表长度推出维数或借未证求和重排。

## 实际公开来源及差异

先前已从固定Beezer原生GitHub src目录实际读到section-S.xml/section-SS.xml路径；本次各raw请求HTTP200，缓存/tmp/finite-coordinate-subspaces-source-cache，requests.json记录URL/时刻/字节/hash。实际读S 1–28、90–136、170–229、413–482、789–835；SS 1–38。主采用S的子空间检验与生成集合子空间证明、SS有限列向量span定义。S后段涉及矩阵/抽象空间等只读以划界不采用；源将部分有限重组和重复闭合略写，本书用已证FLC以及显式项数归纳补齐。源的最小性完整证明与单位系数单项和引理在已读段未见，不冒称来源已给；这两步按本书既有接口原创证明。源例实际读过，借鉴封闭条件分别失败的对照思路；本书重新构造实坐标条件（含新增K两条直线条件）及数值，完整编写证明与8解，不转载或翻译源题解，不将通用思路声称为无来源的新发明。

源主要复数与抽象空间，本书仅实V_n。COPYING GFDL1.2或以后、无不变节与封面文字，版本3.50作者身份沿本会话FRC/FLC实际读缓存；正式sourceJSON绑定精确文件和阅读范围。目录与公式不作为未读内容的证明依据。
