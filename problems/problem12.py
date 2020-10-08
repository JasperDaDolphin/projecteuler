def factors(n):
    return set(x for tup in ([i, n//i] 
                for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)

def problem():
    i=2
    while True:
        t=sum(i for i in range(1, i))
        if (len(factors(t))>500):
            return t
        i+=1
