import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))
memory = [0] + [*map(int, input().split(' '))]
cost = [0] + [*map(int, input().split(' '))]
sum_cost = sum(cost)
dp = [[0] * (sum_cost + 1) for _ in range(n + 1)]

if m == 0:
    print(0)
    sys.exit()

result = sum_cost
for i in range(1, n + 1, 1):
    mem = memory[i]
    c = cost[i]

    for j in range(1, sum_cost + 1, 1):
        dp[i][j] = dp[i-1][j]
    for j in range(c, sum_cost + 1, 1):
        dp[i][j] = max(dp[i - 1][j - c] + mem, dp[i - 1][j])
        
        if dp[i][j] >= m:
            result = min(result, j)

print(result)