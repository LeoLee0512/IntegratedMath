# B2.4 逆函数与原像：独立数学审阅

审阅日期：2026-10-29 UTC。审阅人：`/root/astra_review`，独立数学审阅代理。

**结论：以下冻结正文与八题完整答案通过数学文本审阅，无未解决阻断。** 已逐段全文读正文319行和答案312行，包括全部INV1—INV5、例反例、八题题面及全解；后续两处措辞修订与新增有限图例说明均实际复读。没有依靠作者或教学审阅人的通过声明代替阅读。本报告不授予最终PDF或整体分类章通过。

## 冻结稿

| 文件 | SHA-256 |
| --- | --- |
| `manuscript/foundations/functions_inverse.md` | `28ffc4f4746286d1407bbe873d9e508d81e7ca82393c76cbf818131e819b9270` |
| `manuscript/foundations/functions_inverse_answers.md` | `d664e0c89bad00817b805b9d3551a4b1d4abc9e8b4f7252cc715f92d4e34b063` |

作者明确冻结后重新核对上述哈希；任何后续源修改须检查差异并更新证据。本批仍接续本地提交2311523，不替换项目。

## 实际先修与背景

B2.1的有序对、函数(A,B,G)、条件子集、空函数和像，以及B2.2的FC1—FC5已在前批实际全文读过，本批重核接口和相关证明位置；目标始终属于函数数据，限制保目标，复合中间集合要求完全相同。B2.3当前正文及全部八解也已独立全文读完，其单射/满射/BJ2与改目标构造可直接作为本单元先修，未反过来借逆函数证明B2.3。所用B2.3版本如下：

| 文件 | SHA-256 |
| --- | --- |
| `manuscript/foundations/functions_bijections.md` | `b8eea358d984c1a13e27b83d24c872ae8f6ef1ca966fd1159788860cb35b79db` |
| `manuscript/foundations/functions_bijections_answers.md` | `8a3a14b86373170fcc2089a20e9a56ce47ac9fb2bff14e3c212202d04a36e324` |

实际回查有理数RA6加法消去、RA7减法/方程、RM8非零乘法消去与RD4乘法方程唯一解；已有加乘分配及相反数规律支持本批全部仿射运算。非零限制落在系数/除数上，不排除零输入或零输出。

本单元直接从B×A筛出逆向图、从A筛出原像，存在性依公开采用的朴素集合背景，不宣称完成公理化集合论。从满射提供当前y的一个见证到单射证明该见证唯一，再以整个逆向图定义函数，没有对一族非唯一原像任意选择。正文不证明或无条件宣称任意满射有右逆，也未把单射无条件推出左逆；空域到非空目标的单射反例边界因而没有被遗漏。

## 一般结果逐项核验

- **INV1。** 逆向图先作为B×A子集定义。f满射提供每个y的至少一个x；f单射使两个可能x相等，因而反向记录是函数。反方向分别用反向记录的存在性推出f满射、唯一性推出f单射。求值等价式始终附x∈A、y∈B，未对域外元素求值。不存在用“已经有逆函数”循环证明反向图合法的问题。
- **INV2。** 双射已经给反向函数B→A，然后证明两次往返分别是A→A与B→B恒等。双侧逆反推单射时把相等输出交给已给h；反推满射时以h(y)作为见证。唯一性链h=h∘id_B=h∘(f∘k)=(h∘f)∘k=id_A∘k=k，每行均B→A，中间链B→A→B→A合法。左逆仅推出单射、右逆仅推出满射，与后面单侧反例一致。
- **INV3。** 把原f视为f⁻¹的双侧逆，先用INV2得f⁻¹双射，再得其唯一逆为f，没有先假定待证逆存在。恒等自逆同样核两侧条件。∅→∅的三数据及往返均正确；∅→非空目标不能有反向函数；非空→∅原函数就不存在。没有把不同目标的空图混同。
- **INV4。** 候选f⁻¹∘g⁻¹:C→A先核类型。从A及C各出发，逐次求值并引用相应逆恒等，得到两条双侧逆等式。FC1使用前确认两端集合相同，再由INV2确定复合双射及候选唯一。顺序必须反转；若某集合为空，给定两双射迫使三集合均为空，因此量词推理仍适用。证明没有调用任意满射的右逆选择。
- **仿射例。** 系数a≠0时候选(y−b)/a属于Q，两个代回均由RD4及加法规律逐步完成；(ax)/a=x用唯一解而非无条件消去。a=0时0、1碰撞，b+1未命中，倒数公式也明确无定义。改目标为{b}只修复满射，限制输入与改目标分别说明。
- **新增有限图例。** q:Q→Q、q(x)=2x+1限制到E={0,1,2}仍保Q目标；再显式改为H={1,3,5}才得有限双射。三个不同输出覆盖H，反向值1↦0、3↦1、5↦2与代码例一致。文本和图注明确有限表不能作为全Q图。这里只审核图例文字与数学数据，未冒称已审PDF中的实际图像。
- **INV5。** 任意f及T⊆B均可定义集合原像，不要求双射。空目标子集原像为空，全B原像为A，两个包含和单调性均有成员论证。复合原像先核g⁻¹[V]⊆B，再对任意x∈A展开三个等价条件；两侧均A子集，故处理了A外元素。该定理不偷用逆函数存在。
- **三种逆记号。** f⁻¹(y)是唯一原输入；1/f(x)是非零数值输出的乘法逆元；f⁻¹[T]是集合。双射时单元素原像等于{f⁻¹(y)}，两边均集合。x+1例中逆函数值与倒数不同，输入−1处倒数不存在而逆函数值仍存在，说明正确。

## 八题完整答案

| 题 | 核验内容 |
| --- | --- |
| 1 | 原图三输入恰覆盖且三输出互异、覆盖目标；逆图(3,2),(4,0),(5,1)正确，两个方向各三个输入全数代回，三数据恒等核验完整。 |
| 2 | u逆图在2处多输出且3处漏输出；v逆图仅漏4；三个原像分别{0,1}、∅、{0}，未把目标4加入原像。 |
| 3 | a≠0双侧代回与a=0无逆的充要分类完整；a=−3/2,b=5/4时f⁻¹(2)=−1/2，乘积3/4加5/4=2核验正确。 |
| 4 | s在±1碰撞；限制到{0,1}为双射自逆；限制到{1}仍保{0,1}目标所以无逆；另改目标才得({1},{1},{(1,1)})自逆。 |
| 5 | g∘f=6x+1，所需逆(z−1)/6；逆序复合经方程6w=z−1证明；错误顺序给(z+3)/6，0处−1/6与1/2不等，两顺序类型均Q→Q。 |
| 6 | 逆值2、倒数1/4、集合{2}与{−1,2}区别清楚；−1处逆值−2而输出倒数无定义；常函数原像Q/∅存在而逆不存在。 |
| 7 | 空函数可逆当且仅当B为空；存在时逆及两个复合的三数据均(∅,∅,∅)；任意子集原像仍为空，无逆不影响原像定义。 |
| 8 | p∘i=id_A而i∘p在1处失败，分别识别p是i的左逆、i是p的右逆；一般L、R以正确类型链证明相等，再明确推出两者均为双侧逆，没有假设二者起初各自双侧。 |

## 发现、修订及边界

提出并关闭两项非阻断精度意见：§8原称“上一节仿射例题”，而仿射在§6，现改为可点击的“第6节仿射例题”；§7原像单元素证明原说“逆函数值的输出”，现明确“原函数f在输入f⁻¹(y)处的输出为y”。已实际复读两处最终文本。新增有限图例也已另行核对，没有遗留数学修改请求。

读了本批来源JSON/Markdown：13条实际公开请求记录、Judson与Lean/mathlib两个系列、固定版本与许可、选择公理及非空条件限制均有说明。本代理读的是审计记录，没有重发这些请求或执行Lean；不将源码阅读视作本书形式验证。来源额外提及的像/原像定理不能自动升级为本书已证内容。

## 有限接口与独立实现检查

全文读旧`finite_functions.py`（哈希与前批相同）、新扩展及主验证器。injective在已合法图中检查输出碰撞；surjective将像与声明目标比较；inverse仅接收双射并将所有有序对反转、交换两端；preimage要求显式整数标签子集T⊆目标并返回定义域子集，不要求可逆。输入bool/float、未经验证函数、域外子集均拒绝。新函数不修改旧图；通过构造器得到的逆仍沿用冻结存储。零输出不会阻止函数逆。

主验证器使用{0,1}全部子集间18个函数，按量词计算预期，报告54性质、7逆、11逆拒绝、53原像、90复合、13逆复合、29反向类型对、7双侧逆、58单侧必要蕴含、22非法拒绝及6算例。已核源码哈希；该报告没有被本审阅覆盖写入。

独立oracle用{-2,0,3}全部8子集作两端，直接枚举三标签平方的512个关系子集，总32768候选，以原始关系成员和每输入记录数判断是否合法。得到170函数、32598拒绝。再用各目标的输入集合大小（纤维大小）判单满射，与实现的seen-set算法分开：86单射、64满射、34双射；136非双射逆拒绝、885原像、5696复合、172逆复合通过。对1369反向类型函数对逐点独立检查两侧恒等，每个双射恰有一个双侧逆，共34对，其他函数没有双侧逆。22项非法API拒绝也通过。完整脚本及实际运行输出附后，可从报告提取重放。

有限枚举只支持此实现，不证明任意集合定理、不证明选择公理、不构造无限Q函数或实数连续图像。一般结论的依据是上面逐项审读的证明。

| 文件 | SHA-256 |
| --- | --- |
| `tools/finite_functions.py` | `f863964ff3899de0aa179c3c0bcbc7f8614aff5d08dac1f735d41f66d55528ee` |
| `tools/finite_function_inverses.py` | `62deba9bc0c408c461a97ae06745f0c81acea0ad6319e6a2582f111826846d3b` |
| `tools/validate_finite_function_inverses.py` | `3e4779af60b4267d74fa791b5a93c1aa7e0879babd747170f3f260ffa8ce2582` |
| `research/production/finite_function_inverses_validation.json` | `9baea4aa5f8be09d923023bad6d29d867378e0746fee3a9a847f562360bb7ae3` |
| `research/production/inverse_functions_sources_2026-10-29.json` | `5c57ba2c72c591d0096c80cada1bf57cd0b03f248dee3a3f6366753f5a16cee8` |
| `research/production/inverse_functions_sources_2026-10-29.md` | `67f9403eccf7aaba9a1564ccdfd07ac9b882bdb7491f1b45faa669ec9b162027` |

## 可重放独立oracle

从项目根目录执行下列完整Python代码；只读取代码和主报告，不写项目文件。建议提取到临时文件后用 `PYTHONDONTWRITEBYTECODE=1 python 临时文件` 运行。

脚本UTF-8字节SHA-256：`9b707738707f2214b32e5908f8062a16076497cad9cdf2d49548fa6293a9bd95`。

实际运行输出：

```text
{"bijective": 34, "candidate_relations": 32768, "compositions": 5696, "functions": 170, "injective": 86, "inverse_compositions": 172, "inverse_rejections": 136, "opposite_type_pairs": 1369, "preimages": 885, "rejected_relations": 32598, "surjective": 64, "two_sided_pairs": 34}
PASS: reverse-graph and fiber oracle; unique two-sided inverse; 22 invalid API cases.
```

```python
import hashlib
import itertools
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path.cwd() / 'tools'))
from finite_functions import FiniteFunction, compose, identity
from finite_function_inverses import injective, surjective, bijective, inverse, preimage

labels = (-2, 0, 3)
sets = [frozenset(c) for n in range(4)
        for c in itertools.combinations(labels, n)]
pairs = list(itertools.product(labels, repeat=2))
relations = [[p for i, p in enumerate(pairs) if mask & (1 << i)]
             for mask in range(1 << len(pairs))]
counts = dict(candidate_relations=0, functions=0, rejected_relations=0,
              injective=0, surjective=0, bijective=0, inverse_rejections=0,
              preimages=0, compositions=0, inverse_compositions=0,
              opposite_type_pairs=0, two_sided_pairs=0)
models = []
for a, b in itertools.product(sets, repeat=2):
    for graph in relations:
        counts['candidate_relations'] += 1
        valid = (all(x in a and y in b for x, y in graph)
                 and all(sum(x == u for u, v in graph) == 1 for x in a))
        try:
            f = FiniteFunction(a, b, graph)
        except ValueError:
            assert not valid
            counts['rejected_relations'] += 1
            continue
        assert valid
        rows = dict(graph)
        fibers = {y: frozenset(x for x in a if rows[x] == y) for y in b}
        inj = all(len(xs) <= 1 for xs in fibers.values())
        sur = all(len(xs) >= 1 for xs in fibers.values())
        assert (injective(f), surjective(f), bijective(f)) == (inj, sur, inj and sur)
        counts['functions'] += 1
        counts['injective'] += inj
        counts['surjective'] += sur
        counts['bijective'] += inj and sur
        models.append((f, rows, inj, sur))
        reverse_pairs = frozenset((y, x) for x, y in graph)
        try:
            r = inverse(f)
        except ValueError:
            assert not (inj and sur)
            counts['inverse_rejections'] += 1
        else:
            assert inj and sur
            assert r.domain == b and r.codomain == a
            assert r.graph == reverse_pairs
            assert inverse(r) == f
            assert compose(r, f) == identity(a)
            assert compose(f, r) == identity(b)
        for t in sets:
            if t <= b:
                expected = frozenset(x for x in a if rows[x] in t)
                assert preimage(f, t) == expected
                counts['preimages'] += 1

for f, ft, fi, fs in models:
    inverse_candidates = []
    for g, gt, gi, gs in models:
        if f.codomain == g.domain:
            c = compose(g, f)
            expected = {(x, gt[ft[x]]) for x in f.domain}
            assert c.domain == f.domain and c.codomain == g.codomain
            assert set(c.graph) == expected
            assert not (fi and gi) or injective(c)
            assert not (fs and gs) or surjective(c)
            assert not injective(c) or fi
            assert not surjective(c) or gs
            counts['compositions'] += 1
            if fi and fs and gi and gs:
                assert inverse(c) == compose(inverse(f), inverse(g))
                counts['inverse_compositions'] += 1
        if f.domain == g.codomain and f.codomain == g.domain:
            left = all(gt[ft[x]] == x for x in f.domain)
            right = all(ft[gt[y]] == y for y in f.codomain)
            assert (compose(g, f) == identity(f.domain)) == left
            assert (compose(f, g) == identity(f.codomain)) == right
            assert not left or (fi and gs)
            assert not right or (fs and gi)
            counts['opposite_type_pairs'] += 1
            if left and right:
                inverse_candidates.append(g)
                counts['two_sided_pairs'] += 1
    assert len(inverse_candidates) == (1 if fi and fs else 0)
    if inverse_candidates:
        assert inverse_candidates[0] == inverse(f)

bad_count = 0
for api in (injective, surjective, bijective, inverse):
    for bad in (None, {}, True, 1):
        try:
            api(bad)
        except ValueError:
            bad_count += 1
        else:
            raise AssertionError('unvalidated argument accepted')
f = identity([0])
for t in (None, [True], [0.0], [1], '0'):
    try:
        preimage(f, t)
    except ValueError:
        bad_count += 1
    else:
        raise AssertionError('bad subset accepted')
try:
    preimage(None, [])
except ValueError:
    bad_count += 1
else:
    raise AssertionError('unvalidated function accepted')
assert bad_count == 22
constant = FiniteFunction([-2, 3], [0, 1], [(-2, 0), (3, 0)])
assert preimage(constant, [0]) == frozenset({-2, 3})
assert preimage(constant, [1]) == frozenset()
zero_output = FiniteFunction([3], [0], [(3, 0)])
assert inverse(zero_output)(0) == 3
report = json.loads(Path('research/production/finite_function_inverses_validation.json').read_text())
assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest() == digest
           for p, digest in report['source_sha256'].items())
print(json.dumps(counts, sort_keys=True))
print('PASS: reverse-graph and fiber oracle; unique two-sided inverse; 22 invalid API cases.')
```

只登记上述冻结文本数学通过。最终图片、链接、页面及PDF构建验收应由各自实际证据承担；本代理未改作者稿、构建器、台账或发布产物。
