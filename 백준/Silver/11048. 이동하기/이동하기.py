import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))
maze = [list(map(int, input().split(' '))) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
dp[0][0] = maze[0][0]

for i in range(1, n):
    dp[i][0] = dp[i - 1][0] + maze[i][0]

for j in range(m):
    dp[0][j] = dp[0][j - 1] + maze[0][j]

for i in range(1, n, 1):
    for j in range(1, m, 1):
        dp[i][j] = max(
            dp[i - 1][j],
            dp[i][j - 1],
            dp[i - 1][j - 1]
        ) + maze[i][j]

print(dp[-1][-1])