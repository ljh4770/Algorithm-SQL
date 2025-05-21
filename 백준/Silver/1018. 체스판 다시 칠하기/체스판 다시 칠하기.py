if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split(' '))
    board = [input().rstrip() for _ in range(n)]
    min_cnt = float('inf')

    for i in range(0, n - 8 + 1 , 1):
        for j in range(0, m - 8 + 1 , 1):
            cnt_w = 0
            cnt_b = 0
            start_color = board[i][j]
            for r in range(8):
                for c in range(8):
                    color = board[i + r][j + c]
                    if (r + c) % 2 == 0:
                        if color != 'W':
                            cnt_w += 1
                        else:
                            cnt_b += 1
                    else:
                        if color != 'B':
                            cnt_w += 1
                        else:
                            cnt_b += 1
            min_cnt = min(min_cnt, cnt_w, cnt_b)
    print(min_cnt)
