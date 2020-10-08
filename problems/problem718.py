#!/usr/bin/python

import multiprocess as mp
from math import ceil


def equ(t):
    (a, b, c, p, n) = t
    return 17 ** p * a + 19 ** p * b + 23 ** p * c == n


def find_representation(a,b,c,n):
    for i in range(n, -1, -a):
        for j in range(i, -1, -b):
            if not j % c:
                return True
    return False


def frobenius_number(a, b, c):
    (a, b, c) = sorted((a, b, c))
    base = n = c
    while True:
        if find_representation(a, b, c, n):
            if n == base + a:
                return base
        else:
            base = n
        n += 1


def reachable(pool, p, n):
    inputs = ((a, b, c, p, n) for a in range(1, ceil(n / 17)) for b in
        range(1, ceil(n / 19)) for c in range(1, ceil(n / 23)))
    results = pool.map(equ, inputs)
    return max(results)


def G(p):
    pool = mp.Pool(processes=1)
    min_n = 17 ** p + 19 ** p + 23 ** p
    max_n = frobenius_number(17 ** p, 19 ** p, 23 ** p) + min_n
    a = sum(m for m in range(min_n)) + max_n + sum(n for n in range(min_n, max_n) if not reachable(pool, p, n))
    pool.close()
    pool.join()
    return a


def problem():
    return G(1)
