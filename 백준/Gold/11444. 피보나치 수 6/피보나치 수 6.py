import sys
sys.setrecursionlimit(10**9 + 1)

def recurrence(num):
    global dp, MOD
    if num <= 2:
        return dp[num]
    
    elif dp[num] > 0:
        return dp[num]
    
    half = num // 2
    if num % 2 == 0:
        h0 = recurrence(half)
        h1 = recurrence(half - 1)
        dp[num] = ((2 * h1 + h0) * h0) % MOD
    else:
        h0 = recurrence(half + 1)
        h1 = recurrence(half)
        dp[num] = (h0 ** 2 + h1 ** 2) % MOD
    return dp[num]

if __name__ == '__main__':
    from collections import defaultdict
    n = int(sys.stdin.readline())
    dp = defaultdict(int)
    dp[1], dp[2] = 1, 1
    MOD = 10**9 + 7

    print(recurrence(n))
