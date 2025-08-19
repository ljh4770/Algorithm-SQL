# l : [1, 2 * 10 ** 9], r : [l, 2 * 10 ** 9]
l, r = map(str, input().rstrip().split())

if len(l) != len(r):
    print(0)
    exit(0)

cnt = 0
for i in range(len(l)):
    if l[i] == r[i] and l[i] !='8':
        continue
    if l[i] == '8' and r[i] =='8':
        cnt += 1
    else:
        break
print(cnt)