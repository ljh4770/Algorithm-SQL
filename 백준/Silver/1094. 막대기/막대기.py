x = int(input()) # x : [1, 64]

answer = 0
while x > 0:
    if x % 2 == 1:
        answer += 1
    x = x >> 1

print(answer)