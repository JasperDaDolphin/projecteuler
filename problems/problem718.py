import multiprocess as mp
import itertools

def equ(a, b, c, p, n):
    return ((17**p)*a + (19**p)*b + (23**p)*c) == n

def find_representation(a, b, c, n):
  for i in range(n, -1, -a):
    for j in range(i, -1, -b):
      if not j % c:
        return True
  return False

def frobenius_number(a, b, c):
  a, b, c = sorted((a, b, c))
  base = n = c
  while True:
    if find_representation(a, b, c, n):
        if n == base + a:
            return base
    else:
        base = n
    n += 1

def reachable(n, p):
    if n < 17**p + 19**p + 23**p:
        print(n)
        return False
    for a in range(1, n):
        for b in range(1, n):
            for c in range(1, n):
                if equ(a, b, c, p, n):
                    return True
    print(n)
    return False

def G(p):    
    max_n = frobenius_number(17**p, 19**p, 23**p) + 17**p + 19**p + 23**p
    a = max_n + sum(n for n in range(1, max_n) if not reachable(n, p))
    return a

def problem():
    return G(1)
