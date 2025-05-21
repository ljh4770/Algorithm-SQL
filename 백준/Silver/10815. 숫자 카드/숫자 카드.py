def binary_search(A, q):
    l = 0
    h = len(A) - 1

    while l <= h:
        idx = (l + h) // 2
        if A[idx] == q:
            return True
        
        if A[idx] > q:
            h = idx - 1
        else:
            l = idx + 1

    return False


if __name__ == '__main__':
    import sys

    input = sys.stdin.readline

    N = int(input())
    cards = list(map(int, input().strip().split()))
    M = int(input())
    queries = list(map(int, input().strip().split()))

    cards.sort()
    res = []
    for q in queries:
        if binary_search(cards, q):
            res.append('1')
        else:
            res.append('0')

    print(' '.join(res))