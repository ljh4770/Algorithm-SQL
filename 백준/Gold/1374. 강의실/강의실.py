import sys; input = sys.stdin.readline
from heapq import heappush, heappop


N = int(input())
lectures = [tuple(map(int, input().split())) for _ in range(N)]
lectures.sort(key=lambda x: x[1])

mh = []
cnt = 0
for lecture in lectures:
    while mh and mh[0] <= lecture[1]:
        heappop(mh)
    heappush(mh, lecture[2])
    cnt = max(cnt, len(mh))

print(cnt)