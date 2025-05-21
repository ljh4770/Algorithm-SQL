if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n = int(input())
    arr = [tuple(map(int, input().split(' '))) for _ in range(n)]
    arr.sort(key=lambda x: (x[1], x[0]))

    for x, y in arr:
        print(x, y)