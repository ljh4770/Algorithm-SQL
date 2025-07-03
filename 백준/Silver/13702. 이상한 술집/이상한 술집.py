import sys; input = sys.stdin.readline

n, k = map(int, input().split(' '))
amts = [int(input()) for _ in range(n)]

result = 1
start, end = 1, max(amts)
while start <= end:
    mid = (start + end) // 2
    cnt = 0 
    
    for a in amts:
        cnt += (a // mid)
    
    if cnt >= k:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)