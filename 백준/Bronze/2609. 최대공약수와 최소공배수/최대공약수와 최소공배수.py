def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return int(a * b / gcd(a, b))

if __name__ == '__main__':
    import sys

    x, y = map(int, sys.stdin.readline().split(' '))
    print(gcd(x, y))
    print(lcm(x, y))

