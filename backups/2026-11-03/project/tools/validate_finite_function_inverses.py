"""Independent bounded truth-table oracle; finite support, not general proofs."""
from pathlib import Path
from itertools import product, combinations
import datetime
import hashlib
import json
from finite_functions import FiniteFunction, compose, identity
from finite_function_inverses import injective, surjective, bijective, inverse, preimage

ROOT = Path(__file__).resolve().parents[1]


def subsets(a):
    return [frozenset(c) for n in range(len(a)+1) for c in combinations(sorted(a), n)]


def rejects(fn, *args):
    try:
        fn(*args)
    except ValueError:
        return
    raise AssertionError('expected ValueError')


def main():
    sets = subsets({0, 1})
    models = []
    for a, b in product(sets, repeat=2):
        for values in product(sorted(b), repeat=len(a)):
            table = dict(zip(sorted(a), values))
            f = FiniteFunction(a, b, list(table.items()))
            # Oracle states the quantified definitions, not the production algorithms.
            inj = all(table[x] != table[y] or x == y for x in a for y in a)
            sur = all(any(table[x] == y for x in a) for y in b)
            models.append((f, table, inj, sur))
    counts = dict(functions=len(models), property_checks=0, inverse_functions=0,
                  inverse_rejections=0, preimages=0, compositions=0,
                  inverse_compositions=0, opposite_type_pairs=0,
                  two_sided_inverses=0, one_sided_implications=0,
                  invalid_rejections=0)
    for f, table, inj, sur in models:
        assert (injective(f), surjective(f), bijective(f)) == (inj, sur, inj and sur)
        counts['property_checks'] += 3
        if inj and sur:
            inv = inverse(f)
            expected = {y: next(x for x in f.domain if table[x] == y) for y in f.codomain}
            assert inv.domain == f.codomain and inv.codomain == f.domain
            assert dict(inv.graph) == expected
            assert inverse(inv) == f
            assert compose(inv, f) == identity(f.domain)
            assert compose(f, inv) == identity(f.codomain)
            counts['inverse_functions'] += 1
        else:
            rejects(inverse, f)
            counts['inverse_rejections'] += 1
        for t in subsets(f.codomain):
            expected = frozenset(x for x in f.domain if table[x] in t)
            assert preimage(f, t) == expected
            counts['preimages'] += 1
    for f, ft, fi, fs in models:
        for g, gt, gi, gs in models:
            if f.codomain == g.domain:
                c = compose(g, f)
                ci = all(gt[ft[x]] != gt[ft[y]] or x == y for x in f.domain for y in f.domain)
                cs = all(any(gt[ft[x]] == z for x in f.domain) for z in g.codomain)
                assert (injective(c), surjective(c)) == (ci, cs)
                assert not (fi and gi) or ci
                assert not (fs and gs) or cs
                assert not ci or fi
                assert not cs or gs
                counts['compositions'] += 1
                if fi and fs and gi and gs:
                    assert inverse(c) == compose(inverse(f), inverse(g))
                    counts['inverse_compositions'] += 1
            if f.domain == g.codomain and f.codomain == g.domain:
                # Compute pointwise without using compose to decide the oracle.
                left = all(gt[ft[x]] == x for x in f.domain)
                right = all(ft[gt[y]] == y for y in f.codomain)
                assert (compose(g, f) == identity(f.domain)) == left
                assert (compose(f, g) == identity(f.codomain)) == right
                assert not left or fi
                assert not right or fs
                counts['opposite_type_pairs'] += 1
                counts['one_sided_implications'] += 2
                if left and right:
                    assert fi and fs and g == inverse(f)
                    counts['two_sided_inverses'] += 1
    for api in [injective, surjective, bijective, inverse]:
        for bad in [None, {}, 1, True]:
            rejects(api, bad); counts['invalid_rejections'] += 1
    f = FiniteFunction({0}, {0}, {(0, 0)})
    for bad in [None, {True}, {0.0}, {1}, '0']:
        rejects(preimage, f, bad); counts['invalid_rejections'] += 1
    rejects(preimage, None, set()); counts['invalid_rejections'] += 1

    examples = []
    empty = FiniteFunction(set(), set(), set())
    assert inverse(empty) == empty and bijective(empty)
    examples.append('empty-to-empty bijection is its own inverse')
    expanded = FiniteFunction(set(), {0}, set())
    assert injective(expanded) and not surjective(expanded)
    rejects(inverse, expanded)
    examples.append('empty domain with nonempty codomain is not surjective')
    expanded = FiniteFunction({0}, {0, 1}, {(0, 0)})
    assert injective(expanded) and not surjective(expanded)
    assert bijective(FiniteFunction({0}, {0}, {(0, 0)}))
    examples.append('same graph and different codomain change surjectivity')
    constant = FiniteFunction({-1, 1}, {1}, {(-1, 1), (1, 1)})
    assert not injective(constant) and surjective(constant)
    assert preimage(constant, {1}) == frozenset({-1, 1})
    rejects(inverse, constant)
    examples.append('preimage exists for a noninvertible constant function')
    affine = FiniteFunction({0, 1, 2}, {1, 3, 5}, {(0, 1), (1, 3), (2, 5)})
    assert inverse(affine)(1) == 0 and inverse(affine)(3) == 1
    assert inverse(affine)(5) == 2
    examples.append('finite affine table inverse reverses all three arrows')
    zero_output = FiniteFunction({1}, {0}, {(1, 0)})
    assert inverse(zero_output)(0) == 1
    examples.append('zero output does not prevent a function inverse; reciprocal differs')
    paths = ['tools/finite_functions.py', 'tools/finite_function_inverses.py',
             'tools/validate_finite_function_inverses.py']
    report = dict(status='passed', checked_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  domain='All total functions between all subsets of {0,1}; finite integer labels only',
                  counts=counts, explicit_examples=examples,
                  source_sha256={p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
                  limits='Finite oracle tests support implementation only. No general proof, real-number model, or choice principle is inferred.')
    out = ROOT/'research/production/finite_function_inverses_validation.json'
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(counts, indent=2))


if __name__ == '__main__':
    main()
