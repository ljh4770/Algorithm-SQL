import sys; input = sys.stdin.readline
from heapq import heapify, heappush, heappop

n = int(input())
hq = []

header = [*map(int, input().split())]
for num in header:
    heappush(hq, num)

for _ in range(n - 1):
    row = [*map(int, input().split())]
    for num in row:
        if hq[0] < num:
            heappush(hq, num)
            heappop(hq)

print(hq[0])