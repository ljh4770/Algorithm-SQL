import sys
input = sys.stdin.readline

board = [list(input().rstrip()) for _ in range(8)]
cnt = 0
for i in range(0, 8, 1):
    for j in range(0, 8, 1):
        if (i + j) % 2 == 0 and board[i][j] == 'F':
            cnt += 1
print(cnt)
            