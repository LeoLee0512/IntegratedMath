"""Independent finite checks of exact coordinate and affine routines.

SymPy solves the original equations; finite graph expectations are enumerated
from all maps on the supplied finite sets, not the tested uniqueness algorithm.
These checks do not prove the manuscript's universal statements.
"""
from fractions import Fraction as F
from itertools import product, combinations
from pathlib import Path
import datetime
import hashlib
import json
import sympy as sp
from rational_affine import (affine_value, slope_through, intercepts,
                            intersect_affine, classify_linear_relation,
                            finite_graph_test)

ROOT = Path(__file__).resolve().parents[1]


def symbol(q):
    return sp.Rational(q.numerator, q.denominator)


def subsets(items):
    return [tuple(c) for n in range(len(items)+1) for c in combinations(items, n)]


def reject(fn, *args):
    try:
        fn(*args)
    except ValueError:
        return
    raise AssertionError(('invalid input accepted', fn.__name__, args))


def main():
    values = [F(-1), F(-1, 2), F(0), F(1, 2), F(1)]
    x, y = sp.symbols('x y')
    counts = dict(values=0, two_points=0, equal_x_rejected=0,
                  intersections=0, intersection_membership=0,
                  intercepts=0, linear_relations=0, relation_membership=0,
                  finite_graphs=0, input_rejections=0, duplicate_graphs=0)
    for a, b, t in product(values, repeat=3):
        assert symbol(affine_value(a, b, t)) == symbol(a)*symbol(t)+symbol(b)
        counts['values'] += 1
    for x1, y1, x2, y2 in product(values, repeat=4):
        if x1 == x2:
            reject(slope_through, x1, y1, x2, y2)
            counts['equal_x_rejected'] += 1
            continue
        a, b = slope_through(x1, y1, x2, y2)
        aa, bb = sp.symbols('aa bb')
        oracle = sp.linsolve([symbol(x1)*aa+bb-symbol(y1),
                             symbol(x2)*aa+bb-symbol(y2)], (aa, bb))
        assert oracle == sp.FiniteSet((symbol(a), symbol(b)))
        counts['two_points'] += 1
    for a, b, c, d in product(values, repeat=4):
        result = intersect_affine(a, b, c, d)
        oracle = sp.linsolve([y-symbol(a)*x-symbol(b),
                             y-symbol(c)*x-symbol(d)], (x, y))
        if result['kind'] == 'none':
            assert oracle == sp.EmptySet and result['point'] is None
        elif result['kind'] == 'unique':
            assert oracle == sp.FiniteSet(tuple(symbol(t) for t in result['point']))
        else:
            assert result['kind'] == 'coincident' and result['point'] is None
            assert oracle != sp.EmptySet
            pair = next(iter(oracle))
            assert set().union(*(v.free_symbols for v in pair))
            assert sp.expand(pair[1]-symbol(a)*pair[0]-symbol(b)) == 0
            assert sp.expand(pair[1]-symbol(c)*pair[0]-symbol(d)) == 0
        for u, v in product(values, repeat=2):
            expected = v == a*u+b and v == c*u+d
            actual = (result['point'] == (u, v) if result['kind'] == 'unique'
                      else v == a*u+b if result['kind'] == 'coincident' else False)
            assert actual == expected
            counts['intersection_membership'] += 1
        counts['intersections'] += 1
    for a, b in product(values, repeat=2):
        result = intercepts(a, b)
        assert result['vertical'] == (0, b)
        oracle = sp.linsolve([symbol(a)*x+symbol(b)], (x,))
        if result['horizontal_kind'] == 'unique':
            assert result['horizontal'][1] == 0
            assert oracle == sp.FiniteSet((symbol(result['horizontal'][0]),))
        elif result['horizontal_kind'] == 'none':
            assert oracle == sp.EmptySet and result['horizontal'] is None
        else:
            assert result['horizontal_kind'] == 'all'
            assert oracle == sp.FiniteSet((x,)) and result['horizontal'] is None
        counts['intercepts'] += 1
    for p, q, r in product(values, repeat=3):
        result = classify_linear_relation(p, q, r)
        oracle = sp.linsolve([symbol(p)*x+symbol(q)*y-symbol(r)], (x, y))
        kind = result['kind']
        if kind == 'none':
            assert oracle == sp.EmptySet
        else:
            assert oracle != sp.EmptySet
            pair = next(iter(oracle))
            if kind == 'all':
                assert pair == (x, y)
            elif kind == 'vertical':
                assert pair == (symbol(result['x']), y)
            else:
                assert kind == 'affine'
                assert sp.expand(pair[1]-symbol(result['a'])*pair[0]-symbol(result['b'])) == 0
                assert pair != (x, y)
        for u, v in product(values, repeat=2):
            actual = (True if kind == 'all' else False if kind == 'none'
                      else u == result['x'] if kind == 'vertical'
                      else v == result['a']*u+result['b'])
            assert actual == (p*u+q*v == r)
            counts['relation_membership'] += 1
        counts['linear_relations'] += 1
    universe = [F(-1), F(0), F(1)]
    point_sets = subsets(list(product(universe, repeat=2)))
    for domain in subsets(universe):
        for codomain in subsets(universe):
            possible_graphs = {frozenset(zip(domain, outputs))
                               for outputs in product(codomain, repeat=len(domain))}
            for graph in point_sets:
                expected = frozenset(graph) in possible_graphs
                assert finite_graph_test(domain, codomain, graph) == expected
                counts['finite_graphs'] += 1
    for domain, codomain, graph in [([0, 0], [1, 1], [(0, 1), (0, 1)]),
                                     ([], [], []), ([], [0], [])]:
        assert finite_graph_test(domain, codomain, graph)
        counts['duplicate_graphs'] += 1
    bad = [None, True, False, 0.5, '1/2', (1, 2)]
    specs = [(affine_value, [1, 0, 1]), (slope_through, [0, 1, 1, 2]),
             (intercepts, [1, 0]), (intersect_affine, [1, 0, -1, 0]),
             (classify_linear_relation, [1, 1, 1])]
    for fn, template in specs:
        for i in range(len(template)):
            for value in bad:
                args = list(template); args[i] = value
                reject(fn, *args); counts['input_rejections'] += 1
    for args in [([True], [0], []), ([0], [0.5], []),
                 ([0], [0], [(0, False)]), ([0], [0], [(0,)]),
                 ([0], [0], [(0, 0, 0)]), ([0], [0], [0]),
                 ('0', [0], []), ([0], None, []), ([0], [0], None),
                 ([0], [0], [(1, 0), (0, True)])]:
        reject(finite_graph_test, *args); counts['input_rejections'] += 1
    examples = [
        {'case': '2x-1 and -x+2', 'result': intersect_affine(2, -1, -1, 2)},
        {'case': 'zero graph intercepts', 'result': intercepts(0, 0)},
        {'case': 'constant nonzero intercepts', 'result': intercepts(0, 3)},
        {'case': 'vertical relation 2x=1', 'result': classify_linear_relation(2, 0, 1)},
        {'case': 'two points (0,-1),(1,1)', 'result': slope_through(0, -1, 1, 1)},
        {'case': 'missing input', 'result': finite_graph_test([0, 1], [0], [(0, 0)])},
    ]
    report = {'schema_version': 1, 'status': 'passed',
              'validated_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'oracle': 'SymPy '+sp.__version__+' exact linsolve; original-equation membership; all finite maps',
              'source_sha256': {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
                  for p in ['tools/rational_affine.py', 'tools/validate_rational_affine.py',
                            'tools/linear_equation_solvers.py']},
              'counts': counts, 'examples': examples,
              'limits': 'Finite exact checks, not universal proofs. Concrete finite graphs only; no inference from a sample to an infinite graph.'}
    path = ROOT/'research/production/rational_affine_validation.json'
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2, default=str)+'\n')
    print(json.dumps(counts, indent=2))


if __name__ == '__main__':
    main()
