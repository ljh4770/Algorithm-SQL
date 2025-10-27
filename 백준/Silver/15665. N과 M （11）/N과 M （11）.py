def tracking():
    global n, m, arr

    if len(perm) == m:
        print(*perm)
        return
    
    for i in range(n):
        perm.append(arr[i])
        tracking()
        perm.pop()


if __name__ == "__main__":
    import sys; input = sys.stdin.readline

    n, m = map(int, input().split())
    arr = [*set(map(int, input().split()))]
    arr.sort()

    perm = []
    n = len(arr)
    tracking()