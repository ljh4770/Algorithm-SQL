import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))
table = [list(map(int, input().split(' '))) for _ in range(n)]
query = [tuple(map(int, input().split(' '))) for _ in range(m)]

dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[1][1] = table[0][0]

for i in range(2, n + 1, 1):
    dp[1][i] = dp[1][i - 1] + table[0][i - 1]
    dp[i][1] = dp[i - 1][1] + table[i - 1][0]

for x in range(1, n + 1, 1):
    for y in range(1, n + 1, 1):
        dp[x][y] = table[x - 1][y - 1] + dp[x - 1][y] + dp[x][y - 1] - dp[x - 1][y - 1]

for x1, y1, x2, y2 in query:
    print(
        dp[x2][y2]
        - dp[x2][y1 - 1]
        - dp[x1 - 1][y2]
        + dp[x1 - 1][y1 - 1]
    )