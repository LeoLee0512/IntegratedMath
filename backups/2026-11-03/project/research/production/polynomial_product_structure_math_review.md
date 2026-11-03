# B2.16 独立数学审读及配套API审查报告

审阅日期：2026-10-29。审阅人：独立数学审阅代理 `/root/polynomial_next`。作者：`/root/polynomial_math`。审阅结论：下列冻结版本在本单元数学范围内通过；无数学阻断问题。

这份报告只审B2.16，不自审审阅代理撰写的B2.15，也不授予教学、构建、视觉或全章完成状态。作者已写全八题答案并通知冻结后，审阅人按全文读取两份文件，逐段核对一般证明和全部题答；报告不是根据文件存在、程序通过或作者自述推定通过。

## 冻结范围与哈希

| 预期正式路径 | 本次实际读取文件 | SHA-256 |
|---|---|---|
| manuscript/foundations/polynomial_product_structure.md | /tmp/polynomial_product_structure.md | 8dce7a9623ccac953c71113623156c6e0faca5abf82900fdfe3a6f6413e115b8 |
| manuscript/foundations/polynomial_product_structure_answers.md | /tmp/polynomial_product_structure_answers.md | 2342e21afec69515c80f6b8b5063ce0f404efbd8de1c991767fd6be4bbe1c1c2 |

实际正文406行，答案428行。审核末再次计算的哈希与作者冻结通知一致。正式安装后已逐字节比较两份正文与答案（也记录前置PM两稿版本），均与实际审读的临时冻结稿完全一致。任何后续修订均需重新核对，不可继续沿用本报告的通过结论。

## 定义与先修核验

多项式是规范非空系数记录，零记录(0)、零次数未定义、C(a)、S(P)、卷积乘法⋆、数乘aP及求值E_P的对象类型与B2.13—B2.15一致。正文没有提前定义一般多项式幂；第7节仅定义平方P²=P⋆P，区分X²与有理数a²，并用C(a²)衔接。

逐一核对PR3/4/5/6、PO2/3/4、SUM1—5、自然数前驱/比较/差、POW递推及有理零积的现有锚。新PM1、PM3、PM4、PM5接口已在所读B2.15暂存正文中实际证明；本报告以这些命题作为已完成数学先修来检查B2.16依赖方向，并不替代B2.15自身的独立审阅。

全部正文与答案的内部链接已脚本检查。最初临时拼接时待组装的来源锚`poly-product-sources`现已在正式来源Markdown中实际存在；正式化时已读取该文件并绑定来源JSON/Markdown当前版本。最后一次来源行修正明确区分库的一般移位S_h与本批只实现的单步S，本人已重读该行，未引入正文额外先修。未将链接闭合等同于最终构建或页面验收。

## 一般证明审读

1. **可表示长度。** 第1节与题1答案按正原记录长度分支，单项记录直接取T=0，未对空记录调用N。长度至少二时尾记录仍非空。归纳命题是“能由n+1项原记录表示”，故全零尾部或规范化缩短不会破坏归纳假设。全部自然指标的分解已核，n=1和全零长记录均覆盖。
2. **PL1结合律。** 固定P,Q，常量R=C(a)起点由PM4常量和右标量相容得到，两边等于a(P⋆Q)。后继步R=C(a)+S(T)将两侧分别化成a(P⋆Q)+S((P⋆Q)⋆T)及a(P⋆Q)+S(P⋆(Q⋆T))。每一步只用先证分配、标量、PM5移位；归纳假设只用于原记录少一项的T。没有以“移位等于乘X”偷用结合律，也没有多重求和换序。正项数前驱覆盖全部R。
3. **移位求值。** 先使用PR5允许未规范但等价的记录，再用SUM4将首项零与n项尾部连续分开。尾部正确读取t^(j+1)，按有理幂递推及有理因子交换得到t(a_j t^j)，SUM1/2适用。t=0、P=0都包含；未除以t。
4. **PL2乘积求值。** 固定P,t，按Q的可表示长度归纳；起点和后继的形式变形均先用PM4/5建立，再由PO4、移位引理和当前T的归纳假设求值。aE_P+t(E_PE_T)=E_P(a+tE_T)仅在有理数中整理，允许E_P=0。没有借求值函数相等反推形式相等，也未假设一般双重和。
5. **PL3最高项。** 每个卷积自然差k−i先有i≤k。k>d+e时若i≤d且k−i≤e则k≤d+e矛盾，否则至少一个系数零。k=d+e时分i<d、i=d、i>d；前后项零，仅留下c_P(d)c_Q(e)。SUM4分d项、1项、e项正确，d=0/e=0使用空和而非负索引。由有理零积先得乘积此系数非零，随后才定义积次数d+e。零输入另由PM4处理，不使用deg0。
6. **零积与消去。** 双向零积结论由PM4零乘法和PL3非零积推导。消去先展开P(Q−R)，要求共同因子非零，再从差为零逐系数加回，最后PR4。零共同因子反例C(0)与C(1)正确。
7. **PL4及方程。** X先作为规范记录(0,1)定义，再由PM5和单位证明X⋆P=S(P)，依赖方向正确。C的加、乘、相反数相容与单射性都从位置零/一项记录得到。平方差的两次分配及交叉项消去合法；答案补出了逐系数的消去式。求值向有理恒等式传递使用已证PL2。方程限定Q，零积先穷尽两个候选，再分别代回确认，未除以可能为零的t−2。

## 八题完整答案逐题核验

- 题1：两种长度分支、全零长记录、全部系数相同以及归纳性质理由完整。
- 题2：常量起点、后继左右展开、合法尾对象及最终量词覆盖齐全，未用待证结合律。
- 题3：两条卷积路线均独立展开，得到(0,2,−1,−1)；候选尾零与规范化正确，明确单个算例不代替全称证明。
- 题4：从未规范原始表出发的SUM1/2/4应用完整；t=0、P=0及t=2但E_P=0的边界核对正确。
- 题5：可表示长度归纳、零尾部、零输入、零求值三个不同边界都覆盖；因子整理不含除法。
- 题6：卷积(−1,3,−2,6)，次数2+1=3、最高系数2·3=6正确；改零输入后明确不写零对象的次数或最高次系数。
- 题7：超过最高指标与最高指标本身分开证明，先判非零再写次数；空段、零积双向性、左右消去及反例完整。
- 题8：X与C接口、平方定义、逐系数交叉项消去、求值、方程候选必要性与充分性、非法除法丢解解释均完整。

## 辅助检查及限度

正文17个锚，答案9个锚，无重复；题/答前缀各01—08；显示公式分隔成对（正文36对、答案46对）。这些只是结构检查，不代替数学审读。

另用独立的稀疏系数字典与Fraction算术核对题3两种括号，均得到{1:2,2:−1,3:−1}；题6得到{0:−1,1:3,2:−2,3:6}。该有限核验只检查具体算例，不是一般结合律或次数定理的证据。

阻断问题：无。数学修订请求：无。正式路径哈希一致性与来源附录锚已核；教学、构建及实际页面检查由各自独立证据承担，本报告不得作为这些范围已经通过的证据。


## 正式安装时的全部版本绑定

以下SHA在正式仓库重新计算。B2.16两稿属于本报告的独立正文审读范围；B2.15两稿只绑定已引用前置接口的版本，本人是其作者，不将它们列为自我独立审读通过。B2.15须使用另一审阅者的报告。五份代码及JSON诊断属于下附实际执行的独立API审查；来源两文件用于固定条件与许可记录，不声称本审阅人重新执行外部网络抓取。

```json
{
  "manuscript/foundations/polynomial_multiplication.md": "048a6c96c9297cae0a4c2ee3e040a5265640515c31433dd06d615690af0f249d",
  "manuscript/foundations/polynomial_multiplication_answers.md": "4bab95e111a375b72a1b6b66675e447714f3158261790218209f508b46fc6cc1",
  "manuscript/foundations/polynomial_product_structure.md": "8dce7a9623ccac953c71113623156c6e0faca5abf82900fdfe3a6f6413e115b8",
  "manuscript/foundations/polynomial_product_structure_answers.md": "2342e21afec69515c80f6b8b5063ce0f404efbd8de1c991767fd6be4bbe1c1c2",
  "tools/rational_polynomial_product.py": "a8fac5ff74d635c6b9b9fe3454ec9f1279f0cf6ca8cb3bcaf782496fd4d63246",
  "tools/validate_rational_polynomial_product.py": "a092019a0dbc7fe65783e6e8464ea1656bd162cedd04a7626714f82a2d1b11bd",
  "tools/rational_polynomial_basic.py": "4ab57898877c291e338241126e36ed79d4aeef8723c23e647f3591afbcf2243d",
  "tools/rational_powers_sums.py": "fad8cf2a22151b4d584ba09ea3464526668cf34d2737afdf0374f241f16cfda4",
  "tools/linear_equation_solvers.py": "c3ec0ab4a892397d3d0af59a1acd367bf1f1cfea80e3e14bd6b2b6cd790b74c9",
  "research/production/rational_polynomial_product_validation.json": "57141446d654b4c5f82b4ff713b594da40bc86e7498e705fe52e69abb19cb47f",
  "research/production/polynomial_product_sources_2026-10-29.json": "2265e01989e281845c5df2a5c315dcc709907d1c454ed2f6961a5f60e002913b",
  "research/production/polynomial_product_sources_2026-10-29.md": "ada4257f2a713edf86ce91cd942aad03fde9f28e9d86f9ff1f09bcd072fdbe27"
}
```

## 配套API的独立审查附录

下文为本审阅人实际完成的API审查，含完整回放代码及其实际输出。正式化只复核了当前五份代码、正式JSON报告和已运行脚本的字节/哈希，没有重复扩大测试。另从下方Python代码块抽取代码，确认与实际执行脚本逐字节相同，SHA与输出内replay_sha256一致。此API证据可供其他报告明确引用；引用者不得声称自己运行了本次独立实验。

### 多项式移位与乘法API独立数学审查

审查日期：2026-10-29。审查人：独立代理 `/root/polynomial_next`。

结论：下列五份源文件的当前版本与正式有限验证报告一致；代码审读及本次独立递归oracle有限核验通过，没有阻断问题或需修改API的问题。未修改正式代码、验证器或报告。此范围是API与有限验证的审查，不是本人所写B2.15的自审，也不改变已单独通过的B2.16数学稿件报告。

## 静态审读

实际全文读取新API `tools/rational_polynomial_product.py`、其正式验证器及当前JSON报告，并检查调用链 `rational_polynomial_basic.py`、`rational_powers_sums.py` 与 `linear_equation_solvers.rational`。

- `shift`先由record校验完整输入，再前接有理零并规范化。零记录仍返回一项Fraction(0)，原记录不会被修改。
- `multiply`在任何乘积运算前分别调用record校验两侧；零输入没有提前返回，因此另一侧的非法记录及非法尾项仍被拒绝。输入必须为实际list或tuple，非空；系数必须恰为int或Fraction，bool/float及子类不获隐式转换。
- 两输入实际长度n,m为正，候选数组n+m项合法。两层循环下标i+j最高为n+m−2，所以最后一项保持零；这是正文允许的多一尾零，不是越界或次数错误。候选只累加精确Fraction，规范化后仍为非空tuple、每项为Fraction。
- 规范化在校验全记录后仅删尾零，不删除首零或中间零。degree对零显式抛ValueError，符合书稿零次数未定义；求值使用精确幂和有限和，本次另用Horner独立比对。
- 正式验证器用SymPy QQ多项式生成独立参考积，有限范围含84记录、7056对、1728三元组。读遍所有循环和示例后，核对报告计数与范围、源哈希、版本信息及有限验证边界，未发现漏报或把有限计算冒充一般证明。正式报告没有单独宣称覆盖本次补测的全部非法类别及消去条件，本报告补充这些边界，不反向扩大原报告范围。

## 独立oracle与实际运行

本次oracle没有导入SymPy，也不抄写生产双循环卷积。将第一个因子保存为稀疏系数字典，按第二因子的非空记录递归，使用P·(C(a)+S(T))=aP+S(P·T)。稀疏加法、缩放、移位、规范输出和Horner求值均在回放脚本中独立实现，没有调用生产normalize/add/scale/multiply来生成参考结果；生产add/scale只出现在被测试组合中。

记录范围为系数{-2/3,0,3/2}的1—3项记录，另加四份含整数、负分数、内部零及长尾零的记录，共43份。点集{-3/2,0,2/3,2}。三元组使用相同系数的1—2项记录，共12³=1728组。非法输入共51类代表案例；对每例检查shift及multiply两侧，另一侧分别取短零、长零、非零常量、非零混合分数记录，共459次拒绝检查。包含空记录、非list/tuple、容器子类、bool/float/非有限float/complex/字符串/Decimal/嵌套容器/数字子类，以及两个零之后的非法尾项。

实际命令（退出码0）：

```bash
python /tmp/polynomial_product_recursive_review.py /workspace/IntegratedMath-book > /tmp/polynomial_product_recursive_review_result.json
```

全部乘积对核查递归参考、交换、左右移位、两侧非对称尾补零、数乘、求值、零积及非零次数/最高系数。每个零积均检查degree拒绝。三元组核查两种结合、左右分配；共同因子非零时核查两侧消去的等价条件，并显式保留一个零因子消去失败反例。还核验list输入与不可变性。

计数是具体执行范围，不是总体正确率或一般定理。一次非法输入代表某种类型，不等于枚举Python全部可能对象；函数对所有合法记录的数学解释仍由源代码审读及已证明系数规则支持。

## 当前绑定与实际结果

下面是本次脚本实际输出，含五份源文件、正式报告与回放脚本的SHA-256。报告导入最终审查证据前应复核这些绑定；代码或报告变化使这份证据需重新核对。

```json
{
  "status": "passed",
  "counts": {
    "shift_evaluations": 172,
    "records": 43,
    "immutability": 43,
    "tail_padding": 5547,
    "scalings": 5547,
    "product_evaluations": 7396,
    "nonzero_degree": 1521,
    "pairs": 1849,
    "zero_degree_rejections": 328,
    "nonzero_cancellation_triples": 1440,
    "triples": 1728,
    "zero_cancellation_counterexamples": 1,
    "invalid_input_rejections": 459,
    "invalid_input_cases": 51
  },
  "source_sha256": {
    "tools/rational_polynomial_product.py": "a8fac5ff74d635c6b9b9fe3454ec9f1279f0cf6ca8cb3bcaf782496fd4d63246",
    "tools/validate_rational_polynomial_product.py": "a092019a0dbc7fe65783e6e8464ea1656bd162cedd04a7626714f82a2d1b11bd",
    "tools/rational_polynomial_basic.py": "4ab57898877c291e338241126e36ed79d4aeef8723c23e647f3591afbcf2243d",
    "tools/rational_powers_sums.py": "fad8cf2a22151b4d584ba09ea3464526668cf34d2737afdf0374f241f16cfda4",
    "tools/linear_equation_solvers.py": "c3ec0ab4a892397d3d0af59a1acd367bf1f1cfea80e3e14bd6b2b6cd790b74c9"
  },
  "formal_report_sha256": "57141446d654b4c5f82b4ff713b594da40bc86e7498e705fe52e69abb19cb47f",
  "replay_sha256": "5f01bc509ab9d3e9015daba870fe2a64d9e7c8e9057466d46f35ea6bf0b24365",
  "oracle": "recursive C(a)+S(T) with independent sparse arithmetic and Horner",
  "limits": "Bounded exact checks only, not general mathematical proofs."
}
```

## 完整可回放代码

下列代码与实际执行文件逐字一致；保存为 `polynomial_product_recursive_review.py`，可将命令第一个参数改为完整仓库根目录。正式JSON报告必须已存在且绑定当前源文件，脚本会核验而不改写它。

```python
"""Independent bounded API review using recursive constant-plus-shift products."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from decimal import Decimal
from collections import Counter
import hashlib
import json
import sys

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else '/workspace/IntegratedMath-book').resolve()
sys.path.insert(0, str(ROOT / 'tools'))
from rational_polynomial_product import multiply, shift
from rational_polynomial_basic import evaluate, degree, add, scale

counts = Counter()


def sparse(record):
    return {i: F(a) for i, a in enumerate(record) if a != 0}


def plus(a, b):
    result = a.copy()
    for i, v in b.items():
        result[i] = result.get(i, F(0)) + v
        if result[i] == 0:
            del result[i]
    return result


def scaled(a, q):
    return {i: v * q for i, v in a.items() if v * q != 0}


def moved(a):
    return {i + 1: v for i, v in a.items()}


def recursive_product(a, right):
    # Q=C(q0)+S(T). No pairwise coefficient convolution and no production calls.
    head = scaled(a, F(right[0]))
    if len(right) == 1:
        return head
    return plus(head, moved(recursive_product(a, right[1:])))


def canonical(a):
    if not a:
        return (F(0),)
    return tuple(a.get(i, F(0)) for i in range(max(a) + 1))


def horner(record, at):
    value = F(0)
    for q in reversed(record):
        value = value * at + q
    return value


def exact(actual, expected):
    assert type(actual) is tuple
    assert all(type(q) is F for q in actual)
    assert actual == expected, (actual, expected)


values = (F(-2, 3), F(0), F(3, 2))
records = [a for n in (1, 2, 3) for a in product(values, repeat=n)]
records += [(0, 0, 0, 0), (1, 0, -2, 0, 0), (F(-5, 7), 0, 0), (0, 1, 0, 0)]
points = (F(-3, 2), F(0), F(2, 3), F(2))
for a in records:
    expected = canonical(moved(sparse(a)))
    exact(shift(a), expected)
    exact(shift(list(a)), expected)
    exact(multiply(a, (1,)), canonical(sparse(a)))
    exact(multiply((1,), a), canonical(sparse(a)))
    for t in points:
        assert evaluate(a, t) == horner(a, t)
        assert evaluate(shift(a), t) == t * horner(a, t)
        counts['shift_evaluations'] += 1
    aa = list(a)
    saved = aa.copy()
    shift(aa)
    multiply(aa, aa)
    assert aa == saved
    counts['records'] += 1
    counts['immutability'] += 1

for a, b in product(records, repeat=2):
    oracle = recursive_product(sparse(a), b)
    expected = canonical(oracle)
    actual = multiply(a, b)
    exact(actual, expected)
    exact(multiply(b, a), expected)
    exact(multiply(list(a), list(b)), expected)
    exact(multiply(shift(a), b), canonical(moved(oracle)))
    exact(multiply(a, shift(b)), canonical(moved(oracle)))
    for tail_a, tail_b in ((1, 0), (0, 2), (2, 3)):
        exact(multiply(a + (0,) * tail_a, b + (0,) * tail_b), expected)
        counts['tail_padding'] += 1
    for scalar in (F(-4, 5), F(0), F(2)):
        target = canonical(scaled(oracle, scalar))
        exact(multiply(scale(scalar, a), b), target)
        exact(multiply(a, scale(scalar, b)), target)
        counts['scalings'] += 1
    for t in points:
        assert evaluate(actual, t) == horner(a, t) * horner(b, t)
        counts['product_evaluations'] += 1
    zero_a, zero_b = not sparse(a), not sparse(b)
    assert (actual == (F(0),)) == (zero_a or zero_b)
    if not zero_a and not zero_b:
        da, db = max(sparse(a)), max(sparse(b))
        assert degree(actual) == da + db
        assert actual[-1] == sparse(a)[da] * sparse(b)[db]
        counts['nonzero_degree'] += 1
    else:
        try:
            degree(actual)
        except ValueError:
            counts['zero_degree_rejections'] += 1
        else:
            raise AssertionError('zero degree was defined')
    counts['pairs'] += 1

small = [a for n in (1, 2) for a in product(values, repeat=n)]
for a, b, c in product(small, repeat=3):
    expected = canonical(recursive_product(recursive_product(sparse(a), b), c))
    exact(multiply(multiply(a, b), c), expected)
    exact(multiply(a, multiply(b, c)), expected)
    left_sum = plus(sparse(a), sparse(b))
    exact(multiply(add(a, b), c), canonical(recursive_product(left_sum, c)))
    right_sum = plus(sparse(b), sparse(c))
    exact(multiply(a, add(b, c)), canonical(recursive_product(sparse(a), canonical(right_sum))))
    if sparse(a):
        assert (multiply(a, b) == multiply(a, c)) == (sparse(b) == sparse(c))
        assert (multiply(b, a) == multiply(c, a)) == (sparse(b) == sparse(c))
        counts['nonzero_cancellation_triples'] += 1
    counts['triples'] += 1
assert multiply((0,), (0,)) == multiply((0,), (1,))
assert sparse((0,)) != sparse((1,))
counts['zero_cancellation_counterexamples'] += 1


class IntSubclass(int):
    pass


class FractionSubclass(F):
    pass


class ListSubclass(list):
    pass


class TupleSubclass(tuple):
    pass


bad_records = [[], (), None, 1, F(1), True, 1.0, 1j, '1', b'1',
               {0: 1}, {1}, frozenset({1}), range(1), iter([1]),
               ListSubclass([1]), TupleSubclass((1,))]
bad_coefficients = [True, False, 1.0, float('nan'), float('inf'), 1j,
                    '1', b'1', None, Decimal('0.5'), [], (), {0: 1},
                    {1}, object(), IntSubclass(1), FractionSubclass(1, 2)]
bad_records += [[bad] for bad in bad_coefficients]
bad_records += [[0, 0, bad] for bad in bad_coefficients]
for bad in bad_records:
    calls = [(shift, (bad,))]
    for valid in ((0,), (0, 0, 0), (1,), (1, F(-1, 3), 0)):
        calls += [(multiply, (bad, valid)), (multiply, (valid, bad))]
    for fn, args in calls:
        try:
            fn(*args)
        except (TypeError, ValueError):
            counts['invalid_input_rejections'] += 1
        else:
            raise AssertionError(('invalid input accepted', type(bad), fn.__name__))
    counts['invalid_input_cases'] += 1

paths = ['tools/rational_polynomial_product.py', 'tools/validate_rational_polynomial_product.py',
         'tools/rational_polynomial_basic.py', 'tools/rational_powers_sums.py',
         'tools/linear_equation_solvers.py']
bindings = {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in paths}
formal_path = ROOT / 'research/production/rational_polynomial_product_validation.json'
formal = json.loads(formal_path.read_text())
assert formal['status'] == 'passed'
assert formal['source_sha256'] == bindings
assert formal['counts'] == dict(records=84, pairs=7056, evaluations=35280,
                                padding=21168, scalings=21168, triples=1728,
                                rejections=33, immutability=84)
print(json.dumps(dict(status='passed', counts=dict(counts), source_sha256=bindings,
                     formal_report_sha256=hashlib.sha256(formal_path.read_bytes()).hexdigest(),
                     replay_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                     oracle='recursive C(a)+S(T) with independent sparse arithmetic and Horner',
                     limits='Bounded exact checks only, not general mathematical proofs.'),
                 ensure_ascii=False, indent=2))
```

阻断问题：无。API修订建议：无。本报告不登记整章、正文审读、图像或最终PDF构建通过；有限检查不替代全称证明。
