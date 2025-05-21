import sys
input = sys.stdin.readline

N, M, B = map(int, input().split(' '))
# N x M arr
freq = [0] * 257
for _ in range(N):
    row = list(map(int, input().rstrip().split(' ')))
    for h in row:
        freq[h] += 1

min_time = float('inf')
answer = 0


for h in range(0, 257, 1):
    remove_total = 0
    add_total = 0

    for x in range(257):
        if freq[x] == 0:
            continue
        if x < h:
            add_total += (h - x) * freq[x]
        else:
            remove_total += (x - h) * freq[x]
    
    if remove_total + B < add_total:
        continue

    time = remove_total * 2 + add_total

    if time < min_time:
        min_time = time
        answer = h
    elif time == min_time and h > answer:
        answer = h

print(min_time, answer)
