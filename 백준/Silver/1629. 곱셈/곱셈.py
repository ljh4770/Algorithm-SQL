def sol(num, pow, div):
    if pow == 1:
        return num % div
    
    tmp = sol(num, pow // 2, div)

    if pow % 2 == 1:
        return ((tmp * tmp) % c) * a % c
    else:
        return (tmp * tmp) % c

if __name__ == '__main__':
    import sys

    a, b, c = map(int, sys.stdin.readline().split(' '))

    print(sol(a, b, c))