import sys; input = sys.stdin.readline

n = int(input()) # n : [1, 1000]
# p : [1, 10000]
p_arr = [0] + [*map(int, input().split(' '))]

dp = p_arr.copy()

for i in range(2, n + 1, 1):
    for j in range(1, i, 1):
        dp[i] = min(dp[i], dp[i - j] + p_arr[j])

print(dp[n])