from collections import deque


def topology_sort(n, times, next_works, indegree):
    q = deque()
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
        dp[i] = times[i]
    
    while q:
        cur = q.popleft()

        for nxt in next_works[cur]:
            # update the time
            if dp[nxt] < dp[cur] + times[nxt]:
                dp[nxt] = dp[cur] + times[nxt]
            indegree[nxt] -= 1 # mark cur as completed

            # if all previous works are completed
            if indegree[nxt] == 0:
                q.append(nxt) # start work

    return max(dp)


if __name__ == '__main__':
    import sys; input = sys.stdin.readline

    n = int(input())
    # 1-based
    times = [0]
    # next work information
    next_works = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1) # number of previous works before the index node

    for i in range(1, n + 1, 1):
        # input stream
        line = [*map(int, input().split())]
        
        # time for current work
        time = line[0]
        times.append(time)

        num_prev_work = line[1] # check number of previous works
        if num_prev_work > 0: # if exist
            # parse input from previous info to next work info
            prev_works = line[2:]
            for prev in prev_works:
                next_works[prev].append(i)
            # add indegree information
            indegree[i] = len(prev_works)

    print(topology_sort(n, times, next_works, indegree))