import sys; input = sys.stdin.readline
from collections import deque

n = int(input()) # Number of data structures
# 0: Queue, 1: Stack
ds = [*map(int, input().split(' '))]
# Initial elements for each data structure, one for each
elements = [*map(int, input().split(' '))]

m = int(input()) # Number of values to insert
targets = [*map(int, input().split(' '))] # Values to insert

# For Queues
# - Add to queue, making as a queue
# For Stack,
# - Skip the operations

# Return values for each target insertion
res = deque()
for i in range(n):
    d = ds[i]
    if d == 1: # Stack
        continue
    # Queue
    t = elements[i]
    res.appendleft(t)
for i in range(m):
    res.append(targets[i])
    print(res.popleft(), end=' ')