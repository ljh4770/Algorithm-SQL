import sys; input = sys.stdin.readline

n = int(input())

MAX_LEN = 10 ** 6
pos_cnt = [0] * (MAX_LEN + 1)
neg_cnt = [0] * (MAX_LEN + 1)
zero_cnt = 0

for _ in range(n):
    num = int(input())
    if num > 0:
        pos_cnt[num] += 1
    elif num < 0:
        neg_cnt[num] += 1
    else:
        zero_cnt += 1

for num in range(MAX_LEN, 0, -1):
    arr = [num] * pos_cnt[num]
    if arr:
        print(*arr, sep='\n')

arr = [0] * zero_cnt
if arr:
    print(*arr, sep='\n')

for num in range(-1, -1 * MAX_LEN - 1, -1):
    arr = [num] * neg_cnt[num]
    if arr:
        print(*arr, sep='\n')