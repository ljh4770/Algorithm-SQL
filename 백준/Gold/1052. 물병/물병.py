n, k = map(int, input().split())

cur = n
cnt = 0
while bin(cur).count('1') > k:
    cur += 1
    cnt += 1

print(cnt)