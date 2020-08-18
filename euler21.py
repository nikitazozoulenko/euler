def proper_divisor_sum(n):
    result = 0
    for i in range(1, n):
        if n%i==0:
            result+=i
    return result

n_max = 10000
pairs = {}
for n in range (2, n_max+1):
    pairs[n] = proper_divisor_sum(n)

count =0
for n in range (2, n_max+1):
    if(pairs[n] in pairs and n!=pairs[n]):
        if(pairs[pairs[n]] == n):
            count+=n
            print(n, pairs[n])

print(count)


