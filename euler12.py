import numpy as np
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

def prime_factorization(n, primes): #positive n
    factors = {}
    for p in primes:
        if(n<=1):
            break
        while(n%p==0):
            n = n//p
            if p not in factors:
                factors[p] = 1
            else:
                factors[p] += 1
    return factors

MAX_ITER = 100000
MAX_N = MAX_ITER*(MAX_ITER+1)//2
primes = primes_up_to(int(np.sqrt(MAX_N))+1)
for i in range(1, MAX_ITER):
    n = i*(i+1)//2
    factors = prime_factorization(n, primes)
    n_divisors=1
    for p, power in factors.items():
        n_divisors *= power+1
    if(n_divisors>=500):
        print(, n_divisors)