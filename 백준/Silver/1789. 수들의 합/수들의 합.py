import sys

s = int(sys.stdin.readline())

num = 1
while s > 0:
    s -= num
    num += 1

if s == 0:
    print(num - 1)
else:
    print(num - 2)