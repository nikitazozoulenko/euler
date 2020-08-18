import numpy as np

with open("euler22_names.txt") as f:
    data = f.read().replace('"', "").split(",")
    data = sorted(data)
    result=0
    for i,name in enumerate(data):
        score=0
        for c in name:
            score += ord(c)-64
        result += score*(i+1)
    print(result)

