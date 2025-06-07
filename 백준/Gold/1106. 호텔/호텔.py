import sys
input = sys.stdin.readline

c, n = map(int, input().split(' '))
costs = [0]
effects = [0]
for _ in range(n):
    a, b = map(int, input().split(' '))
    costs.append(a)
    effects.append(b)
dp = [float('inf')] * (c + 100)
dp[0] = 0

for i in range(1, n + 1):
    cost = costs[i]
    effect = effects[i]
    for j in range(effect, c + 100):
        dp[j] = min(
            dp[j],
            dp[j - effect] + cost
        )

print(min(dp[c:]))