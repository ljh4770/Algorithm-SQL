import sys
input = sys.stdin.readline

m = int(input())
s = [0] * 21

for _ in range(m):
    op = input().rstrip().split(' ')
    if len(op) == 2:
        num = int(op[1])
    op = op[0]
    if op == 'add':
        s[num] = 1
    elif op == 'remove':
        s[num] = 0
    elif op == 'check':
        if s[num] == 1:
            print(1)
        else:
            print(0)
    elif op == 'toggle':
        s[num] = (s[num] + 1) % 2
    elif op == 'all':
        for i in range(1, 21, 1):
            s[i] = 1
    elif op == 'empty':
        s = [0] * 21