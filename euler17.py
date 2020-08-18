import numpy as np


words = "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty thirty forty fifty sixty eighty ninety hundred thousand"
words = words.split()
counts = set()
for word in words:
    for char in word:
        counts.add(char)
print(len(counts))

first="one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty".split()
second="twenty thirty forty fifty sixty seventy eighty ninety".split()
def intToWord(x):
    if x==0:
        return ""
    elif x<20:
        return first[x-1]
    elif x<100:
        digit = x//10
        return second[digit-2]+intToWord(x%10)
    elif x<1000:
        digit = x//100
        aand = "and"
        if x%100==0:
            aand=""
        return first[digit-1]+"hundred"+aand+intToWord(x%100)
    else:
        return "onethousand"

res=0
for i in range(1,1001):
    s=intToWord(i)
    print(i,s)
    res+=len(s)
print(res)