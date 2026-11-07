"""Finite function graphs on integer labels, with declared domain and codomain.

This teaching implementation does not represent all functions on Q or R.
Inputs are finite explicit collections; repeated identical graph pairs denote
one set member. Conflicting outputs, missing inputs and out-of-set pairs fail.
Composition uses exactly the book's matching-codomain convention; it does not
claim that other image-compatible composition conventions are impossible.
"""
from dataclasses import dataclass


def labels(values):
    if not isinstance(values, (tuple, list, set, frozenset)):
        raise ValueError('expected an explicit finite collection of integer labels')
    if any(type(v) is not int for v in values):
        raise ValueError('labels must be integers; bool is not an integer label here')
    return frozenset(values)


@dataclass(frozen=True)
class FiniteFunction:
    domain: frozenset
    codomain: frozenset
    graph: frozenset

    def __post_init__(self):
        a, b = labels(self.domain), labels(self.codomain)
        if not isinstance(self.graph, (tuple, list, set, frozenset)):
            raise ValueError('graph must be an explicit finite collection of pairs')
        pairs = []
        values = {}
        for item in self.graph:
            if not isinstance(item, (tuple, list)) or len(item) != 2:
                raise ValueError('each graph entry must have two coordinates')
            x, y = item
            if type(x) is not int or type(y) is not int:
                raise ValueError('graph coordinates must be integer labels')
            if x not in a or y not in b:
                raise ValueError('graph pair is outside domain times codomain')
            if x in values and values[x] != y:
                raise ValueError('an input has two different outputs')
            values[x] = y
            pairs.append((x, y))
        if set(values) != a:
            raise ValueError('some domain element has no output')
        object.__setattr__(self, 'domain', a)
        object.__setattr__(self, 'codomain', b)
        object.__setattr__(self, 'graph', frozenset(pairs))

    def __call__(self, x):
        if type(x) is not int or x not in self.domain:
            raise ValueError('input is outside the declared integer domain')
        for left, right in self.graph:
            if left == x:
                return right
        raise AssertionError('validated graph lost an input')

    def image(self):
        return frozenset(y for _, y in self.graph)


def require_function(f):
    if type(f) is not FiniteFunction:
        raise ValueError('expected a validated FiniteFunction')
    return f


def restrict(f, subset):
    require_function(f)
    d = labels(subset)
    if not d <= f.domain:
        raise ValueError('restriction domain is not a subset')
    return FiniteFunction(d, f.codomain, [(x, y) for x, y in f.graph if x in d])


def compose(g, f):
    """g after f; this interface requires f.codomain == g.domain."""
    require_function(f)
    require_function(g)
    if f.codomain != g.domain:
        raise ValueError('declared middle sets do not match')
    return FiniteFunction(f.domain, g.codomain, [(x, g(f(x))) for x in f.domain])


def identity(domain):
    a = labels(domain)
    return FiniteFunction(a, a, [(x, x) for x in a])
