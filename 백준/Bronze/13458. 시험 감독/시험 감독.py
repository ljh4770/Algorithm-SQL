import sys
input = sys.stdin.readline

n = int(input())
a = [*map(int, input().split(' '))]
b, c = map(int, input().split(' '))

answer = 0

for num in a:
    if num <= b:
        answer += 1
    else:
        answer += 1
        num -= b
        q, r = divmod(num, c)
        answer += q
        if r > 0:
            answer += 1

print(answer)