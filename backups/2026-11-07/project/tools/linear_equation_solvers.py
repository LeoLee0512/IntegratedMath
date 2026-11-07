"""Exact rational linear equations and two-equation systems.

Inputs are Python integers or Fraction values, not floats or booleans.
The unknowns range over all Q. This code does not parse arbitrary expressions,
clear denominators, or impose extra user-domain restrictions automatically.
A line result means base + t*direction for every rational t.
"""
from fractions import Fraction


def rational(value):
    if type(value) not in (int, Fraction):
        raise ValueError('expected int or exact Fraction, not float or bool')
    return Fraction(value)


def solve_linear(a, b, c):
    """Solve a*x+b=c over Q, including a=0."""
    a, b, c = (rational(v) for v in (a, b, c))
    if a != 0:
        return {'kind': 'unique', 'value': (c-b)/a}
    return {'kind': 'all' if b == c else 'none'}


def solve_system(a, b, c, d, e, f):
    """Solve a*x+b*y=c and d*x+e*y=f over Q x Q.

    Return unique/none/line/all. No division occurs before a nonzero test.
    Row replacement retains the other equation; no geometric assumptions.
    """
    a, b, c, d, e, f = (rational(v) for v in (a, b, c, d, e, f))
    if a == 0 and b == 0:
        if c != 0:
            return {'kind': 'none'}
        if d == 0 and e == 0:
            return {'kind': 'all' if f == 0 else 'none'}
        a, b, c, d, e, f = d, e, f, a, b, c
    if a != 0:
        coefficient = e-d*b/a
        right = f-d*c/a
        if coefficient != 0:
            y = right/coefficient
            x = (c-b*y)/a
            return {'kind': 'unique', 'point': (x, y)}
        if right != 0:
            return {'kind': 'none'}
        return {'kind': 'line', 'base': (c/a, Fraction(0)),
                'direction': (-b/a, Fraction(1))}
    # The first row is nonzero, so a=0 implies b!=0.
    y = c/b
    right = f-e*y
    if d != 0:
        return {'kind': 'unique', 'point': (right/d, y)}
    if right != 0:
        return {'kind': 'none'}
    return {'kind': 'line', 'base': (Fraction(0), y),
            'direction': (Fraction(1), Fraction(0))}
