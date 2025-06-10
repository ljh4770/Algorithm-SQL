import sys
input = sys.stdin.readline

n = int(input())
pivot_word = list(input())
pivot_len = len(pivot_word)

for _ in range(n - 1):
    word = list(input())
    for j in range(pivot_len):
        if pivot_word[j] != word[j]:
            pivot_word[j] = '?'
print(*pivot_word, sep='')