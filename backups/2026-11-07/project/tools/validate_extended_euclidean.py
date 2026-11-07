"""Finite independent arithmetic and witness checks, not general proofs."""
from pathlib import Path
import datetime
import hashlib
import json
from extended_euclidean import extended_gcd, linear_solution, reduced_record

ROOT = Path(__file__).resolve().parents[1]


def reference_divides(d, n):
    return n == 0 if d == 0 else n % d == 0


def reference_gcd(a, b):
    if a == 0 and b == 0:
        return 0
    return max(d for d in range(1, max(abs(a), abs(b)) + 1)
               if reference_divides(d, a) and reference_divides(d, b))


def main():
    counts = dict(gcd_pairs=0, invariant_rows=0, coefficient_shift_checks=0,
                  linear_equations=0, reduced_records=0, equivalent_record_pairs=0,
                  coprime_cancellation_cases=0, coprime_product_cases=0,
                  invalid_rejections=0)
    for a in range(-30, 31):
        for b in range(-30, 31):
            result = extended_gcd(a, b)
            g, x, y = (result[k] for k in ('g', 'x', 'y'))
            assert g == reference_gcd(a, b) and a * x + b * y == g
            u, v = abs(a), abs(b)
            cx, cy = (1 if a >= 0 else -1), 0
            cX, cY = 0, (1 if b >= 0 else -1)
            assert len(result['trace']) <= abs(b)
            for row in result['trace']:
                assert (row['u'], row['v'], row['x'], row['y'], row['X'], row['Y']) == (u, v, cx, cy, cX, cY)
                assert u == a * cx + b * cy and v == a * cX + b * cY
                q, r = row['q'], row['r']
                assert v > 0 and u == v * q + r and 0 <= r < v
                nx, ny = row['next_x'], row['next_y']
                assert (nx, ny) == (cx - q * cX, cy - q * cY)
                assert a * nx + b * ny == r
                u, v, cx, cy, cX, cY = v, r, cX, cY, nx, ny
                counts['invariant_rows'] += 1
            assert (u, v, cx, cy) == (g, 0, x, y)
            for t in (-2, -1, 0, 1, 2):
                assert a * (x + t * b) + b * (y - t * a) == g
                counts['coefficient_shift_checks'] += 1
            counts['gcd_pairs'] += 1
    for a in range(-8, 9):
        for b in range(-8, 9):
            g = reference_gcd(a, b)
            for c in range(-12, 13):
                solution = linear_solution(a, b, c)
                # Independently find bounded witnesses; the small domain is
                # checked here, no bounded search is used as a general proof.
                witnesses = [(x, y) for x in range(-12, 13) for y in range(-12, 13)
                             if a * x + b * y == c]
                assert (solution is not None) == bool(witnesses)
                assert (solution is not None) == reference_divides(g, c)
                if solution is not None:
                    assert a * solution[0] + b * solution[1] == c
                counts['linear_equations'] += 1
    records = [(a, b) for a in range(-12, 13) for b in range(1, 13)]
    normalized = {}
    for a, b in records:
        p, q = reduced_record(a, b)
        g = reference_gcd(a, b)
        assert (p, q) == (a // g, b // g)
        assert a * q == b * p and q > 0 and reference_gcd(p, q) == 1
        if a == 0:
            assert (p, q) == (0, 1)
        normalized[(a, b)] = (p, q)
        counts['reduced_records'] += 1
    for a, b in records:
        for c, d in records:
            if a * d == b * c:
                assert normalized[(a, b)] == normalized[(c, d)]
                counts['equivalent_record_pairs'] += 1
    for a in range(-8, 9):
        for b in range(-8, 9):
            for c in range(-8, 9):
                if reference_gcd(a, b) == 1 and reference_divides(a, b * c):
                    assert reference_divides(a, c)
                    counts['coprime_cancellation_cases'] += 1
                assert (reference_gcd(a, b * c) == 1) == (reference_gcd(a, b) == 1 and reference_gcd(a, c) == 1)
                counts['coprime_product_cases'] += 1
    bad = [True, False, 0.0, 2.5, '3', None, [], (1,)]
    for fn, arity in [(extended_gcd, 2), (linear_solution, 3), (reduced_record, 2)]:
        for value in bad:
            for position in range(arity):
                args = [1] * arity
                args[position] = value
                try:
                    fn(*args)
                except ValueError:
                    counts['invalid_rejections'] += 1
                else:
                    raise AssertionError((fn.__name__, args))
    for b in (-3, 0):
        try:
            reduced_record(1, b)
        except ValueError:
            counts['invalid_rejections'] += 1
        else:
            raise AssertionError('nonpositive record denominator accepted')
    examples = []
    for a, b, expected in [(48, 18, (6, -1, 3)), (-48, 18, (6, 1, 3)),
                           (0, -7, (7, 0, -1)), (-7, 0, (7, -1, 0)),
                           (0, 0, (0, 1, 0)), (6, 10, (2, 2, -1)),
                           (84, 30, (6, -1, 3)), (-84, 30, (6, 1, 3)),
                           (30, 18, (6, -1, 2))]:
        result = extended_gcd(a, b)
        assert tuple(result[k] for k in ('g', 'x', 'y')) == expected
        examples.append(dict(operation='extended_gcd', inputs=[a, b], result=result))
    for a, b, c, expected in [(6, 10, 14, (14, -7)), (6, 10, 7, None),
                              (0, 0, 0, (0, 0)), (0, 0, 1, None),
                              (48, 18, 30, (-5, 15)), (48, 18, 31, None),
                              (30, 18, 42, (-7, 14)), (30, 18, 41, None)]:
        result = linear_solution(a, b, c)
        assert result == expected
        examples.append(dict(operation='linear_solution', inputs=[a, b, c], result=result))
    for a, b, expected in [(-12, 18, (-2, 3)), (0, 9, (0, 1)), (14, 21, (2, 3)),
                            (-42, 30, (-7, 5)), (-14, 10, (-7, 5)), (12, 18, (2, 3)),
                            (0, 7, (0, 1))]:
        result = reduced_record(a, b)
        assert result == expected
        examples.append(dict(operation='reduced_record', inputs=[a, b], result=result))
    sources = ['tools/extended_euclidean.py', 'tools/validate_extended_euclidean.py',
               'tools/integer_euclidean.py', 'tools/natural_algorithms.py']
    report = dict(status='passed', validated_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  source_sha256={p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sources},
                  scope=dict(gcd_inputs=[-30, 30], equation_ab=[-8, 8], equation_c=[-12, 12],
                             equation_witness_box=[-12, 12], record_a=[-12, 12], record_b=[1, 12],
                             coprime_abc=[-8, 8], sign_of_zero=1),
                  counts=counts, examples=examples,
                  independent_models='Exhaustive positive-factor gcd; bounded integer-equation witness search; exact cross products and positive-factor gcd for primitive records.',
                  limits='Finite implementation and theorem-instance checks only; not an infinite existence proof, formal verification, coefficient uniqueness claim or performance guarantee.')
    (ROOT/'research/production/extended_euclidean_validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'status': report['status'], 'counts': counts, 'examples': len(examples)}, indent=2))


if __name__ == '__main__':
    main()
