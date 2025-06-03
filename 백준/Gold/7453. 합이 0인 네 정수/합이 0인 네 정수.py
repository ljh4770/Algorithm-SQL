import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
A, B, C, D = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a); B.append(b)
    C.append(c); D.append(d)

AB = [a + b for a in A for b in B]
CD = [c + d for c in C for d in D]

cnt = 0
CD = Counter(CD)
for i in AB:
    cnt += CD[-i]
print(cnt)