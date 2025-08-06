import sys; input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))
cache = {}


def find_permutations(n):
    if n in cache:
        return cache[n]

    elif n <= 1:
        return 1

    else:
        cache[n] = n * find_permutations(n - 1)
        return cache[n]


if data[0] == 1:
    k = data[1]
    arr = [x for x in range(1, n + 1)]
    ans = []

    for i in range(n):
        x = find_permutations(n - 1 - i)
        step = (k - 1) // x
        ans.append(arr[step])
        arr.remove(arr[step])
        k -= x * step

    print(*ans)

else:
    input_permu = data[1:]
    sort_permu = sorted(data[1:])
    ans = 1

    for i in range(n):
        step = sort_permu.index(input_permu[i])
        sort_permu.remove(input_permu[i])
        x = find_permutations(n - 1 - i)
        ans += x * step

    print(ans)