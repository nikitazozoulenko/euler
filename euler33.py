import numpy as np

def prime_factorization(n, primes): #positive n, WARNING: primes is a set
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


def reduce_fraction(num, den, primes):
    num_factors = prime_factorization(num, primes)
    den_factors = prime_factorization(den, primes)
    common = {}
    for p, power in num_factors.items():
        if p in den_factors:
            comm_pow = min(num_factors[p] , den_factors[p])
            if comm_pow>0:
                common[p] = comm_pow
    
    for p, power in common.items():
        if(power == num_factors[p]):
            num_factors.pop(p)
        else:
            num_factors[p]-=power
        if(power == den_factors[p]):
            den_factors.pop(p)
        else:
            den_factors[p]-=power

    return num_factors, den_factors


def get_number(factors):
    value=1
    for p, power in factors.items():
        value *= p**power
    return value

list_num = []
list_den = []
primes = primes_up_to(100)
for numerator in range(10, 100):
    for denominator in range(numerator+1, 100):
        if numerator!=denominator:
            n=0
            d=0
            if (numerator//10 == denominator%10):
                n=numerator%10
                d=denominator//10
            elif(numerator%10 == denominator//10):
                n=numerator//10
                d=denominator%10
            
            if n!=0 and d!=0:
                num_fac, den_fac = reduce_fraction(numerator, denominator, primes)
                n_fac, d_fac = reduce_fraction(n, d, primes)
                if (n_fac==num_fac) and (d_fac==den_fac):
                    list_num.append(get_number(n_fac))
                    list_den.append(get_number(d_fac))

primes = primes_up_to(100000)
num=1
den=1
for n, d in zip(list_num, list_den):
    num *= n
    den *= d

num_fac, den_fac = reduce_fraction(num, den, primes)
print(get_number(den_fac))
