import sys; input = sys.stdin.readline


n = int(input())

answer = 0
start, end = 1, n // 2
while True:
    mid = (start + end) // 2
    n_sq = mid ** 2

    if n_sq == n:
        answer = mid
        break
    elif n_sq < n:
        start = mid
    else:
        end = mid

print(answer)