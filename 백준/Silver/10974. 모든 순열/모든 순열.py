def tracking():
    global n

    if len(perm) == n:
        print(*perm)
        return
    
    for num in range(1, n + 1, 1):
        if visited[num]:
            continue

        visited[num] = True
        perm.append(num)
        tracking()
        perm.pop()
        visited[num] = False


if __name__ == "__main__":
    n = int(input())

    perm = []
    visited = [False] * (n + 1)
    tracking()