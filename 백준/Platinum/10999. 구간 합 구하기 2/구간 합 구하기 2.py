class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self._arr = [0] + arr
        self.tree_size = 4 * self.n
        self._segment_tree = [0] * self.tree_size
        self._lazy = [0] * self.tree_size
    
        self._build()

    def _build_recursive(self, arr_left, arr_right, tree_idx):
        if arr_left == arr_right:
            self._segment_tree[tree_idx] = self._arr[arr_left]
            return
        
        mid = (arr_left + arr_right) // 2
        lchd_idx = tree_idx * 2
        rchd_idx = tree_idx * 2 + 1

        self._build_recursive(arr_left, mid, lchd_idx)
        self._build_recursive(mid + 1, arr_right, rchd_idx)

        self._segment_tree[tree_idx] = (
            self._segment_tree[lchd_idx]
            + self._segment_tree[rchd_idx]
        )

    def _propagate(self, tree_left, tree_right, tree_idx):
        if self._lazy[tree_idx] != 0:
            self._segment_tree[tree_idx] += (
                (tree_right - tree_left + 1) * self._lazy[tree_idx]
            )
            if tree_left != tree_right:
                self._lazy[2 * tree_idx] += self._lazy[tree_idx]
                self._lazy[2 * tree_idx + 1] += self._lazy[tree_idx]
            self._lazy[tree_idx] = 0

    def _update_range(
        self,
        tree_left, tree_right, tree_idx, 
        arr_left, arr_right, diff
    ):
        self._propagate(tree_left, tree_right, tree_idx)

        if tree_right < arr_left or arr_right < tree_left:
            return

        if arr_left <= tree_left and tree_right <= arr_right:
            self._segment_tree[tree_idx] += (tree_right - tree_left + 1) * diff
            if tree_left != tree_right:
                self._lazy[2 * tree_idx] += diff
                self._lazy[2 * tree_idx + 1] += diff
            return

        mid = (tree_left + tree_right) // 2
        self._update_range(
            tree_left, mid, 2 * tree_idx,
            arr_left, arr_right, diff
        )
        self._update_range(
            mid + 1, tree_right, 2 * tree_idx + 1,
            arr_left, arr_right, diff
        )
        self._segment_tree[tree_idx] = (
            self._segment_tree[2 * tree_idx]
            + self._segment_tree[2 * tree_idx + 1]
        )
    
    def _query(
        self,
        arr_left, arr_right, tree_idx,
        query_left, query_right
    ):
        self._propagate(arr_left, arr_right, tree_idx)

        if arr_right < query_left or query_right < arr_left:
            return 0
        
        if query_left <= arr_left and arr_right <= query_right:
            return self._segment_tree[tree_idx]
        
        mid = (arr_left + arr_right) // 2
        left_sum = self._query(
            arr_left, mid, tree_idx * 2,
            query_left, query_right
        )
        right_sum = self._query(
            mid + 1, arr_right, tree_idx * 2 + 1,
            query_left, query_right
        )
        return left_sum + right_sum

    def _build(self):
        self._build_recursive(1, self.n, 1)

    def update(self, start, end, value):
        self._update_range(1, self.n, 1, start, end, value)

    def query(self, start, end):
        return self._query(1, self.n, 1, start, end)


if __name__ == "__main__":
    import sys; input = sys.stdin.readline

    n, m, k = map(int, input().split())
    arr = [int(input()) for _ in range(n)]
    operations = [tuple(map(int, input().split())) for _ in range(m + k)]

    tree = SegmentTree(arr)
    for op in operations:
        if op[0] == 1:
            # update arr - add d to all elements from b-th to c-th index
            # 1, b, c, d
            _, b, c, d = op
            tree.update(b, c, d)
        else:
            # query the range sum from b-th index to c-th index
            # 2, b, c 
            _, b, c = op
            print(tree.query(b, c))