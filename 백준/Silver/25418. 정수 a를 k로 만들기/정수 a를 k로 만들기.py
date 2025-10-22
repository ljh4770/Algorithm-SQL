from collections import deque

def bfs(start, end):
    q = deque()
    q.append(start)
    visited = [0] * (k + 1)


    ops = [lambda x: 2 * x, lambda x: x + 1]
    while q:
        x = q.popleft()

        if x == end:
            return visited[x]

        for f in ops:
            nx = f(x)

            if not (0 < nx <= k):
                continue

            if visited[nx]:
                continue

            q.append(nx)
            visited[nx] = visited[x] + 1


if __name__ == "__main__":
    import sys; input = sys.stdin.readline

    a, k = map(int, input().split())
    print(bfs(a, k))