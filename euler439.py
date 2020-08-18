import math

def sum_of_sum_of_divisors(N): #O(sqrt(N)) time complexity
    div_sum = 0
    q = int(math.sqrt(N))
    for i in range(1, q+1):
        div_sum += (i * (N // i))

    for i in range(1, N//(q+1)+1):
        m = N // i
        k = N // (i + 1)
        div_sum += (i * (m * (m + 1) - k * (k + 1)) // 2)
        i += 1
    
    return div_sum


def sum_of_divisors(N): #O(N)
    div_sum=0
    for i in range(1, N+1):
        if N%i==0:
            div_sum+=i
    return div_sum



def increment(num, counts):
    if num not in counts:
        counts[num] = 1
    else:
        counts[num] +=1


def f1(N):
    counts={}
    q = int(math.sqrt(N))
    for p in range(2,N+1):
        num = N//p
        increment(num, counts)
    return counts

def f2(N):
    counts={}
    q = int(math.sqrt(N))
    for p in range(2,q+1):
        num = N//p
        increment(num, counts)
    for p in range(1, q+1):
        cnt = int(N/p) - int(N/(p+1))
        counts[p] = cnt
    return counts

s_o_s_o_s = {}
mod = 10**9

def S(N):
    if N==1:
        return 1
    global s_o_s_o_s
    if N in s_o_s_o_s:
        return s_o_s_o_s[N]
    
    sos = sum_of_sum_of_divisors(N)
    counts = f2(N)
    
    minus = 0
    start = 2
    for key in sorted(counts.keys(), reverse=True):
        count = counts[key]
        p_sum = (count * (start + start + count-1)) //2
        minus += p_sum * S(key) % mod
        start += count
    res = (sos*sos - minus) % mod
    s_o_s_o_s[N] = res
    return res


import time
N=10**11
t = time.time()
print(S(N))
print(time.time()-t)

# N_MAX= 15
# for N in range(1, N_MAX+1):
#     accum=0
#     for i in range(1,N+1):
#         accum += sum_of_divisors(i)
#     print(N, accum, sum_of_sum_of_divisors(N))
#     print() 


# 968697378
# 852.0721166133881
