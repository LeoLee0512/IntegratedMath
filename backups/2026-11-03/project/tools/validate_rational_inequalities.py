"""Finite exact interval checks; external real-set oracle is restricted to Q.

All finite endpoints here are rational. Equality of these finite real interval
unions implies equality of their restrictions to Q. This is implementation
evidence, not a proof of the manuscript's general theorems.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import datetime
import hashlib
import json
import operator
import sympy as sp
from rational_inequalities import solve_linear, solve_absolute, contains

ROOT = Path(__file__).resolve().parents[1]
OPS = {'<': operator.lt, '<=': operator.le,
       '>': operator.gt, '>=': operator.ge}


def symbol(q):
    return sp.Rational(q.numerator, q.denominator)


def real_intervals(solution):
    sets = []
    for low, high, lc, rc in solution:
        assert type(lc) is bool and type(rc) is bool
        assert low is None or type(low) is F
        assert high is None or type(high) is F
        assert low is not None or lc is False
        assert high is not None or rc is False
        if low is not None and high is not None:
            assert low < high or (low == high and lc and rc)
        sets.append(sp.Interval(-sp.oo if low is None else symbol(low),
                                sp.oo if high is None else symbol(high),
                                left_open=not lc, right_open=not rc))
    return sp.Union(*sets)


def reject(fn, *args):
    try:
        fn(*args)
    except ValueError:
        return
    raise AssertionError(('invalid input accepted', fn.__name__, args))


def main():
    x = sp.Symbol('x', real=True)
    values = [F(-1), F(-1, 2), F(0), F(1, 2), F(1)]
    counts = dict(linear=0, absolute=0, full_set_oracle=0,
                  rational_membership=0, finite_endpoint_checks=0,
                  invalid_coefficients=0, invalid_relations=0,
                  invalid_membership_values=0, extra_domain_checks=0)
    for absolute in [False, True]:
        fn = solve_absolute if absolute else solve_linear
        for a, b, c in product(values, repeat=3):
            expression = symbol(a)*x+symbol(b)
            if absolute:
                expression = sp.Abs(expression)
            for relation, op in OPS.items():
                result = fn(a, b, c, relation)
                expected = sp.solve_univariate_inequality(
                    op(expression, symbol(c)), x, relational=False)
                actual = real_intervals(result)
                assert actual == expected, (a, b, c, relation, result, expected)
                counts['absolute' if absolute else 'linear'] += 1
                counts['full_set_oracle'] += 1
                endpoints = {q for interval in result for q in interval[:2]
                             if q is not None}
                candidates = {F(n, 2) for n in range(-4, 5)} | endpoints
                for end in endpoints:
                    candidates.update([end-F(1, 3), end+F(1, 3)])
                for q in candidates:
                    value = abs(a*q+b) if absolute else a*q+b
                    assert contains(result, q) == op(value, c)
                    counts['rational_membership'] += 1
                    if q in endpoints:
                        counts['finite_endpoint_checks'] += 1
    bad = [None, True, False, 0.5, '1/2', (1, 2)]
    for fn in [solve_linear, solve_absolute]:
        for i in range(3):
            for value in bad:
                args = [1, 0, 1, '<=']; args[i] = value
                reject(fn, *args); counts['invalid_coefficients'] += 1
        for relation in ['=', '!=', 'le', None, True, 1]:
            reject(fn, 1, 0, 1, relation); counts['invalid_relations'] += 1
    for value in bad:
        reject(contains, (), value); counts['invalid_membership_values'] += 1
    # A caller's extra D is filtered explicitly; the solver itself knows no D.
    domain = [F(-1), F(0), F(1), F(2)]
    solution = solve_linear(-2, 1, 0, '<')
    assert tuple(q for q in domain if contains(solution, q)) == (F(1), F(2))
    counts['extra_domain_checks'] += 1
    assert not any(contains(solve_absolute(1, 0, 1, '<'), q) for q in [])
    counts['extra_domain_checks'] += 1
    examples = [
        ('negative coefficient reverses strict direction', solve_linear(-2, 1, 0, '<') == ((F(1, 2), None, False, False),)),
        ('zero coefficient equal threshold: strict false, weak true', solve_linear(0, 1, 1, '<') == () and solve_linear(0, 1, 1, '<=') == ((None, None, False, False),)),
        ('negative absolute threshold: upper empty and lower all', solve_absolute(1, 0, -1, '<=') == () and solve_absolute(1, 0, -1, '>') == ((None, None, False, False),)),
        ('zero threshold distinguishes singleton, empty, all, punctured set', solve_absolute(2, -1, 0, '<=') == ((F(1, 2), F(1, 2), True, True),) and solve_absolute(2, -1, 0, '<') == () and solve_absolute(2, -1, 0, '>=') == ((None, None, False, False),) and solve_absolute(2, -1, 0, '>') == ((None,F(1,2),False,False),(F(1,2),None,False,False))),
        ('constant absolute value checked before dividing by a', solve_absolute(0, -2, 1, '<=') == () and solve_absolute(0, -2, 1, '>') == ((None, None, False, False),)),
        ('negative affine slope has a positive half width', solve_absolute(-2, 1, 3, '<=') == ((F(-1),F(2),True,True),)),
    ]
    assert all(ok for _, ok in examples)
    paths = ['tools/linear_equation_solvers.py', 'tools/rational_inequalities.py',
             'tools/validate_rational_inequalities.py']
    report = dict(status='passed', checked_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  domain='Five coefficients {-1,-1/2,0,1/2,1}, three slots, four comparisons, each of two solver families',
                  oracle='SymPy '+sp.__version__+' exact full real interval unions, then rational membership checks',
                  source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
                  counts=counts, explicit_examples=[name for name, _ in examples],
                  limits='Finite coefficient cases only; interval records represent Q subsets. No expression parsing, additional D filtering, real construction or formal proof is provided.')
    (ROOT/'research/production/rational_inequalities_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(counts,indent=2))


if __name__ == '__main__':
    main()
