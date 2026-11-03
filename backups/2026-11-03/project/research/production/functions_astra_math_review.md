# B2.1—B2.2 独立数学复核（astra_review）

审阅日期：2026-10-29 UTC。审阅人：独立代理 `/root/astra_review`。

**结论：以下冻结四稿的数学文本审核通过，无未解决的数学阻断问题。** 已完整读两单元正文及全部16题完整答案，另读实现、验证器与来源审计。没有用其他审阅人的结论替代实际阅读。本报告不批准最终PDF、排版截图、发布或整个97I20分类章的完成。

## 冻结版本与实际覆盖

初读时B2.1答案尚未落盘，故未提前给整批通过。随后实际全文读完完整八解，核对作者冻结通知，并检查最后的分类题名、公式折行和措辞修订。B2.1正文439行、答案327行；B2.2正文303行、答案213行。以下SHA-256绑定本次结论；后续改稿须核对差异，不能沿用不匹配哈希。

| 文件 | SHA-256 |
| --- | --- |
| `manuscript/foundations/functions_definition.md` | `1dee6ffb8bada53f6f09ea4ad908c0a03fd06c937fb685538566175cb9655650` |
| `manuscript/foundations/functions_definition_answers.md` | `0cfcaad175aa77f787b368f3ba0fd52793e1544b627b285e2f6ec61b0e28af9a` |
| `manuscript/foundations/functions_composition.md` | `806b32944f8253b2e2af3b2a551a25cc0ce6bf17ce51cc6b50216cf28e58a94a` |
| `manuscript/foundations/functions_composition_answers.md` | `ffb56ac2171cb8776889e2eff69c24a100ef038bd23c8c3b8b33afb6620d1fd9` |

## 采用背景与依赖检查

已读BATCH_CHECKPOINT、LEARNING_PATH、PRODUCTION_PLAN、EXECUTION_PREFERENCES，确认这是原稿接续的B2.1—B2.2，不是替代项目或完成整章的证明。检查点描述上一批，不将其旧审核状态移植到本批。

实际返回阅读B1.7 `int-pairs` 的有序对及朴素集合说明；B1.14 `rat-classes` 的外延判等与等价类、`rat-integers` 的整数嵌入；B1.15 `radd-laws`、`radd-subtraction`；B1.16 `rmul-laws`、`rmul-distributive`；B1.17 `rdiv-division` 的非零除数及乘法方程唯一解；B1.21 `qty-conversion`、`qty-consistency` 的单位模型与两次换算。这些先修的声明和所需结论实际存在，未借本批函数定理反证它们自身。负号题解另直接链接既有 `rmul-signs`、`rdiv-signs`，不把负分母视为新定义的数。

B2.1公开采用有限集合、已有数集、笛卡尔积、从已给集合按条件选子集和三项记录。因而函数图、像与复合图均可在公开背景下形成；没有宣称已经从公理集合论建立其存在性，也没有无条件构造“所有对象的集合”。有序对按位置判等，三项数据按各项判等，这些是明确采用的记录原则。一般函数结论只用此背景和函数定义；有理数算例只用此前运算。全批不依赖实数、完备性、连续曲线、微积分或尚未教完的单射满射与逆函数。

源内数学先修、题答锚点均有对应。两正文的 `functions-sources` 不是独立稿中的锚点；已实际定位为 `tools/build_learning_batch.py` 生成的参考资料锚点。这是整稿构建环节需要核验的链接，不是当前数学文本的缺失定理；本次未将源级检索说成最终PDF链接验收。

## B2.1 逐项核验

1. 元素与子集各有定义，集合双包含判等和子集传递给出逐元素证明。空集唯一依外延原则，存在性属采用背景；空集为任意集合子集的空真解释没有把空集当作一个遗漏输入。空集与单元素集合、数字的记号角色有区分。
2. 笛卡尔积按第一、第二分量定义；有限例的四对逐分支穷尽。任一因子为空时，任何候选对均迫使有元素属于空集，故积为空，理由正确。
3. 关系先要求为A×B子集。F1把“恰有一个”拆为每输入至少一个及同输入至多一个，并证明双向。多个输入共享输出不违反唯一性；目标元素没有被命中不违反存在性。
4. 函数为三数据(A,B,G)，目标B属于记录。求值只在a∈A时定义；图内第二分量由唯一性识别为f(a)。公式构造仍须证明对所有输入有唯一且落在B中的输出，未把公式外形当作合法性证明。
5. 有限平方例逐项核图合法性、存在性、唯一性，再计算像。目标9没被命中但不妨碍函数，也不允许因此求f(9)。绘图仅表示已列完的有限图，不被当作无限有理域或连续实函数的图。
6. F2固定目标B后，空域的图只能为空且条件空真，所以恰一函数。换B即换三数据，两个空图不能消去目标差异。A非空、B为空时，选一个已知存在的a迫使有输出属于空集，矛盾。这个证明没有错误地从积为空直接断言无函数。
7. F3的像先从B筛选。成员判据双向均证明，反向特别补出f(a)∈B。非空域推出像非空只使用一个已知存在输入的输出，不借选择公理；空域时不存在见证，像为空。
8. 无限有理数例x+1依已证运算封闭和唯一；倒数明确去掉零。有限值表在有限定义域可列完全部图，在无限域只记录所列点；正文与题8明确展示不能以有限同值确定全函数。

## B2.2 逐项核验

1. FC1先核A=A′、B=B′，再以任意图对证明Gf⊆Gg与反向包含。共同空域时逐点条件空真但目标相等仍必须保留。常零函数目标Q与{0}的反例合法，图相同而函数不同。
2. FC2限制为(S,B,G|S)，目标保持B。任取x∈S先用S⊆A取得原函数唯一值，再说明该对被保留；若另一对被保留，原唯一性排除不同值。S为空单列。全域限制与嵌套限制均先核双方域及目标，再逐点用FC1，不偷改为像作为目标。
3. 严格复合明确要求前目标恰等于后定义域，并明确这是当前定义约定，不宣称像相容的其他定义本质不可能。FC3将复合图作为A×C子集，从f和g的存在性连续给出见证；两个可能中间值先由f唯一性相等，终值再由g唯一性相等。输出唯一与固定两端集合后整函数唯一分别证明，无逻辑混同。空域也合法。
4. 恒等图每输入有对(x,x)，若另一对等于(t,t)，按有序对相等得输出=x，故唯一。FC4左右单位分别使用id_B和id_A，核中间集合匹配及复合两端为A、B后，才逐点推得相等。
5. 限制恒等id_A|S:S→A与id_S:S→S图相同但目标可能不同；相等当且仅当S=A，两方向有依据。S为空、A非空时仍不相等，未被空图误导。
6. FC5两种括号先分别得A→D，中间函数分别A→C、B→D。每次求值核f(x)∈B及g(f(x))∈C，然后展开为同一h(g(f(x)))。结合仅改括号，不交换顺序；非交换反例零处输出2与1有效。
7. FC6两侧均S→C。右侧的可复合性正由限制保留目标B保证；两侧逐点都为g(f(x))，空S亦成立。没有将g的定义域擅改为像。
8. 厘米→米→千米是Q上的数值函数，单位由应用背景携带。两个除数非零保证全Q合法；令z=(x/100)/1000再导出100000z=x，唯一解给直接公式。250→5/2→1/400与直接值一致；无向长度只用非负输入，全Q为代数扩展，没有宣称负长度的物理意义。

## 全部16题与答案逐题核验

| 单元/题 | 实际核验内容与结论 |
| --- | --- |
| B2.1/1 | 双包含证明C=D；0是A不包含于C的见证；成员/子集、空集子集和空集不等{0}完整。 |
| B2.1/2 | 两个四元素笛卡尔积列举均正确；(-1,0)区分两积；分量顺序与集合列举顺序区分正确。 |
| B2.1/3 | G1合法；G2漏输入1；G3输入0有两个不同输出；G4输出3越界。每个失败有具体见证。 |
| B2.1/4 | (-1)(-1)=1引用先修符号规律；完整三对、像{0,1}双包含、重复输出及f(2)未定义全部回答。 |
| B2.1/5 | 零分母障碍明确；D上的图是D×Q子集，逐输入存在、唯一均证；2与-2输出±1/2并核倒数关系。 |
| B2.1/6 | 空→空和空→{0,1}分别唯一，非空→空无函数；{0}→{0,1}四种关系候选逐项排查，恰两合法图。 |
| B2.1/7 | 甲全Q合法，乙输入1输出2越界，丙图{(-1,0),(0,1)}、像{0,1}；非法乙两种图解释均不能补救。 |
| B2.1/8 | u和v在全Q合法，0处均0、1处均1，2处分别2与4；相同两行不足确定全Q图；域{0,1}时则完整。 |
| B2.2/1 | 任意x用分配律与系数2方程唯一解证两表达式同值；常零异目标反例完整。 |
| B2.2/2 | 两个空域异目标记录不同；固定B的存在与唯一均说明；{0}→空的0输入矛盾正确。 |
| B2.2/3 | 三项记录逐个列对，嵌套限制相等；空限制保Q；改目标为像会改变第二项，用3区分两目标。 |
| B2.2/4 | f、g各自覆盖有限域；正向图{(0,5),(1,5)}、目标{5,6}、像{5}；反向C≠A且f(5)未定义。 |
| B2.2/5 | 全Q上两顺序合法，公式2x+2与2x+1；输入0证不同，不把合法性当作相等。 |
| B2.2/6 | 全Q公式由乘法方程证明，包括x=0；数值250、5/2、1/400计算正确，未把不同裸数值说成相等。 |
| B2.2/7 | 两种括号均Q→Q，公式均2x−1，每个中间函数类型明确；左右恒等正确，交换顺序不获许可。 |
| B2.2/8 | 两个限制复合三数据均(S,Q,{(0,2),(1,4)})；限制恒等与id_S因目标不同不等；空S两比较结论分别仍等、仍不等。 |

## 具体发现与修订闭环

本审阅提出一处需要准确化的措辞：B2.2题6答案原用“非零商的性质”，但任意输入包括x=0，此时商为零；真正所用条件是除数非零。已向主编说明，并实际复读最终答案确认改为“除数非零时商与乘法方程的对应”。该句之后的100000z=x及唯一解推导正确。这不是要求额外排除零输入。此问题已关闭。

未发现待修复的一般定理、反例、条件遗漏或16题算术错误。没有因作者称“冻结”就省略答案阅读；没有将教材来源中不同函数编码的约定直接当作本书三元记录定理。

## 有限程序与来源审计的范围

实际全文读 `finite_functions.py` 与当前验证器。实现只接受显式有限集合容器及精确Python整数标签；bool、float不作为整数标签。构造先查每对坐标所属，再查相同输入冲突，再查定义域全覆盖。相同对重复可去重；缺输出、不同输出、域外/目标外记录拒绝。空域对不同目标仍是不同dataclass记录。限制保目标，复合精确检查中间集合相等。冻结dataclass和frozenset/tuple存储防止普通字段改写和原输入容器后续变化；这不是针对Python反射强行修改对象的安全机制。

原报告的枚举范围为∅、{0}、{0,1}之间全部11个函数，121对相等检查、47合法复合、74错配、211结合三元组等计数与该范围一致；当前版本另有6个明确算例，含B2.2题4。已核报告内两个源码哈希与当前源码相同。本独立复核没有重写主编的验证报告。

为了避免仅用已构造对象的图作“独立”预期，我另从原始候选关系直接判定合法性：域与目标分别取{-2,3}的全部4个子集；候选图遍历{-2,3,7}²全部512个子集。外部标签7可检查越界，按原始图每输入的记录数是否为1得预期，不调用生产构造器产生期望。实际8192候选恰18合法、8174非法，逐项与实现比较成功；另核90合法复合、234类型不符拒绝、466匹配三元组。规律检查同时核域和目标，不只比图。14个额外非法构造/求值检查、重复对、空图异目标、像相容但严格条件不符、输入容器后续修改和普通字段冻结均通过。完整实际运行脚本附后，计数是运行输出而不是手填结论。

这些是有限实现证据，不能证明一般集合上的函数定理，不能构造全Q函数，也没有关于数值近似、实数连续性或形式验证的证明能力。

实际读来源JSON及Markdown的11条请求记录和两个系列：Judson图式函数与Lean/mathlib类型化函数。审计明确注明二者均不能直接充当本书(A,B,G)的同一编码；有对应的相等、空集、限制、复合条件核查。审计记录的许可、固定版本、请求状态可追溯；本代理没有重新发起公开请求，也未运行Lean，不把读审计说成独立网络复验或形式验证。正文所需一般证明已在本书自证，审计不是替代证明。

| 辅助证据文件 | SHA-256 |
| --- | --- |
| `tools/finite_functions.py` | `f863964ff3899de0aa179c3c0bcbc7f8614aff5d08dac1f735d41f66d55528ee` |
| `tools/validate_finite_functions.py` | `d1666d2d0fd866899a11d411481907665b3997531f52bce2ebc0087660000ed2` |
| `research/production/finite_functions_validation.json` | `d34c23d7113fa86a093661ded20d09ce4901d487bceb7cbc00511f9b78a8918b` |
| `research/production/functions_sources_2026-10-29.json` | `2eaf3b39500b459d14a492f1f926b37beb2c6d9e11270f1d9dcad588846d8a34` |
| `research/production/functions_sources_2026-10-29.md` | `213070584976efe530391655f3480d1a96dfb9e6a4eb9c1ddc2e524128f7ee0e` |

## 可重放的独立有限检查

以下Python代码是本次实际执行脚本的逐字内容，不是伪代码。从项目根目录运行；仅用标准库与被审实现，不写仓库报告。可将此代码块提取至临时文件，再用 `PYTHONDONTWRITEBYTECODE=1 python 临时文件` 执行。脚本检查当前主验证报告含6个算例，该断言绑定本批版本。

脚本UTF-8字节SHA-256：`769d68e0924f6941cb820f6d74ae8be4284cd96b2354202894f15cfb15f595e6`。

实际执行输出：

```text
{"boundary_rejections": 14, "candidate_graphs": 8192, "compositions": 90, "invalid": 8174, "mismatches": 234, "triples": 466, "valid": 18}
PASS: relation-subset oracle, function laws, boundaries, immutable copies, source hashes.
```

```python
import hashlib
import itertools
import json
import sys
from dataclasses import FrozenInstanceError
from pathlib import Path

sys.path.insert(0, str(Path.cwd() / 'tools'))
from finite_functions import FiniteFunction, compose, identity, restrict

labels = (-2, 3)
sets = [frozenset(c) for n in range(3)
        for c in itertools.combinations(labels, n)]
universe = list(itertools.product((-2, 3, 7), repeat=2))
counts = dict(candidate_graphs=0, valid=0, invalid=0, compositions=0,
              mismatches=0, triples=0, boundary_rejections=0)
valid = []
for a, b in itertools.product(sets, repeat=2):
    for mask in range(1 << len(universe)):
        graph = [p for i, p in enumerate(universe) if mask & (1 << i)]
        expected = (all(x in a and y in b for x, y in graph)
                    and all(sum(x == u for u, v in graph) == 1 for x in a))
        counts['candidate_graphs'] += 1
        try:
            f = FiniteFunction(a, b, graph)
        except ValueError:
            assert not expected, (a, b, graph)
            counts['invalid'] += 1
        else:
            assert expected, (a, b, graph)
            rows = {x: y for x, y in graph}
            assert f.domain == a and f.codomain == b
            assert set(f.graph) == set(graph)
            assert all(f(x) == rows[x] for x in a)
            assert f.image() == frozenset(rows.values())
            assert FiniteFunction(a, b, graph + graph) == f
            valid.append((f, rows))
            counts['valid'] += 1

for f, fo in valid:
    assert compose(identity(f.codomain), f) == f
    assert compose(f, identity(f.domain)) == f
    for s in sets:
        if s <= f.domain:
            r = restrict(f, s)
            assert r.domain == s and r.codomain == f.codomain
            assert set(r.graph) == {(x, fo[x]) for x in s}
            for t in sets:
                if t <= s:
                    assert restrict(r, t) == restrict(f, t)
    for g, go in valid:
        assert (f == g) == (f.domain == g.domain
                           and f.codomain == g.codomain and fo == go)
        if f.codomain != g.domain:
            try:
                compose(g, f)
            except ValueError:
                counts['mismatches'] += 1
            else:
                raise AssertionError('strict mismatch accepted')
            continue
        c = compose(g, f)
        assert c.domain == f.domain and c.codomain == g.codomain
        assert set(c.graph) == {(x, go[fo[x]]) for x in f.domain}
        counts['compositions'] += 1
        for s in sets:
            if s <= f.domain:
                assert restrict(c, s) == compose(g, restrict(f, s))
        for h, ho in valid:
            if g.codomain == h.domain:
                left = compose(h, c)
                right = compose(compose(h, g), f)
                assert left.domain == right.domain == f.domain
                assert left.codomain == right.codomain == h.codomain
                assert left == right
                assert set(left.graph) == {(x, ho[go[fo[x]]]) for x in f.domain}
                counts['triples'] += 1

bad = [([0], [], []), ([0], [0], []),
       ([0], [0, 1], [(0, 0), (0, 1)]),
       ([True], [0], [(True, 0)]), ([0], [False], [(0, False)]),
       ([0], [0], [(False, 0)]), ([0], [0], [(0, False)]),
       ([0.0], [0], [(0, 0)]), ([0], [0], [(0, 0.0)]),
       ([0], [0], [(0,)]), ([0], [0], [(0, 0, 0)])]
for data in bad:
    try:
        FiniteFunction(*data)
    except ValueError:
        counts['boundary_rejections'] += 1
    else:
        raise AssertionError(data)
f = FiniteFunction([0], [0], [(0, 0), (0, 0)])
assert f.graph == frozenset({(0, 0)})
for x in [False, 0.0, 1]:
    try:
        f(x)
    except ValueError:
        counts['boundary_rejections'] += 1
    else:
        raise AssertionError(x)

f = FiniteFunction([0], [0, 1], [(0, 0)])
g = identity([0])
assert f.image() <= g.domain
try:
    compose(g, f)
except ValueError:
    pass
else:
    raise AssertionError('image compatibility silently accepted')
assert FiniteFunction([], [], []) != FiniteFunction([], [0], [])
assert restrict(identity([0, 1]), [0]) != identity([0])

a, b, graph = [-2, 3], [-2, 3], [[-2, -2], [3, 3]]
f = FiniteFunction(a, b, graph)
a.clear()
b.append(7)
graph[0][1] = 3
assert f == identity([-2, 3])
try:
    f.domain = frozenset()
except FrozenInstanceError:
    pass
else:
    raise AssertionError('attribute mutable')

report = json.loads(Path('research/production/finite_functions_validation.json').read_text())
assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest() == digest
           for p, digest in report['source_sha256'].items())
assert len(report['examples']) == 6
first = FiniteFunction([0, 1], [2, 3, 4], [(0, 2), (1, 3)])
second = FiniteFunction([2, 3, 4], [5, 6], [(2, 5), (3, 5), (4, 6)])
assert compose(second, first) == FiniteFunction([0, 1], [5, 6], [(0, 5), (1, 5)])
print(json.dumps(counts, sort_keys=True))
print('PASS: relation-subset oracle, function laws, boundaries, immutable copies, source hashes.')
```

本次仅新增本审阅报告；未修改作者稿、接受记录、旧检查点、网络/凭据设置或发布产物。主编可按上列四稿哈希登记数学文本范围通过；最终构建、图像与PDF仍须各自实际验收证据。
