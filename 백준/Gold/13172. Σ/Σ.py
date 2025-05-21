MOD = 10**9 + 7

def div_con_power(num, exp):
    global MOD
    if exp == 1:
        return num
    
    if exp % 2 == 0:
        half = div_con_power(num, exp // 2)
        return half * half % MOD
    
    return num * div_con_power(num, exp - 1) % MOD

def modular_div(a, b):
    return a * div_con_power(b, MOD - 2) % MOD

if __name__ == '__main__':
    import sys
    from math import gcd
    input = sys.stdin.readline

    m = int(input())
    
    res = 0
    for _ in range(m):
        n, s = map(int, input().split(' '))
        div = gcd(n, s)
        n //= div
        s //= div

        res += modular_div(s, n)
        res %= MOD

    print(res)