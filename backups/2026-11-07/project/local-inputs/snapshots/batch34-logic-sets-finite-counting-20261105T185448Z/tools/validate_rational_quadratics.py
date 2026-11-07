"""Finite exact quadratic and rational-square checks, supporting general proofs."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import math,json,hashlib
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
import sympy as s
from rational_quadratics import integer_sqrt,rational_square_root,solve_quadratic
x=s.Symbol('x');counts=dict(integer_bounds=0,rational_squares=0,quadratics=0,all=0,none=0,finite_one=0,finite_two=0,rejections=0)
for n in list(range(4096))+[10**100+k for k in (-1,0,1)]+[(10**60+1)**2+k for k in (-1,0,1)]:
 z=integer_sqrt(n);assert type(z)is int and z>=0 and z*z<=n<(z+1)*(z+1) and z==math.isqrt(n)
 counts['integer_bounds']+=1
for a,b in product(range(-80,81),range(1,20)):
 value=F(a,b);actual=rational_square_root(value)
 if value<0:assert actual is None
 else:
  p,q=value.numerator,value.denominator;m,n=math.isqrt(p),math.isqrt(q)
  expected=F(m,n) if m*m==p and n*n==q else None
  assert actual==expected
  if actual is not None:assert type(actual)is F and actual>=0 and actual*actual==value
 counts['rational_squares']+=1
vals=(F(-2),F(-1),F(-3,4),F(-1,2),F(0),F(1,2),F(2,3),F(1),F(2))
for a,b,c in product(vals,repeat=3):
 actual=solve_quadratic(a,b,c)
 if a==b==c==0:expected={'kind':'all'}
 else:
  p=s.Poly.from_dict({(2,):s.Rational(a.numerator,a.denominator),(1,):s.Rational(b.numerator,b.denominator),(0,):s.Rational(c.numerator,c.denominator)},x,domain=s.QQ)
  roots=tuple(sorted(F(int(r.p),int(r.q)) for r in p.ground_roots()))
  expected={'kind':'finite','roots':roots} if roots else {'kind':'none'}
 assert actual==expected,(a,b,c,actual,expected)
 if actual['kind']=='finite':
  roots=actual['roots'];assert type(roots)is tuple and len(roots)in(1,2)
  assert all(type(t)is F and a*t*t+b*t+c==0 for t in roots)
  assert tuple(sorted(set(roots)))==roots
  counts['finite_one' if len(roots)==1 else 'finite_two']+=1
 else:counts[actual['kind']]+=1
 counts['quadratics']+=1
for bad in [True,False,1.0,F(1),-1,None,'1']:
 try:integer_sqrt(bad)
 except (ValueError,TypeError):counts['rejections']+=1
 else:raise AssertionError('illegal integer accepted')
for bad in [True,False,1.0,None,'1',complex(1),[1]]:
 for fun,args in [(rational_square_root,(bad,)),(solve_quadratic,(bad,0,0)),(solve_quadratic,(0,bad,0)),(solve_quadratic,(0,0,bad))]:
  try:fun(*args)
  except (ValueError,TypeError):counts['rejections']+=1
  else:raise AssertionError('illegal rational accepted')
examples=[]
for name,value,expected in [('square_zero',F(0),F(0)),('square_reduced',F(8,18),F(2,3)),('square_nonsquare',F(2),None)]:
 output=rational_square_root(value);assert output==expected
 examples.append(dict(name=name,operation='rational_square_root',inputs=[value],output=output))
for name,args,expected in [
 ('linear',(0,2,-6),{'kind':'finite','roots':(F(3),)}),
 ('quadratic_two',(F(3,2),-1,F(-1,2)),{'kind':'finite','roots':(F(-1,3),F(1))}),
 ('quadratic_repeated',(1,-3,F(9,4)),{'kind':'finite','roots':(F(3,2),)}),
 ('quadratic_all',(0,0,0),{'kind':'all'}),
 ('quadratic_negative_leading',(-1,3,-2),{'kind':'finite','roots':(F(1),F(2))})]:
 output=solve_quadratic(*args);assert output==expected
 examples.append(dict(name=name,operation='solve_quadratic',inputs=args,output=output))
paths=['rational_quadratics.py','validate_rational_quadratics.py','linear_equation_solvers.py']
r=dict(schema_version=1,status='passed',validated_at=datetime.now(timezone.utc).isoformat(),
 source_sha256={'tools/'+n:hashlib.sha256((ROOT/'tools'/n).read_bytes()).hexdigest() for n in paths},
 scope={'integer_range':[0,4095],'large_integer_cases':6,'fraction_numerators':[-80,80],'fraction_denominators':[1,19],
        'quadratic_coefficients':['-2','-1','-3/4','-1/2','0','1/2','2/3','1','2']},
 counts=counts,examples=examples,oracle='Python math.isqrt and SymPy '+s.__version__+' Poly QQ ground_roots',
 limits='Finite exact implementation checks only; not universal proof, formal verification or final manuscript/build acceptance.')
out=ROOT/'research/production/rational_quadratics_validation.json';out.write_text(json.dumps(r,ensure_ascii=False,indent=2,default=str)+'\n')
print(json.dumps(r,ensure_ascii=False,indent=2,default=str))
