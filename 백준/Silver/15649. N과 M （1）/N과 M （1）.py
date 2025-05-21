def tracking():
    global m, selected
    if len(selected) == m:
        print(' '.join(map(str, selected)))
        return
    
    global n
    for num in range(1, n + 1, 1):
        if visited[num] == True:
            continue
        visited[num] = True
        selected.append(num)
        tracking()
        selected.pop()
        visited[num] = False

if __name__ == '__main__':
    import sys
    n, m = map(int, sys.stdin.readline().split(' '))
    visited = [False] * (n + 1)
    selected = []
    tracking()