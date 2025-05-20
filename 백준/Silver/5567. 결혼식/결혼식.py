from collections import deque

def bfs(graph, n):
    q = deque()
    q.append(1)
    visited = [False] * (n + 1)
    visited[1] = True

    cnt = 0
    depth = 0

    while q:
        depth += 1
        for _ in range(len(q)):
            cur = q.popleft()

            for nxt in graph[cur]:
                if visited[nxt] == False:
                    q.append(nxt)
                    visited[nxt] = True
                    cnt += 1

        if depth == 2:
            break

    return cnt


if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n = int(input())
    m = int(input())

    friend = [tuple(map(int, input().split(' '))) for _ in range(m)]
    graph = [[] for _ in range(n + 1)]

    for a, b in friend:
        graph[a].append(b)
        graph[b].append(a)
    
    print(bfs(graph, n))