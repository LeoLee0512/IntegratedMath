# 第25批分割倒数与除法来源审计 {#dedekind-inverse-sources}

实际复核：2026-10-30T02:46:28.825523+00:00，代理 `/root/prepare22_build`。仅/tmp。现已核最终四稿与三份实际审阅报告的字节及对应哈希；本审计不重新签发数学、教学、构建或视觉验收。

## 当前范围和构造顺序

先证明正倒数候选四条件及正逆元存在，再扩展非零倒数与唯一性，最后定义非零分母商、证明方程全参数分类与商比较，才能汇总有序域。同一分割集合及包含序上的旧DC4上确界性质，才给本书采用的Dedekind完备性。正倒数的ε见证证明不以该完备性为前提。当前稿件实际承担以下义务，既有独立审阅报告另列；本审计只绑定报告而不代签新的证明通过。

本书Inv只定义于非零子集，商只接受非零分母。mathlib的inv_zero=0是其全域符号约定，不意味着零有乘法逆元；本书不采用此额外约定。源码中非零逆元律的a≠0条件仍须逐项保留。

## 缓存、历史、署名与许可

实际重算十份原缓存SHA-256与字节数，全部一致；另核已有lebl_front署名版本证据。原三次新抓取仍为2026-10-30 02:26，七项旧记录仍为2026-10-29；本代理本次无网络请求。完整原来源JSON对象原样保存在original_plan_source_record，不覆盖23/24来源。

四份mathlib数学源码Authors均实际核第4行。Lebl前言第289行署名、382行version6.3及401行版权声明实际读取；对应缓存与原HTTP200抓取保留。PG许可发布者为Project Gutenberg，Dedekind/Beman只为作品作者/译者；原不准确许可作者字段留档并修正当前角色。

mathlib适用Apache2.0；Lebl许可证实际列CC-BY-SA-4.0与CC-BY-NC-SA-4.0双许可；Dedekind元数据仅称美国公有领域，另保留PG与所在地条件。仅对照数学事实、历史与结构义务，没有复制外部证明文字、题目、插图或代码。

| 来源 | 原抓取UTC | 字节数 | SHA-256 |
|---|---|---:|---|
| mathlib_field_basic | 2026-10-29T19:52:19.119904+00:00 | 31120 | `7a0a7285fa3a0adad6ffeaae3dc254d68d1cb8573b0932507178b2ea111d8197` |
| mathlib_license | 2026-10-29T17:29:06.420671+00:00 | 11357 | `b40930bbcf80744c86c46a12bc9da056641d722716c378f5659b9e555ef833e1` |
| dedekind_tex | 2026-10-29T19:51:08.612324+00:00 | 243143 | `f837b8376cbbfca11690cea3bc0fac14fffecb88ae669e4f15158f096c915f44` |
| dedekind_license | 2026-10-29T19:51:08.612777+00:00 | 17504 | `1e301e03fb28addf6ad03d42b1429e87679013d1ee7e141c7c968fbef0ad961d` |
| dedekind_metadata | 2026-10-29T19:52:19.458448+00:00 | 1216 | `fa7d92b7841e4b84a3ce2c7f603a17c37b74afe5112aa868e1520c17ebd147f2` |
| lebl_reals | 2026-10-29T19:51:08.613314+00:00 | 80337 | `d492090591013b5845ddfa48f7dc0f15500180bf04aa8a0af10dd7d3919f01a3` |
| lebl_license | 2026-10-29T19:51:08.949458+00:00 | 467 | `682fedaab34d7d47962da7276284e608f43881c07c3c887cb66368688748c13d` |
| mathlib_field_defs | 2026-10-30T02:26:34.910028+00:00 | 10439 | `8fc4e2e1a3464f05fa92bc4f6d31daece2f70a508f1094e5fda3c21957dac151` |
| mathlib_groupzero_defs | 2026-10-30T02:26:35.180309+00:00 | 13280 | `3a89c91ad2f605c40378e23926fe4046668b6a1d5a00109f6472397d948ce00e` |
| mathlib_order_field_defs | 2026-10-30T02:26:35.455785+00:00 | 1508 | `8af25639e0ca0a462258eec35ea35ce97f629cc9e17b1dfc70790f78d443a3f3` |

补充署名缓存 `lebl_front`：SHA-256 `a355edf1ff287d98d13bfc50fa9cfcd541b42b8210f0172dfb5dadafb58a47ee`，原抓取 2026-10-29T19:51:54.424412+00:00。mathlib固定v4.24.0；Lebl固定提交 `e21ec524ca7d54f800c693b948020c188d21d01f`；Dedekind固定提交 `7a0bcaf5e279121cb675058d7e323556343087d0`。完整URL/署名/许可/缓存路径在JSON。

## 实际源码定位与条件

- **mathlib_field_defs，行102–117,166–176**：DivisionRing requires nontrivial ring and inverse law for nonzero inputs; it also imposes totalized inv_zero=0. Field extends CommRing and DivisionRing. IR3 must construct each nonzero cut inverse and prove the identity before DQ4 names a field. Book Inv has domain R^× and does not adopt totalized zero inversion or division. Source inv_zero is a convention, not 0·0=1.

- **mathlib_groupzero_defs，行197–219,242–250**：GroupWithZero includes a total inverse with inv_zero=0, and mul_inv_cancel only under a≠0. Multiplication/division cancellation lemmas explicitly preserve nonzero hypotheses. Use as a definition/condition comparison only. IR3 and DQ1/2 write all domain/nonzero checks and prove identities with cut associativity. Do not import a GroupWithZero instance before providing inverse witnesses.

- **mathlib_order_field_defs，行11–16,26–36**：Ordered-field obligations: ordered addition, positive products and 0<1; old combined structures are deprecated in this tag in favor of separate Field/LinearOrder/IsStrictOrderedRing assumptions. DQ4 lists proved cut field and order obligations. Do not infer any missing inverse existence from an order structure. No Lean instance or compilation claimed.

- **mathlib_field_basic，行23–25,73–93,132–134**：Existing ordered semifield assumptions precede positive reciprocal order statements and midpoint inequalities. IR1/2 use only Q, whose corresponding arithmetic has already been proved. DQ3 reciprocal order for cuts comes later from constructed inverses and SR3, not from these field-assuming source lemmas.

- **lebl_reals，行121–130**：Least-upper-bound property requires every nonempty upper-bounded subset to have a least upper bound; called Dedekind completeness. DQ4 explicitly uses this meaning only and preserves both nonempty and bounded hypotheses; no Cauchy completeness or uniqueness theorem is thereby supplied.

- **lebl_reals，行165–234,249–262**：Field axiom list includes 1≠0, nonzero inverse existence, and distributivity; ordered field adds ordered translation and positive product. Source begins axiomatically; book must prove IR2/3 rather than assume source M5. Use as precise structure checklist after cut construction.

- **dedekind_tex，行1047–1062**：Historical §VI says quotients and other elementary operations can be defined, without giving this strict one-sided positive outer-point reciprocal and complete ε witness proof. History only. I(A), ε=a0(1−q) and q=0 case are independent book derivations, not claimed quotations or externally supplied full proofs.

Lebl原文开头明说假定具有正确性质的实数集存在，不能用其域公理M5跳过本书IR2/IR3存在性证明。历史VI节没有直接给出本书严格单侧正外点倒数与完整ε反向包含；未找到同版现成完整证明，不虚构该出处。

## 当前IR/DQ义务

- **IR1** `#cutinv-positive-definition`：Only A>0: I(A) consists of rational q below1/r for a positive rational exterior r. Positive exterior witnesses place all q≤0 inside; a positive interior a0 gives exterior1/a0 using a0<r. Prove downward closure and no greatest member with rational midpoints, then positivity and positive-domain function closure.

- **IR2** `#cutinv-positive-inverse`：Prove both member inclusions P(A,I(A))=i(1). Reverse q<0 uses P negative branch; for0≤q<1 choose ε=a0(1−q)>0 and DA1 u∈A,v∉A with gap<ε. Interior/exterior separation gives v>a0>0, not u≥a0. Strict chain gives u>qv≥0, includingq=0; rational b betweenq/u and1/v supplies legal positive product witnesses. No cut inverse, real Archimedean theorem, limit or supremum is assumed.

- **IR3** `#cutinv-signed-unique`：Inv defined only on nonzero cuts. Negative branch N(I(N(A))) has legal positive I input and is negative; positive branch positive. Prove both inverse products, then uniqueness from associativity and an already constructed inverse. Zero has no inverse because0≠1; do not import a totalized inv_zero convention.

- **IR4** `#cutinv-rational-identities`：Use rational inverse identity and SP4 before uniqueness to obtain Inv(i(r))=i(1/r), onlyr≠0. Check each domain for inverse of1, inverse of inverse and inverse of negation. Examples do not replace all-cut proof.

- **DQ1** `#cutdiv-definition`：Define quotient onlyR×R_nonzero→R as A⊗Inv(B). Derive both multiplication-back identities explicitly from inverse/associativity, handle zero numerator, prohibit zero denominator, and prove rational compatibility fors≠0.

- **DQ2** `#cutdiv-equations`：Declare solution sets with candidate domainR and R-valued sides. ForC⊗X=D, prove existence and necessity whenC≠0 and both coefficient-zero branches(allR or empty). Show actual two-sided inverse of fixed nonzero multiplication map, then affine equation reduction and its three parameter branches.

- **DQ3** `#cutdiv-order`：Only nonzero denominators: Inv(C) has the same sign, so apply priorSR3 to explicit quotient definitions, with full weak/strict two-way positive and negative chains. For positiveA,B, a positive common inverse product yields reciprocal reversal; do not claim uniform reversal acrosszero. Division byzero remains undefined.

- **DQ4** `#cutdiv-complete-field`：AfterIR3 exists, match all nontrivial commutative-ring and inverse obligations before naming a field; retain same cut set and inclusion order for ordered-field laws. Completeness means exactly existingDC4 nonempty bounded-above subset supremum as union, with conditions and rational member formula explicit. No Cauchy equivalence, uniqueness isomorphism, root existence, real Archimedean theorem or limits is implied.

## 分类及后续绑定

12J15在正式taxonomy为Ordered fields、中文映射为“有序域”。当前四稿及实际独立报告现已绑定；B2.30据此增加12J15交叉定位，B2.29仅交叉06A05/06F25。主归属仍第526章97F50，不把交叉叶记为写成。预计51单元422题答（408基础+14引论），18图25附录，仍5草稿章29草稿叶0完成章。

最终四稿、概念报告及数学/教学报告的实际字节与各自范围已在下表绑定。正式安装仍待root核验。没有新增数值模块、有限分割模拟或绘图；不声称任意分割成员可判定。最终构建和视觉证据另存，不绑定到来源审计形成循环哈希。


## 最终文本与实际报告绑定

实际核验：2026-10-30T02:54:14.151883+00:00。报告作者与范围按报告原文记载；不把候选绑定写成正式安装通过。

| 文件 | SHA-256 |
|---|---|
| `/tmp/dedekind_inverse.md` | `c44af9a30044a893e4bab3b94ce6a2bb3f949eabd64dd3d51b36fb7d7f76627a` |
| `/tmp/dedekind_inverse_answers.md` | `a95b6e48978c4c00c3d3269063555777764152515d205270aa0dd1a003f6cac3` |
| `/tmp/dedekind_division_field.md` | `f69f9304027ec15fbeb50ebddc1198e203d1676e7bd014b721f146aa9b1db610` |
| `/tmp/dedekind_division_field_answers.md` | `cd5b266feb27187daa74131d6a2484042729b401667aabf072ca1a8522f27dc1` |
| `/tmp/dedekind_inverse_math_review.md` | `82d114bb99c237c4d79cf62c973df3593aa6694018b4d659c9a534136e6fb08f` |
| `/tmp/dedekind_division_field_math_review.md` | `025f6c7ed0c884e74385ac00797d5785344887cb11e967900e4c869b6665e088` |
| `/tmp/dedekind_inverse_pedagogy_review.md` | `bfecfd659900f7f478244e5b8d6363d591ab43b71f8cfb6296396b52e470d2f6` |
| `/tmp/dedekind_inverse_plan.md` | `6570cc36c11365cc6dfa0eb8c76aeb4c2407edaedfef0ef6c18b5d04b88a7209` |
| `/tmp/dedekind_inverse_concept_review.md` | `84ebef24238f95d49a36be65ec98fff05e1acd3923a96ce8f8556e80c98df035` |

数学/教学报告范围：

- `review22`：Independent full B2.29 IR1–IR4 and all eight complete answers; final four prerequisite links rechecked。
- `/root/plan_multiplication`：Independent full B2.30 DQ1–DQ4 and all eight complete answers; final body and answer read in full。
- `/root/visual21_front`：Independent pedagogy and prerequisite review of both bodies and all sixteen complete answers; final links and object statement verified。

## 主编正式安装复核

2026-10-30T02:55:42.165386+00:00，/root实际核四稿、三份真实署名审读报告及两份规划与正式文件逐字节一致，十缓存再次核SHA和大小。三工具从第24批已核基线安装，独立来源锚及51/422/18/25结构在候选组装中通过；正式构建和页面尚待验收。上文/tmp候选状态保留为原审计历史，本节记录已完成安装；未把下游验收嵌入来源哈希。
