from math import comb

def binomial(k, p):
    return comb(18, k) * (p ** k) * ((1 - p) ** (18 - k))

PRIMES = [2, 3, 5, 7, 11, 13, 17]

a = int(input()) / 100
b = int(input()) / 100

exclusive = 0
for i in range(0, 19):
    if i in PRIMES:
        continue
    for j in range(0, 19):
        if j in PRIMES:
            continue
        prob_a = binomial(i, a)
        prob_b = binomial(j, b)
        exclusive += prob_a * prob_b
print(1 - exclusive)