"""Exact positive-denominator records for B1.14/B1.15.

A tuple is a representative, not the infinite equivalence class itself.
Outputs use the unique primitive positive-denominator representative.
Only integer arithmetic and the previously proved gcd reduction are used.
No rational multiplication, reciprocal, division or order is implemented.
The inherited elementary division algorithm is for teaching, not speed.
"""
from integer_euclidean import integer
from extended_euclidean import reduced_record


def checked_pair(record):
    if type(record) not in (tuple, list) or len(record) != 2:
        raise ValueError('expected two integer components')
    a, b = record
    integer(a, 'numerator')
    integer(b, 'denominator')
    if b <= 0:
        raise ValueError('denominator must be positive')
    return a, b


def equivalent(left, right):
    a, b = checked_pair(left)
    c, d = checked_pair(right)
    return a * d == b * c


def normalize(record):
    a, b = checked_pair(record)
    return reduced_record(a, b)


def embed(n):
    integer(n, 'integer input')
    return n, 1


def add(left, right):
    a, b = checked_pair(left)
    c, d = checked_pair(right)
    return normalize((a * d + b * c, b * d))


def negate(record):
    a, b = checked_pair(record)
    return normalize((-a, b))


def subtract(left, right):
    return add(left, negate(right))


if __name__ == '__main__':
    print(normalize((-42, 30)))
    print(equivalent((1, 2), (2, 4)))
    print(add((1, 2), (1, 3)))
    print(add((-2, 3), (1, 6)))
    print(subtract((1, 3), (5, 6)))
