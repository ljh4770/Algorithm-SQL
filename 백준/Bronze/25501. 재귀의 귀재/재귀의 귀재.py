import sys
sys.setrecursionlimit(10**9)

def recursion(target, l, r):
    global cnt
    cnt += 1
    if l >= r:
        return 1
    elif target[l] != target[r]:
        return 0
    return recursion(target, l + 1, r - 1)

def is_palindrome(target):
    return recursion(target, 0, len(target) - 1)


if __name__ == '__main__':
    input = sys.stdin.readline

    t = int(input()) # t : [1, 1000]
    # len(s) : [1, 1000]
    testcases = [input().rstrip() for _ in range(t)]
    
    for s in testcases:
        cnt = 0
        res = is_palindrome(s)
        print(res, cnt)