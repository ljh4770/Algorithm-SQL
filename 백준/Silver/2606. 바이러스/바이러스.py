from collections import deque

def bfs(graph, n):
    q = deque()
    visited = [False for _ in range(n)]
    q.append(0)
    visited[0] = True
    res = 0

    while q:
        v = q.popleft()

        for i in range(0, n, 1):
            if graph[v][i] == 1 and visited[i] == False:
                q.append(i)
                visited[i] = True
                res += 1

    return res

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n = int(input())
    edges = int(input())
    graph = [[0] * n for _ in range(n)]

    for _ in range(edges):
        a, b = map(lambda x: int(x) - 1, input().split(' '))
        graph[a][b] = 1
        graph[b][a] = 1

    print(bfs(graph, n))