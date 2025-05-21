import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

def union(v1, v2):
    r1 = find(v1)
    r2 = find(v2)

    if rank[r1] > rank[r2]:
        root[r2] = r1
    elif rank[r1] < rank[r2]:
        root[r1] = r2
    else:
        root[r2] = r1
        rank[r1] += 1


def find(v):
    if v == root[v]:
        return v
    root[v] = find(root[v])
    return root[v]


if __name__ == "__main__":
    n, m = map(int, input().split())
    root = [i for i in range(n)]
    rank = [0 for _ in range(n)]
    conn = [0 for _ in range(n)]

    for i in range(m):
        a, b = map(int, input().split())
        if find(a) == find(b):
            print(i + 1)
            sys.exit(0)
        union(a, b)
    print(0)
