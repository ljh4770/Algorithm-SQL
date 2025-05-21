from collections import Counter

x1, y1 = map(int, input().split(' '))
x2, y2 = map(int, input().split(' '))
x3, y3 = map(int, input().split(' '))

x = [x1, x2, x3]
y = [y1, y2, y3]

x_cnt = Counter(x)
y_cnt = Counter(y)

x_res = 0
y_res = 0

for i in range(3):
    if x_cnt[x[i]] == 1:
        x_res = x[i]
    if y_cnt[y[i]] == 1:
        y_res = y[i]

print(x_res, y_res)