from collections import deque

def bfs(length, a, b):
    q = deque()
    q.append((a, 0))

    while q:
        x, t = q.popleft()

        if x > b:
            continue

        if x == b:
            return t

        q.append((int(str(x) + '1'), t + 1))
        q.append((x * 2, t + 1))

    return -1

if __name__ == '__main__':
    import sys
    a, b = map(int, sys.stdin.readline().split(' '))

    time = bfs(10**9 + 1, a, b)
    if time == -1:
        print(time)
    else:
        print(time + 1)