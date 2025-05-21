import sys

input = sys.stdin.readline

N = int(input())

data = [int(input()) for _ in range(N)]
stack = []
max = 0

for i, h in enumerate(data):
    while stack and stack[-1] <= h:
        stack.pop()
    stack.append(h)

print(len(stack))