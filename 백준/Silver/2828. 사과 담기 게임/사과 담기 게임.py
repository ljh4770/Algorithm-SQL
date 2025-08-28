import sys; input = sys.stdin.readline

n, m = map(int, input().split())
j = int(input())
apples = [int(input()) for _ in range(j)]

basket = (1, m)
cnt = 0
for pos in apples:
    if basket[0] <= pos <= basket[1]:
        continue

    if pos > basket[1]:
        cnt += pos - basket[1]
        basket = (pos - m + 1, pos)
    else:
        cnt += basket[0] - pos
        basket = (pos, pos + m - 1)
print(cnt)