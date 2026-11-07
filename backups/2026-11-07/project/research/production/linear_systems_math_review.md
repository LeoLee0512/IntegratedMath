# B2.6 二元一次方程组与可逆消元：独立数学审阅

审阅日期：2026-10-29 UTC。审阅人：`/root/astra_review`。

**结论：下列冻结正文与八题完整答案的数学文本审阅通过，无未解决阻断。** 已实际全文阅读正文295行、答案241行及全部八题题面，检查SYS1—SYS3、所有退化分支、参数族完整性及互异性。作者后来修订的交换后符号说明、题6题名、分类章名称与新增图注均实际复读。没有依其他审阅人结论取代阅读。

## 冻结版本

| 文件 | SHA-256 |
| --- | --- |
| `manuscript/foundations/linear_systems.md` | `a990e27b6c36e0b3f02e468696c89102b3c9e120a77730c8f43b804c8863c46b` |
| `manuscript/foundations/linear_systems_answers.md` | `5c08573cbcd8d99324a8d7d8dcaa42fe6ab09aad8029f2d314a8db5495672a27` |

本批从352bb4d接续。哈希只绑定此文本，不能自动批准后续修改或最终PDF、整章及整部分完成。

## 依赖、定义域与理论范围

本单元候选始终为Q²=Q×Q，解为同一个有理有序对同时满足两式，不是分别找不同的解。B2.1集合/有序对背景、此前有理加乘分配及RD4的非零系数方程唯一性已有实际审读；本次返回核查RA7、RM8、RD4及相关消去条件。B2.5当前两稿也已全文读完，LIN1—LIN3有双向证明且覆盖零系数与允许范围；所用版本为：

| 文件 | SHA-256 |
| --- | --- |
| `manuscript/foundations/linear_equations.md` | `46f013a3d82fa47fc1fdaf73325ed90baf6f7a92bb73e27f1bac98642eed70b4` |
| `manuscript/foundations/linear_equations_answers.md` | `a0b6ca7006d52327c4bddcbe7c48d8a9e3e56eada3f9088d81ca4dae3c90d7b4` |

采用朴素集合、条件子集及有序对按分量判等，不声称已从公理集合论建立所有基础。Q含互异自然数嵌入用于证明参数族确有无限多个解；这与前文整数及有理数嵌入一致。没有以几何交点、矩阵秩、行最简形或行列式定理作为书稿证明前提。Δ仅命名ae−bd这个有理数，后续名称提示不等于借用未教理论。

## SYS1—SYS3逐项检查

**SYS1：每个行操作可撤销。** 交换只改变两个同时条件的次序。某行非零倍乘的反向使用该倍数倒数，另一行保持；倍数零被明确排除。第二行加第一行λ倍的正向用分配律，反向利用仍保留的第一式，从新第二式减回λ倍，因此恢复原式；此处λ允许零。反向不是把两个不知相等的值分别减去，因为保留的一式保证它们相等。丢掉保留式的反例(3,0)确实满足消元式2x=6而不满足原两式。

**SYS2：代入法的完整性。** a≠0先保证x=(c−by)/a是第一式的等价描述。对原解取t=y得到所列参数式及第二式条件；对任何满足附加条件的t，先由除法方程验证第一式，再由条件验证第二式。两个包含都证明，绝非仅生成若干候选。例题得(3,2)，代回两式且用唯一y再唯一x排除其他解。

**消元算例。** 2x+3y=7、4x−y=7保留第一式并令第二式减两倍第一式，剩−7y=−7，依次y=1、x=2。−7与2均非零，代回两条原式为7与7。最终图注与此(2,1)例一致；本报告只核图注和文字数据，不替最终图片或PDF视觉验收。

**SYS3第一层：四系数全零。** a=b=d=e=0时，c=f=0给全Q²；任一常数非零给空集。没有错误地把所有零行视作同一情形，也没有除零。

**SYS3换行层。** 至少一系数行非零时，必要交换使首行非零；交换前后的组合互为相反数，零/非零保持。最终正文明确按交换后的当前位置重新指称六参数并重新记Δ，后面公式因而不会误用旧符号的数值。

**SYS3分支A。** a≠0时保留首行，第二行先乘a再减d倍首行，得到Δy=U，U=af−dc。逆操作先加d倍首行再乘1/a，故双向合法。Δ≠0时y=U/Δ，x=(c−by)/a，两商有定义；在新系统代回，再由等价性得到原系统存在，任何原解依非零系数唯一性只能如此。Δ=0,U≠0给矛盾无解；Δ=U=0时保留首行，解恰为{((c−bt)/a,t):t∈Q}。每个参数满足两原式，每个原解以其第二坐标作为t被收录，且不同t有不同第二坐标。

**SYS3分支B。** a=0,b≠0时保留by=c，第二行先乘b再减e倍首行，得bdx=V，V=bf−ec；反向先加e倍首行再乘1/b。Δ=−bd，故Δ≠0时bd与b均非零，两坐标唯一；Δ=0则由b≠0推出d=0。V非零时无解，V为零时解恰为{(t,c/b):t∈Q}，其必要、充分与参数互异均逐项证明。

这些层次穷尽所有六参数，包括交换前首行0=c而c非零的情况：交换后分类仍检测出矛盾。两参数族以自由坐标直接恢复参数，选互异自然数t给互异解；全Q²也含互异(t,0)。所以“无穷多”有实际依据，不靠仅写出参数字母。Δ=0之后仍查常数，两个同系数反例分别无解及无穷多，未误推Δ=0必无穷。

## 八题题答

| 题 | 核验结果 |
| --- | --- |
| 1 | 四对两式左值依次(5,1)、(5,3)、(5,−1)、(1,1)，仅(3,2)通过；答案明确有限候选核验不证明全Q²唯一。 |
| 2 | 丢掉另一行会接受(3,0)；保留x+y=5后加法可反向恢复，唯一x=3、y=2并代回，完整解集正确。 |
| 3 | 代入x=(1+y)/2得5y=15，解(2,3)；仅除非零2和5，两原式代回为1与8，任意解被迫得到同对。 |
| 4 | 第一行乘6保第二行，再第一行减三倍第二行保第二行，得5y=3；解(8/5,3/5)，原分数等式4/5+1/5=1，另一式为1。恢复操作和唯一性完整。 |
| 5 | 两Δ均零；常数6时全部{(3−2t,t)}，常数7时0=1无解；族的双向完整性和不同t互异均证明。 |
| 6 | 保留x+y=1，第二行减k倍首行得0=m−k，无需除k。m=k给{(1−t,t)}，m≠k给空集；k=0两边界包含。明确此题任何参数都没有唯一解。 |
| 7 | 四支分别Q²、∅、{((4+t)/2,t)}、{(−1,3)}；零式不需除法，交换后2非零，末支仅除2、3；每支充分与必要均说明。 |
| 8 | 第二行乘2再减p倍首行，得到Δy=U，其中Δ=2q−3p、U=2r−5p；反向次序正确。非零Δ候选先核首式，再由2(px+qy)=p(2x+3y)+Δy=2r核次式；零Δ两常数支完整。p=q=r=0仍保留首行，不能变为全Q²。 |

## 发现与闭环

本审阅提出两处需澄清的信息，作者同时修正并给出新冻结版：

- 原SYS3换行后重命名系数，却未足够明确Δ也按新位置重记。最终版先以旧字母说明换行使组合取反，再明确重记，已经复读确认。
- 题6原题名“一个参数控制三个分支”不符合两个固定参数k,m及仅有相容/不相容两类结果。最终改为“倍数行的相容条件”，答案明确任何参数都不产生唯一解。

这两项已关闭，无未解决数学意见。分类章名称“代数教育”的修订不改变证明。未改动作者稿。

## 来源与有限实现检查

读了来源Markdown及JSON的范围、请求记录和许可：OpenStax Elementary Algebra 2e与Beezer A First Course in Linear Algebra两个系列，24请求中23次200、一次误猜仓库404明确保留。OpenStax的实数/图像叙述、Beezer的复数和一般行最简形结果均不被当作本书已具备先修。本文用自己的有理2×2逐支证明；本代理未重新发起那些网络请求，也未以阅读审计替代源稿证明。

全文读solver及主验证器，并复读最终主算例已同步为(2,1)。只接受精确int/Fraction，bool、float及其他类型拒绝。solve_system的零首行/矛盾行、换行、非零a分支、a=0非零b分支均在实际除法前检查系数。输出none/unique/all/line分别表示空集、唯一有理对、全Q²、参数族。`line`只是代码标签；若base=(p,q)、direction=(u,v)，其语义为{(p+tu,q+tv):t∈Q}，不依靠几何直线的预先定义。代码不解析任意表达式，不清未知数分母，不处理额外D限制。

主报告使用SymPy 1.14.0精确solveset/rank/inverse与Fraction代入：125一元、732系统（433唯一、200无解、98单参数、1全Q²）、18300候选对、490参数点、732交换、54非法拒绝及6算例。秩在这里仅是外部程序oracle，不是书稿证明的省略前提。源码哈希与最终报告已核相符。

另写并实际执行独立Fraction oracle：六系数各取{−1,−1/2,0,1/2,1}，共15625组。预期用交叉乘积条件及非零行(r,s,z)的base=(zr/(r²+s²),zs/(r²+s²))、direction=(−s,r)，与生产代码的按a/b选除数消元不同。比较参数族时，不只核几个点：计算t=β+αs并验证α≠0、两个坐标的常数和系数分别相同，由可逆有理换参比较所列两族。有限实例结果为12400唯一、2648无解、576单参数、1全Q²；15625换行、46875保留首行的行加法、31250非零行倍率、2880互异参数点、54非法拒绝均通过。125个含分数系数的一元方程也通过。

此oracle仍是有限代码验证，不代替SYS1—SYS3对任意有理系数的证明。完整脚本与实际输出附后，未覆盖写入主验证报告。

| 文件 | SHA-256 |
| --- | --- |
| `tools/linear_equation_solvers.py` | `c3ec0ab4a892397d3d0af59a1acd367bf1f1cfea80e3e14bd6b2b6cd790b74c9` |
| `tools/validate_linear_equation_solvers.py` | `9050c270f187574f30408605be3818450a9ae33a4ff16fa70732e32a4d85994b` |
| `research/production/linear_equation_solvers_validation.json` | `d00c8b005594d5de3f1a0e745ac20d5bc5b7a5f374c7e2d7b95413cafdfff459` |
| `research/production/linear_equations_sources_2026-10-29.json` | `9a49138e004ff2687e75bf1330eaae2c6e6986b0cdd1338563b780a4717e38ed` |
| `research/production/linear_equations_sources_2026-10-29.md` | `fc2fb71c760aa2ff62db09afa6196b81fc55bc2cc620b6ed2427525e032c03bf` |

## 可重放独立oracle

从项目根目录把下列完整代码提取至临时文件，再用 `PYTHONDONTWRITEBYTECODE=1 python 临时文件` 执行。只读项目代码及主报告，不生成或修改书稿产物。

脚本UTF-8字节SHA-256：`b30de6d0695b55df3ad4c2d79d9bb079be2aa46ffc0651ec3d92d72707166254`。

实际执行输出：

```text
{"all": 1, "invalid_rejections": 54, "line": 576, "line_parameter_points": 2880, "linear": 125, "none": 2648, "nonzero_row_scales": 31250, "row_additions": 46875, "swaps": 15625, "systems": 15625, "unique": 12400}
PASS: scalar-product oracle, exact affine-set equivalence, reversible row operations.
```

```python
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json
import sys

sys.path.insert(0, str(Path.cwd() / 'tools'))
from linear_equation_solvers import solve_linear, solve_system


def oracle(a, b, c, d, e, f):
    delta = a*e-b*d
    if delta:
        return dict(kind='unique', point=((c*e-b*f)/delta, (a*f-c*d)/delta))
    if not any((a, b, d, e)):
        return dict(kind='none' if c or f else 'all')
    if a*f-d*c or b*f-e*c:
        return dict(kind='none')
    r, s, z = (a, b, c) if a or b else (d, e, f)
    norm = r*r+s*s
    assert norm > 0
    return dict(kind='line', base=(z*r/norm, z*s/norm), direction=(-s, r))


def same_set(left, right):
    assert left['kind'] == right['kind']
    if left['kind'] in ('none', 'all'):
        return
    if left['kind'] == 'unique':
        assert left['point'] == right['point']
        return
    p, u = left['base'], left['direction']
    q, v = right['base'], right['direction']
    assert u != (0, 0) and v != (0, 0)
    j = 0 if u[0] else 1
    alpha = v[j]/u[j]
    beta = (q[j]-p[j])/u[j]
    assert alpha != 0
    assert tuple(p[i]+beta*u[i] for i in (0, 1)) == q
    assert tuple(alpha*u[i] for i in (0, 1)) == v
    # The substitution t = beta + alpha*s is bijective on Q.


values = (F(-1), F(-1, 2), F(0), F(1, 2), F(1))
counts = dict(linear=0, systems=0, unique=0, none=0, line=0, all=0,
              swaps=0, row_additions=0, nonzero_row_scales=0,
              line_parameter_points=0, invalid_rejections=0)
for a, b, c in product(values, repeat=3):
    result = solve_linear(a, b, c)
    if a:
        assert result['kind'] == 'unique'
        assert a*result['value']+b == c
    else:
        assert result == dict(kind='all' if b == c else 'none')
    counts['linear'] += 1

for data in product(values, repeat=6):
    a, b, c, d, e, f = data
    expected = oracle(*data)
    result = solve_system(*data)
    same_set(result, expected)
    counts['systems'] += 1
    counts[result['kind']] += 1
    same_set(solve_system(d, e, f, a, b, c), expected)
    counts['swaps'] += 1
    for k in (F(-2), F(0), F(3, 2)):
        same_set(solve_system(a, b, c, d+k*a, e+k*b, f+k*c), expected)
        counts['row_additions'] += 1
    for k in (F(-2), F(3, 2)):
        same_set(solve_system(k*a, k*b, k*c, d, e, f), expected)
        counts['nonzero_row_scales'] += 1
    if result['kind'] == 'unique':
        x, y = result['point']
        assert a*x+b*y == c and d*x+e*y == f
    elif result['kind'] == 'line':
        p, u = result['base'], result['direction']
        assert a*p[0]+b*p[1] == c and d*p[0]+e*p[1] == f
        assert a*u[0]+b*u[1] == 0 and d*u[0]+e*u[1] == 0
        points = []
        for t in values:
            x, y = p[0]+t*u[0], p[1]+t*u[1]
            assert a*x+b*y == c and d*x+e*y == f
            points.append((x, y))
            counts['line_parameter_points'] += 1
        assert len(set(points)) == len(values)

for api, arity in ((solve_linear, 3), (solve_system, 6)):
    for position in range(arity):
        for bad in (None, True, False, 0.5, '1/2', (1, 2)):
            args = [0]*arity
            args[position] = bad
            try:
                api(*args)
            except ValueError:
                counts['invalid_rejections'] += 1
            else:
                raise AssertionError('inexact or invalid coefficient accepted')

report = json.loads(Path('research/production/linear_equation_solvers_validation.json').read_text())
assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest() == digest
           for p, digest in report['source_sha256'].items())
print(json.dumps(counts, sort_keys=True))
print('PASS: scalar-product oracle, exact affine-set equivalence, reversible row operations.')
```

本次批准限上述冻结数学文本及实际审阅范围；最终PDF、图像与链接须由构建和视觉证据另行验收。未修改构建器、台账、网络凭据或发布产物。
