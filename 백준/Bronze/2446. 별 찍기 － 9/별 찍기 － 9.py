import sys
n = int(sys.stdin.readline())

for i in range(n, 0, -1):
    for j in range(n - i):
        print(' ', end='')
    print('*' * (2 * i - 1), end=' ')
    print()
for i in range(2, n + 1, 1):
    for j in range(n - i):
        print(' ', end='')
    print('*' * (2 * i - 1), end=' ')
    print()