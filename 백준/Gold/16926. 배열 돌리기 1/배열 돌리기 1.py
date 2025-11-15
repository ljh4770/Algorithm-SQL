import sys; input = sys.stdin.readline
from collections import deque

n, m, r = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(n)]
arr_rotated = [[0] * m for _ in range(n)]

deq = deque()
for i in range(min(n, m) // 2):
    deq.clear()
    deq.extend(arr[i][i:m - i])
    deq.extend([row[m - i - 1] for row in arr[i + 1:n - i - 1]])
    deq.extend(arr[n - i - 1][i:m - i][::-1])
    deq.extend([row[i] for row in arr[i + 1:n - i - 1]][::-1])
    
    deq.rotate(-r)
    
    for j in range(i, m - i):
        arr_rotated[i][j] = deq.popleft()
    for j in range(i + 1, n - i - 1):
        arr_rotated[j][m - i - 1] = deq.popleft()
    for j in range(m - i - 1, i - 1, -1):
        arr_rotated[n - i - 1][j] = deq.popleft()  
    for j in range(n - i - 2, i, -1):
        arr_rotated[j][i] = deq.popleft()

for row in arr_rotated:
    print(*row)