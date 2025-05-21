from collections import deque

def bfs(graph, visited, n, m, x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    area = 1

    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < n and 0 <= ny < m):
                continue

            if graph[nx][ny] == 0 and visited[nx][ny] == False:
                q.append((nx, ny))
                visited[nx][ny] = True
                area += 1

    return visited, area

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    m, n, k = map(int, input().split(' '))
    cords = [tuple(map(int, input().split(' '))) for _ in range(k)]

    paper = [[0] * m for _ in range(n)]

    for a, b, x, y in cords:
        for i in range(a, x, 1):
            for j in range(b, y, 1):
                paper[i][j] = 1
    
    visited = [[False] * m for _ in range(n)]
    areas = []
    for x in range(n):
        for y in range(m):
            if paper[x][y] == 0 and visited[x][y] == False:
                visited, area = bfs(paper, visited, n, m, x, y)
                areas.append(area)

    areas.sort()

    print(len(areas))
    for area in areas:
        print(area, end=' ')