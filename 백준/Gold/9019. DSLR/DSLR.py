from collections import deque

def move(value):
    return {
        'D': (2 * value) % 10000,
        'S': (value - 1) % 10000 ,
        'L': value // 1000 + (value % 1000) * 10,
        'R': value // 10 + (value % 10) * 1000,
    }

def bfs(a, b):
    q = deque()
    q.append((a, ''))
    visited = [False] * 10001
    visited[a] = True

    while q:
        x, ops = q.popleft()

        if x == b:
            return ops
        
        for op, nx in move(x).items():
            if visited[nx] == False:
                q.append((nx, ops + op))
                visited[nx] = True

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        a, b = map(int, input().split(' '))
        ops = bfs(a, b)
        print(ops)