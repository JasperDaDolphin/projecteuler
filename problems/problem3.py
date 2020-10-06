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

def largest_prime_factor(x):
    return [i for i in range(1, x + 1) if is_prime(i) and x % i == 0][-1]

def problem():
    return largest_prime_factor(600851475143)

