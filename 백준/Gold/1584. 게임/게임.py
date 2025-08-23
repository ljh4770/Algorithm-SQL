from collections import deque

SIZE = 501

def bfs(graph):
    q = deque()
    q.append((0, 0, 0))
    visited = [[False] * SIZE for _ in range(SIZE)]
    visited[0][0] = True

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while q:
        x, y, d = q.popleft()

        if (x, y) == (500, 500):
            return d

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < SIZE and 0 <= ny < SIZE):
                continue
            if visited[nx][ny] == True:
                continue

            zone = graph[nx][ny]
            if zone == 0: # ok
                q.appendleft((nx, ny, d))
            elif zone == 1: # life - 1
                q.append((nx, ny, d + 1))
            visited[nx][ny] = True
    return -1

if __name__ == '__main__':
    import sys; input = sys.stdin.readline

    board = [[0] * SIZE for _ in range(SIZE)]

    n = int(input())
    danger = [tuple(map(int, input().split())) for _ in range(n)]
    m = int(input())
    death = [tuple(map(int, input().split())) for _ in range(m)]

    for x1, y1, x2, y2 in danger:
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        for r in range(x1, x2 + 1, 1):
            for c in range(y1, y2 + 1, 1):
                board[r][c] = 1

    for x1, y1, x2, y2 in death:
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        for r in range(x1, x2 + 1, 1):
            for c in range(y1, y2 + 1, 1):
                board[r][c] = 2
    print(bfs(board))