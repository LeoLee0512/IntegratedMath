"""Exact nonnegative integer powers and finite rational sums.

The discrete convention power(0,0)=1 is part of this definition. No negative
exponents, infinite sums, arbitrary sequence callbacks or floating inputs.
Finite records are concrete lists/tuples, indexed from zero.
"""
from fractions import Fraction
from linear_equation_solvers import rational


def natural_index(value):
    if type(value) is not int or value < 0:
        raise ValueError('expected a nonnegative integer index, not bool')
    return value


def finite_record(values):
    if type(values) not in (list, tuple):
        raise ValueError('expected a finite list or tuple')
    return tuple(rational(value) for value in values)


def power(base, exponent):
    """Return base**exponent for exact rational base and natural exponent.

    Start at one, then multiply by the fixed base exactly exponent times.
    The empty iteration returns one even when base is zero.
    """
    base = rational(base)
    exponent = natural_index(exponent)
    result = Fraction(1)
    for _ in range(exponent):
        result = result*base
    return result


def partial_sums(values):
    """Return (S_0,...,S_n), including the empty-prefix sum S_0=0.

    All input terms are validated first. S_(i+1)=S_i+values[i].
    This includes n+1 accumulated values for an input record of length n.
    """
    values = finite_record(values)
    result = [Fraction(0)]
    for value in values:
        result.append(result[-1]+value)
    return tuple(result)


def finite_sum(values):
    """Return the sum of every term of a finite record; the empty sum is zero."""
    return partial_sums(values)[-1]


def segment_sum(values, start, count):
    """Sum count consecutive terms starting at index start.

    Require 0<=start<=len(values), count>=0, start+count<=len(values).
    In particular, start=len(values), count=0 is valid and returns zero.
    Every input term is validated, including terms outside the chosen segment.
    """
    values = finite_record(values)
    start = natural_index(start)
    count = natural_index(count)
    if start > len(values) or start+count > len(values):
        raise ValueError('segment must lie inside the given finite record')
    return finite_sum(values[start:start+count])
