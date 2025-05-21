import sys

query = sys.stdin.readline().strip()

res = 0
cnt = 0
prev = ''
for bracket in query:
    if bracket == '(':
        cnt += 1
    elif bracket == ')':
        cnt -= 1
        if prev == '(':
            res += cnt
        elif prev == ')':
            res += 1
    prev = bracket

print(res)