import sys; input = sys.stdin.readline

INF = float('inf')

v, e = map(int, input().split())

dist = [[INF] * (v + 1) for _ in range(v + 1)]
for _ in range(e):
    x, y, c = map(int, input().split())
    dist[x][y] = c

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

answer = INF
for i in range(1, v+1):
    answer = min(answer, dist[i][i])

print(answer if answer != INF else -1)