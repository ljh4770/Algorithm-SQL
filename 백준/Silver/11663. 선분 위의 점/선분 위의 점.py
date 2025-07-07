import sys; input = sys.stdin.readline
from bisect import bisect_left, bisect_right

n, m = map(int, input().split())
points = list(map(int, input().split()))
lines = [tuple(map(int, input().split())) for _ in range(m)]
points.sort()

for s, e in lines:
    l = bisect_left(points, s)
    r = bisect_right(points, e)
    
    print(r - l)