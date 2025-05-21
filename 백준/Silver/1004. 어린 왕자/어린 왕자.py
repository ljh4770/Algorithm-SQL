def L2(a1, b1, a2, b2):
    return (a1 - a2) ** 2 + (b1 - b2) ** 2

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        x1, y1, x2, y2 = map(int, input().split())
        n = int(input())

        cnt = 0
        for _ in range(n):
            x, y, r = map(int, input().split())

            if L2(x1, y1, x, y) <= r ** 2 and L2(x2, y2, x, y) <= r ** 2:
                continue
            elif L2(x1, y1, x, y) <= r ** 2 or L2(x2, y2, x, y) <= r ** 2:
                cnt += 1
        print(cnt)