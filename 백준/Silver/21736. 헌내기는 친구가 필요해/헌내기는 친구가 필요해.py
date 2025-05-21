from collections import deque

def oob(x, y, n, m):
    return not(0 <= x < n and 0 <= y < m)

def bfs(campus, start, n, m):
    visited = [[False] * m for _ in range(n)]
    
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

        for dx, dy in dxdy:
            nx, ny = x + dx, y + dy

            if oob(nx, ny, n, m) or campus[nx][ny] == 'X':
                continue
            if campus[nx][ny] in ['O', 'P'] and visited[nx][ny] == False:
                q.append((nx, ny))
                visited[nx][ny] = True
                if campus[nx][ny] == 'P':
                    cnt += 1
                    campus[nx][ny] = 'O'

    return cnt

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    
    N, M = map(int, input().split(' '))
    campus = [list(input().rstrip()) for _  in range(N)]

    for r in range(N):
        for c in range(M):
            if campus[r][c] == 'I':
                start = (r, c)
                campus[r][c] = 'O'

    res = bfs(campus, start, N, M)
    if res == 0:
        print('TT')
    else:
        print(res)