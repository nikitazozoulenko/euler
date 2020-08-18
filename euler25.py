f1 = 1
f2=  1
digits = 10**999
i =2
while(f2//digits==0):
    fib = f1+f2
    f1=f2
    f2=fib
    i+=1
print(i)