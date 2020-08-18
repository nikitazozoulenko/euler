import numpy as np

if __name__=="__main__":
    for c in range(1, 999):
        for b in range(1, 1000-c):
            a = 1000-c-b
            if(a*a+b*b==c*c):
                print(a,b,c)
    print(375* 200 *425)
        