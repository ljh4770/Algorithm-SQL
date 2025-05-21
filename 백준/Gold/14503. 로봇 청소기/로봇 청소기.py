import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))
x, y, d = map(int, input().split(' ')) # 0: North, 1: East, 2: South, 3: West
space = [[*map(int, input().split(' '))] for _ in range(n)]

clean = [[False] * m for _ in range(n)]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
block = 0

while True:
    # 1
    if clean[x][y] == False:
        clean[x][y] = True
        block += 1
    
    found = False
    for _ in range(4):
        d = (d - 1) % 4
        dx, dy = directions[d]
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < m and space[nx][ny] == 0 and not clean[nx][ny]:
            x, y = nx, ny
            found = True
            break
    if not found:
        back_dir = (d + 2) % 4
        bx, by = x + directions[back_dir][0], y + directions[back_dir][1]

        if 0 <= bx < n and 0 <= by < m and space[bx][by] == 0:
            x, y = bx, by
        else:
            break
print(block)