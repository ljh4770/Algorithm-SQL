import sys; input = sys.stdin.readline
from collections import Counter

setence = input().rstrip() # len(setence) : [1, 50]
n = int(input()) # n : [1, 50]
words = [input().rstrip() for _ in range(n)] # len(word) : [1, 50]

INF = float('inf')
len_sentence = len(setence)
dp = [0] + [INF] * len_sentence

for i in range(1, len_sentence + 1, 1):
    sub_sentence = setence[:i]
    for word in words:
        len_word = len(word)
        if len_word > i:
            # word is longer than sub_sentence
            continue
        
        cnt_sub = Counter(sub_sentence[-len_word:]) # Counter the sub_sentence
        cnt_word = Counter(word) # Counter the word
        # Check if all alpabet is include and the count is same
        for c, cnt in cnt_sub.items():
            if c not in cnt_word:
                break # not match
            if cnt_sub[c] != cnt_word[c]:
                break # not match
        else:
            # match -> calculate the cost and assign to dp
            cost = 0
            for j in range(1, len_word + 1, 1):
                if word[-j] != sub_sentence[-j]:
                    cost += 1
            if dp[i - len_word] != INF:
                cum_cost = cost + (0 if dp[i - len_word] == INF else dp[i - len_word])
                dp[i] = min(dp[i], dp[i - len_word] + cost)
print(dp[-1] if dp[-1] != INF else -1)