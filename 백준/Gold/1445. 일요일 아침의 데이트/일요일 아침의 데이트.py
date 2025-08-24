from heapq import heappush, heappop
INF = float('inf')
BASE = 50 * 50 + 1

def dijkstra(sx, sy, ex, ey):
    global n, m
    hq = []
    heappush(hq, (0, sx, sy))
    # matrix for check cost
    distance = [[INF] * m for _ in range(n)]
    distance[sx][sy] = 0

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while hq:
        garbage, x, y = heappop(hq)

        if (x, y) == (ex, ey):
            # end condition
            return garbage
        
        if distance[x][y] < garbage:
            # do not need to check
            continue

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if not(0 <= nx < n and 0 <= ny < m):
                continue
            
            weight = 0 # problem condition
            if forest[nx][ny] == 'g':
                weight = BASE
            elif forest[nx][ny] == '.':
                for ddx, ddy in directions:
                    cx, cy = nx + ddx, ny + ddy
                    if not(0 <= cx < n and 0 <= cy < m):
                        continue
                    if forest[cx][cy] == 'g':
                        weight = 1
                        break
            if garbage + weight < distance[nx][ny]:
                distance[nx][ny] = garbage + weight
                heappush(hq, (distance[nx][ny], nx, ny))


if __name__ == '__main__':
    import sys; input = sys.stdin.readline

    # n, m : [3, 50]
    n, m = map(int, input().split())
    forest = [input().rstrip() for _ in range(n)]
    # S - start / F - end / g - garbage / . - clean

    # Find start and end point
    start, end = None, None
    for r in range(n):
        for c in range(m):
            if start and end:
                break
            if forest[r][c] == 'S':
                start = (r, c)
            elif forest[r][c] == 'F':
                end = (r, c)

    # sssp with garbage weight
    garbage = dijkstra(start[0], start[1], end[0], end[1])
    # cost = BASE * (through garbage cell) + 1 * (adjacent garbage cell)
    q, r = divmod(garbage, BASE) 
    print(q, r)