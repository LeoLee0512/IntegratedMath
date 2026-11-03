# 第34批计划者接口定位记录

记录者：`/root/plan_multiplication`，2026-10-30。身份：第34批计划者、实际来源路线核对者；本记录**不是对本人计划的独立概念审**。独立概念判断归 root。后续 EV/UC 正文由另两作者完成，本记录者将在真实冻结后作非作者全文数学审。本次仅定位先修和给作者数学提醒，不提前验收尚未冻结的正文或十六份解答。

冻结计划 `/tmp/real_extrema_uniform_plan.md`：SHA-256 `0f6d5690bcfb0d1d7ace3d63fa8556dd91ce8a810eb4988e0df540b374e31d29`。
冻结实际来源 JSON `/tmp/real_extrema_uniform_sources.json`：SHA-256 `1eeb6ba2420237a21a0b2dab5b7a168c9ed9b434aa1539d8d8dd8c07dca5d7e7`。
以上两份文件本次未改，旧批审计亦未改。

## 实际锚定位

以下逐个读取实际文件，定位计划先修段内的全部精确锚。定位不是声称本次重新通读每个早期单元；深读范围另列。

| 精确锚 | 实际路径和行 |
|---|---|
| `fun-sets` | `/workspace/IntegratedMath-book/manuscript/foundations/functions_definition.md:25` |
| `fun-definition` | `/workspace/IntegratedMath-book/manuscript/foundations/functions_definition.md:145` |
| `fun-image` | `/workspace/IntegratedMath-book/manuscript/foundations/functions_definition.md:251` |
| `fc-composition` | `/workspace/IntegratedMath-book/manuscript/foundations/functions_composition.md:77` |
| `cut-order-embedding` | `/workspace/IntegratedMath-book/manuscript/foundations/dedekind_cuts_order.md:74` |
| `cutgroup-laws` | `/workspace/IntegratedMath-book/manuscript/foundations/dedekind_additive_order.md:20` |
| `cutgroup-negation-subtraction` | `/workspace/IntegratedMath-book/manuscript/foundations/dedekind_additive_order.md:197` |
| `cutgroup-translation` | `/workspace/IntegratedMath-book/manuscript/foundations/dedekind_additive_order.md:132` |
| `cutsigned-signs` | `/workspace/IntegratedMath-book/manuscript/foundations/dedekind_signed_product.md:71` |
| `cutsigned-associative` | `/workspace/IntegratedMath-book/manuscript/foundations/dedekind_signed_product.md:202` |
| `cutsigned-rational-zero` | `/workspace/IntegratedMath-book/manuscript/foundations/dedekind_signed_product.md:249` |
| `cutring-distributive` | `/workspace/IntegratedMath-book/manuscript/foundations/dedekind_ring_order.md:169` |
| `cutring-multiplication-order` | `/workspace/IntegratedMath-book/manuscript/foundations/dedekind_ring_order.md:256` |
| `cutdiv-definition` | `/workspace/IntegratedMath-book/manuscript/foundations/dedekind_division_field.md:24` |
| `cutdiv-equations` | `/workspace/IntegratedMath-book/manuscript/foundations/dedekind_division_field.md:86` |
| `cutdiv-order` | `/workspace/IntegratedMath-book/manuscript/foundations/dedekind_division_field.md:207` |
| `realabs-definition-bounds` | `/workspace/IntegratedMath-book/manuscript/foundations/real_absolute_distance.md:22` |
| `realabs-products-triangle` | `/workspace/IntegratedMath-book/manuscript/foundations/real_absolute_distance.md:112` |
| `realsqrt-square-order` | `/workspace/IntegratedMath-book/manuscript/foundations/real_square_roots.md:28` |
| `cutadd-rational` | `/workspace/IntegratedMath-book/manuscript/foundations/dedekind_addition.md:198` |
| `cut-supremum` | `/workspace/IntegratedMath-book/manuscript/foundations/dedekind_cuts_order.md:213` |
| `continuity-definition` | `/tmp/real_continuity.md:7` |
| `continuity-local-restriction` | `/tmp/real_continuity.md:62` |
| `continuity-algebra` | `/tmp/real_continuity.md:125` |
| `continuity-composition` | `/tmp/real_continuity.md:234` |
| `intermediate-intervals` | `/tmp/real_intermediate_value.md:9` |
| `intermediate-values` | `/tmp/real_intermediate_value.md:114` |

本批 C/IV 冻结候选正文仍分别为 `/tmp/real_continuity.md` SHA `328b1782b55447f050c93470128b707cd499e4bca0cf14a33e784a75257d9450`、`/tmp/real_intermediate_value.md` SHA `2b5e8bbd9edadcdd25f1cf52ccd3f6d80bc7f6909aa103d45c34f370100e865c`。本人先前已全文读四主题和所有答案；对应独立报告 `/tmp/real_continuity_math_review.md` SHA `22351ade077c6f41bd4384b7745fa0e539d6b2a0c5f807e3a0d2f248f0b1203a`、`/tmp/real_intermediate_value_math_review.md` SHA `d4d6917ca6d8dbac1e8ae8c171c456ec077e3bf0f34c8e92044c334ef0e6a5b9`。是否已正式整合由 root/build 决定，不能由锚存在自行升级验收状态。

## 新接口的依赖方向

- EV1 `extreme-bounds`：只用函数/像、全序、实际 DC4 最小上界性质，证明二元较大值、取得点与值区别、严格低于上确界的实数上方有成员。
- EV2 `extreme-bounded`：用 EV1 的有限见证与 C2 局部界，直接前缀上确界。没有调用 EV3/UC2。
- EV3 `extreme-attainment`：用 EV2 与 C3 的正差倒数函数，得到实际最大点；最小点取反。没有调用精确像、介值、一般紧致性或一致连续。
- EV4 `extreme-image`：在已取得两个极值点后，调用 IV1/IV3 的闭子区间限制及两方向弱介值，证明精确像。平方算例使用已有实数平方式，不用导数。
- UC1 `uniform-definition`：新量词定义与现有函数/实数运算；限制及逐点连续直接由定义。
- UC2 `uniform-closed-interval`：唯一需要的新跨单元结论是 EV1 的严格较小点上方存在成员。其余使用 DC4、C1 与绝对值；既不依赖 EV3 极值，也不依赖 UC3 运算法则或 UC4 的例子。
- UC3 `uniform-rules`：只用 UC1 定义及有限正半径，包含同域和差、倍数、限制和目标域合法的复合。不从逐点 C3 推出统一结论。
- UC4 `uniform-examples`：实数差平方/绝对值/正除法及 UC1，逐点连续可调用 C3；平方失败还能反证无条件乘积保持。一般乘商和延拓没有反向流入前述证明。

上述依赖图无环。作者可在各自稿内把有限见证重述为引理，但跨链接仍须绑定实际 EV1 冻结稿，不能只有计划标题。

## 本次实际深读与数学提醒

本次重读正式 DC4 全部证明（`dedekind_cuts_order.md` 第213—250行），正式 DQ3 正负除法及正倒数反序（`dedekind_division_field.md` 第207—273行），RS1 全部平方式及非负比较（`real_square_roots.md` 第28—110行），绝对值乘商及三角相关段（`real_absolute_distance.md` 第112—193行）。实际接口足够，不需新增完备性、一般分式或极值先修。

EV3 有一项可精确追溯的写法选择：从正倒数反序得到 `1/g(x)` 的比较后，如果直接化成原正差，双倒数公式已在正式 `/workspace/IntegratedMath-book/manuscript/foundations/dedekind_inverse.md` 第216/240行的 `cutinv-rational-identities` 明确证明。可以在成稿先修补该链接；也可只用计划已有 `cutdiv-equations`，显式以乘回唯一性验证这一化简。此为先修透明性提醒，不是发现数学缺口；已通知 EV 作者。不得把逆元只“存在”当作足够的化简理由而省掉已可追溯的唯一性接口。

其他需在实际成稿保留的条件：

1. 有界前缀集合的成员提供一个非负界，局部界也有明确非负数，两者只合二元较大值。先证明候选在域再用连续性；最后确证末端属于集合，不能止于上确界等于末端。
2. 最大值反证用全域正差，故倒数的实际定义域仍为整个非空闭区间。辅助分母是正的界加一，不是可能为零或负的最大值。
3. UC 前缀集合必须先固定正误差；选出的一个前缀半径仅针对该误差。两点交换名称后，要分别验证全在旧前缀和跨前缀两支；较大点可等于新末端，较小点可等于旧端点，误差仍严格。
4. UC2 的局部连续误差需取全误差的一半，两份严格误差相加才给严格终界。不得让延伸端点在固定集合定义以外随另一个误差变化。
5. 统一平方估计用始终正的两倍界加一，涵盖零界；绝不直接除可能为零的原绝对界。常数倍和仿射均保留零系数支。
6. 指定平方极值例的最大等号同时受实际输入区间限制；平方相等的正负两支须过滤，不能只给正确值却漏报全部取得点。
7. 讨论删“闭端点”条件是对当前实区间的具体域比较，不据此引入尚未定义的一般闭集或紧致判据。常数/空域/单点的一致连续与非空闭区间极值存在应分清。

## 公开来源比较的进一步提醒

实际来源与许可已按冻结 JSON 复核；本次不添加网络请求或未经读取的新引用。Lebl 函数章缓存第1391—1567行的有界/极值证明与第1997—2193行的一致连续定理证明使用任意逐指标实点序列及 BW。书内现有自然最小元递归能构造确定的指标子列，不能自动当成任意实点的可数选择规则。两种前缀上确界证明正好避免该额外义务，不能反过来声称源文给了相同直接证明。

源文的开域倒数反例按“足够小点”讨论；本书计划给两个实际点并统一核任意正半径，尤其很大半径时也必须仍在开域。平方与倒数是标准数学对象，计划中具体坏点公式与证明需由作者独立展开，不复制源文叙述。第2193行以后完整延拓部分未在本次来源范围内审阅，也不在本批承诺内。许可仍为双 CC BY-SA 4.0 / CC BY-NC-SA 4.0，非公有领域，原HTTP时间不冒充重新抓取时间。

## 成稿待审状态

本记录产生时未收到 EV、UC 的真实冻结通知。收到后将分别检查实际四主题、全部八题和八份完整答案，单独输出非作者数学报告，绑定当时最终散列；本记录不提前判定作者尚未落盘内容通过。来源整合、教学审阅、排版/PDF及最终验收不由此记录代签。
