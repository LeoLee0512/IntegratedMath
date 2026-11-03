"""Independent finite checks using SymPy QQ polynomials, not textbook proofs."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib,json,sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
import sympy as sp
import rational_polynomial_basic as api

VALUES=(F(-1),F(0),F(1,2))
POINTS=(F(-2),F(-1,2),F(0),F(1),F(2))
x=sp.Symbol('x')
def records(maximum):
    return [tuple(a) for n in range(1,maximum+1) for a in product(VALUES,repeat=n)]
def oracle(a):
    return sp.Poly.from_dict({(i,):sp.Rational(v.numerator,v.denominator) for i,v in enumerate(a)},x,domain=sp.QQ)
def fraction(v):return F(int(v.p),int(v.q))
def canonical(p):return tuple(fraction(v) for v in reversed(p.all_coeffs()))
def main():
    counts={key:0 for key in ['records','coefficients','evaluations','padding','scalings','pairs','evaluation_linearity','triples','rejected_inputs','input_immutability']}
    for a in records(4):
        p=oracle(a);n=api.normalize(a);assert n==canonical(p)
        assert api.normalize(n)==n
        if p.is_zero:
            try:api.degree(a)
            except ValueError:pass
            else:raise AssertionError('zero degree accepted')
        else:assert api.degree(a)==int(p.degree())
        counts['records']+=1
        for i in range(len(a)+3):
            assert api.coefficient(a,i)==fraction(p.nth(i));counts['coefficients']+=1
        for t in POINTS:
            assert api.evaluate(a,t)==fraction(p.eval(sp.Rational(t.numerator,t.denominator)));counts['evaluations']+=1
        for extra in range(4):
            padded=a+(F(0),)*extra
            assert api.normalize(padded)==n and api.same_polynomial(a,padded)
            for t in POINTS:assert api.evaluate(padded,t)==api.evaluate(a,t)
            counts['padding']+=1
        for scalar in VALUES:
            result=api.scale(scalar,a)
            assert result==canonical(sp.Rational(scalar.numerator,scalar.denominator)*p)
            assert api.scale(1,a)==n and api.scale(0,a)==(F(0),)
            for t in POINTS:assert api.evaluate(result,t)==scalar*api.evaluate(a,t)
            if scalar and not p.is_zero:assert api.degree(result)==api.degree(a)
            counts['scalings']+=1
        mutable=list(a);copy=mutable.copy()
        api.normalize(mutable);api.evaluate(mutable,F(1,2));api.scale(-1,mutable)
        assert mutable==copy;counts['input_immutability']+=1
    small=records(3)
    for a,b in product(small,repeat=2):
        p,q=oracle(a),oracle(b);result=api.add(a,b)
        assert result==canonical(p+q)
        assert api.subtract(a,b)==canonical(p-q)
        assert api.same_polynomial(a,b)==(p==q)
        assert result==api.add(b,a)
        if not p.is_zero and not q.is_zero and not (p+q).is_zero:
            assert api.degree(result)<=max(api.degree(a),api.degree(b))
        for t in POINTS:
            assert api.evaluate(result,t)==api.evaluate(a,t)+api.evaluate(b,t)
            counts['evaluation_linearity']+=1
        for scalar in VALUES:
            assert api.scale(scalar,result)==api.add(api.scale(scalar,a),api.scale(scalar,b))
        counts['pairs']+=1
    for a,b,c in product(records(2),repeat=3):
        assert api.add(api.add(a,b),c)==api.add(a,api.add(b,c));counts['triples']+=1
    for a in small:
        for s,t in product(VALUES,repeat=2):
            assert api.scale(s,api.scale(t,a))==api.scale(s*t,a)
            assert api.scale(s+t,a)==api.add(api.scale(s,a),api.scale(t,a))
        assert api.add(a,api.scale(-1,a))==(F(0),)
    invalid=[]
    for bad in [[],(),None,1,'1',{0:1},{1},iter([1]),[True],[1.0],[F(1),False]]:
        invalid.extend([(api.normalize,(bad,)),(api.coefficient,(bad,0)),(api.evaluate,(bad,0)),(api.scale,(0,bad)),(api.add,((1,),bad)),(api.add,(bad,(1,))), (api.same_polynomial,((1,),bad))])
    for bad in [True,1.0,F(1),-1,None]:invalid.append((api.coefficient,((1,),bad)))
    for bad in [True,1.0,None,'1']:
        invalid.extend([(api.evaluate,((0,),bad)),(api.scale,(bad,(0,)))])
    invalid.append((api.degree,((0,0),)))
    for function,args in invalid:
        try:function(*args)
        except (TypeError,ValueError):counts['rejected_inputs']+=1
        else:raise AssertionError((function.__name__,args))
    result={'status':'passed','oracle':'SymPy '+sp.__version__+' Poly over QQ from independent coefficient dictionary','counts':counts,'limits':'Finite examples support the implementation; not general proofs or a formalization of the manuscript.'}
    result['scope']={'coefficient_values':[str(x) for x in VALUES], 'record_lengths':[1,4], 'pair_lengths':[1,3], 'triple_lengths':[1,2], 'points':[str(x) for x in POINTS]}
    root=Path(__file__).resolve().parents[1]
    names=['tools/rational_polynomial_basic.py','tools/validate_rational_polynomial_basic.py','tools/rational_powers_sums.py','tools/linear_equation_solvers.py']
    result['source_sha256']={name:hashlib.sha256((root/name).read_bytes()).hexdigest() for name in names}
    result['examples']=[
        {'name':'tail_zero_normalization','input':[1,0,2,0,0],'output':[str(x) for x in api.normalize((1,0,2,0,0))]},
        {'name':'zero_normalization','input':[0,0,0],'output':[str(x) for x in api.normalize((0,0,0))]},
        {'name':'internal_zero_is_not_tail','at':2,'left':str(api.evaluate((1,0,2),2)),'right':str(api.evaluate((1,2),2))},
        {'name':'leading_cancellation','left':[1,2],'right':[3,-2],'output':[str(x) for x in api.add((1,2),(3,-2))]},
        {'name':'total_cancellation','output':[str(x) for x in api.add((1,2),(-1,-2))]},
        {'name':'negative_scaling','output':[str(x) for x in api.scale(F(-1,2),(1,-1,2))]}
    ]
    output=root/'research/production/rational_polynomial_basic_validation.json'
    output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
