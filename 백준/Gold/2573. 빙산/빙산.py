from collections import deque

def bfs(graph, visited, n, m, x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    melt_area = []

    while q:
        x, y = q.popleft()

        num_water = 0

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < n and 0 <= ny < m):
                continue

            if graph[nx][ny] > 0 and visited[nx][ny] == False:
                q.append((nx, ny))
                visited[nx][ny] = True
            elif graph[nx][ny] <= 0: # 값이 0이하 -> 물
                num_water += 1
        # 녹아야 하는 높이 추가
        melt_area.append((x, y, num_water))
    return melt_area

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split(' '))
    map_ = [list(map(int, input().split(' '))) for _ in range(n)]

    year = 0
    while True:
        # 매년 초기화
        visited = [[False] * m for _ in range(n)]
        melt_area = []
        num_area = 0
        for x in range(n):
            for y in range(m):
                # 값이 0 이하 -> 물 , 값이 0 초과 -> 빙산 칸
                if map_[x][y] > 0 and visited[x][y] == False:
                    melt_area.extend(bfs(map_, visited, n, m, x, y))
                    num_area += 1
        # 영역이 두개 이상 -> 종료
        if num_area >= 2:
            break
        # 녹아야하는 칸이 없음 -> 출력 0
        if len(melt_area) == 0:
            year = 0
            break
        year += 1
        # 칸 녹이기
        for x, y, minus in melt_area:
            map_[x][y] -= minus
    print(year)