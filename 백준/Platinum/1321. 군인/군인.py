from typing import List

class SegmentTree:
    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self._arr = [0] + arr

        self.tree_size = self.n * 4
        self._segment_tree = [0] * self.tree_size
        
        self.build()
    
    def __get__(self):
        return self._segment_tree

    def _build_recursive(self, left: int, right: int, i: int):
        # leaf node
        if left == right:
            self._segment_tree[i] = self._arr[left]
            return
        
        mid = (left + right) // 2
        left_child_index = i * 2
        right_child_index = i * 2 + 1
        
        self._build_recursive(left, mid, left_child_index)
        self._build_recursive(mid + 1, right, right_child_index)
        self._segment_tree[i] = (
            self._segment_tree[left_child_index]
            + self._segment_tree[right_child_index]
        )

    def _update_recursive(
        self,
        start: int, end: int, i: int,
        update_index: int, update_diff: int
    ):
        if not (start <= update_index <= end):
            return
        
        self._segment_tree[i] += update_diff
        if start != end:
            mid = (start + end) // 2
            self._update_recursive(
                start, mid, i * 2,
                update_index, update_diff
            )
            self._update_recursive(
                mid + 1, end, i * 2 + 1,
                update_index, update_diff
            )

    def _query_recursive(
        self,
        start: int, end: int, i: int,
        query_num: int
    ):
        if start == end:
            return start
        
        mid = (start + end) // 2
        left_child_index = i * 2
        left_result = self._segment_tree[left_child_index]

        if query_num <= left_result:
            return self._query_recursive(
                start, mid, left_child_index,
                query_num
            )
        else:
            right_child_index = left_child_index + 1
            return self._query_recursive(
                mid + 1, end, right_child_index,
                query_num - left_result
            )


    def build(self):
        self._build_recursive(1, self.n, 1)

    def update(self, index: int, delta: int):
        self._arr[index] += delta
        self._update_recursive(1, self.n, 1, index, delta)
    
    def query(self, soldier_num: int):
        return self._query_recursive(1, self.n, 1, soldier_num)

if __name__ == "__main__":
    import sys; input = sys.stdin.readline

    n = int(input())
    arr = [*map(int, input().split())]
    m = int(input())
    operations = [tuple(map(int, input().split())) for _ in range(m)]

    segment_tree = SegmentTree(arr)

    for op in operations:
        if len(op) == 3:
            segment_tree.update(op[1], op[2])
        else:
            print(segment_tree.query(op[1]))