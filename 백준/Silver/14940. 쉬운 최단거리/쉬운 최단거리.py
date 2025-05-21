import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split(' '))
map_ = [list(map(int, input().split(' '))) for _ in range(n)]

for x in range(n):
    for y in range(m):
        if map_[x][y] == 2:
            start = (x, y)

q = deque()
q.append((start[0], start[1], 0))
visited = [[False] * m for _ in range(n)]
visited[start[0]][start[1]] = True

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while q:
    x, y, dist = q.popleft()
    
    map_[x][y] = dist

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if not (0 <= nx < n and 0 <= ny < m):
            continue

        if map_[nx][ny] == 1 and visited[nx][ny] == False:
            q.append((nx, ny, dist + 1))
            visited[nx][ny] = True

for x in range(n):
    for y in range(m):
        if visited[x][y] == False and map_[x][y] != 0:
            map_[x][y] = -1

for row in map_:
    for item in row:
        print(item, end=' ')
    print()