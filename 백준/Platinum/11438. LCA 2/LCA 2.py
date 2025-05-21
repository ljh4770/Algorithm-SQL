import sys
input = sys.stdin.readline

n = int(input())
edges = [tuple(map(int, input().split(' '))) for _ in range(n - 1)]
m = int(input())
query = [tuple(map(int, input().split(' '))) for _ in range(m)]

adj = [[] for _ in range(n + 1)]
for a, b in edges:
    adj[a].append(b)
    adj[b].append(a)

LOG = 20 # log(100,000) < 20
parent = [[0] * (n + 1) for _ in range(LOG)]
visited = [False] * (n + 1)
depth = [0] * (n + 1)

stack = []
stack.append((1, 0))

while stack:
    cur, rank = stack.pop()
    visited[cur] = True
    depth[cur] = rank

    for next in adj[cur]:
        if visited[next] == False:
            parent[0][next] = cur
            stack.append((next, rank + 1))

# parent 테이블 채우기
for k in range(1, LOG):
    for v in range(1, n + 1):
        parent[k][v] = parent[k - 1][parent[k - 1][v]]

def lca(a, b):
    # 1) depth[a] >= depth[b] 되도록 조정
    if depth[a] < depth[b]:
        a, b = b, a

    # 2) a를 b 깊이까지 올리기
    diff = depth[a] - depth[b]
    for k in range(LOG):
        if diff & (1 << k):
            a = parent[k][a]

    # 이미 같으면 반환
    if a == b:
        return a

    # 3) 위에서부터 내려오면서 부모가 달라지는 지점 찾기
    for k in range(LOG - 1, -1, -1):
        if parent[k][a] != parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]

    # 4) 바로 위 부모가 LCA
    return parent[0][a]

for a, b in query:
    print(lca(a, b))
