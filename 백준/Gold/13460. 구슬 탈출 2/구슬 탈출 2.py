from collections import deque

def move(graph, x, y, dx, dy):
    count = 0  # 이동한 칸 수
    # 다음 위치가 벽(#)이 아니고, 현재 위치가 구멍(O)이 아닐 동안 이동
    while graph[x + dx][y + dy] != '#' and graph[x][y] != 'O':
        x, y = x + dx, y + dy
        count += 1
        if graph[x][y] == 'O':
            break
    return x, y, count
        

def bfs(graph, n, m, red, blue):
    q = deque()
    q.append((red[0], red[1], blue[0], blue[1], 0))
    visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    visited[red[0]][red[1]][blue[0]][blue[1]] = True

    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    while q:
        rx, ry, bx, by, cnt = q.popleft()
        if cnt >= 10:
            break

        for dx, dy in directions:
            # 빨간 구슬 이동
            nrx, nry, rc = move(graph, rx, ry, dx, dy)
            # 파란 구슬 이동
            nbx, nby, bc = move(graph, bx, by, dx, dy)

            # 파란 구슬이 구멍에 빠지면 실패 -> 무시하고 다음 탐색
            if graph[nbx][nby] == 'O':
                continue
            # 빨간 구슬만 구멍에 빠지면 성공
            if graph[nrx][nry] == 'O':
                return cnt + 1
            
            # 둘 다 벽에 막히거나 구멍이 아닐 때 위치가 같아지면 조정
            if nrx == nbx and nry == nby:
                # 더 많이 이동한 구슬을 한 칸 뒤로
                if rc > bc:
                    nrx, nry = nrx - dx, nry - dy
                else:
                    nbx, nby = nbx - dx, nby - dy
            
            if visited[nrx][nry][nbx][nby] == False:
                q.append((nrx, nry, nbx, nby, cnt + 1))
                visited[nrx][nry][nbx][nby] = True

    return -1

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split(' '))
    board = [list(input().rstrip()) for _ in range(n)]

    red = None
    blue = None
    for x in range(n):
        for y in range(m):
            if board[x][y] == 'R':
                red = (x, y)
                board[x][y] = '.'
            if board[x][y] == 'B':
                blue = (x, y)
                board[x][y] = '.'
            if (red != None) and (blue != None):
                break
    cnt = bfs(board, n, m, red, blue)
    print(cnt)