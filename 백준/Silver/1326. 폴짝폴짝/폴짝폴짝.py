from collections import deque


def bfs(graph, n, start, end):
    q = deque()
    q.append((start, 0))
    visited = [False] * (n + 1)
    visited[start] = True

    while q:
        cur, d = q.popleft()

        if cur == end:
             return d
        
        for sign in [-1, 1]: # direction to jump
            base = graph[cur]
            mult = 1
            while 0 < (nxt := cur + sign * base * mult) <= n:
                mult += 1
                if visited[nxt]:
                    continue
                q.append((nxt, d + 1))
                visited[nxt] = True
    
    return -1

if __name__ == '__main__':
    import sys; input = sys.stdin.readline

    n = int(input()) # n : [1, 10**4]
    stones = [0] + [*map(int, input().split( ))] # e : [1, 10**4]
    a, b = map(int, input().split()) # a, b : [1, n]

    answer = bfs(stones, n, a, b)
    print(answer)