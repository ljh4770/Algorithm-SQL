from collections import deque

def oob(x, y, n, m):
    return not (0 <= x < n and 0 <= y < m)

def bfs(maze):
    q = deque()
    row = len(maze)
    col = len(maze[0])

    q.append((0, 0, 1))
    maze[0][0] = 2

    dxdy = [
        (0, -1), # 상
        (0, 1),  # 하
        (-1, 0),  # 좌
        (1, 0)  # 우
    ]

    while q:
        (x, y, length) = q.popleft()
        if x == row - 1 and y == col - 1:
            return length

        for dx, dy in dxdy:
            nx, ny = x + dx, y + dy
            
            if not oob(nx, ny, row, col) and maze[nx][ny] == 1:
                q.append((nx, ny, length + 1))
                maze[nx][ny] = 2
    
    return None

if __name__ == '__main__':
    import sys

    input = sys.stdin.readline
    N, M = map(int, input().split(' '))
    maze = [list(map(int, str(input().strip()))) for _ in range(N)]

    minimal_length = bfs(maze)
    print(minimal_length)
