import heapq

def dijkstra(graph, n, start, target):
    push = heapq.heappush
    pop = heapq.heappop

    heap = []
    push(heap, (0, start))
    distance = [float('inf')] * n
    distance[start] = 0

    while heap:
        dist, cur = pop(heap)

        if cur == target:
            return dist
        
        if distance[cur] < dist:
            continue

        for w, next in graph[cur]:
            if dist + w < distance[next]:
                distance[next] = dist + w
                push(heap, (dist + w, next))
    return -1

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n, e = map(int, input().split(' ')) # 노드 개수, 간선 개수
    # 가중치 간선 입력
    edges = [tuple(map(int, input().split(' '))) for _ in range(e)]
    # 반드시 거쳐야하는 노드 두 개
    v1, v2 = list(map(lambda x: int(x) - 1, input().split(' ')))

    # 양방향 가중치 그래프
    graph = [[] for _ in range(n)]

    # 0-based
    for a, b, w in edges: 
        # heap 사용 고려, key인 가중치를 튜플의 첫 요소로
        graph[a - 1].append((w, b - 1))
        graph[b - 1].append((w, a - 1))

    dist = []

    # 0 -> v1 -> v2 -> n - 1
    d = 0
    while True:
        res = dijkstra(graph, n, 0, v1)
        if res == -1:
            d = -1
            break
        d += res
        res = dijkstra(graph, n, v1, v2)
        if res == -1:
            d = -1
            break
        d += res
        res = dijkstra(graph, n, v2, n - 1)
        if res == -1:
            d = -1
            break
        d += res
        break
    dist.append(d)
    
    # 0 -> v2 -> v1 -> n - 1
    d = 0
    while True:
        res = dijkstra(graph, n, 0, v2)
        if res == -1:
            d = -1
            break
        d += res
        res = dijkstra(graph, n, v2, v1)
        if res == -1:
            d = -1
            break
        d += res
        res = dijkstra(graph, n, v1, n - 1)
        if res == -1:
            d = -1
            break
        d += res
        break
    dist.append(d)

    print(min(dist))