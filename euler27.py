import numpy as np

def f(n,a,b):
    return n*n + a*n + b

def primes_up_to(x):
    primes = []
    numbers = np.arange(x-1)+2
    is_prime = np.ones(x-1)
    for i, n in enumerate(numbers):
        if(is_prime[i]):
            primes.append(n)
            for j in range(i, x-1, n):
                is_prime[j]=0
    return primes


primes=set(primes_up_to(1000*1000*2))
print(primes)
max_ab = (0, 0, 0)
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n=0
        while f(n,a,b) in primes:
            n+=1
        if n >= max_ab[0]:
            max_ab = (n, a, b)
            print(max_ab)
