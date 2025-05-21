import sys
input = sys.stdin.readline

n = int(input())
lines = [tuple(map(int, input().split(' '))) for _ in range(n)]
dp = [1] * n 

lines.sort(key=lambda x: x[0])

for i in range(1, n, 1):
    for j in range(0, i, 1):
        if lines[j][1] < lines[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))