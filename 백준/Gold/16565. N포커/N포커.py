MOD = 10007
n = int(input())

comb = [[0]*53 for _ in range(53)]
comb[0][0] = 1
comb[1][0] = 1
comb[1][1] = 1

for i in range(2, 53) :
    comb[i][0] = 1
    comb[i][i] = 1

    for j in range(1, i) :
        comb[i][j] = comb[i - 1][j] + comb[i - 1][j - 1]

result = 0
cnt, pos = 1, 1

while n >= 4 :
    result += pos * comb[13][cnt] * comb[52 - cnt * 4][n - 4]
    cnt += 1
    pos = -pos
    n -= 4

print(result % MOD)