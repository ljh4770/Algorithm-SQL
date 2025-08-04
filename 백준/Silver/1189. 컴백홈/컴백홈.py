def dfs(x, y, d):
    global answer

    if d == k:
        if (x, y) == (0, c - 1):
            answer += 1
        return

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < r and 0 <= ny < c):
            continue
        if visited[nx][ny]:
            continue
        if map_[nx][ny] == 'T':
            continue

        visited[nx][ny] = True
        dfs(nx, ny, d + 1)
        visited[nx][ny] = False


if __name__ == '__main__':
    import sys; input = sys.stdin.readline
    sys.setrecursionlimit(10**2)

    r, c, k = map(int, input().split())
    map_ = [list(input().rstrip()) for _ in range(r)]

    answer = 0 # cnt of paths
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False] * c for _ in range(r)]
    visited[r - 1][0] = True

    dfs(r - 1, 0, 1)
    print(answer)