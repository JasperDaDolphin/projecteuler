def is_prime(n):
    if n < 2: 
        return False
    elif n == 2:
        return True
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True

def nth_prime(n):
    return [x for x in range(3, n**2, 2) if is_prime(x)][n]

def problem():
    return nth_prime(100001)
    



