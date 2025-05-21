import sys
from itertools import combinations_with_replacement as cwr
input = sys.stdin.readline

n, m = map(int, input().split(' '))
for item in cwr(range(1, n + 1, 1), m):
    for num in item:
        print(num, end=' ')
    print()