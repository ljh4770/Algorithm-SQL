def flip_submatrix(r, c):
    global a

    for i in range(3):
        for j in range(3):
            a[r + i][c + j] ^= 1


if __name__ == '__main__':
    n, m = map(int, input().split())

    a = [list(map(int, input().rstrip())) for _ in range(n)]
    b = [list(map(int, input().rstrip())) for _ in range(n)]

    cnt = 0
    for i in range(n - 2):
        for j in range(m - 2):
            if a[i][j] != b[i][j]:
                flip_submatrix(i, j)
                cnt += 1
    
    print(cnt if a == b else -1)