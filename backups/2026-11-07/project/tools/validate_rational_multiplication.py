"""Independent finite checks supporting the rational multiplication manuscript."""
from pathlib import Path
from fractions import Fraction
from itertools import product
import datetime
import hashlib
import json
from rational_addition import equivalent, normalize, embed, add, negate
from rational_multiplication import multiply, reciprocal, divide

ROOT = Path(__file__).resolve().parents[1]


def pair(value):
    return value.numerator, value.denominator


def rejects(fn, *args):
    try:
        fn(*args)
    except ValueError:
        return
    raise AssertionError((fn.__name__, args))


def main():
    records = [(a, b) for a in range(-6, 7) for b in range(1, 6)]
    small = [(a, b) for a in range(-2, 3) for b in range(1, 4)]
    counts = dict(records=0, reciprocals=0, zero_reciprocal_rejections=0,
                  product_pairs=0, division_pairs=0, zero_division_rejections=0,
                  representative_changes=0, association_triples=0,
                  distributivity_triples=0, cancellation_triples=0,
                  integer_embedding_pairs=0, invalid_input_rejections=0)
    for r in records:
        f = Fraction(*r)
        assert multiply(r, (1, 1)) == normalize(r)
        assert multiply(r, (0, 1)) == (0, 1)
        if r[0] == 0:
            rejects(reciprocal, r)
            counts['zero_reciprocal_rejections'] += 1
        else:
            inv = reciprocal(r)
            assert inv == pair(1 / f)
            assert multiply(r, inv) == multiply(inv, r) == (1, 1)
            assert reciprocal(inv) == normalize(r)
            assert reciprocal((3*r[0], 3*r[1])) == inv
            counts['reciprocals'] += 1
        counts['records'] += 1
    for r, s in product(records, repeat=2):
        f, g = Fraction(*r), Fraction(*s)
        result = multiply(r, s)
        assert result == pair(f*g) == multiply(s, r)
        assert (result == (0, 1)) == (r[0] == 0 or s[0] == 0)
        assert multiply(negate(r), s) == negate(result)
        assert multiply(negate(r), negate(s)) == result
        for k, l in [(2, 3), (3, 2)]:
            rr, ss = (k*r[0], k*r[1]), (l*s[0], l*s[1])
            assert multiply(rr, ss) == result
            if s[0] != 0:
                assert divide(rr, ss) == divide(r, s)
            counts['representative_changes'] += 1
        if s[0] == 0:
            rejects(divide, r, s)
            counts['zero_division_rejections'] += 1
        else:
            q = divide(r, s)
            assert q == pair(f/g)
            assert multiply(q, s) == normalize(r)
            assert divide(multiply(r, s), s) == normalize(r)
            counts['division_pairs'] += 1
        counts['product_pairs'] += 1
    for r, s, t in product(small, repeat=3):
        assert multiply(multiply(r, s), t) == multiply(r, multiply(s, t))
        assert multiply(r, add(s, t)) == add(multiply(r, s), multiply(r, t))
        if t[0] != 0:
            assert (multiply(r, t) == multiply(s, t)) == equivalent(r, s)
            counts['cancellation_triples'] += 1
        counts['association_triples'] += 1
        counts['distributivity_triples'] += 1
    for m, n in product(range(-8, 9), repeat=2):
        assert multiply(embed(m), embed(n)) == embed(m*n)
        if n != 0:
            expected_record = (m, n) if n > 0 else (-m, -n)
            assert divide(embed(m), embed(n)) == normalize(expected_record)
        counts['integer_embedding_pairs'] += 1
    invalid = [None, (), (1,), (1, 2, 3), '12', (True, 1), (1, False),
               (1.0, 2), (1, 2.0), ('1', 2), (1, 0), (1, -2)]
    for r in invalid:
        rejects(reciprocal, r)
        counts['invalid_input_rejections'] += 1
        for fn in [multiply, divide]:
            rejects(fn, r, (1, 2))
            rejects(fn, (1, 2), r)
            counts['invalid_input_rejections'] += 2
    cases = [('multiply', [(-2, 3), (9, 4)], (-3, 2)),
             ('multiply', [(-2, 3), (-9, 4)], (3, 2)),
             ('multiply', [(0, 7), (3, 5)], (0, 1)),
             ('reciprocal', [(-6, 8)], (-4, 3)),
             ('reciprocal', [(6, 8)], (4, 3)),
             ('divide', [(2, 3), (-4, 5)], (-5, 6)),
             ('divide', [(0, 7), (3, 5)], (0, 1)),
             ('divide', [(-3, 1), (-6, 1)], (1, 2)),
             ('multiply', [(-2, 3), (3, 5)], (-2, 5)),
             ('multiply', [(0, 7), (-3, 2)], (0, 1)),
             ('multiply', [(2, 4), (-6, 10)], (-3, 10)),
             ('multiply', [(-6, 15), (5, 7)], (-2, 7)),
             ('multiply', [(2, 3), (-15, 35)], (-2, 7)),
             ('multiply', [(-2, 3), (10, 8)], (-5, 6)),
             ('multiply', [(-3, 1), (2, 5)], (-6, 5)),
             ('multiply', [(1, 2), (9, 18)], (1, 4)),
             ('reciprocal', [(-4, 6)], (-3, 2)),
             ('reciprocal', [(-6, 15)], (-5, 2)),
             ('divide', [(-5, 6), (-2, 9)], (15, 4)),
             ('multiply', [(-2, 9), (15, 4)], (-5, 6)),
             ('divide', [(6, 5), (-3, 7)], (-14, 5)),
             ('multiply', [(-3, 7), (-14, 5)], (6, 5)),
             ('divide', [(3, 5), (-4, 7)], (-21, 20)),
             ('divide', [(-6, 15), (8, 21)], (-21, 20)),
             ('divide', [(-6, 1), (-15, 1)], (2, 5)),
             ('divide', [(6, 1), (-15, 1)], (-2, 5)),
             ('divide', [(1, 2), (5, 6)], (3, 5)),
             ('divide', [(1, 3), (5, 6)], (2, 5)),
             ('divide', [(5, 6), (5, 6)], (1, 1)),
             ('divide', [(1, 2), (3, 1)], (1, 6)),
             ('divide', [(1, 1), (2, 3)], (3, 2))]
    functions = {fn.__name__: fn for fn in [multiply, reciprocal, divide]}
    examples = []
    for operation, inputs, expected in cases:
        result = functions[operation](*inputs)
        assert result == expected
        fs = [Fraction(*r) for r in inputs]
        oracle = (fs[0]*fs[1] if operation == 'multiply' else
                  1/fs[0] if operation == 'reciprocal' else fs[0]/fs[1])
        assert result == pair(oracle)
        examples.append(dict(operation=operation, inputs=inputs, result=result))
    sources = ['tools/rational_multiplication.py', 'tools/validate_rational_multiplication.py',
               'tools/rational_addition.py', 'tools/extended_euclidean.py',
               'tools/integer_euclidean.py', 'tools/natural_algorithms.py']
    report = dict(status='passed', validated_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  source_sha256={p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sources},
                  scope=dict(record_a=[-6, 6], record_b=[1, 5], triple_a=[-2, 2],
                             triple_b=[1, 3], embedding=[-8, 8], scaling_pairs=[[2, 3], [3, 2]]),
                  counts=counts, examples=examples,
                  independent_model='Python standard-library Fraction and exact integer cross products; no floating-point arithmetic.',
                  limits='Finite implementation and theorem-instance checks only, not general proofs or formal verification. Zero reciprocal/division are rejected, not assigned a conventional value.')
    (ROOT/'research/production/rational_multiplication_validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(dict(status='passed', counts=counts, examples=len(examples)), indent=2))


if __name__ == '__main__':
    main()
