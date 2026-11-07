#!/usr/bin/env python3
"""Finite independent checks of the B1.7/B1.8 representative implementation.

Python signed integers supply a comparison model, never the manuscript proof.
Run from any working directory. No network requests or third-party data.
"""
from collections import defaultdict
from datetime import datetime, timezone
from hashlib import sha256
from itertools import product
import json
from pathlib import Path

from integer_pairs import (equivalent, embed, add, negate, subtract,
                           multiply, leq, canonical, checked_pair)

ROOT = Path(__file__).resolve().parents[1]


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def value(record):
    # Independent comparison model: deliberately uses Python signed subtraction.
    return record[0] - record[1]


def main():
    records = list(product(range(7), repeat=2))
    small = list(product(range(4), repeat=2))
    counts = dict(unary_records=0, binary_pairs=0, law_triples=0,
                  replacement_checks=0, invalid_input_rejected=0,
                  input_immutability=0, examples=0)
    groups = defaultdict(list)
    zero, one = embed(0), embed(1)
    for record in records:
        groups[value(record)].append(record)
        n = canonical(record)
        require(n == ((value(record), 0) if value(record) >= 0 else (0, -value(record))),
                ('canonical form', record))
        require(equivalent(n, record) and equivalent(record, record), ('reflexive', record))
        require(equivalent(add(record, negate(record)), zero), ('additive inverse', record))
        require(equivalent(multiply(record, one), record), ('multiplicative identity', record))
        require(equivalent(multiply(record, zero), zero), ('zero factor', record))
        counts['unary_records'] += 1
    for left, right in product(records, repeat=2):
        lv, rv = value(left), value(right)
        require(equivalent(left, right) == (lv == rv), ('equivalence model', left, right))
        require(equivalent(left, right) == equivalent(right, left), ('symmetry', left, right))
        require(leq(left, right) == (lv <= rv), ('order model', left, right))
        for operation, expected in [(add, lv + rv), (subtract, lv - rv), (multiply, lv * rv)]:
            a, b = list(left), list(right)
            before = a.copy(), b.copy()
            result = operation(a, b)
            require(value(result) == expected, ('operation model', operation.__name__, left, right))
            require((a, b) == before, 'input mutation')
            require(checked_pair(result) == result, 'result is not a natural pair')
            counts['input_immutability'] += 1
        counts['binary_pairs'] += 1
    for x, y, z in product(small, repeat=3):
        if equivalent(x, y) and equivalent(y, z):
            require(equivalent(x, z), 'equivalence transitivity')
        require(equivalent(add(add(x, y), z), add(x, add(y, z))), 'addition associativity')
        require(equivalent(multiply(multiply(x, y), z), multiply(x, multiply(y, z))),
                'multiplication associativity')
        require(equivalent(multiply(x, add(y, z)), add(multiply(x, y), multiply(x, z))),
                'distributivity')
        if leq(x, y):
            require(leq(add(x, z), add(y, z)), 'translation preserves order')
            if value(z) > 0:
                require(leq(multiply(x, z), multiply(y, z)), 'positive factor order')
            elif value(z) < 0:
                require(leq(multiply(y, z), multiply(x, z)), 'negative factor reverses order')
        counts['law_triples'] += 1
    # All representatives within each finite value-group, with either operand replaced.
    for group in groups.values():
        for original, replacement in product(group, repeat=2):
            require(equivalent(negate(original), negate(replacement)), 'negation representative')
            for other in records:
                for operation in [add, multiply]:
                    require(equivalent(operation(original, other), operation(replacement, other)),
                            'first representative choice')
                    require(equivalent(operation(other, original), operation(other, replacement)),
                            'second representative choice')
                require(leq(original, other) == leq(replacement, other), 'first order representative')
                require(leq(other, original) == leq(other, replacement), 'second order representative')
                counts['replacement_checks'] += 1
    invalid = [(), (1,), (1, 2, 3), (True, 0), (-1, 0), (0, 0.5), '12', None]
    for record in invalid:
        for operation in [canonical, negate]:
            try:
                operation(record)
            except ValueError:
                counts['invalid_input_rejected'] += 1
            else:
                raise AssertionError('invalid unary record accepted')
        for operation in [equivalent, add, subtract, multiply, leq]:
            for left, right in [(record, zero), (zero, record)]:
                try:
                    operation(left, right)
                except ValueError:
                    counts['invalid_input_rejected'] += 1
                else:
                    raise AssertionError('invalid binary record accepted')
    for n in [True, -1, 0.5, '1', None]:
        try:
            embed(n)
        except ValueError:
            counts['invalid_input_rejected'] += 1
        else:
            raise AssertionError('invalid natural embedding accepted')
    examples = []
    for operation, left, right, expected in [
        (add, (0, 3), (5, 0), (2, 0)),
        (subtract, (3, 0), (5, 0), (0, 2)),
        (multiply, (0, 3), (0, 4), (12, 0)),
        (multiply, (0, 3), (4, 0), (0, 12)),
        (multiply, (5, 5), (0, 4), (0, 0)),
        (multiply, (3, 1), (1, 4), (0, 6)),
        (multiply, (5, 3), (1, 4), (0, 6)),
        (multiply, (0, 2), (0, 3), (6, 0)),
        (multiply, (3, 5), (2, 7), (10, 0)),
        (add, (2, 5), (7, 1), (3, 0)),
        (add, (0, 3), (6, 0), (3, 0)),
        (subtract, (3, 0), (8, 0), (0, 5)),
        (subtract, (3, 0), (0, 8), (11, 0)),
        (subtract, (0, 3), (0, 8), (5, 0)),
    ]:
        raw = operation(left, right)
        result = canonical(raw)
        require(result == expected, ('example', operation.__name__, left, right))
        examples.append(dict(operation=operation.__name__, left=left, right=right,
                             expected=expected, raw_result=raw, actual=result, result='pass'))
    counts['examples'] = len(examples)
    sources = ['tools/integer_pairs.py', 'tools/validate_integer_pairs.py']
    report = dict(schema_version=1, result='pass', checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  scope=dict(pair_entry_inclusive_range=[0, 6], triple_pair_entry_inclusive_range=[0, 3],
                             comparison_model='Independent Python signed integer arithmetic',
                             representative_checks='All same-value pair replacements within the stated finite domain'),
                  counts=counts, manuscript_examples=examples,
                  source_sha256={p:sha256((ROOT/p).read_bytes()).hexdigest() for p in sources},
                  reproduce='python tools/validate_integer_pairs.py',
                  limitations=['Finite checks do not prove the general mathematical claims.',
                               'Pairs are representatives; Python tuple equality is not integer-class equality.',
                               'No formal proof assistant, efficiency claim or PDF validation is implied.'])
    destination = ROOT/'research/production/integer_pairs_validation.json'
    destination.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(dict(result=report['result'], counts=counts, report=str(destination.relative_to(ROOT))), indent=2))


if __name__ == '__main__':
    main()
