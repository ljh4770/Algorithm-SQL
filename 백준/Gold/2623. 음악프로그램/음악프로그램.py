from collections import deque

def topological_sort(graph, indegree, n):
    q = deque()
    for i in range(1, n + 1, 1):
        if indegree[i] == 0:
            q.append(i)

    result = []
    while q:
        cur = q.popleft()
        result.append(cur)

        for nxt in graph[cur]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)
    
    # There exists a cycle in the graph
    if len(result) < n:
        return [0]
    
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split(' '))
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for _ in range(m):
        # index 0 : length of the permutation
        # index 1 ~ n : the permutation
        tmp = tuple(map(int, input().split(' ')))
        for i in range(1, tmp[0]):
            a, b = tmp[i],  tmp[i + 1]
            graph[a].append(b)
            indegree[b] += 1

    result = topological_sort(graph, indegree, n)
    for value in result:
        print(value)