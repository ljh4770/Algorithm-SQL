import sys
input = sys.stdin.readline

n = int(input())
data = [tuple(map(int, input().split(' '))) for _ in range(n)]
dp = [0 for _ in range(n + 2)]

for i in range(n, 0, -1):
    t = data[i - 1][0]
    p = data[i - 1][1]
    end_day = i + t - 1

    if end_day <= n:
        dp[i] = max(dp[i + 1], dp[end_day + 1] + p)
    else:
        dp[i] = dp[i + 1]

print(dp[1])