import sys
input = sys.stdin.readline

def check_row(r, num):
    for x in range(9):
        if num == board[r][x]:
            return False
    return True

def check_col(c, num):
    for x in range(9):
        if num == board[x][c]:
            return False
    return True

def check_block(r, c, num):
    nr = (r // 3) * 3
    nc = (c // 3) * 3
    for x in range(3):
        for y in range(3):
            if board[nr + x][nc + y] == num:
                return False
    return True

def tracking(k):
    global board, zeros
    if k >= len(zeros):
        for i in range(9):
            print(''.join(map(str, board[i])))
        sys.exit(0)
    
    nr, nc = zeros[k]
    for i in range(1, 9 + 1, 1):
        if check_row(nr, i) and check_col(nc, i) and check_block(nr, nc, i):
            board[nr][nc] = i
            tracking(k + 1)
            board[nr][nc] = 0


if __name__ == '__main__':
    board = [[*map(int, input().rstrip())] for _ in range(9)]
    zeros = []

    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                zeros.append((r,c ))

    tracking(0)