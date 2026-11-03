"""Exact comparison, absolute value and distance of rational representatives.

Each input is an integer pair (a,b) with b>0. Comparisons use cross products.
Value outputs are normalized positive-denominator records, not infinite classes.
No floating-point arithmetic, real completeness or geometric assumptions are used.
The inherited gcd reduction is educational, not optimized for large integers.
"""
from rational_addition import checked_pair, normalize, subtract


def compare(left, right):
    a, b = checked_pair(left)
    c, d = checked_pair(right)
    delta = a * d - b * c
    if delta < 0:
        return -1
    if delta > 0:
        return 1
    return 0


def leq(left, right):
    return compare(left, right) <= 0


def lt(left, right):
    return compare(left, right) < 0


def absolute(record):
    a, b = checked_pair(record)
    if a < 0:
        a = -a
    return normalize((a, b))


def distance(left, right):
    return absolute(subtract(left, right))


if __name__ == '__main__':
    print(compare((-2, 3), (-3, 4)))
    print(absolute((-6, 8)))
    print(distance((-3, 2), (3, 2)))
