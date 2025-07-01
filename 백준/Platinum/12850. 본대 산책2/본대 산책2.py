def div_and_conq(d, start, end):
    if d <= 1:
        return m[d][start][end]

    m.setdefault(d, [[0 for _ in range(N)] for _ in range(N)])
    if m[d][start][end]:
        return m[d][start][end]

    half = d // 2
    other = half + 1 if d % 2 else half # 홀수면 +1
    # half <= other

    for k in range(N):
        m[d][start][end] += div_and_conq(half, start, k) * div_and_conq(other, k, end)
        m[d][start][end] %= MOD

    return m[d][start][end]


if __name__ == "__main__":
    d = int(input())
    
    MOD = 10 ** 9 + 7
    N = 8
    
    m = dict()
    m[1] = [
        [0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1],
        [0, 1, 0, 1, 0, 0, 1, 1],
        [0, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 1, 1, 0, 1, 0, 1],
        [1, 1, 1, 0, 0, 0, 1, 0],
    ]

    print(div_and_conq(d, 0, 0))