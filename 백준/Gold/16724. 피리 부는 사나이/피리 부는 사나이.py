def find_set_2d(x, y):
    if parents[x][y] != (x, y):
        parents[x][y] = find_set_2d(*parents[x][y])
    return parents[x][y]

def union_2d(x1, y1, x2, y2):
    root1 = find_set_2d(x1, y1)
    root2 = find_set_2d(x2, y2)

    if root1 == root2:
        return False

    parents[root1[0]][root1[1]] = root2
    return True

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    # n: num rows, m: num columns
    n, m = map(int, input().split(' '))
    # n * m map info with directions, UDLR
    # No direction leads outside the map
    map_ = [input().rstrip() for _ in range(n)]

    parents = [[(i, j) for j in range(m)] for i in range(n)]
    
    directions = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }
    for x in range(n):
        for y in range(m):
            d = map_[x][y]
            dx, dy = directions[d]
            nx, ny = x + dx, y + dy

            root_cur = find_set_2d(x, y)   # parents of current cell
            root_nxt = find_set_2d(nx, ny) # parents of next cell

            if root_cur != root_nxt:
                union_2d(x, y, nx, ny)
    
    safe_zones = set()
    for x in range(n):
        for y in range(m):
            root = find_set_2d(x, y)
            safe_zones.add(root)

    print(len(safe_zones))