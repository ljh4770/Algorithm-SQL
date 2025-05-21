import sys
from copy import deepcopy
from collections import deque
sys.setrecursionlimit(8**(2 * 3) + 1)

def infection():
    global n, m, lab
    global viruses

    lab_infected = deepcopy(lab)
    visited = [[False] * m for _ in range(n)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    q = deque(viruses)
    for x, y in viruses:
        visited[x][y] = True
    
    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if lab_infected[nx][ny] == 0 and visited[nx][ny] == False:
                q.append((nx, ny))
                visited[nx][ny] = True
                lab_infected[nx][ny] = 2
    
    return lab_infected


def cnt_area(lab_infected):
    global n, m

    cnt = 0
    for x in range(n):
        for y in range(m):
            if lab_infected[x][y] == 0:
                cnt += 1
    return cnt


def tracking(k, prev):
    global n, m, lab
    global blanks
    global max_area

    if k == 3:
        lab_infected = infection()
        area = cnt_area(lab_infected)
        max_area = max(max_area, area)
        return None
    
    for i in range(prev, len(blanks), 1):
        x, y = blanks[i]
        lab[x][y] = 1
        tracking(k + 1, i + 1)
        lab[x][y] = 0

if __name__ == '__main__':
    input = sys.stdin.readline

    n, m = map(int, input().split(' '))
    lab = [[*map(int, input().split(' '))] for _ in range(n)]

    blanks = []
    viruses = []

    for x in range(n):
        for y in range(m):
            if lab[x][y] == 0:
                blanks.append((x, y))
            elif lab[x][y] == 2:
                viruses.append((x, y))
    
    max_area = -1
    tracking(0, 0)
    print(max_area)