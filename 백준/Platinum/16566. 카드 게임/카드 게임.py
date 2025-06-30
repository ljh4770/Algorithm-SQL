def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    parent[find(a)] = find(b)

if __name__ == "__main__":
    import sys; input = sys.stdin.readline
    from bisect import bisect_right

    n, m, k = map(int, input().split(' '))
    nums = [*map(int, input().split(' '))]
    pivots = [*map(int, input().split(' '))]
    parent = [i for i in range(n)]
    nums.sort()
    
    for p in pivots:
        idx = bisect_right(nums, p)
        idx = find(idx)
        union(idx, idx + 1)

        print(nums[idx])