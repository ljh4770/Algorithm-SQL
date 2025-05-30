from heapq import heappush, heappop

def topological_sort(graph, indegree, n):
    # Initialize a min heap for nodes with indegree 0
    q = []
    for i in range(1, n + 1, 1):
        if indegree[i] == 0:
            heappush(q, i)

    # Answer: order of solving problems
    result = []

    # Topological Sort - Kahn's Algorithm
    while q:
        cur = heappop(q)
        result.append(cur) # Add to the result

        # Related problems
        for nxt in graph[cur]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                # Add to the heap
                heappush(q, nxt)

    return result


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    # n: number of problems
    # m: number of relationships
    n, m = map(int, input().split(' '))
    
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1) # Initialize indegree for each problem
    for _ in range(m):
        a, b = map(int, input().split(' '))
        graph[a].append(b)
        indegree[b] += 1
    
    # Get the order of solving problems
    order = topological_sort(graph, indegree, n)
    print(*order)