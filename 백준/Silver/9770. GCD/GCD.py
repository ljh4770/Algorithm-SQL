import sys
from math import gcd
from itertools import combinations

numbers = []
while line := sys.stdin.readline():
    numbers.extend([*map(int, line.rstrip().split())])

answer = max([gcd(a, b) for a, b in combinations(numbers, 2)])
print(answer)