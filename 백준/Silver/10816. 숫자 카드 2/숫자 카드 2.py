import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().strip().split()))
M = int(input())
queries = list(map(int, input().strip().split()))

cnt = Counter(cards)

res = []
for q in queries:
    res.append(str(cnt[q]))

print(' '.join(res))