import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split(' '))) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for x in range(n):
    for y in range(n):
        amt = board[x][y]
        if amt == 0: # Cannot Jump
            continue
        if x + amt < n: # Down
            dp[x + amt][y] += dp[x][y]
        if y + amt < n: # Right
            dp[x][y + amt] += dp[x][y]
            
print(dp[-1][-1])