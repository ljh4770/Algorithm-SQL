from collections import deque


def bfs(graph, sx, sy, sym, visited):
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = True

    directions = {
        '-': {(0, 1), (0, -1)},
        '|': {(1, 0), (-1, 0)},
    }

    while q:
        x, y = q.popleft()

        for dx, dy in directions[sym]:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < N and 0 <= ny < M):
                continue
            
            if visited[nx][ny]:
                continue

            if graph[nx][ny] == sym:
                q.append((nx, ny))
                visited[nx][ny] = True


if __name__ == "__main__":
    import sys; input = sys.stdin.readline


    N, M = map(int, input().split())
    room = [input().rstrip() for _ in range(N)]

    cnt = 0
    visited = [[False] * M for _ in range(N)]
    for x in range(N):
        for y in range(M):
            if visited[x][y]:
                continue
            cnt += 1
            sym = room[x][y]        
            bfs(room, x, y, sym, visited)

    print(cnt)
