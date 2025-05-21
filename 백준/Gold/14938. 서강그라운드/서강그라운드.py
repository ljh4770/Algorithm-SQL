from collections import deque

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

    n, m, r = map(int, input().split(' '))
    num_items = [*map(int, input().split(' '))]
    map_ = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        map_[i][i] = 0

    for _ in range(r):
        a, b, l = map(int, input().split(' '))
        a -= 1
        b -= 1
        map_[a][b] = l
        map_[b][a] = l
    
    map_ = floyd_warshall(map_, n)
    max_items = 0
    for start in range(n):
        item = 0
        for area in range(n):
            if map_[start][area] <= m:
                item += num_items[area]
        max_items = max(max_items, item)
        
    print(max_items)
