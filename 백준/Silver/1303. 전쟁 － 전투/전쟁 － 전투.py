import sys
from collections import deque

def bfs(sx, sy, side):
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = True

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    cnt = 1
    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if visited[nx][ny]:
                continue

            if graph[nx][ny] == side:
                q.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1

    return cnt

if __name__ == '__main__':
    input = sys.stdin.readline

    m, n = map(int, input().split())
    graph = [input().rstrip() for _ in range(n)]


    visited = [[False] * m for _ in range(n)]

    white_power = 0
    black_power = 0
    for r in range(n):
        for c in range(m):
            if not visited[r][c]:
                cnt = bfs(r, c, graph[r][c])
                if graph[r][c] == 'W':
                    white_power += cnt ** 2
                else:
                    black_power += cnt ** 2

    print(white_power, black_power)