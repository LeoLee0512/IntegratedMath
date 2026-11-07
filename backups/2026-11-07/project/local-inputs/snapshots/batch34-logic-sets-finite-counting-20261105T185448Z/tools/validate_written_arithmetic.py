#!/usr/bin/env python3
"""Reproduce finite checks of B1.6 written arithmetic companion code.

This is implementation validation over declared finite domains, not a proof
of the general mathematical theorems. Run from any working directory.
"""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json

from written_arithmetic import add_digits, subtract_digits

ROOT = Path(__file__).resolve().parents[1]
BASES = (2, 3, 10, 16)
MAX_INPUT = 60


def independent_digits(number, base):
    """Use Python divmod, independently of the textbook division algorithm."""
    result = []
    while number:
        number, remainder = divmod(number, base)
        result.append(remainder)
    return list(reversed(result or [0]))


def require(condition, description):
    if not condition:
        raise AssertionError(description)


def main():
    counts = {
        'addition': 0,
        'nonnegative_subtraction': 0,
        'negative_subtraction_rejected': 0,
        'invalid_input_rejected': 0,
        'input_immutability': 0,
        'manuscript_examples': 0,
    }
    for base in BASES:
        for left_value in range(MAX_INPUT + 1):
            for right_value in range(MAX_INPUT + 1):
                left = [0] + independent_digits(left_value, base)
                right = independent_digits(right_value, base)
                before_left, before_right = left.copy(), right.copy()
                actual = add_digits(left, right, base)
                require(actual == independent_digits(left_value + right_value, base),
                        ('addition mismatch', base, left_value, right_value))
                counts['addition'] += 1
                require(left == before_left and right == before_right,
                        'addition mutated input')
                counts['input_immutability'] += 1
                if left_value >= right_value:
                    actual = subtract_digits(left, right, base)
                    require(actual == independent_digits(left_value - right_value, base),
                            ('subtraction mismatch', base, left_value, right_value))
                    counts['nonnegative_subtraction'] += 1
                else:
                    try:
                        subtract_digits(left, right, base)
                    except ValueError:
                        counts['negative_subtraction_rejected'] += 1
                    else:
                        raise AssertionError('negative natural result accepted')
                require(left == before_left and right == before_right,
                        'subtraction mutated input')
                counts['input_immutability'] += 1

    invalid_cases = [
        ('empty_left', [], [0], 10),
        ('empty_right', [0], [], 10),
        ('boolean_digit', [True], [0], 10),
        ('negative_digit', [-1], [0], 10),
        ('digit_equal_to_base', [10], [0], 10),
        ('base_one', [1], [0], 1),
        ('boolean_base', [1], [0], True),
        ('floating_digit', [1.0], [0], 10),
    ]
    for operation in (add_digits, subtract_digits):
        for label, left, right, base in invalid_cases:
            try:
                operation(left, right, base)
            except ValueError:
                counts['invalid_input_rejected'] += 1
            else:
                raise AssertionError((operation.__name__, label))

    manuscript_cases = [
        ('1002 - 587', subtract_digits, [1, 0, 0, 2], [5, 8, 7], 10, [4, 1, 5]),
        ('1000 - 46', subtract_digits, [1, 0, 0, 0], [4, 6], 10, [9, 5, 4]),
        ('758 + 486', add_digits, [7, 5, 8], [4, 8, 6], 10, [1, 2, 4, 4]),
        ('999 + 1', add_digits, [9, 9, 9], [1], 10, [1, 0, 0, 0]),
        ('11010 - 01011 in base 2', subtract_digits,
         [1, 1, 0, 1, 0], [0, 1, 0, 1, 1], 2, [1, 1, 1, 1]),
    ]
    manuscript_results = []
    for label, operation, left, right, base, expected in manuscript_cases:
        before_left, before_right = left.copy(), right.copy()
        actual = operation(left, right, base)
        require(actual == expected, ('manuscript example mismatch', label))
        require(left == before_left and right == before_right,
                ('manuscript example mutated input', label))
        counts['manuscript_examples'] += 1
        counts['input_immutability'] += 1
        manuscript_results.append({'case': label, 'base': base,
                                   'left': left, 'right': right,
                                   'expected_canonical_result': expected,
                                   'actual': actual, 'result': 'pass'})

    sources = ['tools/written_arithmetic.py', 'tools/natural_algorithms.py',
               'tools/validate_written_arithmetic.py']
    report = {
        'schema_version': 1,
        'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'result': 'pass',
        'scope': {
            'bases': list(BASES),
            'left_value_inclusive_range': [0, MAX_INPUT],
            'right_value_inclusive_range': [0, MAX_INPUT],
            'input_layout': 'Left input has one additional leading zero; right is canonical.',
            'expected_results': 'Independent Python integer arithmetic and divmod digit conversion.',
            'invalid_case_labels': [case[0] for case in invalid_cases],
            'checks_input_immutability': True,
            'checks_canonical_output': True,
        },
        'counts': counts,
        'manuscript_examples': manuscript_results,
        'arithmetic_and_negative_rejection_checks': sum(counts[k] for k in
            ('addition', 'nonnegative_subtraction', 'negative_subtraction_rejected')),
        'source_sha256': {name: sha256((ROOT / name).read_bytes()).hexdigest()
                          for name in sources},
        'limitations': [
            'Finite implementation checks are not proofs for all natural numbers or bases.',
            'The manuscript mathematical review is separate.',
            'This validation does not certify PDF rendering or computational efficiency.',
        ],
        'reproduce': 'python tools/validate_written_arithmetic.py',
    }
    destination = ROOT / 'research/production/written_arithmetic_validation.json'
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'result': report['result'], 'counts': counts,
                      'report': str(destination)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
