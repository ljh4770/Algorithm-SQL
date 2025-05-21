from collections import deque

def bfs(n, start, end):
    q = deque()
    q.append((start[0], start[1], 0))
    visited = [[False] * n for _ in range(n)]
    visited[start[0]][start[1]] = True

    directions = [(-1, 2), (-1, -2), (-2, 1), (-2, -1), (1, 2), (1, -2), (2, -1), (2, 1)]

    while q:
        x, y, dist = q.popleft()

        if (x, y) == end:
            break

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < n and 0 <= ny < n):
                continue

            if visited[nx][ny] == False:
                q.append((nx, ny, dist + 1))
                visited[nx][ny] = True
    
    return dist

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        l = int(input())
        start = tuple(map(int, input().split(' ')))
        end = tuple(map(int, input().split(' ')))
        
        cnt = bfs(l, start, end)
        print(cnt)