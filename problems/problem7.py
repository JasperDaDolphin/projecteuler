#!/usr/bin/python


def nth_prime(n):
    c = 2
    for i in range(3, n ** 2, 2):
        k = 1
        while k * k < i:
            k += 2
            if i % k == 0:
                break
        else:
            c += 1
        if c == n:
            return i


def problem():
    return nth_prime(10001)
