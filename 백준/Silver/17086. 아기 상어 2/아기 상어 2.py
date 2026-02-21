import sys; input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(N)]

q = deque()
dist = [[-1] * M for _ in range(N)]
directions = [
    (0, 1), (0, -1), (1, 0), (-1, 0),
    (1, 1), (1, -1), (-1, 1), (-1, -1)
]

for x in range(N):
    for y in range(M):
        if board[x][y] == 1:
            q.append((x, y))
            dist[x][y] = 0

answer = 0
while q:
    x, y = q.popleft()
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if not (0 <= nx < N and 0 <= ny < M):
            continue

        if dist[nx][ny] == -1:
            q.append((nx, ny))
            dist[nx][ny] = dist[x][y] + 1
            answer = max(answer, dist[nx][ny])

print(answer)
