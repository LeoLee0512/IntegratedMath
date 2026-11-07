"""Exact multiplication and partial division of positive-denominator records.

Tuples represent rational classes; outputs are normalized integer records.
The reciprocal of zero and every division by zero raise ValueError.
Branching on a numerator's sign uses integer order, not rational order.
No floating point or rational order is used. This is a teaching implementation.
"""
from rational_addition import checked_pair, normalize


def multiply(left, right):
    a, b = checked_pair(left)
    c, d = checked_pair(right)
    return normalize((a * c, b * d))


def reciprocal(record):
    a, b = checked_pair(record)
    if a == 0:
        raise ValueError('zero has no reciprocal')
    if a > 0:
        return normalize((b, a))
    return normalize((-b, -a))


def divide(left, right):
    checked_pair(left)
    return multiply(left, reciprocal(right))


if __name__ == '__main__':
    print(multiply((-2, 3), (9, 4)))
    print(multiply((-2, 3), (-9, 4)))
    print(reciprocal((-6, 8)))
    print(divide((2, 3), (-4, 5)))
    print(divide((0, 7), (3, 5)))
