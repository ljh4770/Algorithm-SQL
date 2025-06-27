import sys
sys.setrecursionlimit(10**9)

def OOB(x, y):
    return not (0 <= x < n and 0 <= y < n)

def upper_bound(diag):
    cnt = 0
    for d in range(diag, 2 * n - 1):
        for y in range(d + 1):
            x = d - y
            if OOB(x, y) == False and board[x][y] and back_slash[y - x] == 0:
                cnt += 1
                break
    return cnt

def tracking(diag, cnt):
    global answer
    if diag == 2 * n:
        answer = max(answer, cnt)
        return 
    
    ub = upper_bound(diag)
    if ub + cnt <= answer:
        return
    
    for x in range(diag + 1):
        y = diag - x
        if OOB(x, y) == True or board[x][y] == 0 or back_slash[y - x] == 1:
            continue
        back_slash[y - x] = 1
        tracking(diag + 1, cnt + 1)
        back_slash[y - x] = 0

    tracking(diag + 1, cnt)

if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    board = [[*map(int, input().split(' '))] for _ in range(n)]

    back_slash = dict()
    for i in range(-n + 1, n):
        back_slash[i] = 0
    
    answer = 0
    tracking(0, 0)
    print(answer)