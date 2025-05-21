import sys
input = sys.stdin.readline
MOD = 1000

def mul(U, V):
    n = len(U)
    Z = [[0] * n for _ in range(n)]
    
    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n):
                e += U[row][i] * V[i][col]
            Z[row][col] = e % MOD

    return Z

def square(A, B):
    if B == 1:
        for x in range(len(A)):
            for y in range(len(A)):
                A[x][y] %= MOD
        return A
    
    tmp = square(A, B//2)
    if B % 2 == 1:
        return mul(mul(tmp, tmp), A)
    else:
        return mul(tmp, tmp)

if __name__ == '__main__':
    n, b = map(int, input().split())
    a = [[*map(int, input().split())] for _ in range(n)]

    result = square(a, b)
    for r in result:
        print(*r)