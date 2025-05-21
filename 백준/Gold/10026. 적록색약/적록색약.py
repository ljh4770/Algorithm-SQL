from collections import deque

def bfs(graph, visited, n, x, y, is_abnoraml):
    color = graph[x][y]
    q = deque()
    q.append((x, y, color))
    visited[x][y] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        x, y, color = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if not(0 <= nx < n and 0 <= ny < n):
                continue
            
            if visited[nx][ny] == False:
                if is_abnoraml == False:
                    if graph[nx][ny] == color:
                        q.append((nx, ny, color))
                        visited[nx][ny] = True
                else:
                    if color in 'RG' and graph[nx][ny] in 'RG':
                        q.append((nx, ny, color))
                        visited[nx][ny] = True
                    elif color == 'B' and graph[nx][ny] == 'B':
                        q.append((nx, ny, color))
                        visited[nx][ny] = True
    return visited

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n = int(input())
    image = [list(input().rstrip()) for _ in range(n)]

    normal = 0
    abnormal = 0

    visited = [[False] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if visited[x][y] == False:
                normal += 1
                visited = bfs(image, visited, n, x, y, False)
    
    visited = [[False] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if visited[x][y] == False:
                abnormal += 1
                visited = bfs(image, visited, n, x, y, True)
    
    print(normal, abnormal)