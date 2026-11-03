"""Exact polynomial shift and product, on nonempty rational records."""
from fractions import Fraction
from rational_polynomial_basic import record, normalize


def shift(values):
    """Prepend a zero coefficient, then restore the canonical record."""
    coefficients = record(values)
    return normalize((Fraction(0),) + coefficients)


def multiply(left, right):
    """Convolve two checked records; the deliberate final zero is harmless."""
    a, b = record(left), record(right)
    coefficients = [Fraction(0) for _ in range(len(a) + len(b))]
    for i, first in enumerate(a):
        for j, second in enumerate(b):
            coefficients[i + j] += first * second
    return normalize(coefficients)
