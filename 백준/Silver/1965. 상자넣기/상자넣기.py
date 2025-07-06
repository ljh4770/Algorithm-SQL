import sys; input = sys.stdin.readline
from bisect import bisect_left

n = int(input())
boxes = [*map(int, input().split(' '))]
LIS = [boxes[0]]

for i in range(1, n, 1):
    box = boxes[i]
    if box > LIS[-1]:
        LIS.append(box)
    else:
        idx = bisect_left(LIS, box)
        LIS[idx] = box

print(len(LIS))