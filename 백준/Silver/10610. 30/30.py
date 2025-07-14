n = input()

if '0' not in n:
    print(-1)
    exit(0)

sum_ = 0
for c in n:
    sum_ += int(c)

if sum_ % 3 != 0:
    print(-1)
    exit(0)

print(''.join(sorted(n, reverse=True)))