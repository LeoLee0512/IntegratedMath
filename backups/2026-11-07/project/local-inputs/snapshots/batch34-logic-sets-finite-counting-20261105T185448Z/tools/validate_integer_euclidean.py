"""Finite independent checks, not general mathematical proofs."""
from pathlib import Path
import datetime
import hashlib
import json
from integer_euclidean import divide_integer, divides, gcd_trace, gcd_integer

ROOT = Path(__file__).resolve().parents[1]


def reference_divides(d, n):
    return n == 0 if d == 0 else n % d == 0


def reference_gcd(a, b):
    # Independent finite search, not Euclidean iteration.
    if a == 0 and b == 0:
        return 0
    return max(d for d in range(1, max(abs(a), abs(b)) + 1)
               if reference_divides(d, a) and reference_divides(d, b))


def main():
    count = dict(division_pairs=0, divisibility_pairs=0, gcd_pairs=0,
                 trace_rows=0, common_divisor_checks=0, invalid_rejections=0)
    for a in range(-36, 37):
        for b in range(-12, 13):
            if b == 0:
                continue
            q, r = divide_integer(a, b)
            expected_r = a % abs(b)
            expected_q = (a - expected_r) // b
            assert (q, r) == (expected_q, expected_r)
            assert a == b * q + r and 0 <= r < abs(b)
            count['division_pairs'] += 1
    for a in range(-36, 37):
        for b in range(-36, 37):
            assert divides(a, b) == reference_divides(a, b)
            count['divisibility_pairs'] += 1
            g, rows = gcd_trace(a, b)
            assert g == reference_gcd(a, b) and g >= 0
            assert gcd_integer(a, b) == g
            assert len(rows) <= abs(b)
            u, v = abs(a), abs(b)
            for row in rows:
                assert (row['u'], row['v']) == (u, v)
                q, r = row['q'], row['r']
                assert v > 0 and u == v * q + r and 0 <= r < v
                for d in range(-36, 37):
                    old = reference_divides(d, u) and reference_divides(d, v)
                    new = reference_divides(d, v) and reference_divides(d, r)
                    assert old == new
                    count['common_divisor_checks'] += 1
                u, v = v, r
                count['trace_rows'] += 1
            assert (u, v) == (g, 0)
            for d in range(-36, 37):
                assert (reference_divides(d, a) and reference_divides(d, b)) == reference_divides(d, g)
                count['common_divisor_checks'] += 1
            count['gcd_pairs'] += 1
    bad = [True, False, 0.0, 2.5, '3', None, [], (1,)]
    for function in (divide_integer, divides, gcd_trace, gcd_integer):
        for value in bad:
            for args in ((value, 1), (1, value)):
                try:
                    function(*args)
                except ValueError:
                    count['invalid_rejections'] += 1
                else:
                    raise AssertionError((function.__name__, args))
    for a in (-7, 0, 7):
        try:
            divide_integer(a, 0)
        except ValueError:
            count['invalid_rejections'] += 1
        else:
            raise AssertionError('zero divisor accepted')
    examples = []
    for a, b, expected in [(-23, 5, (-5, 2)), (-23, -5, (5, 2)),
                           (-20, 5, (-4, 0)), (0, -7, (0, 0))]:
        actual = divide_integer(a, b)
        assert actual == expected
        examples.append(dict(operation='division', inputs=[a, b], result=list(actual)))
    for d, n, expected in [(0, 0, True), (0, 7, False), (-3, 6, True), (4, 6, False)]:
        actual = divides(d, n)
        assert actual is expected
        examples.append(dict(operation='divides', inputs=[d, n], result=actual))
    for a, b, expected in [(48, 18, 6), (-48, 18, 6), (0, -7, 7),
                           (-7, 0, 7), (0, 0, 0), (84, 30, 6),
                           (-84, -30, 6), (14, 25, 1), (18, 30, 6)]:
        actual, rows = gcd_trace(a, b)
        assert actual == expected
        examples.append(dict(operation='gcd', inputs=[a, b], result=actual, trace=rows))
    sources = ['tools/integer_euclidean.py', 'tools/validate_integer_euclidean.py',
               'tools/natural_algorithms.py']
    report = dict(status='passed', verified_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  source_sha256={p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sources},
                  scope=dict(integer_inputs=[-36, 36], division_divisors=[-12, 12],
                             division_excludes_zero=True, common_divisor_probes=[-36, 36],
                             gcd_double_zero=0, remainder_convention='0 <= r < abs(b)'),
                  counts=count, examples=examples,
                  independent_models='Division uses Python remainder with abs(b) and exact quotient; gcd uses exhaustive positive-factor search; divisibility uses Python modulo with explicit zero handling.',
                  limits='Finite implementation and example checks; not proof for arbitrary integers, formal verification or a complexity guarantee.')
    target = ROOT/'research/production/integer_euclidean_validation.json'
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'status': report['status'], 'counts': count, 'examples': len(examples)}, indent=2))


if __name__ == '__main__':
    main()
