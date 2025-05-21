import sys
n = int(sys.stdin.readline())
dp = [[0] * 10 for _ in range(n + 1)]
dp[1] = [1] * 10
dp[1][0] = 0

for i in range(2, n + 1, 1):
    dp[i][0] = dp[i - 1][1]
    for num in range(1, 9, 1):
        dp[i][num] = dp[i - 1][num - 1] + dp[i - 1][num + 1]
    dp[i][9] = dp[i - 1][8]
print(sum(dp[n]) % (10 ** 9)) 