from typing import List
from math import ceil, log

class SegmentTree:
    """
    A Segment Tree class using 1-based indexing.
    Supports range sum queries and point updates.
    """
    def __init__(self, arr: List[int]):
        """Initializes the SegmentTree.

        Args:
            arr (List[int]): The initial list of numbers (0-based).
        """
        self.n = len(arr)
        self._arr = [0] + arr

        self.tree_size = self.n * 4
        self._segment_tree = [0] * self.tree_size
        
        self.build()
    
    def __get__(self):
        return self._segment_tree

    def _build_recursive(self, left: int, right: int, i: int):
        """Recursively constructs the segment tree.

        Args:
            left (int): The starting index of the array segment (1-based).
            right (int): The ending index of the array segment (1-based).
            i (int): The index of the current node in the segment tree.
        """
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
        """Recursively updates the tree nodes affected by a value change.

        Args:
            start (int): The starting index of the range for the current node.
            end (int): The ending index of the range for the current node.
            node_index (int): The index of the current node.
            update_idx (int): The 1-based index in the original array that was updated.
            update_diff (int): The difference (new_value - old_value) to propagate.
        """
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
        """Recursively queries the sum of a given range.

        Args:
            start (int): The starting index of the range for the current node.
            end (int): The ending index of the range for the current node.
            i (int): The index of the current node.
            query_left (int): The starting index of the query range.
            query_right (int): The ending index of the query range.

        Returns:
            int: The sum of the elements within the queried range.
        """
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
        """Updates the value at a specific index and propagates the change.

        Args:
            index (int): The 1-based index of the element to update.
            value (int): The new value for the element.
        
        Raises:
            IndexError: If the index is out of the valid 1-based bounds.
        """
        if not (1 <= index <= self.n):
            raise IndexError("Index out of bounds.")
        
        diff = value - self._arr[index]
        self._arr[index] = value

        self._update_recursive(1, self.n, 1, index, diff)
    
    def query(self, left, right):
        """Queries the sum of the elements in a given range [left, right].

        Args:
            left (int): The starting index of the query range (1-based).
            right (int): The ending index of the query range (1-based).

        Returns:
            int: The sum of the specified range.

        Raises:
            IndexError: If the query range is invalid.
        """
        if not (1 <= left <= right <= self.n):
            raise IndexError("Query range is invalid.")
        return self._query_recursive(1, self.n, 1, left, right)

if __name__ == "__main__":
    import sys; input = sys.stdin.readline

    n, m, k = map(int, input().split())
    arr = [int(input()) for _ in range(n)]
    operations = [tuple(map(int, input().split())) for _ in range(m + k)]
    """
    operations
    [(a, b, c), ...]
    a == 1 -> update b-th element as c
    a == 2 -> print sum of a[b:c + 1]
    """

    segment_tree = SegmentTree(arr)

    for a, b, c in operations:
        if a == 1:
            segment_tree.update(b, c)
        elif a == 2:
            range_sum = segment_tree.query(b, c)
            print(range_sum)