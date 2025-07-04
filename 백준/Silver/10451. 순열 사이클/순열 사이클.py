from collections import deque

def bfs(perm, visited, start):
    q = deque()
    q.append(start)
    visited[start] = start

    while q:
        cur = q.popleft()

        nxt = perm[cur]
        if cur == nxt:
            break
        
        if visited[nxt] == 0:
            if cur != nxt:
                q.append(nxt)
                visited[nxt] = start
        else:
            visited[cur] = visited[nxt]

    
def count_cycle(n, perm):
    visited = [0] * (n + 1)
    
    cnt = 0
    for i in range(1, n + 1, 1):
        if visited[i] == 0:
            bfs(perm, visited, i)
            cnt += 1
    return cnt

def solve():
    n = int(input())
    perm = [0] + [*map(int, input().split(' '))]

    cnt = count_cycle(n, perm)
    print(cnt)

if __name__ == '__main__':
    import sys; input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        solve()