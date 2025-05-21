import heapq
INF = float('inf')

def dijkstra(graph, n, start):
    push = heapq.heappush
    pop = heapq.heappop

    distance = [INF] * n
    heap = []
    push(heap, (0, start))
    distance[start] = 0

    while heap:
        dist, cur = pop(heap)

        if distance[cur] < dist:
            continue

        for next in graph[cur]:
            if dist + 1 < distance[next]:
                distance[next] = dist + 1
                push(heap, (dist + 1, next))
    
    return distance

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n, m, k, x = map(int, input().split(' '))
    edges = [tuple(map(lambda x: int(x) - 1, input().split(' '))) for _ in range(m)]

    # directed, unweighted
    city = [[] for _ in range(n)]
    for a, b in edges: # 0-based
        city[a].append(b)
    
    distance = dijkstra(city, n, x - 1)

    cnt = 0
    for i, dist in enumerate(distance):
        if dist == k:
            cnt += 1
            print(i + 1) # 0-base
    if cnt == 0:
        print(-1)