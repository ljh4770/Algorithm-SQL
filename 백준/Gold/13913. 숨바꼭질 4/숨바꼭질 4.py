from collections import deque

def bfs(start, end):
    MAX_LEN = 10 ** 5

    q = deque()
    q.append(start)
    visited = [-1] * (MAX_LEN + 1)
    visited[start] = start

    directions = [
        lambda x: x - 1,
        lambda x: x + 1,
        lambda x: x * 2,
    ]
    
    while q:
        cur = q.popleft()

        if cur == end:
            break

        for f in directions:
            nxt = f(cur)

            if not (0 <= nxt <= MAX_LEN):
                continue

            if visited[nxt] == -1:
                q.append(nxt)
                visited[nxt] = cur

    result = []
    while cur != start:
        result.append(cur)
        cur = visited[cur]
    result.append(cur)

    return result


if __name__ == '__main__':
    n, k = map(int, input().split(' '))
    result = bfs(n, k)
    print(len(result) - 1)
    print(*result[::-1])