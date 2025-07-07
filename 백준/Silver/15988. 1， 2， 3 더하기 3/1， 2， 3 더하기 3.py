import sys; input = sys.stdin.readline

MOD = 10 ** 9 + 9

t = int(input())
ns = [int(input()) for _ in range(t)]
max_ = max(ns)

dp = [0] * (max_ + 1)
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, max_ + 1, 1):
    dp[i] += (dp[i - 1] + dp[i - 2] + dp[i - 3]) % MOD

for n in ns:
    print(dp[n])