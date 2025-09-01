n, m = map(int, input().split())
arr = [*map(int, input().split())]

cnt = 0 
sum_ = 0
j = 0
for i in range(n):
    while sum_ < m and j < n:
        sum_ += arr[j]
        j += 1
    if sum_ == m:
        cnt += 1
    sum_ -= arr[i]

print(cnt)