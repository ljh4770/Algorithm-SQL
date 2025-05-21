from collections import deque

def bfs(graph, visited, start, group):
    q = deque()
    q.append(start)
    visited[start] = group

    while q:
        cur = q.popleft()

        for next in graph[cur]:
            if visited[next] == False:
                q.append(next)
                visited[next] = -1 * visited[cur]

            elif visited[next] == visited[cur]:
                return visited, False
            
    return visited, True

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    k = int(input())
    for _ in range(k): # TestCase
        v, e = map(int, input().split(' '))
        edges = [tuple(map(lambda x: int(x) - 1, input().split(' '))) for _ in range(e)]
        
        graph = [[] for _ in range(v)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False] * v
        for node in range(v):
            if visited[node] == False:
                visited, result = bfs(graph, visited, node, 1)
                if result == False:
                    break
        if result == True:
            print('YES')
        else:
            print('NO')