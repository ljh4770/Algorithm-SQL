def LCS(a, b):
    len_a = len(a)
    len_b = len(b)

    dp = [[0] * (len_b + 1) for _ in range(len_a + 1)]
    
    for x in range(1, len_a + 1, 1):
        for y in range(1, len_b + 1, 1):
            if a[x - 1] == b[y - 1]:
                dp[x][y] = dp[x - 1][y - 1] + 1
            else:
                dp[x][y] = max(dp[x - 1][y], dp[x][y - 1])
    
    return dp[len_a][len_b]

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    a = input().rstrip()
    b = input().rstrip()

    print(LCS(a, b))