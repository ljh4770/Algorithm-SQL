n = int(input())

if n <= 3:
    match n:
        case 1:
            print(0)
        case 2:
            print(1)
        case 3:
            print(2)
    exit(0)

dp = [0] * (n + 1)

dp[1] = 0
dp[2] = 1
dp[3] = 2

MOD = 10 ** 9

for i in range(4, n + 1, 1):
    dp[i] = (i - 1) * (dp[i - 2] + dp[i - 1]) % MOD

print(dp[n])