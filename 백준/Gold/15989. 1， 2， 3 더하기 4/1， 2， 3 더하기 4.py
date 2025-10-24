import sys; input = sys.stdin.readline

t = int(input())
nums = [int(input()) for _ in range(t)]

MAX_LEN = 10_000 + 1
dp = [1] * MAX_LEN

for i in range(2, MAX_LEN, 1):
    dp[i] += dp[i - 2]

for i in range(3, MAX_LEN, 1):
    dp[i] += dp[i - 3]

for n in nums:
    print(dp[n])