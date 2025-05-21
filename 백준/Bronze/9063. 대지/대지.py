import sys
input = sys.stdin.readline

n = int(input())
min_x = float('inf')
min_y = float('inf')
max_x = -10000 - 1
max_y = -10000 - 1
for _ in range(n):
    x, y = map(int, input().split(' '))
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)

print((max_x - min_x) * (max_y - min_y))