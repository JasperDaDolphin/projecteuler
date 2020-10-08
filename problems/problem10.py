#!/usr/bin/python


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    k = 3
    while k * k <= n:
        if n % k == 0:
            return False
        k += 2
    return True


def problem():
    return sum([x for x in range(2, 2000000) if is_prime(x)])
