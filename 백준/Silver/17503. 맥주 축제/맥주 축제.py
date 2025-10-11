import sys; input = sys.stdin.readline
from heapq import heappush, heappop

n, m, k = map(int, input().split())
beers = [tuple(map(int, input().split())) for _ in range(k)]
beers.sort(key=lambda x: (x[1], -x[0]))

hq = []
answer = -1
total_pref = 0

for pref, alco in beers:
    heappush(hq, pref)
    total_pref += pref

    if len(hq) > n:
        lowest_pref = heappop(hq)
        total_pref -= lowest_pref

    if len(hq) == n and total_pref >= m:
        answer = alco
        break

print(answer)