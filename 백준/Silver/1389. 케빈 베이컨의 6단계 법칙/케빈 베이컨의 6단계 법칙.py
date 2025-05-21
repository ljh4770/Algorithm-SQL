from collections import deque

def bfs(graph, start, end, n):
    visited = [False] * n
    q = deque()
    q.append((start, 0))
    visited[start] = True

    while q:
        v, dist = q.popleft()
        if v == end:
            return dist

        for i in range(0, n, 1):
            if graph[v][i] == 1 and visited[i] == False:
                q.append((i, dist + 1))
                visited[i] = True

    return None

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split(' '))
    edges = [tuple(map(lambda x: int(x) - 1, input().split(' '))) for _ in range(m)]

    graph = [[0] * n for _ in range(n)]
    bacon = [[0] * n for _ in range(n)]

    for v, w, in edges:
        graph[v][w] = 1
        graph[w][v] = 1

    for start in range(0, n, 1):
        for end in range(start + 1, n, 1):
            dist = bfs(graph, start, end, n)
            bacon[start][end] = dist
            bacon[end][start] = dist
    
    min_bacon = float('inf')
    min_idx = 0
    for i in range(0, n, 1):
        s = sum(bacon[i])
        if min_bacon > s:
            min_idx = i
            min_bacon = s

    print(min_idx + 1)

