# B2.15 移位、有限倒序与多项式乘法：独立数学复核（正式绑定）

审阅者：B2.16作者代理，独立审阅另一作者的B2.15。日期：2026-10-29。结论：下列冻结版本的B2.15正文与八题全部解答数学通过，无待解决数学阻断。本报告不对本人撰写的B2.16作独立验收；实现与来源的核读和有限证据另节注明，不代表整批或PDF已通过。

## 实际阅读与依赖核对

已在本次任务实际完整读取 `/tmp/polynomial_multiplication.md` 与 `/tmp/polynomial_multiplication_answers.md`，逐题核对八题题面与全部解答。不是依据提纲、作者摘要或只检查锚来作结论。前批PR1—6、PO1—5及其全解已在本代理此前实际完整阅读；本批直接使用的自然差、自然比较、有限和SUM1—5等先修接口此前也已实际核读。再次检查当前PM正文与答案的全部本地链接，已有先修与题答链接均解析；`poly-product-sources` 已在正式来源审计中登记；本报告不声称已实际验收最终PDF跳转。

入口先从两个有理求值表达式相乘给出动机，已明确补充有理幂指数加法的先修，不用尚未证明的多项式乘积求值性质。自然下标加一、结合、交换已有自然加法接口。正式构造及相等判据始终依全部系数，未把有限样本或求值函数相等用于反推形式相等。

## PM1：移位、表示无关与分解

S在非空规范记录开头接零再规范化，得到合法n+1项原始记录。位置零与所有后继位置分别证明系数式；j<n与j≥n覆盖边界，任意正位置由前驱写成j+1。任意尾零表示给相同全指标系数，故PR4给表示独立。移位加法与数乘线性都同时核零位置与后继位置，λ=0未被排除。全零仍规范为(0)，不生成空对象。

常数项分解在至少两项时使用非空尾记录；一项时直接指定T=0，多项式P=C(a)+S(T)逐系数成立，没有调用N(空记录)。这一接口足够支持后续按“能由n+1项表示”归纳，即使尾部全零或规范化缩短，也不漏对象。

## PM2：有限倒序的证明独立完整

(k+1)−(j+1)=k−j先核j≤k与差存在，令r=k−j，通过(j+1)+r=k+1及差唯一性得到。k−(k−i)=i也先核两层差，再用自然加法交换及唯一性。没有借整数负指标补漏洞。

倒序按k归纳，量词覆盖所有长度k+1的表；起点单项。后继用SUM4拆出倒序首项u_(k+1)，后段j对应原倒序位置j+1；已证差式识别后段为原前缀的倒序。归纳假设只用于长度k+1前缀，随后只交换两个已确定的有理加数，再识别求和递推。没有预用任意排列或双和换序。空表不在此命题所量化的k+1项对象内，未制造n−1负索引。

## PM3：乘法候选与全指标良定义

每个b_k读取k+1项；i≤k保证k−i合法，两个补零系数都处处有值。先取规范输入实际正长度n,m，候选长度L=n+m≥2，输出存在。k≥n+m时，i≥n使第一因子零；若i<n又假定k−i<m，则k=i+(k−i)<n+(k−i)<n+m矛盾，故第二因子零。SUM3得整个界外系数零，包括恰好k=n+m的边界。

先分别核k<L与k≥L的系数公式，再宣布结果不依赖任意L′≥n+m。任意原始输入改用其实际项数n′,m′以及覆盖n′+m′的长度，补零系数保持及SUM1使所有b_k不变；PR4结束表示无关证明。没有把“有限支持显然”替代界外证明，也没有把只覆盖规范长度的界误用来读取更长原表。长度n+m不是声称最短长度或次数，例中最后多一项零明确处理。

## PM4—5：运算规律无循环

左常量公式只留下卷积第零项，其余k项零；k=0后段为空，SUM3/4仍适用。a=0/1先得到左零与左单位。左分配逐项有理分配后用同长SUM2；左标量相容先有理结合再SUM2提固定λ，含λ=0。

交换律独立使用PM2倒序，k−(k−j)=j合法，再逐项交换两个有理因子，识别反向乘积系数。右常量、右零与单位、右分配及右标量均在交换律之后推导，没有预用多项式结合律。所有结果由PR4形式判等。

PM5先核位置零；对k+1位置，原和有k+2项，去掉含移位零系数的第零项后，连续后段以i=j+1、j=0…k索引。差式与移位系数式把其识别为b_k(P,Q)，再由PR4得左移位相容。右移位只用已证交换和左移位，不把移位先解释成乘X，也不偷用三因子结合。全部零输入包括在证明内。

## 八题全部解答

| 题 | 实际核验 |
| --- | --- |
| 1 | (1,0,2)移位为(0,1,0,2)，长尾零表示同结果，零仍(0)。前接与尾接含义分清；一般两支系数证明完整。 |
| 2 | 原累加1、−1、2、6，逆序4、7、5、6正确；差合法性、全量词归纳、SUM4后段及两加数交换全部写出。 |
| 3 | 五个系数0、3、−3、6、0逐项展开正确；规范(0,3,−3,6)，内部配对与首零解释正确，逐系数同位置乘积错误被准确定位。 |
| 4 | 短候选四项、长候选七项均规范为(3,5,−2)；长候选后四项零有指标和≤2的理由。一般界外证明及长度/表示独立全覆盖。 |
| 5 | 常量公式第零项与零后段拆分正确，含k=0；a=0、a=1、P=0及重合边界均答，没有借次数。 |
| 6 | 分配用SUM2逐项加，标量用SUM2缩放，λ=0合法；两条具体路线均得到(0,2)，分别乘积(0,1,1)/(0,1,−1)正确。 |
| 7 | 只用一维倒序、自然差与有理因子交换证明乘积交换；(1,1)平方(1,2,1)，错误同位置相乘得(1,1)，索引一/二见证均正确。 |
| 8 | 零指标、k+1后段索引、差恒等式及左右移位推导完整。三条路线均得(0,2,−1,−1)，最后P=0三式各自归零。 |

## 正式迁仓复核与范围

四份正式稿与/tmp冻结稿逐字节相同，B2.15数学批准延续到下表正式路径。表中B2.16两稿仅绑定同批接口背景，本人是其作者，不将字节核验或一般API有限验证转写为对其正文的独立数学批准。B2.16有另一位代理的单独审阅。

B2.15自身没有提前宣称结合律、乘积求值或非零积次数已经在本单元证明；它向后续提供的PM1—5接口与实际证明一致。图注0、3、−3、6及第五个候选尾零与计算一致，本报告没有实际观看最终图片或PDF，不替代构建及视觉验收。未修改正式正文、代码或主验证JSON，未发布或推送。冻结内容变化须复核差异并更新绑定。

## 正式实现与主有限验证

正式整合阶段，本审阅者实际全文读取tools/rational_polynomial_product.py、其验证器与保存的主JSON；所调用record/normalize、幂/有限和及rational类型检查已在前批实际阅读，这次再次校验其源码哈希不变。shift先校验整张非空记录，再前接Fraction(0)并规范化；multiply先校验双输入，不因一侧为零提前忽略另一侧非法项。两重循环把第i、j项乘积累加到i+j；候选长度为n+m，最大可能写入下标n+m−2，最后一项故意为零，和正文PM3允许多一尾零一致。所有系数运算精确，输出规范非空Fraction元组，首/中间零保留。未发现实现与已证系数定义不一致。

主验证器使用SymPy 1.14.0的QQ多项式作有限参考，保存记录为84张、7056配对、35280求值、21168尾补零、21168缩放、1728三元组、33拒绝和84输入不变性；各类计数的循环与声明范围相符。五份源文件哈希与主JSON实际逐一核对匹配。本审阅者读取并核对保存运行，不声称本次重新执行了主验证器；报告中的实际时刻保持不变。

## 独立API证据的来源与复放边界

另一位独立审查者/root/polynomial_next在/tmp/polynomial_product_api_math_review.md记录了实际执行：python /tmp/polynomial_product_recursive_review.py /workspace/IntegratedMath-book，退出码0。本审阅者已全文读取该报告及完整代码，核对其中结果与保存的实际输出JSON相同、五份源码及主报告哈希仍匹配，并验证嵌入代码与其实际执行脚本逐字节一致。以下收录该审查者的实际结果与完整可回放代码，使证据不依赖临时路径存续；这是明确归属的既有运行，**不是本审阅者新运行的计数**。本次未为复制代码而重复执行oracle。

参考算法独立使用稀疏字典与按右记录长度递归的P·(C(a)+S(T))，通过参考缩放、移位和相加生成积，未照抄生产双循环卷积，也未调用生产normalize/add/scale生成参考结果。Horner求值另作数值对照。43记录、1849配对与1728三元组覆盖尾零、左右移位、标量、求值、最高系数/次数、零积、非零消去及零因子反例。51类非法代表输入对应459次拒绝，覆盖两个操作、乘法两侧以及另一侧为短零/长零/非零的情形；零乘积次数拒绝328次。具体计数如下，不能扩展为Python所有对象已穷举或一般数学命题的证明。

## 来源条件与使用边界

已实际完整阅读正式polynomial_product_sources_2026-10-29.md，解析JSON，核对请求摘要、模型条件、稿件接口和实现诊断绑定。当前审计复用11条历史HTTP200字节记录，另登记2次新请求：Degree/Operations.lean成功、Eval/Basic.lean为HTTP404并保存14字节错误正文；eval_mul随后在已有Eval/Defs.lean缓存定位。总共13条选用请求，旧Degree/Defs.lean的404不重复计入。本审阅不重新联网，不把读取这些记录说成本人完成那些历史请求，也未独立认证全部远端原始字节。

OpenStax固定commit ad40c7e3c9a909cde81a24c526f52fe26a51fb14，CC-BY-NC-SA-4.0；mathlib v4.24.0，Apache-2.0。OpenStax形式表达式及分配教学提供动机，不能替代本书规范记录乘法的构造；FOIL只适用于二项式，不作为卷积通法。mathlib系数、乘法与有限反对角求和依赖已建半环和有限支持结构，不能把这些库实例直接借作本书先修；本书只新增一维倒序、单步移位和原记录长度归纳，不引入一般重排或一般多项式幂。

eval₂_mul_noncomm有系数像与输入交换的条件，交换目标版本和本书有理数情形满足相应交换性，但本书仍独立证明求值性质。次数乘法需要最高系数乘积非零；有理零乘积判据提供这一条件，不能泛化到含零因子的任意系数环。库degree使用WithBot N，natDegree在零处为0，都不替代本书零次数未定义的约定。外部源码阅读不等于Lean编译或书稿形式化；来源条件核对、主SymPy有限运行、另一审查者的递归oracle和本次数学文本复核分别记账。

来源JSON中带正式相对路径的稿件、依赖或报告哈希已递归核验，共14个不同文件匹配。此项是字节一致性检查，不另授予所有被引用旧稿或本人新稿的独立全文验收。

## 正式稿件与接口背景绑定

| 文件 | SHA-256 |
| --- | --- |
| `manuscript/foundations/polynomial_multiplication.md` | `048a6c96c9297cae0a4c2ee3e040a5265640515c31433dd06d615690af0f249d` |
| `manuscript/foundations/polynomial_multiplication_answers.md` | `4bab95e111a375b72a1b6b66675e447714f3158261790218209f508b46fc6cc1` |
| `manuscript/foundations/polynomial_product_structure.md` | `8dce7a9623ccac953c71113623156c6e0faca5abf82900fdfe3a6f6413e115b8` |
| `manuscript/foundations/polynomial_product_structure_answers.md` | `2342e21afec69515c80f6b8b5063ce0f404efbd8de1c991767fd6be4bbe1c1c2` |

## PM先修、五份代码、主报告与来源绑定

| 文件 | SHA-256 |
| --- | --- |
| `manuscript/foundations/finite_sums.md` | `ea736adc9c09e27a9443cd24a11af4c3a1f1fcad72824a8f7430b3a4b670ea23` |
| `manuscript/foundations/natural_numbers.md` | `709c9ebf1f580c8bf7af17b494ecd07505dd33f65ccfe49482675fe7712880f3` |
| `manuscript/foundations/natural_order.md` | `4ad8e874bedda7f4c15739fd47344903ec71bd9a5b538c71bde0f9827b091435` |
| `manuscript/foundations/natural_subtraction.md` | `92d1ac5e3cf6c07f61afd8f84e1e96d0556bf62d752e1d2a854121b66c412247` |
| `manuscript/foundations/polynomial_linear_operations.md` | `c7836f2dcb0684865109f3c44dc58eaea5ba434d9fd058f3e49b6686ad6a23f5` |
| `manuscript/foundations/polynomial_records.md` | `d243e9a7e7231f121182494b32a38f7799fd897beb4d3bd5f67431438846a8c5` |
| `manuscript/foundations/rational_powers.md` | `581010522535b41a771d0dd920531b37669b379ea64ce6001028620988bb3ee2` |
| `manuscript/foundations/rationals_addition.md` | `9b349aec9a9df0c7c45c9d33e7d0cfa483dc22432f0250baa23ab2a6d02b417b` |
| `manuscript/foundations/rationals_multiplication.md` | `033ed077c363d91143247bebedb790d4c444b5574c5085509a2b6c207d0b9c20` |
| `tools/rational_polynomial_product.py` | `a8fac5ff74d635c6b9b9fe3454ec9f1279f0cf6ca8cb3bcaf782496fd4d63246` |
| `tools/validate_rational_polynomial_product.py` | `a092019a0dbc7fe65783e6e8464ea1656bd162cedd04a7626714f82a2d1b11bd` |
| `tools/rational_polynomial_basic.py` | `4ab57898877c291e338241126e36ed79d4aeef8723c23e647f3591afbcf2243d` |
| `tools/rational_powers_sums.py` | `fad8cf2a22151b4d584ba09ea3464526668cf34d2737afdf0374f241f16cfda4` |
| `tools/linear_equation_solvers.py` | `c3ec0ab4a892397d3d0af59a1acd367bf1f1cfea80e3e14bd6b2b6cd790b74c9` |
| `research/production/rational_polynomial_product_validation.json` | `57141446d654b4c5f82b4ff713b594da40bc86e7498e705fe52e69abb19cb47f` |
| `research/production/polynomial_product_sources_2026-10-29.md` | `ada4257f2a713edf86ce91cd942aad03fde9f28e9d86f9ff1f09bcd072fdbe27` |
| `research/production/polynomial_product_sources_2026-10-29.json` | `2265e01989e281845c5df2a5c315dcc709907d1c454ed2f6961a5f60e002913b` |

独立API原报告SHA-256：`4760525f7d4bc6cff22bea8b1bc6818d3a90486fbe7649b19195d6e52d5bdb9f`；原执行脚本SHA-256：`5f01bc509ab9d3e9015daba870fe2a64d9e7c8e9057466d46f35ea6bf0b24365`。原报告作者与执行归属如上。

## 另一审查者的实际oracle输出

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

## 完整可回放oracle

将以下唯一python代码块保存为.py，以仓库绝对路径作为第一个命令参数执行。脚本只核对已存在的主JSON，不重写它。

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
