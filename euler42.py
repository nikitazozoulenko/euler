import numpy as np


numbers = set([n*(n+1)/2 for n in range(1, 10000)])
with open("euler42_words.txt") as f:
    data = f.read().replace('"', "").split(",")
    data = sorted(data)
    count=0
    for i,name in enumerate(data):
        score=0
        for c in name:
            score += ord(c)-64
        if score in numbers:
            count +=1
    print(count)

