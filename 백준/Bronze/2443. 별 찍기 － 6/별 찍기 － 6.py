n = int(input())

for i in range(n, 0, -1):
    b = n - i
    print(' ' * b, end='')
    print('*' * (2 * i - 1))