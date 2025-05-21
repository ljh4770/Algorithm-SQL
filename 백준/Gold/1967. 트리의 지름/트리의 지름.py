import sys
sys.setrecursionlimit(10**9)

def dfs(start, distance):
    for next, weight in tree[start]:
        if visited[next] == -1:
            visited[next] = distance + weight
            dfs(next, distance + weight)

if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input())
    edges = [tuple(map(int, input().split(' '))) for _ in range(n - 1)]
    tree = [[] for _ in range(n)]
    
    for a, b, w in edges:
        tree[a - 1].append((b - 1, w))
        tree[b - 1].append((a - 1, w))
    
    # 시작 정점에서 임의의 정점까지의 거리를 구하고 그 중 가장 먼 거리를 구한다.
    visited = [-1] * n
    visited[0] = 0
    dfs(0, 0)
    
    # 위에서 찾은 노드에 대한 가장 먼 노드를 찾는다.
    # 가장 먼 노드를 시작지점으로 하여 다시 한번 가장 긴 거리를 찾는다.
    max_node = visited.index(max(visited))
    visited = [-1] * n
    visited[max_node] = 0
    dfs(max_node, 0)
    
    print(max(visited))