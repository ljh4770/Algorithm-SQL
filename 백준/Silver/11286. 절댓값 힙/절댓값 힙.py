import sys
import heapq

input = sys.stdin.readline

N = int(input())
data = [int(input()) for _ in range(N)]

left = []
right = []

for num in data:
    if num != 0:
        if num < 0:
            heapq.heappush(left, -num)
        else:
            heapq.heappush(right, num)

    elif len(left) != 0 and len(right) != 0:
        if left[0] <= right[0]:
            print(heapq.heappop(left) * (-1))
        else:
            print(heapq.heappop(right))
    elif len(left) != 0:
        print(heapq.heappop(left) * (-1))
    elif len(right) != 0:
        print(heapq.heappop(right))
    else:
        print(0)
