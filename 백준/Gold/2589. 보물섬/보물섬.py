from collections import deque
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(graph, n, m, start):
    q = deque()
    q.append((start[0], start[1], 0))
    visited = [[False] * m for _ in range(n)]
    visited[start[0]][start[1]] = True

    global directions

    while q:
        r, c, d = q.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if not (0 <= nr < n and 0 <= nc < m):
                continue
            if graph[nr][nc] == 'L' and visited[nr][nc] == False:
                q.append((nr, nc, d + 1))
                visited[nr][nc] = True
    return d

def solve(graph, n, m):
    # 모든 육지 덩어리에 대해 조사
    # 하나의 육지 안의 한칸으로 부터 bfs, 거리정보 포함
        # bfs 적용 시 이동하지 않는 칸 저장 -> 보물 후보
        # 보물 후보로 부터 bfs로 최대 거리 반환 -> 정답 후보
    visited = [[False] * m for _ in range(n)]

    global directions

    dist = -1

    for x in range(n):
        for y in range(m):
            # 방문하지 않은 육지 칸인 경우
            if graph[x][y] == 'L' and visited[x][y] == False:
                # BFS
                q = deque()
                q.append((x, y, 0))
                visited[x][y] = True

                candidate = []

                while q:
                    r, c, d = q.popleft()

                    cnt_not_mov = 0 # 이동하지 못한 방향 count
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc

                        if not (0 <= nr < n and 0 <= nc < m):
                            cnt_not_mov += 1
                            continue
                        if graph[nr][nc] == 'L' and visited[nr][nc] == False:
                            q.append((nr, nc, d + 1))
                            visited[nr][nc] = True
                        else:
                            cnt_not_mov += 1
                    # 이동하지 못한 칸 저장
                    if cnt_not_mov == 4:
                        candidate.append((r, c))
                # --------------------
                # 후보에 대하여 거리 계산
                if candidate:
                    for start in candidate:
                        d = bfs(graph, n, m, start)
                        dist = max(dist, d)
    return dist

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split(' '))

    map_ = [input().rstrip() for _ in range(n)]
    dist = solve(map_, n, m)
    print(dist)