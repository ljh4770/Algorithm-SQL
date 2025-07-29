import sys
from collections import deque


def bfs():
    global k, w, h, map_

    q = deque()
    visited = [[[False] * w for _ in range(h)] for _ in range(k + 1)]
    
    q.append((0, 0, 0, 0)) # (x, y, jump count, distance)
    visited[0][0][0] = True

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    jump_directions = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]

    while q:
        x, y, j, d = q.popleft()

        if (x, y) == (h - 1, w - 1):
            return d

        if j < k:
            for dx, dy in jump_directions:
                nx, ny = x + dx, y + dy
                
                if not (0 <= nx < h and 0 <= ny < w):
                    continue

                if map_[nx][ny] == 1 or visited[j + 1][nx][ny]:
                    continue

                # jumpable cell
                visited[j + 1][nx][ny] = True
                q.append((nx, ny, j + 1, d + 1))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if not (0 <= nx < h and 0 <= ny < w):
                continue

            if map_[nx][ny] == 1 or visited[j][nx][ny]:
                continue

            # movable cell
            visited[j][nx][ny] = True
            q.append((nx, ny, j, d + 1))

    return -1


if __name__ == "__main__":
    input = sys.stdin.readline
    
    k = int(input())
    w, h = map(int, input().split())
    map_ = [list(map(int, input().split())) for _ in range(h)]

    print(bfs())