import numpy as np
import math
import time

from math import factorial
from operator import mul
from functools import reduce


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
    if(n,d) in store:
        return store[(n,d)]
    elif d==1:
        return store_and_return(n<=max_exponential, n, d)
    elif d%2 == 0:
        return store_and_return( sum([ binom[n][k]*g_new(k,d//2)*g_new(n-k,d//2) for k in range(n+1)]), n ,d)
    else:
        return store_and_return( sum([ binom[n][k]*g_new(k,d-1)*g_new(n-k,1) for k in range(n+1)]), n , d)


# n=10
# d=8
# binom = create_binom_tree(n)
# t1 = time.time()
# t2 = time.time()+0.001
# for n in [10**i for i in range(100)]:
#     binom = create_binom_tree(n)
#     g_new(n,d)
#     t3 = time.time()
#     print(n,d, t3-t2, (t3-t2)/(t2-t1), count)
#     t1=t2
#     t2=t3
#     count=0


max_n=5
m_people = 2
days_interval = 1 #leq max_d
max_d = 365


def gg(n,d, vect, pos=0): # (x1+ ... + xd)^n
    if d==1:
        if pos==0:
            for i in range(days_interval): #think days_interval=2
                idx = i % max_d
                vect[idx] += n
        val = 1
        for i in range(days_interval): #think days_interval=2
            idx = (pos+i) % max_d
            if vect[idx]>m_people:
                val=0
                break
        return val
    else:
        summ=0
        for k in range(n+1):
            powers = np.zeros(max_d)
            for i in range(days_interval): #think days_interval=2
                idx = (d-1+i) % max_d
                powers[idx] = n-k
            summ+= binom[n][k]*gg(k, d-1, vect+powers) * gg(n-k , 1, vect+powers, d-1)
        return summ


def g(n, d):
    if d==1:
        return (n<=m_people)
    if d%2 == 0:
        return sum([ binom[n][k]*g(k,d//2)*g(n-k,d//2) for k in range(n+1)])
    else:
        return sum([ binom[n][k]*g(k,d//2+1)*g(n-k,d//2) for k in range(n+1)])


# val1 = gg(max_n, max_d, np.zeros(max_d))
# val2 = g(max_n, max_d)
# print(val1)
# print(val2)

solutions = [0 for _ in range(100)]
binom = create_binom_tree(100 +1)
for max_n in range(100):
    # solutions[max_n] = gg(max_n, max_d, np.zeros(max_d))
    solutions[max_n] = g(max_n, max_d)
    print(max_n, solutions[max_n])