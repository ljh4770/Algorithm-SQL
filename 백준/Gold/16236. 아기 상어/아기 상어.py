from collections import deque

def bfs(graph, n, x, y, size):
    q = deque()
    q.append((x, y))
    dist = [[-1] * n for _ in range(n)]
    dist[x][y] = 0

    dxdy = [(-1, 0) , (0, -1), (1, 0), (0, 1)]

    while q:
        x, y = q.popleft()

        for dx, dy in dxdy:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < n and 0 <= ny < n):
                continue

            if graph[nx][ny] <= size and dist[nx][ny] == -1:
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1
    return dist

def find_fish(graph, n, dist, size):
    x, y = None, None
    min_dist = float('inf')

    for i in range(n):
        for j in range(n):
            if 0 < graph[i][j] < size and dist[i][j] != -1:
                if dist[i][j] < min_dist:
                    min_dist = dist[i][j]
                    x, y = i, j
                elif dist[i][j] == min_dist:
                    if x is not None:
                        if i < x or (i == x and j < y):
                            x, y = i, j 
    
    if min_dist == float('inf'):
        return None
    else:
        return x, y, min_dist

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n = int(input())
    map_ = [list(map(int, input().split(' '))) for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if map_[x][y] == 9:
                shark_x = x
                shark_y = y
                map_[x][y] = 0
                break
    
    kill = 0
    size = 2
    answer = 0
    while True:
        dist = bfs(map_, n, shark_x, shark_y, size)
        result = find_fish(map_, n, dist, size)
        
        if not result:
            break
        
        x, y, fish_dist = result
        answer += fish_dist
        kill += 1

        shark_x, shark_y = x, y
        map_[x][y] = 0
        if kill == size:
            kill = 0
            size += 1

    print(answer)