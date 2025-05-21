import sys
input = sys.stdin.readline

n, k = map(int, input().split(' '))
values = [int(input()) for _ in range(n)]

value = k
cnt = 0

for coin in values[::-1]:
    if value // coin > 0:
        cnt += value // coin
        value %= coin
    if value == 0:
        break

print(cnt)