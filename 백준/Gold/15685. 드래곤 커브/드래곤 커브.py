def dragon_curve(n, cur_dirs, k):
    if n == k:
        return cur_dirs
    
    rotated = [(d + 1) % 4 for d in cur_dirs[::-1]]
    nxt_dirs = cur_dirs + rotated

    return dragon_curve(n + 1, nxt_dirs, k)

def cnt_square_grid():
    global MAX_LEN, map_

    cnt = 0
    for x in range(MAX_LEN - 1):
        for y in range(MAX_LEN - 1):
            if map_[x][y] != 1:
                continue

            if (
                (map_[x + 1][y] == 1)
                and (map_[x][y + 1] == 1)
                and (map_[x + 1][y + 1] == 1)
            ):
                cnt += 1
    return cnt


if __name__ == "__main__":
    import sys; input = sys.stdin.readline

    MAX_LEN = 101
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]

    n = int(input())
    curves = [tuple(map(int, input().split())) for _ in range(n)]
    map_ = [[0] * MAX_LEN for _ in range(MAX_LEN)]

    
    for y, x, d, k in curves:
        curve_directions = dragon_curve(0, [d], k)
        map_[x][y] = 1
        
        for cur_d in curve_directions:
            dx, dy = directions[cur_d]
            x, y = x + dx, y + dy

            map_[x][y] = 1

    print(cnt_square_grid())