from collections import deque

def bfs(graph, n, start, end):
    q = deque()
    q.append((start, 0))
    visited = [False] * n
    visited[start] = True

    while q:
        cur, dist = q.popleft()
        
        if cur == end:
            return dist

        for i in range(n):
            if graph[cur][i] == 1 and visited[i] == False:
                q.append((i, dist + 1))
                visited[i] = True
    return -1

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n = int(input())
    start, end = map(lambda x: int(x) - 1, input().split(' '))
    m = int(input())
    data = [tuple(map(lambda x: int(x) - 1, input().split(' '))) for _ in range(m)]

    graph = [[0] * n for _ in range(n)]
    for a, b in data:
        graph[a][b] = 1
        graph[b][a] = 1
    
    dist = bfs(graph, n, start, end)
    print(dist)