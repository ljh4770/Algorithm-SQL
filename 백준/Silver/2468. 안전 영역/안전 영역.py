from collections import deque

def bfs(graph, visited, n, x, y, h):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if not(0 <= nx < n and 0 <= ny < n):
                continue
            if graph[nx][ny] > h and visited[nx][ny] == False:
                q.append((nx, ny))
                visited[nx][ny] = True
    
    return visited

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n = int(input())
    map_ = [list(map(int, input().split(' '))) for _ in range(n)]

    max_ = 1
    for h in range(1, 100 + 1, 1):
        visited = [[False] * n for _ in range(n)]
        cnt = 0
        for x in range(n):
            for y in range(n):
                if map_[x][y] > h and visited[x][y] == False:
                    visited = bfs(map_, visited, n, x, y, h)
                    cnt += 1

        max_ = max(max_, cnt)
        if cnt == 0:
            break

    print(max_)