import sys; input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [[*map(int, input().rstrip())] for _ in range(n)]

dp = [[0] * m for _ in range(n)]

max_len = 0
for r in range(n):
    for c in range(m):
        if 0 in (r, c):
            dp[r][c] = matrix[r][c]
        elif matrix[r][c] == 0:
            dp[r][c] = 0
        else:
            dp[r][c] = min(dp[r - 1][c - 1], dp[r - 1][c], dp[r][c - 1]) + 1

        max_len = max(max_len, dp[r][c])

print(max_len ** 2)