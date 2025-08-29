import sys; input = sys.stdin.readline

n, m = map(int, input().split())
prices = [tuple(map(int, input().split())) for _ in range(m)]

INF = float('inf')
min_six = INF
min_one = INF
for six, one in prices:
    min_six = min(min_six, six)
    min_one = min(min_one, one)

if min_six <= min_one * 6:
    q, r = divmod(n, 6)
    result = min_six * q
    if min_six <= min_one * r:
        result += min_six
    else:
        result += min_one * r
else:
    result = min_one * n

print(result)