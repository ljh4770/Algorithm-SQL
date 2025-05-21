import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    if x == m - 1 and y == n - 1:
        return 1

    if visited[x][y] != -1:
        return visited[x][y]
    
    visited[x][y] = 0
    
    stack = []
    stack.append((0, 0))

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if not (0 <= nx < m and 0 <= ny < n):
            continue

        if map_[nx][ny] < map_[x][y]:
            visited[x][y] += dfs(nx, ny)
    
    return visited[x][y]

if __name__ == '__main__':
    input = sys.stdin.readline

    m, n = map(int, input().split(' '))
    map_ = [list(map(int, input().split(' '))) for _ in range(m)]
    visited = [[-1] * n for _ in range(m)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    print(dfs(0, 0))