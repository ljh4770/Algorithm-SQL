import sys
input = sys.stdin.readline

n = int(input())
rope = [int(input()) for _ in range(n)]
rope.sort(key=lambda x: -x)

answer = -1
for i in range(n):
    answer = max(answer, rope[i] * (i + 1))
print(answer)