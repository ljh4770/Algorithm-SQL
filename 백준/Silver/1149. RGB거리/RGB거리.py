import sys

input = sys.stdin.readline

N = int(input())
costs = [list(map(int, input().strip().split(' '))) for _ in range(N)]
dp = [[0] * 3 for _ in range(N)]
dp[0] = costs[0]

for i in range(1, N, 1):
    dp[i][0] = costs[i][0] + min(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] = costs[i][1] + min(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] = costs[i][2] + min(dp[i - 1][0], dp[i - 1][1])

print(min(dp[N - 1]))
