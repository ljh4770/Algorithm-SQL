def tracking(pw, idx):
    global l, c, chars
    global visited, mos

    if len(pw) == l:
        mo_cnt = 0
        for char in pw:
            if char in mos:
                mo_cnt += 1
        ja_cnt = l - mo_cnt
        if mo_cnt < 1 or ja_cnt < 2:
            return
        print(pw)
        return
    
    for i in range(idx, c, 1):
        if visited[i]:
            continue
        pw += chars[i]
        visited[i] = True
        tracking(pw, i + 1)
        visited[i] = False
        pw = pw[:-1]


if __name__ == '__main__':
    l, c = map(int, input().split())
    chars = input().rstrip().split()
    chars.sort()
    
    visited = [False] * c

    mos = 'aeiou'
    tracking('', 0)