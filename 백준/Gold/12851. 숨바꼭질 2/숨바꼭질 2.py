from collections import deque
MAX_LEN = 10 ** 5 + 1

def bfs(n, k):
    q = deque()
    q.append(n)
    visited = [-1] * MAX_LEN
    visited[n] = 0

    # Next posiible positions
    directions = [
        lambda x: x - 1,
        lambda x: x + 1,
        lambda x: x * 2,
    ]

    cnt = 0
    
    while q:
        cur = q.popleft()
        
        # if target position, do not move
        if cur == k:
            cnt += 1

        for func in directions: # move
            nxt = func(cur)

            # Prevent invalid movement
            if not (0 <= nxt < MAX_LEN):
                continue

            # Enqueue next position
            if visited[nxt] == -1 or visited[nxt] >= visited[cur] + 1:
                q.append(nxt)
                visited[nxt] = visited[cur] + 1
    
    return visited[k], cnt

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n, k = map(int, input().split())

    dist, cnt = bfs(n, k)

    print(dist)
    print(cnt)