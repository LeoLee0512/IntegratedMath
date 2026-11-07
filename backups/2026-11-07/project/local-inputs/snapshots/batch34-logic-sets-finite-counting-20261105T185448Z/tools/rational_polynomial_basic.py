"""Exact nonempty rational coefficient records; no polynomial multiplication."""
from fractions import Fraction
from linear_equation_solvers import rational
from rational_powers_sums import natural_index, power, finite_sum


def record(values):
    if type(values) not in (list, tuple):
        raise TypeError('a nonempty list or tuple of rational coefficients is required')
    if not values:
        raise ValueError('the empty coefficient record is not used in this model')
    return tuple(rational(value) for value in values)


def normalize(values):
    coefficients = record(values)
    length = len(coefficients)
    while length > 1 and coefficients[length - 1] == 0:
        length -= 1
    return coefficients[:length]


def coefficient(values, index):
    coefficients = record(values)
    index = natural_index(index)
    return coefficients[index] if index < len(coefficients) else Fraction(0)


def same_polynomial(left, right):
    a, b = record(left), record(right)
    return normalize(a) == normalize(b)


def degree(values):
    coefficients = normalize(values)
    if coefficients == (Fraction(0),):
        raise ValueError('the zero polynomial has no degree in this convention')
    return len(coefficients) - 1


def evaluate(values, at):
    coefficients, at = record(values), rational(at)
    terms = tuple(value * power(at, index)
                  for index, value in enumerate(coefficients))
    return finite_sum(terms)


def add(left, right):
    a, b = record(left), record(right)
    length = max(len(a), len(b))
    terms = tuple((a[index] if index < len(a) else Fraction(0))
                  + (b[index] if index < len(b) else Fraction(0))
                  for index in range(length))
    return normalize(terms)


def scale(scalar, values):
    scalar, coefficients = rational(scalar), record(values)
    return normalize(tuple(scalar * value for value in coefficients))


def subtract(left, right):
    a, b = record(left), record(right)
    return add(a, scale(-1, b))
