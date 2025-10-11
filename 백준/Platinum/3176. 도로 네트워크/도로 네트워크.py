def dfs(cur, d, p, dist):
    depth[cur] = d
    parent[cur][0] = p
    min_distances[cur][0] = dist
    max_distances[cur][0] = dist

    for nxt, w in graph[cur]:
        if nxt != p:
            dfs(nxt, d + 1, cur, w)

def query(u, v):
    if depth[u] < depth[v]:
        u, v = v, u

    min_dist = float('inf')
    max_dist = 0

    for j in range(MAX_LOG - 1, -1, -1):
        if depth[u] - depth[v] >= (1 << j):
            min_dist = min(min_dist, min_distances[u][j])
            max_dist = max(max_dist, max_distances[u][j])
            u = parent[u][j]

    if u == v:
        return min_dist, max_dist

    for j in range(MAX_LOG - 1, -1, -1):
        if parent[u][j] != 0 and parent[u][j] != parent[v][j]:
            min_dist = min(min_dist, min_distances[u][j], min_distances[v][j])
            max_dist = max(max_dist, max_distances[u][j], max_distances[v][j])
            u = parent[u][j]
            v = parent[v][j]

    min_dist = min(min_dist, min_distances[u][0], min_distances[v][0])
    max_dist = max(max_dist, max_distances[u][0], max_distances[v][0])

    return min_dist, max_dist


if __name__ == "__main__":
    import sys
    import math
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 9)

    n = int(input()) # n : [2, 100_000]
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    k = int(input()) # k : [1, 100_000]
    queries = [tuple(map(int, input().split())) for _ in range(k)]

    MAX_LOG = int(math.log2(n)) + 1
    depth = [0] * (n + 1)
    parent = [[0] * MAX_LOG for _ in range(n + 1)]
    min_distances = [[0] * MAX_LOG for _ in range(n + 1)]
    max_distances = [[0] * MAX_LOG for _ in range(n + 1)]

    dfs(1, 0, 0, 0)

    for j in range(1, MAX_LOG):
        for i in range(1, n + 1):
            p = parent[i][j - 1]
            if p != 0:
                parent[i][j] = parent[p][j - 1]
                min_distances[i][j] = min(min_distances[i][j - 1], min_distances[p][j - 1])
                max_distances[i][j] = max(max_distances[i][j - 1], max_distances[p][j - 1])

    for u, v in queries:
        print(*query(u, v))