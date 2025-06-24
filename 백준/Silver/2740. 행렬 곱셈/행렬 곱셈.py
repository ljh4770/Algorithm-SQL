import sys; input = sys.stdin.readline

n, m = map(int, input().split())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))
m, k = map(int, input().split())
B = []
for _ in range(m):
    B.append(list(map(int, input().split())))

RES = [[0 for _ in range(k)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        for t in range(k):
            RES[i][t] += A[i][j] * B[j][t]

for row in RES:
    print(*row)