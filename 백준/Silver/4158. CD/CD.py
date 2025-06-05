import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().split(' '))
    if (n, m) == (0, 0):
        break

    SG = {int(input()) for _ in range(n)}
    SY = {int(input()) for _ in range(m)}

    print(len(SG & SY))