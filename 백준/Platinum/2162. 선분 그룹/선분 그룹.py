def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)


def is_overlap(line1, line2):
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2

    mx1, my1 = min(x1, x2), min(y1, y2)
    mx2, my2 = max(x1, x2), max(y1, y2)
    mx3, my3 = min(x3, x4), min(y3, y4)
    mx4, my4 = max(x3, x4), max(y3, y4)

    ccw123 = ccw(x1, y1, x2, y2, x3, y3)
    ccw124 = ccw(x1, y1, x2, y2, x4, y4)
    ccw341 = ccw(x3, y3, x4, y4, x1, y1)
    ccw342 = ccw(x3, y3, x4, y4, x2, y2)

    if ccw123 * ccw124 == 0 and ccw341 * ccw342 == 0:
        if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4 and my3 <= my2:
            return True
    else:
        if ccw123 * ccw124 <= 0 and ccw341 * ccw342 <= 0:
            return True

    return False

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    x, y = find(a), find(b)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


if __name__ == '__main__':
    import sys; input = sys.stdin.readline
    from collections import Counter

    n = int(input())
    lines = []

    for _ in range(n):
        cords = tuple(map(int, input().split(' ')))
        lines.append(cords)

    parent = [i for i in range(n)]
    for i in range(n - 1):
        a = lines[i]
        for j in range(i + 1, n):
            b = lines[j]
            if is_overlap(a, b) == True:
                union(i, j)

    uniq_cnt = 0
    line_cnt = [0] * n
    for i in range(n):
        if i == parent[i]:
            uniq_cnt += 1
        line_cnt[find(i)] += 1
    
    print(uniq_cnt)
    print(max(line_cnt))