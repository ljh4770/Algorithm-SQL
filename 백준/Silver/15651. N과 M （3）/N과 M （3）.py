def tracking():
    global m, selected
    if len(selected) == m:
        print(' '.join(map(str, selected)))
        return
    
    global n
    for num in range(1, n + 1, 1):
        selected.append(num)
        tracking()
        selected.pop()

if __name__ == '__main__':
    import sys
    n, m = map(int, sys.stdin.readline().split(' '))

    selected = []
    tracking()