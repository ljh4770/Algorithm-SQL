class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self._arr = [0] + arr

        self.tree_size = self.n * 4
        self._segment_tree = [0] * self.tree_size
        
        self.build()

    def _build_recursive(self, left, right, i):
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
        start, end, i,
        update_index, update_diff
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
        start, end, i,
        query_left, query_right
    ):
        if end < query_left or start > query_right:
            return 0
        
        if query_left <= start and end <= query_right:
            return self._segment_tree[i]
        
        mid = (start + end) // 2
        left_sum = self._query_recursive(
            start, mid, i * 2,
            query_left, query_right
        )
        right_sum = self._query_recursive(
            mid + 1, end, i * 2 + 1,
            query_left, query_right
        )
        return left_sum + right_sum

    def build(self):
        self._build_recursive(1, self.n, 1)

    def update(self, index, value):
        diff = value - self._arr[index]
        self._arr[index] = value

        self._update_recursive(1, self.n, 1, index, diff)
    
    def query(self, left, right):
        return self._query_recursive(1, self.n, 1, left, right)


if __name__ == "__main__":
    import sys; input = sys.stdin.readline

    n = int(input())
    arr = [*map(int, input().split())]
    m = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(m)]
    updates = [x for x in queries if x[0] == 1]
    range_sums = [x for x in queries if x[0] == 2]

    sum_query_by_k = [[] for _ in range(len(updates) + 1)]
    for idx, query in enumerate(range_sums):
        _, k, i, j = query
        sum_query_by_k[k].append((i, j, idx))
    
    answers = [0] * len(range_sums)
    tree = SegmentTree(arr)

    if sum_query_by_k[0]:
        for i, j, idx in sum_query_by_k[0]:
            answers[idx] = tree.query(i, j)
    

    for k in range(len(updates)):
        _, idx, new_val = updates[k]
        tree.update(idx, new_val)

        update_version = k + 1
        
        if update_version < len(sum_query_by_k):
            for i, j, pos in sum_query_by_k[update_version]:
                answers[pos] = tree.query(i, j)

    for ans in answers:
        print(ans)