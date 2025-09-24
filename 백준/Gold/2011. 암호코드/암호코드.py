if __name__ == "__main__":
    code = input()
    n = len(code)
    code = ' ' + code
    MOD = 10 ** 6

    if code[1] == '0':
        print(0)
        exit(0)

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1, 1):
        if int(code[i]) > 0:
            dp[i] += dp[i - 1] % MOD

        num = int(code[i - 1:i + 1])
        if 10 <= num <= 26:
            dp[i] += dp[i - 2] % MOD
    
    print(dp[-1] % MOD)

"""
abcde
fghij
klmno
pqrst
uvwxy
z
"""