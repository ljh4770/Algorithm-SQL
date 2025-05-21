from collections import deque

def oob(x, y, n, m):
    return not(0 <= x < n and 0 <= y < m)

def bfs(graph, visited, x, y, n, m):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    dxdy = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    while q:
        x, y = q.popleft()

        for dx, dy in dxdy:
            nx, ny = x + dx, y + dy

            if oob(nx, ny, n, m) == True:
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                q.append((nx, ny))
                visited[nx][ny] = True

    return visited

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        m, n, k = map(int, input().split(' '))
        data = [tuple(map(int, input().split(' '))) for _ in range(k)]

        farm = [[0] * m for _ in range(n)]
        for a, b in data:
            farm[b][a] = 1
    
        visited = [[False] * m for _ in range(n)]
        cnt = 0
        for x in range(n):
            for y in range(m):
                if visited[x][y] == False and farm[x][y] == 1:
                    visited = bfs(farm, visited, x, y, n, m)
                    cnt += 1

        print(cnt)

    