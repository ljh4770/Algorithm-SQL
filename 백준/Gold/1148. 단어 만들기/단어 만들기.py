import sys; input = sys.stdin.readline
from collections import Counter


dictionary = []
while (word := input().strip()) != '-':
    dictionary.append(word)

dic_info = [(word, Counter(word)) for word in dictionary]

while (board := input().strip()) != '#':
    board_cnt = Counter(board)
    char_cnt = {c: 0 for c in board_cnt}

    for word, w_cnt in dic_info:
        if all(w_cnt[c] <= board_cnt.get(c, 0) for c in w_cnt):
            for c in w_cnt:
                if c in char_cnt:
                    char_cnt[c] += 1

    min_chars, min_cnt = [], float('inf')
    max_chars, max_cnt = [], 0
    for c, cnt in char_cnt.items():
        if cnt < min_cnt:
            min_chars = [c]
            min_cnt = cnt
        elif cnt == min_cnt:
            min_chars.append(c)
        
        if cnt > max_cnt:
            max_chars = [c]
            max_cnt = cnt
        elif cnt == max_cnt:
            max_chars.append(c)

    print(
        ''.join(sorted(min_chars)), min_cnt,
        ''.join(sorted(max_chars)), max_cnt
    )
