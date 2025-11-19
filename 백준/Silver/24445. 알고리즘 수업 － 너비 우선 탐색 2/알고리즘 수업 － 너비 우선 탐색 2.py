from collections import deque


def bfs(start):
    global n, order

    q = deque()
    q.append(start)
    visited = [False] * (n + 1)
    visited[start] = True

    num = 1
    while q:
        cur = q.popleft()
        order[cur] = num
        num += 1
        

        for nxt in graph[cur]:
            if visited[nxt]:
                continue
            q.append(nxt)
            visited[nxt] = True


if __name__ == "__main__":
    import sys; input = sys.stdin.readline

    n, m, r = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    for v in range(1, n + 1, 1):
        graph[v].sort(reverse=True)
    
    order = [0] * (n + 1)
    bfs(r)

    for o in order[1:]:
        print(o)