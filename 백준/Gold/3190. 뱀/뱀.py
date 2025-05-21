import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
K = int(input())

# unique (row, col)
# no apple on (1, 1)
apples = [tuple(map(int, input().split(' '))) for _ in range(K)]

L = int(input())
data = [input().strip().split(' ') for _ in range(L)]
shifts = deque()
for X, C in data:
    item = (int(X), C)
    shifts.append(item)

board = [[0] * N for _ in range(N)]
for r, c in apples:
    board[r - 1][c - 1] = -1
board[0][0] = 1

snake = deque()
snake.append((0, 0))
direction = 'R' # U, D, R, L
tick = 0
while True:
    tick += 1
    if direction == 'U':
        dx, dy = -1, 0
    elif direction == 'D':
        dx, dy = 1, 0
    elif direction == 'R':
        dx, dy = 0, 1
    else:
        dx, dy = 0, -1
    x = snake[-1][0] + dx
    y = snake[-1][1] + dy

    snake.append((x, y))

    if not(0 <= x < N and 0 <= y < N):
        break
    
    if board[x][y] == 1:
        break
    elif board[x][y] == -1: # 사과
        board[x][y] = 1
    else:
        board[x][y] = 1
        tail = snake.popleft()
        board[tail[0]][tail[1]] = 0

    if shifts and shifts[0][0] == tick:
        shift = shifts.popleft()
        if shift[1] == 'L':
            if direction == 'U':
                direction = 'L'
            elif direction == 'D':
                direction = 'R'
            elif direction == 'R':
                direction = 'U'
            else:
                direction = 'D'
        else:
            if direction == 'U':
                direction = 'R'
            elif direction == 'D':
                direction = 'L'
            elif direction == 'R':
                direction = 'D'
            else:
                direction = 'U'
    

print(tick)