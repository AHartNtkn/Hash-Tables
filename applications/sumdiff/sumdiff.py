import sys
sys.path.append('../../hashtable')
from hashtable import HashTable
from itertools import permutations

"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = list(range(1, 10))
q = list(range(1, 200))
#q = [1, 3, 4, 7, 12]


def f(x):
    return x * 4 + 6

# f[a] + f[b] == f[c] - f[d]
#   ==>
# 4 a + 6 + 4 b + 6 == 4 c + 6 - 4 d - 6
#   ==>
# 4 (a + b + d) + 12 == 4 c
#   ==>
# a + b + d + 3 == c
# Ultimately, we're looking for all the triples that sum to a given value - 3

quads = []

for i, x in enumerate(q):
  for j, y in enumerate(q[i:], start=i):
    for k, z in enumerate(q[j:], start=j):
      if 3 + x + y + z in q:
          quads.append((x, y, z, 3 + x + y + z))

for (x, y, z, c) in quads:
  p = set(permutations([x,y,z]))

  for x, y, z in p:
    print(f"f({x}) + f({y}) = f({c}) - f({z})")
