n = input()
p = len(n)
digit_cnt = [0] * 10

for d in n:
    p -= 1

    for i in range(int(d)):
        digit_cnt[i] += 10 ** p
        if p == 0:
            continue
        for j in range(10):
            digit_cnt[j] += p * (10 ** (p - 1))
    digit_cnt[0] -= 10 ** p

    if p:
        digit_cnt[int(d)] += (int(''.join(n[-p:])) + 1)
    else:
        digit_cnt[int(d)] += 1

print(*digit_cnt)