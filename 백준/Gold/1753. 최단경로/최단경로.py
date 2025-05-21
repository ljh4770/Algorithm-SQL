import heapq

def dijkstra(graph, v, start):
    push = heapq.heappush
    pop = heapq.heappop

    heap = []
    push(heap, (0, start))
    distance = [float('inf')] * v
    distance[start] = 0

    while heap:
        dist, cur = pop(heap)

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

    v, e = map(int, input().split(' '))
    k = int(input())
    edges = [tuple(map(int, input().split(' '))) for _ in range(e)]

    graph = [[] for _ in range(v)]
    for a, b, w in edges:
        graph[a - 1].append((w, b - 1))

    distance = dijkstra(graph, v, k - 1)

    for dist in distance:
        if dist == float('inf'):
            print('INF')
        else:
            print(dist)