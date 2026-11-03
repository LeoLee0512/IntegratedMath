"""Exact rational squares and quadratic equations; no real-root approximation."""
from fractions import Fraction
from linear_equation_solvers import rational


def integer_sqrt(value):
    """Return s with s*s <= value < (s+1)*(s+1), for a nonnegative int."""
    if type(value) is not int or value < 0:
        raise ValueError('expected a nonnegative integer')
    low, high = 0, value + 1
    while high - low > 1:
        middle = (low + high) // 2
        if middle * middle <= value:
            low = middle
        else:
            high = middle
    return low


def rational_square_root(value):
    """Return the nonnegative rational square root, or None if none exists."""
    value = rational(value)
    if value < 0:
        return None
    p, q = value.numerator, value.denominator
    m, n = integer_sqrt(p), integer_sqrt(q)
    if m * m != p or n * n != q:
        return None
    return Fraction(m, n)


def solve_quadratic(a, b, c):
    """Solve a*x*x+b*x+c=0 over Q; finite roots are sorted and distinct."""
    a, b, c = (rational(v) for v in (a, b, c))
    if a == 0:
        if b == 0:
            return {'kind': 'all' if c == 0 else 'none'}
        return {'kind': 'finite', 'roots': (-c / b,)}
    delta = b*b - 4*a*c
    s = rational_square_root(delta)
    if s is None:
        return {'kind': 'none'}
    roots = tuple(sorted(set(((-b-s)/(2*a), (-b+s)/(2*a)))))
    return {'kind': 'finite', 'roots': roots}
