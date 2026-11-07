# 一次除式商余API：独立数学与实现审查

日期：2026-10-29。审阅及实际独立实验执行人：`/root/polynomial_next`。

结论：当前正式API及依赖的代码审读、独立精确oracle有限核验通过，无阻断问题。没有修改API、验证器或其报告。该结论只针对API实现及有限检查，不构成本人所写B2.17正文的独立审读；B2.17必须使用另一位审阅人的数学报告。

## 静态对应与输入条件

全文读取正式`tools/rational_polynomial_linear_division.py`，并与原临时实现核对；审查record/add、shift及有理输入校验调用链。正式实现先执行`record(values)`和`rational(at)`，再建立Q=(Fraction(0),)、r=最后系数。倒序读取全部较低系数时，先按旧r执行Q=add(shift(Q),(r,))，然后执行r=当前系数+a*r。这与PD4的初值及同时状态更新一致，不会错误地把新r放入当前商。

输入为至少一项的实际list/tuple，系数及a必须恰为int或Fraction。bool、float、容器子类及数字子类均被显式类型规则排除。全部系数在计算前完成校验；a也在零/常量输入返回前校验。空记录因此不会执行非法的最后项读取，合法一项记录则不进入循环，返回零商及该常量余数。长尾零导致额外合法状态而不会提前停止；中间零照样占据一次乘加步骤。所有运算精确、输出商为非空规范Fraction元组、余数为Fraction；输入list未被修改。

返回类型是二元tuple `(quotient, remainder)`，其中第一个分量是规范多项式记录，第二个分量是有理数；本次核验逐一检查这些类型，未把余数误认成多项式记录。没有定义零商次数，也不解析任意表达式、接受浮点近似或执行一般多项式除法。

正式验证器与其当前JSON亦已全文读取并核对绑定。它采用SymPy QQ除以X−a的参考，实现有限123记录、615除法、1845尾零、2190后缀、43拒绝；这是主编此前执行的诊断，本审阅人不声称重新运行该验证器。本报告下方是本人另行实际执行、参考规则不同的独立核验。

## 独立参考公式与回放范围

对原记录p_0,…,p_(n−1)，独立oracle直接计算

- q_i = sum(p_k*a**(k−i−1), k=i+1,…,n−1)，0≤i<n−1；
- r = sum(p_k*a**k, k=0,…,n−1)。

所有幂是Fraction的非负整数幂，求和从Fraction(0)开始；oracle没有调用生产divide_linear、shift、add、normalize、power或evaluate来生成参考值，没有用生产综合除法的同一递归，也没有用Horner或SymPy。参考结果自己规范化。n=1时商系数候选为空，由oracle内部规则转成合法零商，不改变生产输入必须非空的规定。

参考公式可独立逐系数核对：对正指标k，相邻两有限和相减q_(k−1)−a*q_k只留下p_k；最高位置来自q_(n−2)=p_(n−1)，常数位置r−a*q_0只留下p_0。一项常量单独核。a=0时所有出现的指数仍非负，零次为一，无除法。脚本还独立以系数`q_(k−1)−a*q_k+r*δ_(k,0)`重建原记录，不借生产多项式乘法复核。

记录范围是系数{-3/5,0,1/2,2}的1—4项记录，加四份指定记录（含长全零、三次对象的长尾零、负分数/中间零、六项稀疏记录），共344份；参数为0,1,−2,−2/3,3/5。共1720主除法及重建、5160额外尾零核验、6370后缀除法、1720输入不可变性核验；非零正次数输入1635例检查商非零、次数减一和最高系数，常量/零输入85例检查零商与余数。

非法记录51类代表案例各配三个合法参数，153次拒绝；非法参数17类各配短零、长零、常量和非零记录，68次拒绝。包含bool、浮点及NaN/inf、complex、字符串、Decimal、嵌套容器、类子类型、空/非具体记录及合法零前缀后的非法尾项。五份正文算例另核商余类型、系数和值。类型样本是明确的有限代表集合，不声称枚举所有Python对象。

实际命令（退出码0）：

```bash
python /tmp/polynomial_linear_division_independent_review.py /workspace/IntegratedMath-book > /tmp/polynomial_linear_division_independent_review_result.json
```

## 实际输出及当前绑定

以下为实际独立执行结果，含正式API与四份依赖SHA，以及完整回放代码SHA。生成本报告前已再次核对每份源哈希。

```json
{
  "status": "passed",
  "record_count": 344,
  "point_count": 5,
  "counts": {
    "reconstructions": 1720,
    "zero_or_constant_inputs": 85,
    "tail_padding": 5160,
    "immutability": 1720,
    "suffix_divisions": 6370,
    "divisions": 1720,
    "positive_degree_quotients": 1635,
    "invalid_record_rejections": 153,
    "invalid_point_rejections": 68,
    "text_examples": 5
  },
  "examples": [
    {
      "input": [
        "-6",
        "11",
        "-6",
        "1"
      ],
      "at": "1",
      "quotient": [
        "6",
        "-5",
        "1"
      ],
      "remainder": "0"
    },
    {
      "input": [
        "1",
        "0",
        "2"
      ],
      "at": "2",
      "quotient": [
        "4",
        "2"
      ],
      "remainder": "9"
    },
    {
      "input": [
        "1/2",
        "-1",
        "1"
      ],
      "at": "-1/2",
      "quotient": [
        "-3/2",
        "1"
      ],
      "remainder": "5/4"
    },
    {
      "input": [
        "-3/2"
      ],
      "at": "0",
      "quotient": [
        "0"
      ],
      "remainder": "-3/2"
    },
    {
      "input": [
        "0"
      ],
      "at": "-1/2",
      "quotient": [
        "0"
      ],
      "remainder": "0"
    }
  ],
  "source_sha256": {
    "tools/rational_polynomial_linear_division.py": "6f246113bf509122628e9878a3898d0ce20070eb4447e7ef6fa2cc462c75fb5e",
    "tools/rational_polynomial_product.py": "a8fac5ff74d635c6b9b9fe3454ec9f1279f0cf6ca8cb3bcaf782496fd4d63246",
    "tools/rational_polynomial_basic.py": "4ab57898877c291e338241126e36ed79d4aeef8723c23e647f3591afbcf2243d",
    "tools/rational_powers_sums.py": "fad8cf2a22151b4d584ba09ea3464526668cf34d2737afdf0374f241f16cfda4",
    "tools/linear_equation_solvers.py": "c3ec0ab4a892397d3d0af59a1acd367bf1f1cfea80e3e14bd6b2b6cd790b74c9"
  },
  "replay_sha256": "bbbe97cc76ef57ce40ec1abddb9ca6ff1f0edd09ac53b33e9a8f1848389a69a7",
  "oracle": "explicit finite coefficient sums with Fraction powers; direct reconstruction",
  "limits": "Bounded exact API checks, not a general theorem or parser for arbitrary inputs."
}
```

另行核验但未冒称本次重新运行的正式验证器及其报告绑定如下：

```json
{
  "tools/validate_rational_polynomial_linear_division.py": "61a371a36c570fd99c5a07c3218dd88c1deedd5eedc0bb0387c65a2f73be969e",
  "research/production/rational_polynomial_linear_division_validation.json": "e9f04c2f0e9d84947655f343b96da335475bd181480bc7c812db441df832967c"
}
```

## 完整实际执行代码

将下方代码保存为独立Python脚本，命令第一个参数为完整仓库根目录。代码块已与实际执行文件逐字节核对；报告不依赖临时文件继续存在。

```python
"""Bounded independent exact review, using explicit quotient coefficient sums."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from collections import Counter
from decimal import Decimal
import hashlib
import json
import sys

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else '/workspace/IntegratedMath-book').resolve()
sys.path.insert(0, str(ROOT / 'tools'))
from rational_polynomial_linear_division import divide_linear

counts = Counter()


def canonical(coefficients):
    result = [F(x) for x in coefficients]
    while result and result[-1] == 0:
        result.pop()
    return tuple(result) if result else (F(0),)


def explicit_oracle(values, at):
    p = tuple(F(x) for x in values)
    a = F(at)
    # Closed finite sums, no production calls, synthetic recursion, or Horner.
    quotient = [sum((p[k] * a ** (k - i - 1)
                     for k in range(i + 1, len(p))), F(0))
                for i in range(len(p) - 1)]
    remainder = sum((p[k] * a ** k for k in range(len(p))), F(0))
    return canonical(quotient), remainder


def check_output(result, expected):
    assert type(result) is tuple and len(result) == 2
    quotient, remainder = result
    assert type(quotient) is tuple and len(quotient) >= 1
    assert all(type(x) is F for x in quotient)
    assert type(remainder) is F
    assert quotient == (F(0),) or quotient[-1] != 0
    assert result == expected, (result, expected)


def reconstruct(quotient, remainder, at):
    a = F(at)
    coefficients = []
    for k in range(len(quotient) + 1):
        qk = quotient[k] if k < len(quotient) else F(0)
        previous = quotient[k - 1] if k > 0 else F(0)
        coefficients.append(previous - a * qk + (remainder if k == 0 else F(0)))
    return canonical(coefficients)


values = (F(-3, 5), F(0), F(1, 2), 2)
records = [a for n in (1, 2, 3, 4) for a in product(values, repeat=n)]
records += [(0, 0, 0, 0, 0, 0), (-6, 11, -6, 1, 0, 0),
            (F(1, 2), -1, 1, 0), (1, 0, 0, 0, 0, 2)]
points = (0, 1, -2, F(-2, 3), F(3, 5))
for p, a in product(records, points):
    expected = explicit_oracle(p, a)
    actual = divide_linear(p, a)
    check_output(actual, expected)
    q, r = actual
    assert reconstruct(q, r, a) == canonical(p)
    counts['reconstructions'] += 1
    normalized = canonical(p)
    if len(normalized) == 1:
        assert q == (F(0),) and r == normalized[0]
        counts['zero_or_constant_inputs'] += 1
    else:
        assert q != (F(0),)
        assert len(q) - 1 == (len(normalized) - 1) - 1
        assert q[-1] == normalized[-1]
        counts['positive_degree_quotients'] += 1
    for extra in (1, 2, 4):
        check_output(divide_linear(p + (0,) * extra, a), expected)
        counts['tail_padding'] += 1
    mutable = list(p)
    saved = mutable.copy()
    check_output(divide_linear(mutable, a), expected)
    assert mutable == saved
    counts['immutability'] += 1
    # Every suffix is independently checked, including the one-item base.
    for start in range(len(p)):
        suffix = p[start:]
        check_output(divide_linear(suffix, a), explicit_oracle(suffix, a))
        counts['suffix_divisions'] += 1
    counts['divisions'] += 1


class IntSubclass(int):
    pass


class FractionSubclass(F):
    pass


class ListSubclass(list):
    pass


class TupleSubclass(tuple):
    pass


invalid_coefficients = [True, False, 1.0, float('nan'), float('inf'), 1j, '1', b'1',
                        None, Decimal('0.5'), [], (), {0: 1}, {1}, object(),
                        IntSubclass(1), FractionSubclass(1, 2)]
invalid_records = [[], (), None, 1, F(1), True, 1.0, 1j, '1', b'1', {0: 1}, {1},
                   frozenset({1}), range(1), iter([1]), ListSubclass([1]), TupleSubclass((1,))]
invalid_records += [[bad] for bad in invalid_coefficients]
invalid_records += [[0, 0, bad] for bad in invalid_coefficients]
for bad in invalid_records:
    for a in (0, F(-2, 3), 2):
        try:
            divide_linear(bad, a)
        except (TypeError, ValueError):
            counts['invalid_record_rejections'] += 1
        else:
            raise AssertionError(('invalid record accepted', type(bad)))
for bad in invalid_coefficients:
    for p in ((0,), (0, 0, 0), (1,), (1, F(-1, 2), 0)):
        try:
            divide_linear(p, bad)
        except (TypeError, ValueError):
            counts['invalid_point_rejections'] += 1
        else:
            raise AssertionError(('invalid point accepted', type(bad)))

examples = []
for p, a in [((-6, 11, -6, 1), 1), ((1, 0, 2), 2),
             ((F(1, 2), -1, 1), F(-1, 2)), ((F(-3, 2),), 0), ((0,), F(-1, 2))]:
    result = divide_linear(p, a)
    check_output(result, explicit_oracle(p, a))
    examples.append(dict(input=[str(v) for v in p], at=str(a),
                         quotient=[str(v) for v in result[0]], remainder=str(result[1])))
    counts['text_examples'] += 1

source_paths = ['tools/rational_polynomial_linear_division.py',
                'tools/rational_polynomial_product.py', 'tools/rational_polynomial_basic.py',
                'tools/rational_powers_sums.py', 'tools/linear_equation_solvers.py']
bindings = {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in source_paths}
output = dict(status='passed', record_count=len(records), point_count=len(points),
              counts=dict(counts), examples=examples, source_sha256=bindings,
              replay_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              oracle='explicit finite coefficient sums with Fraction powers; direct reconstruction',
              limits='Bounded exact API checks, not a general theorem or parser for arbitrary inputs.')
print(json.dumps(output, ensure_ascii=False, indent=2))
```

阻断问题：无。修改请求：无。上述有限核验与代码审查不替代PD一般存在唯一证明，不授予正文独立审读、教学、图像或最终PDF构建通过。
