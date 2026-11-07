# B2.13 有限系数记录与多项式：独立数学复核

审阅者：独立数学复核代理。日期：2026-10-29。结论：绑定版本的B2.13正文与8题完整解答数学通过，无待解决数学阻断。同批B2.14正文及另8题全解也已重新完整阅读，用于核对后续接口。

## 构造、唯一性、求值与边界

原始数据为(n,a:I_n→Q)，n≥1；n−1只在正长度下使用。补零函数的i<n与n≤i两支互斥且完备，界外不读取未定义表项。PR1逐位置证明等价三性质；补k个尾零的三个索引范围包含k=0；L=max(n,m)只选两数较大者，i≥L两边皆零，有限判据充分必要。补齐所用L−n与L−m均先满足自然减法条件。

PR2把归纳变量写为k，处理k+1项记录：一项基例，末项非零取新末指标，末项零再分前缀全零或非零。前驱覆盖全部正项数，反对称性给最大指标唯一，不偷用任意非空集合的最大值。PR3全零留(0)，非零截至d；保系数按i≤d、d<i<n、i≥n分支。两等价规范记录先分零，再以较大末指标一侧非零、一侧补零排除不同长度，最后逐系数判等。两向等价判据及规范化幂等均无循环。

正式多项式为规范非空记录，0_pol是记录而非有理数0；常量包括零，次数和最高次系数只在非零对象定义。次数为最大非零指标，不是原始项数；首部、中间零保留。PR4形式相等只靠全部补零系数，未借根数定理。PR5先用SUM5证明尾补零求值不变，再用同一L上SUM1证明等价表示同值。t=0时幂仍合法，0^0=1保常数项。

PR6零输入先分索引零与正指标，用一项表接n−1个零；n=1时后段为空。输入一各项乘1，常量在所有输入取同一个q。标准求值函数固定Q→Q，有唯一输出；改变目标所得函数是另一对象。有限样本反例的数值与系数见证均正确；未把尚未证明的全Q反向识别错误地判为假。

## 八题完整答案

| 题 | 实际逐项核验 |
| --- | --- |
| 1 | 四规范结果(0)、(3)、(1,0,2)、(0,−1)；全零无最大非零指标，首/中零保留，各分支补零系数相同。 |
| 2 | 不同记录间仅A/B等价；其余五配对的指标见证全部正确；A/B长度不同，原记录不相等。 |
| 3 | 零常量无次数；(5)次数0、最高系数5；其余两非零结果次数2，最高系数3、−1；没有取deg0。 |
| 4 | 一般t下先证共同1−2t；三个样本−1、0、1/2得3、1、0；不由有限检查外推。 |
| 5 | 两记录在0/1处同为1/3，在2处为9/5；索引1的0/2直接判异，删中间零不是规范化。 |
| 6 | 全零/非零保系数分支、两向判据、规范唯一性的零与非零末索引比较均重述，不只引用PR3。 |
| 7 | d只是末索引，含零对象不称次数；一般零/一输入证明含d=0；R三值0、0、2，非零输出可否定零对象。 |
| 8 | (Q,Q,G)与(Q,{2},G)各自合法，同图异目标故函数不等；标准函数仍只有指定目标Q；零与R以索引1判异。 |

## 实际阅读、先修与非循环性

本次最终复核重新完整读取仓库中的两篇正文与16题全部解答，没有把恢复前的临时笔记或其他代理结论当作本次全文阅读。已有笔记仅用于交叉检查遗漏。四稿字节哈希均与已冻结的教学审阅表一致，本次未修改稿件。

实际复核的先修接口包括：B1.1从零起的归纳；自然数前驱、反对称与传递、后继比较、三歧性、加法保序反映和有条件自然减法；有序对、笛卡尔积、函数三项数据及FC1同域同目标逐点相等；有理加法、相反数与消去、乘法、分配律、符号规则和零乘积判据；B2.11幂定义与POW1；B2.12有限索引表、固定状态递归和SUM1—5。这里核读这些被使用的章节接口与证明段落，不声称重新全文审阅全部旧单元。

PR2先按k+1项归纳取得最后非零指标，PR3再构造规范代表；PR4判等建立之后PO1才按全体系数证明运算良定义。PR5先有表示无关求值，PO4随后用共同有限长度与SUM2推求值兼容。依赖顺序无循环：没有使用尚未定义的多项式乘法、X的多项式幂、一般重排、根数上界或插值证明这些结论。零次数始终未定义；正式相等推出标准Q→Q函数相等，反方向本批未证而未被宣称为假。

全体非空有限有理记录组成集合是本批公开采用的背景，不是声称由此前集合公理推导的定理。对象为唯一规范记录；不另构造商集合，也不把记录结构与求值函数结构等同。本批没有完成多项式环、一般模/向量空间、卷积、因式定理或97H20/第528章的全部内容。

## 实现与主验证报告

本次完整读取正式tools/rational_polynomial_basic.py及其主验证器，另读取幂/和依赖代码与rational输入检查。record只接受exact list/tuple且非空，所有系数必须为exact int/Fraction，拒bool、float、迭代器及回调。normalize先验证全表，再只删尾零，至少保留一项；内部零不删。coefficient先验证全表和exact int非负指标，界外返回精确零，查询界外不会掩盖表内坏项。same_polynomial核双输入后比较规范记录；degree对全零抛ValueError，非零常量返回0。

evaluate先验证记录与输入，再调用已建有理幂/有限和，零输入和零多项式不跳过参数检查，常数位使用0^0=1。add选两份非空原始记录实际长度的最大值，故长度至少1；scale即使标量零也验证所有系数；subtract先验证双输入，再加负一倍。运算输出规范Fraction元组，输入不修改，没有多项式乘法API。Fraction(1)作为指标被拒是程序类型约定，不是否定它在数学上对应自然数一。

主JSON的四份源码哈希已实际逐一与当前文件核对，全部一致。该已保存运行使用SymPy 1.14.0的QQ多项式独立字典构造，对照120记录、786系数、600求值、480补零、360缩放、1521配对、7605求值线性、1728结合律三元组、91非法或未定义输入拒绝及120输入不变性，并保存六个示例。91中含零次数拒绝，不统称类型错误。本次读取并校验此主运行记录，没有声称重新执行主SymPy验证器。

## 本次实际执行的独立oracle

本次逐行核读恢复下来的独立脚本后，实际运行其正式路径版本。脚本断言导入对象确为仓库tools/rational_polynomial_basic.py。规范化预期从稀疏非零系数字典的最大键重建，不照抄被测删尾零循环；加减在键并集上合成，形式相等比较非零系数字典。求值预期使用整数分子/分母的Horner递推，每一步表示旧值乘输入再加当前系数，最后构造Fraction；不调用被测power/finite_sum，也不用SymPy或有限采样推断形式相等。

实际通过780张1至4项记录、6050系数、5460独立求值、3900补零、3900缩放、780输入不变性；24025对1至3项记录的加减/相等/次数检查及72075求值线性；1728结合律三元组和1500条标量复合/标量和分配检查。274非法输入拒绝与10零次数拒绝分开。覆盖空记录、全零、内部零、常量、零标量、查询界外遇坏项、零输入遇非法参数及双输入左右位置。计数是脚本各类计数器的单位，不把一次计数内部的多次断言虚增为独立样本。

有限枚举支持实现和边界核查，不是一般命题的证明，也不是Lean形式化。本次没有复写脚本为新成果；完整保留已核读并重跑的代码以便复放。两份最终报告均嵌入相同代码与实际输出，各自提取后与原脚本逐字节核对并实际重放，输出一致；代码哈希见下。

## 来源与批准边界

本次读取正式来源Markdown，解析JSON并核对全部稿件/先修哈希条目，共13个不同文件匹配；检查访问摘要、来源条件、模型边界及实际稿接口。来源审计记录沿用14条历史公开访问（13条HTTP200、一条候选Degree/Defs.lean路径404及随后正确路径），本审阅未重新联网，也不把读取审计记录说成自己完成历史访问或独立认证所有远端下载字节。

OpenStax固定提交ad40c7e3c9a909cde81a24c526f52fe26a51fb14，CC-BY-NC-SA-4.0；mathlib v4.24.0，Apache-2.0。来源的有限支撑/半环模型不是本书非空规范记录模型；mathlib degree的底元素和natDegree的零值0均未搬入本书。OpenStax的笼统常数次数措辞不扩展到零，非零底数的零指数条款不用于证明本书0^0约定。常数多项式乘积只作来源边界对照，本书只构造有理数乘。来源预备诊断、主SymPy验证和本次独立oracle分别记账。

图注的索引、尾零与对象关系已核读；本报告不授予最终图片/PDF逐页视觉、构建、发布、合并或推送批准。该任务只写两份数学报告及临时复放文件，不修改四稿、实现或主验证报告。冻结内容若改变，须复核差异并重新绑定。

## 四稿最终哈希

| 文件 | 行数 | 字节数 | SHA-256 |
| --- | ---: | ---: | --- |
| `manuscript/foundations/polynomial_records.md` | 388 | 24209 | `d243e9a7e7231f121182494b32a38f7799fd897beb4d3bd5f67431438846a8c5` |
| `manuscript/foundations/polynomial_records_answers.md` | 328 | 12884 | `81a61101bd3382311ec4a460f6b9153279adc08c8f58e947589131c93a3783be` |
| `manuscript/foundations/polynomial_linear_operations.md` | 413 | 21391 | `c7836f2dcb0684865109f3c44dc58eaea5ba434d9fd058f3e49b6686ad6a23f5` |
| `manuscript/foundations/polynomial_linear_operations_answers.md` | 352 | 15141 | `e374e4b3051009476f113b4cf460cfddf7b335d20bf66668a08fb55799041427` |

## 先修、代码与来源审计绑定

| 文件 | SHA-256 |
| --- | --- |
| `manuscript/foundations/finite_sums.md` | `ea736adc9c09e27a9443cd24a11af4c3a1f1fcad72824a8f7430b3a4b670ea23` |
| `manuscript/foundations/functions_composition.md` | `806b32944f8253b2e2af3b2a551a25cc0ce6bf17ce51cc6b50216cf28e58a94a` |
| `manuscript/foundations/functions_definition.md` | `1dee6ffb8bada53f6f09ea4ad908c0a03fd06c937fb685538566175cb9655650` |
| `manuscript/foundations/natural_numbers.md` | `709c9ebf1f580c8bf7af17b494ecd07505dd33f65ccfe49482675fe7712880f3` |
| `manuscript/foundations/natural_order.md` | `4ad8e874bedda7f4c15739fd47344903ec71bd9a5b538c71bde0f9827b091435` |
| `manuscript/foundations/natural_subtraction.md` | `92d1ac5e3cf6c07f61afd8f84e1e96d0556bf62d752e1d2a854121b66c412247` |
| `manuscript/foundations/rational_powers.md` | `581010522535b41a771d0dd920531b37669b379ea64ce6001028620988bb3ee2` |
| `manuscript/foundations/rationals_addition.md` | `9b349aec9a9df0c7c45c9d33e7d0cfa483dc22432f0250baa23ab2a6d02b417b` |
| `manuscript/foundations/rationals_multiplication.md` | `033ed077c363d91143247bebedb790d4c444b5574c5085509a2b6c207d0b9c20` |
| `tools/rational_polynomial_basic.py` | `4ab57898877c291e338241126e36ed79d4aeef8723c23e647f3591afbcf2243d` |
| `tools/validate_rational_polynomial_basic.py` | `e075b836b99427256cf3ba76d0952072159f0a561c4dd8eb3f0b9577af4f0591` |
| `tools/rational_powers_sums.py` | `fad8cf2a22151b4d584ba09ea3464526668cf34d2737afdf0374f241f16cfda4` |
| `tools/linear_equation_solvers.py` | `c3ec0ab4a892397d3d0af59a1acd367bf1f1cfea80e3e14bd6b2b6cd790b74c9` |
| `research/production/rational_polynomial_basic_validation.json` | `82210e28f3531c75885be77b50305c88001e0f632a82715a31b032d07fd2a17c` |
| `research/production/polynomial_basic_sources_2026-10-29.md` | `d88d750cf16709f730c3e562ddc3ae3e543a968935c4cf3afca405ca7d827b71` |
| `research/production/polynomial_basic_sources_2026-10-29.json` | `c2c2a70a0e638ddd82e167468cef7e8fb78408d9a70b8cd68655f65bf4f722f0` |

## 可重放完整oracle及实际输出

脚本SHA-256：`32a57ea2e092213484cfe858c04d2bdc37bcc3e096cfd3d92577e38ec8f353b6`。从本报告提取唯一的python代码块并保存为临时.py，以Python 3执行；ROOT固定为本次实际仓库路径。无需安装SymPy。

```python
"""Independent bounded sparse-coefficient and integer-Horner checks."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import sys,json,hashlib
ROOT=Path('/workspace/IntegratedMath-book')
sys.path.insert(0,str(ROOT/'tools'))
import rational_polynomial_basic as api
assert Path(api.__file__).resolve()==ROOT/'tools/rational_polynomial_basic.py'
counts=dict(records=0,coefficients=0,evaluations=0,padding=0,scalings=0,
            pairs=0,evaluation_linearity=0,triples=0,scalar_laws=0,
            rejected=0,zero_degree_rejected=0,input_immutability=0)

def sparse(values):
    return {i:F(v) for i,v in enumerate(values) if v!=0}

def canonical(mapping):
    support={i:v for i,v in mapping.items() if v!=0}
    if not support:
        return (F(0),)
    return tuple(support.get(i,F(0)) for i in range(max(support)+1))

def combine(left,right,sign):
    a,b=sparse(left),sparse(right)
    return canonical({i:a.get(i,F(0))+sign*b.get(i,F(0)) for i in a.keys()|b.keys()})

def horner_integer(values,at):
    """Unreduced integer numerator/denominator Horner; no api power or sum."""
    t=F(at)
    numerator,denominator=0,1
    for value in reversed(values):
        a=F(value)
        numerator=numerator*t.numerator*a.denominator+a.numerator*denominator*t.denominator
        denominator=denominator*t.denominator*a.denominator
    return F(numerator,denominator)

def reject(function,*args,zero_degree=False):
    try:
        function(*args)
    except (TypeError,ValueError):
        counts['zero_degree_rejected' if zero_degree else 'rejected']+=1
    else:
        raise AssertionError(('unexpected acceptance',function.__name__,args))

VALUES=(F(-2),F(-1,2),F(0),F(1,3),F(2))
POINTS=(F(-3),F(-1),F(-1,2),F(0),F(1,2),F(1),F(3))
def records(limit,values=VALUES):
    return [r for size in range(1,limit+1) for r in product(values,repeat=size)]
for record in records(4):
    mapping=sparse(record)
    expected=canonical(mapping)
    actual=api.normalize(record)
    assert type(actual) is tuple and all(type(v) is F for v in actual)
    assert actual==expected and api.normalize(actual)==actual
    assert api.record(list(record))==record
    if mapping:
        assert api.degree(record)==max(mapping)
    else:
        reject(api.degree,record,zero_degree=True)
    counts['records']+=1
    for index in range(len(record)+4):
        value=api.coefficient(record,index)
        assert type(value) is F and value==mapping.get(index,F(0))
        counts['coefficients']+=1
    for point in POINTS:
        value=api.evaluate(record,point)
        assert type(value) is F and value==horner_integer(record,point)
        counts['evaluations']+=1
    for extra in range(5):
        padded=record+(F(0),)*extra
        assert api.normalize(padded)==expected
        assert api.same_polynomial(record,padded) is True
        assert api.evaluate(padded,F(0))==record[0]
        counts['padding']+=1
    for scalar in VALUES:
        result=api.scale(scalar,record)
        assert result==canonical({i:scalar*v for i,v in mapping.items()})
        if scalar and mapping:
            assert api.degree(result)==max(mapping)
        else:
            assert result==(F(0),)
        for point in POINTS:
            assert api.evaluate(result,point)==scalar*horner_integer(record,point)
        counts['scalings']+=1
    mutable=list(record);before=mutable.copy()
    api.record(mutable);api.normalize(mutable);api.coefficient(mutable,99)
    api.evaluate(mutable,F(1,3));api.scale(-1,mutable)
    api.add(mutable,[1,0]);api.subtract([1,0],mutable)
    api.same_polynomial(mutable,record)
    assert mutable==before
    counts['input_immutability']+=1
for left,right in product(records(3),repeat=2):
    result=api.add(left,right)
    assert result==combine(left,right,1)
    assert api.subtract(left,right)==combine(left,right,-1)
    assert api.same_polynomial(left,right)==(sparse(left)==sparse(right))
    assert result==api.add(right,left)
    a,b,c=sparse(left),sparse(right),sparse(result)
    if a and b and c:
        assert api.degree(result)<=max(max(a),max(b))
        if max(a)!=max(b):
            assert api.degree(result)==max(max(a),max(b))
    for point in (F(-1,2),F(0),F(2)):
        assert api.evaluate(result,point)==horner_integer(left,point)+horner_integer(right,point)
        counts['evaluation_linearity']+=1
    counts['pairs']+=1
small=records(2,(F(-1),F(0),F(1)))
for a,b,c in product(small,repeat=3):
    assert api.add(api.add(a,b),c)==api.add(a,api.add(b,c))
    counts['triples']+=1
for a in records(2):
    assert api.add(a,api.scale(-1,a))==(F(0),)
    for s,t in product(VALUES,repeat=2):
        assert api.scale(s,api.scale(t,a))==api.scale(s*t,a)
        assert api.scale(s+t,a)==api.add(api.scale(s,a),api.scale(t,a))
        counts['scalar_laws']+=2
bad_records=[[],(),None,True,1,F(1),'0',b'0',{0:1},{1},frozenset({1}),range(2),iter([1]),lambda i:1,
             [True],[False],[1.0],[None],['1'],[(1,2)],[F(0),F(1),False]]
for bad in bad_records:
    for function in (api.record,api.normalize,api.degree):
        reject(function,bad)
    reject(api.coefficient,bad,99)
    reject(api.evaluate,bad,0)
    reject(api.scale,0,bad)
    for function in (api.add,api.subtract,api.same_polynomial):
        reject(function,bad,(0,))
        reject(function,(0,),bad)
for bad in (True,False,-1,-99,1.0,F(1),None,'1'):
    reject(api.coefficient,(1,),bad)
for bad in (True,False,0.0,None,'0',(1,2),complex(0,0)):
    reject(api.evaluate,(0,),bad)
    reject(api.scale,bad,(0,))
for length in range(1,7):
    reject(api.degree,[0]*length,zero_degree=True)
assert api.normalize([0,0,0])==(F(0),)
assert api.normalize([1,0,2,0])==(F(1),F(0),F(2))
assert api.same_polynomial([1,0,2],[1,2]) is False
assert api.evaluate([1,0,2],0)==api.evaluate([1,2],0)==1
assert api.evaluate([1,0,2],1)==api.evaluate([1,2],1)==3
assert api.evaluate([1,0,2],2)==9 and api.evaluate([1,2],2)==5
print(json.dumps(counts,sort_keys=True,indent=2))
```

实际标准输出：

```json
{
  "coefficients": 6050,
  "evaluation_linearity": 72075,
  "evaluations": 5460,
  "input_immutability": 780,
  "padding": 3900,
  "pairs": 24025,
  "records": 780,
  "rejected": 274,
  "scalar_laws": 1500,
  "scalings": 3900,
  "triples": 1728,
  "zero_degree_rejected": 10
}
```
