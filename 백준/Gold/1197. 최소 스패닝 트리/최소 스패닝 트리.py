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
    v, e = map(int, input().split(' '))
    edges = [tuple(map(int, input().split(' '))) for _ in range(e)]
    edges.sort(key=lambda x: x[2])

    parents = [i for i in range(v + 1)]
    rank = [0] * (v + 1)  # 각 정점의 초기 랭크는 0
    distance, cnt = 0, 0

    for a, b, value in edges:
        # union이 성공했을 때(= 사이클을 만들지 않을 때)만 MST에 포함
        if union(a, b):
            distance += value
            cnt += 1
            # MST 완성 조건: v - 1개의 간선을 선택하면 종료
            if cnt == v - 1:
                break

    print(distance)
