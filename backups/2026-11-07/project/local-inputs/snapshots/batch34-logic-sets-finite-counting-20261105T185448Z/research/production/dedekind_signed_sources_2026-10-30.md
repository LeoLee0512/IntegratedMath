# 第24批全符号分割乘法来源审计 {#dedekind-signed-sources}

实际核验：2026-10-30T02:33:41.489872+00:00。代理 `/root/prepare22_build`；仅/tmp候选，不写正式仓库，不重新签发数学、教学、构建或视觉验收。

## 当前范围及先后边界

本批仅B2.27（SP1—SP4）与B2.28（SR1—SR4）。先前B2.25—B2.26非负乘积为已写先修；本次接续定义全符号乘法，证明符号、结合、有理相容、零积、全分配、各符号因子比较与非零消去，从而得到有序交换环。倒数、除法、有序域、实数根式与极限仍未建立。原23审计不改写；其当时的未来范围须结合当前独立审计阅读。

B2.27主属第526章97F50，交叉06A05；B2.28另交叉06F25“有序环、有序代数、有序模”。已实核taxonomy与中文映射，交叉不增加覆盖；预期49单元、406题答（392基础+14引论）、18图、25编号附录，仍5草稿章、29草稿叶、0完成章。

## 实际缓存复核、作者及许可

本次实际读取并重算八份缓存SHA-256及字节数，均匹配原记录；没有新网络请求。原五次2026-10-29、三次2026-10-30 01:47抓取时间和HTTP状态按原日志保留。JSON完整保留原来源对象，历史reused_cached_bytes不冒充本次抓取状态；本次八项均复用。

四份mathlib数学源码第4行Authors均逐项核实；许可为Apache 2.0。Dedekind作品作者与Beman英译者由元数据第16、5行确认；Project Gutenberg是许可发布者，不把作品作者误列为许可文字作者。元数据仅称美国公有领域，另有PG及所在地法律条件；未作全球公有领域承诺。

| 来源 | 作者或角色 | 原抓取UTC | 字节数 | SHA-256 |
|---|---|---|---:|---|
| mathlib_field_basic | Robert Y. Lewis; Leonardo de Moura; Mario Carneiro; Floris van Doorn | 2026-10-29T19:52:19.119904+00:00 | 31120 | `7a0a7285fa3a0adad6ffeaae3dc254d68d1cb8573b0932507178b2ea111d8197` |
| mathlib_license | mathlib contributors | 2026-10-29T17:29:06.420671+00:00 | 11357 | `b40930bbcf80744c86c46a12bc9da056641d722716c378f5659b9e555ef833e1` |
| dedekind_tex | Richard Dedekind; English translator Wooster Woodruff Beman | 2026-10-29T19:51:08.612324+00:00 | 243143 | `f837b8376cbbfca11690cea3bc0fac14fffecb88ae669e4f15158f096c915f44` |
| dedekind_license | Project Gutenberg (license publisher; no individual license-text author asserted) | 2026-10-29T19:51:08.612777+00:00 | 17504 | `1e301e03fb28addf6ad03d42b1429e87679013d1ee7e141c7c968fbef0ad961d` |
| dedekind_metadata | Richard Dedekind; English translator Wooster Woodruff Beman | 2026-10-29T19:52:19.458448+00:00 | 1216 | `fa7d92b7841e4b84a3ce2c7f603a17c37b74afe5112aa868e1520c17ebd147f2` |
| mathlib_ring_defs | Jeremy Avigad; Leonardo de Moura; Floris van Doorn; Yury Kudryashov; Neil Strickland | 2026-10-30T01:47:32.455340+00:00 | 14951 | `862a43694ab1713c95776f08634b9bd4697536c76ee80aa26127caadb6e30c72` |
| mathlib_order_ring_defs | Jeremy Avigad; Leonardo de Moura; Mario Carneiro; Yaël Dillies; Yuyang Zhao | 2026-10-30T01:47:32.782039+00:00 | 19592 | `ce16d26f079c7ec0323d98c20d1a8d078a758b230d673abb4f6641ee93192bfd` |
| mathlib_order_ring_basic | Jeremy Avigad; Robert Y. Lewis | 2026-10-30T01:47:33.144381+00:00 | 9056 | `e974bbf6c2d1385964f9aae9dda7959b528c3c93ba58cd6c9b6c6b25bdb8488c` |

mathlib固定版本v4.24.0；历史译本固定提交 `7a0bcaf5e279121cb675058d7e323556343087d0`。完整URL、缓存位置及原许可字段保存在JSON。1872是原作年代，2007-04-08是Gutenberg电子版发布日，不混为一次出版。

## 实际定位与条件区别

- **mathlib_ring_defs，行59–96, 116–143, 375**：Distrib requires both quantified distributive laws; semiring/ring/commutative ring names bundle stated obligations. NP/NL/SP/SR must prove these cut operations separately before using the structure names; full distributivity is only reached in B2.28.

- **mathlib_ring_defs，行308–327**：Within an already assumed NonUnitalNonAssocRing, neg_mul and mul_neg are derived using distributivity; mul_sub/add_sub identities then follow. This dependency cannot be imported for SP2: our signs are first verified directly from the cut sign definition; full distributivity is later proved using these signs. Only after SR2 may the difference identities be used.

- **mathlib_order_ring_defs，行115–137**：Nonnegative factors preserve weak order; positive factors preserve strict order. An algebraic semiring and ordered addition are prior assumptions. SR3 conditions comparison: use already established SR2 ring and additive order; preserve nonnegative/positive/negative/zero distinctions.

- **mathlib_order_ring_defs，行147–161**：IsOrderedRing.of_mul_nonneg and IsStrictOrderedRing.of_mul_pos derive order multiplication from positivity of a difference product, assuming Ring. Use as dependency comparison. The actual book SR3 calculation must explicitly invoke earlier SR2 distribution and DG4 difference order; no circular use of an abstract ring before SR2.

- **mathlib_order_ring_basic，行1–29**：Basic ordered-ring lemmas start with existing algebra and order assumptions; IsSquare.nonneg assumes Semiring, LinearOrder and monotone multiplication. Reviewed only to reject it as a construction source or proof of missing cut roots. No theorem from this file is needed by the four planned units.

- **mathlib_field_basic，行23–25,132–134**：Midpoint inequalities under existing ordered-field/semifield assumptions. Prior Q midpoint evidence only, not an assumption of an ordered field on cuts or a new SP/SR lemma.

- **dedekind_tex，行1006–1062,1080–1090**：Part I §VI gives addition and says other elementary operations can be defined; distributivity is discussed through continuity rather than supplying this plan’s modern strict one-sided cut proof. Historical attribution only. Do not attribute our P formula, zero branch, common witness, signed distributivity or rational reciprocal proof to an exact passage not found. These are independent book derivations.

mathlib在已有环内用分配推出取反乘积；本书SP2先由四支定义证明取反，再用它证明SR1—SR2，因此不能照搬库中相反依赖顺序。历史VI节只详细处理加法并说明其他运算、连续性路线，没有直接给出本书单侧分割的四支、标签表与异号分配证明。不伪造逐行历史出处，不移植外部证明、习题或代码。

## 当前SP/SR逐项义务

- **SP1** `#cutsigned-definition`：四个互斥穷尽的符号区域定义R×R到R的乘法。P只接收非负分割，N在全部分割定义；负输入取反后为正。逐支闭合，并以实际有理子集展开负支，不借代表选择或已有域结构。

- **SP2** `#cutsigned-signs`：分别证明两位置零乘、四支交换和单位；非零分割唯一正幅度及二值标签。由四支定义及取反自反证明单次取反与双负乘积，零另证；不借尚未证明的全分配律。

- **SP3** `#cutsigned-associative`：三处零输入各自处理；非零输入的中间幅度仍正，任意正幅度的结合来自NL2。八行标签表穷尽三个二值标签，连同一般幅度证明全称结合，不把有限数值抽样当证明。

- **SP4** `#cutsigned-rational-zero`：先处理零，再四种有理符号组合，以NP4和取反嵌入相容还原有理乘积。证明零积双向：两个非零输入的积由符号及正幅度不为零；此结论不构造倒数。

- **SR1** `#cutring-distributive-nonnegative-factor`：固定非负共同因子。同非负用NL3，同非正用取反乘积及和取反。异号以Y≤X或X<Y分支，先从加法群构造D=X−Y≥0或E=Y−X>0并证明加法分解，再用NL3和加法消去。相等幅度及零因子均覆盖，另一加项顺序显式交换；不提前用乘法差式。

- **SR2** `#cutring-distributive`：负共同因子先取正幅度K=N(C)，用已证SP2把SR1推出任意因子分配；交换得到另一侧。只有此后展开加法差定义证明两侧乘法差式，并汇总闭合、加法交换群、乘法结合单位与全分配命名交换环。0不等于1另由有理保序嵌入。

- **SR3** `#cutring-multiplication-order`：任意A,B取非负或正差D=B−A，只有D与非负C送入P。SR2差乘和已有差序判据给弱或严格保持；全序与严格保持给正因子反射，负因子经N反序单列双向条件，零因子排除严格保持和反射；左因子版本用交换。此后才汇总有序交换环。

- **SR4** `#cutring-cancellation`：非零C分正负用比较反射证明消去；另一路在SR2后用乘积差为零、SP4零积及加法消去。零因子反例及相等反向齐全；固定非零C的R→R乘法映射闭合且单射，不由唯一性推满射或倒数存在。

## 当前稿件与实际审阅报告绑定

以下四稿哈希均实际重算，数学报告分别由 `/root/review22`、`/root/plan_multiplication` 署名，教学报告由 `/root/visual21_front` 署名，报告含各自所审当前稿哈希。这里只记录它们的实际范围，不冒称本代理重新全文数学审查或签发新通过。原计划27/28当时为后续规划，当前已进入本批；倒数仍是未来。

| 文件 | SHA-256 |
|---|---|
| `/tmp/dedekind_signed_product.md` | `62211d16723a7ca83b2c38789191b265c74831a176bbca1afef4a0686cb07f09` |
| `/tmp/dedekind_signed_product_answers.md` | `35209f53753538d6308f25e4a65bdd2077717a74bde1e866b914635982ff42da` |
| `/tmp/dedekind_ring_order.md` | `e15922d9102ed98bddb4077a6b88cc0e74ebff9e2fe8bcbed3c6df493bdf8495` |
| `/tmp/dedekind_ring_order_answers.md` | `d7daa010c33e90fca79aaa55387d331b661071db20f0810bea00c5fe5b7ea807` |
| `/tmp/dedekind_signed_product_math_review.md` | `fe2283e93a2d73de984c6788f8ab6934fcb24313ccbc832eb8952dc05fab278d` |
| `/tmp/dedekind_ring_order_math_review.md` | `9b624a8bdec004a386eabc0ea77331b7e35a6141d07a0d79d4e52d9d2e8ed195` |
| `/tmp/dedekind_signed_pedagogy_review.md` | `3ab6c98d41c36d7428c851976dcfcd34b4faa4c9f2d88b72923ede1293a3548f` |
| `/tmp/dedekind_multiplication_plan.md` | `4c91fead6ca077a852c7f2621737ce5709dde48f55a4d408c180ddcf221751d1` |
| `/tmp/dedekind_multiplication_concept_review.md` | `766d1ef66c54d5f01db4d713ac945fcd3e0ea546387ab7223e9a884305d89cd1` |

## 整合边界

目前正式安装待root进行并逐字节核对。来源审计不绑定下游聚合构建或视觉结果，以免循环哈希。没有新图、数值模块、有限分割模拟或代码附录；全称成员与符号证明不声称给出任意分割成员判定算法。既有18图及附录一至二十五保留。完整原JSON对象以original_plan_source_record保存；原来源MD/JSON哈希也保留，未覆盖23审计。

## 主编正式安装复核

2026-10-30T02:36:28.461193+00:00，/root实际核四稿、三份真实署名审读报告及两份既有规划与正式文件逐字节一致，八缓存再次核SHA和大小。三工具从已核基线安装，独立来源锚及49/406/18/25结构在候选组装中通过；正式构建和页面尚待验收。上文/tmp候选状态保留为原审计历史，本节记录已完成安装；未把下游验收嵌入来源哈希。
