"""Exact column addition/subtraction accompanying the B1.6 manuscript.

Inputs are nonempty most-significant-first digit lists in a common base >= 2.
Leading zeroes are permitted; results are canonical. This is a companion to
the written proofs, not a proof of them. Python integers are exact; no floats.
The source is reproduced in the written-arithmetic appendix.
"""
from natural_algorithms import value_digits, divide_nat


def canonical(low_first):
    while len(low_first) > 1 and low_first[-1] == 0:
        low_first.pop()
    return list(reversed(low_first))


def add_digits(left, right, base):
    """Add legal digit lists by columns, recording carry as quotient by base."""
    value_digits(left, base)
    value_digits(right, base)
    a, b = list(reversed(left)), list(reversed(right))
    width = max(len(a), len(b))
    a.extend([0] * (width - len(a)))
    b.extend([0] * (width - len(b)))
    carry, output = 0, []
    for x, y in zip(a, b):
        carry, digit = divide_nat(x + y + carry, base)
        output.append(digit)
    if carry:
        output.append(carry)
    return canonical(output)


def subtract_digits(left, right, base):
    """Return left minus right, only when the result is a natural number."""
    left_value = value_digits(left, base)
    right_value = value_digits(right, base)
    if left_value < right_value:
        raise ValueError('natural subtraction requires left >= right')
    a, b = list(reversed(left)), list(reversed(right))
    width = max(len(a), len(b))
    a.extend([0] * (width - len(a)))
    b.extend([0] * (width - len(b)))
    borrow, output = 0, []
    for x, y in zip(a, b):
        needed = y + borrow
        if needed <= x:
            digit, borrow = x - needed, 0
        else:
            digit, borrow = x + base - needed, 1
        output.append(digit)
    if borrow != 0:
        raise AssertionError('final borrow contradicts left >= right')
    return canonical(output)


if __name__ == '__main__':
    print('999 + 1:', add_digits([9, 9, 9], [1], 10))
    print('1002 - 587:', subtract_digits([1, 0, 0, 2], [5, 8, 7], 10))
