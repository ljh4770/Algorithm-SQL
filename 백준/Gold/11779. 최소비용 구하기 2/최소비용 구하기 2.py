import heapq

def dijkstra(graph, n, start):
    push = heapq.heappush
    pop = heapq.heappop

    heap = []
    push(heap, (0, start))
    distance = [float('inf')] * n
    distance[start] = 0
    trace = [0] * n

    while heap:
        dist, cur = pop(heap)
        
        if distance[cur] < dist:
            continue

        for w, next in graph[cur]:
            if dist + w < distance[next]:
                distance[next] = dist + w
                trace[next] = cur
                push(heap, (dist + w, next))
    return distance, trace

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n = int(input())
    m = int(input())
    city = [[] * n for _ in range(n)]

    for _ in range(m):
        a, b, w = map(int, input().split(' '))
        city[a - 1].append((w, b - 1))

    start, end = map(lambda x: int(x) - 1, input().split(' '))

    distance, trace = dijkstra(city, n, start)
    route = [end]
    cur = end
    while cur != start:
        cur = trace[cur]
        route.append(cur)

    print(distance[end])
    print(len(route))
    print(*map(lambda x: x+ 1, route[::-1]))