import sys; input = sys.stdin.readline

n, k = map(int, input().split())
lvs = [int(input()) for _ in range(n)]

answer = 0
start = min(lvs)
end = start + k
while start <= end:
    mid = (start + end) // 2

    available_lv = k
    for lv in lvs:
        if lv < mid:
            available_lv -= mid - lv
    
    if available_lv >= 0:
        answer = max(answer, mid)
        start = mid + 1
    else:
        end = mid - 1
    
print(answer)