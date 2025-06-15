import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
arr = ''
for c in input().split(' '):
    arr += str(int(c) - 1)
m = int(input())
ops = [(tuple(map(int, input().split(' ')))) for _ in range(m)]

hq = [(0, arr)] # Treat each array as a node.
dist = {arr: 0} # Dictionary to store the minimum distance to each node.

while hq: # Dijkstra's algorithm
    d, cur = heappop(hq)
    if dist[cur] < d:
        # If the current distance is greater than the recorded distance, skip it.
        continue

    for l, r, c in ops:
        # Next state after applying the operation.
        nxt = cur[:l - 1] + cur[r - 1] + cur[l:r - 1] + cur[l - 1] + cur[r:]
        if (nxt not in dist) or (dist[nxt] > d + c):
            dist[nxt] = d + c
            heappush(hq, (d + c, nxt))

# Sorted array
res = ''.join(sorted(arr))
if res not in dist.keys():
    # Cannot reach the sorted array.
    print(-1)
else:
    # Print the minimum distance to reach the sorted array.
    print(dist[res])