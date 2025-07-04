import sys; input = sys.stdin.readline
from bisect import bisect_left

n = int(input())
arr = [0] + [*map(int, input().split(' '))]
LIS_list = [-float("inf")]
LIS_value = [1] * (n + 1)

for idx in range(1, n + 1):
    if LIS_list[-1] < arr[idx]: # 증가하는 경우
        LIS_list.append(arr[idx])
        LIS_value[idx] = len(LIS_list) - 1
    else: # 감소/같은 경우
        move = bisect_left(LIS_list, arr[idx])
        LIS_list[move] = arr[idx]
        LIS_value[idx] = move

order_top = len(LIS_list) - 1
print(order_top)

# 역추적
result = []
for idx in range(n, 0, -1):
    if LIS_value[idx] == order_top:
        result.append(arr[idx])
        order_top -= 1

print(*result[::-1])