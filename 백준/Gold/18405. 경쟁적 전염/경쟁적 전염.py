from collections import deque


import sys; input = sys.stdin.readline

n, k = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(n)]
s, x, y = map(int, input().split())

virus = {v: deque() for v in range(1, k + 1, 1)}
for r in range(n):
    for c in range(n):
        if board[r][c] == 0:
            continue
        v = board[r][c]
        if v in virus.keys():
            virus[v].append((r, c))

time = 0
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
while time < s:
    for v in range(1, k + 1, 1):
        dq_nxt = deque()
        while virus[v]:
            r, c = virus[v].popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < n and 0 <= nc < n):
                    continue
                if board[nr][nc] == 0:
                    board[nr][nc] = v
                    dq_nxt.append((nr, nc))
                    
        virus[v] = dq_nxt
    time += 1

print(board[x - 1][y - 1])