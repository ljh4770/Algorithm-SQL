import sys
from typing import List
from collections import deque
MAX_LEN = 10 ** 6

def op(n) -> List[int]:
    result = []
    if n % 3 == 0:
        result.append(n // 3)
    if n % 2 == 0:
        result.append(n // 2)
    result.append(n - 1)
    
    return result

def bfs(n):
    q = deque()
    q.append([n])
    visited = [False] * (MAX_LEN + 1)

    while q:
        trace = q.popleft()
        cur = trace[-1]
        
        if cur == 1:
            break

        for nxt in op(cur):
            if not (0 < n <= MAX_LEN):
                continue

            if visited[nxt] == False:
                q.append((trace + [nxt]))
                visited[nxt] = True
                
    return trace


if __name__ == '__main__':
    n = int(sys.stdin.readline())

    trace = bfs(n)
    print(len(trace) - 1)
    print(*trace)