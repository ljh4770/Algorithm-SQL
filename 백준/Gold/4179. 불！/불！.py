from collections import deque

def bfs(jihoon, fires):
    q = deque()
    q.append((0, jihoon[0], jihoon[1]))
    for f in fires:
        q.append((-1, f[0], f[1]))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        time, x, y = q.popleft()

        if time >= 0 and maze[x][y] != 'F' and (x in [0, r - 1] or y in [0, c - 1]):
            return time + 1
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if not (0 <= nx < r and 0 <= ny < c):
                continue
            if maze[nx][ny] == '#':
                continue

            if time >= 0 and maze[nx][ny] == '.':
                q.append((time + 1, nx, ny))
                maze[nx][ny] = 'J'
            elif time == -1 and maze[nx][ny] != 'F':
                q.append((-1, nx, ny))
                maze[nx][ny] = 'F'

    return "IMPOSSIBLE"

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    r, c = map(int, input().split(' '))
    maze = [[''] * c for _ in range(r)]
    fires = []
    for i in range(r):
        maze[i] = list(input().rstrip())
        for j in range(c):
            if maze[i][j] == 'J':
                jihoon = (i, j)
            elif maze[i][j] == 'F':
                fires.append((i, j))
    
    time = bfs(jihoon, fires)
    
    print(time)