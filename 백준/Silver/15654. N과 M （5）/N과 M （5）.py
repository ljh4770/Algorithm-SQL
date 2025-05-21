import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))
nums.sort()

for item in permutations(nums, m):
    for num in item:
        print(num, end=' ')
    print()