import sys
n = int(input())
arr = [int(input()) for _ in range(n)]

if n in [1, 2]:
    print(sum(arr))
    exit(0)
if n == 3:
    max_ = max(
        arr[0] + arr[2],
        arr[0] + arr[1],
        arr[1] + arr[2]
    )
    print(max_)
    exit(0)
# if n == 4:
#     max_ = max(
#             arr[0] + arr[1] + arr[3],
#             arr[0] + arr[2] + arr[3]
#     )
#     print(max_)
#     exit(0)

dp = [0] * n
dp[0] = arr[0]
dp[1] = arr[0] + arr[1]
dp[2] = max(
    arr[0] + arr[2],
    arr[1] + arr[2]
)
dp[3] = max(
    arr[0] + arr[1] + arr[3],
    arr[0] + arr[2] + arr[3]
)

for i in range(4, n, 1):
    dp[i] = max(
        dp[i - 2],
        dp[i - 3] + arr[i - 1],
        dp[i - 4] + arr[i - 1]
    )
    dp[i] += arr[i]
print(max(dp))