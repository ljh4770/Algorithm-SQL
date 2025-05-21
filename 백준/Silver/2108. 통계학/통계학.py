import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()

mean = round(sum(nums) / n)

median = nums[n // 2]

counts = Counter(nums)
counts = sorted(counts.items(), key=lambda x: -x[1])

if len(counts) > 1 and counts[0][1] == counts[1][1]:
    mode = counts[1][0]
else:
    mode = counts[0][0]

range_ = nums[-1] - nums[0]

print(mean)
print(median)
print(mode)
print(range_)