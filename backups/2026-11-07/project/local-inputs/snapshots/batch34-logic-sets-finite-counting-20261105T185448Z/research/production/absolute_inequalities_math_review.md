# B2.8 绝对值条件与有理距离范围：独立数学复核

审阅者：Astra/high独立数学代理。日期：2026-10-29。结论：当前冻结正文和8题完整答案数学通过；无待处理数学阻断。

## 命题、边界与修改复核

ABI1的非严格上界明确复用RAB3；严格上界用固定界与取反的正向、按u正负的反向另行证明。两个外侧等价逐方向按绝对值定义和固定界证明，连接词是包含两者同时成立情形的“或”。四式均对任意有理r成立；负r时外侧可重叠，r=0时严格外侧只删零，没有错误宣称两射线总互不相交。

ABI2逐项核验四关系×r负/零/正共12格。负阈值内空外全，零阈值≤给中心、<空、≥全Q、>删中心；正阈值内侧是交、外侧是并，非严格含两端，严格排两端。正端点次序由2r>0推出；每格有一般证明。可读性修订把原大表拆为负/零表及正值表，已实际重读；零阈值严格外侧用条件集表示，证明中保留双开射线，含义一致。

ABI3先隔离a=0直接比较|b|与r，并细列负/零/正阈值及|b|相对r情形。a≠0才定义c=−b/a、ρ=r/|a|，先证两个商有定义、|a|>0，再由ac=−b及分配律、RAB4得到|ax+b|=|a||x−c|。同除正数保向且可恢复，r与ρ同号；负a没有倒置端点错误。任意额外D以成员双向证明筛选D∩S，空D和中心不属于D均处理。

本审阅提出题1答案中“五分之六不是这里的数”的突兀旁句应改直述；作者改为“所得数5/6大于零”，已重读确认。此为表达精度修订，原算术结果5/6正确。未发现其他待修数学错误。

## 八题逐题核查

| 题 | 独立核验结果 |
| --- | --- |
| 1 | 两有序差为±5/6，距离同为5/6，自距离0；x=1/2的距离1/6仅满足非严格条件。 |
| 2 | x=2分别反驳错用“或”的上界及错用“且”的下界；正确内闭区间及双闭外侧，负一与一之间不被外侧收入。 |
| 3 | 中心−2/3、阈值5/6，端点−3/2及1/6；两向平移和端点绝对值5/6均正确。 |
| 4 | c=2/3、r=−1/0的8个结果与ABI2一致；零阈值严格下界用零判据加三歧性排中心。 |
| 5 | 外侧阈值端点−1和2，≥收入而>排除；中心1/2两式均不满足，外侧用析取。 |
| 6 | [-1,1]与(1,3)无交；改第二为[1,3]恰交{1}，完整双包含论证成立。 |
| 7 | −3x+1的中心1/3、缩放半径2/3；内开(−1/3,1)，外闭两射线。直接负除数两次反向和正因子缩放一致。 |
| 8 | a零/非零及r负/零/正分类全部覆盖；≤和>互补的常数分支正确。D={−1,0,1}依交集筛选，c=2例确实令≤无解、>全D。 |


## 实际阅读与依赖边界

本批四稿均已完整阅读：B2.7正文412行、答案275行，B2.8正文324行、答案335行；两组题目与全部16份答案逐项对应。本报告不是基于作者或另一审阅者的通过声明。随后重新检查了修订位置、当前文件哈希和题答锚点；来源附录锚点由构建程序提供。

复核实际依赖接口：functions_definition公开采用按元素判等及按条件取子集的朴素集合背景，并未声称从公理构造全部集合；linear_equations的表达式有定义、共同D及双向解集等价仍适用。rationals_order的RO2提供三歧性、反对称和严格/非严格混合传递，RO4/RO5提供平移与取反，RO6/RO8明确正负乘除和零因子的区别。rationals_absolute的RAB1给非负性与零判据，RAB3仅给非严格两侧界且允许负上界，RAB4给绝对值乘积，RAB7给有理距离。新稿没有把尚未证明的实数完备性、连续数轴或几何事实当作推导依据。

## 精确代码与有限核算

实际阅读tools/rational_inequalities.py及主验证器。两个solve接口只接受int/Fraction（bool和float不接受），先核四种关系，再按a=0、a正负和绝对值阈值分支求解。区间联合以不可变tuple记录，有限端点为Fraction，None仅是无界标记；空tuple为空集，同端点全闭记录为单点。a≠0的绝对值正阈值分支用正数abs(a)产生有序端点；r=0分别给空、单点、全域、删中心的双开射线。

contains只核其数值输入，并信任求解器产生的区间记录，不是任意记录校验器。内部compare仅核比较符号；不得把它描述成验证任意数值对象的公开解析接口。代码不解析题目表达式、不自动筛选D、不实现一般区间交并规范化，也不证明书中一般定理。

已读主验证器实际JSON输出，核对其中三份源码哈希与当前文件一致：SymPy 1.14.0对500组线性、500组绝对值条件进行1000次完整实区间联合比较，另有10616次有理成员、760次有限端点、36次非法系数、12次非法关系、6次非法成员值和2次显式D筛选检查，6个显式例均通过。这是主验证器的现存运行记录，不冒称本审阅者重新进行了该次SymPy运行。有限端点均为有理数，外部实集合比较后限制到Q是实现证据；书稿的先修及证明仍完全在Q内。

本审阅者另实际运行独立Fraction oracle：七值系数集合{-3,-1,-1/2,0,1/2,1,3}的三位置笛卡尔积，每种四关系，得到1372组线性和1372组绝对值。独立使用operator比较原表达式，收集原表达式阈值点、绝对值转折点及返回端点，检查全部分割点、相邻中点及两端外侧代表点。它不调用生产compare，也独立检查区间成员与contains一致。实际通过11480点、2548区间记录、54非法输入及7显式例。392个a=0、392个第三参数为零、1176个第三参数负值计数跨两类求解器；不能把后两项都称作“绝对值半径”计数。有限枚举及代表点检查不是任意系数上的一般证明。

## 来源与批准范围

实际阅读本地来源审计Markdown及JSON的来源、条件、分类和限制记录。审计有15次成功公开请求，分属OpenStax与mathlib两个系列；本审阅者没有重新联网取证。OpenStax许可记录为CC-BY-NC-SA-4.0，mathlib为Apache-2.0；只据其核条件，没有复制外部题目或图像。审计明确排除“绝对值总严格为正”的局部误述，保留mathlib零逆元约定与本书除零无定义的差异；@[to_additive]源码阅读不等于Lean编译或本书形式验证。

结论只覆盖下列哈希对应的数学文本、16份解答和实现边界。未作最终PDF逐页排版批准，也未批准发布、合并或完整分类章完成；若正文或题答再改，须按差异重审并更新绑定。

## 绑定的四份稿件

| 文件 | SHA-256 |
| --- | --- |
| `manuscript/foundations/linear_inequalities.md` | `89a72b6ff336ee06f23c19fef9f689d5c091182ce61f09b1f914408f6ca038a6` |
| `manuscript/foundations/linear_inequalities_answers.md` | `a5a1878a6e9175bc09a02598fa23035aef867b6817769dfbace506ba3085747c` |
| `manuscript/foundations/absolute_inequalities.md` | `766c49a4d2ef4ab13bab56aebd663c827b2ba49d1b1f1f26ba772f8787bf75c5` |
| `manuscript/foundations/absolute_inequalities_answers.md` | `c0673fd63b78f46fefac4581057de06c7790b282786ceff9d35dfeb76bc7dc88` |

## 依赖与审计证据哈希

| 文件 | SHA-256 |
| --- | --- |
| `manuscript/foundations/functions_definition.md` | `1dee6ffb8bada53f6f09ea4ad908c0a03fd06c937fb685538566175cb9655650` |
| `manuscript/foundations/linear_equations.md` | `46f013a3d82fa47fc1fdaf73325ed90baf6f7a92bb73e27f1bac98642eed70b4` |
| `manuscript/foundations/rationals_order.md` | `db52d14c0642912bc281e22e1846f778bc9aa876d1a6ba22e04d5eb3ae28f3ba` |
| `manuscript/foundations/rationals_absolute.md` | `fe10f17f72f2128cd1ad9230b381fd3da2a000fb36b99c7bf097f9522b87b406` |
| `tools/linear_equation_solvers.py` | `c3ec0ab4a892397d3d0af59a1acd367bf1f1cfea80e3e14bd6b2b6cd790b74c9` |
| `tools/rational_inequalities.py` | `c4c54bceea7c55549a1d27cfecb35bdc8e082e9123ef20c309b20d140d72c254` |
| `tools/validate_rational_inequalities.py` | `6ddee0e0db7d39d9f12e95625978bae63b374098c5a5fc06819a93e399efbfd6` |
| `research/production/rational_inequalities_validation.json` | `dd7c94ca40a8c59d92ee9cce805019d9980a67c7798142082ec64ed95835adbb` |
| `research/production/linear_inequalities_sources_2026-10-29.md` | `6de00de991d757736e19c6823a9b04ed7a5944bdb0984df9c503368cc876b1f6` |
| `research/production/linear_inequalities_sources_2026-10-29.json` | `6c7814d77d7b01d80c822f8d1f7825cc8bf2289a18ad250fcad37580a707cf7c` |

## 独立oracle完整可重放脚本

实际命令：`python -B /tmp/inequalities_astra_oracle.py`。可将下方Python块原样保存再运行；仓库位置见脚本ROOT。脚本SHA-256：`f662cebe6b4c4fb5418fc712d6a06438ed03b50b3ec822994e86d57a4aa8ec2e`。下方输出是本审阅者实际运行取得。

```python
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json
import operator
import sys

ROOT = Path('/workspace/IntegratedMath-book')
sys.path.insert(0, str(ROOT / 'tools'))
from rational_inequalities import solve_linear, solve_absolute, contains

OPS = {'<': operator.lt, '<=': operator.le, '>': operator.gt, '>=': operator.ge}
VALUES = tuple(map(F, [-3, -1])) + (F(-1, 2), F(0), F(1, 2), F(1), F(3))
counts = dict(linear=0, absolute=0, partition_points=0, interval_records=0,
              zero_coefficients=0, negative_thresholds=0, zero_thresholds=0,
              rejected_inputs=0, explicit_examples=0)

def membership(records, x):
    return any((lo is None or x > lo or (x == lo and lc)) and
               (hi is None or x < hi or (x == hi and rc))
               for lo, hi, lc, rc in records)

def validate_records(records):
    assert type(records) is tuple
    for i, record in enumerate(records):
        assert type(record) is tuple and len(record) == 4
        lo, hi, lc, rc = record
        assert type(lc) is bool and type(rc) is bool
        assert lo is None or type(lo) is F
        assert hi is None or type(hi) is F
        assert lo is not None or not lc
        assert hi is not None or not rc
        assert lo is None or hi is None or lo < hi or (lo == hi and lc and rc)
        if i:
            previous_hi, previous_rc = records[i-1][1], records[i-1][3]
            assert previous_hi is not None and lo is not None
            assert previous_hi < lo or (previous_hi == lo and not previous_rc and not lc)
        counts['interval_records'] += 1

def points_between(breaks):
    edges = sorted(breaks)
    if not edges:
        return {F(0)}
    return set(edges) | {edges[0]-1, edges[-1]+1} | {
        (left+right)/2 for left, right in zip(edges, edges[1:])}

for absolute, fn in [(False, solve_linear), (True, solve_absolute)]:
    for a, b, threshold in product(VALUES, repeat=3):
        for relation, op in OPS.items():
            records = fn(a, b, threshold, relation)
            validate_records(records)
            counts['absolute' if absolute else 'linear'] += 1
            counts['zero_coefficients'] += (a == 0)
            counts['negative_thresholds'] += (threshold < 0)
            counts['zero_thresholds'] += (threshold == 0)
            breaks = {end for record in records for end in record[:2] if end is not None}
            if a:
                breaks.add((threshold-b)/a)
                if absolute:
                    breaks.update({(-threshold-b)/a, -b/a})
            for x in points_between(breaks):
                value = a*x+b
                expected = op(abs(value) if absolute else value, threshold)
                assert membership(records, x) == expected, (absolute,a,b,threshold,relation,x,records)
                assert contains(records, x) == expected
                counts['partition_points'] += 1

bad = (None, True, False, 0.5, '1/2', (1,2))
def reject(fn, *args):
    try:
        fn(*args)
    except ValueError:
        counts['rejected_inputs'] += 1
    else:
        raise AssertionError(('accepted invalid argument',fn.__name__,args))
for fn in (solve_linear, solve_absolute):
    for slot in range(3):
        for value in bad:
            args = [1,0,1,'<=']
            args[slot] = value
            reject(fn,*args)
    for relation in ('=', '!=', 'le', None, True, 1):
        reject(fn,1,0,1,relation)
for value in bad:
    reject(contains,(),value)

examples = [
    (solve_linear(F(-2,3),F(-1,3),1,'<='), ((F(-2),None,True,False),)),
    (solve_absolute(-3,1,2,'<'), ((F(-1,3),F(1),False,False),)),
    (solve_absolute(-3,1,2,'>='), ((None,F(-1,3),False,True),(F(1),None,True,False))),
    (solve_absolute(0,0,0,'>'), ()),
    (solve_absolute(0,-1,1,'>='), ((None,None,False,False),)),
    (solve_absolute(2,-1,0,'<='), ((F(1,2),F(1,2),True,True),)),
    (solve_absolute(2,-1,0,'>'), ((None,F(1,2),False,False),(F(1,2),None,False,False))),
]
for actual, expected in examples:
    assert actual == expected
    counts['explicit_examples'] += 1
print(json.dumps(counts, sort_keys=True, indent=2))
```

```text
{
  "absolute": 1372,
  "explicit_examples": 7,
  "interval_records": 2548,
  "linear": 1372,
  "negative_thresholds": 1176,
  "partition_points": 11480,
  "rejected_inputs": 54,
  "zero_coefficients": 392,
  "zero_thresholds": 392
}
```
