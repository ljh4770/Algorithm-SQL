def floyd_warshall(graph, n):
    for k in range(1, n + 1, 1):
        for i in range(1, n + 1, 1):
            for j in range(1, n + 1, 1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    return graph


if __name__ == "__main__":
    import sys; input = sys.stdin.readline

    INF = float('inf')

    n = int(input())
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1, 1):
        graph[i][i] = 0


    while True:
        a, b = map(int, input().split())
        if a == -1:
            break
        graph[a][b] = 1
        graph[b][a] = 1
    
    graph = floyd_warshall(graph, n)
    scores = [0] * (n + 1)

    min_score = INF
    for i in range(1, n + 1, 1):
        scores[i] = max(graph[i][1:])
        min_score = min(min_score, scores[i])
    
    candidates = []
    for i in range(1, n + 1, 1):
        if scores[i] == min_score:
            candidates.append(i)
    print(min_score, len(candidates))
    print(*sorted(candidates))