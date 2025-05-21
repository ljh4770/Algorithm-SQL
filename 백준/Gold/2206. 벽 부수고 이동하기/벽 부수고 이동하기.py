from collections import deque

def bfs(graph, n, m):
    q = deque()
    q.append((0, 0, 0, 1))
    visited = [[[False] * m for _ in range(n)] for _ in range(2)]
    visited[0][0][0] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    end = (n - 1, m - 1)

    while q:
        x, y, w, dist = q.popleft()
        if (x, y) == end:
            return dist

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < n and 0 <= ny < m):
                continue

            if graph[nx][ny] == 0 and visited[w][nx][ny] == False:
                q.append((nx, ny, w, dist + 1))
                visited[w][nx][ny] = True
            elif graph[nx][ny] == 1 and w == 0 and visited[1][nx][ny] == False:
                q.append((nx, ny, 1, dist + 1))
                visited[1][nx][ny] = True
    return -1

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split(' '))

    map_ = [list(map(int, input().rstrip())) for _ in range(n)]

    min_dist = bfs(map_, n, m)
    print(min_dist)