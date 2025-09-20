from collections import deque

def bfs(sr, sc):
    global n, m, visited
    
    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = True
    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    cnt = 0
    while q:
        x, y = q.popleft()
        cnt += 1

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < n and 0 <= ny < m):
                continue

            if not visited[nx][ny] and (nx, ny) in trash:
                visited[nx][ny] = True
                q.append((nx, ny))
    
    return cnt

if __name__ == '__main__':
    import sys; input = sys.stdin.readline

    n, m, k = map(int, input().split())
    trash = set(tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(k))
    visited = [[False] * m for _ in range(n)]

    answer = 0
    for r, c in trash:
        if visited[r][c]:
            continue
        answer = max(answer, bfs(r, c))
    print(answer)