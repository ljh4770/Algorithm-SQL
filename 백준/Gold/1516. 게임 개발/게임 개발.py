from collections import deque

def topology_sort():
    q = deque()
    total_times = [0] * (n + 1)

    for i in range(1, n + 1, 1):
        if indegree[i] == 0:
            q.append(i)
        total_times[i] = times[i]

    while q:
        cur = q.popleft()

        for nxt in graph[cur]:
            if total_times[nxt] < total_times[cur] + times[nxt]:
                total_times[nxt] = total_times[cur] + times[nxt]
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)
    
    return total_times


if __name__ == '__main__':
    import sys; input = sys.stdin.readline

    n = int(input()) # n: [1, 500]

    times = [0] * (n + 1)
    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for i in range(1, n + 1, 1):
        # (t, num, -1) == (time, number required, suffix)
        # t : [1, 10 ** 5] - build time for the number
        # num : [1, n] | None - Required building number for current number
        items = [*map(int, input().split())]
        
        times[i] = items[0]
        idx = 1
        while items[idx] != -1:
            indegree[i] += 1
            graph[items[idx]].append(i)
            idx += 1

    total_times = topology_sort()

    for t in total_times[1:]:
        print(t)