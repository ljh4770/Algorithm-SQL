def hash(item):
    h = 0
    r = 31
    m = 1234567891
    for i, c in enumerate(item):
        num = ord(c) - ord('a') + 1
        h += num * (r ** i)
    return h % m

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n = int(input())
    item = input().rstrip()
    print(hash(item))