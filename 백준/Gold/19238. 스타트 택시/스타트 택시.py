from collections import deque

DIRECTIONS = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def select_customer(sx, sy, customers):
    global n, DIRECTIONS

    q = deque()
    q.append((sx, sy, 0))
    visited = [[False] * n for _ in range(n)]
    visited[sx][sy] = True

    candidates = []
    min_dist = float('inf')

    while q:
        x, y, d = q.popleft()
        
        if d > min_dist:
            break

        # return the index with shortest path distance
        # assume served customer removed from the list
        # assume the list is sorted by the condition
        for idx, (cx, cy, ex, ey) in enumerate(customers):
            if (x, y) == (cx, cy):
                min_dist = d
                candidates.append((d, x, y, idx))
        
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < n and 0 <= ny < n):
                continue

            if visited[nx][ny]:
                continue

            if map_[nx][ny] == 1:
                continue
            
            visited[nx][ny] = True
            q.append((nx, ny, d + 1))
    
    if not candidates:
        return -1, -1
    
    candidates.sort()
    d, _, _, idx = candidates[0]

    return idx, d

def move_and_charge(customer, fuel, distance):
    global n, DIRECTIONS

    cx, cy, ex, ey = customer
    
    q = deque()
    q.append((cx, cy, 0))
    visited = [[False] * n for _ in range(n)]
    visited[cx][cy] = True

    while q:
        x, y, d = q.popleft()

        if fuel < d + distance:
            # Out of fuel
            return -1, -1, -1
        
        if (x, y) == (ex, ey):
            return ex, ey, d

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < n and 0 <= ny < n):
                continue

            if visited[nx][ny]:
                continue

            if map_[nx][ny] == 1:
                continue

            visited[nx][ny] = True
            q.append((nx, ny, d + 1))
    
    return -1, -1, -1


if __name__ == "__main__":
    import sys; input = sys.stdin.readline

    n, m, fuel = map(int, input().split())
    map_ = [[*map(int, input().split())] for _ in range(n)]
    sx, sy = map(lambda x: int(x) - 1, input().split())
    customers = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
    customers.sort(key=lambda x: (x[0], x[1]))

    while customers:
        idx, distance1 = select_customer(sx, sy, customers)
        # There not exist customer to serve
        if distance1 == -1:
            print(-1)
            sys.exit(0)
        
        # serve and charge the fuel, update coord of the taxi
        # remove served customer from the list
        sx, sy, distance2 = move_and_charge(customers.pop(idx), fuel, distance1)

        # Out of fuel
        if distance2 == -1:
            print(-1)
            sys.exit(0)

        # update fuel
        fuel = fuel - distance1 + distance2
        
    print(fuel)