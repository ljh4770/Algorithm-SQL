import sys
input = sys.stdin.readline

n, k = map(int, input().split(' '))
coins = [int(input()) for _ in range(n)]
dp = [float('inf')] * (k + 1)

for coin in coins:
    if coin <= k:
        dp[coin] = 1

for i in range(1, k + 1, 1):
    for coin in coins:
        if i > coin and dp[i] > dp[i - coin] + 1:
            dp[i] = dp[i - coin] + 1
if dp[k] == float('inf'):
    print(-1)
else:
    print(dp[k])