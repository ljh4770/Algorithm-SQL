import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split(' ')))
min_ = -1000 - 1

cur_sum = arr[0]
max_sum = arr[0]

for i in range(1, n, 1):
    cur_sum = max(arr[i], cur_sum + arr[i])
    max_sum = max(max_sum, cur_sum)
print(max_sum)