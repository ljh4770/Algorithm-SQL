import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split(' '))
positions = list(map(int, input().split(' ')))
positions = [x - 1 for x in positions]
dq = deque([i for i in range(0, N, 1)])

cnt = 0
amt = 0
for pos in positions:
    m = len(dq) // 2
    idx = dq.index(pos)
    if idx <= m:
        amt = -idx
    else:
        amt = len(dq) - idx
    dq.rotate(amt)
    dq.popleft()
    cnt += abs(amt)
    
print(cnt)

