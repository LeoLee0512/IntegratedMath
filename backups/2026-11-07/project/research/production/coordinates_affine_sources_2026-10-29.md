# 有理坐标与仿射函数：公开来源审计（2026-10-29）

状态：来源审计，不是书稿审阅或完成判定。范围为B2.9有理坐标与函数图、B2.10仿射函数图/斜率/截距/单调/交点。由已实核临时计划正式化，保留原访问时间与哈希，本次正式化未重新网络抓取。

## 已实际核查的两个系列

13次公开请求全部HTTP 200，访问时间、固定版本、字节数和SHA-256保留于同名JSON；全部响应重新核对哈希。环境运行且策略enforced，经继承代理与TLS验证读取，无凭据操作。

### COORD-OPENSTAX：Intermediate Algebra 2e

版本：osbooks-prealgebra-bundle commit ad40c7e3c9a909cde81a24c526f52fe26a51fb14。许可：CC-BY-NC-SA-4.0。仅核数学事实、条件和教学边界，独立编写证明与题答，不拷贝题干、图表、连续正文；许可不可误写CC BY。图片另有例外说明，本批不使用图片。

- [m81369，fs-id1167834538411](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81369/index.cnxml#L48)（modules/m81369/index.cnxml，行48–70）：有序对先横坐标后纵坐标。来源以通常几何平面为背景；本书只定义Q²为有理有序对集合，不能宣称所有实际几何点都有有理坐标。
- [m81369，fs-id1167835330675](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81369/index.cnxml#L88)（modules/m81369/index.cnxml，行88–97）：横轴点的第二坐标为零，纵轴点的第一坐标为零；书稿用集合定义并保留原点同时在两轴上。
- [m81369，fs-id1167835350108](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81369/index.cnxml#L291)（modules/m81369/index.cnxml，行291–302）：来源画三个点再连接的作图步骤只作展示参考；有限点不能证明函数在所有Q输入上的图，更不能把连笔曲线误作已构造的实连续点集。
- [m81369，fs-id1167832075518](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81369/index.cnxml#L458)（modules/m81369/index.cnxml，行458–472）：x=c为竖直，y=b为水平。固定输入x下竖直集合有多个输出，水平集合给出常函数。
- [m81369，fs-id1167826874383](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81369/index.cnxml#L705)（modules/m81369/index.cnxml，行705–718）：轴截点定义。书稿区分截点有序对与截距数值，补足零函数与非零常函数的横轴交集。
- [m81370，fs-id1167834504980](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81370/index.cnxml#L232)（modules/m81370/index.cnxml，行232–239）：水平斜率为零，竖直斜率因分母零而未定义，不写无穷大斜率。
- [m81370，fs-id1167832041523](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81370/index.cnxml#L330)（modules/m81370/index.cnxml，行330–335）：两点斜率差商，书稿必须显式要求x1≠x2；同一点与竖直两点另分支。
- [m81370，fs-id1167834194235](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81370/index.cnxml#L502)（modules/m81370/index.cnxml，行502–514）：斜截式y=mx+b。书稿称仿射函数，固定a,b∈Q，不引入尚未定义的线性空间。
- [m81370，同斜率与不同截距](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81370/index.cnxml#L972)（modules/m81370/index.cnxml，行972–987）：行972简说同斜率平行，行973的精确条件还要求不同纵截距；同斜率同截距是重合图，必须独立处理。竖直线斜率未定义。
- [m81373，关系的domain/range](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81373/index.cnxml#L56)（modules/m81373/index.cnxml，行56–60）：来源由关系的第一、第二坐标集合定义域和值域；本书函数三元组另含声明目标集合，不能只由图恢复任意目标集合。
- [m81373，fs-id1167836614987](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81373/index.cnxml#L195)（modules/m81373/index.cnxml，行195–202）：每个定义域输入恰一个输出；书稿须同时要求存在与唯一，包含空定义域边界。
- [m81374，fs-id1167833386905](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81374/index.cnxml#L64)（modules/m81374/index.cnxml，行64–70）：竖线至多交一点只保证在第一坐标投影域上的函数性；对预先给定D还须每个x∈D至少有一点且不含D外输入。
- [m81374，fs-id1167829598148](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81374/index.cnxml#L128)（modules/m81374/index.cnxml，行128–141）：图为全部(x,f(x))，不只是值表中有限样本。源实平面背景不直接继承到Q²。

### COORD-MATHLIB：mathlib sets, function graphs and ordered multiplication

版本：mathlib4 v4.24.0。许可：Apache-2.0。只读公开源码核前提，不复制代码；未运行Lean，未形式化本书。

- [Set.mem_graphOn / graphOn_eq_empty / image_fst_graphOn / image_snd_graphOn / fst_injOn_graph / graphOn_inj](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Data/Set/Prod.lean#L910)（Mathlib/Data/Set/Prod.lean，行910–948）：图的成员条件、空集边界、投影、第一投影单射及同域逐点相等；固定类型α,β和既有函数f，不等同于忽略目标集合的三元组。
- [graphOn_univ_inj / exists_eq_graphOn_image_fst / exists_eq_graphOn](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Data/Set/Function.lean#L414)（Mathlib/Data/Set/Function.lean，行414–435）：逆向存在声明有[Nonempty β]且图定义在Prod.fst的像上，证明用choose!延拓到α全域。书稿按既有图式函数定义直接验证D上存在唯一，不照搬任意延拓或漏掉范围/存在条件。
- [strictMono_mul_left_of_pos / strictMono_mul_right_of_pos / StrictMono.const_mul](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Order/GroupWithZero/Unbundled/Basic.lean#L581)（Mathlib/Algebra/Order/GroupWithZero/Unbundled/Basic.lean，行581–597）：正倍数严格保序明确以0<a为前提；a<0和a=0的仿射分支由本书已证有理序律另证。不声称此段已给出全部负斜率/零斜率分类。

## 必须保留的证明与范围条件

1. Q²定义为Q×Q。点仅指有理有序对；(x,y)=(u,v)当且仅当x=u且y=v。两轴、原点与象限通过坐标零值和正负定义，不以未建立的欧氏平面作本体。
2. 对给定D,B⊆Q，图H属于函数D→B的充要条件是H⊆D×B且每个x∈D恰有一个y∈B使(x,y)∈H。证明直接用函数三元组定义；H的第一投影是D，第二投影是实际输出像，目标B不能从图唯一恢复。
3. 竖线至多相交一点只是输出唯一性；若某个声明输入没有点，则不是D上的函数。空图对应空定义域；对非空D空图失败。固定H、固定D和B时函数至多一个；改变B可保持同一图但改变函数。
4. 横线H_b={(x,b):x∈Q}是常函数图，竖线V_c={(c,y):y∈Q}含(c,0)和(c,1)故不是横坐标作输入的函数图。若改纵坐标作输入须明确改变输入约定。
5. 限制到S⊆D的图为H∩(S×Q)，目标集合沿用B；用成员条件双向证。有限值表与画点只作样本，不能决定无限域上整个函数。
6. 令f:Q→Q，f(x)=ax+b，a,b∈Q。任意x1≠x2有f(x2)−f(x1)=a(x2−x1)，非零消去给差商a。证明斜率与所取不同横坐标的两点无关；反向排序同时改变分子分母符号。
7. 给(x1,y1),(x2,y2)：x1≠x2时a=(y2−y1)/(x2−x1)，b=y1−ax1，代入证存在、相减证唯一。x1=x2且y1=y2时任取a后b=y1−ax1均适合；x1=x2且y1≠y2则无仿射函数经过两点。
8. 纵轴交点恒为(0,b)。横轴交集：a≠0时{(−b/a,0)}；a=0,b≠0时空集；a=b=0时整条有理横轴。若用截距表示数值须先说明，不能把整轴交集误写唯一截点。
9. 先定义严格递增、严格递减与常值。全Q上a>0严格递增，a<0严格递减，a=0常函数；用x2−x1>0与乘法符号逐向证明。逆向取0<1。空或单点D上的严格单调可真空成立，限制域时不得无条件说严格递增iff a>0。非严格单调仅为来源相关延伸；若使用非减/非增术语才先定义并说明常函数两者兼具，不把它登记为当前正文已教目标。
10. Γ(a,b)与Γ(c,d)交点：a≠c时x=(d−b)/(a−c)、y=ax+b且唯一；a=c,b=d时两图重合；a=c,b≠d时不交。分母a−c仅在非零分支出现。若定义域分别D,E再筛x∈D∩E。
11. 可选桥接：Ax+By=C在Q²中，B≠0为仿射函数图；B=0,A≠0为竖直集合x=C/A；A=B=0,C=0为全Q²；A=B=0,C≠0为空集。先判参数再除法，关联SYS但不引入秩。
12. 本批不建立实数完备性、连续性、欧氏距离、角度、垂直斜率积、任意实际点的坐标表示或完整解析几何。示意连接线只表示公式趋势，不表示本书已经定义全部实点。

## 分类、先修与验收计划

两单元主97I20（第529章97Ixx）；97H30为交点方程的交叉，97G70为坐标教学交叉。实际分类数据已核；不登记51N20欧氏解析几何或26A03极限与拓扑的覆盖。仅登记有限函数教学目标，不表示所属章或叶完成。

B2.9复用fun-pairs、fun-definition、fun-empty、fun-image及fc-equality/fc-restriction；B2.10复用已证有理四则/序律、lin-affine/lin-two-sides及sys-solution，再接B2.9新图像定义。JSON按实际正文逐条登记先修锚、定义与命题；新锚已核存在，锚点存在不代替内容审阅。

单元接口：rational_coordinates.md / coord-unit / coord-q01…08、coord-a01…08；affine_graphs.md / affgraph-unit / affgraph-q01…08、affgraph-a01…08。保持functions模块内顺序，不增加反向先修环或声称完整线性代数/几何。

精确有限核查通过：{"slope": 5832, "monotonicity": 5832, "intersections": 59049, "axis_intersections": 729, "graph_criterion": 64}。检查使用Fraction与有限关系穷举，不替代一般证明。

临时副本已核31单元、248基础题加绪论14题共262题，题答锚全部成对；5章/27末级有草稿，0章/部分完成，43模块无环，push仍未到期。正式台账当前不动，等待主线程最终QA。

来源边界：OpenStax本身的NC-SA条件和图片例外保留；不复制题目或图像。mathlib的图延拓带Nonempty及choose!，本书采用自身图式函数定义；没有运行Lean，不声称本书已形式化。已抓到m81372实为二元不等式作图，不将错误猜测的模块用途写成证据。

逐文件作者：mathlib集合积文件由Mario Carneiro、Johannes Hölzl、Patrick Massot署名；集合函数文件由Jeremy Avigad、Andrew Zipperer、Haitao Zhang、Minchao Wu、Yury Kudryashov署名；有序乘法文件由Damiano Testa、Yuyang Zhao署名。完整对应与补充候选文件作者见JSON。

## 实际单元锚与临时登记核验

B2.9（coord-unit）：CO1 #coord-quadrants 有理坐标点九类符号位置的完整互斥分类；CO2 #coord-graph 函数图的点成员判据及域与像的坐标读取；CO3 #coord-function-test 声明范围内逐横坐标存在且唯一的函数图判据；CO4 #coord-intersections 函数图与轴及另一函数图的共同点成员公式。各8题与8个答案锚均存在。

B2.10（affgraph-unit）：AG1 #affgraph-intercepts 仿射图的纵轴唯一交点及横轴全部参数分支；AG2 #affgraph-slope 仿射输出差式与非零输入差下的恒定差商；AG3 #affgraph-monotonicity 全Q上严格单调或常值与系数符号的充要条件；AG4 #affgraph-two-points 不同横坐标两点确定唯一仿射函数；AG5 #affgraph-intersection 两仿射图唯一交点、不交或重合的完整分类。各8题与8个答案锚均存在。

与021bf61比对，旧29条UNIT_SPECS、43条MODULES、58个旧BRIDGE路径及CH01接口逐项保持。新增先修全部指向此前单元；第529章续写不增加分类章数。临时生成目录为/tmp/coordinates-ledger-check-2orwetrn，正式data/production七份JSON在本次检查前后哈希未变。临时副本未复制构建PDF，因此未把本次台账测试当作最终构建审阅。
