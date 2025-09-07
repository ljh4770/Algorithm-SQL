import sys; input = sys.stdin.readline

n = int(input())
arr = [*map(int, input().split())]
x = int(input())
arr.sort()

cnt = 0
l, r = 0, n - 1
while l < r:
    sum_ = arr[l] + arr[r]
    if sum_ == x:
        cnt += 1
        l += 1
    elif sum_ > x:
        r -= 1
    else:
        l += 1
print(cnt)