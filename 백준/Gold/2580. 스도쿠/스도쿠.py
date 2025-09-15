import sys
sys.setrecursionlimit(10 ** 5)


def check_row(x, num):
    for i in range(9):
        if board[x][i] == num:
            return False
    return True

def check_col(y, num):
    for i in range(9):
        if board[i][y] == num:
            return False
    return True

def check_block(x, y, num):
    bx = (x // 3) * 3
    by = (y // 3) * 3

    for i in range(3):
        for j in range(3):
            if board[bx + i][by + j] == num:
                return False
    return True

def tracking(d):
    global board
    global zero_cells, zero_cnt

    if d == zero_cnt:
        for line in board:
            print(*line)
        sys.exit(0)
    
    x, y = zero_cells[d]
    for num in range(1, 9 + 1, 1):
        if (
            check_row(x, num)
            and check_col(y, num)
            and check_block(x, y, num)
        ):
            board[x][y] = num
            tracking(d + 1)
            board[x][y] = 0


if __name__ == '__main__':
    input = sys.stdin.readline

    board = [[*map(int, input().split())] for _ in range(9)]
    zero_cells = []
    zero_cnt = 0
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                zero_cells.append((i, j))
                zero_cnt += 1

    tracking(0)