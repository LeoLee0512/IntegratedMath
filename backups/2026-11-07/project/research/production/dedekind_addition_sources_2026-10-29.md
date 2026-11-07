# 第22批来源审计候选：分割加法、相反数与次序平移

当前快照核验：2026-10-30T02:00:36.844488+00:00。状态：来源审计候选位于 `/tmp`；root已安装的四稿、六份报告/计划及绘图模块已只读核对，不授予最终构建、书页或汇总验收。

本补记与对应JSON记录当前四稿、既有独立数学报告及主编格式续核、教学报告和M=5图。文末保留原预研全文；其中原访问日期、旧概念审阅哈希和N=5图证据属于各自历史版本，不能替代当前绑定。统一来源锚仍为 `dedekind-addition-sources`。

## 来源缓存、作者及许可复核

重新读取原11份缓存字节，SHA-256与字节数全部匹配。新增核对原有Lebl首页缓存1份（没有新网络请求）：固定提交、作者与6.3版均与原记录一致。原预研“1次新请求、10份复用”计数不重写为本轮网络活动。本轮为0次网络请求、12份本地缓存复核。

五份mathlib数学源码的第4行作者声明均逐一匹配；Dedekind作者与Beman译者从元数据第16、5行核对；Lebl作者及版本从 `realanal.tex` 第289、382行核对。Project Gutenberg许可的发布者是Project Gutenberg，不能把Dedekind/Beman当作许可文本作者；当前JSON纠正这个角色并完整保留原字段。元数据及许可记录中的其余作者字段也明确是作品署名或项目归属，不冒称标准许可文本作者。

| 来源 | 字节数 | SHA-256 |
|---|---:|---|
| mathlib_lower_basic | 14011 | `7d752b38fba8f5bed0be3fd70a1fa97497dfb3fe6c4add8ade66783b229caa43` |
| mathlib_field_basic | 31120 | `7a0a7285fa3a0adad6ffeaae3dc254d68d1cb8573b0932507178b2ea111d8197` |
| mathlib_archim_basic | 25104 | `78c9a88bc670d67318367a3531fdae32b806a280fa3a1ee0ee5bc7728e05c09f` |
| mathlib_group_defs | 52245 | `5fe7a3a3f0827d6f50ea422574316731b470631308fe5a5d4faf8a5f97b9d885` |
| mathlib_license | 11357 | `b40930bbcf80744c86c46a12bc9da056641d722716c378f5659b9e555ef833e1` |
| dedekind_tex | 243143 | `f837b8376cbbfca11690cea3bc0fac14fffecb88ae669e4f15158f096c915f44` |
| dedekind_license | 17504 | `1e301e03fb28addf6ad03d42b1429e87679013d1ee7e141c7c968fbef0ad961d` |
| dedekind_metadata | 1216 | `fa7d92b7841e4b84a3ce2c7f603a17c37b74afe5112aa868e1520c17ebd147f2` |
| lebl_reals | 80337 | `d492090591013b5845ddfa48f7dc0f15500180bf04aa8a0af10dd7d3919f01a3` |
| lebl_license | 467 | `682fedaab34d7d47962da7276284e608f43881c07c3c887cb66368688748c13d` |
| mathlib_order_upperlower | 7938 | `41bc0117344f1ec0c8d45bd2e3b08766551bce730a778b81eef6f8f58194ac41` |
| lebl_front | 18862 | `a355edf1ff287d98d13bfc50fa9cfcd541b42b8210f0172dfb5dadafb58a47ee` |

Lebl首页原URL：https://raw.githubusercontent.com/jirilebl/ra/e21ec524ca7d54f800c693b948020c188d21d01f/realanal.tex
原抓取时间：2026-10-29T19:51:54.424412+00:00；本次仅复用缓存。

mathlib的Apache 2.0、Lebl双CC许可、Dedekind作品在美国公有领域及Project Gutenberg/所在地条件均保持原义。未编译Lean，未移植外部证明文字、习题、图像或源码。已再次读取19项记录的实际源码位置；定义端点、已存在环境群及实数先修的差异仍须保留。31项既有先修的完整文件哈希、标题与行号和分类文件哈希全部未变。

## 当前正文与答案绑定

| 文件 | 字节数 | SHA-256 |
|---|---:|---|
| `/tmp/dedekind_addition.md` | 15821 | `1e1297d265344259094f503025d42f951dc0a9ce74025d582aeb6835226d8a24` |
| `/tmp/dedekind_addition_answers.md` | 12604 | `02841b87929c5ca19f11a0c8b8036d29adf3b4b727a82070ffd5d72fcadc145e` |
| `/tmp/dedekind_additive_order.md` | 17033 | `f46ce5d5c91060cbb0b76d84ab8cb9874bcde7a54214ae07619df0f6270eb003` |
| `/tmp/dedekind_additive_order_answers.md` | 12935 | `94d4ed3e4729b55f877832b18459277e09d968e9bbf59d9139608a051533ddb9` |

## 计划与审阅证据的层次

数学报告保留2026-10-29原独立审阅与原接受哈希；末尾2026-10-30段是主编对格式后字节的续核，不是原审阅者重新签署。教学报告含当前四稿哈希。这里只实际绑定文件并核对哈希出现位置，不签发新的数学或教学通过。

| 证据 | 当前SHA-256 |
|---|---|
| `/tmp/dedekind_addition_plan.md` | `23d82dd8789052273135d20c5514e0b6352cd2dab590282091ac298458f22b4d` |
| `/tmp/dedekind_addition_concept_review.md` | `fed63b4b9c306b4b974ad793614cf9ab13a8ac674efb0cb36cb122403d0cd9ab` |
| `/tmp/dedekind_addition_math_review.md` | `21a7f7b51386ec831b4bd1f82cf961047ee78efcfe1415fe3e8d0cba6cc73c1b` |
| `/tmp/dedekind_additive_order_math_review.md` | `84ccf7939ff345db21530d35ca10005a104bb79cf1f54c4487f1aa441bb393c6` |
| `/tmp/dedekind_addition_pedagogy_review.md` | `d56a45511ebf5c0adcfabe7b4c9334e3375f01f30a57dda0f9fc933fe9cedb07` |
| `/tmp/ped22_format_changes.json` | `313578f554d4456530d9b98c90e166cc3c27e378c7fc4abf76a284991b95110e` |

概念报告原来源预研哈希为 `bc12184c29ce758faf96ee1571d1edac826ed8c48a92e03c05d6a47905d044ec`，当前报告为上表所列；两版本的意义已经分开保留，未把后来补记伪装成早先抓取时已存在。四份格式差异与逐项替换JSON均另行绑定；当前四稿哈希与替换记录一致。

## M=5图与完整函数绑定

已实际打开当前PNG，看见右端M=5、首次退出m=2，六点与前二内后四外、u/v和严格间距一致；仅是独立PNG观察，不等于最终书页验收。现有整数对检查再次运行通过，输出另存 `dedekind_grid_figure_integer_pair_recheck.json`；未导入绘图模块或重绘，也不是一般分割成员算法。旧独立输出仍绑定旧N=5 PNG，作为历史证据保留。

| 对象 | SHA-256 |
|---|---|
| 当前独立绘图脚本 | `4a13641c2cc43d604b28b3930ff533810aba54fc547c3d6d09e8ae5f763a1673` |
| 当前M=5 PNG | `d89c138785739d43eaef849703f4d13e2b9b8060bb02a315612bde7be848b85d` |
| 完整函数原文（末尾一换行） | `e2771ff3bdedc7cc7f588686af1a842132503775bb63c20be6bad17b36ecb957` |
| 完整函数AST（不含位置信息） | `decf1a9c5994883a5f8975c9d4c6fea6e4b19547d008cc74ca32d536f21cbcd9` |
| 图审报告（含主编M=5续核） | `384908b44c111266615efb054fec21098d1cd3f61000b8681efaa7d3a1706936` |
| 当前整数对诊断输出 | `d55c0bbcc5d51ea1eb74b04961994dc2b25c0059c60e420e06fe1f4ec13c573f` |

完整函数为 `draw_dedekind_grid(out)`，脚本第11—59行；最长源码行86字符。精确原文和AST哈希算法见JSON。独立脚本整体包含/tmp入口，正式整合模块的整体哈希必须另外计算；当前正式模块已经另外绑定，完整函数原文与AST均匹配；正式全量构建与附录的最终书页排版仍待核，没有拿独立脚本冒充正式模块。诊断保留的内部变量N和`N_is_first_exit`键只代表指标5，当前图中文字M=5由源码和实际图面分别核对。

## root安装后的只读续核

2026-10-30T02:02:20.928040+00:00：实际重读四份正式正文/答案与六份正式计划/报告，全部和本审计绑定字节相同。主编已经复制的正式PNG也与M=5版本一致。未改正式文件。

正式绘图模块 `tools/draw_foundations_batch.py` SHA-256：`804ea2d414bf728d8a6ffaeced181c69b3f00448f33bdb758cd036160459dbe1`。完整函数原文与AST分别等于前表哈希；`main()`确实以 `out` 调用该函数。实际调用已安装函数但把输出限定在 `/tmp/batch22-integration/installed-figure-recheck/`，生成PNG与候选SHA完全相同；这不是全量正式构建或最终书页验收。

已实际调用当前已安装构建器的 `compose_body()`，仅将尚待复制的本批来源审计读取临时指向最终/tmp候选，其余正文、附录和绘图源码全部读取正式已安装文件。组合字符串完整包含当前绘图函数，并且新来源锚与附录二十五锚各恰出现一次；未执行PDF构建，不声称最终排版通过。

## 交付root的确切剩余操作

1. Copy both final source-audit candidates to the stated repository paths and check byte identity before build. Their own installed hashes belong in the build input manifest, not a self-hash inside this audit.

2. These supporting files are bound at observed /tmp paths; if archived into repository, copy byte-for-byte to their stated intended paths. Do not claim installation where no installed_repository_sha256 exists. The six main reports/plans and four manuscripts were already verified.

3. Proceed with production build/validator and final PDF visual review outside this source audit. Installed current compose_body already contains the exact complete function and unique appendix/source anchors. Keep build and visual reports separate to avoid circular hash dependencies; this audit grants no aggregate acceptance.

不需要把文件自身哈希写回自身；root核对复制字节后，由构建输入清单绑定最终JSON/MD。构建及视觉报告另外记录，避免循环哈希依赖。

## 以下为原始预研全文（历史记录，原文保留）

# 第22批来源预研：分割加法、相反数与次序平移

核验时间：2026-10-29T20:11:44.459067+00:00。仅 `/tmp`。统一锚 `dedekind-addition-sources`。
B2.23 DA1–DA4 rational grid witnesses / exact cut sums / strict negative cut / rational compatibility; B2.24 DG1–DG4 additive laws / inverse / order translation / subtraction. No formal batch22 edits or acceptance.

主归属97F50、第526章；06F20、06A05仅交叉。计划与概念审查SHA见JSON，不能据计划预发正文验收。

## 已核结论与证据边界

All listed bytes actually read and SHA checked. One new public 200; ten cached records reused at original fetch dates. Exact grid and strict-negation inverse proof not located externally in inspected sources and explicitly recorded as independent book derivation.

- Book strict i(0)=Iio(0) versus library all-LowerSet additive zero Iic(0).
- Historical C1 uses weak sum witness and allows endpoint allocation; book exact/strict sum equivalence uses no maximum.
- Pointwise reflection of complement can include a largest endpoint; the book strict q<−r definition removes it.
- Abstract group laws and already-built R sources cannot be premises of the same cut construction.

## 访问、版本与许可

Mathlib Apache-2.0. Lebl dual CC-BY-SA-4.0 / CC-BY-NC-SA-4.0. Dedekind ebook metadata: public domain in USA, with Project Gutenberg license; no global public-domain claim. License caches and metadata preserve original URLs and hashes.
Original factual/condition summaries only; no external proof prose, exercises, diagrams or Lean source copied into manuscript. Latin-1 for Dedekind TeX as declared inputenc; hashes use original bytes. No Lean compilation.

### mathlib_lower_basic

Yaël Dillies; Sara Rousta，Order/UpperLower/Basic.lean；mathlib v4.24.0 (public tagged source; checked text only, no Lean compilation)。
URL：https://raw.githubusercontent.com/leanprover-community/mathlib4/v4.24.0/Mathlib/Order/UpperLower/Basic.lean
许可：Apache-2.0; source file notice and reused fixed-tag LICENSE inspected
原请求时间：2026-10-29T19:52:19.118716+00:00；本批复用：True。
SHA-256：`7d752b38fba8f5bed0be3fd70a1fa97497dfb3fe6c4add8ade66783b229caa43`；缓存 `/tmp/rational-gaps-cuts-source-audit/mathlib_lower_basic`。

### mathlib_field_basic

Robert Y. Lewis; Leonardo de Moura; Mario Carneiro; Floris van Doorn，Algebra/Order/Field/Basic.lean；mathlib v4.24.0 (public tagged source; checked text only, no Lean compilation)。
URL：https://raw.githubusercontent.com/leanprover-community/mathlib4/v4.24.0/Mathlib/Algebra/Order/Field/Basic.lean
许可：Apache-2.0; source file notice and reused fixed-tag LICENSE inspected
原请求时间：2026-10-29T19:52:19.119904+00:00；本批复用：True。
SHA-256：`7a0a7285fa3a0adad6ffeaae3dc254d68d1cb8573b0932507178b2ea111d8197`；缓存 `/tmp/rational-gaps-cuts-source-audit/mathlib_field_basic`。

### mathlib_archim_basic

Mario Carneiro，Algebra/Order/Archimedean/Basic.lean；mathlib v4.24.0 (public tagged source; checked text only, no Lean compilation)。
URL：https://raw.githubusercontent.com/leanprover-community/mathlib4/v4.24.0/Mathlib/Algebra/Order/Archimedean/Basic.lean
许可：Apache-2.0; source file notice and reused fixed-tag LICENSE inspected
原请求时间：2026-10-29T19:51:08.957096+00:00；本批复用：True。
SHA-256：`78c9a88bc670d67318367a3531fdae32b806a280fa3a1ee0ee5bc7728e05c09f`；缓存 `/tmp/rational-gaps-cuts-source-audit/mathlib_archim_basic`。

### mathlib_group_defs

Jeremy Avigad; Leonardo de Moura; Simon Hudon; Mario Carneiro，Mathlib/Algebra/Group/Defs.lean；mathlib v4.24.0。
URL：https://raw.githubusercontent.com/leanprover-community/mathlib4/v4.24.0/Mathlib/Algebra/Group/Defs.lean
许可：Apache-2.0
原请求时间：2026-10-29T17:29:05.670992+00:00；本批复用：True。
SHA-256：`5fe7a3a3f0827d6f50ea422574316731b470631308fe5a5d4faf8a5f97b9d885`；缓存 `/tmp/powers-polynomials-source-audit/mathlib_group_defs`。

### mathlib_license

mathlib contributors，mathlib LICENSE；mathlib v4.24.0 (public tagged source; checked text only, no Lean compilation)。
URL：https://raw.githubusercontent.com/leanprover-community/mathlib4/v4.24.0/LICENSE
许可：Apache-2.0
原请求时间：2026-10-29T17:29:06.420671+00:00；本批复用：True。
SHA-256：`b40930bbcf80744c86c46a12bc9da056641d722716c378f5659b9e555ef833e1`；缓存 `/tmp/powers-polynomials-source-audit/mathlib_license`。

### dedekind_tex

Richard Dedekind; English translator Wooster Woodruff Beman，Essays on the Theory of Numbers, Part I: Continuity and Irrational Numbers；Gutenberg ebook 21016 released 2007-04-08; GITenberg commit 7a0bcaf5e279121cb675058d7e323556343087d0。
URL：https://raw.githubusercontent.com/GITenberg/Essays-on-the-Theory-of-Numbers_21016/7a0bcaf5e279121cb675058d7e323556343087d0/21016-t/21016-t.tex
许可：Metadata states Public domain in the USA; Project Gutenberg license and local-law caveat apply; no global public-domain claim
原请求时间：2026-10-29T19:51:08.612324+00:00；本批复用：True。
SHA-256：`f837b8376cbbfca11690cea3bc0fac14fffecb88ae669e4f15158f096c915f44`；缓存 `/tmp/rational-gaps-cuts-source-audit/dedekind_tex`。

### dedekind_license

Richard Dedekind; English translator Wooster Woodruff Beman，Project Gutenberg License；Gutenberg ebook 21016 released 2007-04-08; GITenberg commit 7a0bcaf5e279121cb675058d7e323556343087d0。
URL：https://raw.githubusercontent.com/GITenberg/Essays-on-the-Theory-of-Numbers_21016/7a0bcaf5e279121cb675058d7e323556343087d0/LICENSE
许可：Metadata states Public domain in the USA; Project Gutenberg license and local-law caveat apply; no global public-domain claim
原请求时间：2026-10-29T19:51:08.612777+00:00；本批复用：True。
SHA-256：`1e301e03fb28addf6ad03d42b1429e87679013d1ee7e141c7c968fbef0ad961d`；缓存 `/tmp/rational-gaps-cuts-source-audit/dedekind_license`。

### dedekind_metadata

Richard Dedekind; English translator Wooster Woodruff Beman，GITenberg metadata.yaml；Gutenberg ebook 21016 released 2007-04-08; GITenberg commit 7a0bcaf5e279121cb675058d7e323556343087d0。
URL：https://raw.githubusercontent.com/GITenberg/Essays-on-the-Theory-of-Numbers_21016/7a0bcaf5e279121cb675058d7e323556343087d0/metadata.yaml
许可：Metadata states Public domain in the USA; Project Gutenberg license and local-law caveat apply; no global public-domain claim
原请求时间：2026-10-29T19:52:19.458448+00:00；本批复用：True。
SHA-256：`fa7d92b7841e4b84a3ce2c7f603a17c37b74afe5112aa868e1520c17ebd147f2`；缓存 `/tmp/rational-gaps-cuts-source-audit/dedekind_metadata`。

### lebl_reals

Jiří Lebl，Basic Analysis I, chapter The Real Numbers；version 6.3; commit e21ec524ca7d54f800c693b948020c188d21d01f。
URL：https://raw.githubusercontent.com/jirilebl/ra/e21ec524ca7d54f800c693b948020c188d21d01f/ch-real-nums.tex
许可：Dual CC-BY-SA-4.0 / CC-BY-NC-SA-4.0, as repository LICENSE states; no text/figure adaptation here
原请求时间：2026-10-29T19:51:08.613314+00:00；本批复用：True。
SHA-256：`d492090591013b5845ddfa48f7dc0f15500180bf04aa8a0af10dd7d3919f01a3`；缓存 `/tmp/rational-gaps-cuts-source-audit/lebl_reals`。

### lebl_license

Jiří Lebl，Basic Analysis LICENSE.md；version 6.3; commit e21ec524ca7d54f800c693b948020c188d21d01f。
URL：https://raw.githubusercontent.com/jirilebl/ra/e21ec524ca7d54f800c693b948020c188d21d01f/LICENSE.md
许可：Dual CC-BY-SA-4.0 / CC-BY-NC-SA-4.0, as repository LICENSE states; no text/figure adaptation here
原请求时间：2026-10-29T19:51:08.949458+00:00；本批复用：True。
SHA-256：`682fedaab34d7d47962da7276284e608f43881c07c3c887cb66368688748c13d`；缓存 `/tmp/rational-gaps-cuts-source-audit/lebl_license`。

### mathlib_order_upperlower

Yaël Dillies，Mathlib/Algebra/Order/UpperLower.lean；mathlib v4.24.0。
URL：https://raw.githubusercontent.com/leanprover-community/mathlib4/v4.24.0/Mathlib/Algebra/Order/UpperLower.lean
许可：Apache-2.0; file header plus reused LICENSE
原请求时间：2026-10-29T20:07:23.186892+00:00；本批复用：False。
SHA-256：`41bc0117344f1ec0c8d45bd2e3b08766551bce730a778b81eef6f8f58194ac41`；缓存 `/tmp/dedekind-addition-source-audit/mathlib_order_upperlower`。

## 实际读到的位置与条件差异

### DA1–DA3 / strict_lower

`mathlib_lower_basic` 第323—338行：`isLowerSet_iff_forall_lt / isLowerSet_iff_Iio_subset`。
来源条件：PartialOrder; weak closure is equivalent to strict closure via equality case.
本书义务：Book lower closure is strict q<a; this matches after checking equality separately. Nonempty/proper/no-max are additional conditions, not consequences of lower closure.

### DA3 / complement

`mathlib_lower_basic` 第38—52行：`IsLowerSet.compl / IsUpperSet.compl`。
来源条件：Set complement of a lower set is an upper set, for the existing ambient order.
本书义务：Complement alone is not a negative cut. Reflection turns upper into lower but does not remove a possible maximum.

### DA3 / midpoint

`mathlib_field_basic` 第23—25行：`LinearOrderedSemifield assumptions`。
来源条件：Already given ordered semifield structure.
本书义务：Applicable to established Q, not to not-yet-constructed cut arithmetic.

### DA3 / midpoint_bounds

`mathlib_field_basic` 第132—134行：`left_lt_add_div_two / add_div_two_lt_right`。
来源条件：Given a<b, midpoint strictly between; no completeness.
本书义务：For q<−r choose (q−r)/2, keeping the same complement witness; this proves no maximum for the strict negative cut.

### DA1 / rational_natural_bound

`mathlib_archim_basic` 第358—400行：`archimedean_iff_nat_lt and Archimedean Q`。
来源条件：Field/order structure; library rational proof uses rational ceiling in an intermediary step.
本书义务：Book already has QG1 explicit rational-record bound; use it on (b0−a0)/δ to get a natural exit bound, without real Archimedean property, floor or cut arithmetic.

### DA2/DG1 / pointwise_ambient_assumptions

`mathlib_order_upperlower` 第38—46行：`OrderedCommGroup variable block, translation image`。
来源条件：CommGroup, PartialOrder, IsOrderedMonoid; multiplicative text marked to_additive.
本书义务：Read source annotations only, no Lean elaboration/compilation. The additive specialization may be applied to Q whose additive laws are proved. It does not assume or prove that newly constructed cuts form a group.

### DA2 / pointwise_lower_closure

`mathlib_order_upperlower` 第53—67行：`IsLowerSet.mul_left / mul_right with to_additive`。
来源条件：Pointwise operation on arbitrary subsets; lower closure when the indicated factor is lower, in the prior ordered-group context.
本书义务：Book proves exact-sum lower closure using a′=p−b; it must separately prove nonempty, proper and no maximum. Do not treat library lower closure as cut closure.

### DA3 / reflection

`mathlib_order_upperlower` 第69—73行：`IsUpperSet.inv / IsLowerSet.inv with to_additive`。
来源条件：Reflection/inverse changes upper to lower and lower to upper in an ordered group.
本书义务：Source guarantees only lower closure of reflected complement. Book N(A)={q:∃r∉A,q<−r} has an additional strict rounding step. For A=i(0), raw reflected complement is {q≤0} and fails no-maximum.

### DA2 / exact_pointwise_sum

`mathlib_order_upperlower` 第153—173行：`LowerSet One / Mul / coe_mul, to_additive annotations`。
来源条件：Bundled lower sets use image2 of ambient operation; all lower sets allowed.
本书义务：Image2 corresponds to exact rational sum witnesses, but neither the restricted type nor its zero is the book type. Exact and strict sum witness equivalence must be proved from no-max/downward closure.

### DG1 / closed_zero_trap

`mathlib_order_upperlower` 第155—157行：`LowerSet One defined by Iic 1, to_additive`。
来源条件：Additive translation of this definition gives the CLOSED lower segment Iic 0.
本书义务：Book 0_R=i(0)=Iio(0) excludes rational zero. Cannot cite library zero/unit proof as the book proof; use an internal larger a and z=q−a<0 in the reverse inclusion.

### DG1/DG2 / lower_monoid

`mathlib_order_upperlower` 第188—206行：`LowerSet commSemigroup / one_mul / CommMonoid, to_additive`。
来源条件：Commutative monoid of all lower sets, with closed principal unit. No cut inverse construction here.
本书义务：Only a comparison for inherited associativity/commutativity. Book nested witness proofs establish these on restricted cuts; DA1 is still required for inverse reverse inclusion. Arbitrary lower sets do not all have additive inverses.

### DG1 / group_associative_commutative

`mathlib_group_defs` 第187—209行：`AddSemigroup and AddCommMagma declarations`。
来源条件：add_assoc and add_comm are fields required of structures.
本书义务：They name obligations, not automatic theorems of the new cut operation. Prove by two-direction witness regrouping using only old Q laws.

### DG2 / group_inverse

`mathlib_group_defs` 第1095—1103行：`AddGroup declaration and neg_add_cancel field`。
来源条件：Existing SubNegMonoid plus a neg_add_cancel proof; subtraction convention discussed.
本书义务：Book must prove A⊕N(A)=0_R in both directions before using inverse uniqueness, double negation or cancellation.

### DG2–DG4 / commutative_group_name

`mathlib_group_defs` 第1167—1168行：`AddCommGroup declaration`。
来源条件：AddGroup plus AddCommMonoid.
本书义务：After the laws are proved, the name describes the concrete structure. It is not a prior abstract axiom or a claim of ordered field / multiplication.

### DA1–DA4 / modern_cut_context

`lebl_reals` 第1053—1067行：`exercise:Dedekind`。
来源条件：Existing complete R, lower rational subset bounded above, sup_R A not a member.
本书义务：This source characterizes cuts after R already exists. Do not obtain small rational boundary gaps from an assumed real supremum/density. Book uses Q grid and natural least index instead.

### DA1 / reject_complete_real_route

`lebl_reals` 第693—723行：`thm:arch and proof`。
来源条件：Real Archimedean property is proved using sup_R N; Q density in R is subsequently derived.
本书义务：This route would assume the target ambient real structure. Book needs Q-only Archimedean bound and least natural index, and does not call cut-supremum either.

### DA2/history / history_addition

`dedekind_tex` 第1006—1025行：`Part I §VI Operations with Real Numbers`。
来源条件：Two-sided historical cuts; C1 membership uses c≤a1+b1; endpoint may be assigned to the first side.
本书义务：Not literally the modern strict-cut definition. For BOOK cuts, exact, ≤-witness and <-witness versions can be connected by lower closure and no maximum; the historical endpoint convention cannot simply be dropped.

### DA4 / history_rational_compatibility

`dedekind_tex` 第1025—1045行：`§VI rational addition compatibility and halving positive gap`。
来源条件：Rational endpoints and two-sided cuts; splits positive p into two halves to produce members.
本书义务：Book independently uses h=(r+s−q)/2 and exact witnesses r−h,s−h; prove both inclusions for strict principal lower sets.

### DG2–DG4 exclusion / history_not_full_proof

`dedekind_tex` 第1047—1062行：`§VI statement about other operations`。
来源条件：Author says other operations may likewise be defined and discusses scope, without supplying this book strict-negation/grid inverse proof.
本书义务：Do not cite this paragraph as a complete proof of strict negative cuts, ε-grid lemma, inverse law, order translation, or subsequent multiplication/root existence.

## 独立推导义务：不能由引用省略

- **DA1** `#cutadd-grid`：Separate each internal a from external b by rational trichotomy and lower closure. For epsilon>0 set delta=epsilon/2; choose a0∈A,b0∉A and QG1 positive natural N with eta(N)delta>b0−a0. E={n:a0+eta(n)delta∉A} is nonempty, excludes 0. Use ord-a07 least m; m=k+1 gives k∉E. Then u in, v out, v−u=delta strictly between 0 and epsilon. No cut arithmetic, cut supremum, real density or simultaneous choices.

- **DA1 computational boundary** `#cutadd-grid`：Well-ordering yields a least member of a specified nonempty natural set under classical logic. An arbitrary cut supplies no decidable membership predicate, so no general executable first-exit search, computed real boundary, or terminating cut API is inferred. A rational principal-cut example may have an independent decision procedure.

- **DA2 closure** `#cutadd-definition`：A⊕B={q:∃a∈A,b∈B,q=a+b}. Internal a0+b0 gives nonempty; external r+s is outside because all a+b<r+s; p<q=a+b uses a′=p−b<a; increasing a gives no maximum. Only after four conditions declare R×R→R, with exterior equality giving a unique output subset.

- **DA2 witness conventions** `#cutadd-definition`：For book cuts, q=a+b can be strengthened to q<a1+b by increasing a. Conversely q<a+b gives exact q=(q−b)+b with q−b<a. A weak q≤a+b version also needs equality or lower closure. Historical cuts that admit endpoint maxima are not silently equivalent to this restricted convention.

- **DA3** `#cutadd-negation`：N(A)={q:∃r∉A,q<−r}. External r0 gives −r0−1 inside; internal a0 makes −a0 outside; same external witness gives lower closure; midpoint (q−r)/2 gives no maximum. Do not identify it with raw −A or raw reflection of complement. For i(0), raw reflected complement {q≤0} has maximum 0.

- **DA4 addition** `#cutadd-rational`：i(r)⊕i(s)=i(r+s): forward sum of strict inequalities; backward q<r+s, h=(r+s−q)/2>0, a=r−h,b=s−h, a+b=q. Covers negative and zero endpoints with exact rational arithmetic.

- **DA4 negation** `#cutadd-rational`：N(i(r))=i(−r): external t means t≥r so q<−t≤−r; converse use external t=r. Principal compatibility does not prove all-cut laws since nonprincipal cuts exist.

- **DG1** `#cutgroup-laws`：Exchange witnesses; expand both nested sum memberships before using rational associativity. A⊕i(0)⊆A follows from z<0. Reverse uses q<a∈A then z=q−a<0; rational zero is NOT in i(0).

- **DG2 inverse existence** `#cutgroup-inverses`：Forward q=a+c with c<−r, r∉A, a<r gives q<a−r<0. Reverse any x<0: DA1 with epsilon=−x yields v−u<−x, hence c=x−u<−v, so c∈N(A) and x=u+c. A nonstrict gap may yield equality and fail the negative-cut witness; strictness is essential.

- **DG2 consequences** `#cutgroup-inverses`：After both inverse inclusions, use already established association, commutation and unit to prove inverse uniqueness. Then N(N(A))=A, cancellation, and group terminology. Do not assume any of these in DA1 or in inverse existence.

- **DG3** `#cutgroup-translation`：Weak monotonicity follows from member inclusion. Reflection requires adding N(C) after inverse law. Strict preservation follows from weak preservation plus equality cancellation; strict reflection similarly excludes equality. Translation T_C has two-sided inverse T_N(C), a function on established cut set R.

- **DG4** `#cutgroup-negation-subtraction`：A⊆B gives r∉B⇒r∉A, hence N(B)⊆N(A). Reflection uses double negation only after DG2. Prove inverse of sum by actual parenthesized rearrangement and uniqueness. Define A⊖B=A⊕N(B), then solve A⊕X=B uniquely and derive order-by-difference from translation.

- **Background and endpoint scope** `#cutadd-unit/cutgroup-unit`：Use existing Q and cut-set P(Q) background, products and conditional subsets. No new unrestricted object collection or choice axiom. All witnesses are selected for one given input/claim; no global choice function. No real multiplication, inverse/division, roots, limits, or complete ordered-field claim.

## 网格最小指标的实际先修与算法边界

已逐行读 `natural_order_answers.md` 第169—185行：假设非空自然集合无最小元，以已证强归纳推出所有自然数均不属于它，再与非空见证矛盾；唯一性由反对称。因此这是已证明的结论，不是本批新采用的良序公理。

DA1的E是条件子集：先有N∈E、0∉E，再取最小正m的前驱k，得u在内、v在外、v−u=ε/2。推理只说明见证存在，不提供任意分割的成员判断程序。具体i(3/2)示例中u=5/4、v=3/2、ε=1/2，外点可以正好落在有理端点。

## 真实先修位置

- `#cut-set-background` → `/workspace/IntegratedMath-book/manuscript/foundations/dedekind_cuts_order.md:9`；状态 `formal_manuscript`；SHA `a244695551c88b167daac9ddf76c8becc5e70411ea5e30063af9cf8e7ce22ee4`。
- `#cut-definition` → `/workspace/IntegratedMath-book/manuscript/foundations/dedekind_cuts_order.md:25`；状态 `formal_manuscript`；SHA `a244695551c88b167daac9ddf76c8becc5e70411ea5e30063af9cf8e7ce22ee4`。
- `#cut-order-embedding` → `/workspace/IntegratedMath-book/manuscript/foundations/dedekind_cuts_order.md:74`；状态 `formal_manuscript`；SHA `a244695551c88b167daac9ddf76c8becc5e70411ea5e30063af9cf8e7ce22ee4`。
- `#cut-supremum` → `/workspace/IntegratedMath-book/manuscript/foundations/dedekind_cuts_order.md:213`；状态 `formal_manuscript`；SHA `a244695551c88b167daac9ddf76c8becc5e70411ea5e30063af9cf8e7ce22ee4`。
- `#qgap-density-archimedean` → `/workspace/IntegratedMath-book/manuscript/foundations/rational_gaps_bounds.md:28`；状态 `formal_manuscript`；SHA `20ab8bd8ee996a2b69f297020caf7138c533e8781ff35bc794c8fe6cad0f4ff3`。
- `#pow-compatibility` → `/workspace/IntegratedMath-book/manuscript/foundations/rational_powers.md:240`；状态 `formal_manuscript`；SHA `581010522535b41a771d0dd920531b37669b379ea64ce6001028620988bb3ee2`。
- `#int-order-laws` → `/workspace/IntegratedMath-book/manuscript/foundations/integers_addition_order.md:471`；状态 `formal_manuscript`；SHA `bd18f2b22e9a8b2ef116c5835140eb79beacc4499e489dbfc8e6a38c89778672`。
- `#rord-integers` → `/workspace/IntegratedMath-book/manuscript/foundations/rationals_order.md:141`；状态 `formal_manuscript`；SHA `db52d14c0642912bc281e22e1846f778bc9aa876d1a6ba22e04d5eb3ae28f3ba`。
- `#ord-predecessor` → `/workspace/IntegratedMath-book/manuscript/foundations/natural_order.md:19`；状态 `formal_manuscript`；SHA `4ad8e874bedda7f4c15739fd47344903ec71bd9a5b538c71bde0f9827b091435`。
- `#ord-successor-comparison` → `/workspace/IntegratedMath-book/manuscript/foundations/natural_order.md:163`；状态 `formal_manuscript`；SHA `4ad8e874bedda7f4c15739fd47344903ec71bd9a5b538c71bde0f9827b091435`。
- `#ord-trichotomy` → `/workspace/IntegratedMath-book/manuscript/foundations/natural_order.md:217`；状态 `formal_manuscript`；SHA `4ad8e874bedda7f4c15739fd47344903ec71bd9a5b538c71bde0f9827b091435`。
- `#ord-a07` → `/workspace/IntegratedMath-book/manuscript/foundations/natural_order_answers.md:169`；状态 `formal_manuscript`；SHA `ba046797e6a2ebf8b06cf1795fb6a1b03f92922e0e4caaf98f3a4d5d58c0f1d8`。
- `#ord-strong-induction` → `/workspace/IntegratedMath-book/manuscript/foundations/natural_order.md:336`；状态 `formal_manuscript`；SHA `4ad8e874bedda7f4c15739fd47344903ec71bd9a5b538c71bde0f9827b091435`。
- `#radd-laws` → `/workspace/IntegratedMath-book/manuscript/foundations/rationals_addition.md:99`；状态 `formal_manuscript`；SHA `9b349aec9a9df0c7c45c9d33e7d0cfa483dc22432f0250baa23ab2a6d02b417b`。
- `#radd-opposite` → `/workspace/IntegratedMath-book/manuscript/foundations/rationals_addition.md:163`；状态 `formal_manuscript`；SHA `9b349aec9a9df0c7c45c9d33e7d0cfa483dc22432f0250baa23ab2a6d02b417b`。
- `#radd-cancellation` → `/workspace/IntegratedMath-book/manuscript/foundations/rationals_addition.md:239`；状态 `formal_manuscript`；SHA `9b349aec9a9df0c7c45c9d33e7d0cfa483dc22432f0250baa23ab2a6d02b417b`。
- `#radd-subtraction` → `/workspace/IntegratedMath-book/manuscript/foundations/rationals_addition.md:284`；状态 `formal_manuscript`；SHA `9b349aec9a9df0c7c45c9d33e7d0cfa483dc22432f0250baa23ab2a6d02b417b`。
- `#rmul-laws` → `/workspace/IntegratedMath-book/manuscript/foundations/rationals_multiplication.md:104`；状态 `formal_manuscript`；SHA `033ed077c363d91143247bebedb790d4c444b5574c5085509a2b6c207d0b9c20`。
- `#rmul-distributive` → `/workspace/IntegratedMath-book/manuscript/foundations/rationals_multiplication.md:148`；状态 `formal_manuscript`；SHA `033ed077c363d91143247bebedb790d4c444b5574c5085509a2b6c207d0b9c20`。
- `#rdiv-division` → `/workspace/IntegratedMath-book/manuscript/foundations/rationals_division.md:130`；状态 `formal_manuscript`；SHA `b2adb43e3d4b0fbe5c57dd6b745cfa1550f050321a2208df618a666ca8ecfc64`。
- `#rdiv-cancellation` → `/workspace/IntegratedMath-book/manuscript/foundations/rationals_division.md:260`；状态 `formal_manuscript`；SHA `b2adb43e3d4b0fbe5c57dd6b745cfa1550f050321a2208df618a666ca8ecfc64`。
- `#rord-laws` → `/workspace/IntegratedMath-book/manuscript/foundations/rationals_order.md:99`；状态 `formal_manuscript`；SHA `db52d14c0642912bc281e22e1846f778bc9aa876d1a6ba22e04d5eb3ae28f3ba`。
- `#rord-translation` → `/workspace/IntegratedMath-book/manuscript/foundations/rationals_order.md:179`；状态 `formal_manuscript`；SHA `db52d14c0642912bc281e22e1846f778bc9aa876d1a6ba22e04d5eb3ae28f3ba`。
- `#rord-negation` → `/workspace/IntegratedMath-book/manuscript/foundations/rationals_order.md:230`；状态 `formal_manuscript`；SHA `db52d14c0642912bc281e22e1846f778bc9aa876d1a6ba22e04d5eb3ae28f3ba`。
- `#rord-multiplication` → `/workspace/IntegratedMath-book/manuscript/foundations/rationals_order.md:260`；状态 `formal_manuscript`；SHA `db52d14c0642912bc281e22e1846f778bc9aa876d1a6ba22e04d5eb3ae28f3ba`。
- `#rord-division` → `/workspace/IntegratedMath-book/manuscript/foundations/rationals_order.md:330`；状态 `formal_manuscript`；SHA `db52d14c0642912bc281e22e1846f778bc9aa876d1a6ba22e04d5eb3ae28f3ba`。
- `#fun-sets` → `/workspace/IntegratedMath-book/manuscript/foundations/functions_definition.md:25`；状态 `formal_manuscript`；SHA `1dee6ffb8bada53f6f09ea4ad908c0a03fd06c937fb685538566175cb9655650`。
- `#fun-pairs` → `/workspace/IntegratedMath-book/manuscript/foundations/functions_definition.md:85`；状态 `formal_manuscript`；SHA `1dee6ffb8bada53f6f09ea4ad908c0a03fd06c937fb685538566175cb9655650`。
- `#fun-definition` → `/workspace/IntegratedMath-book/manuscript/foundations/functions_definition.md:145`；状态 `formal_manuscript`；SHA `1dee6ffb8bada53f6f09ea4ad908c0a03fd06c937fb685538566175cb9655650`。
- `#fc-equality` → `/workspace/IntegratedMath-book/manuscript/foundations/functions_composition.md:17`；状态 `formal_manuscript`；SHA `806b32944f8253b2e2af3b2a551a25cc0ce6bf17ce51cc6b50216cf28e58a94a`。
- `#inv-two-sided` → `/workspace/IntegratedMath-book/manuscript/foundations/functions_inverse.md:51`；状态 `formal_manuscript`；SHA `28ffc4f4746286d1407bbe873d9e508d81e7ca82393c76cbf818131e819b9270`。

## 采用与未采用

Only prior explicit classical logic and set background including batch21 P(Q), products and conditional subsets; no new Archimedean/completeness or group axiom for cuts.

- 不采用：Existing complete real field or rational density in it
- 不采用：mathlib full lower-set closed zero Iic(0)
- 不采用：Historical two-sided endpoint identification without translation
- 不采用：Decidable membership or a first-exit algorithm for arbitrary cuts
- 不采用：Choice functions, cut multiplication, real square roots or limits

## 限制

- Plan/concept/source review is not manuscript acceptance.
- No claim of direct external textual evidence for exact epsilon-grid or strict negative-cut inverse argument.
- No general cut API, member-decision algorithm, real multiplication, ordered-field completion or root existence.

本次不修改第20、21批正式文件、冻结来源、图像、ledger或验收。新增网络请求只有上述数学库文件一次；原第21批版本查询与许可时间不改写成新抓取。

## 分类位置实查

已实际读取 `data/msc_taxonomy.json`：97F50 为实数与复数的教育方面；06F20 为有序阿贝尔群、里斯群、有序线性空间；06A05 为全序。本批只以97F50为主归属，另两项只交叉，不因此登记抽象群论或一般序理论已覆盖。分类文件字节绑定见JSON。
