import sys; input = sys.stdin.readline

n, m = map(int, input().split())
info = []
for _ in range(n):
    name, pivot = input().split()
    info.append((name, int(pivot)))
strengths = [int(input()) for _ in range(m)]

for s in strengths:
    start, end = 0, n - 1
    while start <= end:
        mid = (start + end) // 2
        if s <= info[mid][1]:
            end = mid - 1
        else:
            start = mid + 1
    print(info[start][0])