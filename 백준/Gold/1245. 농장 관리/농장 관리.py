import sys
from collections import deque


def bfs(sx, sy):
    global n, m
    global heights, visited, directions

    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = True

    sh = heights[sx][sy]
    is_peak = True
    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < n and 0 <= ny < m):
                continue
            
            nh = heights[nx][ny]

            if nh > sh:
                is_peak = False

            elif nh == sh and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

    return is_peak


if __name__ == "__main__":
    input = sys.stdin.readline

    n, m = map(int, input().split())
    heights = [[*map(int, input().split())] for _ in range(n)]

    visited = [[False] * m for _ in range(n)]    
    directions = [
        (1, 0), (-1, 0), (0, 1), (0, -1),
        (1, 1), (-1, 1), (1, -1), (-1, -1)
    ]

    peak_count = 0
    for x in range(n):
        for y in range(m):
            if not visited[x][y]:
                if bfs(x, y):
                    peak_count += 1
                    
    print(peak_count)