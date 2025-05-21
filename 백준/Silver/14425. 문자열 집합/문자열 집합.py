import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())
S = [input().strip() for _ in range(N)]
query = [input().strip() for _ in range(M)]

cnt = 0
for s in query:
    if s in S:
        cnt += 1

print(cnt)