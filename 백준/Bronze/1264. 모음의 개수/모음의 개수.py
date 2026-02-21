from collections import Counter


vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
while True:
    word_cnt = Counter(input())
    if '#' in word_cnt:
        break

    cnt = 0

    for v in vowels:
        cnt += word_cnt[v]
    
    print(cnt)
