from typing import List


class SegmentTree:
    def __init__(self, arr: List[int], MOD: int):
        self.n = len(arr)
        self._arr = [0] + arr
        self.MOD = MOD

        self.tree_size = self.n * 4
        self._segment_tree = [0] * self.tree_size

        self._build()

    def _build_recursive(self, arr_left: int, arr_right: int, tree_idx: int):
        # leaf node
        if arr_left == arr_right:
            self._segment_tree[tree_idx] = self._arr[arr_left]
            return
        
        # Calc child node index of tree
        arr_mid = (arr_left + arr_right) // 2
        left_child_idx = tree_idx * 2
        right_child_idx = tree_idx * 2 + 1

        # Recursively call build child tree
        self._build_recursive(arr_left, arr_mid, left_child_idx)
        self._build_recursive(arr_mid + 1, arr_right, right_child_idx)

        # Assign value to the current node(index)
        self._segment_tree[tree_idx] = (
            self._segment_tree[left_child_idx]
            * self._segment_tree[right_child_idx]
        ) % self.MOD

    def _update_recursive(
        self,
        tree_start: int, tree_end: int, tree_idx: int,
        arr_idx: int, update_value: int
    ):
        # Out of update path(index range)
        if not (tree_start <= arr_idx <= tree_end):
            return
        
        # leaf node -> update value
        if tree_start == tree_end:
            self._segment_tree[tree_idx] = update_value
            return
        
        # Calc child node index of tree
        tree_mid = (tree_start + tree_end) // 2
        left_child_idx = tree_idx * 2
        right_child_idx = tree_idx * 2 + 1

        # Recursively update value of child tree
        self._update_recursive(
            tree_start, tree_mid, tree_idx * 2,
            arr_idx, update_value
        )
        self._update_recursive(
            tree_mid + 1, tree_end, tree_idx * 2 + 1,
            arr_idx, update_value
        )

        # Update value of the current node(index)
        self._segment_tree[tree_idx] = (
            self._segment_tree[left_child_idx]
            * self._segment_tree[right_child_idx]
        ) % self.MOD

    def _query_recursive(
        self,
        tree_start: int, tree_end: int, tree_idx: int,
        query_left: int, query_right: int
    ) -> int:
        # Out of path
        if tree_end < query_left or query_right < tree_start:
            return 1
        
        if query_left <= tree_start and tree_end <= query_right:
            return self._segment_tree[tree_idx]
        
        mid = (tree_start + tree_end) // 2
        left_result = self._query_recursive(
            tree_start, mid, tree_idx * 2,
            query_left, query_right
        )
        right_result = self._query_recursive(
            mid + 1, tree_end, tree_idx * 2 + 1,
            query_left, query_right
        )
        
        return (left_result * right_result) % self.MOD

    def _build(self):
        self._build_recursive(
            arr_left=1,
            arr_right=self.n,
            tree_idx=1
        )

    def update(self, arr_index: int, value: int):
        self._update_recursive(
            tree_start=1, tree_end=self.n, tree_idx=1,
            arr_idx=arr_index, update_value=value
        )
        self._arr[arr_index] = value

    def query(self, query_left: int, query_right: int) -> int:
        return self._query_recursive(
            tree_start=1, tree_end=self.n, tree_idx=1,
            query_left=query_left, query_right=query_right
        )


if __name__ == "__main__":
    import sys; input = sys.stdin.readline

    MOD = 10 ** 9 + 7
    n, m, k = map(int, input().split())
    arr = [int(input()) for _ in range(n)]
    operations = [tuple(map(int, input().split())) for _ in range(m + k)]

    segment_tree = SegmentTree(arr, MOD)
    for a, b, c in operations:
        match a:
            case 1:
                segment_tree.update(b, c)
            case 2:
                print(segment_tree.query(b, c))