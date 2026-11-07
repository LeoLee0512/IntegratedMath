# B3.2 集合包含、相等与有限次集合运算计划

日期2026-11-05。作者`/root/part1_pedagogy`。主代理已授权原创两稿；不注册第33批、不改第一部分或B3.1冻结稿、台账与accepted。本计划承接PRODUCTION_PLAN及whole_book_route_checkpoint_2026-11-05的B3有限路线，不宣称补完公理集合论。

## 分类、稿件与限定目标

已核原MSC及章节顺序：主归第8章03Exx“集合论”的03E20（Other classical set theory, including functions, relations, and set algebra），交叉第525章97E60（Sets, relations, set theory, educational aspects）。沿原分类，不新造章号，保持章和叶partial。稿件为manuscript/foundations/sets_inclusion_operations.md与manuscript/foundations/sets_inclusion_operations_answers.md，八题独立全解；预计正文14—22页，答案另计。

“有限次运算”指二元交、并、差及有限个嵌套，不要求所论集合自身都是有限集。只用已给工作全集U及其子集A,B,C，允许U为空；不把U说成所有对象总集合。它是B3.1非空背景对象域里的一个限制集合，可以为空，两层角色不混同。交、并、差都由U内条件子集取得，不调用任意概括或任意并/幂集存在；不展开无穷集合族运算、基数、选择公理、关系理论或悖论导读。

采用身份保持：集合成员、按元素判等的外延原则、明确有限集合/已有数集以及从给定集合按明确条件取子集沿fun-sets公开采用。本单元证明的是在这些背景及B3.1经典语义下的包含和集合恒等式，不是从无集合背景证明外延或子集存在，也不是自然数ZFC构造。

## 精确先修

- functions_definition.md#fun-sets：成员/子集/空集/外延相等/条件子集；#fun-pairs只用于辨认对象，不新增有序对证明。
- natural_numbers.md#b1-peano-rules：有限例中0—5的名字与不同，不用新的数系性质。
- logic_connectives_quantifiers.md#lcq-conventions/#lcq-connectives/#lcq-equivalence/#lcq-inference/#lcq-quantifiers/#lcq-scope-negation：已写的经典二值、且/包容或/条件、德摩根、前提保真、限定量词、否定和空域。B3.1当前已独立文本审读，未注册/未构建，不冒称已完成PDF。

## 目标、锚点与证明义务

1. sio-background：工作全集及采用背景；成员陈述x∈A、包含陈述A⊆B与集合值A∩B区分。外延是采用的判等原则，不是新定理。
2. sio-inclusion（SI1）：A⊆B写为∀x∈A(x∈B)；否定为一个x∈A且x∉B的见证；双向包含判等。重写反身/传递的任意输入证明，空集不偷偷取成员。
3. sio-operations：A∩B、A∪B、A\B为已给U中的条件子集；相对补C_U(A)=U\A，写下标直到固定。并允许重叠，不是排他或。有限例逐成员核，差一般不交换。
4. sio-element-method（SI2）：用两个包含证明A∩B⊆A、A⊆A∪B、A∪∅=A、A∩U=A及双补C_U(C_U(A))=A；比较对象都在相同U内。未列出的集合运算法则不只挂名称。
5. sio-distribution（SI3）：两条分配律均完整两向。交对并逐或分支；并对交反向先按x∈A或x∉A分情况，明确使用经典二值，不暗引未证逻辑分配律。
6. sio-demorgan（SI4）：同一固定U下两条德摩根逐成员两向，第二条用LQ1¬(P∧Q)等价于¬P∨¬Q。每次从“非成员”组成补集都保留x∈U。U空时各集合必空，公式仍真。
7. sio-universe：U改变补集可变；混用两个全集的补集不能套同一德摩根。若U⊆V且A⊆U，用成员证明U\A=U∩(V\A)。不把符号“补”当成没有背景的绝对对象。

## 八题与全解要求

| 题锚 | 任务 | 核验义务 |
|---|---|---|
| sio-q01/a01 | 成员/子集、两有限集合的包含与反例、∅和{∅} | 逐对象说明，不能凭空集无成员否定其为元素；不预设自然数为集合或非集合 |
| sio-q02/a02 | U={0,1,2,3,4,5}, A={0,2,5}, B={1,2,4}, C={0,4,5}的交并差补和嵌套 | 逐项算成员，差不交换，A\(B∪C)=∅及(A\B)∩C={0,5} |
| sio-q03/a03 | A⊆B与A∩B=A、A∪B=B的等价 | 四个方向逐元素，空A/B同样成立，不能只从A∩B⊆A倒推出等号 |
| sio-q04/a04 | 并对交分配完整两向；删漏A因子的错误公式 | 同时在两并内且不在A时推出在B,C；给A=B=∅、C单点否定A∩(B∪C)=(A∩B)∪C |
| sio-q05/a05 | 同全集两条德摩根及空U | 每次保留域，分支穷尽，两包含均写，U空不取虚构元素 |
| sio-q06/a06 | 差对并/交的两公式 | A\(B∪C)=(A\B)∩(A\C)、A\(B∩C)=(A\B)∪(A\C)的成员等价链；A条件不能漏 |
| sio-q07/a07 | 包含的交并保留及补反向 | A⊆B推出交/并包含与C_U(B)⊆C_U(A)；用C=∅、A单点、B空反驳由交的包含倒推A⊆B |
| sio-q08/a08 | 两全集比较与错误混用 | U={0,1}, V={0,1,2}, A={0}算补并给混用德摩根反例；一般U⊆V、A⊆U证明U\A=U∩(V\A) |

## 来源实读与真实访问历史

遵从不重试API域：本任务未访问api.github.com。初始四个旧/候选原生路径sec_intro-sets.ptx、sec_sets-basics.ptx、ch_sets.ptx、main.ptx均404，均保留响应身份而不当正文。随后正常公开原生README.md给project.ptx入口，manifest给source/dmoi.ptx，实际主文件明确4th Edition并指向ch_structures.ptx，该章包含sec_structures-sets.ptx。沿这些实际文件引用HTTP200取得真实集合节，未镜像、未绕过访问限制。

真实数学来源：https://raw.githubusercontent.com/oscarlevin/discrete-book/master/source/sec_structures-sets.ptx ，42971字节，SHA 0d525f026c14b828c16a7e4534dbe7df0bed77919456262d31a088eb643c8af7。实际读1—130、190—294、614—884、885—1030行，覆盖集合/成员/外延、限定集合写法、包含/空集、并交及背景相关补/差。源文提及的幂集和基数段虽实际看过但不迁入本单元；XML注释中的“universe set of all elements”不作为活动正文或本书采用规则。正文保留既有⊆允许相等约定，不采用源书⊂/⊆的模糊措辞；不将源例中“数不是集合”的描述升级为本书数系构造公理。

源书该范围支持定义和典型操作说明，未核到与本书同一逐元素分配/德摩根证明；这两组证明依本书LQ接口原创完成，由独立数学/教学审读负责。许可证沿本次已实读的LICENSE及frontmatter缓存，第四版CC BY-NC-SA4.0，不套第三版许可。源书例题、答案及图不转载/翻译/改编。所有原生响应仅在被.gitignore忽略的local-inputs/b3-sets-source-cache，元数据另列sets_inclusion_operations_sources.json，不收入分发包。

作者完成后自检8对题答、内链、有限集合例和一般证明的条件；数学/教学独立签署后仍需另行构建和实际页面检查。当前计划不授予任何accepted或完整章状态。
