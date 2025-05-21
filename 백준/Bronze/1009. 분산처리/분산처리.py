def find_cycle(a, d = 10):
    org = a % d
    checked = [org]

    while True:
        a = (a * org) % d
        if a in checked:
            break
        checked.append(a)
    
    return checked

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    t = int(input())
    inputs = [tuple(map(int, input().split(' '))) for _ in range(t)]

    for a, b in inputs:
        cycle = find_cycle(a)
        r = b % len(cycle)
        answer = cycle[r - 1]
        if answer == 0:
            print(10)
        else:
            print(answer)