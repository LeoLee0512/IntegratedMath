# 第26批实数阿基米德性质与平方根来源审计 {#real-arch-sqrt-sources}

实际核验：2026-10-30T03:06:14.062987+00:00，代理 `/root/prepare22_build`。仅/tmp。现已绑定最终四稿和三份实际报告；本来源审计不重新签发数学、教学、构建或视觉验收。

## 范围与独立依赖

B2.31从分割内外点直接建立自然数严格界、有理像稠密，再用既有除法得到正单位倍率、小倒数和给定宽度夹逼。B2.32从已构造有序域重证平方规律，以DC4上确界及双侧扰动证明任意非负平方根存在唯一。RS2不需要RA1—RA4；教学阅读先后不变成额外证明先修。当前稿件实际承担以下义务；既有独立审阅报告另列，这里不代签新的证明通过。

外部Lebl教材先假定完备有序域R存在；本书实际已有的分割运算与上确界证明才是先修。不得把该外部假设当成本书的实数构造证据，也不能把mathlib已经假设Archimedean实例的exists_nat_gt倒用为当前阿基米德证明。

## 缓存、署名、许可及真实抓取历史

五份缓存实际重算SHA-256和字节数，均匹配原记录；逐项核原HTTP200日志、URL、日期与字节。全部抓取仍是2026-10-29，本次无新请求，不把缓存复核写成新HTTP200。完整原来源对象原样保留，旧23—25审计不改。

Mario Carneiro署名实际核mathlib源码第4行；Lebl作者页第289行、版本第382行、版权第401行已读。Lebl固定commit `e21ec524ca7d54f800c693b948020c188d21d01f`，version6.3；mathlib固定v4.24.0。前言435—456及LICENSE均给CC-BY-SA-4.0/CC-BY-NC-SA-4.0双许可；mathlib为Apache2.0。许可文件中的工作署名不冒充标准许可证文字作者。没有复制来源证明措辞、习题、图或代码。

| 来源 | 原抓取UTC | 字节数 | SHA-256 |
|---|---|---:|---|
| mathlib_archim_basic | 2026-10-29T19:51:08.957096+00:00 | 25104 | `78c9a88bc670d67318367a3531fdae32b806a280fa3a1ee0ee5bc7728e05c09f` |
| mathlib_license | 2026-10-29T17:29:06.420671+00:00 | 11357 | `b40930bbcf80744c86c46a12bc9da056641d722716c378f5659b9e555ef833e1` |
| lebl_reals | 2026-10-29T19:51:08.613314+00:00 | 80337 | `d492090591013b5845ddfa48f7dc0f15500180bf04aa8a0af10dd7d3919f01a3` |
| lebl_front | 2026-10-29T19:51:54.424412+00:00 | 18862 | `a355edf1ff287d98d13bfc50fa9cfcd541b42b8210f0172dfb5dadafb58a47ee` |
| lebl_license | 2026-10-29T19:51:08.949458+00:00 | 467 | `682fedaab34d7d47962da7276284e608f43881c07c3c887cb66368688748c13d` |

## 实际读取位置与推导差异

- **lebl_reals** 535-537: real field and least-upper-bound background already assumed

- **lebl_reals** 595-670: existence/uniqueness of positive square root of 2 by supremum and perturbations

- **lebl_reals** 684-773: Archimedean multiples and rational density; source proves natural unboundedness from completeness and density by least natural integer

- **lebl_reals** 672-682: irrationality statement; general nth roots mentioned but excluded here

- **lebl_reals** 772–775: negative-endpoint density cases reduce by negation; read for complete source argument, not adopted construction route.

- **mathlib_archim_basic** 39-44: class Archimedean with additive natural multiples and weak inequality

- **mathlib_archim_basic** 157-176: exists_nat_ge/exists_nat_gt assume Archimedean structure; not proof of cut construction

- **lebl_license** 1-13: dual CC BY NC SA 4.0 / CC BY SA 4.0

Lebl以严格不等式x²<2组成候选集，证明的是正平方根二，后述一般n次根留作练习。本书使用任意A≥0、非负输入与闭条件X²≤A；先不假设上确界属于族。上调h取两个明确正数的min，下调h=(s²−A)/(2s)借A≥0推出h≤s/2，并对任意族成员证明更小上界。这里只借鉴上确界双侧扰动的数学方法并核条件，具体叙述、全参数与零边界证明独立写出。没有据来源练习宣称n次根已证。

mathlib的Archimedean定义在有序加法交换幺半群中使用自然数次相加和弱界；本书ν(n)X在具体已构造实数域中证明严格倍率界，并另述递推，不默引一般实数有限和或程序。

## 当前RA/RS义务

- **RA1** `#realarch-natural-bound`：Define ν:N→R via existing N→Q→R embeddings and check operation/order compatibility. A rational exterior r of any cut A and a positive natural Q bound give A⊆ν(n); r itself witnesses strictness. Prove natural-image unboundedness with correct quantifiers and two-sided bounds without real absolute value.

- **RA2** `#realarch-scaled-reciprocal`：ForX>0 use legal Y/X,RA1 and positive multiplication-back to obtainν(n)X>Y. Forε>0 chooseν(n)>Inv(ε)>0, use already proved positive inverse reversal and double inverse to obtain0<Inv(ν(n))<ε and rational compatibility. n=0 and ε=0 excluded; no sequence limit or general finite-sum interface is introduced.

- **RA3** `#realarch-rational-density`：ForA<B take rationalr∈B\A then largers∈B. ShowA<i(s) usingr as strict witness andi(s)<B usings as distinct strict witness. The first pointr alone may yieldi(r)=A; do not use square roots, Archimedean instance, floor or surjectivity of rational embedding.

- **RA4** `#realarch-rational-brackets`：Givenε>0 form positive half-widthE withE+E=ε by legal division and multiplication-back. ApplyRA3 twice and combine strict inequalities using negation/translation; express width asi(q−p), reflectp<q and prove both positive side errors<ε. Eachε has witnesses, not a uniform algorithm or infinite choice.

- **RS1** `#realsqrt-square-order`：Define real square as self-product only. Reprove all-sign nonnegativity/zero criterion, positive and negative perturbation expansions and difference-of-squares from actualR distribution. Cross terms need commutation and2=1+1. Strict/weak comparison and reflection apply only to nonnegative inputs; show negative-input counterexample.

- **RS2** `#realsqrt-existence`：ForA≥0, S_A={X∈R:0≤X andX²≤A} is a subset of cuts. Zero gives nonempty; U=A+1 withU²>A bounds it; DC4 gives s≥0 but not yet s∈S_A. Ifs²<A, explicitly define two-inputmin, takeh=min(1,(A−s²)/(2s+2))>0 and prove strict perturbation chain. Ifs²>A, s>0 and0<δ≤s²; h=δ/(2s)≤s/2 via multiplication-back, t=s−h>0,t<s,t²=A+h²>A. Prove everyX∈S_A lies belowt before callingt an upper bound and invoking leastness. This proof is independent ofRA1–RA4.

- **RS3** `#realsqrt-function`：Nonnegative square reflection gives uniqueness after existence. Define sqrt_R only from nonnegativeR to nonnegativeR; root sign,zero andone follow by candidates/uniqueness. Rational compatibility uses old partialsqrt_Q only onS_Q; reverse rational-image root implies rational-square membership via embedding reflection and injectivity.

- **RS4** `#realsqrt-equations-irrational`：In candidate domainR classifyX²=A into negative/zero/positive target branches. Positive case verifies±s then proves exhaustion by difference-of-squares and zero-product law, without dividing a possiblyzero difference. Existence ofsqrt(i2) precedes its irrationality proof usingQ no-square-of-two and embedding injectivity. Define irrational asR\i(Q), prove1<sqrt(i2)<2 and translated-square solutions without general real quadratic formula or geometric length claim.

## 当前先修与后续绑定

原来源中的九份正式先修逐项重核散列和真实锚；原来仅计划中的29/30倒数、商与域接口现已在正式文件实核，当前审计单独记录实际安装路径与字节，原历史字段不篡改。此处不据可读接口重签25构建通过。

主属第526章97F50，交叉06A05/12J15表示次序及已有有序域结构应用；不登记26A03。预计53单元438题答（424基础+14引论）、18图25编号附录，仍5草稿章29草稿叶0完成章。一般实数幂、n次根、极限、柯西等价、唯一同构与几何长度仍待后续。

最终四稿与实际概念、数学、教学报告的字节及范围现已绑定。正式安装仍待root实际核对。新来源审计不绑定下游构建与PDF视觉证据；不增加任意分割成员判定、浮点开方或数值算法。


## 最终文本与实际报告绑定

实际核验：2026-10-30T03:15:56.830543+00:00。报告署名和范围均按原文记录；候选绑定不等同正式安装。

| 文件 | SHA-256 |
|---|---|
| `/tmp/real_archimedean_density.md` | `07c238327229f4b1ea5ce8eb5db9fe4ae90f434740f88230338fbc51546c996e` |
| `/tmp/real_archimedean_density_answers.md` | `d9532ea72f9bf98a48cba5ea2293dc9977f98c9b64b07e9a973eb3a27e517165` |
| `/tmp/real_square_roots.md` | `35d8419b09e136e278431b4584e3252080f4110bf9c2b649ede9a7001843afcf` |
| `/tmp/real_square_roots_answers.md` | `2a4d542d0326a6e6e9577a11363ad0434847de976cb6d40c851ec4a906f44732` |
| `/tmp/real_archimedean_density_math_review.md` | `c3d35dce9b5c33249aa4d66ef66030c61ac927ad88156f0f26b67de58f404c8d` |
| `/tmp/real_square_roots_math_review.md` | `745c9c9f6a27142e9a22274f62b9462421a407b11f67ae0aa496efbc4d28e207` |
| `/tmp/real_arch_sqrt_pedagogy_review.md` | `db38177a6cc57e010d4b0a60579c4e351427352539dca8c4cc55364ccc890109` |
| `/tmp/real_arch_sqrt_plan.md` | `6e4b4fa94f86735c23dc7c3faff36b9095d2f54412934da29d167673813f9e64` |
| `/tmp/real_arch_sqrt_concept_review.md` | `f4442515aac02c79cd57121580d4fcaacaf3d80c90a46e6ca16731b0be124d69` |

数学及教学报告范围：

- `review22`：独立全文数学审阅B2.31 RA1—RA4与八份完整解答，核最终先修链接差分。
- `/root/plan_multiplication`：独立全文数学审阅B2.32 RS1—RS4与八份完整解答；两处单空格排版修订已实际逆差绑定。
- `/root/visual21_front`：独立全文教学审阅四稿和16份完整解答、先修与题答双链；新来源仅核锚存在。

## 主编正式安装复核

2026-10-30T03:19:31.025738+00:00，/root实际核四稿、三份真实署名审读报告及两份规划与正式文件逐字节一致，五缓存再次核SHA和大小。三工具从第25批已核基线安装，独立来源锚及53/438/18/25结构在候选组装中通过；正式构建和页面尚待验收。上文/tmp候选状态保留为原审计历史，本节记录已完成安装；未把下游验收嵌入来源哈希。
