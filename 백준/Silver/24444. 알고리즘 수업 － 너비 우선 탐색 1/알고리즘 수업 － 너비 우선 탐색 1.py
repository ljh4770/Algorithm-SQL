from collections import deque

def bfs(graph, start):
    q = deque()
    q.append(start)
    visited = [0] * len(graph)
    visited[start] = 1

    order = 2
    while q:
        cur = q.popleft()

        for nxt in sorted(graph[cur]):
            if visited[nxt] != 0:
                continue
            q.append(nxt)
            visited[nxt] = order
            order += 1

    for v in visited[1:]:
        print(v)


if __name__ == "__main__":
    import sys; input = sys.stdin.readline

    n, m, r = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    bfs(graph, r)