import sys

input = sys.stdin.readline

N = int(input())

data = [int(input()) for _ in range(N)]
stack = []
prev = 0

for i, h in enumerate(data):
    while stack and data[stack[-1]] > h:
        height = data[stack.pop()]
        width = i if not stack else(i - stack[-1] - 1)
        prev = max(prev, height * width)
    stack.append(i)
        
while stack:
    height = data[stack.pop()]
    width = N if not stack else (N - stack[-1] - 1)
    prev = max(prev, height * width)

print(prev)