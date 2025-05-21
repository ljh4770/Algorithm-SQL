import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m, n, x, y = map(int, input().split(' '))
    while x <= m * n: # 최대 범위
        if (x-y) % n == 0: # 나머지로 확인
            print(x)
            break
        x += m
    else:
        print(-1)