#!/usr/bin/python

from math import ceil


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


def largest_prime_factor(x):
    r = x - 2
    if x % 2 == 0:
        r = x - 1
    for i in range(r, 2, -2):
        if is_prime(i) and x % i == 0:
            return i


def problem():
    return largest_prime_factor(600851475143)
