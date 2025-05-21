from collections import deque

def floyd_warshall(graph, n):
    dist = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                dist[i][j] = graph[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

dist = floyd_warshall(matrix, n)

for row in dist:
    for d in row:
        if d == float('inf'):
            print(0, end = ' ')
        else:
            print(1, end = ' ')
    print()