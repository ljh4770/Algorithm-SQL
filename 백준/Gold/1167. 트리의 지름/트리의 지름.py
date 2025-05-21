import heapq

def dijkstra(graph, n, start):
    push = heapq.heappush
    pop = heapq.heappop
    
    heap = []
    push(heap, (0, start))
    distance = [float('inf')] * n
    distance[start] = 0

    while heap:
        dist, cur = pop(heap)

        for w, next in graph[cur]:
            if distance[next] > dist + w:
                distance[next] = dist + w
                push(heap, (dist + w, next))
    return distance

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n = int(input())
    edges = [tuple(map(int, input().split(' '))) for _ in range(n)]
    tree = [[] for _ in range(n)]

    # 간선 정보 파싱
    for info in edges:
        node = info[0] # 첫 번째 요소는 시작 노드
        num_info = len(info[1:]) # 나머지 인덱스가 (연결된 노드, 가중치) * k, 마지막 요소는 항상 -1
        for i in range(1, num_info, 2):
            tree[node - 1].append((info[i + 1], info[i] - 1))

    distance = dijkstra(tree, n, 0)
    node = distance.index(max(distance))
    distance = dijkstra(tree, n, node)
    print(max(distance))