def check(road):
    global n, l

    inc = []
    dec = []
    for i in range(0, n - 1, 1):
        d = road[i] - road[i + 1]
        if d == 0:
            continue
        elif d == 1:
            inc.append(i + 1)
        elif d == -1:
            dec.append(i)
        else:
            return False

    slide = [False] * n
    for i in inc:
        for j in range(i, i + l, 1):
            if j >= n:
                return False
            if road[i] != road[j]:
                return False
            if slide[j] == True:
                return False
            slide[j] = True
            
    for i in dec:
        for j in range(i, i - l, -1):
            if j < 0:
                return False
            if road[i] != road[j]:
                return False
            if slide[j] == True:
                return False
            slide[j] = True
    return True

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n, l = map(int, input().split(' '))
    map_ = [list(map(int, input().split(' '))) for _ in range(n)]

    cnt = 0
    for row in map_:
        if check(row) == True:
            cnt += 1
    for i in range(n):
        col = [map_[j][i] for j in range(n)]
        if check(col) == True:
            cnt += 1
    print(cnt)