if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n = int(input())
    words = list(set([input().rstrip() for _ in range(n)]))
    len_words = [0] * n
    mapping = []

    for i, word in enumerate(words):
        item = (len(word), word)
        mapping.append(item)
    mapping.sort(key=lambda x: (x[0], x[1]))

    for len_word, word in mapping:
        print(word)