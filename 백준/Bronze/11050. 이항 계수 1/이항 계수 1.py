import sys
input = sys.stdin.readline

n, k = map(int, input().split(' '))

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1, 1):
    dp[i][i] = 1
    dp[1][i] = i

for i in range(2, n + 1, 1):
    for j in range(i, n + 1, 1):
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]

if k == 0:
    print(1)
else:
    print(dp[k][n])