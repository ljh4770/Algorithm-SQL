import sys; input = sys.stdin.readline

# n : [2, 2000000], h : [2, 500000]
n, h = map(int, input().split())

up = [0] * h
down = [0] * h

for i in range(n):
    obstacle = int(input())
    if i % 2 == 0:
        down[h - obstacle] += 1
    else:
        up[obstacle - 1] += 1

min_value = n + 1
min_count = 0 

count = n // 2

for i in range(h):
    count += down[i]

    if count < min_value:
        min_value = count
        min_count = 1
    elif count == min_value:
        min_count += 1

    count -= up[i]


print(min_value, min_count)