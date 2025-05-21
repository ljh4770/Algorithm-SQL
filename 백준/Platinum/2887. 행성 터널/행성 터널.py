def find(parents, x):
    if x != parents[x]:
        parents[x] = find(parents, parents[x])  # 경로 압축
    return parents[x]

def union(parents, rank, a, b):
    # 각각의 대표 원소(루트) 찾기
    rootA = find(parents, a)
    rootB = find(parents, b)

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

    n = int(input().strip())
    planets = []

    for i in range(n):
        x, y, z = map(int, input().split())
        # (x, y, z, 행성인덱스) 저장
        planets.append((x, y, z, i))

    edges = []

    # x좌표 기준으로 정렬 후 인접 노드 간선
    planets.sort(key=lambda x: x[0])
    for i in range(n - 1):
        # i번째와 i+1번째 행성 간의 거리
        w = min(
            abs(planets[i][0] - planets[i+1][0]),
            abs(planets[i][1] - planets[i+1][1]),
            abs(planets[i][2] - planets[i+1][2])
        )
        # (가중치, 행성인덱스1, 행성인덱스2)
        edges.append((w, planets[i][3], planets[i+1][3]))

    # y좌표 기준으로 정렬 후 인접 노드 간선
    planets.sort(key=lambda x: x[1])
    for i in range(n - 1):
        w = min(
            abs(planets[i][0] - planets[i+1][0]),
            abs(planets[i][1] - planets[i+1][1]),
            abs(planets[i][2] - planets[i+1][2])
        )
        edges.append((w, planets[i][3], planets[i+1][3]))

    # z좌표 기준으로 정렬 후 인접 노드 간선
    planets.sort(key=lambda x: x[2])
    for i in range(n - 1):
        w = min(
            abs(planets[i][0] - planets[i+1][0]),
            abs(planets[i][1] - planets[i+1][1]),
            abs(planets[i][2] - planets[i+1][2])
        )
        edges.append((w, planets[i][3], planets[i+1][3]))

    # 모든 간선을 가중치 오름차순으로 정렬
    edges.sort(key=lambda x: x[0])

    parents = [i for i in range(n)]
    rank = [0] * n

    result = 0
    count = 0  # MST에 포함된 간선 수

    # Kruskal MST
    for w, a, b in edges:
        if find(parents, a) != find(parents, b):
            union(parents, rank, a, b)
            result += w
            count += 1
            if count == n - 1:
                break

    print(result)