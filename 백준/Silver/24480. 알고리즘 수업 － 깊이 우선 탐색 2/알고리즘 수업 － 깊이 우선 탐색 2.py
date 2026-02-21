def dfs(cur):
    global graph, visited, order
    visited[cur] = order

    for nxt in graph[cur]:
        if visited[nxt]:
            continue
        order += 1
        dfs(nxt)

if __name__ == "__main__":
    import sys; input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)


    N, M, R = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    for i in range(N + 1):
        graph[i].sort(reverse=True)
    
    visited = [0] * (N + 1)
    order = 1
    dfs(R)
    for order in visited[1:]:
        print(order)
