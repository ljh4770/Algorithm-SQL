target = input().rstrip()

answer = ''
for t in target:
    if 'a' <= t <= 'z':
        t = ord(t) + 13
        if t > 122:
            t -= 26
        answer += chr(t)
    elif 'A' <= t <= 'Z':
        t = ord(t) + 13
        if t > 90:
            t -= 26
        answer += chr(t)
    else:
        answer += t
print(answer)