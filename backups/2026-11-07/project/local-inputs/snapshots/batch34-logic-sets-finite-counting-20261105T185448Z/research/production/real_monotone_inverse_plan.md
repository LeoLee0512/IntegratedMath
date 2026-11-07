# B4.10 有界单元计划：闭区间上的严格单调与逆函数连续性

日期：2026-11-05。作者任务：`/root/part1_pedagogy`。状态：已授权计划与两稿原创写作；独立审读、构建、视觉及作者验收另行进行。本单元不注册当前构建，不改台账和accepted记录。主归第146章26A15，交叉97I20；只承担下列限定目标，章及MSC叶保持partial。

## 1. 最小充分范围

新增 `manuscript/foundations/real_monotone_inverse.md` 与 `real_monotone_inverse_answers.md`，八题及完整分离答案。正文预计约12—18页，答案另计。分两段阅读：严格单调、像与函数类型；逆函数连续的内部/端点证明及应用。若实测超预算则另分阅读单元，不缩短证明。

只取有限闭区间I=[a,b]，a≤b。先处理a<b的严格递增与严格递减连续实值函数f:I→R；a=b单列。证明实际像等于端值闭区间J；按BJ4重新声明目标得到F:I→J双射，按INV1取得g:J→I。再另造实值记录g_R:J→R，图与g相同，只有g_R按CT定义谈连续。可用包含映射ι:I→R说明g_R=ι∘g，但不将g与g_R误判同一个三项记录。

本单元不推广任意开/半开/无界区间，不要求一般单调函数的间断结构，不引入单侧极限、序列判据、导数、一般逆函数定理、紧致、极值或一致连续。f连续在本单元用于保证像是整段J；不宣称原函数连续是“逆在实际像上连续”的必要条件。

## 2. 已读的精确先修

- `functions_definition.md#fun-definition/#fun-image`、`functions_composition.md#fc-equality/#fc-composition/#fc-identity`：三项记录、实际像及严格类型复合。
- `functions_bijections.md#bij-injective/#bij-surjective/#bij-bijective/#bij-retarget`：单射、满射与BJ4改目标。已实际读BJ4完整证明。
- `functions_inverse.md#inv-reverse-graph/#inv-two-sided`：INV1逆向图合法当且仅当双射、INV2双向求值。已完整阅读当前全文，不把实数连续性归入旧纯集合证明。
- `real_function_continuity.md#cont-definition/#cont-isolated-limit/#cont-basic-restriction/#cont-algebra`：连续不去心，只对实值函数定义；单点域连续；限制、包含、有限运算。
- `real_intermediate_value.md#ivt-interval/#ivt-proof/#ivt-boundaries`：当前已写IV1含端点、反向端值及退化。IVT由实数上确界直接证明，不依赖本单元逆函数；当前两稿此前已完整阅读。
- `real_absolute_distance.md#realabs-definition-bounds/#realabs-products-triangle`、实数有序域：双侧绝对值界、正最小半径、取反等距、乘除的符号规则。
- `real_square_roots.md#realsqrt-square-order/#realsqrt-function`：仅用于平方根应用的名称及非负根唯一性。平方函数严格递增可现场用平方差证明；逆函数连续性不以平方根连续作先修。

## 3. 逐项证明义务与拟锚

- `minv-definition`：严格递增为u<v⇒f(u)<f(v)，严格递减反向；不降允许等号。单点域严格条件为空真，但退化情况单列。严格单调⇒单射必须对不同输入排序，不把弱单调误当单射。
- `minv-image`（MI1）：递增时端点界给f(I)⊆[f(a),f(b)]，反向包含逐一应用IV1。递减时J=[f(b),f(a)]同理；不只证明IV1给的一个包含。原目标R仍不满射，因为J有限上端值加1没有原输入。
- `minv-inverse-records`（MI2）：BJ4得到F:I→J，与原f一般不是同一记录；单射加满射使INV1给g:J→I。写出g(F(x))=x、F(g(y))=y并核各输入域。另构造g_R:J→R，图合法；所有连续量词明确属于g_R。逆严格单调性由取反假设的排序反证得出。
- `minv-continuity`（MI3）：先递增，任取y0∈J，c=g(y0)，故f(c)=y0。内部a<c<b时取t=min(ε/2,(c−a)/2,(b−c)/2)>0，l=c−t、u=c+t；取δ=min(y0−f(l),f(u)−y0)>0。若y∈J且|y−y0|<δ，置x=g(y)；若x≤l或x≥u，单调给y≤f(l)或y≥f(u)，分别矛盾。因此|x−c|<t≤ε/2<ε。
- 左端c=a：取t=min(ε/2,(b−a)/2)>0、u=a+t、δ=f(u)−f(a)>0；由y∈J给x≥a，距离控制排除x≥u。右端c=b对称取l=b−t、δ=f(b)−f(l)，用x≤b及排除x≤l。这两支不要求像域在端值两侧有输入。
- 递减：令p=−f，则p严格递增连续，像K=[−f(a),−f(b)]=−J。按已证递增情形得到逆实值记录q_R:K→R连续；对y∈J，由唯一原输入证明q_R(−y)=g_R(y)。给ε取q_R在−y0的δ，再用|−y−(−y0)|=|y−y0|直接得g_R连续，不循环调用递减结论或未经类型声明的复合。
- `minv-singleton`：a=b，I={a}、J={f(a)}；新F双射，g将唯一值送回a，实值g_R在单点域连续。无严格端值差，不使用任何为零的δ。
- `minv-square-root`：A>0，f(x)=x²于[0,A]连续且严格递增，像[0,A²]，逆实值记录是非负平方根限制，含0及A²连续；A=0另用单点分支。只证明有限域版本，不偷换为全部非负实域已证明连续。

## 4. 八题与独立答案的必须检查项

| 题 | 锚 | 任务与必查边界 |
| --- | --- | --- |
| 1 | minv-q01/a01 | f(x)=2x−1于[−1,2]；像[−3,3]、原目标R非满射、新F双射、逆(y+1)/2的两端与往返、实值逆连续 |
| 2 | minv-q02/a02 | f(x)=5−2x于[0,2]严格递减；像[1,5]，逆(5−y)/2；y=1与5的相对连续直接误差δ=2ε核端点 |
| 3 | minv-q03/a03 | 重建递增内部点两阈值证明；δ正、l/u域内、x=g(y)合法、双侧反证与ε控制、量词次序 |
| 4 | minv-q04/a04 | 递增两个端点各写单阈值；a=b单点另证，不把零差作为正δ |
| 5 | minv-q05/a05 | [0,2]上f(x)=x当x<1，f(x)=x+2当x≥1；三种输入排序证明严格递增，像[0,1)∪[3,4]，1处不连续，不能用MI1得整段[0,4]；逆在实际像仍可构造，不从原函数不连续推断逆不连续 |
| 6 | minv-q06/a06 | [-1,1]上f(x)=0当x≤0，f(x)=x当x>0；用(x+|x|)/2证明连续，分支证明不降，像[0,1]；0有多个原输入，重设目标仍非单射无逆 |
| 7 | minv-q07/a07 | 平方规则于[0,A]，A≥0分零/正；平方差严格性、像、逆记录与sqrt名、有限域连续含两端 |
| 8 | minv-q08/a08 | x³于[0,1]，有限乘积连续、差式正性、像[0,1]；定义唯一非负区间立方根的逆，0处直接δ=ε³证明相对连续，未假定导数非零 |

题5选择有限域、不同跳点和跳幅，独立核验全部分支与实际像，不复制外部例题答案。题8不引入全实域立方根总理论；只定义本区间的唯一原输入。

## 5. 实际来源与阅读边界

没有新增网络请求。实际读官方固定提交e21ec524ca7d54f800c693b948020c188d21d01f的现有缓存 `local-inputs/function-limits-source-cache/ch-contfunc.tex`，SHA-256 `3fe56fe7261f3db0dfb0dbabe8e807b0781c41255c2b9cb463f4868fbb13c14d`，119775字节。真实来源链接：https://raw.githubusercontent.com/jirilebl/ra/e21ec524ca7d54f800c693b948020c188d21d01f/ch-contfunc.tex 。作者Jiří Lebl，Basic Analysis I，6.3；作者/版本与双许可CC BY-SA 4.0或CC BY-NC-SA 4.0的实际核验沿用本代理已读主文件和LICENSE记录，见前一计划，不声称公有领域。

本次实际阅读2950—2990行的单调定义，以及3234—3333行的逆函数连续命题、完整源证明和例子。源命题在任意实区间上仅要求严格单调，**不要求f本身连续**；它以单侧极限和sup/inf论证，单侧不存在的边界部分留为练习。本单元采用较窄的“有限闭区间且f连续”以获得整段像，并自行完整证明内部及两端的直接ε—δ结论，不把未学的单侧极限作为隐含先修，也不称独立阈值证明为源书原证明。未读该文件其他未列部分，不复制外部TeX或图入分发稿。

## 6. 当前依赖身份与后续验收

| 文件 | SHA-256 |
| --- | --- |
| functions_inverse.md | 28ffc4f4746286d1407bbe873d9e508d81e7ca82393c76cbf818131e819b9270 |
| functions_bijections.md | b8eea358d984c1a13e27b83d24c872ae8f6ef1ca966fd1159788860cb35b79db |
| real_intermediate_value.md | e79d53a89cf8266f39d76a3f4f35b3e3baecf99d8bfa3db9d679872b37e7f676 |
| real_intermediate_value_answers.md | 5e96183e4c669cbff38b5bb9f67fba65e4cee679ae87ca6ddcb03f6b0cb1b48a |
| real_function_continuity.md | c28fe5c66a2895d0db3ad9cfbc2ada9f3e9f8e7942faaa80802529312d19a21b |
| real_square_roots.md | 35d8419b09e136e278431b4584e3252080f4110bf9c2b649ede9a7001843afcf |

各文件均在manuscript/foundations。以上是阅读时接口身份，不把其他单元的accepted传给新稿。作者自检覆盖锚点、八题答案配对、阈值正性与域；独立数学与教学审读须另行签署当前源码散列。构建及实际页面视觉不在本写作任务内；没有完成这些检查之前保持draft/pending。
