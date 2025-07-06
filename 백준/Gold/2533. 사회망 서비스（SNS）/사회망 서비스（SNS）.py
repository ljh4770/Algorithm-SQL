import sys
sys.setrecursionlimit(10 ** 9)


def dfs(cur):
    global n, tree
    global visited, dp

    visited[cur] = True
    for nxt in tree[cur]:
        if visited[nxt] == True:
            continue
        # Post-order traversal
        dfs(nxt) # Solve sub-problems first (sub trees first)
        # If cur is an adopter, then children can be either adopters or not
        dp[cur][1] += min(dp[nxt][0], dp[nxt][1])
        # If cur is not an adopter, then all children must be adopters
        dp[cur][0] += dp[nxt][1]
    # Count for cur is an adopter
    dp[cur][1] += 1


if __name__ == "__main__":
    input = sys.stdin.readline
    
    n = int(input()) # n : [2, 10 ** 6]
    tree = [[] for _ in range(n)]
    for _ in range(n - 1):
        # convert to 0-based index
        a, b = map(lambda x: int(x) - 1, input().split(' '))
        tree[a].append(b)
        tree[b].append(a)
    
    # dp[cur][0] : number of adopters if cur is not an adopter
    # dp[cur][1] : number of adopters if cur is an adopter
    dp = [[0, 0] for _ in range(n)]
    visited = [False] * n

    dfs(0) # Set 0 as the root of the tree

    print(min(dp[0][0], dp[0][1]))