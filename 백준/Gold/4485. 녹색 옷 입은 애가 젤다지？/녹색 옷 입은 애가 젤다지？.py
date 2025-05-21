import heapq

def dijkstra(graph, n):
    push = heapq.heappush
    pop = heapq.heappop

    heap = []
    push(heap, (graph[0][0], 0, 0))
    INF = float('inf')
    distance = [[INF] * n for _ in range(n)]
    distance[0][0] = graph[0][0]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while heap:
        dist, x, y = pop(heap)

        if distance[x][y] < dist:
            continue

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < n and 0 <= ny < n):
                continue

            weight = graph[nx][ny]

            if dist + weight < distance[nx][ny]:
                distance[nx][ny] = dist + weight
                push(heap, (dist + weight, nx, ny))

    return distance[n - 1][n - 1]
    

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    INF = float('inf')

    p = 1
    while True:
        n = int(input())
        if n == 0:
            break
        cave = [[*map(int, input().split(' '))] for _ in range(n)]

        answer = dijkstra(cave, n)
        print(f"Problem {p}: {answer}")
        p += 1