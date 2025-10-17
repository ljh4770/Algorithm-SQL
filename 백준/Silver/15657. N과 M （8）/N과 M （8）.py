def tracking(idx):
    global n

    if len(perm) == m:
        print(*perm)
        return
    
    for i in range(idx, n):
        perm.append(arr[i])
        tracking(i)
        perm.pop()


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [*map(int, input().split())]
    arr.sort()

    perm = []
    tracking(0)