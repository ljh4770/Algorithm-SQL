import sys

input = sys.stdin.readline

string = input().strip()
word = list(input().strip())
stack = []

n = len(word)

for c in string:
    stack.append(c)
    if stack[-n:] == word:
        for _ in range(n):
            stack.pop()

if len(stack) == 0:
    print('FRULA')
else:
    print(''.join(stack))