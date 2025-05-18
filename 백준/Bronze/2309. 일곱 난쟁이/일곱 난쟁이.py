import sys
sys.setrecursionlimit(10 ** 3)

def tracking(cur, k):
    if k == 2:
        sum_ = 0
        real = []
        for i, v in enumerate(visited):
            if v == False:
                sum_ += heights[i]
                real.append(heights[i])
        if sum_ == 100:
            return real
        else:
            return None
        
    for nxt in range(cur, 9, 1):
        if visited[nxt] == False:
            visited[nxt] = True
            real = tracking(nxt + 1, k + 1)
            visited[nxt] = False
            if real:
                return real
    return None

if __name__ == '__main__':
    input = sys.stdin.readline

    heights = [int(input()) for _ in range(9)]
    visited = [False] * 9

    real = tracking(0, 0)
    real.sort()
    for h in real:
        print(h)