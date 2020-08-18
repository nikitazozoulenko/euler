import numpy as np

digits = ["0", "1", "2", "3","4","5","6","7","8","9"]
permutations=[]
i=0
def perm(current_perm, digits_left):
    if(not digits_left):
        global i
        i+=1
        if(i==1000000):
            print(current_perm)
    for d in digits_left:
        perm(current_perm+d, [dig for dig in digits_left if d!=dig])

perm("", digits)
