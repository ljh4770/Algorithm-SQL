import sys
input = sys.stdin.readline
a, b, c, d, e, f = map(int, input().split(' '))

for x in range(-999, 999 + 1, 1):
    for y in range(-999, 999 + 1, 1):
        if a * x + b * y == c:
            if d * x + e * y == f:
                print(x, y)
                break