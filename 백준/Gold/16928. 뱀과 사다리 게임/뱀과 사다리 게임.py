import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split(' ')) # n: 사다리 개수, m: 뱀 개수
ladders = [-1] * (100 + 1)
snakes = [-1] * (100 + 1)

for i in range(n):
    x, y = map(int, input().split(' '))
    ladders[x] = y

for i in range(m):
    u, v = map(int, input().split(' '))
    snakes[u] = v

visited = [False] * (100 + 1)
visited[1] = True

q = deque()
q.append((1, 0))

dice = [1, 2, 3, 4, 5, 6]

while q:
    cur, dist = q.popleft()
    if cur == 100:
        break

    for d in dice:
        next = cur + d

        if next > 100 or visited[next] == True:
            continue
        
        if ladders[next] != -1:
            visited[ladders[next]] = True
            q.append((ladders[next], dist + 1))
        elif snakes[next] != -1:
            visited[snakes[next]] = True
            q.append((snakes[next], dist + 1))
        else:
            visited[next] = True
            q.append((next, dist + 1))

print(dist)