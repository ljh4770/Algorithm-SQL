import sys

expr = sys.stdin.readline().strip()

symbol = set(['+', '-', '*', '/', '(', ')'])
priority = {
    '+': 0,
    '-': 0,
    '*': 1,
    '/': 1,
}

stack = []
res = []

for c in expr:
    if c not in symbol:
        res.append(c)
        continue
    
    if c == '(':
        stack.append(c)
        continue
    
    if c == ')':
        while stack and stack[-1] != '(':
            res.append(stack.pop())
        stack.pop()
        continue
    
    if not stack:
        stack.append(c)
        continue

    while stack and stack[-1] != '(' and priority[stack[-1]] >= priority[c]:
        res.append(stack.pop())
    stack.append(c)

while stack:
    res.append(stack.pop())

print(''.join(res))