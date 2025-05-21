def BEP(A, B, C):
    if B >= C:
        return -1

    return A // (C - B) + 1
    
if __name__ == '__main__':
    import sys

    A, B, C = map(int, sys.stdin.readline().split(' '))

    print(BEP(A, B, C))