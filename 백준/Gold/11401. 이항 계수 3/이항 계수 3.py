def factorial(N):
    n = 1
    for i in range(2, N + 1):
        n = (n * i) % MOD
    return n

def square(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n
    
    tmp = square(n, k // 2)
    if k % 2:
        return tmp * tmp * n % MOD
    else:
        return tmp * tmp % MOD

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n, k = map(int, input().split())
    MOD = 1000000007

    top = factorial(n)
    bot = factorial(n - k) * factorial(k) % MOD

    print(top * square(bot, MOD - 2) % MOD)