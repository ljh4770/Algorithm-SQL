import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**4)


def dfs(cur, distance):
    if cur == v:
        print(distance) 
        return

    for nxt, dist in tree[cur]:
        if visited[nxt]:
            continue
        
        visited[nxt] = True
        dfs(nxt, distance + dist)
        visited[nxt] = False

# n : [2, 1000] - number of nodes
# m : [1, 1000] - number of queries
n, m = map(int, input().split())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    # u, v : [1, n] - nodes connected by an edge
    # d : [1, 10000] - distance between u and v
    u, v, d = map(int, input().split())
    tree[u].append((v, d))
    tree[v].append((u, d))

queries = [tuple(map(int, input().split())) for _ in range(m)]

for u, v in queries:
    visited = [False] * (n + 1)
    visited[u] = True
    dfs(u, 0)