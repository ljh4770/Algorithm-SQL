import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))
cards = list(map(int, input().split(' ')))

answer = 0
for a in range(n - 2):
    for b in range(a + 1, n - 1, 1):
        for c in range(b + 1, n, 1):
            tmp_sum = cards[a] + cards[b] + cards[c]
            if tmp_sum <= m:
                answer = max(answer, tmp_sum)
print(answer)