from heapq import heappush, heappop
INF = float('inf')

def dijkstra(start, end):
    global n, k
    global graph, magic_cost
    hq = []
    heappush(hq, (0, start, 0)) # (dist, node, num_magic)
    distance = [[INF] * (k + 1) for _ in range(n + 1)]
    distance[start][0] = 0

    while hq:
        d, cur, magic_cnt = heappop(hq)

        if distance[cur][magic_cnt] < d:
            continue

        for nxt, i in graph[cur]:
            for magic in range(magic_cnt, k + 1, 1):
                cost = magic_cost[i][magic]
                if d + cost < distance[nxt][magic]:
                    distance[nxt][magic] = d + cost
                    heappush(hq, (distance[nxt][magic], nxt, magic))
    return min(distance[b])


if __name__ == '__main__':
    import sys; input = sys.stdin.readline

    # n : [2, 1000] - num node
    # m : [n - 1, 2000] - num road
    # a, b : [1, n], a != b
    # a - start, b - end
    n, m, a, b = map(int, input().split())
    graph = [[] for _ in range(n + 1)] # 1-based
    magic_cost = [[] for _ in range(m)] # cost for k-th magic
    for i in range(m):
        # u, v : [1, n] - node
        # t : [0, 10 ** 9] - cost
        u, v, t = map(int, input().split())
        magic_cost[i].append(t)
        graph[u].append((v, i))
        graph[v].append((u, i))
    
    # k : [0, 100] - magic count(change cost)
    k = int(input())
    # (t, t_k) : [0, 10 ** 9] - convert all t cost road to cost t_k
    for _ in range(k):
        t_k = list(map(int, input().split()))
        for i in range(m):
            magic_cost[i].append(t_k[i])
    
    print(dijkstra(a, b))