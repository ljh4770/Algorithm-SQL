from collections import deque

def bfs(graph, l, r, c, sl, sx, sy, end):
    q = deque()
    q.append((sl, sx, sy, 0))
    visited = [[[False] * c for _ in range(r)] for _ in range(l)]
    visited[sl][sx][sy] = True

    directions = [
        (1, 0, 0), (-1, 0, 0),
        (0, 1, 0), (0, -1, 0),
        (0, 0, 1), (0, 0, -1)
    ]

    while q:
        cl, cx, cy, dist = q.popleft()

        if (cl, cx, cy) == end:
            print(f"Escaped in {dist} minute(s).")
            return

        for dl, dx, dy in directions:
            nl, nx, ny = cl + dl, cx + dx, cy + dy

            if not (0 <= nl < l and 0 <= nx < r and 0 <= ny < c):
                continue

            if visited[nl][nx][ny]:
                continue

            if graph[nl][nx][ny] == '.':
                q.append((nl, nx, ny, dist + 1))
                visited[nl][nx][ny] = True
    
    print("Trapped!")
    return

def solve(l, r, c):
    # building = [[[''] * c for _ in range(r)] for _ in range(l)]
    building = []
    start = (0, 0, 0)
    end = (0, 0, 0)
    for i in range(l):
        floor = [list(input().rstrip()) for _ in range(r)]
        consume = input() # empty line

        for x in range(r):
            for y in range(c):
                if floor[x][y] == 'S':
                    start = (i, x, y)
                    floor[x][y] = '.'
                elif floor[x][y] == 'E':
                    end = (i, x, y)
                    floor[x][y] = '.'
        building.append(floor)

    sl, sx, sy = start[0], start[1], start[2]
    bfs(building, l, r, c, sl, sx, sy, end)


if __name__ == '__main__':
    import sys; input = sys.stdin.readline

    while True:
        l, r, c = map(int, input().split()) # l, r, c : [1, 30]
        if (l, r, c) == (0, 0, 0):
            break

        solve(l, r, c)