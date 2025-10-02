from collections import deque


def bfs(sx, sy):
    global visited, r, c

    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = True

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    o_cnt, v_cnt = 0, 0
    while q:
        x, y = q.popleft()
        
        if field[x][y] == 'o':
            o_cnt += 1
        elif field[x][y] == 'v':
            v_cnt += 1
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < r and 0 <= ny < c):
                continue

            if field[nx][ny] == '#':
                continue
            
            if not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True

    return o_cnt, v_cnt


if __name__ == "__main__":
    import sys; input = sys.stdin.readline


    r, c = map(int, input().split()) # r, c: [3, 250]
    field = [list(input().rstrip()) for _ in range(r)]
    # . -> Empty / # -> Fence / o -> Sheep / v -> Wolf
    
    visited = [[False] * c for _ in range(r)]
    area_cnt = dict()
    area_key = 0
    for x in range(r):
        for y in range(c):
            if visited[x][y]:
                continue
            if field[x][y] == '#':
                continue
            
            area_cnt[area_key] = bfs(x, y)
            area_key += 1

    o_cnt, v_cnt = 0, 0
    for o, v in area_cnt.values():
        if o > v:
            o_cnt += o
        else:
            v_cnt += v
    
    print(o_cnt, v_cnt)