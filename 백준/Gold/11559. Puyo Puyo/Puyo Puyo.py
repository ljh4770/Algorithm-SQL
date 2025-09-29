from collections import deque

MAX_ROW = 12
MAX_COL = 6
COLORS = ['R', 'G', 'B', 'P', 'Y']
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def check(sx, sy, color):
    # BFS to check if they should be removed
    global field, visited

    q = deque([(sx, sy)])
    visited[sx][sy] = True

    trace = []
    while q:
        x, y = q.popleft()
        trace.append((x, y))

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < MAX_ROW and 0 <= ny < MAX_COL):
                continue

            if visited[nx][ny]:
                continue

            if field[nx][ny] == color:
                q.append((nx, ny))
                visited[nx][ny] = True
    
    if len(trace) < 4:
        return []

    return trace

def puyo(trace):
    # overwrite with upper element to implement gravity
    # upper element first
    for x, y in sorted(trace, key=lambda a: (a[0], a[1])):
            for i in range(x, 0, -1):
                field[i][y] = field[i - 1][y]
            field[0][y] = '.'


if __name__ == '__main__':
    import sys; input = sys.stdin.readline

    field = [list(input().rstrip()) for _ in range(MAX_ROW)]

    visited = [[False] * MAX_COL for _ in range(MAX_ROW)]
    
    chain = 0
    while True:
        flag = False
        trace = [] # coord of removable cells for current chain

        # loop for all field
        for r in range(MAX_ROW - 1, -1, -1):
            for c in range(0, MAX_COL, 1):
                if visited[r][c]:
                    continue # skip for checked cell
                
                if field[r][c] in COLORS:
                    # if color cell -> check if it should remove
                    cur_trace = check(r, c, field[r][c]) # [] or [(x, y), ...]
                    
                    if cur_trace:
                        trace.extend(cur_trace)

        if trace:
            chain += 1
            puyo(trace) # remove from field and drop by gravity
            visited = [[False] * MAX_COL for _ in range(MAX_ROW)]
        else:
            break
    
    print(chain)