import sys
input = sys.stdin.readline

t = int(input())
inputs = [tuple(map(int, input().split(' '))) for _ in range(t)]

for x, y in inputs:
    distance = y - x
    tmp = 0
    cnt = 0
    moving = 0

    while tmp < distance:
        cnt += 1
        if cnt % 2 != 0:
            moving += 1
        tmp += moving
    print(cnt)