t = int(input())

for _ in range(t):
    res = int(input())
    n = int(input())
    for __ in range(n):
        p, q = map(int, input().split())
        res += p * q
    print(res)