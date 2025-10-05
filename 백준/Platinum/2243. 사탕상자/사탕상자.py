class SegmentTree:
    MAX_LEN: int = 10 ** 6
    tree_size: int = MAX_LEN * 4

    def __init__(self):
        self._arr = [0] + [0] * self.MAX_LEN # 1-based
        self._segment_tree = [0] * self.tree_size
        self.n = self.MAX_LEN + 1

    def _update_recursive(
        self,
        arr_left: int, arr_right: int, tree_idx: int,
        update_idx: int, update_value: int
    ):
        # Out of the index range
        if not (arr_left <= update_idx <= arr_right):
            return
        
        # Add (or subtract) candies
        self._segment_tree[tree_idx] += update_value

        # leaf node
        if arr_left == arr_right:
            return 
        
        mid = (arr_left + arr_right) // 2
        if update_idx <= mid:
            # Target index is at the left sub-tree
            self._update_recursive(
                arr_left, mid, tree_idx * 2,
                update_idx, update_value
            )
        else:
            # Target index is at the right sub-tree
            self._update_recursive(
                mid + 1, arr_right, tree_idx * 2 + 1,
                update_idx, update_value
            )

    def _query_recursive(
        self,
        arr_left: int, arr_right: int, tree_idx: int,
        query_num: int
    ):        
        # leaf node
        if arr_left == arr_right:
            return arr_left
        
        mid = (arr_left + arr_right) // 2
        if query_num <= self._segment_tree[tree_idx * 2]:
            # Target rank is at the left sub-tree
            # target rank <= amount of candies at the left
            return self._query_recursive(
                arr_left, mid, tree_idx * 2,
                query_num
            )
        else:
            # Target rank is at the right sub-tree
            return self._query_recursive(
                mid + 1, arr_right, tree_idx * 2 + 1,
                query_num - self._segment_tree[tree_idx * 2]
            )

    def update(self, candy_value: int, amount: int):
        self._update_recursive(
            arr_left=1, arr_right=self.n, tree_idx=1,
            update_idx=candy_value, update_value=amount
        )

    def query(self, rank: int) -> int:
        value = self._query_recursive(
            arr_left=1, arr_right=self.n, tree_idx=1,
            query_num=rank
        )
        self.update(candy_value=value, amount=-1)

        return value


if __name__ == "__main__":
    import sys; input = sys.stdin.readline

    n = int(input()) # n : [1, 100_000]
    operations = [tuple(map(int, input().split())) for _ in range(n)]

    tree = SegmentTree()
    for op in operations:
        if len(op) == 2:
            # pop b-th candy from the box
            b = op[1]
            # print the value(flavor) of the candy
            print(tree.query(b))
        else:
            # put candy to the box
            # b - value(flavor) of candy / c - amount of the candy
            b, c = op[1], op[2]
            tree.update(b, c)