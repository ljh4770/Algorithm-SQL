import sys
from collections import deque

input = sys.stdin.readline
T = int(input())


for _ in range(T):
    query = input().strip()
    n = int(input())
    arr = input().strip()[1:-1]
    is_reversed = False
    
    if n == 0:
        arr = deque()
    else:
        arr = deque(arr.split(','))
    
    for q in query:
        if q == 'R':
            is_reversed = not is_reversed

        elif q == 'D':
            if len(arr) == 0:
                print('error')
                break
            if is_reversed == True:
                arr.pop()
            else:
                arr.popleft()
    else:
        if is_reversed == True:
            arr.reverse()
        print(f"[{','.join(arr)}]")
