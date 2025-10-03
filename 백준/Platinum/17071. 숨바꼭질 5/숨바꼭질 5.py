from collections import deque

def bfs(sx, end, upper_bound):
    if sx == end:
        return 0
    
    q = deque()
    q.append((sx, 0))

    # parity dimension for even and odd
    visited = [[-1] * 2 for _ in range(upper_bound + 1)]
    visited[sx][0] = 0

    directions = [
        lambda x: x + 1,
        lambda x: x - 1,
        lambda x: x * 2
    ]

    # mark minimal arrival time for each cell
    while q:
        x, t = q.popleft()

        nt = t + 1  # next time
        np = nt % 2 # next parity
        
        for fx in directions:
            nx = fx(x) # next position

            # OOB
            if not (0 <= nx <= upper_bound):
                continue
            
            # Already visitied / Not minimal time
            if visited[nx][np] != -1:
                continue

            q.append((nx, nt))
            visited[nx][np] = nt
    
    # check they can meet (at same parity)
    time = 0
    while end <= upper_bound:
        cp = time % 2

        arrival_time = visited[end][cp]

        if (arrival_time != -1) and (arrival_time <= time):
            return time
        
        time += 1
        end += time

    return -1


if __name__ == "__main__":
    import sys; input = sys.stdin.readline

    n, k = map(int, input().split())
    MAX_LEN = 500_000

    print(bfs(n, k, MAX_LEN))