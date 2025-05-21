import sys
n, m = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))
data = [tuple(map(lambda x: int(x) - 1, input().split(' '))) for _ in range(m)]
cum_sum = [0] * n
cum_sum[0] = nums[0]

for i in range(1, n, 1):
    cum_sum[i] = cum_sum[i - 1] + nums[i]

for i, j in data:
    print(cum_sum[j] - cum_sum[i] + nums[i])