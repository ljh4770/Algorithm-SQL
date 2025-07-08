from collections import deque

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def bfs(n, house, stores, fest):
    q = deque()
    q.append(house) # Start from house
    visited = [False] * n
    MAX = 1000

    while q:
        x, y = q.popleft()

        # If reachable to festival
        if dist((x, y), fest) <= MAX:
            return True
        
        # Or not, move to reachable store
        for i, (nx, ny) in enumerate(stores):
            if visited[i] == True:
                # Already visited
                continue
            # Append reachable store
            if dist((x, y), (nx, ny)) <= MAX:
                visited[i] = True
                q.append((nx, ny))

    return False

def solve():
    n = int(input()) # n : [0, 100]

    # (x, y) : [-32,768, 32,767]
    house = tuple(map(int, input().split(' ')))
    stores = [tuple(map(int, input().split(' '))) for _ in range(n)]
    fest = tuple(map(int, input().split(' ')))

    # store
    visited = [False] * (n + 1)
    visited[0] = True

    answer = bfs(n, house, stores, fest)
    answer = 'happy' if answer else 'sad'
    print(answer)

if __name__ == '__main__':
    import sys; input = sys.stdin.readline

    MAX = 1000
    t = int(input()) # t : [1, 50]
    for _ in range(t):
        solve()