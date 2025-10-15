def tracking(idx):
    global n, m, perm

    if len(perm) == m:
        print(*perm)
        return
    
    for i in range(idx, n, 1):
        perm.append(arr[i])
        tracking(i + 1)
        perm.pop()
    

if __name__ == "__main__":
    import sys; input = sys.stdin.readline

    n, m = map(int, input().split())
    arr = [*map(int, input().split())]
    arr.sort()

    perm = []
    tracking(0)