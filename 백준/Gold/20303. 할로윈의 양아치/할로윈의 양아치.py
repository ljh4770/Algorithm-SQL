from collections import deque

def connect(x):
    x_friend = 1
    x_candy = candies[x]
    q = deque()
    q.append(x)
    
    checked[x] = 1

    while q:
        cur = q.popleft()
        for i in friend[cur]:
            if checked[i] == 0:
                q.append(i)
                checked[i] = 1
                x_friend += 1
                x_candy += candies[i]

    return [x_friend, x_candy]


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n, m, k = map(int,input().split(' '))
    candies = [0] + list(map(int,input().split(' ')))

    friend = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int,input().split(' '))
        friend[a].append(b)
        friend[b].append(a)

    child_group = []
    checked = [0] * (n + 1)
    for i in range(1, n + 1):
        if checked[i] == 0:
            child_group.append(connect(i))

    dp = [0 for _ in range(k + 1)]
    for i in range(len(child_group)):
        child_cnt,candy_cnt = child_group[i]
        for j in range(k,child_cnt - 1, -1):
            dp[j] = max(dp[j - child_cnt] + candy_cnt, dp[j])

    print(dp[k - 1])