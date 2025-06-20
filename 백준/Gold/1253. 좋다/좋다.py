import sys; input = sys.stdin.readline

n = int(input())
arr = [*map(int, input().split(' '))]
arr.sort()

cnt = 0
for i in range(n):
    cur = arr[i]
    start, end = 0, n - 1

    while start < end:
        if arr[start] + arr[end] == cur:
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                cnt += 1
                break
        elif arr[start] + arr[end] > cur:
            end -= 1
        elif arr[start] + arr[end] < cur:
            start += 1

print(cnt)