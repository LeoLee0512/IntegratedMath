"""Finite checks against Fraction and exact cross products, not general proofs."""
from pathlib import Path
from fractions import Fraction
from itertools import product
import datetime
import hashlib
import json
from rational_addition import checked_pair, equivalent, normalize, embed, add, negate, subtract

ROOT = Path(__file__).resolve().parents[1]


def pair(value):
    return value.numerator, value.denominator


def main():
    records = [(a, b) for a in range(-6, 7) for b in range(1, 6)]
    small = [(a, b) for a in range(-2, 3) for b in range(1, 4)]
    counts = dict(records=0, record_pairs=0, representative_changes=0,
                  association_triples=0, equivalence_transitivity_triples=0,
                  embedding_pairs=0, invalid_rejections=0)
    for r in records:
        f = Fraction(*r)
        assert normalize(r) == pair(f)
        assert equivalent(r, r) and equivalent(r, normalize(r))
        assert normalize(normalize(r)) == normalize(r)
        assert (normalize(r) == (0, 1)) == (r[0] == 0)
        assert negate(r) == pair(-f)
        assert negate(negate(r)) == normalize(r)
        assert add(r, (0, 1)) == normalize(r)
        assert add(r, negate(r)) == (0, 1)
        counts['records'] += 1
    for r, s in product(records, repeat=2):
        f, g = Fraction(*r), Fraction(*s)
        assert equivalent(r, s) == equivalent(s, r) == (f == g)
        assert equivalent(r, s) == (normalize(r) == normalize(s))
        assert add(r, s) == pair(f + g) == add(s, r)
        assert subtract(r, s) == pair(f - g)
        assert add(subtract(s, r), r) == normalize(s)
        for k, l in [(2, 3), (3, 2)]:
            rr, ss = (k*r[0], k*r[1]), (l*s[0], l*s[1])
            assert equivalent(r, rr) and equivalent(s, ss)
            assert add(rr, ss) == add(r, s)
            assert negate(rr) == negate(r)
            counts['representative_changes'] += 1
        counts['record_pairs'] += 1
    for r, s, t in product(small, repeat=3):
        assert add(add(r, s), t) == add(r, add(s, t))
        if equivalent(r, s) and equivalent(s, t):
            assert equivalent(r, t)
            counts['equivalence_transitivity_triples'] += 1
        counts['association_triples'] += 1
    for m, n in product(range(-8, 9), repeat=2):
        assert add(embed(m), embed(n)) == embed(m+n)
        assert equivalent(embed(m), embed(n)) == (m == n)
        counts['embedding_pairs'] += 1
    invalid = [None, (), (1,), (1, 2, 3), '12', (True, 1), (1, False),
               (1.0, 2), (1, 2.0), ('1', 2), (1, 0), (1, -2)]
    for record in invalid:
        for fn, args in ([(fn, (record,)) for fn in [checked_pair, normalize, negate]]
                         + [(fn, (record, (1, 2))) for fn in [equivalent, add, subtract]]
                         + [(fn, ((1, 2), record)) for fn in [equivalent, add, subtract]]):
            try:
                fn(*args)
            except ValueError:
                counts['invalid_rejections'] += 1
            else:
                raise AssertionError((fn.__name__, args))
    for n in [True, False, 1.0, '1', None]:
        try:
            embed(n)
        except ValueError:
            counts['invalid_rejections'] += 1
        else:
            raise AssertionError(n)
    cases = [('normalize', [(-42, 30)], (-7, 5)),
             ('normalize', [(0, 9)], (0, 1)),
             ('equivalent', [(1, 2), (2, 4)], True),
             ('equivalent', [(1, 2), (1, 3)], False),
             ('embed', [-3], (-3, 1)),
             ('add', [(1, 2), (1, 3)], (5, 6)),
             ('add', [(-2, 3), (1, 6)], (-1, 2)),
             ('add', [(2, 4), (2, 6)], (5, 6)),
             ('add', [(-2, 3), (4, 6)], (0, 1)),
             ('negate', [(-2, 6)], (1, 3)),
             ('subtract', [(1, 3), (5, 6)], (-1, 2)),
             ('normalize', [(-18, 30)], (-3, 5)),
             ('normalize', [(8, 12)], (2, 3)),
             ('normalize', [(14, 21)], (2, 3)),
             ('normalize', [(0, 11)], (0, 1)),
             ('normalize', [(-6, 15)], (-2, 5)),
             ('normalize', [(6, 15)], (2, 5)),
             ('normalize', [(0, 15)], (0, 1)),
             ('equivalent', [(8, 12), (14, 21)], True),
             ('add', [(-5, 8), (3, 8)], (-1, 4)),
             ('add', [(1, 2), (-1, 3)], (1, 6)),
             ('add', [(1, 6), (1, 6)], (1, 3)),
             ('add', [(-1, 3), (1, 6)], (-1, 6)),
             ('add', [(1, 2), (-3, 18)], (1, 3)),
             ('negate', [(-3, 7)], (3, 7)),
             ('add', [(-3, 7), (3, 7)], (0, 1)),
             ('add', [(-2, 1), (1, 3)], (-5, 3)),
             ('subtract', [(1, 3), (-2, 5)], (11, 15)),
             ('add', [(11, 15), (-2, 5)], (1, 3)),
             ('add', [(3, 6), (-4, 6)], (-1, 6))]
    functions = {fn.__name__: fn for fn in [normalize, equivalent, embed, add, negate, subtract]}
    examples = []
    for operation, inputs, expected in cases:
        result = functions[operation](*inputs)
        assert result == expected
        examples.append(dict(operation=operation, inputs=inputs, result=result))
    sources = ['tools/rational_addition.py', 'tools/validate_rational_addition.py',
               'tools/extended_euclidean.py', 'tools/integer_euclidean.py', 'tools/natural_algorithms.py']
    report = dict(status='passed', validated_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  source_sha256={p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sources},
                  scope=dict(record_a=[-6, 6], record_b=[1, 5], triple_a=[-2, 2],
                             triple_b=[1, 3], embedding=[-8, 8], scaling_pairs=[[2, 3], [3, 2]]),
                  counts=counts, examples=examples,
                  independent_model='Python standard-library Fraction, exact cross products; no floating point.',
                  limits='Finite checks of normalization, equivalence and additive operations; not infinite quotient construction or proofs. Fraction is only an external validation oracle, not a prerequisite in the textbook or implementation.')
    (ROOT/'research/production/rational_addition_validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(dict(status='passed', counts=counts, examples=len(examples)), indent=2))


if __name__ == '__main__':
    main()
