import sys
input = sys.stdin.readline

def manacher_odd(arr):
    n = len(arr)
    d1 = [0]*n
    l, r = 0, -1
    for i in range(n):
        k = 1 if i > r else min(d1[l+r-i], r - i + 1)
        while 0 <= i-k and i+k < n and arr[i-k] == arr[i+k]:
            k += 1
        d1[i] = k
        k -= 1
        if i + k > r:
            l = i - k
            r = i + k
    return d1

def manacher_even(arr):
    n = len(arr)
    d2 = [0]*n
    l, r = 0, -1
    for i in range(n):
        k = 0 if i > r else min(d2[l+r - i + 1], r - i + 1)
        while 0 <= i-k-1 and i+k < n and arr[i-k-1] == arr[i+k]:
            k += 1
        d2[i] = k
        k -= 1
        if i + k > r:
            l = i - k - 1
            r = i + k
    return d2

def solve():
    N = int(input())
    arr = list(map(int, input().split()))
    M = int(input())

    # 1. Manacher 전처리
    d1 = manacher_odd(arr)   # 홀수 길이
    d2 = manacher_even(arr)  # 짝수 길이

    # 2. 질의 처리
    #   S, E (1-based) → s, e (0-based)
    #   길이 L = e-s+1
    #   홀수면 center = (s+e)//2, 필요한 반지름 = (L+1)//2
    #   짝수면 center = (s+e+1)//2, 필요한 반지름 = L//2

    out = []
    for _ in range(M):
        S, E = map(int, input().split())
        s, e = S-1, E-1
        length = e - s + 1

        if length == 1:
            out.append('1')  # 길이 1은 항상 팰린드롬
            continue

        if length % 2 == 1:
            # 홀수 길이
            center = (s + e) // 2
            needed = (length + 1) // 2
            if d1[center] >= needed:
                out.append('1')
            else:
                out.append('0')
        else:
            # 짝수 길이
            center = (s + e + 1) // 2
            needed = length // 2
            if d2[center] >= needed:
                out.append('1')
            else:
                out.append('0')

    print('\n'.join(out))

if __name__ == "__main__":
    solve()
