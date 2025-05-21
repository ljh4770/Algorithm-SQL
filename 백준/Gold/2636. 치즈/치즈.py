import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split(' '))
cheese = [list(map(int, input().split(' '))) for _ in range(r)]

# 처음 치즈 개수 파악
num_cheese = 0
last_cheese = 0
for i in range(r):
    num_cheese += sum(cheese[i])

if num_cheese == 0:
    print(0)
    print(0)
    sys.exit(0)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
time = 0

# 치즈가 다 녹을 때까지 반복
while num_cheese > 0:
    last_cheese = num_cheese
    q = deque()
    q.append((0, 0)) # 주어진 행렬의 가장자리는 치즈가 아니라는 것이 보장
    visited = [[False] * c for _ in range(r)]
    visited[0][0] = True

    targets = []

    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < r and 0 <= ny < c) or visited[nx][ny] == True:
                continue
            
            # 공기
            if cheese[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = True
            # 녹일 치즈 좌표
            elif cheese[nx][ny] == 1:
                targets.append((nx, ny))
                visited[nx][ny] = True
    # 치즈 녹이기
    for x, y in targets:
        cheese[x][y] = 0
    num_cheese -= len(targets)
    time += 1
print(time)
print(last_cheese)