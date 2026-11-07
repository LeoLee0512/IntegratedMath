"""Exact extended Euclidean computations for B1.12/B1.13.

The original signed inputs a,b stay fixed in every coefficient invariant.
The sign factor of zero is chosen as 1, so extended_gcd(0,0) returns
(g,x,y)=(0,1,0). Coefficients are witnesses, not unique canonical answers.
The implementation uses elementary natural division, not an efficient method.
"""
from integer_euclidean import integer, divide_integer
from natural_algorithms import divide_nat


def extended_gcd(a, b):
    """Return g,x,y,trace with g>=0, g=gcd(a,b), a*x+b*y=g."""
    integer(a, 'a')
    integer(b, 'b')
    sign_a = 1 if a >= 0 else -1
    sign_b = 1 if b >= 0 else -1
    u, v = sign_a * a, sign_b * b
    x, y, X, Y = sign_a, 0, 0, sign_b
    rows = []
    while v != 0:
        q, r = divide_nat(u, v)
        next_x, next_y = x - q * X, y - q * Y
        rows.append(dict(u=u, v=v, x=x, y=y, X=X, Y=Y,
                         q=q, r=r, next_x=next_x, next_y=next_y))
        u, v, x, y, X, Y = v, r, X, Y, next_x, next_y
    return dict(g=u, x=x, y=y, trace=rows)


def linear_solution(a, b, c):
    """One integer solution of a*x+b*y=c, or None; not the full solution set."""
    integer(c, 'c')
    result = extended_gcd(a, b)
    g = result['g']
    if g == 0:
        return (0, 0) if c == 0 else None
    k, remainder = divide_integer(c, g)
    if remainder != 0:
        return None
    return k * result['x'], k * result['y']


def reduced_record(a, b):
    """Return primitive integer pair (p,q), q>0; this is not a rational type."""
    integer(a, 'a')
    integer(b, 'b')
    if b <= 0:
        raise ValueError('record requires a positive second component')
    g = extended_gcd(a, b)['g']
    p, r = divide_integer(a, g)
    q, s = divide_integer(b, g)
    if r != 0 or s != 0:
        raise AssertionError('gcd must divide both inputs')
    return p, q


if __name__ == '__main__':
    print(extended_gcd(48, 18))
    print(extended_gcd(-48, 18))
    print(extended_gcd(0, 0))
    print(linear_solution(6, 10, 14))
    print(reduced_record(-12, 18))
