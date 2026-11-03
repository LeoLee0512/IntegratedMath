"""Finite exact checks supporting B1.18/B1.19; not universal proofs."""
from pathlib import Path
from fractions import Fraction
from itertools import product
import datetime
import hashlib
import json
from rational_addition import normalize, equivalent, embed, add, negate, subtract
from rational_multiplication import multiply, reciprocal, divide
from rational_order import compare, leq, lt, absolute, distance

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
    zero = (0, 1)
    records = [(a, b) for a in range(-6, 7) for b in range(1, 6)]
    small = [(a, b) for a in range(-2, 3) for b in range(1, 4)]
    counts = dict(records=0, order_pairs=0, representative_changes=0,
                  absolute_product_pairs=0, absolute_quotient_pairs=0,
                  triangle_pairs=0, reverse_triangle_pairs=0,
                  order_triples=0, translation_triples=0,
                  multiplication_triples=0, division_triples=0,
                  distance_triples=0, distance_translation_triples=0, distance_scaling_triples=0,
                  integer_embedding_pairs=0,
                  invalid_input_rejections=0)
    for r in records:
        f = Fraction(*r)
        ar = absolute(r)
        assert ar == pair(abs(f))
        assert ar == absolute(negate(r)) == absolute(ar)
        assert leq(zero, ar) and ((ar == zero) == (r[0] == 0))
        assert leq(negate(ar), r) and leq(r, ar)
        assert compare(r, zero) == ((f > 0) - (f < 0))
        assert leq(r, r) and not lt(r, r)
        assert distance(r, r) == zero
        if r[0] != 0:
            assert compare(reciprocal(r), zero) == compare(r, zero)
        counts['records'] += 1
    for r, s in product(records, repeat=2):
        f, g = Fraction(*r), Fraction(*s)
        cmp = compare(r, s)
        assert cmp == ((f > g) - (f < g)) == -compare(s, r)
        assert leq(r, s) == (f <= g) and lt(r, s) == (f < g)
        assert (leq(r, s) and leq(s, r)) == equivalent(r, s)
        assert compare(negate(r), negate(s)) == -cmp
        for k, l in [(2, 3), (3, 2)]:
            rr, ss = (k*r[0], k*r[1]), (l*s[0], l*s[1])
            assert compare(rr, ss) == cmp
            assert absolute(rr) == absolute(r)
            assert distance(rr, ss) == distance(r, s)
            counts['representative_changes'] += 1
        dist = distance(r, s)
        assert dist == pair(abs(f-g)) == distance(s, r)
        assert leq(zero, dist) and ((dist == zero) == equivalent(r, s))
        assert absolute(multiply(r, s)) == multiply(absolute(r), absolute(s))
        counts['absolute_product_pairs'] += 1
        if s[0] != 0:
            assert absolute(divide(r, s)) == divide(absolute(r), absolute(s))
            counts['absolute_quotient_pairs'] += 1
        assert leq(absolute(add(r, s)), add(absolute(r), absolute(s)))
        assert leq(absolute(subtract(absolute(r), absolute(s))), dist)
        assert leq(absolute(r), s) == (leq(negate(s), r) and leq(r, s))
        counts['triangle_pairs'] += 1
        counts['reverse_triangle_pairs'] += 1
        counts['order_pairs'] += 1
    for r, s, t in product(small, repeat=3):
        if leq(r, s) and leq(s, t):
            assert leq(r, t)
        if lt(r, s) and leq(s, t):
            assert lt(r, t)
        if leq(r, s) and lt(s, t):
            assert lt(r, t)
        cmp = compare(r, s)
        assert compare(add(r, t), add(s, t)) == cmp
        sign = compare(t, zero)
        assert compare(multiply(r, t), multiply(s, t)) == cmp*sign
        if sign:
            assert compare(divide(r, t), divide(s, t)) == cmp*sign
            counts['division_triples'] += 1
        assert leq(distance(r, t), add(distance(r, s), distance(s, t)))
        assert distance(add(r, t), add(s, t)) == distance(r, s)
        assert distance(multiply(t, r), multiply(t, s)) == multiply(absolute(t), distance(r, s))
        counts['distance_translation_triples'] += 1
        counts['distance_scaling_triples'] += 1
        counts['order_triples'] += 1
        counts['translation_triples'] += 1
        counts['multiplication_triples'] += 1
        counts['distance_triples'] += 1
    for m, n in product(range(-8, 9), repeat=2):
        assert compare(embed(m), embed(n)) == ((m > n) - (m < n))
        assert absolute(embed(m)) == embed(abs(m))
        counts['integer_embedding_pairs'] += 1
    invalid = [None, (), (1,), (1, 2, 3), '12', (True, 1), (1, False),
               (1.0, 2), (1, 2.0), ('1', 2), (1, 0), (1, -2)]
    for r in invalid:
        rejects(absolute, r)
        counts['invalid_input_rejections'] += 1
        for fn in [compare, leq, lt, distance]:
            rejects(fn, r, (1, 2))
            rejects(fn, (1, 2), r)
            counts['invalid_input_rejections'] += 2
    cases = [('compare', [(-2, 3), (-3, 4)], 1),
             ('compare', [(1, 2), (2, 4)], 0),
             ('absolute', [(-6, 8)], (3, 4)),
             ('absolute', [(0, 7)], (0, 1)),
             ('distance', [(-3, 2), (-1, 2)], (1, 1)),
             ('distance', [(-1, 2), (3, 2)], (2, 1)),
             ('distance', [(-3, 2), (3, 2)], (3, 1)),
             ('absolute', [(7, 3)], (7, 3)),
             ('absolute', [(8, 27)], (8, 27)),
             ('absolute', [(5, 12)], (5, 12)),
             ('absolute', [(-11, 12)], (11, 12)),
             ('compare', [(1, 6), (5, 6)], -1),
             ('compare', [(5, 12), (11, 12)], -1),
             ('compare', [(7, 3), (0, 1)], 1),
             ('compare', [(-9, 4), (0, 1)], -1),
             ('compare', [(-5, 6), (5, 4)], -1),
             ('compare', [(2, 4), (6, 10)], -1),
             ('compare', [(-1, 3), (1, 2)], -1),
             ('compare', [(4, 5), (3, 2)], -1),
             ('compare', [(-5, 4), (5, 6)], -1),
             ('absolute', [(3, 2)], (3, 2)),
             ('distance', [(-2, 3), (1, 4)], (11, 12)),
             ('distance', [(1, 3), (2, 3)], (1, 3))]
    functions = {fn.__name__: fn for fn in [compare, absolute, distance]}
    examples = []
    for operation, inputs, expected in cases:
        result = functions[operation](*inputs)
        fs = [Fraction(*r) for r in inputs]
        oracle = (((fs[0] > fs[1]) - (fs[0] < fs[1])) if operation == 'compare' else
                  pair(abs(fs[0])) if operation == 'absolute' else pair(abs(fs[0]-fs[1])))
        assert result == expected == oracle
        examples.append(dict(operation=operation, inputs=inputs, result=result))
    sources = ['tools/rational_order.py', 'tools/validate_rational_order.py',
               'tools/rational_multiplication.py', 'tools/rational_addition.py',
               'tools/extended_euclidean.py', 'tools/integer_euclidean.py',
               'tools/natural_algorithms.py']
    report = dict(status='passed', validated_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  source_sha256={p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sources},
                  scope=dict(record_a=[-6, 6], record_b=[1, 5], triple_a=[-2, 2],
                             triple_b=[1, 3], embedding=[-8, 8], scaling_pairs=[[2, 3], [3, 2]]),
                  counts=counts, examples=examples,
                  independent_model='Python Fraction with exact integers, no floating-point arithmetic.',
                  limits='Finite representative/implementation checks, not universal proofs, real completeness, formal verification, or geometric construction of a real line.')
    (ROOT/'research/production/rational_order_validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(dict(status='passed', counts=counts, examples=len(examples)), indent=2))


if __name__ == '__main__':
    main()
