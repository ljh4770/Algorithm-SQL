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

    n = int(input())
    m = int(input())
    graph = [list(map(int, input().split(' '))) for _ in range(n)]
    plan = list(map(lambda x: int(x) - 1, input().split(' ')))

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                graph[i][j] = float('inf')
    
    for i in range(n):
        graph[i][i] = 0

    distance = floyd_warshall(graph, n)

    prev = plan[0]
    for cur in plan[1:]:
        if distance[prev][cur] == float('inf'):
            print('NO')
            break
        prev = cur
    else:
        print('YES')