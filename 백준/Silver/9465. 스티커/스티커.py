import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    stickers = [list(map(int, input().split(' '))) for _ in range(2)]

    # [윗칸, 아래칸] * n
    dp = [[0, 0] for _ in range(n)]
    # 초기값
    dp[0][0] = stickers[0][0] 
    dp[0][1] = stickers[1][0]

    for i in range(1, n, 1):
        dp[i][0] = max(
            dp[i - 1][0], # 윗칸을 안 붙이는 것이 더 높은 점수
            dp[i - 1][1] + stickers[0][i] # 윗칸을 붙여야 더 높은 점수
        )
        dp[i][1] = max(
            dp[i - 1][1],
            dp[i - 1][0] + stickers[1][i]
        )
    print(max(dp[n - 1]))