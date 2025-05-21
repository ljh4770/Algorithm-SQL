import sys

input = sys.stdin.readline

T = int(input())
data = [tuple(map(int, input().split(' '))) for _ in range(T)]

for (H, W, N) in data:
    q, r = divmod(N, H)
    if r == 0:
        y = str(H)
        xx = str(q).zfill(2)    
    else:
        y = str(r)
        xx = str(1 + q).zfill(2)
    print(y + xx)