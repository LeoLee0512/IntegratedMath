"""Finite exact cross-checks; mathematical induction remains in the manuscript."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import datetime
import hashlib
import json
from rational_powers_sums import power, partial_sums, finite_sum, segment_sum

ROOT = Path(__file__).resolve().parents[1]


def reject(fn, *args):
    try:
        fn(*args)
    except ValueError:
        return
    raise AssertionError(('invalid input accepted', fn.__name__, args))


def main():
    values = [F(-2), F(-1, 2), F(0), F(1, 3), F(2)]
    counts = dict(powers=0, exponent_addition=0, power_iteration=0,
                  product_power=0, records=0, prefix_values=0, segments=0,
                  splits=0, padded_records=0, scaled_records=0,
                  pointwise_sums=0, rejected_inputs=0, input_immutability=0)
    for a, n in product(values, range(10)):
        actual = power(a, n)
        assert type(actual) is F and actual == a**n
        counts['powers'] += 1
    for a, m, n in product(values, range(7), range(7)):
        assert power(a, m+n) == power(a, m)*power(a, n)
        counts['exponent_addition'] += 1
        assert power(power(a, m), n) == a**(m*n)
        counts['power_iteration'] += 1
    for a, b, n in product(values, values, range(7)):
        assert power(a*b, n) == a**n*b**n
        counts['product_power'] += 1
    for length in range(5):
        for items in product(values, repeat=length):
            mutable = list(items)
            prefixes = partial_sums(mutable)
            assert mutable == list(items)
            assert type(prefixes) is tuple and len(prefixes) == length+1
            assert all(type(q) is F for q in prefixes)
            for n, actual in enumerate(prefixes):
                assert actual == sum(items[:n], F(0))
                counts['prefix_values'] += 1
            assert finite_sum(mutable) == sum(items, F(0))
            assert mutable == list(items)
            counts['input_immutability'] += 1
            counts['records'] += 1
            for start in range(length+1):
                for count in range(length-start+1):
                    actual = segment_sum(mutable, start, count)
                    assert type(actual) is F
                    assert actual == sum(items[start:start+count], F(0))
                    counts['segments'] += 1
            for k in range(length+1):
                assert segment_sum(items, 0, k)+segment_sum(items, k, length-k) == sum(items, F(0))
                counts['splits'] += 1
            for count in range(4):
                assert finite_sum(items+(F(0),)*count) == sum(items, F(0))
                counts['padded_records'] += 1
            for c in values:
                assert finite_sum(tuple(c*t for t in items)) == c*sum(items, F(0))
                counts['scaled_records'] += 1
    # Same-length pairs are enumerated independently up to length three.
    for length in range(4):
        for flat in product(values, repeat=2*length):
            left, right = flat[:length], flat[length:]
            actual = finite_sum(tuple(a+b for a, b in zip(left, right)))
            assert actual == sum(left, F(0))+sum(right, F(0))
            counts['pointwise_sums'] += 1
    for base in [None, True, False, 0.5, '2', (1, 2)]:
        reject(power, base, 0); counts['rejected_inputs'] += 1
    for exponent in [-1, True, False, F(1), 1.0, '1', None]:
        reject(power, 0, exponent); counts['rejected_inputs'] += 1
    for bad in [None, True, False, 0.5, '1', (1, 2)]:
        for fn in [partial_sums, finite_sum]:
            reject(fn, [0, bad]); counts['rejected_inputs'] += 1
        # Bad term outside the selected empty segment still must be rejected.
        reject(segment_sum, [0, bad], 0, 0); counts['rejected_inputs'] += 1
    for container in [None, {1, 2}, frozenset(), '12', 1, True]:
        for fn in [partial_sums, finite_sum]:
            reject(fn, container); counts['rejected_inputs'] += 1
        reject(segment_sum, container, 0, 0); counts['rejected_inputs'] += 1
    for index in [-1, True, False, F(0), 0.0, '0', None]:
        reject(segment_sum, [1], index, 0); counts['rejected_inputs'] += 1
        reject(segment_sum, [1], 0, index); counts['rejected_inputs'] += 1
    for items, start, count in [([], 1, 0), ([], 0, 1), ([1], 2, 0),
                                ([1], 1, 1), ([1, 2], 0, 3)]:
        reject(segment_sum, items, start, count); counts['rejected_inputs'] += 1
    examples = [
        {'case': 'zero base zero exponent', 'result': power(0, 0)},
        {'case': 'negative fractional cube', 'result': power(F(-2, 3), 3)},
        {'case': 'empty record prefixes', 'result': partial_sums([])},
        {'case': 'four terms', 'result': partial_sums([F(1, 2), -1, F(3, 2), 2])},
        {'case': 'shifted last three terms', 'result': segment_sum([1, -2, 3, -4, 5], 2, 3)},
        {'case': 'empty segment at end', 'result': segment_sum([1, -1], 2, 0)},
    ]
    expected = [F(1), F(-8, 27), (F(0),),
                (F(0), F(1, 2), F(-1, 2), F(1), F(3)), F(4), F(0)]
    assert [x['result'] for x in examples] == expected
    report = {'schema_version': 1, 'status': 'passed',
              'validated_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'oracle': 'Python Fraction integer powers and standard exact sum of independently sliced records',
              'scope': {'rational_values': [str(x) for x in values],
                        'power_exponents': [0, 9], 'law_exponents': [0, 6],
                        'record_lengths': [0, 4], 'pointwise_pair_lengths': [0, 3],
                        'padding_lengths': [0, 3]},
              'source_sha256': {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
                  for p in ['tools/rational_powers_sums.py', 'tools/validate_rational_powers_sums.py',
                            'tools/linear_equation_solvers.py']},
              'counts': counts, 'examples': examples,
              'limits': 'Finite exact implementation checks, not proofs of universal exponent or sum laws. No negative exponent, infinite sum or arbitrary sequence callback.'}
    path = ROOT/'research/production/rational_powers_sums_validation.json'
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2, default=str)+'\n')
    print(json.dumps(counts, indent=2))


if __name__ == '__main__':
    main()
