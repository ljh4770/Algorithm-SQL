from collections import deque
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(n, base):
    global paper
    global directions
    q = deque()
    q.append((0, 0))
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True
    color = paper[base[0]][base[1]]

    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if paper[base[0]+ nx][base[1] + ny] != color:
                return False
            elif paper[base[0]+ nx][base[1] + ny] == color and visited[nx][ny] == False:
                q.append((nx, ny))
                visited[nx][ny] = True

    return True

def check_and_cut(start, n):
    global paper
    
    if n == 1 or bfs(n, start):
        if paper[start[0]][start[1]] == 0:
            return 1, 0
        else:
            return 0, 1
    else:
        nw, nb = 0, 0
        next_starts = [start, 
                       (start[0] + (n // 2), start[1]),
                       (start[0], start[1] + (n // 2)),
                       (start[0] + (n // 2), start[1] + (n // 2))]
        next_size = n // 2
        for next_start in next_starts:
            w, b = check_and_cut(next_start, next_size)
            nw, nb = nw + w, nb + b
                
    return nw, nb

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n = int(input())
    paper = [list(map(int, input().split(' '))) for _ in range(n)]
    start = (0, 0)
    num_white, num_blue = check_and_cut(start, n)
    print(num_white)
    print(num_blue)