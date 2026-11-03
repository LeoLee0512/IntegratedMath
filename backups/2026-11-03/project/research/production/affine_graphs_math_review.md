# B2.10 仿射图像与方程交点：独立数学复核

审阅者：Astra/high独立数学代理。日期：2026-10-29。结论：正文和8题完整答案数学通过；无待处理数学阻断。

## 定义、AG1—AG5及一般关系

仿射函数先定义为Q→Q的ax+b，a=0也包括；合法性来自精确有理乘加，图成员依定义检验。AG1纵轴始终单点(0,b)；横轴分a≠0唯一(−b/a,0)、a=0且b≠0空、a=b=0整个横轴。截点为有序对、截距为坐标数，负截距不解释为负长度；零函数不能称唯一横截距0。

AG2先用运算律建立所有输入的差式，随后x1≠x2才形成差商并用RD4唯一性得a。相同输入只留下0=0，不给0/0赋值；交换输入的合法差商仍a。斜率无角度或欧氏长度先修。

AG3先定义严格递增、严格递减和常值。充分方向对任意有序输入对用正差及a的符号；三个必要方向明确在全Q中取0<1。审阅建议后已补单点域与空域：两个严格条件可同时无反例，单点恒值，空域可取k=0满足常值，因而不能从退化限制推出原a的符号或为零。

AG4只有不同横坐标的两点才确定仿射族中的唯一Q→Q函数；先非零差商构造，再逐点代回，最后相减求参数并核同域同目标以用FC1。相同横坐标不同输出不可能是函数图；同一点的例子说明不能确定唯一仿射规则。两处相同但第三处不同的合法函数反例限制了“两点确定”的范围。

AG5对交图与两方程逐成员双向转换，求横坐标时保留共同纵坐标条件。a≠c唯一点并代回两式，a=c但b≠d无点，两参数相同全图重合；不同参数t给不同第一坐标，说明重合并非唯一点。示例2x−1与−x+2共点(1,1)及四个轴交点计算正确。

§7固定横坐标V_h合法为集合，但输入h多输出、h+1无输出，所以不是Q→Q图；与仿射图交点恰(h,ah+b)。§8将px+qy=r完整分为q≠0仿射、q=0且p≠0竖向、p=q=r=0全Q²、p=q=0且r≠0空。每次除法先核非零，每种集合描述两向成立；后三类分别违反固定全Q域函数的唯一或存在条件。

## 修订复核

已实际复核作者新增的空/单点域边界、显式仿射函数定义、统一mathsf轴记号、图注样本及空心圈含义说明。AG2负号与分组、AG4第二点和参数唯一、AG5保留纵坐标，以及答案3/4/6的【依据】展开均已读回；各短等式与条件正确。新增图注说明有限样本不等于完整图、墨点符号不排除函数成员；该数学表述正确，本报告不代替图片和PDF视觉审阅。

## 八题完整答案逐项结果

| 题 | 核验结论 |
| --- | --- |
| 1 | 四点依次是/否/是/是；两轴交集{(0,−1)}、{(1/2,0)}，截距与点区分。 |
| 2 | 常值3横交空、纵交(0,3)；零函数横交全轴、纵交原点。两图各两个不同点，不因重复输出否定函数。 |
| 3 | 输出11/4、−1/4、−13/4，两次差商−3/2；任意不同p,q差商同值，p=q只保差式不保商。 |
| 4 | 经(−1,3),(2,−3)的唯一仿射规则−2x+1；参数唯一与两点代回正确。F=x与H=x+x(x−1)在0/1同值、2处2/4不同。 |
| 5 | 3/2正斜率严格增，−2/3负斜率严格减，4常值；任意输入对证明成立性质，用0/1反例排除其余性质。 |
| 6 | 2x+1与−x+4唯一交点(1,3)，代回两式；与2x+4交空，不凭图像判平行。 |
| 7 | k≠2唯一u=(m−2)/(k−2),v=ku+2；k=2,m≠2空；k=m=2全共同图。k=0已包括且只除−2，不除k。 |
| 8 | V的存在/唯一均失败，与−x+1图交点(2,−1)；一般p,q,r四分支完整，空图不偷换为全Q域合法函数。 |


## 实际审阅与依赖核查

已完整阅读本批四份实际稿件及全部16题完整解答，随后逐项复读作者修订处，不以计划或其他代理的结论代替全文阅读。终稿规模：rational_coordinates.md 395行、rational_coordinates_answers.md 275行、affine_graphs.md 366行、affine_graphs_answers.md 281行。两作者已确认冻结；下方哈希才是本次通过的具体版本。检查四稿内部引用均可定位，来源锚coordinates-affine-sources由构建程序提供。

实际核对既有函数接口：有序对按分量相等、A×B的元素是有序对；函数仍为(A,B,G)，G⊆A×B并对每个输入存在且唯一输出，空域与空目标的边界保持F2。FC1要求域、目标和图，FC2限制保留目标。图可决定域与像，但不能凭图恢复未命中的目标元素。旧B2.7交并仅明说Q的子集，新B2.9已先推广到共同已给U再用于Q²。系统先修把共同解定义为同一有理数对同时满足所有条件；一次方程和有理非零除法提供参数分支及唯一性，次序的三歧性与乘法符号提供九类位置和单调证明。没有为新稿引入实数、完备性、欧氏平面公理或未经教学的矩阵/秩结论。

## 实现与主验证器范围

已全文阅读tools/rational_affine.py及tools/validate_rational_affine.py，并核当前验证JSON中三份源码哈希一致。六个API范围如下：affine_value精确求值；slope_through返回不同横坐标两点确定的(a,b)，同横坐标无论纵坐标相同或不同都拒绝；intercepts分别记录纵轴点与横轴unique/none/all，all特指整个有理横轴而非Q²；intersect_affine返回唯一点/空/重合；classify_linear_relation返回仿射/竖向/全Q²/空；finite_graph_test仅检验给定的有限域、有限目标和有限点集。

数值输入只接受int或Fraction，拒绝bool/float及其他类型，运算使用Fraction；所有除法都位于已核非零分支。有限图容器为list/tuple/set/frozenset，点为两项list/tuple；重复记录和相等分数合并为同一集合成员。全部实际输入先验证形状/类型，随后才判断越界点；格式正确但域外或目标外的记录返回False，而非法形状/数值抛ValueError。存在与唯一都检查，空域空图合法，包括空目标；非空域空目标失败。有限样本不能认证无限函数，也不能替代目标集合的声明；本模块没有自动限制任意D或解析任意题目表达式。

主JSON记录SymPy 1.14.0原式linsolve及精确成员检查：125次求值，500组不同横坐标两点，125组同横坐标拒绝，625组仿射交集及15625次成员，25组截点，125组一般一次关系及3125次成员，32768份有限图，106非法输入和3组重复/空图检查。另记录6个示例结果。这里报告的是已读取并核哈希的主验证器实际输出，不冒称由本审阅者重新执行了该次SymPy运行。

## 本审阅者独立有限oracle

已实际运行独立Fraction脚本，完整代码及输出附于affine_graphs_math_review.md。它不调用被测交点公式来构造预期，也不依赖SymPy：用独立两未知数Gauss–Jordan消元处理原始方程行；比较规范化后行条件及唯一解；对有限图独立穷举候选关系并计每个允许输入的配对数。

七值系数集合{−3,−1,−1/2,0,1/2,1,3}给2401组仿射交集：2058唯一、294无解、49重合。2401组两点中2058可唯一确定、343同横坐标被拒；49组截点，343次求值，343组一般关系及16807次原式成员均一致。有限图采用三个Fraction标签{−1/2,0,2}，对域/目标的全部8×8子集及环境9点的全部512子集，实际检查32768份记录，恰有170份合法函数。另有6个显式重复、空域、空目标、越界、多输出案例。总拒绝计数450包含343个同横坐标及107个非法类型/形状输入，不能把450都称作类型错误。

这些检查只是有限实现证据，不是任意有理参数的证明；一般数学结论来自逐步正文与题解审读。验证脚本的通用消元也不是向书稿增添新的先修要求。

## 来源审计及批准边界

已读本地coordinates_affine来源审计Markdown，并检查JSON的来源、访问摘要和范围记录；没有重新联网抓取。审计保留13次HTTP 200公开访问，OpenStax与mathlib两个来源系列；正式化没有冒充重新访问。OpenStax许可CC-BY-NC-SA-4.0、mathlib Apache-2.0，未复制外部题目或图像。mathlib相关图延拓包含Nonempty和choose!，本书按已有三数据图条件直接证明，没有引入这种任意延拓。未编译Lean，未形式化验证本书。

本审阅建议将来源记录中的非严格单调表述与实际教学范围分开，来源代理已修订：正文只教严格递增/递减与常值；非减/非增仅属相关延伸，不登记为本批已教目标。坐标模型不等于全部欧氏点，也不授予完整解析几何或分类章完成。

本结论仅覆盖下列哈希的数学文本、题答与实现边界。图注的代数坐标和样本声明已核，未给最终PDF逐页视觉批准；没有批准发布、合并或推送。若冻结文本改变，应复核相应差异并更新绑定。

## 四稿最终哈希

| 文件 | SHA-256 |
| --- | --- |
| `manuscript/foundations/rational_coordinates.md` | `13f253560a79cb0eaf336dbebd78cc4cb89ba43937bf9cad6f77dfa67d6c9e48` |
| `manuscript/foundations/rational_coordinates_answers.md` | `fe7b4f82a1a76cbd6ebb8d9ccdfa316da16ed63a70acbd68c1322a82c92f1eb6` |
| `manuscript/foundations/affine_graphs.md` | `1df31c69a925d64179d069cd450bd6a53c876fa55eae8727d394ba01b9438c92` |
| `manuscript/foundations/affine_graphs_answers.md` | `f41cc17b765ac4bc7d33fd6b8c7c9d1bbc7b1c6671f44e22d6f8400850ecbd09` |

## 依赖、源码与审计绑定

| 文件 | SHA-256 |
| --- | --- |
| `manuscript/foundations/functions_definition.md` | `1dee6ffb8bada53f6f09ea4ad908c0a03fd06c937fb685538566175cb9655650` |
| `manuscript/foundations/functions_composition.md` | `806b32944f8253b2e2af3b2a551a25cc0ce6bf17ce51cc6b50216cf28e58a94a` |
| `manuscript/foundations/rationals_order.md` | `db52d14c0642912bc281e22e1846f778bc9aa876d1a6ba22e04d5eb3ae28f3ba` |
| `manuscript/foundations/linear_equations.md` | `46f013a3d82fa47fc1fdaf73325ed90baf6f7a92bb73e27f1bac98642eed70b4` |
| `manuscript/foundations/linear_systems.md` | `a990e27b6c36e0b3f02e468696c89102b3c9e120a77730c8f43b804c8863c46b` |
| `manuscript/foundations/linear_inequalities.md` | `89a72b6ff336ee06f23c19fef9f689d5c091182ce61f09b1f914408f6ca038a6` |
| `tools/linear_equation_solvers.py` | `c3ec0ab4a892397d3d0af59a1acd367bf1f1cfea80e3e14bd6b2b6cd790b74c9` |
| `tools/rational_affine.py` | `e62a96b5f79062d7abf96e73a1795e645ce735932c9af2f57ec2376033261a8c` |
| `tools/validate_rational_affine.py` | `953eabd65e00889a2f1ee26ea41232ed4911ea5c0484eefa0f6d742eac1d9f6d` |
| `research/production/rational_affine_validation.json` | `1c031079d131160857b96ddab6415ef478d63ee6d20e22a203b3518eca428f9f` |
| `research/production/coordinates_affine_sources_2026-10-29.md` | `bdcfbae348b36e4bfa5a1bd00daf3b8e1d97e05cb03a231ab49bffea4858fcd2` |
| `research/production/coordinates_affine_sources_2026-10-29.json` | `292f8e7318dd100689b00cc9afe622f758f3fa8d4d3112e44b1c6ce77a24f45c` |

## 独立oracle完整脚本与实际输出

实际命令：`python -B /tmp/coordinates_affine_astra_oracle.py`。下方代码可原样保存重放；ROOT指当前仓库路径。脚本SHA-256：`2902f96dfbe1cd681b16316fa033751a9a2e6071f356fec292eaa9d1a58e5be6`。

```python
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import sys
ROOT = Path('/workspace/IntegratedMath-book')
sys.path.insert(0, str(ROOT/'tools'))
from rational_affine import (affine_value, slope_through, intercepts,
    intersect_affine, classify_linear_relation, finite_graph_test)
V = (F(-3),F(-1),F(-1,2),F(0),F(1,2),F(1),F(3))
counts = dict(intersections=0, unique=0, coincident=0, disjoint=0,
    point_pairs=0, determined=0, equal_x_rejected=0, intercepts=0,
    relations=0, relation_memberships=0, finite_graphs=0, functions=0,
    rejected_inputs=0, explicit_graph_cases=0, values=0)

def reduce_rows(rows):
    """Independent exact Gauss-Jordan elimination, two unknowns."""
    rows = [[F(v) for v in row] for row in rows]
    lead = 0
    for col in range(2):
        pivot = next((i for i in range(lead,len(rows)) if rows[i][col]),None)
        if pivot is None:
            continue
        rows[lead],rows[pivot] = rows[pivot],rows[lead]
        scale = rows[lead][col]
        rows[lead] = [v/scale for v in rows[lead]]
        for i in range(len(rows)):
            if i != lead:
                scale = rows[i][col]
                rows[i] = [v-scale*w for v,w in zip(rows[i],rows[lead])]
        lead += 1
    if any(not row[0] and not row[1] and row[2] for row in rows):
        return ('none',None)
    nonzero = tuple(tuple(row) for row in rows if row[0] or row[1])
    if len(nonzero) == 2:
        return ('unique',(nonzero[0][2],nonzero[1][2]))
    return ('line',nonzero[0]) if nonzero else ('all',None)

def expect_rejection(fn,*args):
    try:
        fn(*args)
    except ValueError:
        counts['rejected_inputs'] += 1
    else:
        raise AssertionError(('accepted invalid input',fn.__name__,args))

for a,b,c,d in product(V,repeat=4):
    expected = reduce_rows([[-a,1,b],[-c,1,d]])
    actual = intersect_affine(a,b,c,d)
    counts['intersections'] += 1
    if expected[0] == 'unique':
        assert actual == {'kind':'unique','point':expected[1]}
        counts['unique'] += 1
    elif expected[0] == 'none':
        assert actual == {'kind':'none','point':None}
        counts['disjoint'] += 1
    else:
        assert expected[0] == 'line'
        assert actual == {'kind':'coincident','point':None}
        counts['coincident'] += 1

for x1,y1,x2,y2 in product(V,repeat=4):
    counts['point_pairs'] += 1
    expected = reduce_rows([[x1,1,y1],[x2,1,y2]])
    if expected[0] == 'unique':
        a,b = slope_through(x1,y1,x2,y2)
        assert (a,b) == expected[1]
        assert a*x1+b == y1 and a*x2+b == y2
        counts['determined'] += 1
    else:
        expect_rejection(slope_through,x1,y1,x2,y2)
        counts['equal_x_rejected'] += 1

for a,b in product(V,repeat=2):
    actual = intercepts(a,b)
    assert actual['vertical'] == reduce_rows([[-a,1,b],[1,0,0]])[1]
    horizontal = reduce_rows([[-a,1,b],[0,1,0]])
    if horizontal[0] == 'unique':
        assert actual['horizontal_kind']=='unique' and actual['horizontal']==horizontal[1]
    elif horizontal[0] == 'none':
        assert actual['horizontal_kind']=='none' and actual['horizontal'] is None
    else:
        assert horizontal == ('line',(F(0),F(1),F(0)))
        assert actual['horizontal_kind']=='all' and actual['horizontal'] is None
    counts['intercepts'] += 1
    for x in V:
        assert affine_value(a,b,x) == a*x+b
        counts['values'] += 1

for p,q,r in product(V,repeat=3):
    actual=classify_linear_relation(p,q,r)
    expected=reduce_rows([[p,q,r]])
    kind=actual['kind']
    if kind=='affine':
        reconstructed=reduce_rows([[-actual['a'],1,actual['b']]])
    elif kind=='vertical':
        reconstructed=reduce_rows([[1,0,actual['x']]])
    elif kind=='all':
        reconstructed=('all',None)
    else:
        assert kind=='none'
        reconstructed=('none',None)
    assert reconstructed==expected
    assert (kind=='affine') == bool(q)
    counts['relations'] += 1
    for x,y in product(V,repeat=2):
        member=(y==actual['a']*x+actual['b']) if kind=='affine' else (
            x==actual['x'] if kind=='vertical' else kind=='all')
        assert member==(p*x+q*y==r)
        counts['relation_memberships'] += 1

U=(F(-1,2),F(0),F(2))
subsets=[tuple(v for i,v in enumerate(U) if mask>>i&1) for mask in range(8)]
pairs=tuple(product(U,repeat=2))
for domain,codomain in product(subsets,repeat=2):
    for mask in range(1<<len(pairs)):
        graph=tuple(point for i,point in enumerate(pairs) if mask>>i&1)
        inside=all(x in domain and y in codomain for x,y in graph)
        expected=inside and all(sum(x==a for x,y in graph)==1 for a in domain)
        assert finite_graph_test(domain,codomain,graph)==expected
        counts['finite_graphs'] += 1
        counts['functions'] += expected

cases=[
    (([],[],[]),True),(([],[1],[]),True),(([0],[],[]),False),
    (([0,0],[F(1,2),F(2,4)],[(0,F(1,2)),(0,F(2,4))]),True),
    (([0],[0,1],[(0,0),(0,1)]),False),
    (([0],[0],[(1,0)]),False),
]
for args,expected in cases:
    assert finite_graph_test(*args)==expected
    counts['explicit_graph_cases'] += 1
bad=(None,True,False,0.5,'1/2',(1,2))
for fn,args in [(affine_value,[1,0,1]),(slope_through,[0,0,1,1]),
                (intercepts,[1,0]),(intersect_affine,[1,0,0,1]),
                (classify_linear_relation,[1,1,1])]:
    for i in range(len(args)):
        for value in bad:
            altered=args.copy(); altered[i]=value
            expect_rejection(fn,*altered)
for args in [(None,[],[]),([],None,[]),([],[],None),([0],[0],[(0,)]),
             ([0],[0],[(0,0,0)]),([0],[0],[0]),([True],[0],[]),
             ([0],[False],[]),([0],[0],[(0,0.0)]),
             ([0],[0],[(1,0),(0,True)]),([],[],[(0,0),(0,None)])]:
    expect_rejection(finite_graph_test,*args)
print(json.dumps(counts,sort_keys=True,indent=2))
```

```text
{
  "coincident": 49,
  "determined": 2058,
  "disjoint": 294,
  "equal_x_rejected": 343,
  "explicit_graph_cases": 6,
  "finite_graphs": 32768,
  "functions": 170,
  "intercepts": 49,
  "intersections": 2401,
  "point_pairs": 2401,
  "rejected_inputs": 450,
  "relation_memberships": 16807,
  "relations": 343,
  "unique": 2058,
  "values": 343
}
```
