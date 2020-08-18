from datetime import date
from collections import Counter

counters = {}

for year in range(1901, 2001):
    for month in range(1, 13):
        day = date(year, month, 1)
        weekday = day.weekday()
        print(weekday)
        if weekday not in counters:
            counters[weekday] =1
        else:
            counters[weekday] +=1

print(counters)