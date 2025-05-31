from collections import deque

def bfs(graph, start, end, weight):
    q = deque()
    q.append(start)
    visited = [False] * (n + 1)
    visited[start] = True

    while q:
        cur = q.popleft()

        if cur == end:
            return True
        
        for nxt, limit in graph[cur]:
            if visited[nxt] == False and weight <= limit:
                visited[nxt] = True
                q.append(nxt) 

    return False


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    # n: number of nodes, island
    # m: number of edges, bridge
    n, m = map(int, input().split(' '))
    edges = [[] for _ in range(n + 1)]
    for _ in range(m):
        # a, b: island number
        # c: weight limit for the edge, bridge
        a, b, c = map(int, input().split(' '))
        edges[a].append((b, c))
        edges[b].append((a, c))
    # Target islands
    start, end = map(int, input().split(' '))

    result = 0
    left, right = 1, 10 ** 9
    while left <= right:
        mid = (left + right) // 2

        if bfs(edges, start, end, mid) == True:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    print(result)