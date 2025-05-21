import sys

K = int(sys.stdin.readline())
data = [int(sys.stdin.readline().strip()) for i in range(K)]

stack = []
for num in data:
    if num == 0: # guarantee number exist
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))
