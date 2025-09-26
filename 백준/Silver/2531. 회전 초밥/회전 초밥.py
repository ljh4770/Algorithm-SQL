if __name__ == '__main__':
    import sys; input = sys.stdin.readline

    n, d, k, c = map(int, input().split())
    dishes = [int(input()) for _ in range(n)]

    max_uniq_cnt = 0

    for i in range(0, n - k + 1, 1):
        picks = dishes[i: i + k] + [c]
        max_uniq_cnt = max(max_uniq_cnt, len(set(picks)))

    for i in range(n - k + 1, n + 1, 1):
        # print(dishes[i:], "asdf", dishes[:i - n + k])
        picks = dishes[i:] + dishes[:i - n + k] + [c]
        max_uniq_cnt = max(max_uniq_cnt, len(set(picks)))
    
    print(max_uniq_cnt)