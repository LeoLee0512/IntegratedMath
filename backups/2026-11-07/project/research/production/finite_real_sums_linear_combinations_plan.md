# 有限实数和与有限坐标线性组合：拆分计划

2026-11-05，作者/root/part1_pedagogy，依据root明确授权。全在/tmp暂存，不安装或注册33/34冻结输入。本次先完成单元A；单元B待A独立审读与接口冻结后继续，避免未证实数和值成为隐含先修。两单元各8题完整独立答案，不引无限级数、任意重排、双重求和或抽象群。

## A：有限实数和

文件拟`finite_real_sums.md`与`finite_real_sums_answers.md`，锚rfs。主归第528章97H20初等代数教育的实数有限求和局部；服务第84章15A03的线性代数先修，不把单纯实数求和伪称已完成线性组合或向量空间。分类局部保持partial。

精确先修：b1-induction、b1-recursion-principle、b1-addition-definition、b1-add-one、b1-addition-associative；ord-successor-comparison、ord-trichotomy、ord-partial-order、ord-strict-equivalence、ord-addition-order、ord-cancellation、sub-definition；fun-pairs、fun-definition、fc-equality、sum-indices；实数cutadd-definition、cutgroup-laws、cutgroup-inverses、cutgroup-negation-subtraction、cutsigned-definition、cutsigned-signs、cutsigned-rational-zero、cutring-distributive；实数零定义cutadd-unit及有理嵌入cutadd-rational及旧sum-definition、sum-extensionality只为相容性比较。旧有理和公式不直接用作实数结论。

| 目标 | 拟锚 | 证明义务 |
|---|---|---|
| RFS1实数递归和 | rfs-definition | 固定u:N→R，以N×R和(0_N,0_R)为状态；T(k,s)=(k+1,s+u_k)是唯一固定自映射；递归存在唯一F；归纳第一坐标k正确；第二坐标S_n^R满足空0/后继加；另归纳候选部分和唯一。 |
| RFS2前缀与有限表 | rfs-prefix-table | 对n归纳，性质量化所有u,v前n项一致；零延拓a:I_n→R合法，n0无a0；定义Sum_R(a)，任何延拓同前n和。 |
| RFS3逐项规则 | rfs-linearity | 单独归纳逐项加法/固定实数缩放；四加数用六行结合交换展开而非任意重排；传回同长有限表时核零延拓或前缀；取反/差为推论。 |
| RFS4连续拼接 | rfs-concatenation | 移位u^[m]_j=u_(m+j)，固定m/u对n归纳；有限a:I_m/b:I_n拼接检查前后域不交、m+j唯一、j=i−m仅m≤i时存在，并反映j<n；由前缀识别两段。 |
| RFS5补零与空边界 | rfs-padding | 归纳全零前n和为0；拼接零表保和但不同长记录仍不同；和零不能推出空表或逐项零。 |
| RFS6有理嵌入相容 | rfs-rational-compatibility | i:Q→R；对有理序列q归纳S_n^R(i∘q)=i(S_n^Q(q))，空和i(0)=0、后继保加；对有限q用零延拓且i(0)=0逐点核延拓相容。 |

八题固定范围：1任意实参数表(r+1,−r,2)的状态/空和/单项；2固定更新不能漏步数及零延拓合法性；3前缀相同仅要求范围内，归纳与不同尾部例；4一般逐项加法/缩放独立全证与零负标量；5具体两表拼接及自然差索引一般核；6补零/和零反例并证明全零表和；7有理有限表嵌入全归纳及精确分数例；8逐项乘积之和不等于两和值相乘的反例及正确二项四项展开，区分已证分配与未证任意重排。原题原创，答案逐题独立完整。

## B：有限坐标向量线性组合（后续接口计划）

依赖A全部已证接口及FRC1–5；明确n为坐标数、m为向量项数。给表v:I_m→V_n和实系数表a:I_m→R，定义输出向量w∈V_n，w_j=Sum_R(k↦a_k(v_k)_j)。每个j所得是长度m实数表，检查规则唯一，m0输出0_n，n0输出唯一空向量，两个零参数不可混淆。仅通过有限实数和的逐项规则逐坐标证明系数相加、共同缩放、向量项逐点相加和连续拼接；不定义基/张成/线性相关或矩阵，不假设换序/重排。不把位置数当维数。

八题候选：1两实坐标向量具体组合；2m0/n0与错类型；3系数可加逐点全证；4共同缩放及零系数；5各项向量相加全证；6连续拼接与两种索引角色；7非唯一系数表示反例（仅具体计算，不定义线性相关）；8固定坐标重编号保持组合（逐j用FRC5及A，且不调向量项次序）。正式写B时须再固定题目和源内容，不把本计划当正文或验收。

## 实际来源核读与原创边界

作者本次实际读既有Lebl固定版ch-seq-ser缓存3000–3060、3302–3387：前段在级数背景内写有限部分和定义，后段直接列有限部分和的缩放与逐项加法等式，也提示有限和不能逐项相乘得到和值积；题8使用独立数值与完整原创解释。仅采用这些有限表达的术语与公式核对，不导入任何无限级数/极限论证；源文不提供本书所需固定状态递归、零延拓、零起索引与全归纳证明。上述新增证明与8题独立原创。已完整读该缓存LICENSE的CC BY-SA4.0/CC BY-NC-SA4.0双许可，固定公开URL和哈希将另记作者source JSON；无新网络请求。B可另核Beezer有限线性组合具体段，未找到和读过前不预写来源已核。
