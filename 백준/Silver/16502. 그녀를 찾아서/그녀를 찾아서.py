import sys; input = sys.stdin.readline


N = 4
node_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3}

t = int(input())
m = int(input())
chain = [[0] * N for _ in range(N)]
for _ in range(m):
    u, v, p = input().rstrip().split()
    chain[node_map[u]][node_map[v]] = float(p)

props = [1 / N] * N
for _ in range(t):
    new_props = [0] * N
    for i in range(N):
        for j in range(N):
            new_props[j] += props[i] * chain[i][j]
    props = new_props

for p in props:
    print(f"{p * 100:.2f}")