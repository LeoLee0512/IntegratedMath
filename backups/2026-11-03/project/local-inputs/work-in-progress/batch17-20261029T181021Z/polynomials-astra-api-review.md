# 多项式规范记录与线性运算：临时API独立检查

Astra/high，2026-10-29。只针对本报告绑定的/tmp程序。已实际全文读取实现及主验证器，另写并实际执行不同oracle；未发现实现或API边界错误。本结论不是B2.13/14正文或答案验收，未修改当前冻结稿、构建或台账。

## API与完整输入校验

record只接受exact list/tuple且必须非空；每个系数均先经既有rational检查，返回Fraction元组。空系数表被拒，尽管有限和模块本身允许空表。bool、float和其他数值容器类型被拒；具体非法容器使用TypeError，空表/非法有理值等使用ValueError，本检查接受两类所声明错误。

normalize先验证完整原始记录，随后只删末尾零且最短保留一项，全零结果恒为(Fraction(0),)。内部零保留。coefficient先验证整张表及exact int非负指标，再决定读表内还是补零；即使指标在表外也不跳过非法原项。same_polynomial先验证两边，再比较规范记录，未用有限求值样本作为对象相等判据。

degree对全零记录抛ValueError，其余给最大非零指标，非零常量返回0。evaluate先验证整张记录和有理输入，即使在t=0或系数全零也不跳过非法项/输入，之后以已定义自然幂和有限和求值；常数位0^0=1。add使用两非空记录的最大长度，故公共长度至少1，逐系数相加再规范化；scale即使scalar=0也先验证整张记录；subtract先验证双方，再加负一倍。所有返回系数记录均为规范Fraction元组，未引入多项式乘法。

主验证器已实际读完，其独立对照为SymPy QQ系数字典构造，包含degree零、尾零、缩放、加减、相等、求值线性和部分代数规律。父线程报告的主运行结果不冒称本审阅者重新执行了SymPy；下方只给本审阅者独立运行的实际输出。

## 独立oracle与边界

规范预期采用稀疏非零系数字典，以支持集最大指标恢复记录，而非照抄从尾端删零循环。加减预期在两个字典键的并集上合成；相等直接比较完整非零系数字典。求值用整数分子/分母的Horner过程，不调用被测power、finite_sum或SymPy，也不把有限样本当成对象相等的定义。

780张1至4项表检验规范化、幂等性、degree、6050个含界外的系数、5460次Horner求值、3900个补零情形、3900个标量情形及780次输入不变性。24025对1至3项表比较加、减和对象相等，并检查非零和的次数上界及异次数相加的等号；72075次独立求值线性。另1728组三表加法结合、1500次标量结合/标量和分配检查。274次非法输入覆盖每个API及双输入两侧，特别包含零缩放/零输入/界外系数查询不能掩盖坏项；10次零degree拒绝单独计数，不混入类型非法计数。

显式检查(1,0,2)与(1,2)在0、1同值却在2分别9、5，规范对象也不同。所有有限证据均不证明一般代数规律；正式文本必须另给逐位置等式及有限和证明。脚本当前明确从/tmp导入临时API，正式迁入仓库时应更新被测模块定位和版本绑定后再重放。

## 绑定哈希

| 文件 | SHA-256 |
| --- | --- |
| `/tmp/rational_polynomial_basic.py` | `4ab57898877c291e338241126e36ed79d4aeef8723c23e647f3591afbcf2243d` |
| `/tmp/validate_rational_polynomial_basic.py` | `ee02896ff2505b910187073da021e1b97e0d0306c1951f931e52bf1f5e564877` |
| `/tmp/polynomials_astra_oracle.py` | `169c00d1e965cd69a2f204620e38b5ea3b570c0aa261492b9ad971e2bef6fa33` |
| `/workspace/IntegratedMath-book/tools/rational_powers_sums.py` | `fad8cf2a22151b4d584ba09ea3464526668cf34d2737afdf0374f241f16cfda4` |
| `/workspace/IntegratedMath-book/tools/linear_equation_solvers.py` | `c3ec0ab4a892397d3d0af59a1acd367bf1f1cfea80e3e14bd6b2b6cd790b74c9` |

## 可重放完整脚本

命令：`python -B /tmp/polynomials_astra_oracle.py`。

```python
"""Independent bounded sparse-coefficient and integer-Horner checks."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import sys,json,hashlib
ROOT=Path('/workspace/IntegratedMath-book')
sys.path[:0]=['/tmp',str(ROOT/'tools')]
import rational_polynomial_basic as api
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

实际输出：

```text
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
