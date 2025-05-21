from copy import deepcopy

def move_up(board):
    global n
    
    for col in  range(n):
        idx = 0
        for i in range(n):
            if board[i][col] != 0:
                tmp = board[i][col]
                board[i][col] = 0

                if board[idx][col] == 0:
                    board[idx][col] = tmp
                elif board[idx][col] == tmp:
                    board[idx][col] *= 2
                    idx += 1
                else:
                    idx += 1
                    board[idx][col] = tmp
    return board

def move_down(board):
    global n
    
    for col in  range(n):
        idx = n - 1
        for i in range(n - 1, -1, -1):
            if board[i][col] != 0:
                tmp = board[i][col]
                board[i][col] = 0

                if board[idx][col] == 0:
                    board[idx][col] = tmp
                elif board[idx][col] == tmp:
                    board[idx][col] *= 2
                    idx -= 1
                else:
                    idx -= 1
                    board[idx][col] = tmp
    return board

def move_left(board):
    global n
    
    for row in range(n):
        idx = 0
        for j in range(n):
            if board[row][j] != 0:
                tmp = board[row][j]
                board[row][j] = 0

                if board[row][idx] == 0:
                    board[row][idx] = tmp
                elif board[row][idx] == tmp:
                    board[row][idx] *= 2
                    idx += 1
                else:
                    idx += 1
                    board[row][idx] = tmp
    return board

def move_right(board):
    global n
    
    for row in range(n):
        idx = n - 1
        for j in range(n - 1, - 1, -1):
            if board[row][j] != 0:
                tmp = board[row][j]
                board[row][j] = 0

                if board[row][idx] == 0:
                    board[row][idx] = tmp
                elif board[row][idx] == tmp:
                    board[row][idx] *= 2
                    idx -= 1
                else:
                    idx -= 1
                    board[row][idx] = tmp
    return board

def tracking(board, k):
    global n, max_
    if k == 5: # Update max number
        for row in board:
            max_tmp = max(row)
            max_ = max(max_, max_tmp)
        return None
    
    move_func = [move_up, move_down, move_left, move_right]

    for move in move_func:
        board_next = deepcopy(board)
        board_next = move(board_next)
        tracking(board_next, k + 1)

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n = int(input())
    board = [[*map(int, input().split(' '))] for _ in range(n)]
    max_ = 0

    tracking(board, 0)
    print(max_)