import numpy as np
from itertools import permutations

max_n=100000
triangles = set([n*(n+1)//2 for n in range(1,max_n)])
pentagons = set([n*(n+n+n-1)//2 for n in range(1,max_n)])
hexagons = set([n*(n+n-1) for n in range(1,max_n)])

print(triangles.intersection(pentagons).intersection(hexagons))