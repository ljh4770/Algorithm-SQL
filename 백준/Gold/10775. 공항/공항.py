def find_set(x):
    if x != parents[x]:
        # Path Compression
        parents[x] = find_set(parents[x])
    return parents[x]

def union(a, b):
    rootA = find_set(a)
    rootB = find_set(b)

    parents[rootA] = rootB

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    g = int(input())
    p = int(input())
    planes = [int(input()) for _ in range(p)]

    # Each element denote the gate number the index plane can use
    parents = [i for i in range(g + 1)]

    cnt = 0 # Count of planes docked
    for num in planes:
        root = find_set(num)
        if root == 0:
            break

        union(root, root - 1)
        cnt += 1

    print(cnt)