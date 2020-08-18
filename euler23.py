import numpy as np

def proper_divisor_sum(n):
    result = 0
    for i in range(1, int(np.sqrt(n))+1):
        if n%i==0:
            result+=i
            if n/i != i:
                result += n/i
    return result-n


def can_be_written_as_two_ele(n, abundant):
    l = 0
    r = len(abundant)-1
    while(True):
        val = abundant[l] + abundant[r]
        if val==n:
            return True
        elif l==r:
            return False
        elif val<n:
            l+=1
        else:
            r-=1
    return False


max_n=28123
abundant = []
for i in range(1, max_n+1):
    if(i<proper_divisor_sum(i)):
        abundant.append(i)

print(abundant)

summable = []
for i in range(1, max_n+1):
    if(not can_be_written_as_two_ele(i, abundant)):
        summable.append(i)
print(summable)
print(sum(summable))
