"""Exact rational kernels for ratios and changes of numerical unit values.

Records (a,b) have integer components and b>0. This module receives numerical
values only: callers must establish matching quantity kinds and unit relations.
It does not infer dimensions, validate physical measurements, or convert affine
scales. Positive scale k means NEW unit = k * OLD unit. Rate conversion uses
positive scales k for the numerator unit and l for the denominator unit.
"""
from rational_addition import checked_pair, equivalent
from rational_multiplication import multiply, divide


def positive_scale(record):
    a, b = checked_pair(record)
    if a <= 0:
        raise ValueError('unit scale must be strictly positive')
    return a, b


def ratio(first, second):
    """first:second; second must be nonzero, and may otherwise have either sign."""
    return divide(first, second)


def proportion(a, b, c, d):
    """Return whether a:b=c:d, rejecting zero b or d before using cross products."""
    checked_pair(a)
    bn, _ = checked_pair(b)
    checked_pair(c)
    dn, _ = checked_pair(d)
    if bn == 0 or dn == 0:
        raise ValueError('both ratio denominators must be nonzero')
    return equivalent(multiply(a, d), multiply(b, c))


def convert_value(value, new_in_old):
    """For v=k*u and Q=x*u=y*v, return y=x/k. k must be positive."""
    checked_pair(value)
    return divide(value, positive_scale(new_in_old))


def convert_rate(value, numerator_scale, denominator_scale):
    """For v=k*u, z=l*w, convert x in u/w to y=x*l/k in v/z."""
    checked_pair(value)
    k = positive_scale(numerator_scale)
    l = positive_scale(denominator_scale)
    return divide(multiply(value, l), k)
