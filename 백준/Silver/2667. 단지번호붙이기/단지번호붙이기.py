from collections import deque

def oob(x, y, n):
    return not (0 <= x < n and 0 <= y < n)

def bfs(graph, visited, n, start):
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = True

    cnt = 0
    dxdy = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]
    
    while q:
        x, y = q.popleft()

        cnt += 1
        for dx, dy in dxdy:
            nx, ny = x + dx, y + dy

            if oob(nx, ny, n) == True:
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                q.append((nx, ny))
                visited[nx][ny] = True

    return visited, cnt


if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n = int(input())
    map_ = [list(map(int, input().rstrip())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    cnt = []

    for x in range(0, n, 1):
        for y in range(0, n, 1):
            if visited[x][y] == False and map_[x][y] == 1:
                start = (x, y)
                visited, tmp_cnt = bfs(map_, visited, n, start)
                cnt.append(tmp_cnt)

    
    print(len(cnt))
    cnt.sort()
    for num in cnt:
        print(num)