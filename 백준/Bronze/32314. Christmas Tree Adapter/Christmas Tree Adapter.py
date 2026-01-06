a = int(input()) # [1, 20]
w, v = map(int, input().split()) # w: [1, 2000], v: [1, 100]

answer = 1 if a <= (w / v) else 0
print(answer)