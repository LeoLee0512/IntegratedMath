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
