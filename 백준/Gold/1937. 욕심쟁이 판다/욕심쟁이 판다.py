import sys
sys.setrecursionlimit(10 ** 8)

def dfs(i, j):
    # return if already visited
    if dp[i][j]:
        return dp[i][j]
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dp[i][j] = 1 # count current cell, visit checked
    
    for dx, dy in directions:
        nx, ny = i + dx, j + dy # next coord
        # OOB
        if not (0 <= nx < n and 0 <= ny < n):
            continue
        # not fullfilled condition
        if forest[i][j] >= forest[nx][ny]:
            continue
        
        # update
        dp[i][j] = max(dp[i][j], dfs(nx, ny) + 1)

    return dp[i][j]


if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input()) # n : [1, 500]
    # n x n, element : [1, 10 ** 6]
    forest = [[*map(int, input().split())] for _ in range(n)]

    dp = [[0] * n for _ in range(n)]
    answer = 0

    for i in range(n):
        for j in range(n):
            answer = max(answer, dfs(i, j))

    print(answer)