"""Bijections, inverse functions and preimages of finite integer-labelled tables.

The declared codomain is part of the function. inverse is defined only for
bijections. preimage returns a set and never requires invertibility.
No claims about arbitrary infinite one-sided inverses or choice are made.
"""
from finite_functions import FiniteFunction, require_function, labels


def injective(f):
    require_function(f)
    seen = set()
    for _, y in f.graph:
        if y in seen:
            return False
        seen.add(y)
    return True


def surjective(f):
    require_function(f)
    return f.image() == f.codomain


def bijective(f):
    require_function(f)
    return injective(f) and surjective(f)


def inverse(f):
    require_function(f)
    if not bijective(f):
        raise ValueError('inverse function requires a bijection onto the declared codomain')
    return FiniteFunction(f.codomain, f.domain, [(y, x) for x, y in f.graph])


def preimage(f, target_subset):
    require_function(f)
    t = labels(target_subset)
    if not t <= f.codomain:
        raise ValueError('preimage argument must be a subset of the declared codomain')
    return frozenset(x for x, y in f.graph if y in t)
