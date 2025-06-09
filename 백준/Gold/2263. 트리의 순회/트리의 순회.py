import sys
sys.setrecursionlimit(10 ** 9)

def find_preorder(start_in, end_in, start_post, end_post):
    if start_in > end_in or start_post > end_post:
        return None

    root = postorder[end_post]

    left = idx[root] - start_in
    right = end_in - idx[root]

    print(root, end=' ')

    find_preorder(start_in, start_in + left - 1, start_post, start_post + left - 1)
    find_preorder(end_in - right + 1, end_in, end_post - right, end_post - 1)

    return None


if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    inorder = [*map(int, input().split(' '))]
    postorder = [*map(int, input().split(' '))]
    idx = [0] * (n + 1)
    for i in range(n):
        idx[inorder[i]] = i
    
    find_preorder(0, n - 1, 0, n - 1)