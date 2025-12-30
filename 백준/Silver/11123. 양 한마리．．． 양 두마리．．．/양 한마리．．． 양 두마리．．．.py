    # 양 한마리... 양 두마리...
import sys; input = sys.stdin.readline
from collections import deque

from typing import List, Tuple


def bfs(sx, sy, h, w, board, visited):
    global directions

    q: deque = deque()
    q.append((sx, sy))
    visited[sx][sy] = True

    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < h and 0 <= ny < w):
                continue
            
            if visited[nx][ny]:
                continue

            if board[nx][ny] == '#':
                q.append((nx, ny))
                visited[nx][ny] = True

def solve():
    h, w = map(int, input().split())
    board: List[str] = [input().rstrip() for _ in range(h)]

    cnt = 0
    visited: List[List[bool]] = [[False] * w for _ in range(h)]
    for x in range(h):
        for y in range(w):
            if visited[x][y]:
                continue

            if board[x][y] == '#':
                bfs(x, y, h, w, board, visited)
                cnt += 1
            
    print(cnt)
    

if __name__ == "__main__":
    directions: List[Tuple[int, int]] = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    t = int(input())

    for _ in range(t):
        solve()