import heapq

def dijkstra(graph, n, start, end):
    push = heapq.heappush
    pop = heapq.heappop
    
    heap = []
    push(heap, (0, start))
    distance = [float('inf')] * n
    distance[start] = 0

    while heap:
        time, cur = pop(heap)

        if cur == end:
            return time
        
        if distance[cur] < time:
            continue
        
        for w, next in graph[cur]:
            if time + w < distance[next]:
                distance[next] = time + w
                push(heap, (time + w, next))

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n, m, x = map(int, input().split(' '))
    edges = [tuple(map(int, input().split(' '))) for _ in range(m)]
    adj_matrix = [[] for _ in range(n)]

    for a, b, w in edges:
        adj_matrix[a - 1].append((w, b - 1))

    max_time = 0
    x -= 1
    for i in range(n):
        time0 = dijkstra(adj_matrix, n, i, x)
        time1 = dijkstra(adj_matrix, n, x, i)
        max_time = max(max_time, time0 + time1)
    
    print(max_time)