import sys
input = sys.stdin.readline

N, M = map(int, input().split())
parent = [i for i in range(N + 1)]  # 0번 인덱스는 쓰지 않아도 되지만, 편의상 함께 둠

rank = [0] * (N + 1)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    rootA = find(a)
    rootB = find(b)

    if rootA == rootB:
        return

    if rank[rootA] < rank[rootB]:
        parent[rootA] = rootB
    elif rank[rootA] > rank[rootB]:
        parent[rootB] = rootA
    else:
        parent[rootB] = rootA
        rank[rootA] += 1

for _ in range(M):
    op, a, b = map(int, input().split())

    if op == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
