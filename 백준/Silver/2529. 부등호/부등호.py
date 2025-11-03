def is_valid(a, b, sym):
    if sym == '<':
        if a >= b:
            return False
    elif sym == '>':
        if a <= b:
            return False
    
    return True


def tracking(cnt):
    global m, perm, symbols, answers

    if cnt == m:
        answers.append(int(''.join([str(num) for num in perm])))
        return 

    for num in range(10):
        if visited[num]:
            continue
        
        if cnt == 0 or is_valid(perm[cnt - 1], num, symbols[cnt - 1]):
            visited[num] = True
            perm.append(num)
            tracking(cnt + 1)
            perm.pop()
            visited[num] = False


if __name__ == "__main__":
    import sys; input = sys.stdin.readline

    k = int(input())
    symbols = list(input().rstrip().split())

    m = k + 1

    perm = []
    visited = [False] * 10
    answers = []
    tracking(0)
    print(str(answers[-1]).zfill(m))
    print(str(answers[0]).zfill(m))
