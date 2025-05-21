import sys
input = sys.stdin.readline

def force(start, end):
    if start == 0:
        return 2
    elif start == end:
        return 1
    elif abs(start - end) == 2:
        return 4
    return 3

if __name__ == "__main__":
    directs = list(map(int, input().split()))
    dp = [[[500000 for _ in range(5)] for _ in range(5)] for _ in range(100001)]
    dp[0][0][0] = 0

    # dp 테이블 채우기
    for i in range(len(directs) - 1):
        for left in range(5):
            for right in range(5):
                # left
                dp[i + 1][directs[i]][right] = min(dp[i + 1][directs[i]][right], dp[i][left][right] + force(left, directs[i]))
                # right
                dp[i + 1][left][directs[i]] = min(dp[i + 1][left][directs[i]], dp[i][left][right] + force(right, directs[i]))
    
    answer = 500001

    for left in range(5):
        for right in range(5):
            answer = min(answer, dp[len(directs)-1][left][right])

    # 결과 출력
    print(answer)