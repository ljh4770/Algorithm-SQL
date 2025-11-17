def tracking(start, now, value, cnt):
    global answer
    if cnt == n:
        if weights[now][start]:
            value += weights[now][start]
            if answer > value:
                answer = value
        return

    if value > answer:
        return

    for i in range(n):
        if visited[i] or not weights[now][i]:
            continue
        visited[i] = True
        tracking(start, i, value + weights[now][i], cnt + 1)
        visited[i] = False


if __name__ == "__main__":
    import sys; input = sys.stdin.readline

    n = int(input())
    weights = [[*map(int, input().split())] for _ in range(n)]
    
    perm = []
    visited = [False] * n
    answer = float('inf')
    for i in range(n):
        visited[i] = True
        tracking(i, i, 0, 1)
        visited[i] = False
    print(answer)