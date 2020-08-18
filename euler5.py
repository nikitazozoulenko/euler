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
        if(n==1):
            break
        while(n%p==0):
            n /= p
            if p not in factors:
                factors[p] = 1
            else:
                factors[p] += 1
    return factors

if __name__=="__main__":

    q = 20
    primes = primes_up_to(q)
    counts = {}
    for p in primes:
        counts[p]=0

    for i in range(2, q+1):
        factors = prime_factorization(i, primes)
        for key, val in factors.items():
            counts[key]= max(counts[key], val)
    
    number = 1
    for p, power in counts.items():
        number *= p**power
    print(number)

