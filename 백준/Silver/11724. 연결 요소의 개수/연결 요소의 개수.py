from collections import deque

def bfs(graph, visited, start):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        v = q.popleft()

        for i in range(0, n, 1):
            if graph[v][i] == 1 and visited[i] == False:
                q.append(i)
                visited[i] = True
    
    return visited


if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split(' '))
    edges = [tuple(map(lambda x: int(x) - 1, input().split(' '))) for _ in range(m)]

    graph = [[0] * n for _ in range(n)]
    for v, w, in edges:
        graph[v][w] = 1
        graph[w][v] = 1

    visited = [False] * n
    cnt = 0

    for i in range(0, n, 1):
        if visited[i] == False:
            cnt += 1
            visited = bfs(graph, visited, i)

    print(cnt)