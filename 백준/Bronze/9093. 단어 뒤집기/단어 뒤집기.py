import sys; input = sys.stdin.readline

t = int(input())

for _ in range(t):
    sentence = input().rstrip()
    words = sentence.split(' ')
    for word in words:
        print(word[::-1], end=' ')
    print()