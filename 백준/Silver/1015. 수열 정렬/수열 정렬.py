import sys; input = sys.stdin.readline

n = int(input())
a = [*map(int, input().split())]
a_sorted = sorted(a)

p = []
for i in range(n):
    idx = a_sorted.index(a[i])
    p.append(idx)
    a_sorted[idx] = -1

print(*p)