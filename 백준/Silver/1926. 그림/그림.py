from collections import deque

def bfs(graph, visited, n, m, x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    area = 0
    while q:
        x, y = q.popleft()
        area += 1

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                q.append((nx, ny))
                visited[nx][ny] = True
    return visited, area

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split(' '))
    image = [list(map(int, input().split(' '))) for _ in range(n)]

    visited = [[False] * m for _ in range(n)]
    cnt = 0
    max_area = 0

    for x in range(n):
        for y in range(m):
            if image[x][y] == 1 and visited[x][y] == False:
                visited, area = bfs(image, visited, n, m, x, y)
                cnt += 1
                max_area = max(max_area, area)
    print(cnt)
    print(max_area)