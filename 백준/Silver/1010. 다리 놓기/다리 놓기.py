import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a, b = map(int, input().split(' '))
    min_ = min(a, b)
    max_ = max(a, b)
    diff = max_ - min_

    if diff == 0:
        print(1)
        continue

    base = 1
    for mult in range(min_ + 1, max_ + 1, 1):
        base *= mult
    for div in range(2, diff + 1, 1):
        base //= div
    print(base)