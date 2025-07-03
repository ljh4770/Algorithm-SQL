from bisect import bisect_left
from collections import deque


n = int(input())
lines = [tuple(map(int, input().split(' '))) for _ in range(n)]
lines.sort(key=lambda x: x[0])
 
res = []
idx = []
for s, e in lines:
    a = bisect_left(res, e)
    if a == len(res):
        res.append(e)
    else:
        res[a] = e
        
    idx.append(a)
 
cnt = len(res) - 1
q = deque()
for i in range(len(idx) - 1, -1, -1):
    if idx[i] == cnt:
        cnt -= 1
    else:
        # line to cut
        q.appendleft(lines[i])
 
print(len(lines) - len(res))
for k in q:
    print(k[0])