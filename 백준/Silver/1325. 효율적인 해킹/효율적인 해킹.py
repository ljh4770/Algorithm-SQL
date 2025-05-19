import sys
from collections import deque

input = sys.stdin.readline

# BFS 정의
def bfs(start):
    queue = deque([start])
    visited = [0] * (N + 1)
    count = 0  # 개수 세기
    visited[start] = 1  # 방문 처리

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 원소 하나 뽑기
        v = queue.popleft()
        count += 1
        # 해당 원소와 연결된 방문 안한 원소 큐 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
    return count

# N, M 입력
N, M = map(int, input().split())

# 연결 정보 저장 리스트 정의
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    # 연결 정보 입력
    A, B = map(int, input().split())
    # 단방향이니까 B에 A 추가
    graph[B].append(A)

# 컴퓨터 별로 연결된 컴퓨터 저장할 리스트 정의
connections = [0] * (N + 1)

# BFS 수행
for i in range(1, N + 1):
    connections[i] = bfs(i)

# 최대 해킹 가능 컴퓨터 수 계산
max_count = max(connections)

# 정답 저장 리스트 정의
answer = [i for i in range(1, N + 1) if connections[i] == max_count]

# 원하는 결과 출력
print(*answer)