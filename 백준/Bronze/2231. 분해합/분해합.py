def get_gen(n):
    for i in range(1, n, 1):
        digits = list(map(int, list(str(i))))
        tmp = i
        for d in digits:
            tmp += d
        if tmp == n:
            return i
    return 0

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n = int(input())
    print(get_gen(n))