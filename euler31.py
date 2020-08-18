import numpy as np


def count(S,coins, n,m):
    left=0
    up=0
    if(n-coins[m]>=0):
        up=S[n-coins[m], m]
    if(m-1>=0):
        left=S[n, m-1]
    return left+up

coins = [1,2,5,10, 20, 50, 100, 200]
max_number = 200
S = np.zeros((max_number+1, len(coins))).astype(np.integer)
S[0,:] = np.ones(len(coins))
for n in range(1,max_number+1):
    for m in range(len(coins)):
        S[n,m] = count(S, coins, n,m)
print(S[-1,-1])