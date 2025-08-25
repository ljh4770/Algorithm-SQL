import sys
sys.setrecursionlimit(10 ** 6)

def solve(arr, d):
    global tree

    n = len(arr)
    idx = n // 2
    tree[d].append(arr[idx])
    if n > 1:
        solve(arr[:idx], d + 1)
        solve(arr[idx + 1:], d + 1)

if __name__ == '__main__':
    k = int(input()) # level of tree
    inorder_traverse = [*map(int, input().split())]
    tree = [[] for _ in range(k)]
    solve(inorder_traverse, 0)

    for depth in tree:
        print(*depth)