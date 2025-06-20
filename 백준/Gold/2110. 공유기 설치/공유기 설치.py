import sys; input = sys.stdin.readline


n, c = map(int, input().split(' '))
house = [int(input()) for _ in range(n)]
house.sort()

start, end = 1, house[-1] - house[0]
result = 0
while start <= end:
    mid = (start + end) // 2
    cur = house[0]
    cnt = 1

    for i in range(1, n):
        if house[i] >= cur + mid:
            cnt += 1
            cur = house[i]
    
    if cnt >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)
 