import sys
n = int(sys.stdin.readline())
if n == 1:
    print(1)
    exit(0)
dp = [0] * n
dp[0] = 1
dp[1] = 3

for i in range(2, n, 1):
    dp[i] = 2 * dp[i - 2] + dp[i - 1]
print(dp[-1] % 10007)