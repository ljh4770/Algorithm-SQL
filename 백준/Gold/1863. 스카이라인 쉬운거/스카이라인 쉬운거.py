import sys; input = sys.stdin.readline

n = int(input())
skyline = [int(input().split()[1]) for _ in range(n)] + [0]

answer = 0
stack = [0]
for p in skyline:
    height = p
    while stack[-1] > p:
        if stack[-1] != height:
            answer += 1
            height = stack[-1]
        stack.pop()
    stack.append(p)   
print(answer)