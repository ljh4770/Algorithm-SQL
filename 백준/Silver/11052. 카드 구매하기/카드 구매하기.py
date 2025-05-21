import sys
input = sys.stdin.readline

n = int(input())
values = list(map(int, input().split(' ')))
values = [0] + values
dp = [0] * (n + 1)

for i in range(1, n + 1, 1):
    for j in range(1, i + 1, 1):
        dp[i] = max(dp[i], values[j] + dp[i - j])
print(dp[n])