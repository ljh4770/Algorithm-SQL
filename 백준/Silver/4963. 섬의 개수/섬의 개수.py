from collections import deque

def bfs(graph, visited, w, h, x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < h and 0 <= ny < w):
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                q.append((nx, ny))
                visited[nx][ny] = True

    return visited

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    while True:
        w, h = map(int, input().split(' '))
        if w == 0 and h == 0:
            break
        map_ = [list(map(int, input().split(' ')))for _ in range(h)]

        visited = [[False] * w for _ in range(h)]
        cnt = 0
        for x in range(h):
            for y in range(w):
                if map_[x][y] == 1 and visited[x][y] == False:
                    visited = bfs(map_, visited, w, h, x, y)
                    cnt += 1
        print(cnt)