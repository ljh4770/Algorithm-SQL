def floyd_warshall(graph, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    return graph

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    INF = float('inf')

    n = int(input()) # 도시 개수
    m = int(input()) # 버스 개수
    edges = [tuple(map(int, input().split(' '))) for _ in range(m)]
    
    # 버스 비용 인접 행렬, zero-based
    matrix = [[INF] * n for _ in range(n)] 

    # 최소 비용 간선 저장(중복 노드 연결 간선 존재)
    for a, b, w in edges:
        if matrix[a - 1][b - 1] != INF:
            matrix[a - 1][b - 1] = min(matrix[a - 1][b - 1], w)
            continue
        matrix[a - 1][b - 1] = w
    
    for i in range(n):
        matrix[i][i] = 0

    # 플로리드-워셜 알고리즘
    dist = floyd_warshall(matrix, n)

    for i in range(n):
        for j in range(n):
            if dist[i][j] == INF:
                print(0, end=' ')
            else:
                print(dist[i][j], end=' ')
        print()