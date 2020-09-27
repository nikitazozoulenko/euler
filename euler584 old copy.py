import numpy as np
import math
import time

from math import factorial
from operator import mul
from functools import reduce
def n_choose_k(n, k):
    # if k==0 or k==n:
    #     return 1
    # elif k < n-k:
    #     return reduce(mul, range(n-k+1, n+1)) // factorial(k)
    # else:
    #     return reduce(mul, range(k+1, n+1)) // factorial(n-k)
    return 1

count=0
max_exponential=7
def g(n, d):
    global count
    count+=1
    if d==1:
        return (n<=max_exponetial)
    if d%2 == 0:
        return sum([ n_choose_k(n,k)*g(k,d//2)*g(n-k,d//2) for k in range(n+1)])
    else:
        return sum([ n_choose_k(n,k)*g(k,d//2+1)*g(n-k,d//2) for k in range(n+1)])

# d=365

# t1 = time.time()
# t2 = time.time()
# for n in range(100):
#     g(n,d)
#     t3 = time.time()
#     print(n,d, t3-t2, (t3-t2)/(t2-t1), count)
#     t1=t2
#     t2=t3
#     count=0


def create_binom_tree(N):
    binom = [ [1 for _ in range(i+1)] for i in range(N+1)]
    for n in range(1,N+1):
        for k in range(1,n):
            binom[n][k] = binom[n-1][k] + binom[n-1][k-1]
    return binom



store = {} #index with store[(n,d)]

def store_and_return(val, n, d):
    global store
    store[(n,d)] = val
    return val

def g_new(n,d):
    global count
    count+=1
    if d==1:
        return store_and_return(n<max_exponential, n, d)
    elif d%2 == 0:
        return store_and_return( sum([ binom[n][k]*g_new(k,d//2)*g_new(n-k,d//2) for k in range(n+1)]), n ,d)
    else:
        return store_and_return( sum([ binom[n][k]*g_new(k,d-1)*g_new(n-k,1) for k in range(n+1)]), n , d)


n=10
d=8
binom = create_binom_tree(n) #easy way, O(n^2) space. i can do it in O(n) space without recursion
t1 = time.time()
t2 = time.time()+0.001
for n in [365]:
    binom = create_binom_tree(n)
    g_new(n,d)
    t3 = time.time()
    print(n,d, t3-t2, (t3-t2)/(t2-t1), count)
    t1=t2
    t2=t3
    count=0



# max_exponential = 21
# print( g_new(100, 6) )
# print(6**100)
# print( g_new(100, 6)/(6**100) )