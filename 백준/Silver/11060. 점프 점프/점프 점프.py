import sys; input = sys.stdin.readline

n = int(input()) # n : [1, 1000]
arr = [*map(int, input().split())] # a : [0, 100]

INF = float('inf')
dp = [INF] * n
dp[0] = 0

for i in range(n):
    v = arr[i]
    for j in range(1, v + 1, 1):
        if i + j < n:
            dp[i + j] = min(dp[i + j], dp[i] + 1)

if dp[n - 1] == INF:
    print(-1)
else:
    print(dp[n - 1])