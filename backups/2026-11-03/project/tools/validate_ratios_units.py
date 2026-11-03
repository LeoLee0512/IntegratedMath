"""Finite independent Fraction checks for B1.20/21, not physical calibration."""
from pathlib import Path
from fractions import Fraction
from itertools import product
import datetime
import hashlib
import json
from rational_multiplication import multiply, reciprocal
from ratios_units import ratio, proportion, convert_value, convert_rate

ROOT = Path(__file__).resolve().parents[1]


def pair(f):
    return f.numerator, f.denominator


def rejects(fn, *args):
    try:
        fn(*args)
    except ValueError:
        return
    raise AssertionError((fn.__name__, args))


def main():
    records = [(a,b) for a in range(-3,4) for b in range(1,4)]
    small = [(a,b) for a in range(-1,2) for b in range(1,3)]
    scales = [(a,b) for a in range(1,4) for b in range(1,3)]
    counts = dict(ratio_pairs=0, ratio_zero_rejections=0,
                  proportion_quadruples=0, proportion_zero_rejections=0,
                  representative_changes=0, conversion_round_trips=0,
                  conversion_compositions=0, rate_conversions=0,
                  invalid_input_rejections=0, nonpositive_scale_rejections=0)
    for a,b in product(records,repeat=2):
        if b[0]==0:
            rejects(ratio,a,b);counts['ratio_zero_rejections']+=1
        else:
            assert ratio(a,b)==pair(Fraction(*a)/Fraction(*b))
            counts['ratio_pairs']+=1
            aa=(2*a[0],2*a[1]);bb=(3*b[0],3*b[1])
            assert ratio(aa,bb)==ratio(a,b)
            counts['representative_changes']+=1
    for a,b,c,d in product(small,repeat=4):
        if b[0]==0 or d[0]==0:
            rejects(proportion,a,b,c,d);counts['proportion_zero_rejections']+=1
        else:
            expected=Fraction(*a)/Fraction(*b)==Fraction(*c)/Fraction(*d)
            assert proportion(a,b,c,d)==expected
            counts['proportion_quadruples']+=1
    for x,k in product(records,scales):
        y=convert_value(x,k)
        assert y==pair(Fraction(*x)/Fraction(*k))
        assert convert_value(y,reciprocal(k))==pair(Fraction(*x))
        assert convert_value((2*x[0],2*x[1]),(3*k[0],3*k[1]))==y
        counts['conversion_round_trips']+=1
        counts['representative_changes']+=1
        for l in scales:
            assert convert_value(y,l)==convert_value(x,multiply(k,l))
            counts['conversion_compositions']+=1
            r=convert_rate(x,k,l)
            assert r==pair(Fraction(*x)*Fraction(*l)/Fraction(*k))
            assert convert_rate(r,reciprocal(k),reciprocal(l))==pair(Fraction(*x))
            counts['rate_conversions']+=1
    invalid=[None,(),(1,),(1,2,3),'12',(True,1),(1,False),
             (1.0,2),(1,2.0),('1',2),(1,0),(1,-2)]
    for v in invalid:
        for fn,arity in [(ratio,2),(proportion,4),(convert_value,2),(convert_rate,3)]:
            for pos in range(arity):
                args=[(1,1)]*arity;args[pos]=v;rejects(fn,*args)
                counts['invalid_input_rejections']+=1
    for v in [(0,1),(-1,1),(-2,3)]:
        rejects(convert_value,(1,1),v)
        rejects(convert_rate,(1,1),v,(1,1))
        rejects(convert_rate,(1,1),(1,1),v)
        counts['nonpositive_scale_rejections']+=3
    cases=[('ratio',[(2,3),(4,5)],(5,6)),
           ('ratio',[(0,1),(-2,1)],(0,1)),
           ('ratio',[(-3,1),(2,1)],(-3,2)),
           ('proportion',[(2,1),(3,1),(4,1),(6,1)],True),
           ('proportion',[(0,1),(2,1),(0,1),(-3,1)],True),
           ('proportion',[(2,1),(3,1),(3,1),(4,1)],False),
           ('convert_value',[(375,1),(100,1)],(15,4)),
           ('convert_value',[(3,4),(1,100)],(75,1)),
           ('convert_value',[(0,1),(1000,1)],(0,1)),
           ('convert_value',[(-3,2),(1,100)],(-150,1)),
           ('ratio',[(15,2),(3,2)],(5,1)),
           ('convert_rate',[(5,1),(1,1000),(1,3600)],(25,18)),
           ('convert_rate',[(25,18),(1000,1),(3600,1)],(5,1)),
           ('convert_value',[(7,4),(1,100)],(175,1)),
           ('convert_value',[(7,4),(1000,1)],(7,4000)),
           ('convert_value',[(6,1),(3,2)],(4,1)),
           ('convert_value',[(7,1),(2,3)],(21,2)),
           ('convert_value',[(21,2),(5,2)],(21,5)),
           ('convert_value',[(7,1),(5,3)],(21,5)),
           ('convert_value',[(21,5),(3,5)],(7,1)),
           ('ratio',[(3,2),(3,4)],(2,1)),
           ('ratio',[(9,2),(3,4)],(6,1)),
           ('convert_rate',[(6,1),(1,1000),(1,3600)],(5,3)),
           ('ratio',[(10,1),(4,1)],(5,2)),
           ('convert_rate',[(5,2),(2,1),(3,1)],(15,4)),
           ('proportion',[(4,1),(6,1),(2,1),(3,1)],True),
           ('ratio',[(3,4),(5,6)],(9,10)),
           ('proportion',[(2,1),(3,1),(8,1),(12,1)],True),
           ('ratio',[(18,1),(24,1)],(3,4))]
    functions={f.__name__:f for f in [ratio,proportion,convert_value,convert_rate]}
    examples=[]
    for op,inputs,expected in cases:
        result=functions[op](*inputs);fs=[Fraction(*r) for r in inputs]
        oracle=(fs[0]/fs[1]==fs[2]/fs[3] if op=='proportion' else
                pair(fs[0]*fs[2]/fs[1]) if op=='convert_rate' else pair(fs[0]/fs[1]))
        assert result==expected==oracle
        examples.append(dict(operation=op,inputs=inputs,result=result))
    paths=['tools/ratios_units.py','tools/validate_ratios_units.py',
           'tools/rational_multiplication.py','tools/rational_addition.py',
           'tools/extended_euclidean.py','tools/integer_euclidean.py','tools/natural_algorithms.py']
    report=dict(status='passed',validated_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
                scope=dict(records_a=[-3,3],records_b=[1,3],quadruple_a=[-1,1],
                           quadruple_b=[1,2],positive_scales_a=[1,3],positive_scales_b=[1,2]),
                counts=counts,examples=examples,independent_model='Python Fraction; exact integer arithmetic.',
                limits='Finite checks, not proofs, measurement validation, dimensional inference, real construction or affine-scale conversion. Callers supply compatible quantity kinds and correct positive scale relations.')
    (ROOT/'research/production/ratios_units_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(status='passed',counts=counts,examples=len(examples)),indent=2))

if __name__=='__main__':main()
