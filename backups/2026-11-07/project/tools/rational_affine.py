"""Exact rational coordinate and affine calculations.

Numeric inputs are int or Fraction, never bool or float. Every affine function
here has domain Q and codomain Q. A finite graph test checks only the supplied
finite domain/codomain/point set; it cannot certify an infinite sampled graph.
"""
from fractions import Fraction
from linear_equation_solvers import rational


def affine_value(a, b, x):
    """Evaluate a*x+b with exact rational arithmetic."""
    a, b, x = (rational(v) for v in (a, b, x))
    return a*x+b


def slope_through(x1, y1, x2, y2):
    """Return (a,b) for the unique affine graph through distinct x values.

    Equal x values are rejected, whether the y values agree or disagree;
    neither case determines one unique affine rule.
    """
    x1, y1, x2, y2 = (rational(v) for v in (x1, y1, x2, y2))
    if x1 == x2:
        raise ValueError('distinct first coordinates are required')
    a = (y2-y1)/(x2-x1)
    return a, y1-a*x1


def intercepts(a, b):
    """Return vertical point and horizontal unique/none/all classification.

    horizontal=None for none/all; all means the entire rational horizontal
    axis, not all Q-squared. A point and its scalar intercept are distinct.
    """
    a, b = (rational(v) for v in (a, b))
    result = {'vertical': (Fraction(0), b), 'horizontal': None}
    if a != 0:
        result.update(horizontal_kind='unique', horizontal=(-b/a, Fraction(0)))
    else:
        result['horizontal_kind'] = 'all' if b == 0 else 'none'
    return result


def intersect_affine(a, b, c, d):
    """Classify the common points of y=a*x+b and y=c*x+d over Q-squared."""
    a, b, c, d = (rational(v) for v in (a, b, c, d))
    if a == c:
        return {'kind': 'coincident' if b == d else 'none', 'point': None}
    x = (d-b)/(a-c)
    return {'kind': 'unique', 'point': (x, a*x+b)}


def classify_linear_relation(p, q, r):
    """Classify all rational pairs satisfying p*x+q*y=r.

    affine: y=a*x+b; vertical: x=constant and any rational y;
    all: all Q-squared; none: empty set.
    """
    p, q, r = (rational(v) for v in (p, q, r))
    if q != 0:
        return {'kind': 'affine', 'a': -p/q, 'b': r/q}
    if p != 0:
        return {'kind': 'vertical', 'x': r/p}
    return {'kind': 'all' if r == 0 else 'none'}


def finite_graph_test(domain, codomain, points):
    """Test a finite relation against BOTH existence and unique output.

    Containers must be list, tuple, set or frozenset; each point must be a
    two-item list or tuple. Duplicates represent the same set member. Bad
    shapes or numeric types raise ValueError. Well-formed points outside
    domain x codomain yield False. All inputs are validated before evaluation.
    """
    allowed = (list, tuple, set, frozenset)
    if any(type(s) not in allowed for s in (domain, codomain, points)):
        raise ValueError('finite concrete containers are required')
    a = {rational(x) for x in domain}
    b = {rational(y) for y in codomain}
    graph = set()
    for point in points:
        if type(point) not in (list, tuple) or len(point) != 2:
            raise ValueError('each point must have two coordinates')
        graph.add((rational(point[0]), rational(point[1])))
    if any(x not in a or y not in b for x, y in graph):
        return False
    seen = {}
    for x, y in graph:
        if x in seen and seen[x] != y:
            return False
        seen[x] = y
    return set(seen) == a
