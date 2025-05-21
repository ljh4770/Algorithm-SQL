import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    ox = sys.stdin.readline().rstrip()
    len_ox = len(ox)
    scores = [0] * len_ox

    for i in range(len_ox):
        c = ox[i]
        if c == 'O':
            score = scores[i - 1] + 1
        else:
            score = 0
        scores[i] = score
        
    print(sum(scores))