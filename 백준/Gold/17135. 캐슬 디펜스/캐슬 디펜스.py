from collections import deque
from copy import deepcopy


def bfs(board, sx, sy):
    global n, m, d

    q = deque()
    q.append((sx, sy, 1))
    visited = [[False] * m for _ in range(n)]
    visited[sx][sy] = True

    directions = [(0, -1), (-1, 0), (0, 1)]

    while q:
        x, y, r = q.popleft()

        if board[x][y]:
            return (x, y)
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < n and 0 <= ny < m):
                continue

            if visited[nx][ny]:
                continue

            if r < d:
                q.append((nx, ny, r + 1))
                visited[nx][ny] = True

    return None

def attack(archors, board):
    global n

    targets = set()
    for ay in archors:
        enemy = bfs(board, n - 1, ay)
        if enemy:
            targets.add(enemy)
    
    for x, y in targets:
        board[x][y] = 0

    return len(targets)

def forward(board):
    global n, m

    flag = True
    for x in range(n - 1, -1, -1):
        for y in range(m):
            if board[x][y] == 0:
                continue
            flag = False
            board[x][y] = 0

            nx = x + 1
            if not (0 <= nx < n):
                continue
            
            board[nx][y] = 1

    return board, flag

def simulation():
    global archors, board

    sim_board = deepcopy(board)
    cnt, flag = 0, False
    while not flag:
        cnt += attack(archors, sim_board)
        sim_board, flag = forward(sim_board)

    return cnt

def tracking(idx, k):
    global archors, answer

    if k == 3:
        answer = max(answer, simulation())
        return

    for i in range(idx, m, 1):
        archors.append(i)
        tracking(i + 1, k + 1)
        archors.pop()


if __name__ == "__main__":
    import sys; input = sys.stdin.readline

    # n, m : [3, 15]
    # d : [1, 10]
    n, m, d = map(int, input().split())
    board = [[*map(int, input().split())] for _ in range(n)] # binary

    archors = []
    answer = 0
    tracking(0, 0)
    print(answer)