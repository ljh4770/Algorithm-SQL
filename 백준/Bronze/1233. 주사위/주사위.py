a, b, c = map(int, input().split())

cnts = dict()
for i in range(1, a + 1, 1):
    for j in range(1, b + 1, 1):
        for k in range(1, c + 1, 1):
            sum_ = i + j + k
            if sum_ not in cnts:
                cnts[sum_] = 0
            cnts[sum_] += 1

max_cnt = 0
min_mode = 0

for sum_, cnt in cnts.items():
    if cnt > max_cnt:
        max_cnt = cnt
        min_mode = sum_
    elif cnt == max_cnt:
        min_mode = min(min_mode, sum_)
print(min_mode)