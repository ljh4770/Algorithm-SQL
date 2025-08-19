import sys; input = sys.stdin.readline
n = int(input())
options = [input().rstrip() for _ in range(n)]

hot_keys = set()
for option in options:
    words = option.split()
    flag = False

    for i, word in enumerate(words):
        candi = word[0].lower()
        if candi not in hot_keys:
            hot_keys.add(candi)
            words[i] = '[' + word[0] + ']' + word[1:]
            option = ' '.join(words)
            flag = True
            break
    
    if not flag:
        for i in range(len(option)):
            if option[i] == ' ':
                continue
            candi = option[i].lower()
            if candi not in hot_keys:
                hot_keys.add(candi)
                option = option[:i] + '[' + option[i] + ']' + option[i + 1:]
                break
    print(option)