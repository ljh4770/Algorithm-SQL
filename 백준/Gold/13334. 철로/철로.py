import sys; input = sys.stdin.readline
from heapq import heappush, heappop

n = int(input()) # n : [1, 10 ** 5]
positions = [tuple(map(int, input().split(' '))) for _ in range(n)]
d = int(input()) # d: [1, 2 * 10 ** 8]

# Remove people whose lengths is greater than the d
positions = [(a, b) for a, b in positions if abs(a - b) <= d]
positions = [(min(a, b), max(a, b)) for a, b in positions]
positions.sort(key=lambda x: (x[1], x[0])) 

heap = [] # people who are on the rail
cnt = 0 # number of them

for start, end in positions:
    heappush(heap, start)
    # Temporary start point of the rail
    # when the end of rail is equal to current person's end
    line_start = end - d

    # heap[0] : minimum start value in the heap
    while heap and (heap[0] < line_start):
        # out of the rail -> remove
        heappop(heap) # pop the minimal start value
    cnt = max(cnt, len(heap))

print(cnt)