def factorial(n):
    res =1
    for i in range(1,n+1):
        res *=i
    return res

x = factorial(100)
x = str(x)
res = 0
for c in x:
    res += int(c)

print(res)