import sys
from math import sqrt
t = int(input())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split(' '))
    dist12 = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    
    if dist12 == 0 and r1 == r2:
        print(-1)
    elif dist12 < r1 + r2:
        small = min(r1, r2)
        big = max(r1, r2)
        if dist12 + small < big:
            print(0)
        elif dist12 + small == big:
            print(1)
        else:
            print(2)
    elif dist12 == r1 + r2:
        print(1)
    else:
        print(0)