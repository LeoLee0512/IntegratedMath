# 有理数缺口与戴德金分割次序：公开来源审计

B2.21 QG1–QG4 与 B2.22 DC1–DC4 正式正文及各八份答案已登记。独立数学报告绑定实际四稿；教学、验收导入、构建及最终页图检查另设关口。只建立有理缺口及分割的集合与次序结构，不声称完成实数算术、有序域或整个MSC主题。

正式登记时间：2026-10-29T20:08:50.034715+00:00。统一引用锚 `rational-gaps-cuts-sources`。主97F50，第526章；06A05和03E20仅交叉。

## 正式接口与独立数学报告

B2.21：模块number-systems，四组命题、八题及八份答案。
- `manuscript/foundations/rational_gaps_bounds.md`：`20ab8bd8ee996a2b69f297020caf7138c533e8781ff35bc794c8fe6cad0f4ff3`
- `manuscript/foundations/rational_gaps_bounds_answers.md`：`80cdf0a274ae73e0ed7546c4be8345534671f64bef1d441dca7b54507ad33675`

- QG1 `#qgap-density-archimedean`：中点稠密与显式阿基米德界。
- QG2 `#qgap-supremum-definition`：上界、最大元与上确界的定义和性质。
- QG3 `#qgap-perturbation`：平方缺口的显式改进公式。
- QG4 `#qgap-no-rational-supremum`：非空有上界却无有理上确界。

B2.22：模块number-systems，四组命题、八题及八份答案。
- `manuscript/foundations/dedekind_cuts_order.md`：`a244695551c88b167daac9ddf76c8becc5e70411ea5e30063af9cf8e7ce22ee4`
- `manuscript/foundations/dedekind_cuts_order_answers.md`：`cf5de337b8698a917fbabb0cef6d17e66db10227c05fc75179f3d41bfd0bac3c`

- DC1 `#cut-definition`：单侧分割与有理下段。
- DC2 `#cut-order-embedding`：包含全序与有理数的保序嵌入。
- DC3 `#cut-gap`：平方缺口的非主分割。
- DC4 `#cut-supremum`：非空有上界分割族的并集上确界。

- `research/production/rational_gaps_bounds_math_review.md`：`d40cf0239debc8a6e748c8b9e773bac1c9d830eca5488fd37e41a0cbfe59ac97`。
- `research/production/dedekind_cuts_order_math_review.md`：`85fa341aa6c3f87df616b05560d1dabd50f555c639c3836d2f94ea60e1087280`。

本次只绑定已读独立数学报告；报告导入、教学、构建与最终批次验收仍分别核查。新增P(Q)存在是明示采用的集合背景，不能说已从集合论公理证明。

## 图与程序边界

`dist/figures/b2_rational_gap.png`：`d86ad3a6737614ac2ee439abf34c61913bb224220e4e48728783947002762667`。绘图源 `tools/draw_foundations_batch.py`：`dc88d6702cb6ba22b6fccf05a74e001505f48b968e3289c6d5a734bc08a5f823`。

已读独立图审固定六个样本1→4/3→7/5与2→3/2→10/7；两恒等式和平方比较经整数对检查。实际综合绘图函数的AST与已审临时函数一致。不提供实数、分割或极限API。

## 实际登记检查

```json
{
  "units": 43,
  "foundation_exercises": 344,
  "introductory_exercises": 14,
  "exercises": 358,
  "referenced_figures": 17,
  "old41_specs_unchanged": true,
  "formal_data_json_written_by_installer": false,
  "new_network_requests_during_registration": 0,
  "chapters_with_partial_body": 5,
  "leaves_with_partial_body": 29,
  "modules": 43,
  "completed_chapters": 0,
  "completed_parts": 0,
  "module_dag_acyclic": true,
  "chapter01_content_and_registry_unchanged": true,
  "chapter528_fourteen_bridge_scope_preserved": true,
  "leaf97F50_newly_registered": true
}
```

## 历史预审与来源条件原始记录

以下保留原预审的来源、条件定位、许可及当时的待证义务文字；其中“预审”“后来证明”等时态属于历史检查记录。当前稿件阶段以上面的正式接口及报告绑定为准。原12份材料、20处定位和16条义务不改写历史。本次登记没有新网络请求。

# 第21批公开来源预审：有理数缺口与戴德金分割次序

核验时间：2026-10-29T19:57:02.105874+00:00。只写 `/tmp`；统一引用锚 `rational-gaps-cuts-sources`。计划 SHA-256：`3f9e500c20aa899fd2e6fa26619bac604cc49fc78ba4ea3004e80d9ca1bf2492`。主归属 97F50，第526章，交叉 06A05、03E20。

B2.21 QG1–QG4 rational density/explicit natural bounds/square gap; B2.22 DC1–DC4 cut order, rational embedding, nonprincipal gap and conditional union supremum. No formal batch21 files installed or accepted.

## 实际访问与许可

新增 HTTP 请求 21 次，其中 20 次 200、1 次实际 404；另有 2 次公开 git ls-remote。复用已验证 mathlib 许可证缓存 1 份，本批没有为该缓存重新请求。每条原始时间、URL、字节数和 SHA-256 见同名 JSON。

Public unauthenticated HTTPS via inherited proxy and verified TLS; no policy change, bypass or private credentials.

GitHub directory pages are discovery evidence only, not mathematical authority or rights licenses. Initial guessed Data/Rat/Archimedean.lean was an actual 404 and is preserved. OpenLogic directory exploration did not supply an adopted source. Correct Archimedean source is Algebra/Order/Archimedean/Basic.lean. No unseen URL is marked checked.

Only bibliographic metadata, mathematical facts, theorem identifiers and conditions are summarized in original prose. No external prose passage, proof text, exercise wording, diagram, or source code is transplanted into the manuscript. Cached complete files retain source/licensing provenance. No claim that reference use changes the book license.

### mathlib_field_basic

Robert Y. Lewis; Leonardo de Moura; Mario Carneiro; Floris van Doorn，**Algebra/Order/Field/Basic.lean**。版本：mathlib v4.24.0 (public tagged source; checked text only, no Lean compilation)。

公开 URL：https://raw.githubusercontent.com/leanprover-community/mathlib4/v4.24.0/Mathlib/Algebra/Order/Field/Basic.lean
许可：Apache-2.0; source file notice and reused fixed-tag LICENSE inspected
用途：Mathematical conditions and structural comparison; no Lean code copied into book
原请求时间：2026-10-29T19:52:19.119904+00:00；SHA-256：`7a0a7285fa3a0adad6ffeaae3dc254d68d1cb8573b0932507178b2ea111d8197`；缓存：`/tmp/rational-gaps-cuts-source-audit/mathlib_field_basic`。

### mathlib_archim_basic

Mario Carneiro，**Algebra/Order/Archimedean/Basic.lean**。版本：mathlib v4.24.0 (public tagged source; checked text only, no Lean compilation)。

公开 URL：https://raw.githubusercontent.com/leanprover-community/mathlib4/v4.24.0/Mathlib/Algebra/Order/Archimedean/Basic.lean
许可：Apache-2.0; source file notice and reused fixed-tag LICENSE inspected
用途：Mathematical conditions and structural comparison; no Lean code copied into book
原请求时间：2026-10-29T19:51:08.957096+00:00；SHA-256：`78c9a88bc670d67318367a3531fdae32b806a280fa3a1ee0ee5bc7728e05c09f`；缓存：`/tmp/rational-gaps-cuts-source-audit/mathlib_archim_basic`。

### mathlib_lower_basic

Yaël Dillies; Sara Rousta，**Order/UpperLower/Basic.lean**。版本：mathlib v4.24.0 (public tagged source; checked text only, no Lean compilation)。

公开 URL：https://raw.githubusercontent.com/leanprover-community/mathlib4/v4.24.0/Mathlib/Order/UpperLower/Basic.lean
许可：Apache-2.0; source file notice and reused fixed-tag LICENSE inspected
用途：Mathematical conditions and structural comparison; no Lean code copied into book
原请求时间：2026-10-29T19:52:19.118716+00:00；SHA-256：`7d752b38fba8f5bed0be3fd70a1fa97497dfb3fe6c4add8ade66783b229caa43`；缓存：`/tmp/rational-gaps-cuts-source-audit/mathlib_lower_basic`。

### mathlib_lower_complete

Yaël Dillies; Sara Rousta，**Order/UpperLower/CompleteLattice.lean**。版本：mathlib v4.24.0 (public tagged source; checked text only, no Lean compilation)。

公开 URL：https://raw.githubusercontent.com/leanprover-community/mathlib4/v4.24.0/Mathlib/Order/UpperLower/CompleteLattice.lean
许可：Apache-2.0; source file notice and reused fixed-tag LICENSE inspected
用途：Mathematical conditions and structural comparison; no Lean code copied into book
原请求时间：2026-10-29T19:52:19.119395+00:00；SHA-256：`1fb3d369d1c13a9758e2f989defafbd0b983d703c73943540bab2b51c7016b0e`；缓存：`/tmp/rational-gaps-cuts-source-audit/mathlib_lower_complete`。

### mathlib_rat_floor

Johannes Hölzl，**Data/Rat/Floor.lean**。版本：mathlib v4.24.0 (public tagged source; checked text only, no Lean compilation)。

公开 URL：https://raw.githubusercontent.com/leanprover-community/mathlib4/v4.24.0/Mathlib/Data/Rat/Floor.lean
许可：Apache-2.0
用途：Supporting dependency/discovery only; book does not adopt floor operations
原请求时间：2026-10-29T19:51:08.979068+00:00；SHA-256：`1082c98d820a0cb72e00c0ec515555fc364ff330c806345756963a1420df16bd`；缓存：`/tmp/rational-gaps-cuts-source-audit/mathlib_rat_floor`。

### mathlib_license

mathlib contributors，**mathlib LICENSE**。版本：mathlib v4.24.0 (public tagged source; checked text only, no Lean compilation)。

公开 URL：https://raw.githubusercontent.com/leanprover-community/mathlib4/v4.24.0/LICENSE
许可：Apache-2.0
用途：License evidence reused without a new network request
原请求时间：2026-10-29T17:29:06.420671+00:00；SHA-256：`b40930bbcf80744c86c46a12bc9da056641d722716c378f5659b9e555ef833e1`；缓存：`/tmp/powers-polynomials-source-audit/mathlib_license`。

### lebl_reals

Jiří Lebl，**Basic Analysis I, chapter The Real Numbers**。版本：version 6.3; commit e21ec524ca7d54f800c693b948020c188d21d01f。

公开 URL：https://raw.githubusercontent.com/jirilebl/ra/e21ec524ca7d54f800c693b948020c188d21d01f/ch-real-nums.tex
许可：Dual CC-BY-SA-4.0 / CC-BY-NC-SA-4.0, as repository LICENSE states; no text/figure adaptation here
用途：Bounds definitions and modern lower-cut exercise; its ambient real completeness is explicitly not adopted
原请求时间：2026-10-29T19:51:08.613314+00:00；SHA-256：`d492090591013b5845ddfa48f7dc0f15500180bf04aa8a0af10dd7d3919f01a3`；缓存：`/tmp/rational-gaps-cuts-source-audit/lebl_reals`。

### lebl_front

Jiří Lebl，**Basic Analysis I, front matter**。版本：version 6.3; commit e21ec524ca7d54f800c693b948020c188d21d01f。

公开 URL：https://raw.githubusercontent.com/jirilebl/ra/e21ec524ca7d54f800c693b948020c188d21d01f/realanal.tex
许可：Dual CC-BY-SA-4.0 / CC-BY-NC-SA-4.0, as repository LICENSE states; no text/figure adaptation here
用途：Author, title/version and copyright evidence
原请求时间：2026-10-29T19:51:54.424412+00:00；SHA-256：`a355edf1ff287d98d13bfc50fa9cfcd541b42b8210f0172dfb5dadafb58a47ee`；缓存：`/tmp/rational-gaps-cuts-source-audit/lebl_front`。

### lebl_license

Jiří Lebl，**Basic Analysis LICENSE.md**。版本：version 6.3; commit e21ec524ca7d54f800c693b948020c188d21d01f。

公开 URL：https://raw.githubusercontent.com/jirilebl/ra/e21ec524ca7d54f800c693b948020c188d21d01f/LICENSE.md
许可：Dual CC-BY-SA-4.0 / CC-BY-NC-SA-4.0, as repository LICENSE states; no text/figure adaptation here
用途：License evidence
原请求时间：2026-10-29T19:51:08.949458+00:00；SHA-256：`682fedaab34d7d47962da7276284e608f43881c07c3c887cb66368688748c13d`；缓存：`/tmp/rational-gaps-cuts-source-audit/lebl_license`。

### dedekind_tex

Richard Dedekind; English translator Wooster Woodruff Beman，**Essays on the Theory of Numbers, Part I: Continuity and Irrational Numbers**。版本：Gutenberg ebook 21016 released 2007-04-08; GITenberg commit 7a0bcaf5e279121cb675058d7e323556343087d0。

公开 URL：https://raw.githubusercontent.com/GITenberg/Essays-on-the-Theory-of-Numbers_21016/7a0bcaf5e279121cb675058d7e323556343087d0/21016-t/21016-t.tex
许可：Metadata states Public domain in the USA; Project Gutenberg license and local-law caveat apply; no global public-domain claim
用途：Historical date and two-sided cut comparison; different perturbation formula
原请求时间：2026-10-29T19:51:08.612324+00:00；SHA-256：`f837b8376cbbfca11690cea3bc0fac14fffecb88ae669e4f15158f096c915f44`；缓存：`/tmp/rational-gaps-cuts-source-audit/dedekind_tex`。

### dedekind_license

Richard Dedekind; English translator Wooster Woodruff Beman，**Project Gutenberg License**。版本：Gutenberg ebook 21016 released 2007-04-08; GITenberg commit 7a0bcaf5e279121cb675058d7e323556343087d0。

公开 URL：https://raw.githubusercontent.com/GITenberg/Essays-on-the-Theory-of-Numbers_21016/7a0bcaf5e279121cb675058d7e323556343087d0/LICENSE
许可：Metadata states Public domain in the USA; Project Gutenberg license and local-law caveat apply; no global public-domain claim
用途：Distribution/trademark license evidence
原请求时间：2026-10-29T19:51:08.612777+00:00；SHA-256：`1e301e03fb28addf6ad03d42b1429e87679013d1ee7e141c7c968fbef0ad961d`；缓存：`/tmp/rational-gaps-cuts-source-audit/dedekind_license`。

### dedekind_metadata

Richard Dedekind; English translator Wooster Woodruff Beman，**GITenberg metadata.yaml**。版本：Gutenberg ebook 21016 released 2007-04-08; GITenberg commit 7a0bcaf5e279121cb675058d7e323556343087d0。

公开 URL：https://raw.githubusercontent.com/GITenberg/Essays-on-the-Theory-of-Numbers_21016/7a0bcaf5e279121cb675058d7e323556343087d0/metadata.yaml
许可：Metadata states Public domain in the USA; Project Gutenberg license and local-law caveat apply; no global public-domain claim
用途：Public-domain-in-USA declaration, translator and ebook provenance
原请求时间：2026-10-29T19:52:19.458448+00:00；SHA-256：`fa7d92b7841e4b84a3ce2c7f603a17c37b74afe5112aa868e1520c17ebd147f2`；缓存：`/tmp/rational-gaps-cuts-source-audit/dedekind_metadata`。

## 逐接口核查：来源假设与本书义务

### QG1 / midpoint

来源：`mathlib_field_basic` 第 23–25 行，`LinearOrderedSemifield assumptions`。

原条件：Semifield, linear order and strict ordered-ring laws; no completeness premise
本书适用差异：Use established Q field/order interfaces, explain 2>0 and nonzero denominator; this is internal density of Q, not density in an already existing real line.

### QG1 / midpoint_formula

来源：`mathlib_field_basic` 第 132–134 行，`left_lt_add_div_two; add_div_two_lt_right`。

原条件：Strict a<b equivalent to each midpoint inequality in preceding ordered-semifield context
本书适用差异：Independently derive m−a=(b−a)/2 and b−m=(b−a)/2 from prior rational laws.

### QG1 / density

来源：`mathlib_field_basic` 第 182–193 行，`LinearOrderedSemiField.toDenselyOrdered`。

原条件：Midpoint gives a point strictly between ordered endpoints
本书适用差异：Do not import topology, real continuity or completions.

### QG1 / arch_definition

来源：`mathlib_archim_basic` 第 39–44 行，`Archimedean class`。

原条件：For any x and positive y there is natural n with x≤n•y
本书适用差异：Book derives a strict positive-natural bound for each rational record first, then scaled and reciprocal consequences; not an assumed class.

### QG1 / arch_rat

来源：`mathlib_archim_basic` 第 358–400 行，`archimedean_iff_nat_lt; Archimedean Q instance`。

原条件：Field, linear order, strict ordered-ring laws. Rational instance uses rational ceiling in the intermediary implication
本书适用差异：Book does not import floor/ceiling: x=[a,b], b>0, use integer M=|a|+1 and its positive natural preimage. Check b≥1, A≤Ab and strict Ab<Mb.

### QG1 / small_reciprocal

来源：`mathlib_archim_basic` 第 257–269 行，`exists_nat_one_div_lt`。

原条件：Positive epsilon; ordered semifield with Archimedean instance; denominator n+1
本书适用差异：Book proves 0<1/eta(n)<epsilon with n positive. May choose different natural indexing; no sequence or limit conclusion.

### QG2 / bounds

来源：`lebl_reals` 第 54–92 行，`upper bound, least upper bound, uniqueness`。

原条件：Definitions relative to an ordered ambient set; existence not automatic
本书适用差异：State ambient Q, distinguish maximum from supremum, prove uniqueness and examples. Empty set and Q have no Q supremum.

### QG2/DC4 / conditional_completeness

来源：`lebl_reals` 第 121–140 行，`defn:lub`。

原条件：Least-upper-bound property applies only to nonempty bounded-above subsets
本书适用差异：Book must prove it for constructed cuts after defining order; cannot use this property for Q.

### QG1 / reject_real_arch_route

来源：`lebl_reals` 第 693–730 行，`thm:arch and first proof paragraph`。

原条件：Real-number Archimedean property is proved by assuming an R supremum of N if N is bounded; density statement is Q dense in R
本书适用差异：Do not copy this route: it would assume the later completeness construction. Book instead proves only intrinsic Q density and explicit rational-record bounds.

### DC1 / modern_single_side

来源：`lebl_reals` 第 1053–1067 行，`exercise:Dedekind`。

原条件：Nonempty bounded-above rational lower set; sup_R A not in A; ambient R already constructed; characterization A={q∈Q:q<y}
本书适用差异：Comparison source, not construction premise. Book defines nonempty proper lower set with no maximum without mentioning sup_R. For a lower subset of Q, properness is equivalent to a rational upper bound; under already-complete R, sup_R A∉A is equivalent to no maximum. These translations require proof, not silent substitution.

### DC1/DC2 / lower_strict

来源：`mathlib_lower_basic` 第 323–338 行，`isLowerSet_iff_forall_lt; isLowerSet_iff_Iio_subset`。

原条件：PartialOrder suffices to identify weak-lower closure with strict-lower closure via equality case
本书适用差异：Book uses q<a; explain equality case when comparing with library IsLowerSet.

### DC2 / lower_total

来源：`mathlib_lower_basic` 第 342–355 行，`IsLowerSet.total`。

原条件：Underlying type linearly ordered; both subsets lower; no real-number completeness
本书适用差异：Book prove using a∈A and a∉B then every b∈B is below a. Arbitrary subsets are not comparable. Nonempty/proper/no-max needed for cuts elsewhere, not for this lemma.

### DC4 / union_lower

来源：`mathlib_lower_basic` 第 75–97 行，`isLowerSet_sUnion; isLowerSet_iUnion₂`。

原条件：Every member lower; closure of arbitrary union needs no nonempty/bounded restriction for all lower sets
本书适用差异：For restricted cuts additionally prove nonempty from one member, proper from a common upper cut, and no maximum from the same witness member.

### DC4 / union_lub

来源：`mathlib_lower_complete` 第 217–243 行，`LowerSet SupSet and completeLattice`。

原条件：ALL lower sets are included, including empty and full sets; supremum defined by union
本书适用差异：Not the same type as book cuts. Book proves union is a cut only for nonempty bounded families, then upper-bound and minimality separately. Do not call cut order a complete lattice.

### DC4 / union_membership

来源：`mathlib_lower_complete` 第 280–323 行，`LowerSet.coe_sSup; mem_sSup_iff`。

原条件：Membership in supremum is existence of a member lower set containing the element
本书适用差异：Book forms V={q∈Q:∃A∈F,q∈A} via adopted conditional subsets. This does not require a simultaneous choice function.

### DC2/DC4 / library_complete_order

来源：`mathlib_lower_complete` 第 484–505 行，`LowerSet.isTotal_le; instCompleteLinearOrder`。

原条件：LinearOrder on carrier; complete lattice includes bottom empty and top full
本书适用差异：Book proves no global least/greatest cut and excludes empty/unbounded families; do not import library CompleteLinearOrder label.

### Historical sentence / history_1872

来源：`dedekind_tex` 第 1258–1266 行，`Part II preface footnote identifying earlier memoir`。

原条件：Author refers to Continuity and Irrational Numbers, Braunschweig, 1872; translated earlier in this volume
本书适用差异：Permitted short factual sentence: 戴德金在1872年的《连续性与无理数》中以有理数的分割讨论连续性与无理数。 Follow with this book uses a modern one-sided lower-set presentation; no claim to reproduce historical wording.

### Historical corroboration / history_preface

来源：`dedekind_tex` 第 399–417 行，`Part I preface dated March 20, 1872`。

原条件：Preface date is not the 2007 ebook release date
本书适用差异：Keep historical work date, translation/digital edition and retrieval time separate.

### DC1/history / historical_cuts

来源：`dedekind_tex` 第 704–730 行，`Part I section IV Creation of Irrational Numbers`。

原条件：Two classes with each first-class rational below each second-class rational; rational endpoint may belong to either side; two versions not regarded essentially different
本书适用差异：Book canonically chooses lower side with no maximum and complement may have minimum. Historical source is not literally the four-condition modern definition.

### QG3/DC3 comparison / historical_gap

来源：`dedekind_tex` 第 735–804 行，`Part I section IV nonsquare positive integer D example`。

原条件：Uses y=x(x²+3D)/(3x²+D) for positive x; shows both sides improve; separately uses descent to show D has no rational square root
本书适用差异：This is NOT book f(q)=(2q+2)/(q+2). Book f on q≥0 and two identities independently derive from prior rational arithmetic; do not attribute its exact formula to Dedekind. Book uses already-proved non-square 2, no new general nonsquare-integer theorem or descent route.

## 显式公式和历史句的归属

No inspected source is claimed to state the exact f=(2q+2)/(q+2). Both identities are independently derived; Dedekind source gives a different rational perturbation.

对 f(q)=(2q+2)/(q+2)，清分母后两式余项均为零：
`(2q+2)−q(q+2)−(2−q²)=0`；
`(2q+2)²−2(q+2)²−2(q²−2)=0`。
这是精确多项式展开核对，正文仍须给出逐行等式和 q≥0 下分母、分子的正性。未把计算或来源当作正文证明。

戴德金在1872年的《连续性与无理数》中以有理数的分割讨论连续性与无理数。
本书采用现代常见的单侧下集表述；不把四条件定义或本书 f 公式逐字归给历史原文。

## 本书独立证明义务

1. QG1: midpoint differences, denominator 2 positive; q±1 show no endpoints, a separate quantified property.
2. QG1: rational record b>0 gives b≥1 using integer/natural order compatibility; M=|a|+1 has a positive natural preimage; a≤|a|≤|a|b<Mb. Apply same M to −a for two-sided bound. Do not use completeness.
3. QG1: eta order preservation must be composition of integer and rational embedding order laws, not inferred from injectivity. Reciprocal and scaled consequences require positive multipliers.
4. QG2: relative upper-bound/supremum definitions, uniqueness, maximum iff attained supremum, {q<1} counterexample to no-maximum⇒no-supremum; empty and whole Q cases.
5. QG3: domain q≥0; q+2>0, numerator 2q+2>0. Expand both identities explicitly. f is not a total function on all Q: q=−2 is excluded.
6. QG3/QG4: S={q≥0:q²<2} nonempty (0,1), bounded by 2; every upper bound u≥1. Exclude u²<2 using a larger S member, u²=2 by prior SQ4 consequence; u²>2 yields a smaller POSITIVE upper bound, verified against arbitrary s∈S by nonnegative square order reflection.
7. DC1: openly adopt P(Q) existence and conditional subset formation. Previous fun-sets alone did not assert the full powerset. R_cut is a subset of P(Q); no unrestricted all-objects set.
8. DC1: nonempty proper downward closed no-maximum definition. Check four conditions for i(r)={q<r}; complement may have minimum r. Do not use {q≤r}.
9. DC2: prove inclusion reflexive/transitive/antisymmetric and comparability of lower sets; prove i preserves AND reflects ≤, strict < and equality. Only order embedding, no arithmetic structure on cuts.
10. DC2: witness a∈A gives i(a) properly below A; b∉A gives A properly below i(b+1). No global bottom or top.
11. DC3: S is not a cut, since 0∈S but −1∉S. D adds all negatives. Check lower closure and no-max separately for negative/nonnegative inputs; same-square order applies only nonnegative.
12. DC3: prove D={q:∃s∈S,q<s}; D=i(r) would make r the Q supremum of S via order reflection. Do not write D²=i(2) or assign sqrt_Q(2).
13. DC4: given nonempty F and common upper cut U, V={q∈Q:∃A∈F,q∈A} is nonempty/proper/lower/no-max. Give one witness at a time, no choice function.
14. DC4: separate common-upper-bound and leastness proofs. Empty union fails nonempty; union of all i(q) is Q and fails properness, and this family has no cut upper bound. Only conditional order completeness.
15. DC4: F_S={i(s):s∈S} is nonempty bounded by i(2); its union D is its cut-order supremum, compatible with no Q supremum for S.
16. All eight groups require original full manuscript/answer proofs later. No real arithmetic, ordered-field claim for cuts, real-root existence, convergence, topology or general cut decision API is established by this source audit.

## 实际先修锚与集合背景

计划列出的 33 个先修锚均在当前正式稿中存在且唯一；下列文件 SHA-256 绑定核验时实际字节。第20批平方接口的最终接纳仍由 root 批次验收决定。

Read fun-sets plus its adopted-background preamble: finite sets, existing number sets, products, conditional subsets; no blanket powerset grant. Earlier integers/rationals allow specified equivalence-class families, so do not say no set families existed previously.

Read int-embedding and int-order-laws: injectivity in I3, order compatibility and every nonnegative integer has natural preimage at the end of I9.

Read idiv-absolute and SQ1 / non-square 2 sections; SQ anchors exist in formal batch20 manuscripts. Their file hashes bind inspected text, not root final acceptance status.

- `#fun-sets` → `manuscript/foundations/functions_definition.md:25`；SHA-256 `1dee6ffb8bada53f6f09ea4ad908c0a03fd06c937fb685538566175cb9655650`。
- `#fun-definition` → `manuscript/foundations/functions_definition.md:145`；SHA-256 `1dee6ffb8bada53f6f09ea4ad908c0a03fd06c937fb685538566175cb9655650`。
- `#fun-image` → `manuscript/foundations/functions_definition.md:251`；SHA-256 `1dee6ffb8bada53f6f09ea4ad908c0a03fd06c937fb685538566175cb9655650`。
- `#int-pairs` → `manuscript/foundations/integers_addition_order.md:17`；SHA-256 `bd18f2b22e9a8b2ef116c5835140eb79beacc4499e489dbfc8e6a38c89778672`。
- `#rat-classes` → `manuscript/foundations/rationals_construction.md:95`；SHA-256 `0833130ad2bd8f24598a8c8fdfd3ce38e03874036fceac57b019d6d9c7da45a0`。
- `#int-embedding` → `manuscript/foundations/integers_addition_order.md:123`；SHA-256 `bd18f2b22e9a8b2ef116c5835140eb79beacc4499e489dbfc8e6a38c89778672`。
- `#int-order-laws` → `manuscript/foundations/integers_addition_order.md:471`；SHA-256 `bd18f2b22e9a8b2ef116c5835140eb79beacc4499e489dbfc8e6a38c89778672`。
- `#idiv-absolute` → `manuscript/foundations/integer_division.md:27`；SHA-256 `c950dc8b1e8c12faede1ec992a49dfd2ab28b8c568122b4b7b9f7134c7b6381b`。
- `#imul-order` → `manuscript/foundations/integers_multiplication.md:454`；SHA-256 `4bc038ace8d4fe782843098e3f171cf1e2b78b3e79a8169baea9d4bbdfa52bba`。
- `#ord-successor-comparison` → `manuscript/foundations/natural_order.md:163`；SHA-256 `4ad8e874bedda7f4c15739fd47344903ec71bd9a5b538c71bde0f9827b091435`。
- `#rat-integers` → `manuscript/foundations/rationals_construction.md:173`；SHA-256 `0833130ad2bd8f24598a8c8fdfd3ce38e03874036fceac57b019d6d9c7da45a0`。
- `#rat-normal-form` → `manuscript/foundations/rationals_construction.md:233`；SHA-256 `0833130ad2bd8f24598a8c8fdfd3ce38e03874036fceac57b019d6d9c7da45a0`。
- `#rord-definition` → `manuscript/foundations/rationals_order.md:37`；SHA-256 `db52d14c0642912bc281e22e1846f778bc9aa876d1a6ba22e04d5eb3ae28f3ba`。
- `#rord-laws` → `manuscript/foundations/rationals_order.md:99`；SHA-256 `db52d14c0642912bc281e22e1846f778bc9aa876d1a6ba22e04d5eb3ae28f3ba`。
- `#rord-integers` → `manuscript/foundations/rationals_order.md:141`；SHA-256 `db52d14c0642912bc281e22e1846f778bc9aa876d1a6ba22e04d5eb3ae28f3ba`。
- `#rord-sign` → `manuscript/foundations/rationals_order.md:157`；SHA-256 `db52d14c0642912bc281e22e1846f778bc9aa876d1a6ba22e04d5eb3ae28f3ba`。
- `#rord-translation` → `manuscript/foundations/rationals_order.md:179`；SHA-256 `db52d14c0642912bc281e22e1846f778bc9aa876d1a6ba22e04d5eb3ae28f3ba`。
- `#rord-negation` → `manuscript/foundations/rationals_order.md:230`；SHA-256 `db52d14c0642912bc281e22e1846f778bc9aa876d1a6ba22e04d5eb3ae28f3ba`。
- `#rord-multiplication` → `manuscript/foundations/rationals_order.md:260`；SHA-256 `db52d14c0642912bc281e22e1846f778bc9aa876d1a6ba22e04d5eb3ae28f3ba`。
- `#rord-reciprocal` → `manuscript/foundations/rationals_order.md:310`；SHA-256 `db52d14c0642912bc281e22e1846f778bc9aa876d1a6ba22e04d5eb3ae28f3ba`。
- `#rord-division` → `manuscript/foundations/rationals_order.md:330`；SHA-256 `db52d14c0642912bc281e22e1846f778bc9aa876d1a6ba22e04d5eb3ae28f3ba`。
- `#radd-laws` → `manuscript/foundations/rationals_addition.md:99`；SHA-256 `9b349aec9a9df0c7c45c9d33e7d0cfa483dc22432f0250baa23ab2a6d02b417b`。
- `#radd-subtraction` → `manuscript/foundations/rationals_addition.md:284`；SHA-256 `9b349aec9a9df0c7c45c9d33e7d0cfa483dc22432f0250baa23ab2a6d02b417b`。
- `#rmul-laws` → `manuscript/foundations/rationals_multiplication.md:104`；SHA-256 `033ed077c363d91143247bebedb790d4c444b5574c5085509a2b6c207d0b9c20`。
- `#rmul-distributive` → `manuscript/foundations/rationals_multiplication.md:148`；SHA-256 `033ed077c363d91143247bebedb790d4c444b5574c5085509a2b6c207d0b9c20`。
- `#rmul-signs` → `manuscript/foundations/rationals_multiplication.md:275`；SHA-256 `033ed077c363d91143247bebedb790d4c444b5574c5085509a2b6c207d0b9c20`。
- `#rdiv-division` → `manuscript/foundations/rationals_division.md:130`；SHA-256 `b2adb43e3d4b0fbe5c57dd6b745cfa1550f050321a2208df618a666ca8ecfc64`。
- `#rdiv-signs` → `manuscript/foundations/rationals_division.md:209`；SHA-256 `b2adb43e3d4b0fbe5c57dd6b745cfa1550f050321a2208df618a666ca8ecfc64`。
- `#rdiv-cancellation` → `manuscript/foundations/rationals_division.md:260`；SHA-256 `b2adb43e3d4b0fbe5c57dd6b745cfa1550f050321a2208df618a666ca8ecfc64`。
- `#pow-definition` → `manuscript/foundations/rational_powers.md:27`；SHA-256 `581010522535b41a771d0dd920531b37669b379ea64ce6001028620988bb3ee2`。
- `#pow-compatibility` → `manuscript/foundations/rational_powers.md:240`；SHA-256 `581010522535b41a771d0dd920531b37669b379ea64ce6001028620988bb3ee2`。
- `#sqrat-order` → `manuscript/foundations/rational_square_equations.md:23`；SHA-256 `8a1edd98b84ee307666dfe8e7c416bea4530e9332b7eed1e1c813c471a7a2598`。
- `#sqrat-two-not-square` → `manuscript/foundations/rational_square_equations.md:215`；SHA-256 `8a1edd98b84ee307666dfe8e7c416bea4530e9332b7eed1e1c813c471a7a2598`。

## 采用与未采用

- Current classical logic and prior explicit set background
- New explicit P(Q) existence plus subsets selected by conditions; no claimed derivation from axiomatic set theory

- 不作为本书前提：Lebl already-complete R and sup_R based cut characterization
- 不作为本书前提：mathlib floor/ceiling, whole-LowerSet complete lattice, automation and implicit imported structures
- 不作为本书前提：Dedekind general nonsquare-integer descent and historical two-sided endpoint identification

## 限制

- No Lean compilation or reconstruction of the library dependency graph.
- No source here independently certifies the future full manuscript or answers.
- Modern cut comparison from Lebl presupposes existing R; conditional completeness of the restricted cuts is an independent book proof, structurally cross-checked against lower-set union facts.
- No copyright conclusion beyond the inspected licenses/USA public-domain declaration.

本次不修改任何正式稿、正式来源、ledger、验收文件或构建文件。不执行网络资源中的指令。完整请求日志、版本查询和逐字节缓存校验均保留在 `/tmp/rational-gaps-cuts-source-audit/`。

