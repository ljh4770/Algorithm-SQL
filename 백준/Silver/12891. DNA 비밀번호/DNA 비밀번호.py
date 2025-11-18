import sys; input = sys.stdin.readline
from collections import deque

s, p = map(int, input().split())
dna_string = input().rstrip()
a, c, g, t = map(int, input().split())

actg_cnt = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
for i in range(p - 1):
    actg_cnt[dna_string[i]] += 1

cnt = 0
start, end = 0, p - 1
while end < s:
    actg_cnt[dna_string[end]] += 1
    if (
        (actg_cnt['A'] >= a) and (actg_cnt['C'] >= c)
        and (actg_cnt['G'] >= g) and (actg_cnt['T'] >= t)
    ):
        cnt += 1
    actg_cnt[dna_string[start]] -= 1
    start += 1
    end += 1

print(cnt)