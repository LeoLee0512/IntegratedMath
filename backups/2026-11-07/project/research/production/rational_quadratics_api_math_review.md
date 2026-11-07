# 有理平方与二次方程API：独立数学及算法审阅

结论：对下列精确哈希快照，三函数的数学行为、二分算法说明和输入契约通过审阅；未发现阻断问题。审阅对象由根编写，本报告由来源代理独立检查。没有修改被审代码、算法说明或第19批正式文件。

本结论限API及其算法证明，不授予SQ/QC全文、教学、构建、视觉或第20批整体验收。本报告实际执行了文末独立oracle；根的主validator及preliminary报告已通读，本次没有把阅读它们写成重新执行主validator。

审阅UTC：2026-10-29T19:25:17.331219+00:00

## 实际文件与哈希

| 实际审读文件 | SHA-256 |
|---|---|
| `/tmp/rational_quadratics.py` | `b2311b7df377f4e2ae1cd3742bd752e69cebc3068cef25182e772a386a195663` |
| `/tmp/rational_quadratics_algorithm_notes.md` | `312a617204340b8acf58d1723737cd0e74fe56ab885f5a60ee0308c22ba02e6b` |
| `/tmp/validate_rational_quadratics.py` | `1a0e9afd0b501ae342d07358b5f88c55f8ac45afd03df55bb4c6758c32ec76f7` |
| `/tmp/rational-quadratics-preliminary-validation.json` | `b510f15ab7ccf86bf5adc99619fdff53ba5a25a656531d5fcef547c4a0e38531` |
| `/workspace/IntegratedMath-book/tools/linear_equation_solvers.py` | `c3ec0ab4a892397d3d0af59a1acd367bf1f1cfea80e3e14bd6b2b6cd790b74c9` |
| `/tmp/rational_square_equations.md` | `8a1edd98b84ee307666dfe8e7c416bea4530e9332b7eed1e1c813c471a7a2598` |
| `/tmp/rational_square_equations_answers.md` | `2b623ea4477353874f910d0867ca3fc9af8f6e92ed5f74e037450c756ae346c2` |

另核SQ4正文规范平方记录的必要、充分方向及C4两次/R5依赖，作为API数学接口；对SQ全篇的独立教学或全文数学验收不在本报告范围。QC分类公式在本报告中通过恒等式独立核算，不以尚未读审的QC整稿代替本次证明。

## integer_sqrt：一般证明与实际代码相符

代码入口明确：

```python
if type(value) is not int or value < 0:
    raise ValueError('expected a nonnegative integer')
low, high = 0, value + 1
while high - low > 1:
    middle = (low + high) // 2
```

只接收精确内置非负int；bool、int子类、Fraction及浮点均不进入算法。Python任意精度整数的精确加乘比较，以及非负整数`// 2`是带余除法的商，是代码到数学模型的运行时假设，不是新增数论公理。

初值：n≥0，low=0、high=n+1，故0≤low<high；0²≤n，且(n+1)²≥n+1>n。n=0时初始区间差恰为1，while不执行，返回0，目标0²≤0<1²成立。

循环守卫把区间差限制为至少2。记L+H=2M+r，r∈{0,1}。若M≤L，则L+H≤2L+1，与H≥L+2冲突；若M≥H，则L+H≥2H，与L<H冲突。因此L<M<H。算法说明的中点证明没有假定连续区间或实数平均值能作为整数。

若M²≤n，更新L=M，另一端H保持n<H²；否则整数全序给n<M²，更新H=M，另一端L保持L²≤n。两支均保0≤L<H和L²≤n<H²。

更新后的正整数差分别为H−M或M−L，均严格小于旧H−L。严格减少至少1；若执行j次，当前差≤n+1−j（只在允许差的范围书写），故不能执行n+1次更新，至多n次。该界虽然宽松但足以证明终止，n=0也包括在内，不需依赖实际运行耗时。

退出时正差≤1，必为1，返回L满足L²≤n<(L+1)²。若另一非负整数u也满足同界，u>L会给u≥L+1，进而u²≥(L+1)²>n矛盾；u<L对调同理。此处整数平方保序来自既有非负乘法次序，不能反过来依赖待检算法。

实际追踪的是未修改的原函数：在while头核不变式与差下降，在分支判断前核中点严格内部，在return前核差为1；不是另写一份相同二分算法来彼此对照。有限追踪仍不代替上述全称论证。

## rational_square_root：规范表示与定义域

实现关键段：

```python
value = rational(value)
if value < 0:
    return None
p, q = value.numerator, value.denominator
m, n = integer_sqrt(p), integer_sqrt(q)
if m * m != p or n * n != q:
    return None
return Fraction(m, n)
```

现有`linear_equation_solvers.rational`精确使用`type(value) not in (int, Fraction)`拒绝其余类型，再调用Fraction(value)。必须将Python标准库Fraction提供正分母、互素规范表示及精确有理算术列为实现依赖；本审阅不声称重新证明了Python标准库实现。该外部依赖与正文R5数学证明分别记账。

合法负数返回None，因为有理平方非负。非负值的规范分子p≥0、分母q≥1；两个整数算法调用均满足前提。分母候选n不可能为0，因为整数算法给q<(n+1)²，若n=0即q<1，与q≥1冲突。因此返回Fraction(m,n)从不构造零分母。

两平方检验都成功，则返回值非负且平方为p/q；任一失败，根据整数平方界唯一性该分子或分母没有相应非负整数平方根，SQ4排除有理平方根。SQ4的必要方向依赖：规范根(p,q)平方后为(p²,q²)，C4两次和gcd对称使其仍互素，正分母保证合法，R5唯一性允许逐分量相等。充分方向只需任意合法(u,v)代表，不额外要求u,v先互素。没有使用素数或唯一分解。

0规范为0/1，返回精确Fraction(0,1)。未约分形式由Fraction先规范化，如8/18与4/9同返回2/3；原表示分子分母不是平方不能直接作为否定证据。此API是总定义的检测器：对合法Q返回非负根或None；它与正文只在S_Q上定义的部分函数sqrt_Q不同，None不被解释成某个平方根值。非法输入抛ValueError，和合法但无根的None分开。

## solve_quadratic：全参数及类型

代码首先执行：

```python
a, b, c = (rational(v) for v in (a, b, c))
```

赋值完成须消费三个输入后才进入任何退化分支；因此即使a=b=0，非法c也会拒绝，不会被`all`或`none`早返回掩盖。遇到第一个非法输入立即抛异常是正常的校验失败，不要求继续校验其余输入。

a=0时：b≠0返回唯一精确根−c/b；b=c=0返回`{'kind':'all'}`；b=0,c≠0返回`{'kind':'none'}`。这些分支不会形成1/(2a)。

a≠0时，Δ=b²−4ac。直接展开得到

(2at+b)²−Δ = 4a(at²+bt+c)。

因为Q中4a≠0，原式为零当且仅当(2at+b)²=Δ。若没有同域平方根s，必要方向排除全部有理解；不能把这种输出改称已证明存在实根或复根。

若s≥0且s²=Δ，同平方的正负分支给2at+b=s或−s；2a≠0保证可逆，两个候选恰为(−b±s)/(2a)，同时证明必要性和充分性。s=0时两式相同，集合去重为一项；s>0时2s≠0，两式不同。a<0只影响顺序，`sorted`按Fraction的精确有理序排序，不改变解集。集合元素均可哈希的Fraction；输出元组非空，包含一项或两项，且无重复。

精确契约：输入只接受type恰为int或Fraction；finite分支的roots恰为tuple且每项type恰为Fraction。None、字符串、浮点（含inf/nan）、bool、复数、容器、Decimal、自定义可转换对象、int/Fraction子类均拒绝。all/none只含kind，finite另含roots；全部Q与空集不会共用空tuple。输入Fraction不可变，函数不改输入状态。

## 主验证与本次独立验证的区分

已读主报告：整数界4102、有理平方3059、参数三元组729，主oracle是math.isqrt与SymPy 1.14.0 QQ ground_roots，记录35次拒绝。这些数字属于根的已有运行，本次不重复归为独立运行。

本次oracle没有调用math.isqrt、SymPy、ground_roots或判别式公式生成期望根：

- 整数界直接列整数平方表，遍历0…16384；另用已知大整数平方的−1/0/+1边界。
- 有理平方先枚举非负有理见证再平方建映射；输入规范|分子|≤63、分母≤23，SQ4保证若存在规范非负根，其分子、分母落在枚举界内。因而这些有限范围的None期望并非仅“没有搜到”猜测。
- 选择31个有理根候选r,t和6个非零正负标量a，构造a(x−r)(x−t)，直接以{r,t}作完整期望解集；完备性来自Q零积性质，不是复用被审公式。
- 退化式遍历所有b,c；无根例构造a((x−h)²−q)，q取负数、2或1/2。后两者的无Q根是SQ4和整数平方间隙已证事实，不由有限枚举推出。
- 类型拒绝另涵盖三个参数位置及会早返回的退化场景，并以会抛断言的转换方法确保非法自定义对象没有被偷偷转换。

完整代码和实际输出在下方。它们覆盖具体有限样本，仍不能替代一般程序形式化验证、SQ/QC全文审查或构建验收；本报告没有运行网络工具，也没有新增外部来源请求。

## 可复现命令与独立文件

```bash
python /tmp/rational_quadratics_independent_oracle.py > /tmp/rational_quadratics_independent_oracle_output.json
```

独立代码SHA-256：`2963f5f5f274f52a59a08773d3c70ac03cf8003e86f7e53a8422535a14bb4ec7`。实际输出SHA-256：`6c358acdd1e2d52f4d8af6207d61f6f50d395941ed4e1cb6729c668dfe31207e`。

## 完整独立代码

```python
"""Independent finite review: enumerated squares and factor-generated polynomials.
No math.isqrt, SymPy ground_roots, discriminant-based expected-root routine,
or copy of the production binary-search algorithm is used as the oracle.
"""
from fractions import Fraction as F
from decimal import Decimal
from itertools import product
from pathlib import Path
from hashlib import sha256
import ast, inspect, json, sys
sys.path[:0] = ['/tmp', '/workspace/IntegratedMath-book/tools']
import rational_quadratics as api

inputs = [Path('/tmp/rational_quadratics.py'), Path('/tmp/rational_quadratics_algorithm_notes.md'),
          Path('/tmp/validate_rational_quadratics.py'), Path('/tmp/rational-quadratics-preliminary-validation.json'),
          Path('/workspace/IntegratedMath-book/tools/linear_equation_solvers.py'),
          Path('/tmp/rational_square_equations.md'), Path('/tmp/rational_square_equations_answers.md')]
manifest = {str(p): sha256(p.read_bytes()).hexdigest() for p in inputs}
counts = dict(integer_bruteforce=0, integer_large_boundary=0, traced_integer_calls=0,
              trace_loop_head_checks=0, trace_midpoint_checks=0, trace_strict_decreases=0,
              rational_square_inputs=0, rational_square_found=0, rational_square_absent=0,
              normalized_presentations=0, factor_generated=0, factor_repeated=0,
              factor_two_distinct=0, degenerate_all=0, degenerate_none=0,
              degenerate_linear=0, constructed_noroot=0, illegal_integer=0,
              illegal_square=0, illegal_quadratic=0)
# Brute table is a different oracle: each integer square is listed explicitly.
square_table = [(j, j*j) for j in range(130)]
for n in range(16385):
    expected = max(j for j, square in square_table if square <= n)
    actual = api.integer_sqrt(n)
    assert type(actual) is int and actual == expected, (n, actual, expected)
    counts['integer_bruteforce'] += 1
for k in [2, 17, 10**20 + 3, 10**100 + 31, 2**511 + 7]:
    for offset, expected in [(-1, k-1), (0, k), (1, k)]:
        assert api.integer_sqrt(k*k + offset) == expected
        counts['integer_large_boundary'] += 1

# Observe the actual function, without altering its implementation.
tree = ast.parse(Path(api.__file__).read_text())
function = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'integer_sqrt')
while_node = next(n for n in ast.walk(function) if isinstance(n, ast.While))
if_node = next(n for n in while_node.body if isinstance(n, ast.If))
return_node = next(n for n in function.body if isinstance(n, ast.Return))
trace_history = {}
def trace(frame, event, arg):
    if frame.f_code is not api.integer_sqrt.__code__:
        return trace
    if event == 'line' and frame.f_lineno in (while_node.lineno, if_node.lineno, return_node.lineno):
        v = frame.f_locals
        low, high, n = v['low'], v['high'], v['value']
        assert 0 <= low < high and low*low <= n < high*high
        if frame.f_lineno == while_node.lineno:
            gap = high-low
            counts['trace_loop_head_checks'] += 1
            if 'last_gap' in trace_history:
                assert gap < trace_history['last_gap']
                counts['trace_strict_decreases'] += 1
            trace_history['last_gap'] = gap
        elif frame.f_lineno == if_node.lineno:
            assert low < v['middle'] < high
            counts['trace_midpoint_checks'] += 1
        else:
            assert high-low == 1
    return trace
for n in list(range(257)) + [(10**50+9)**2+k for k in (-1,0,1)] + [2**256-1, 2**256, 2**256+1]:
    trace_history.clear()
    sys.settrace(trace)
    try:
        api.integer_sqrt(n)
    finally:
        sys.settrace(None)
    counts['traced_integer_calls'] += 1

# Enumerate rational witnesses once, square them, and look inputs up in the map.
# Completeness for these bounds follows from SQ4: a normalized root of p/q
# must have numerator <= 63 and denominator <= 23 for |p| <= 63, q <= 23.
square_witnesses = {F(u, v)**2: F(u, v) for u in range(64) for v in range(1,24)}
values = sorted({F(p,q) for p in range(-63,64) for q in range(1,24)})
for value in values:
    actual = api.rational_square_root(value)
    expected = square_witnesses.get(value)
    assert actual == expected, (value, actual, expected)
    counts['rational_square_inputs'] += 1
    if expected is None:
        assert actual is None
        counts['rational_square_absent'] += 1
    else:
        assert type(actual) is F and actual >= 0 and actual*actual == value
        counts['rational_square_found'] += 1
for a,b in [(8,18),(0,7),(100,225),(-8,-18),(4,9),(2,4),(-4,9)]:
    expected = square_witnesses.get(F(a,b))
    for scale in [1,2,7,-3]:
        assert api.rational_square_root(F(a*scale,b*scale)) == expected
        counts['normalized_presentations'] += 1

# Expected roots come from chosen factors, not from the quadratic formula.
roots = sorted({F(p,q) for p in range(-5,6) for q in range(1,5)})
scales = [F(-5),F(-3,7),F(-1,2),F(1,5),F(2),F(7,3)]
for a,r,t in product(scales, roots, roots):
    b,c = -a*(r+t), a*r*t
    expected_roots = tuple(sorted({r,t}))
    actual = api.solve_quadratic(a,b,c)
    assert actual == {'kind':'finite','roots':expected_roots}, (a,r,t,actual)
    assert type(actual['roots']) is tuple and all(type(v) is F for v in actual['roots'])
    assert all(a*v*v+b*v+c == 0 for v in actual['roots'])
    counts['factor_generated'] += 1
    counts['factor_repeated' if r == t else 'factor_two_distinct'] += 1

# Every degenerate branch, including c validation before a=b=0 early return.
for b,c in product(roots,repeat=2):
    actual = api.solve_quadratic(0,b,c)
    if b == 0:
        kind = 'all' if c == 0 else 'none'
        assert actual == {'kind':kind}
        counts['degenerate_'+kind] += 1
    else:
        assert actual == {'kind':'finite','roots':(-c/b,)}
        assert type(actual['roots'][0]) is F
        counts['degenerate_linear'] += 1
# Negative rational values cannot be squares; 2 and 1/2 are nonsquares by
# the separately audited SQ4 + integer 0/1/>=2 gap proof, not finite guessing.
for a,h,q in product(scales, roots, [F(-1),F(-3,2),F(2),F(1,2)]):
    # a*((x-h)^2-q) has no Q root, irrespective of the sign of a.
    assert api.solve_quadratic(a,-2*a*h,a*(h*h-q)) == {'kind':'none'}
    counts['constructed_noroot'] += 1

class IntSubclass(int): pass
class FractionSubclass(F): pass
class Coercible:
    def __int__(self): raise AssertionError('unexpected coercion')
    def __index__(self): raise AssertionError('unexpected coercion')
bad = [True,False,1.0,float('inf'),float('nan'),None,'1',complex(1),[1],(1,),{},
       Decimal('1'),IntSubclass(1),FractionSubclass(1),Coercible()]
def rejected(f,*args):
    try: f(*args)
    except ValueError: return
    raise AssertionError(('illegal input accepted',f.__name__,tuple(type(x).__name__ for x in args)))
for value in bad + [F(0),F(1),-1,-10**100]:
    rejected(api.integer_sqrt,value);counts['illegal_integer'] += 1
for value in bad:
    rejected(api.rational_square_root,value);counts['illegal_square'] += 1
    for position in range(3):
        for base in [(0,0,0),(0,0,1),(0,1,0),(1,0,0),(-1,0,-1)]:
            args=list(base);args[position]=value
            rejected(api.solve_quadratic,*args);counts['illegal_quadratic'] += 1
# Exact built-in integer inputs and Fraction inputs are both accepted.
assert api.rational_square_root(4) == F(2) and type(api.rational_square_root(4)) is F
assert api.solve_quadratic(1,-3,2) == {'kind':'finite','roots':(F(1),F(2))}
assert all(sha256(Path(p).read_bytes()).hexdigest() == h for p,h in manifest.items())
report=dict(status='passed',oracle='enumerated integer squares; enumerated rational square witnesses; factor-generated exact rational roots; exhaustive bounded degeneracies; traced actual loop invariants',counts=counts,input_sha256=manifest,finite_bounds=dict(integer_range=[0,16384],rational_numerator_range=[-63,63],rational_denominator_range=[1,23],factor_root_values=len(roots),factor_scales=[str(x) for x in scales]),large_boundary_bits_max=(2**511+7).bit_length()*2,limits='Finite checks plus separate human mathematical audit; no universal program verification, no SymPy or math.isqrt oracle used here, no manuscript/pedagogy/build acceptance granted.')
print(json.dumps(report,ensure_ascii=False,indent=2))
```

## 完整实际输出

```json
{
  "status": "passed",
  "oracle": "enumerated integer squares; enumerated rational square witnesses; factor-generated exact rational roots; exhaustive bounded degeneracies; traced actual loop invariants",
  "counts": {
    "integer_bruteforce": 16385,
    "integer_large_boundary": 15,
    "traced_integer_calls": 263,
    "trace_loop_head_checks": 3741,
    "trace_midpoint_checks": 3478,
    "trace_strict_decreases": 3478,
    "rational_square_inputs": 1839,
    "rational_square_found": 21,
    "rational_square_absent": 1818,
    "normalized_presentations": 28,
    "factor_generated": 5766,
    "factor_repeated": 186,
    "factor_two_distinct": 5580,
    "degenerate_all": 1,
    "degenerate_none": 30,
    "degenerate_linear": 930,
    "constructed_noroot": 744,
    "illegal_integer": 19,
    "illegal_square": 15,
    "illegal_quadratic": 225
  },
  "input_sha256": {
    "/tmp/rational_quadratics.py": "b2311b7df377f4e2ae1cd3742bd752e69cebc3068cef25182e772a386a195663",
    "/tmp/rational_quadratics_algorithm_notes.md": "312a617204340b8acf58d1723737cd0e74fe56ab885f5a60ee0308c22ba02e6b",
    "/tmp/validate_rational_quadratics.py": "1a0e9afd0b501ae342d07358b5f88c55f8ac45afd03df55bb4c6758c32ec76f7",
    "/tmp/rational-quadratics-preliminary-validation.json": "b510f15ab7ccf86bf5adc99619fdff53ba5a25a656531d5fcef547c4a0e38531",
    "/workspace/IntegratedMath-book/tools/linear_equation_solvers.py": "c3ec0ab4a892397d3d0af59a1acd367bf1f1cfea80e3e14bd6b2b6cd790b74c9",
    "/tmp/rational_square_equations.md": "8a1edd98b84ee307666dfe8e7c416bea4530e9332b7eed1e1c813c471a7a2598",
    "/tmp/rational_square_equations_answers.md": "2b623ea4477353874f910d0867ca3fc9af8f6e92ed5f74e037450c756ae346c2"
  },
  "finite_bounds": {
    "integer_range": [
      0,
      16384
    ],
    "rational_numerator_range": [
      -63,
      63
    ],
    "rational_denominator_range": [
      1,
      23
    ],
    "factor_root_values": 31,
    "factor_scales": [
      "-5",
      "-3/7",
      "-1/2",
      "1/5",
      "2",
      "7/3"
    ]
  },
  "large_boundary_bits_max": 1024,
  "limits": "Finite checks plus separate human mathematical audit; no universal program verification, no SymPy or math.isqrt oracle used here, no manuscript/pedagogy/build acceptance granted."
}
```
## 正式迁移附记（第 20 批）

本附记只核对正式迁移后的字节、验证器差异与已执行报告的绑定。上文独立算法审查、完整 oracle 程序和当时的实际输出逐字保留；临时原报告也未修改。API 与算法说明分别和原独立审查所读 `/tmp/rational_quadratics.py`、`/tmp/rational_quadratics_algorithm_notes.md` 字节完全相同，所以原二分循环不变式、`n=0`、规范分数平方判据、全部二次及退化分支和非法输入的审查仍针对同一实现。

正式算法说明 `research/production/rational_quadratics_algorithm_notes.md` 的 SHA-256 为 `312a617204340b8acf58d1723737cd0e74fe56ab885f5a60ee0308c22ba02e6b`。原临时验证器 SHA-256 为 `1a0e9afd0b501ae342d07358b5f88c55f8ac45afd03df55bb4c6758c32ec76f7`。已逐行读取完整 diff：正式验证器删除临时 `sys.path` 注入，改由自身路径取得仓库根目录；导入 `hashlib` 与 UTC 时间工具；从符号 `x` 的初始化到所有原非法输入循环结束的旧检查核心字节完全相同，另经 AST 相等核对。尾部原 preliminary 打印替换为 8 个具名例子的实际断言及正式 JSON 输出，增加 schema、UTC 执行时间、三个文件的 SHA-256、有限测试范围和限制说明。没有改动原有测试范围、判据或核心循环。

8 个新增例子分别检查：平方根 0、约分后的 4/9、非平方 2；退化线性方程根 3；两个根 −1/3 和 1；重根 3/2；恒等方程所有有理数；负首项系数方程的两个根 1 和 2。已将正式报告的全部 8 个输入和输出逐项与验证器所写期望值核对；其中输入 `Fraction(8,18)` 在报告中规范化为 `4/9`。

主线程已执行的正式报告 `research/production/rational_quadratics_validation.json` 声明 `passed`；报告中三个依赖的 SHA-256 均与当前正式文件一致，且只有下列三个依赖。主报告记录整数 4102 例、分数 3059 例、二次/退化参数 729 组、拒绝 35 例，另有上述 8 个例子。该执行归属于主线程；本审查人在迁移核对中未重新运行正式验证器或原独立 oracle，未把读取报告写成新的运行记录。新的本地断言仅核对字节、AST、报告依赖和数据内容，结果如下。

```json
{
  "checked_at": "2026-10-29T19:39:53.870935+00:00",
  "status": "passed",
  "original_review_sha256": "16a455ea4576bf8bc2a027deab0f80f264ccc3aa030da606aa36effc0293c69c",
  "api_and_algorithm_notes_byteexact": true,
  "validator_existing_test_core_byteexact": true,
  "validator_existing_test_core_ast_equal": true,
  "formal_report_sha256": "aaa4f949753cfb7d5130d487a48fb54256ff9e12aee4243baddc6a0ab433184e",
  "formal_report_validated_at": "2026-10-29T19:28:55.453262+00:00",
  "formal_report_dependency_count": 3,
  "formal_report_source_sha256": {
    "tools/rational_quadratics.py": "b2311b7df377f4e2ae1cd3742bd752e69cebc3068cef25182e772a386a195663",
    "tools/validate_rational_quadratics.py": "448465721944a2dde4556b1af57cd9711fe42e54c3bb63fcb4f024a5d37fb752",
    "tools/linear_equation_solvers.py": "c3ec0ab4a892397d3d0af59a1acd367bf1f1cfea80e3e14bd6b2b6cd790b74c9"
  },
  "formal_report_counts": {
    "integer_bounds": 4102,
    "rational_squares": 3059,
    "quadratics": 729,
    "all": 1,
    "none": 522,
    "finite_one": 96,
    "finite_two": 110,
    "rejections": 35
  },
  "formal_report_eight_examples_match_reviewed_expected_values": true,
  "formal_validator_reexecuted_by_this_reviewer": false,
  "independent_oracle_reexecuted_for_migration": false
}
```

这次迁移没有改变上文依赖边界：Python 精确整数与标准库 `Fraction` 的规范化行为为程序背景；书中 SQ4 的规范分数平方判据及已证有理运算为数学接口；主验证器的 `math.isqrt` 和 SymPy 是有限实现核查的 oracle，不作为正文证明前提。本附记不授予来源、全稿、图像、构建或最终批次验收。
