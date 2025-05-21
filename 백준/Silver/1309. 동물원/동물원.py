import sys
n = int(sys.stdin.readline())
MOD = 9901
dp = [0 for _ in range(n + 1)]

if n == 1:
    print(3)
    sys.exit(0)

dp[1] = 3
dp[2] = 7
for i in range(3, n + 1):
    dp[i] = (2 * dp[i - 1] + dp[i - 2]) % MOD

print(dp[n])
