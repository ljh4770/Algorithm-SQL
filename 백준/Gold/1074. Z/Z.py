def Z(n, base_r, base_c, r, c):
    mid = 2 ** (n - 1)
    is_upper = r < base_r + mid
    is_left = c < base_c + mid

    if n == 1:
        # 0
        if is_upper == True and is_left == True:
            return 0
        # 1
        elif is_upper == True and is_left == False:
            return 1
        # 2
        elif is_upper == False and is_left == True:
            return 2
        # 3
        else:
            return 3

    base_cnt = 0
    # 좌상단
    if is_upper == True and is_left == True:
        pass
    # 우상단
    elif is_upper == True and is_left == False:
        base_cnt += 2 ** (2 * n - 2)
        base_c += mid
    # 좌하단
    elif is_upper == False and is_left == True:
        base_cnt += 2 ** (2 * n - 1)
        base_r += mid
    # 우하단
    else:
        base_cnt += 2 ** (2 * n - 2) * 3
        base_r += mid
        base_c += mid
    
    return Z(n - 1, base_r, base_c, r, c) + base_cnt


if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n, r, c = map(int, input().split(' '))
    print(Z(n, 0, 0 , r, c))