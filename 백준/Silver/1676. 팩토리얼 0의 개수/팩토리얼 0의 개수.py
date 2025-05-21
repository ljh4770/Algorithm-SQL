import sys

n = int(sys.stdin.readline())

num2 = 0
num5 = 0
num10 = 0
for i in range(1, n + 1, 1):
    num = i
    while num % 10 == 0:
        num10 += 1
        num = num // 10
    while num % 5 == 0:
        num5 += 1
        num = num // 5
    while num % 2 == 0:
        num2 += 1
        num = num // 2

min_ = min(num2, num5)
print(num10 + min_)