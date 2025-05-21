import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split(' '))
q = deque()
q.append((n, 0))
visited = [False] * 100001
time = 0

choices = [
    lambda x: x - 1,
    lambda x: x + 1,
    lambda x: x * 2
]

while q:
    v, t = q.popleft()

    if v == k:
        time = t
        break

    for func in choices:
        nv = func(v)

        if not (0 <= nv <= 100000):
            continue
        if visited[nv] == False:
            visited[nv] = True
            q.append((nv, t + 1))

print(time)