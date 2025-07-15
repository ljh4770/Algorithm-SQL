e, s, m = map(int, input().split())

year = 1
target_year = (e, s, m)
e, s, m = 1, 1, 1
while target_year != (e, s, m):
    year += 1
    e += 1; s += 1; m += 1
    if e > 15:
        e = 1
    if s > 28:
        s = 1
    if m > 19:
        m = 1
print(year)