import sys

input = sys.stdin.readline

N, K = map(int, input().split(' '))
num = list(input().strip())

stack = []
cnt = K

for n in num:
    while stack and stack[-1] < n and cnt > 0:
        cnt -= 1
        stack.pop()
    stack.append(n)

answer = stack[:N - K]

print(''.join(answer))