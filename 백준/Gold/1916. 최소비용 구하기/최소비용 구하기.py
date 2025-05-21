import heapq

def dijkstra(graph, n, start, end):
    push = heapq.heappush
    pop = heapq.heappop

    heap = []
    push(heap, (0, start))
    distance = [float('inf')] * n
    distance[start] = 0

    while heap:
        dist, cur = pop(heap)
        if cur == end:
            return dist

        if distance[cur] < dist:
            continue

        for weight, next in graph[cur]:
            if dist + weight < distance[next]:
                distance[next] = dist + weight
                push(heap, (dist + weight, next))

    return distance

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    INF = float('inf')

    n = int(input())
    m = int(input())
    edges = [tuple(map(int, input().split(' '))) for _ in range(m)]
    start, end = map(int, input().split(' '))

    graph = [[] for _ in range(n + 1)]

    for a, b, w in edges:
        graph[a].append((w, b))

    dist = dijkstra(graph, n + 1, start, end)
    print(dist)