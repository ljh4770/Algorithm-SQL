import sys; input = sys.stdin.readline
from collections import Counter

n, m = map(int, input().split())
words = []
for _ in range(n):
    word = input().rstrip()
    if len(word) >= m:
        words.append(word)


word_cnt = Counter(words)
word_cnt = sorted(word_cnt.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for word, cnt in word_cnt:
    print(word)
