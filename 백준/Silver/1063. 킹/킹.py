import sys; input = sys.stdin.readline

king, stone, n = input().rstrip().split()
n = int(n)
moves = [input().rstrip() for _ in range(n)]
board = [[0] * 8 for _ in range(8)]

c2n = {chr(65 + i): i for i in range(8)}
n2c = {i: chr(65 + i) for i in range(8)}

directions = {
    'R': (0, 1),
    'L': (0, -1),
    'B': (-1, 0),
    'T': (1, 0),
    'RT': (1, 1),
    'LT': (1, -1),
    'RB': (-1, 1),
    'LB': (-1, -1)
}

kx, ky = int(king[1]) - 1, c2n[king[0]]
sx, sy = int(stone[1]) - 1, c2n[stone[0]]

for mov in moves:
    dx, dy = directions[mov]

    nkx, nky = kx + dx, ky + dy
    if not (0 <= nkx < 8 and 0 <= nky < 8):
        continue

    if (nkx, nky) == (sx, sy):
        nsx, nsy = sx + dx, sy + dy    
        if not (0 <= nsx < 8 and 0 <= nsy < 8):
            continue
        kx, ky = nkx, nky
        sx, sy = nsx, nsy
    else:
        kx, ky = nkx, nky

print(n2c[ky] + str(kx + 1))
print(n2c[sy] + str(sx + 1))