"""Exact quotient and rational remainder for the divisor X-C(a)."""
from fractions import Fraction
from linear_equation_solvers import rational
from rational_polynomial_basic import record, add
from rational_polynomial_product import shift


def divide_linear(values, at):
    """Return (canonical quotient, exact remainder); X-C(at) is never zero."""
    coefficients, at = record(values), rational(at)
    quotient = (Fraction(0),)
    remainder = coefficients[-1]
    for coefficient in reversed(coefficients[:-1]):
        quotient = add(shift(quotient), (remainder,))
        remainder = coefficient + at * remainder
    return quotient, remainder
