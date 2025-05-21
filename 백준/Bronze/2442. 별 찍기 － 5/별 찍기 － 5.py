import sys
n = int(sys.stdin.readline())

for i in range(1, n + 1, 1):
    for j in range(0, n - i, 1):
        print(' ', end='')
    for j in range(2 * i - 1):
        print('*', end='')
    print(' ')