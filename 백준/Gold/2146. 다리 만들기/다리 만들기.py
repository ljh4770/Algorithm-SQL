import sys
from collections import deque

input = sys.stdin.readline

# 1) 입력 및 초기화
n = int(input())
grid = [list(map(int, input().split(' '))) for _ in range(n)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 섬 번호 및 방문 표시용
island = [[0] * n for _ in range(n)]
current_label = 0

# 2) 섬마다 고유 번호 매기기 (레이블링)
for x in range(n):
    for y in range(n):
        if grid[x][y] == 1 and island[x][y] == 0:
            current_label += 1
            dq = deque([(x,y)])
            island[x][y] = current_label
            while dq:
                x,y = dq.popleft()
                for dx,dy in directions:
                    nx, ny = x+dx, y+dy
                    if 0<=nx<n and 0<=ny<n:
                        if grid[nx][ny] == 1 and island[nx][ny] == 0:
                            island[nx][ny] = current_label
                            dq.append((nx,ny))

# 3) 멀티소스 BFS 준비: dist, owner 배열과 초기 큐
dist  = [[-1] * n for _ in range(n)]
owner = [[0]  * n for _ in range(n)]
q = deque()

for x in range(n):
    for y in range(n):
        if grid[x][y] == 1:
            # 경계 셀인지 확인
            for dx, dy in directions:
                nx, ny = x + dx, y + dy 
                if not (0 <= nx < n and 0 <= ny < n):
                    continue
                if grid[nx][ny] == 0:
                    dist[x][y]  = 0
                    owner[x][y] = island[x][y]
                    q.append((x, y))
                    break

# 4) 다리 만들기 BFS
answer = float('inf')
while q:
    x, y = q.popleft()
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < n and 0 <= ny < n):
            continue

        # 물(0)인 경우: 확장
        if grid[nx][ny] == 0:
            # 처음 방문 → 확장
            if dist[nx][ny] == -1:
                dist[nx][ny]  = dist[x][y] + 1
                owner[nx][ny] = owner[x][y]
                q.append((nx,ny))
            # 이미 다른 섬이 확장해 왔는지 검사
            elif owner[nx][ny] != owner[x][y]:
                candidate = dist[x][y] + dist[nx][ny]
                if candidate < answer:
                    answer = candidate

        # 육지(1)인 경우: 만약 다른 섬 소유라면 다리 완성
        else:
            if owner[nx][ny] != 0 and owner[nx][ny] != owner[x][y]:
                total_length = dist[x][y]  # 현재 칸까지 물 거리
                # 상대편 섬까지의 물 거리는 dist[nx][ny]이 육지(경계)이므로 == 0
                # 따라서 총 다리 길이는 dist[x][y]
                answer = min(answer, total_length)

# 5) 결과 출력
print(answer)