import sys

input = sys.stdin.readline
N = int(input())
tops = list(map(int, sys.stdin.readline().strip().split()))

res = [0] * N
stack = []

for i in range(N - 1, -1, -1):
    while stack and tops[stack[-1]] < tops[i]:
        res[stack.pop()] = i + 1
    stack.append(i)

print(' '.join(map(str, res)))