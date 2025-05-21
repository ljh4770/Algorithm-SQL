from collections import deque

def bfs():
    global n, m
    global maze

    q = deque()
    q.append((0, 0))
    dist = [[-1] * m  for _ in range(n)]
    dist[0][0] = 0

    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if not(0 <= nx < n and 0 <= ny < m) or dist[nx][ny] != -1:
                continue
            
            # 길인 경우
            if maze[nx][ny] == 0:
                dist[nx][ny] = dist[x][y]
                q.appendleft((nx, ny))
            # 벽인 경우
            else: 
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
    return dist[n - 1][m - 1]

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    m, n = map(int, input().split(' '))
    maze = [list(map(int, input().rstrip())) for _ in range(n)]

    print(bfs())