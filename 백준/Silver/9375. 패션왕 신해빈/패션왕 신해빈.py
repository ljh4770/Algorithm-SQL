def solve(clothes):
    kinds = dict()
    for name, kind in clothes:
        if kind not in kinds.keys():
            kinds[kind] = 1
        else:
            kinds[kind] += 1
    
    answer = 1
    for kind in kinds:
        answer *= (kinds[kind] + 1)
    return answer - 1


if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        n = int(input())
        clothes = [tuple(input().strip().split(' ')) for _ in range(n)]
        print(solve(clothes))