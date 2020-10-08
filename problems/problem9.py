#!/usr/bin/python

import math
import itertools


def problem():
    for n in range(1, 1000):
        for m in range(n + 1, 1000):
            a = m ** 2 - n ** 2
            b = 2 * n * m
            c = n ** 2 + m ** 2
            if a + b + c == 1000:
                return a * b * c
