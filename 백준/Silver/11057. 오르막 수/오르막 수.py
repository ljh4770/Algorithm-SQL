import sys

n = int(sys.stdin.readline())
dp = [[0] * 10 for _ in range(n + 1)]
dp[1] = [1] * 10
mod = 10007

for i in range(2, n + 1, 1):
    dp[i][0] = 1
    for j in range(1, 10, 1):
        dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % mod
print(sum(dp[n]) % mod)