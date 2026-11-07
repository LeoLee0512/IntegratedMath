"""Bounded exact checks against SymPy rank and solution oracles, not proofs."""
from pathlib import Path
from fractions import Fraction
from itertools import product
import datetime
import hashlib
import json
import sympy as sp
from linear_equation_solvers import solve_linear, solve_system

ROOT = Path(__file__).resolve().parents[1]


def pair(q):
    return [q.numerator, q.denominator]


def as_sympy(q):
    return sp.Rational(q.numerator, q.denominator)


def rejects(fn, args):
    try:
        fn(*args)
    except ValueError:
        return
    raise AssertionError('invalid coefficient accepted')


def contains(result, x, y):
    if result['kind'] == 'none':
        return False
    if result['kind'] == 'all':
        return True
    if result['kind'] == 'unique':
        return (x, y) == result['point']
    px, py = result['base']
    ux, uy = result['direction']
    t = (x-px)/ux if ux != 0 else (y-py)/uy
    return (x, y) == (px+t*ux, py+t*uy)


def main():
    counts = dict(linear_equations=0, linear_candidate_checks=0,
                  systems=0, unique=0, none=0, line=0, all=0,
                  candidate_pairs=0, parameter_points=0,
                  row_swap_checks=0, invalid_rejections=0)
    small = [Fraction(n) for n in [-2, -1, 0, 1, 2]]
    for a, b, c in product(small, repeat=3):
        result = solve_linear(a, b, c)
        x = sp.Symbol('x')
        expected = sp.solveset(as_sympy(a)*x+as_sympy(b)-as_sympy(c), x, domain=sp.S.Rationals)
        if expected is sp.S.Rationals:
            assert result == {'kind': 'all'}
        elif expected is sp.S.EmptySet:
            assert result == {'kind': 'none'}
        else:
            assert result['kind'] == 'unique'
            assert expected == sp.FiniteSet(as_sympy(result['value']))
        for q in small:
            actual = result['kind'] == 'all' or (result['kind'] == 'unique' and q == result['value'])
            assert actual == (a*q+b == c)
            counts['linear_candidate_checks'] += 1
        counts['linear_equations'] += 1
    systems = list(product([Fraction(-1), Fraction(0), Fraction(1)], repeat=6))
    # Fractional pivots, negative coefficients and an independent second row.
    systems += [(Fraction(1,2), Fraction(-2,3), Fraction(5,7), Fraction(-3,4), Fraction(2,5), Fraction(0)),
                (Fraction(0), Fraction(0), Fraction(0), Fraction(2,3), Fraction(4,3), Fraction(-1,2)),
                (Fraction(1,2), Fraction(1,3), Fraction(1,4), Fraction(1), Fraction(2,3), Fraction(1,2))]
    for values in systems:
        a, b, c, d, e, f = values
        result = solve_system(*values)
        m = sp.Matrix([[as_sympy(a), as_sympy(b)], [as_sympy(d), as_sympy(e)]])
        rhs = sp.Matrix([as_sympy(c), as_sympy(f)])
        rank = m.rank(); augmented_rank = m.row_join(rhs).rank()
        expected_kind = 'none' if rank < augmented_rank else ('unique' if rank == 2 else 'line' if rank == 1 else 'all')
        assert result['kind'] == expected_kind
        if expected_kind == 'unique':
            expected = m.inv()*rhs
            assert [as_sympy(q) for q in result['point']] == list(expected)
        elif expected_kind == 'line':
            px, py = result['base']; ux, uy = result['direction']
            assert (ux, uy) != (0, 0)
            assert (a*px+b*py, d*px+e*py) == (c, f)
            assert (a*ux+b*uy, d*ux+e*uy) == (0, 0)
            for t in small:
                x, y = px+t*ux, py+t*uy
                assert (a*x+b*y, d*x+e*y) == (c, f)
                counts['parameter_points'] += 1
        swapped = solve_system(d, e, f, a, b, c)
        assert swapped['kind'] == expected_kind
        for x, y in product(small, repeat=2):
            expected = a*x+b*y == c and d*x+e*y == f
            assert contains(result, x, y) == expected
            assert contains(swapped, x, y) == expected
            counts['candidate_pairs'] += 1
        counts['row_swap_checks'] += 1
        counts['systems'] += 1
        counts[expected_kind] += 1
    invalid = [None, True, False, 0.5, '1/2', (1, 2)]
    for fn, arity in [(solve_linear, 3), (solve_system, 6)]:
        for position in range(arity):
            for bad in invalid:
                args = [0]*arity; args[position] = bad
                rejects(fn, args); counts['invalid_rejections'] += 1
    examples = []
    assert solve_linear(0, 2, 2) == {'kind': 'all'}
    assert solve_linear(0, 2, 3) == {'kind': 'none'}
    examples.append('zero one-variable coefficient: identity and contradiction distinguished')
    assert solve_system(0,0,0,0,0,0) == {'kind': 'all'}
    assert solve_system(0,0,1,0,0,0) == {'kind': 'none'}
    examples.append('both zero rows: all pairs or contradiction')
    assert solve_system(1,2,3,2,4,7) == {'kind': 'none'}
    assert solve_system(1,2,3,2,4,6)['kind'] == 'line'
    examples.append('zero scalar combination: inconsistent and dependent consistent distinguished')
    assert solve_system(0,2,4,3,1,5) == {'kind': 'unique', 'point': (Fraction(1),Fraction(2))}
    examples.append('zero first coefficient uses a nonzero second-coordinate pivot')
    assert solve_system(0,0,0,2,4,6)['kind'] == 'line'
    examples.append('first zero row is swapped with the nonzero row')
    result = solve_system(2,3,7,4,-1,7)
    assert result == {'kind': 'unique', 'point': (Fraction(2),Fraction(1))}
    examples.append('unique pair checked in both original equations')
    files = ['tools/linear_equation_solvers.py','tools/validate_linear_equation_solvers.py']
    report = dict(status='passed', checked_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  domain='125 one-variable equations on {-2,-1,0,1,2}; 729 two-row systems on {-1,0,1} plus 3 rational cases; 25 candidate pairs per system',
                  oracle='SymPy '+sp.__version__+' exact solveset/rank/inverse, direct Fraction substitution',
                  counts=counts, explicit_examples=examples,
                  source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in files},
                  limits='Finite external checks, not proofs. Solvers cover all rational unknowns only; extra domain exclusions are not parsed or imposed.')
    (ROOT/'research/production/linear_equation_solvers_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(counts,indent=2))


if __name__ == '__main__':
    main()
