import sys

input = sys.stdin.readline

nums = [int(input()) for _ in range(5)]

nums.sort()

mean = sum(nums) // 5

median = nums[2]

print(mean)

print(median)