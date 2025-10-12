class SegmentTree:
    MAX_LEN = 200_001
    tree_size = 4 * MAX_LEN

    def __init__(self):
        self._segment_tree = [[0, 0] for _ in range(self.tree_size)]
        self.n = self.MAX_LEN - 1

    def _update(
        self,
        tree_left, tree_right, tree_idx,
        index, value
    ):
        if tree_left == tree_right:
            self._segment_tree[tree_idx][0] += 1
            self._segment_tree[tree_idx][1] += value
            return
        
        
        mid = (tree_left + tree_right) // 2
        if index <= mid:
            self._update(tree_left, mid, tree_idx * 2, index, value)
        else:
            self._update(mid + 1, tree_right, tree_idx * 2 + 1, index, value)
        
        self._segment_tree[tree_idx][0] = (
            self._segment_tree[tree_idx * 2][0]
            + self._segment_tree[tree_idx * 2 + 1][0]
        )
        self._segment_tree[tree_idx][1] = (
            self._segment_tree[tree_idx * 2][1]
            + self._segment_tree[tree_idx * 2 + 1][1]
        )
    
    def _query(
        self,
        tree_left, tree_right, tree_idx,
        left, right
    ):
        if right < tree_left or tree_right < left:
            return [0, 0]
        
        if left <= tree_left and tree_right <= right:
            return self._segment_tree[tree_idx]
        
        mid = (tree_left + tree_right) // 2
        res_left = self._query(tree_left, mid, tree_idx * 2, left, right)
        res_right = self._query(mid + 1, tree_right, tree_idx * 2 + 1, left, right)
        
        return [res_left[0] + res_right[0], res_left[1] + res_right[1]]

    def update(self, index, value):
        self._update(0, self.n, 1, index, value)

    def query(self, left, right):
        if left > right:
            return [0, 0]
        return self._query(0, self.n, 1, left, right)

if __name__ == "__main__":
    import sys; input = sys.stdin.readline

    n = int(input())
    trees = [int(input()) for _ in range(n)]

    segment_tree = SegmentTree()
    segment_tree.update(trees[0], trees[0])

    total_product = 1
    total_sum_of_coords = trees[0]
    num_planted_trees = 1
    MOD = 10 ** 9 + 7

    for pos in trees[1:]:
        num_left, sum_left = segment_tree.query(0, pos)
        
        num_right = num_planted_trees - num_left
        sum_right = total_sum_of_coords - sum_left

        cost_left = (num_left * pos) - sum_left
        cost_right = sum_right - (num_right * pos)
        current_cost = cost_left + cost_right

        total_product = (total_product * current_cost) % MOD

        segment_tree.update(pos, pos)
        num_planted_trees += 1
        total_sum_of_coords += pos

    print(total_product)