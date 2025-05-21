from collections import deque

def topology_sort(graph, indegree, n):
    q = deque()
    for i in range(1, n + 1, 1): # one-based
        if indegree[i] == 0:
            q.append(i)
    
    res = []

    while q:
        cur = q.popleft()
        res.append(cur)

        for next in graph[cur]:
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)
    
    return res

import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))
data = [tuple(map(int, input().split(' '))) for _ in range(m)]
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for a, b in data:
    graph[a].append(b)
    indegree[b] += 1

answer = topology_sort(graph, indegree, n)
for node in answer:
    print(node, end=' ')