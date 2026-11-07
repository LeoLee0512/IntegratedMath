"""Natural-pair representatives for the integer construction in B1.7/B1.8.

A pair (a,b) is a record, not an equivalence class stored by Python. Compare
records with equivalent(), not Python tuple equality. Operations return one
representative; the manuscript separately proves independence of that choice.
No floating point is used. Natural inputs exclude bool, negatives and fractions.
"""


def checked_pair(record):
    if not isinstance(record, (tuple, list)) or len(record) != 2:
        raise ValueError('a record must be a pair of natural numbers')
    if any(type(n) is not int or n < 0 for n in record):
        raise ValueError('pair entries must be natural numbers; bool is excluded')
    return record[0], record[1]


def equivalent(left, right):
    a, b = checked_pair(left)
    c, d = checked_pair(right)
    return a + d == b + c


def embed(n):
    return checked_pair((n, 0))


def add(left, right):
    a, b = checked_pair(left)
    c, d = checked_pair(right)
    return a + c, b + d


def negate(record):
    a, b = checked_pair(record)
    return b, a


def subtract(left, right):
    return add(left, negate(right))


def multiply(left, right):
    a, b = checked_pair(left)
    c, d = checked_pair(right)
    return a * c + b * d, a * d + b * c


def leq(left, right):
    a, b = checked_pair(left)
    c, d = checked_pair(right)
    return a + d <= b + c


def canonical(record):
    """Return (n,0) or (0,n); natural differences are taken only in range."""
    a, b = checked_pair(record)
    if b <= a:
        return a - b, 0
    return 0, b - a


if __name__ == '__main__':
    print('(2,5) and (1,4) represent the same integer:', equivalent((2, 5), (1, 4)))
    print('negative three plus five:', canonical(add((0, 3), (5, 0))))
    print('negative three times negative four:', canonical(multiply((0, 3), (0, 4))))
