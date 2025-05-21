import sys
input = sys.stdin.readline

k, n = map(int, input().split(' '))
sizes = [int(input()) for _ in range(k)]

low = 1
high = max(sizes)

while low <= high:
    mid = (low + high) // 2
    cnt = 0

    for size in sizes:
        cnt += size // mid
    
    if cnt >= n:
        low = mid + 1
    else:
        high = mid - 1
print(high)