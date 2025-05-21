def find_parent(tree, next, parent):
    if len(next) == 0:
        return tree
    
    for node in next:
        tree[node].remove(parent)
        tree = find_parent(tree, tree[node], node)
    
    return tree

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n = int(input())
    edges = [tuple(map(int, input().split(' '))) for _ in range(n - 1)]
    tree = [[] for _ in range(n + 1)]

    for v, w, in edges:
        tree[v].append(w)
        tree[w].append(v)


    stack = []
    stack.append((tree[1], 1))
    while stack:
        next, parent = stack.pop()
        for node in next:
            tree[node].remove(parent)
            stack.append((tree[node], node))

    # next = tree[1]
    # tree = find_parent(tree, next, 1)

    parents = [0] * (n + 1)
    for parent in range(1, n + 1, 1):
        for child in tree[parent]:
            parents[child] = parent

    for parent in parents[2:]:
        print(parent)