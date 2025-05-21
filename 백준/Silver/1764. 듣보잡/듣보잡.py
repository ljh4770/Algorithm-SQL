import sys

N, M = map(int, sys.stdin.readline().strip().split(' '))
a = [sys.stdin.readline().strip() for _ in range(N)]
b = [sys.stdin.readline().strip() for _ in range(M)]

a = set(a)
b = set(b)

res = list(a.intersection(b))
res.sort()
print(len(res))
for name in res:
    print(name)