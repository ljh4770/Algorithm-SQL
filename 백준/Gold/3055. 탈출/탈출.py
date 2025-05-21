import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split(' '))
map_ = [list(input().rstrip()) for _ in range(r)]

start = tuple()
end = tuple()
water = []

for x in range(r):
    for y in range(c):
        if map_[x][y] == 'S':
            start = (x, y)
            map_[x][y] = '.'
        elif map_[x][y] == 'D':
            end = (x, y)
        elif map_[x][y] == '*':
            water.append((x, y))

q = deque()
q.append((start, 0))
visited = [[False] * c for _ in range(r)]
visited[start[0]][start[1]] = True

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
prev = -1

while q:
    (x, y), dist = q.popleft()
    
    if (x, y) == end:
        break
    
    # 물 영역 확장
    if prev != dist:
        water_next = []
        for i, j in water:
            for dx, dy in directions:
                ni, nj = i + dx, j + dy

                # 맵 밖인 경우, 이미 물인 경우
                if not (0 <= ni < r and 0 <= nj < c) or map_[ni][nj] == '*':
                    continue
                # 길인 경우 and 돌이거나 도착지점이 아닌 경우
                if map_[ni][nj] == '.' and map_[ni][nj] not in ['X', 'D']:
                    map_[ni][nj] = '*'
                    water_next.append((ni, nj))
            water = water_next
        prev = dist
    
    # 고슴도치 이동
    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        # 맵 밖으로 이동한 경우 or 물인 경우
        if not (0 <= nx < r and 0 <= ny < c) or map_[nx][ny] == '*':
            continue
        
        # 이동 가능한 칸인 경우, 방문하지 않은 경우
        if map_[nx][ny] in ['.', 'D'] and visited[nx][ny] == False:
            q.append(((nx, ny), dist + 1))
            visited[nx][ny] = True
else:
    dist = 'KAKTUS'

print(dist)