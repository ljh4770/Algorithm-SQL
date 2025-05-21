import sys

string = input().strip()
is_tag = False
stack = []
res = []

for c in string:
    if c == '<':
        is_tag = True
        while stack:
            res.append(stack.pop())
        res.append(c)
        continue
    elif c == '>':
        is_tag = False
        res.append(c)
    elif is_tag == True:
        res.append(c)
        continue
    elif c == ' ':
        while stack:
            res.append(stack.pop())
        res.append(c)
    else:
        stack.append(c)
while stack:
    res.append(stack.pop())

print(''.join(res))
