from collections import deque


def bfs(graph, n, m, fires, sg, visited):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    time = 0
    while sg:
        time += 1

        # Fire first
        while fires and fires[0][2] < time:
            x, y, t = fires.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < n and 0 <= ny < m):
                    continue

                if graph[nx][ny] in ('@', '.'):
                    graph[nx][ny] = '*'
                    fires.append((nx, ny, t + 1))
        
        # Sanggeun
        while sg and sg[0][2] < time:
            x, y, t = sg.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < n and 0 <= ny < m):
                    return time
                
                if visited[nx][ny]:
                    continue

                if graph[nx][ny] == '.':
                    visited[nx][ny] = True
                    sg.append((nx, ny, t + 1))
    
    return "IMPOSSIBLE"

def solve(m, n, graph):
    sg = deque()
    fires = deque()

    visited = [[False] * m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if graph[x][y] == '@':
                sg.append((x, y, 0))
                visited[x][y] = True
            elif graph[x][y] == '*':
                fires.append((x, y, 0))

    print(bfs(graph, n, m, fires, sg, visited))


if __name__ == "__main__":
    import sys; input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        w, h = map(int, input().split())
        building = [list(input().rstrip()) for _ in range(h)]
        solve(w, h, building)