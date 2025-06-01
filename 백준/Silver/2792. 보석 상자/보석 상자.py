import sys
input = sys.stdin.readline

# n: number of children
# m: number of jewel
n, m = map(int, input().split(' '))
jewels = [int(input()) for _ in range(m)] # Each item denote the number of jewels

minimal_jealousy = 0
start, end = 1, max(jewels)
while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for jewel in jewels:
        q, r = divmod(jewel, mid)
        cnt += q
        if r > 0:
            cnt += 1

    if cnt > n:
        start = mid + 1
    else:
        minimal_jealousy = mid
        end = mid - 1

print(minimal_jealousy)