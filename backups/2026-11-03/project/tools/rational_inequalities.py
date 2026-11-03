"""Exact affine and absolute-value inequalities over Q, not R.

A solution is a tuple of intervals (lower, upper, left_closed, right_closed).
Finite endpoints are Fractions; None marks an unbounded side, not a number.
The tuple denotes the union. The empty tuple denotes the empty set.
This module does not parse expressions or impose an additional domain D.
"""
from linear_equation_solvers import rational


RELATIONS = ('<', '<=', '>', '>=')
REVERSE = {'<': '>', '<=': '>=', '>': '<', '>=': '<='}
ALL = ((None, None, False, False),)


def relation_check(relation):
    if type(relation) is not str or relation not in RELATIONS:
        raise ValueError('relation must be <, <=, >, or >=')


def compare(left, right, relation):
    relation_check(relation)
    if relation == '<':
        return left < right
    if relation == '<=':
        return left <= right
    if relation == '>':
        return left > right
    return left >= right


def solve_linear(a, b, c, relation):
    """Return all rational x satisfying a*x+b relation c."""
    relation_check(relation)
    a, b, c = (rational(v) for v in (a, b, c))
    if a == 0:
        return ALL if compare(b, c, relation) else ()
    endpoint = (c-b)/a
    if a < 0:
        relation = REVERSE[relation]
    if relation in ('<', '<='):
        return ((None, endpoint, False, relation == '<='),)
    return ((endpoint, None, relation == '>=', False),)


def solve_absolute(a, b, radius, relation):
    """Return all rational x satisfying abs(a*x+b) relation radius."""
    relation_check(relation)
    a, b, radius = (rational(v) for v in (a, b, radius))
    if a == 0:
        return ALL if compare(abs(b), radius, relation) else ()
    if radius < 0:
        return () if relation in ('<', '<=') else ALL
    center = -b/a
    if radius == 0:
        if relation == '<':
            return ()
        if relation == '<=':
            return ((center, center, True, True),)
        if relation == '>=':
            return ALL
        return ((None, center, False, False),
                (center, None, False, False))
    # a != 0 and radius > 0, hence abs(a) > 0 and half_width > 0.
    half_width = radius/abs(a)
    lower, upper = center-half_width, center+half_width
    if relation in ('<', '<='):
        closed = relation == '<='
        return ((lower, upper, closed, closed),)
    closed = relation == '>='
    return ((None, lower, False, closed),
            (upper, None, closed, False))


def contains(solution, value):
    """Membership for records produced by the two solvers, not a record parser."""
    value = rational(value)
    for lower, upper, left_closed, right_closed in solution:
        left = (lower is None or value > lower
                or (left_closed and value == lower))
        right = (upper is None or value < upper
                 or (right_closed and value == upper))
        if left and right:
            return True
    return False
