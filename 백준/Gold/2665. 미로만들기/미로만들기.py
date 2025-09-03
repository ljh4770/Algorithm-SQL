from heapq import heappush, heappop

def dijkstra(graph, n):
    q = []
    q.append((0, 0, 0))
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while q:
        chg, x, y = heappop(q)

        if (x, y) == (n - 1, n - 1):
            return chg

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if not (0 <= nx <n and 0 <= ny < n):
                continue

            if visited[nx][ny]:
                continue

            if graph[nx][ny] == 0:
                heappush(q, (chg + 1, nx, ny))
            else:
                heappush(q, (chg, nx, ny))
            visited[nx][ny] = True


if __name__ == '__main__':
    import sys; input = sys.stdin.readline

    n = int(input())
    maze = [list(map(int, input().rstrip())) for _ in range(n)]

    print(dijkstra(maze, n))