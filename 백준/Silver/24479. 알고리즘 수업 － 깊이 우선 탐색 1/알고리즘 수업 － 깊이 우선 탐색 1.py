import sys
sys.setrecursionlimit(10**6)

def dfs(start):
    global graph, visited, cnt
    visited[start] = cnt

    for nxt in graph[start]:
        if visited[nxt] == 0:
            cnt += 1
            dfs(nxt)

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m, r = map(int, input().split(' '))
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split(' '))
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, n + 1):
        graph[i].sort()

    visited = [0] * (n + 1)
    cnt = 1
    dfs(r)

    for v in visited[1:]:
        print(v)