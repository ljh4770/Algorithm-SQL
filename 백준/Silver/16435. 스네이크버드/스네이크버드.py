import sys; input = sys.stdin.readline

n, l = map(int, input().split())
fruits = [*map(int, input().split())]
fruits.sort()

cur = l
for f in fruits:
    if cur < f:
        continue
    cur += 1
print(cur)