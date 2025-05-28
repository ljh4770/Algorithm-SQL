import sys
input = sys.stdin.readline

n = int(input())
arr = [*map(int, input().split(' '))]

dp = [1] * n

for i in range(1, n, 1):
    for j in range(0, i, 1):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

answer = []
max_len = max(dp)

for i in range(n - 1, -1, -1):
    if dp[i] == max_len:
        answer.append(arr[i])
        max_len -= 1

print(*answer[::-1])