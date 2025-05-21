import sys
input = sys.stdin.readline

n = int(input())
data = [int(input()) for _ in range(n)]

pos_cnt = [0] * (1000 + 1)
zero_cnt = 0
neg_cnt = [0] * (1000 + 1)
for num in data:
    if num > 0:
        pos_cnt[num] += 1
    elif num == 0:
        zero_cnt += 1
    else:
        neg_cnt[abs(num)] += 1

for num in range(1000, 0, -1):
    for i in range(neg_cnt[num]):
        print(-num)

for i in range(zero_cnt):
    print(0)

for num in range(1, 1000 + 1, 1):
    for i in range(pos_cnt[num]):
        print(num)