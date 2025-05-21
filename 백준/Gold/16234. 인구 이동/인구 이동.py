from collections import deque

def bfs(graph, n, x, y, l, r):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    pop_tot = 0
    cnt = 0
    countries = [(x, y)]

    while q:
        x, y = q.popleft()
        pop_tot += graph[x][y]
        cnt += 1

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < n and 0 <= ny < n):
                continue

            if l <= abs(graph[x][y] - graph[nx][ny]) <= r and visited[nx][ny] == False:
                q.append((nx, ny))
                visited[nx][ny] = True
                countries.append((nx, ny))

    return countries, visited, pop_tot // cnt

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n, l ,r = map(int, input().split(' '))
    counts = [list(map(int, input().split(' '))) for _ in range(n)]


    for cnt in range(0, 2000 + 1, 1):
        change = []
        visited = [[False] * n for _ in range(n)]
        for x in range(n):
            for y in range(n):
                if visited[x][y] == False:
                    countries, visited, pop_next = bfs(counts, n, x, y, l, r)
                    change.append((countries, pop_next))
        moved = False
        for countreis, pop_next in change:
            if len(countreis) > 1:
                moved = True
                for x, y in countreis:
                    counts[x][y] = pop_next
        if moved == False:
            break
        
    print(cnt)