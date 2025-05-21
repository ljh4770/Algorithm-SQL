import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split(' ')))
arr_reversed = arr[::-1]
dp_inc = [1] * n
dp_dec = [1] * n

for i in range(1, n, 1):
    for j in range(i):
        if arr[j] < arr[i]:
            dp_inc[i] = max(dp_inc[i], dp_inc[j] + 1)
        if arr_reversed[j] < arr_reversed[i]:
            dp_dec[i] = max(dp_dec[i], dp_dec[j] + 1)

dp_bitonic = [0] * n
for i in range(n):
    dp_bitonic[i] = dp_inc[i] + dp_dec[n - i - 1] - 1
print(max(dp_bitonic))