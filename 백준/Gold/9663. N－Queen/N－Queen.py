import sys
sys.setrecursionlimit(10**9)

def tracking(k):
    global n, answer
    global used_col, used_pos, used_neg
    if k == n:
        answer += 1
        return None
    
    for i in range(n):
        if used_col[i] or used_pos[k + i] or used_neg[(n - 1) + k - i]:
            continue
        used_col[i] = True
        used_pos[k + i] = True
        used_neg[(n - 1) + k - i] = True
        tracking(k + 1)
        used_col[i] = False
        used_pos[k + i] = False
        used_neg[(n - 1) + k - i] = False

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    used_col = [False] * n
    used_pos = [False] * (2 * n - 1)
    used_neg = [False] * (2 * n - 1)
    answer = 0
    tracking(0)
    print(answer)