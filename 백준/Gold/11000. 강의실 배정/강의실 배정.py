import sys; input = sys.stdin.readline
from heapq import heappop, heappush

n = int(input())
lectures = [tuple(map(int, input().split())) for _ in range(n)]
lectures.sort()

hq = []
heappush(hq, lectures[0][1])

for start, end in lectures[1:]:
    if start >= hq[0]:
        heappop(hq)
    
    heappush(hq, end)

print(len(hq))