def calc(arr):
    res = 0
    for i in range(1, n, 1):
        res += abs(arr[i] - arr[i - 1])
    
    return res

def tracking():
    global n, arr, perm, visited, answer

    if len(perm) == n:
        answer = max(answer, calc(perm))
        return

    for i in range(n):
        if visited[i]:
            continue

        visited[i] = True
        perm.append(arr[i])
        tracking()
        perm.pop()
        visited[i] = False


if __name__ == "__main__":
    import sys; input = sys.stdin.readline

    n = int(input())
    arr = [*map(int, input().split())]

    perm = []
    visited = [False] * n
    answer = 0
    tracking()
    print(answer)