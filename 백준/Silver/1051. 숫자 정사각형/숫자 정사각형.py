import sys; input = sys.stdin.readline

N, M = map(int, input().split())
board = [input().rstrip() for _ in range(N)]

max_area = 1
for i in range(N):
    for j in range(M):
        for k in range(1, min(N - i, M - j)):
            if board[i][j] == board[i+k][j] == board[i][j+k] == board[i+k][j+k]:
                max_area = max(max_area, (k + 1) ** 2)
                
print(max_area)