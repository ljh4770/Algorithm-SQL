from collections import deque

def oob(x, y, n, m):
    return not(0 <= x < n and 0 <= y < m)

def multi_src_bfs(graph, starts, n, m):
    q = deque()
    for x, y in starts:
        q.append((x, y, 0))
    
    dxdy = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    
    max_day = 0

    while q:
        x, y, dist = q.popleft()
        max_day = max(max_day, dist)

        for dx, dy in dxdy:
            nx, ny = x + dx, y + dy

            if oob(nx, ny, n, m) == True:
                continue
                
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                q.append((nx, ny, dist + 1))

    return graph, max_day

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    m, n = map(int, input().split(' '))
    box = [list(map(int, input().rstrip().split(' '))) for _ in range(n)]
    starts = []

    for x in range(n):
        for y in range(m):
            if box[x][y] == 1:
                box[x][y] = 1
                starts.append((x, y))

    box, max_day = multi_src_bfs(box, starts, n, m)

    for x in range(n):
        for y in range(m):
            if box[x][y] == 0:
                print(-1)
                exit(0)

    print(max_day)