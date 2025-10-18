def tracking(idx):
    global n, m, perm

    if len(perm) == m:
        print(*perm)
        return

    tmp = 0
    for i in range(idx, n, 1):
        if visited[i] or tmp == arr[i]:
            continue

        tmp = arr[i]
        visited[i] = True
        perm.append(tmp)
        tracking(i + 1)
        perm.pop()
        visited[i] = False


if __name__ == "__main__":
    import sys; input = sys.stdin.readline

    n, m = map(int, input().split())
    arr = [*map(int, input().split())]
    arr.sort()

    visited = [False] * n
    perm = []
    tracking(0)