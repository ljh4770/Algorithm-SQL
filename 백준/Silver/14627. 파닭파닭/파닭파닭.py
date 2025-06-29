import sys; input = sys.stdin.readline

# s <= c
s, c = map(int, input().split())
pa = [int(input()) for _ in range(s)]

result = 0
start, end = 1, max(pa)
while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for i in pa:
        cnt += i // mid
    
    if cnt >= c:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

ramen = sum(pa) - c * result
print(ramen)