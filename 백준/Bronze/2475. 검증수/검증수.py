import sys

nums = list(map(int, sys.stdin.readline().split(' ')))
sum = 0

for num in nums:
    sum += num * num

print(sum % 10)
