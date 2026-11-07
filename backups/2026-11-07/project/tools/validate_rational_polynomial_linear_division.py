"""Bounded exact checks for quotient and remainder by X-a."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json,hashlib
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
import sympy as s
from rational_polynomial_linear_division import divide_linear
from rational_polynomial_basic import normalize,add,evaluate,degree
from rational_polynomial_product import multiply
x=s.Symbol('x');vals=(F(-1),F(0),F(1,2))
records=[a for n in range(1,5) for a in product(vals,repeat=n)]
records += [tuple(map(F,a)) for a in [(-6,11,-6,1),(1,0,2),(0,0,0,0,0)]]
points=(F(-2),F(-1,2),F(0),F(1),F(2))
counts=dict(records=0,divisions=0,padding=0,suffixes=0,nonconstant_degree=0,constant_zero=0,rejections=0,immutability=0)

def poly(a):return s.Poly.from_dict({(i,):s.Rational(q.numerator,q.denominator) for i,q in enumerate(a)},x,domain=s.QQ)
def canonical(p):return tuple(F(int(q.p),int(q.q)) for q in reversed(p.all_coeffs()))
def verify(a,t):
    q,r=divide_linear(a,t)
    assert type(q)is tuple and len(q)>=1 and all(type(v)is F for v in q) and type(r)is F
    pq,pr=poly(a).div(s.Poly(x-s.Rational(t.numerator,t.denominator),x,domain=s.QQ))
    assert q==canonical(pq) and (r,)==canonical(pr)
    assert add(multiply((-t,F(1)),q),(r,))==normalize(a)
    assert r==evaluate(a,t)
    return q,r
for a in records:
    counts['records']+=1
    aa=list(a);old=aa.copy()
    for t in points:
        q,r=verify(aa,t);counts['divisions']+=1
        if poly(a).is_zero or poly(a).degree()==0:
            assert q==(F(0),);counts['constant_zero']+=1
        else:
            assert q!=(F(0),) and degree(q)+1==degree(a);counts['nonconstant_degree']+=1
        for n in (0,1,3):
            assert verify(a+(F(0),)*n,t)==(q,r);counts['padding']+=1
        for start in range(len(a)):
            verify(a[start:],t);counts['suffixes']+=1
    assert aa==old;counts['immutability']+=1
for bad in [[],(),None,1,'1',{0:1},{1},iter([1]),[True],[1.0],[F(1),False]]:
    for t in [0,F(-1,2)]:
        try:divide_linear(bad,t)
        except (TypeError,ValueError):counts['rejections']+=1
        else:raise AssertionError('accepted invalid record')
for bad in [True,False,1.0,None,'1',complex(1),[1]]:
    for a in [(0,),(1,),(1,0,2)]:
        try:divide_linear(a,bad)
        except (TypeError,ValueError):counts['rejections']+=1
        else:raise AssertionError('accepted invalid parameter')
examples=[]
for name,a,t,wq,wr in [
 ('cubic_root',(-6,11,-6,1),F(1),(6,-5,1),F(0)),
 ('nonzero_remainder',(1,0,2),F(2),(4,2),F(9)),
 ('constant',(F(-3,2),),F(-2),(0,),F(-3,2)),
 ('zero_tail',(0,0,0),F(1,2),(0,),F(0)),
 ('fractional',(F(1,2),F(-1,3),F(2,3)),F(-1,2),(F(-2,3),F(2,3)),F(5,6)),
 ('zero_parameter',(2,-3,4),F(0),(-3,4),F(2))]:
 q,r=verify(a,t);assert q==tuple(map(F,wq)) and r==wr
 examples.append(dict(name=name,record=a,at=t,quotient=q,remainder=r))
paths=['rational_polynomial_linear_division.py','validate_rational_polynomial_linear_division.py',
       'rational_polynomial_product.py','rational_polynomial_basic.py',
       'rational_powers_sums.py','linear_equation_solvers.py']
r={'schema_version':1,'status':'passed','validated_at':datetime.now(timezone.utc).isoformat(),
   'source_sha256':{'tools/'+n:hashlib.sha256((ROOT/'tools'/n).read_bytes()).hexdigest() for n in paths},
   'scope':{'coefficient_values':['-1','0','1/2'],'record_lengths':[1,4],
            'additional_records':[[-6,11,-6,1],[1,0,2],[0,0,0,0,0]],
            'points':['-2','-1/2','0','1','2']},
   'counts':counts,'examples':examples,'oracle':'SymPy '+s.__version__+' Poly over QQ, division by X-a',
   'limits':'Finite exact implementation checks only; neither universal proof nor complete manuscript/build acceptance.'}
out=ROOT/'research/production/rational_polynomial_linear_division_validation.json'
out.write_text(json.dumps(r,ensure_ascii=False,indent=2,default=str)+'\n')
print(json.dumps(r,ensure_ascii=False,indent=2,default=str))
