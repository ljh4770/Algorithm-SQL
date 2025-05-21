import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
ops = [input().rstrip() for _ in range(n)]
deq = deque()

for op in ops:
    res = op.split(' ')
    if len(res) == 2:
        op = int(res[0])
        x = res[1]
    else:
        op = int(res[0])
    
    if op == 1:
        deq.appendleft(x)
    elif op == 2:
        deq.append(x)
    elif op == 3:
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif op == 4:
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif op == 5:
        print(len(deq))
    elif op == 6:
        if deq:
            print(0)
        else:
            print(1)
    elif op == 7:
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif op == 8:
        if deq:
            print(deq[-1])
        else:
            print(-1)