from collections import deque

def topology_sort(graph, indegree, times, n):
    q = deque()
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)

    dp = [0] * n
    for i in range(n):
        dp[i] = times[i]

    while q:
        cur = q.popleft()
        
        for next in graph[cur]:
            if dp[next] < dp[cur] + times[next]:
                dp[next] = dp[cur] + times[next]
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)
    return dp

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split(' '))
        times = list(map(int, input().split(' ')))
        edges = [tuple(map(lambda x: int(x) - 1, input().split(' '))) for _ in range(k)]
        w = int(input()) - 1

        graph = [[] for _ in range(n)]
        indegree = [0] * n
        for a, b in edges:
            graph[a].append(b)
            indegree[b] += 1
        dp = topology_sort(graph, indegree, times, n)
        print(dp[w])