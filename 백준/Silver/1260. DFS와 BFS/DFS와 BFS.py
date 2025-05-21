from collections import deque

def dfs(graph, start_node):
    N = len(graph)
    stack = deque([start_node])
    visited = [False for _ in range(N)]
    res = []

    while stack:
        v = stack.pop()
        if visited[v] == False:
            res.append(str(v)) # 문제 요구사항
        visited[v] = True

        for i in range(N - 1, 0, -1):
            if graph[v][i] == 1 and not visited[i]:
                stack.append(i)
    
    return res

def bfs(graph, start_node):
    N = len(graph)
    queue = deque([start_node])
    visited = [False for _ in range(N)]
    res = []

    while queue:
        v = queue.popleft()
        if visited[v] == False:
            res.append(str(v)) # 문제 요구사항
        visited[v] = True

        for i in range(1, N, 1):
            if graph[v][i] == 1 and not visited[i]:
                queue.append(i)
    
    return res

import sys
input = sys.stdin.readline

N, M, V = map(int, input().split(' '))
edges = [tuple(map(int, input().split(' '))) for _ in range(M)]
graph = [[0] * (N + 1) for _ in range(N + 1)]

for a, b in edges:
    graph[a][b] = 1
    graph[b][a] = 1

res_dfs = dfs(graph, V)
res_bfs = bfs(graph, V)

print(' '.join(res_dfs))
print(' '.join(res_bfs))