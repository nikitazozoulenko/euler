import numpy as np

def len_fraction_cycle(denominator, base): #needs to be integers
    r=1
    expansion = []
    seen={}
    idx=0
    while r not in seen:
        if(r==0):
            seen[r]=idx+1
        else:
            seen[r]=idx
        idx+=1
        top = r*base
        expansion.append(top//denominator)
        r=top%denominator

    print("n",i, "cycle len", idx-seen[r], "exp", expansion)
    return idx-seen[r]


base=10
max_n=1000
cycle_lengths = []
for i in range(2, max_n):
    cycle_lengths.append(len_fraction_cycle(i, base))

print(np.argmax(cycle_lengths))
    