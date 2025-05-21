if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    
    n = int(input())
    house = [list(map(int, input().split(' '))) for _ in range(n)]

    # dp[x][y][0] = 가로, dp[x][y][1] = 세로, dp[x][y][2] = 대각선
    dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]
    # 초기 파이프: (0,0)-(0,1)이므로 (0,1)은 가로 상태만 1
    dp[0][1][0] = 1

    for x in range(n):
        for y in range(n):
            if house[x][y] == 1:
                continue

            # 가로 상태로 (x, y)에 오려면
            if y-1 >= 0:
                dp[x][y][0] += dp[x][y-1][0] + dp[x][y-1][2]
            
            # 세로 상태로 (x, y)에 오려면
            if x-1 >= 0:
                dp[x][y][1] += dp[x-1][y][1] + dp[x-1][y][2]
            
            # 대각선 상태로 (x, y)에 오려면
            if x-1 >= 0 and y-1 >= 0 and house[x-1][y] == 0 and house[x][y-1] == 0:
                dp[x][y][2] += dp[x-1][y-1][0] + dp[x-1][y-1][1] + dp[x-1][y-1][2]
    print(
        dp[n-1][n-1][0] + 
        dp[n-1][n-1][1] + 
        dp[n-1][n-1][2]
    )