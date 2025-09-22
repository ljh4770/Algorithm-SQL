def tracking(idx):
    if len(perm) == m:
        print(*perm)
        return

    perm.append(arr[idx])
    tracking(idx)
    perm.pop()
    for _ in range(idx + 1, n, 1):
        perm.append(arr[_])
        tracking(idx)
        perm.pop()


if __name__ == "__main__":
    import sys; input = sys.stdin.readline

    n, m = map(int, input().split())
    arr = [*map(int, input().split())]
    arr.sort()

    perm = []
    tracking(0)