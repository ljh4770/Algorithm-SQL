def find_set(x):
    if x != parents[x]:
        parents[x] = find_set(parents[x])  # 경로 압축
    return parents[x]

def union(a, b):
    # 각각의 대표 원소(루트) 찾기
    rootA = find_set(a)
    rootB = find_set(b)

    # 이미 같은 집합이면 패스
    if rootA == rootB:
        return False

    # 랭크(높이)를 비교하여 낮은 쪽을 높은 쪽 아래로 붙임
    if rank[rootA] < rank[rootB]:
        parents[rootA] = rootB
    else:
        parents[rootB] = rootA
        if rank[rootA] == rank[rootB]:
            rank[rootA] += 1
    return True


if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n = int(input())
    m = int(input())
    edges = [tuple(map(int, input().split(' '))) for _ in range(m)]
    edges.sort(key=lambda x: x[2])
    
    parents = [i for i in range(n + 1)]
    rank = [0] * (n + 1)
    distance, cnt = 0, 0

    for a, b, w in edges:
        if union(a, b):
            distance += w
            cnt += 1
            if cnt == n - 1:
                break
    print(distance)