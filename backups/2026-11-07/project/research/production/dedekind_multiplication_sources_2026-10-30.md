# 第23批非负分割乘积来源候选

本次核验：2026-10-30T02:13:24.906428+00:00。审计补记仍只在 `/tmp` 准备；现已逐一核对root正式安装的四稿、三份实际审阅报告、两份计划/概念报告和三工具，与候选完全相同。这里不重新签发数学、教学、构建或视觉通过。

## 当前范围与原规划的区别

当前仅B2.25（NP1—NP4）及B2.26（NL1—NL4）：非负乘积、四条件闭合、零与正性、交换单位弱单调、有理相容、非负结合与两侧分配、正因子比较反射及消去。主属第526章97F50，交叉06A05。

原来源规划覆盖B2.25—B2.28并提及更后的倒数路线。B2.27—B2.28、有符号乘法、完整有符号环、倒数与域均只保留为未来边界，未收入当前两单元；原文中的“四单元”不能读成当前四份已完成正文。没有新增插图、数值代码或代码附录，全稿仍18图、附录编号止于二十五。

## 缓存、真实抓取历史及署名

实际读取八份原缓存字节，SHA-256与原字节数全部一致。三次新文件抓取的时间仍为2026-10-30 01:47，另五份复用记录保留2026-10-29时间；本次集成准备没有任何网络请求。原fetch.json及完整原JSON对象随本候选记录保留。

四份mathlib数学源码作者均实际核对第4行Authors声明；Dedekind作品作者与Beman译者核对元数据第16、5行。Project Gutenberg是许可发布者，Dedekind/Beman不是该许可文字的作者；原不准确作者角色在当前JSON中说明并保留原字段。mathlib Apache 2.0与历史作品美国公有领域、Project Gutenberg/所在地条件均未改变，未作全球公有领域声明。

| 来源 | 字节数 | SHA-256 |
|---|---:|---|
| mathlib_field_basic | 31120 | `7a0a7285fa3a0adad6ffeaae3dc254d68d1cb8573b0932507178b2ea111d8197` |
| mathlib_license | 11357 | `b40930bbcf80744c86c46a12bc9da056641d722716c378f5659b9e555ef833e1` |
| dedekind_tex | 243143 | `f837b8376cbbfca11690cea3bc0fac14fffecb88ae669e4f15158f096c915f44` |
| dedekind_license | 17504 | `1e301e03fb28addf6ad03d42b1429e87679013d1ee7e141c7c968fbef0ad961d` |
| dedekind_metadata | 1216 | `fa7d92b7841e4b84a3ce2c7f603a17c37b74afe5112aa868e1520c17ebd147f2` |
| mathlib_ring_defs | 14951 | `862a43694ab1713c95776f08634b9bd4697536c76ee80aa26127caadb6e30c72` |
| mathlib_order_ring_defs | 19592 | `ce16d26f079c7ec0323d98c20d1a8d078a758b230d673abb4f6641ee93192bfd` |
| mathlib_order_ring_basic | 9056 | `e974bbf6c2d1385964f9aae9dda7959b528c3c93ba58cd6c9b6c6b25bdb8488c` |

## 仅本批NP/NL的证明义务

- **NP1** `#cutprod-positive-witnesses`：Identify positive cuts through zero or a positive rational member; find positive exterior rationals and larger positive interior witnesses using only cut closure/order and Q.

- **NP2** `#cutprod-definition`：Define P on nonnegative cuts with an independent q<0 branch and positive internal product witnesses. Prove all four cut conditions, nonnegativity, both zero-factor positions, positive products and the zero-product alternative without inverses.

- **NP3** `#cutprod-basic-laws`：Prove commutation and unit by actual members; 1 is not in i(1), so use a midpoint between q/a and 1. Weak monotonicity inherits witnesses, with zero-factor counterexamples to unjustified strictness/reflection.

- **NP4** `#cutprod-rational`：For nonnegative rational endpoints separately handle zero; reverse principal-cut product inclusion uses two rational midpoints and legitimate positive divisions, no real square root or inverse.

- **NL1** `#cutprod-cofinal-witnesses`：Nonnegative sums and positive-summand positivity; positive inputs permit larger positive sum/product witnesses even when the given rational member is negative. Zero inputs need separate branches.

- **NL2** `#cutprod-associative`：Handle zero inputs and negative rational members, then expand both nested products into positive triple witnesses; construct intermediate positive members by rational midpoints in all reverse directions.

- **NL3** `#cutprod-distributive`：Handle all zero inputs; forward inclusion constructs an exact sum after positive witness enlargement. Reverse inclusion allows original sum members of either sign and uses a common max(a1,a2) member before rational distribution. Prove both sides.

- **NL4** `#cutprod-strict-order`：Only after NL3, use positive difference D=B⊖A and already-proved additive translation to prove strict monotonicity; total order gives reflection and positive-factor cancellation. No multiplicative surjectivity or inverse existence follows.

这里记录来源条件与正文证明义务，另绑定已有审阅报告；本来源审计不重新签发证明通过。已实际读取新缓存的结构声明、分配字段和有序乘法条件，以及历史VI节的相关段落；有序环源码假定既有半环/环，不能反过来成为当前构造的前提。`mathlib_order_ring_basic`只作为拒绝不当先修的边界记录。

## 当前冻结文本与既有审阅报告

实际核验时间：2026-10-30T02:16:00.989024+00:00。四稿逐项匹配root所给冻结哈希，两份数学报告各自含所审单元的当前正文/答案哈希，教学报告含全部四稿当前哈希。此处只绑定证据，不冒称本代理重新全文数学审稿或新签署通过。

| 文件 | 当前SHA-256 |
|---|---|
| `/tmp/dedekind_nonnegative_product.md` | `73e77200fa17f9c5cf8861b0655c3529075a8ce3d4c7dbe309db0527fd0f2be7` |
| `/tmp/dedekind_nonnegative_product_answers.md` | `2fbb1afebf2dd314fa065a92aaae326d13d2928d086b60daa2b9a30e0ed3d511` |
| `/tmp/dedekind_nonnegative_laws.md` | `7a9a8f60774bc3f950efd42be40cc875b6f2c0f698fc0488a1f9f9824cc27c3a` |
| `/tmp/dedekind_nonnegative_laws_answers.md` | `d7b17f64f3b95b0e8f3606536ffd9be9538d91ef5e8d127b7b69146b4db2346c` |
| `/tmp/dedekind_nonnegative_product_math_review.md` | `839e102818454424dfd7d856b991c5b951086374a708d7d6aeb26420383196bf` |
| `/tmp/dedekind_nonnegative_laws_math_review.md` | `579f64c2006f1c9ffde2210aec6d6f9762e207f450c851732faf89e9a3d88616` |
| `/tmp/dedekind_nonnegative_pedagogy_review.md` | `6878f972526436fcbecfcd7b6502570d058878d90b37372f62f95801b8005482` |
| `/tmp/dedekind_multiplication_plan.md` | `4c91fead6ca077a852c7f2621737ce5709dde48f55a4d408c180ddcf221751d1` |
| `/tmp/dedekind_multiplication_concept_review.md` | `766d1ef66c54d5f01db4d713ac945fcd3e0ea546387ab7223e9a884305d89cd1` |

数学报告署名分别为 `/root/review22`（独审NP）和 `/root/plan_multiplication`（独审NL）；教学报告由真实审阅者 `/root/visual21_front` 补明署名。已实际核对：仅增加该署名行及空行，逆向去除后复现先前报告哈希，四稿绑定与审核内容不变。报告范围与最终修订核对保留原文，不据此注册accepted或最终PDF通过。

## 正式安装后的实际只读核验

核验时间：2026-10-30T02:21:50.131657+00:00。root已安装的四稿、三份数学/教学报告与两份计划/概念报告逐字节匹配本审计原绑定；三工具逐字节匹配候选。正式来源JSON/MD也先与本次补记前的候选逐字节相同，原修订哈希另存JSON，以免误称本补记已经复制。没有修改任何正式文件，没有读取并绑定正在修改的README或LEARNING_PATH。

实际调用当前正式工具的 `compose_body()`，所有输入均为已安装文件；在内存组合字符串核得附录一至二十五的完整连续序列，新来源锚唯一，两新单元位于既有第526章续写，各8题及8解均有唯一锚、局部正反链接且全部答案在教学正文后。现有两份完整绘图函数仍出现在各自附录中，注册47单元和18图。此处未运行正式全构建、PDF渲染或书页目视，不冒称最终排版验收。

正式三工具SHA-256：

- `tools/build_production_ledger.py`：`0f77315a5fb90519137581f533d7ec520bfb7f4d6fe49579370fed57b290aced`。
- `tools/validate_learning_batch.py`：`7afaa857701f94b3e306e77fb39925c6cc74b7a5b930cddaa2e15c9061697360`。
- `tools/build_learning_batch.py`：`34726c98ce66b13bafb1641d97b84b3f38f1d547c875614b4290d65ed3ea0b01`。

## 最终集成待办

1. Root should copy this final supplemental source JSON/MD once more and verify identical bytes before build; then let the build input manifest bind the final audit bytes. All four manuscripts, five reviews/plans and three tools have already been checked against their candidates.

2. Preserve original eight-source fetch/cache history and B2.27/B2.28/reciprocal future-only scope. No signed multiplication or full ring/field coverage is registered by this batch.

3. No new image, numerical module, mirror tester or numbered appendix is required. Existing 18 figures and 25 numbered appendices stay registered.

4. Production build, automatic validator and final PDF page reviews remain separate downstream work. No aggregate acceptance/report hash is embedded in this source audit; later audit byte changes require rebuild/validation.

## 原规划来源核验全文（历史记录，原文保留）

# 分割乘法来源核验（第23、24批规划） {#dedekind-multiplication-sources}

核验：2026-10-30T01:54:44.561126+00:00。仅/tmp，当前为计划来源证据，不是正文或审校通过。

Runtime skill and networking read; enforced restricted policy inspected; normal inherited proxy to permitted raw.githubusercontent.com only; no login or access circumvention

## 来源角色与权利

仅核公开合法来源。数学公式与证明义务作事实对照；正文、例题、练习及教学证明独立撰写，不复制外部证明文字、题目或Lean代码。mathlib为Apache-2.0；历史Dedekind元数据仅标美国公有领域，另有Project Gutenberg许可及本地法律条件，未声称全球公有领域。没有Lean编译。

本文未在已检查来源中找到一份与本书严格单侧分割定义完全一致、覆盖全部四单元的完整现成乘法证明；不伪造该来源。以下记录历史依据、抽象义务和条件差异，具体见证证明由本书独立推导并另做独立数学审读。

### mathlib_field_basic

Robert Y. Lewis; Leonardo de Moura; Mario Carneiro; Floris van Doorn；Algebra/Order/Field/Basic.lean；mathlib v4.24.0 (public tagged source; checked text only, no Lean compilation)。

https://raw.githubusercontent.com/leanprover-community/mathlib4/v4.24.0/Mathlib/Algebra/Order/Field/Basic.lean

许可：Apache-2.0; source file notice and reused fixed-tag LICENSE inspected。

访问：verified_http_200；原抓取2026-10-29T19:52:19.119904+00:00；本批复用缓存：True。

SHA-256：`7a0a7285fa3a0adad6ffeaae3dc254d68d1cb8573b0932507178b2ea111d8197`；31120字节。

缓存：`/tmp/rational-gaps-cuts-source-audit/mathlib_field_basic`。

### mathlib_license

mathlib contributors；mathlib LICENSE；mathlib v4.24.0 (public tagged source; checked text only, no Lean compilation)。

https://raw.githubusercontent.com/leanprover-community/mathlib4/v4.24.0/LICENSE

许可：Apache-2.0。

访问：verified_http_200；原抓取2026-10-29T17:29:06.420671+00:00；本批复用缓存：True。

SHA-256：`b40930bbcf80744c86c46a12bc9da056641d722716c378f5659b9e555ef833e1`；11357字节。

缓存：`/tmp/powers-polynomials-source-audit/mathlib_license`。

### dedekind_tex

Richard Dedekind; English translator Wooster Woodruff Beman；Essays on the Theory of Numbers, Part I: Continuity and Irrational Numbers；Gutenberg ebook 21016 released 2007-04-08; GITenberg commit 7a0bcaf5e279121cb675058d7e323556343087d0。

https://raw.githubusercontent.com/GITenberg/Essays-on-the-Theory-of-Numbers_21016/7a0bcaf5e279121cb675058d7e323556343087d0/21016-t/21016-t.tex

许可：Metadata states Public domain in the USA; Project Gutenberg license and local-law caveat apply; no global public-domain claim。

访问：verified_http_200；原抓取2026-10-29T19:51:08.612324+00:00；本批复用缓存：True。

SHA-256：`f837b8376cbbfca11690cea3bc0fac14fffecb88ae669e4f15158f096c915f44`；243143字节。

缓存：`/tmp/rational-gaps-cuts-source-audit/dedekind_tex`。

### dedekind_license

Richard Dedekind; English translator Wooster Woodruff Beman；Project Gutenberg License；Gutenberg ebook 21016 released 2007-04-08; GITenberg commit 7a0bcaf5e279121cb675058d7e323556343087d0。

https://raw.githubusercontent.com/GITenberg/Essays-on-the-Theory-of-Numbers_21016/7a0bcaf5e279121cb675058d7e323556343087d0/LICENSE

许可：Metadata states Public domain in the USA; Project Gutenberg license and local-law caveat apply; no global public-domain claim。

访问：verified_http_200；原抓取2026-10-29T19:51:08.612777+00:00；本批复用缓存：True。

SHA-256：`1e301e03fb28addf6ad03d42b1429e87679013d1ee7e141c7c968fbef0ad961d`；17504字节。

缓存：`/tmp/rational-gaps-cuts-source-audit/dedekind_license`。

### dedekind_metadata

Richard Dedekind; English translator Wooster Woodruff Beman；GITenberg metadata.yaml；Gutenberg ebook 21016 released 2007-04-08; GITenberg commit 7a0bcaf5e279121cb675058d7e323556343087d0。

https://raw.githubusercontent.com/GITenberg/Essays-on-the-Theory-of-Numbers_21016/7a0bcaf5e279121cb675058d7e323556343087d0/metadata.yaml

许可：Metadata states Public domain in the USA; Project Gutenberg license and local-law caveat apply; no global public-domain claim。

访问：verified_http_200；原抓取2026-10-29T19:52:19.458448+00:00；本批复用缓存：True。

SHA-256：`fa7d92b7841e4b84a3ce2c7f603a17c37b74afe5112aa868e1520c17ebd147f2`；1216字节。

缓存：`/tmp/rational-gaps-cuts-source-audit/dedekind_metadata`。

### mathlib_ring_defs

Jeremy Avigad; Leonardo de Moura; Floris van Doorn; Yury Kudryashov; Neil Strickland；Mathlib/Algebra/Ring/Defs.lean；mathlib v4.24.0, textual source only, no Lean compilation。

https://raw.githubusercontent.com/leanprover-community/mathlib4/v4.24.0/Mathlib/Algebra/Ring/Defs.lean

许可：Apache-2.0; file header and fixed-tag LICENSE inspected。

访问：verified_http_200；原抓取2026-10-30T01:47:32.455340+00:00；本批复用缓存：False。

SHA-256：`862a43694ab1713c95776f08634b9bd4697536c76ee80aa26127caadb6e30c72`；14951字节。

缓存：`/tmp/dedekind-multiplication-source-audit/mathlib_ring_defs`。

### mathlib_order_ring_defs

Jeremy Avigad; Leonardo de Moura; Mario Carneiro; Yaël Dillies; Yuyang Zhao；Mathlib/Algebra/Order/Ring/Defs.lean；mathlib v4.24.0, textual source only, no Lean compilation。

https://raw.githubusercontent.com/leanprover-community/mathlib4/v4.24.0/Mathlib/Algebra/Order/Ring/Defs.lean

许可：Apache-2.0; file header and fixed-tag LICENSE inspected。

访问：verified_http_200；原抓取2026-10-30T01:47:32.782039+00:00；本批复用缓存：False。

SHA-256：`ce16d26f079c7ec0323d98c20d1a8d078a758b230d673abb4f6641ee93192bfd`；19592字节。

缓存：`/tmp/dedekind-multiplication-source-audit/mathlib_order_ring_defs`。

### mathlib_order_ring_basic

Jeremy Avigad; Robert Y. Lewis；Mathlib/Algebra/Order/Ring/Basic.lean；mathlib v4.24.0, textual source only, no Lean compilation。

https://raw.githubusercontent.com/leanprover-community/mathlib4/v4.24.0/Mathlib/Algebra/Order/Ring/Basic.lean

许可：Apache-2.0; file header and fixed-tag LICENSE inspected。

访问：verified_http_200；原抓取2026-10-30T01:47:33.144381+00:00；本批复用缓存：False。

SHA-256：`e974bbf6c2d1385964f9aae9dda7959b528c3c93ba58cd6c9b6c6b25bdb8488c`；9056字节。

缓存：`/tmp/dedekind-multiplication-source-audit/mathlib_order_ring_basic`。

## 实际读到的定位与本书义务

### mathlib_ring_defs，行59–96, 116–143, 375

Distrib requires both quantified distributive laws; semiring/ring/commutative ring names bundle stated obligations.

NP/NL/SP/SR must prove these cut operations separately before using the structure names; full distributivity is only reached in B2.28.

### mathlib_ring_defs，行308–327

Within an already assumed NonUnitalNonAssocRing, neg_mul and mul_neg are derived using distributivity; mul_sub/add_sub identities then follow.

This dependency cannot be imported for SP2: our signs are first verified directly from the cut sign definition; full distributivity is later proved using these signs. Only after SR2 may the difference identities be used.

### mathlib_order_ring_defs，行115–137

Nonnegative factors preserve weak order; positive factors preserve strict order. An algebraic semiring and ordered addition are prior assumptions.

Weak monotonicity first follows directly from P witnesses; strict monotonicity NL4 uses already proved nonnegative distributivity and D=B⊖A>0.

### mathlib_order_ring_defs，行147–161

IsOrderedRing.of_mul_nonneg and IsStrictOrderedRing.of_mul_pos derive order multiplication from positivity of a difference product, assuming Ring.

Use as dependency comparison. The actual book SR3 calculation must explicitly invoke earlier SR2 distribution and DG4 difference order; no circular use of an abstract ring before SR2.

### mathlib_order_ring_basic，行1–29

Basic ordered-ring lemmas start with existing algebra and order assumptions; IsSquare.nonneg assumes Semiring, LinearOrder and monotone multiplication.

Reviewed only to reject it as a construction source or proof of missing cut roots. No theorem from this file is needed by the four planned units.

### mathlib_field_basic，行23–25,132–134

Midpoint inequalities under existing ordered-field/semifield assumptions.

Apply only to the established rational numbers. Explicit rational midpoint witnesses prove P closure, identity, rational compatibility and NL association; no real completeness used.

### dedekind_tex，行1006–1062,1080–1090

Part I §VI gives addition and says other elementary operations can be defined; distributivity is discussed through continuity rather than supplying this plan’s modern strict one-sided cut proof.

Historical attribution only. Do not attribute our P formula, zero branch, common witness, signed distributivity or rational reciprocal proof to an exact passage not found. These are independent book derivations.

## 特别核验项目

- 严格负支q<0使乘零仍为i(0)，不会变空；正内见证避免两个任意负内点相乘无界。
- 单位反向不取不在i(1)的1，而用q/a与1之间的有理中点。
- 主下段相容只用已证Q正除法与两次中点，不用平方根或R倒数。
- 非负分配先处理零，再处理和的原见证可能负、右侧两乘积原成员可能负及共同A见证。
- 完整有符号分配用比较X、Y的两支和加法移项，不预用乘法差式。
- 当前四单元至多得到有序交换环和非零消去；倒数候选与其证明路线仅是后续计划。
