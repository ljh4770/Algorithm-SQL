import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split(' '))
for item in combinations(range(1, n + 1, 1), m):
    for num in item:
        print(num, end=' ')
    print()