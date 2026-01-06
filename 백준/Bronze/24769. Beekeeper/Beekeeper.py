import sys; input = sys.stdin.readline


DOUBLE_VOWEL = {'aa', 'ee', 'ii', 'oo', 'uu', 'yy'}

def check(word):
    cnt = 0
    for i in range(len(word) - 1):
        if word[i:i + 2] in DOUBLE_VOWEL:
            cnt += 1

    return cnt


if __name__ == "__main__":
    while True:
        n = int(input())
        if n == 0:
            break
        
        max_cnt = -1
        best_word = ''
        for _ in range(n):
            word = input().rstrip()
            cnt = check(word)
            if cnt > max_cnt:
                max_cnt = cnt
                best_word = word
            
        print(best_word)