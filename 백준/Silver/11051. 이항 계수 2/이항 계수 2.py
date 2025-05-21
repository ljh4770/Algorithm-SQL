import sys
input = sys.stdin.readline
n, k = map(int, input().split(' '))
mod = 10007
bino = [[-1] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1, 1):
    bino[i][0] = 1
    bino[i][i] = 1

if n < 2:
    print(bino[n][k])
    sys.exit(0)

for i in range(2, n + 1, 1):
    for j in range(1, i, 1):
        bino[i][j] = (bino[i - 1][j - 1] + bino[i - 1][j]) % mod

print(bino[n][k])