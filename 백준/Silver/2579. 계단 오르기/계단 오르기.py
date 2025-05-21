import sys

input = sys.stdin.readline

n = int(input())
data = [int(input()) for _ in range(n)]

if n == 1:
    print(data[0])
elif n == 2:
    print(data[0] + data[1])
else:
    dp = [0] * n
    dp[0] = data[0]
    dp[1] = data[0] + data[1]
    dp[2] = max(data[0] + data[2], data[1] + data[2])

    for i in range(3, n):
        dp[i] = max(dp[i - 2] + data[i], dp[i - 3] + data[i - 1] + data[i])

    print(dp[n - 1])