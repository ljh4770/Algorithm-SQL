import sys
input = sys.stdin.readline

k = int(input().strip()) # k : [1, 20]
# weight : [1, 1000]
edges = list(map(int, input().split()))

# max value(cum sum) between left & right edge
dp = [0] * (1 << (k + 1))
for i, w in enumerate(edges, start=2):
    dp[i] = w

answer = 0 # difference from start point to end point
for i in range((1 << k) - 1, 0, -1):
    left  = dp[i * 2]
    right = dp[i * 2 + 1]

    diff = abs(left - right)
    answer += diff

    dp[i] += max(left, right)

print(sum(edges) + answer)