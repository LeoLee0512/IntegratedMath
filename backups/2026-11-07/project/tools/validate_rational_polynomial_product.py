"""Finite SymPy oracle checks; never a universal algebraic proof."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json,hashlib
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
import sympy as s
from rational_polynomial_basic import normalize,add,scale,evaluate,degree
from rational_polynomial_product import shift,multiply
x=s.Symbol('x')
values=(F(-1),F(0),F(1,2),F(2))
records=[a for n in range(1,4) for a in product(values,repeat=n)]
points=(F(-2),F(-1,2),F(0),F(1),F(2))
counts=dict(records=0,pairs=0,evaluations=0,padding=0,scalings=0,triples=0,rejections=0,immutability=0)

def poly(a):
    return s.Poly.from_dict({(i,):s.Rational(q.numerator,q.denominator) for i,q in enumerate(a)},x,domain=s.QQ)

def canonical(p):
    return tuple(F(int(q.p),int(q.q)) for q in reversed(p.all_coeffs()))

def exact(a,b):
    assert type(a) is tuple and all(type(q) is F for q in a) and a==b,(a,b)

oracles={a:poly(a) for a in records}
for a in records:
    pa=oracles[a]
    exact(shift(a),canonical(pa*s.Poly(x,x,domain=s.QQ)))
    exact(multiply(a,(1,)),canonical(pa))
    exact(multiply((0,),a),(F(0),))
    for t in points:assert evaluate(shift(a),t)==t*evaluate(a,t)
    for k in range(3):
        exact(shift(a+(F(0),)*k),canonical(pa*s.Poly(x,x,domain=s.QQ)))
    aa=list(a); old=aa.copy();shift(aa);multiply(aa,aa);assert aa==old
    counts['immutability']+=1;counts['records']+=1
for a,b in product(records,repeat=2):
    expected=canonical(oracles[a]*oracles[b]); result=multiply(a,b)
    exact(result,expected);exact(multiply(b,a),expected)
    exact(multiply(shift(a),b),shift(result));exact(multiply(a,shift(b)),shift(result))
    if not oracles[a].is_zero and not oracles[b].is_zero:
        assert degree(result)==degree(a)+degree(b)
        assert result[-1]==normalize(a)[-1]*normalize(b)[-1]
    else:assert result==(F(0),)
    for t in points:
        assert evaluate(result,t)==evaluate(a,t)*evaluate(b,t)
        counts['evaluations']+=1
    for k in (0,1,3):
        exact(multiply(a+(F(0),)*k,b+(F(0),)*k),expected)
        counts['padding']+=1
    for c in (F(0),F(-1,2),F(2)):
        target=canonical(s.Poly(s.Rational(c.numerator,c.denominator),x,domain=s.QQ)*oracles[a]*oracles[b])
        exact(multiply(scale(c,a),b),target);exact(multiply(a,scale(c,b)),target)
        counts['scalings']+=1
    counts['pairs']+=1
small=[a for n in (1,2) for a in product((F(-1),F(0),F(1,2)),repeat=n)]
for a,b,c in product(small,repeat=3):
    expected=canonical(poly(a)*poly(b)*poly(c))
    exact(multiply(multiply(a,b),c),expected);exact(multiply(a,multiply(b,c)),expected)
    exact(multiply(add(a,b),c),canonical((poly(a)+poly(b))*poly(c)))
    exact(multiply(a,add(b,c)),canonical(poly(a)*(poly(b)+poly(c))))
    counts['triples']+=1
for bad in [[],(),None,1,'1',{0:1},{1},iter([1]),[True],[1.0],[F(1),False]]:
    for fn,args in [(shift,(bad,)),(multiply,(bad,(0,))),(multiply,((0,),bad))]:
        try:fn(*args)
        except (TypeError,ValueError):counts['rejections']+=1
        else:raise AssertionError('accepted illegal input')
examples=[
    {'name':'zero_shift','output':shift((0,0))},
    {'name':'coefficient_convolution','left':[1,-1,2],'right':[0,3], 'output':multiply((1,-1,2),(0,3))},
    {'name':'square_difference','output':multiply((-2,1),(2,1))},
    {'name':'fractional_coefficients','output':multiply((F(1,2),0,F(-1,3)),(-2,1))},
    {'name':'zero_product','output':multiply((0,0),(1,0,2))},
    {'name':'tail_zero_representatives','output':multiply((1,1,0,0),(1,-1,0))}]
expected=[(F(0),),(F(0),F(3),F(-3),F(6)),(F(-4),F(0),F(1)),
          (F(-1),F(1,2),F(2,3),F(-1,3)),(F(0),),(F(1),F(0),F(-1))]
for item,target in zip(examples,expected):exact(item['output'],target)
paths=['rational_polynomial_product.py','validate_rational_polynomial_product.py',
       'rational_polynomial_basic.py','rational_powers_sums.py','linear_equation_solvers.py']
r={'schema_version':1,'status':'passed','validated_at':datetime.now(timezone.utc).isoformat(),
   'source_sha256':{'tools/'+n:hashlib.sha256((ROOT/'tools'/n).read_bytes()).hexdigest() for n in paths},
   'scope':{'coefficient_values':['-1','0','1/2','2'],'record_lengths':[1,3],
            'triple_coefficient_values':['-1','0','1/2'],'triple_lengths':[1,2],
            'points':['-2','-1/2','0','1','2']},
   'counts':counts,'examples':examples,'oracle':'SymPy '+s.__version__+' Poly over QQ',
   'limits':'Finite exact implementation checks only; not universal proofs or final manuscript/build acceptance.'}
out=ROOT/'research/production/rational_polynomial_product_validation.json'
out.write_text(json.dumps(r,ensure_ascii=False,indent=2,default=str)+'\n')
print(json.dumps(r,ensure_ascii=False,indent=2,default=str))
