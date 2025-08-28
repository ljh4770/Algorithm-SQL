stream = input().split('.')
result = []

for chunk in stream:
    if not chunk:
        result.append('')
        continue
    n = len(chunk)
    tmp = ''
    while n >= 4:
        tmp += 'AAAA'
        n -= 4
    while n >= 2:
        tmp += 'BB'
        n -= 2
    result.append(tmp)
    if n > 0 :
        print(-1)
        exit(0)
print('.'.join(result))