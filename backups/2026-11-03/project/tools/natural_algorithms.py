"""Exact natural-number algorithms accompanying B1.4/B1.5.

Definitions and proofs are in the manuscript. Finite program checks are not
proofs for every natural number. All lists have the most significant entry first.
The intentionally elementary division loop performs n steps, not a fast division
method. Python integers are exact; this module performs no floating-point work.
"""

def natural(value, name):
    if type(value) is not int or value < 0:
        raise ValueError(name + ' must be a natural number (bool is not accepted)')
    return value


def divide_nat(n, b):
    """Return q,r with n=b*q+r and 0<=r<b; b must be positive."""
    natural(n, 'n')
    natural(b, 'b')
    if b == 0:
        raise ValueError('division requires a positive divisor')
    q, r = 0, 0
    for _ in range(n):
        if r + 1 == b:
            q, r = q + 1, 0
        else:
            r = r + 1
    return q, r


def digits_nat(n, base):
    """Return canonical digits in base>=2, with zero represented by [0]."""
    natural(n, 'n')
    natural(base, 'base')
    if base < 2:
        raise ValueError('positional base must be at least two')
    if n == 0:
        return [0]
    digits = []
    current = n
    while current > 0:
        current, remainder = divide_nat(current, base)
        digits.append(remainder)
    digits.reverse()
    return digits


def value_digits(digits, base):
    """Evaluate legal digits; leading zeroes are allowed for comparisons."""
    natural(base, 'base')
    if base < 2:
        raise ValueError('positional base must be at least two')
    if not isinstance(digits, (list, tuple)) or not digits:
        raise ValueError('digits must be a nonempty list or tuple')
    value = 0
    for digit in digits:
        natural(digit, 'digit')
        if digit >= base:
            raise ValueError('each digit must be smaller than the base')
        value = base * value + digit
    return value


def normalize_coefficients(coefficients, base):
    """Carry nonnegative coefficients to canonical digits in base>=2."""
    natural(base, 'base')
    if base < 2:
        raise ValueError('positional base must be at least two')
    if not isinstance(coefficients, (list, tuple)) or not coefficients:
        raise ValueError('coefficients must be a nonempty list or tuple')
    for coefficient in coefficients:
        natural(coefficient, 'coefficient')
    low_first = list(reversed(coefficients))
    while True:
        index = next((i for i, c in enumerate(low_first) if c >= base), None)
        if index is None:
            break
        q, r = divide_nat(low_first[index], base)
        low_first[index] = r
        if index + 1 == len(low_first):
            low_first.append(0)
        low_first[index + 1] += q
    while len(low_first) > 1 and low_first[-1] == 0:
        low_first.pop()
    return list(reversed(low_first))


if __name__ == '__main__':
    print('23 divided by 5:', divide_nat(23, 5))
    print('203 in base 10:', digits_nat(203, 10))
    print('13 in base 2:', digits_nat(13, 2))
    print('[1, 25, 100] in base 10:', normalize_coefficients([1, 25, 100], 10))
