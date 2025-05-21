import sys

s = sys.stdin.readline().rstrip()

if len(s) == 1:
    print(0)
    sys.exit(0)

cnt0 = 0
cnt1 = 0
prev = s[0]
if prev == '1':
    cnt1 += 1
else:
    cnt0 += 1

for c in s[1:]:
    if c == prev:
        continue
    else:
        if c == '1':
            cnt1 += 1
        else:
            cnt0 += 1
        prev = c

print(min(cnt0, cnt1))