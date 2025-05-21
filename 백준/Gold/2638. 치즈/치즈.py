from collections import deque

def melt():
    global n, m, chz
    q = deque()
    q.append((0, 0))
    visited = [[0] * m for _ in range(n)]
    visited[0][0] += 1

    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < n and 0 <= ny < m):
                continue

            if chz[nx][ny] == 1:
                visited[nx][ny] += 1
            elif chz[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] += 1
                q.append((nx, ny))

    for x in range(n):
        for y in range(m):
            if visited[x][y] >= 2:
                chz[x][y] = 0

    max_ = -1
    for row in chz:
        max_ = max(max_, max(row))
    
    if max_ == 0:
        return False
    return True

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split(' '))
    chz = [[*map(int, input().split(' '))] for _ in range(n)]

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    t = 0
    flag = True
    while flag:
        flag = melt()
        t +=  1

    print(t)
