def solve():
    n = int(input()) # number of coin values
    coins = [*map(int, input().split(' '))] # ascending order
    m = int(input())

    dp = [0] * (m + 1)
    dp[0] = 1
     
    for coin in coins:
        for i in range(1, m + 1): # Target value
            if i >= coin:
                dp[i] += dp[i - coin]
    
    print(dp[m])
        
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        solve()