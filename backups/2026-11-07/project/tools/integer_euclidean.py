"""Exact integer Euclidean division, divisibility and gcd for B1.9--B1.11.

Division requires b != 0 and returns 0 <= r < |b|, including negative b.
This deliberately uses the earlier natural-number division implementation;
it is educational, not an efficient large-integer algorithm. gcd(0,0)=0.
No floating-point operations occur. Finite tests do not replace the proofs.
"""
from natural_algorithms import divide_nat


def integer(value, name):
    if type(value) is not int:
        raise ValueError(name + ' must be an integer (bool is not accepted)')
    return value


def divide_integer(a, b):
    integer(a, 'a')
    integer(b, 'b')
    if b == 0:
        raise ValueError('Euclidean division requires a nonzero divisor')
    magnitude_a = a if a >= 0 else -a
    magnitude_b = b if b > 0 else -b
    q, r = divide_nat(magnitude_a, magnitude_b)
    if a < 0:
        if r == 0:
            q = -q
        else:
            q, r = -(q + 1), magnitude_b - r
    if b < 0:
        q = -q
    return q, r


def divides(d, n):
    integer(d, 'd')
    integer(n, 'n')
    if d == 0:
        return n == 0
    return divide_integer(n, d)[1] == 0


def gcd_trace(a, b):
    """Return (nonnegative gcd, trace); rows record u,v,q,r before replacement."""
    integer(a, 'a')
    integer(b, 'b')
    u = a if a >= 0 else -a
    v = b if b >= 0 else -b
    rows = []
    while v != 0:
        q, r = divide_nat(u, v)
        rows.append({'u': u, 'v': v, 'q': q, 'r': r})
        u, v = v, r
    return u, rows


def gcd_integer(a, b):
    return gcd_trace(a, b)[0]


if __name__ == '__main__':
    print(divide_integer(-23, 5))
    print(divide_integer(-23, -5))
    print(divides(0, 0), divides(0, 7))
    print(gcd_trace(-48, 18))
    print(gcd_trace(0, 0))
