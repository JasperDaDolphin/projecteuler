# First Solution
# import sys
# a = [x for x in range(0, sys.maxsize) if (sum(1 for i in range(1, 21) if x%i==0) == 20)][1]
# print(a)

# Optimized Solution with help
from functools import reduce
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return  a * b // gcd(a, b)

def lcm_seq(seq):
    return reduce(lcm, seq)

def problem():
    return lcm_seq(range(1, 21))